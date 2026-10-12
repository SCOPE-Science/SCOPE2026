from __future__ import annotations
import cmath


def source_formula_normalized(d: int) -> float:
    return (d + 1.0) / (d * (d + 1.0))


def source_formula_unnormalized(d: int) -> float:
    return (d + float(d * d)) / (d * (d + 1.0))


def true_unitary_average_fidelity(d: int, trace_u: complex) -> float:
    return (abs(trace_u) ** 2 + d) / (d * (d + 1.0))


for d in range(2, 13):
    omega = cmath.exp(2j * cmath.pi / d)
    trace_traceless = sum(omega ** j for j in range(d))
    assert abs(trace_traceless) < 1e-9
    f_identity = true_unitary_average_fidelity(d, complex(d, 0.0))
    f_traceless = true_unitary_average_fidelity(d, trace_traceless)
    assert abs(f_identity - 1.0) < 1e-12
    assert abs(f_traceless - 1.0 / (d + 1.0)) < 1e-12
    assert abs(source_formula_normalized(d) - 1.0 / d) < 1e-12
    assert abs(source_formula_unnormalized(d) - 1.0) < 1e-12
    assert abs(source_formula_normalized(d) - f_identity) > 1e-6
    assert abs(source_formula_unnormalized(d) - f_traceless) > 1e-6

print("VERIFY_OK")
