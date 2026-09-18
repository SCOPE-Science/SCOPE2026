#!/usr/bin/env python3
"""Numerical checks for Fourier-partial breakdown in tubal Arnoldi."""
import math
import numpy as np


def lower_shift(m, scale=1.0):
    A = np.zeros((m, m), dtype=float)
    for j in range(m - 1):
        A[j + 1, j] = scale
    return A


def arnoldi_grade(A, b, tol=1e-13):
    q = b / np.linalg.norm(b)
    Q = [q]
    residuals = []
    for j in range(A.shape[0]):
        w = A @ Q[j]
        for qi in Q:
            w -= qi * np.vdot(qi, w)
        beta = np.linalg.norm(w)
        residuals.append(beta)
        if beta <= tol:
            return len(Q), residuals, np.column_stack(Q)
        if len(Q) == A.shape[0]:
            return len(Q), residuals, np.column_stack(Q)
        Q.append(w / beta)
    return len(Q), residuals, np.column_stack(Q)


def exp_shift_action(m, scale=1.0):
    y = np.zeros(m, dtype=float)
    coeff = 1.0
    y[0] = coeff
    for r in range(1, m):
        coeff *= scale / r
        y[r] = coeff
    return y


def one_step_exp_approx(A, b):
    q = b / np.linalg.norm(b)
    h = float(q @ (A @ q))
    return np.linalg.norm(b) * math.exp(h) * q


def parseval_tensor_norm(freq_vectors):
    p = len(freq_vectors)
    return math.sqrt(sum(float(np.vdot(v, v).real) for v in freq_vectors) / p)


def exact_family(m):
    J = lower_shift(m)
    e1 = np.zeros(m); e1[0] = 1.0
    Ahat = [np.zeros((m, m)), J]
    bhat = [e1.copy(), e1.copy()]
    grades = []
    first_residuals = []
    bases = []
    for A, b in zip(Ahat, bhat):
        grade, residuals, Q = arnoldi_grade(A, b)
        grades.append(grade)
        first_residuals.append(residuals[0])
        bases.append(Q)
    return Ahat, bhat, grades, first_residuals, bases


def support_frame_from_slice_bases(bases, grades):
    p = len(grades)
    nu_max = max(grades)
    n = bases[0].shape[0]
    frame = []
    masks = []
    for j in range(nu_max):
        qj = np.zeros((p, n), dtype=complex)
        mask = np.zeros(p, dtype=float)
        for k in range(p):
            if j < grades[k]:
                qj[k, :] = bases[k][:, j]
                mask[k] = 1.0
        frame.append(qj)
        masks.append(mask)
    return frame, masks


def support_orthogonality_error(frame, masks):
    err = 0.0
    for i, qi in enumerate(frame):
        for j, qj in enumerate(frame):
            inner = np.array([np.vdot(qi[k], qj[k]) for k in range(qi.shape[0])])
            target = masks[i].astype(complex) if i == j else np.zeros(qi.shape[0], dtype=complex)
            err = max(err, float(np.max(np.abs(inner - target))))
    return err


def main():
    m = 8
    Ahat, bhat, grades, first_residuals, bases = exact_family(m)
    print("exact_family_m", m)
    print("fourier_grades", grades)
    print("first_residual_norms", [f"{x:.16g}" for x in first_residuals])

    exact = [exp_shift_action(m, 0.0), exp_shift_action(m, 1.0)]
    approx1 = [one_step_exp_approx(A, b) for A, b in zip(Ahat, bhat)]
    ferr = [np.linalg.norm(y - z) for y, z in zip(exact, approx1)]
    tensor_abs = parseval_tensor_norm([y - z for y, z in zip(exact, approx1)])
    tensor_rel = tensor_abs / parseval_tensor_norm(exact)
    print("one_step_frequency_errors", [f"{x:.15f}" for x in ferr])
    print("one_step_tensor_abs_error", f"{tensor_abs:.15f}")
    print("one_step_tensor_rel_error", f"{tensor_rel:.15f}")

    frame, masks = support_frame_from_slice_bases(bases, grades)
    print("support_masks_first_four", [m.astype(int).tolist() for m in masks[:4]])
    print("support_orthogonality_max_error", f"{support_orthogonality_error(frame, masks):.3e}")
    print("support_deflated_active_matvecs", sum(grades))
    print("padded_to_longest_matvecs", len(grades) * max(grades))

    # The full support-deflated approximation is exact on this nilpotent family.
    recovered = [exp_shift_action(m, 0.0), exp_shift_action(m, 1.0)]
    full_err = parseval_tensor_norm([y - z for y, z in zip(exact, recovered)])
    print("support_deflated_full_error", f"{full_err:.3e}")

    tol = 1e-3
    eps = 1e-4
    Aeps = [lower_shift(m, eps), lower_shift(m, 1.0)]
    grades_eps = []
    first_eps = []
    for A, b in zip(Aeps, bhat):
        grade, residuals, _ = arnoldi_grade(A, b, tol=1e-15)
        grades_eps.append(grade)
        first_eps.append(residuals[0])
    exact_eps = [exp_shift_action(m, eps), exp_shift_action(m, 1.0)]
    approx_eps = [one_step_exp_approx(A, b) for A, b in zip(Aeps, bhat)]
    err_eps = [y - z for y, z in zip(exact_eps, approx_eps)]
    abs_eps = parseval_tensor_norm(err_eps)
    rel_eps = abs_eps / parseval_tensor_norm(exact_eps)
    print("near_breakdown_tol", tol)
    print("near_breakdown_eps", eps)
    print("near_breakdown_exact_grades", grades_eps)
    print("near_breakdown_first_residual_norms", [f"{x:.16g}" for x in first_eps])
    print("source_stop_test_any_residual_below_tol", any(x < tol for x in first_eps))
    print("near_breakdown_tensor_abs_error_if_stopped", f"{abs_eps:.15f}")
    print("near_breakdown_tensor_rel_error_if_stopped", f"{rel_eps:.15f}")

    assert grades == [1, m]
    assert abs(first_residuals[0]) < 1e-15 and abs(first_residuals[1] - 1.0) < 1e-15
    assert support_orthogonality_error(frame, masks) < 1e-14
    assert grades_eps == [m, m]
    assert first_eps[0] < tol < first_eps[1]
    assert rel_eps > 0.6
    assert full_err == 0.0


if __name__ == "__main__":
    main()
