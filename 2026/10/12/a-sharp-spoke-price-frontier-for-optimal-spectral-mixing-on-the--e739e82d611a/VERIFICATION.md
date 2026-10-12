---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and verification

## Analytic verification

The universal proof in `RESULT.md` combines price-class averaging, an exact Fourier block decomposition, a monotone scalar first-order condition, and an equality-in-Rayleigh rigidity argument. The characteristic polynomial for uniform class conductances \(u,v\) is
\[
 z(z-2v)\bigl(z^2-(5u+2v)z+5u(u+v)\bigr)^4.
\]
This identity follows for all positive \(u,v\) from the five Fourier modes; it does not require numerical eigenvalue approximation. The resulting frontier is \(t=2/5\). Positivity, boundary equality, and uniqueness among all fifteen arbitrary nonnegative conductances are separately proved there.

## Executable checks

From the directory containing both files, execute `python3 verify.py`. The standard-library portion uses exact rational Faddeev–LeVerrier characteristic-polynomial calculations, checking all ten coefficients at four explicit rational choices and the respective budgets. With NumPy installed, the program also checks all ten Laplacian eigenvalues' spectral-gap consequences at twelve price parameters and compares 720 independently generated feasible nonsymmetric edge allocations. The completed invocation produced:

`VERIFY_OK 4 exact rational 10-by-10 characteristic identities; 12 full spectra, 720 arbitrary feasible allocations`

The code's pseudo-random seed is fixed and its comparisons are reproducible, but sampled allocations cannot establish optimality or uniqueness for all feasible conductances. The analytical proof is needed for universal conclusions. The computation does not establish novelty and is not an independent scientific audit.

## Scope and limitations

Only the Petersen graph with prices \(1,1,t\) on its three natural edge types, unit linear expenditure, and symmetric continuous-time Laplacian is covered. No theorem for arbitrary graphs, directed rates, discrete-time SLEM, alternative cost functions, or incomplete literature coverage is asserted. Independent audit and validation have not been performed.
