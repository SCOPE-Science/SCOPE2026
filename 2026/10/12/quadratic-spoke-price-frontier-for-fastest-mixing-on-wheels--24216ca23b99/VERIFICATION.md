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

# Verification of the wheel spectral-gap theorem

## Analytical certificate

The proof in `RESULT.md` contains the quantified certificate: (i) two Rayleigh-quotient upper bounds valid for all independent nonnegative edge rates, (ii) explicit optimization of their one-dimensional pointwise minimum under the budget, (iii) the complete eigenvalue spectrum of the uniformly weighted wheel, and (iv) an equality/complex-Fourier argument excluding asymmetric optimal allocations. These steps are the evidence for the claimed global and unique or exactly classified optimal weights. The critical price is \(T_n=1/[4\sin^2(\pi/n)]\); it is not inferred from a numerical crossing.

## Finite reproducibility checks

The accompanying `check_wheel.py` is a stand-alone Python 3 program requiring NumPy and SymPy. It builds the full graph Laplacian from individual edge conductances (not the symmetrized quotient alone). Executing `python check_wheel.py` yields:

```text
VERIFY_OK 1246 supplementary finite wheel spectral and Rayleigh checks; analytical argument proves arbitrary size
```

The program checks exact rational eigenvalues for four budget-normalized six-rim instances spanning cheap, critical and expensive spoke-price regimes; exact rational Rayleigh identities for a nonsymmetric four-rim wheel; numerical spectra for eight different rim sizes at five relative prices each; and 1200 budget-feasible independently sampled, asymmetric edge allocations. A fixed pseudo-random seed makes the trials repeatable. The numerical eigenvalue comparisons use explicitly coded tolerances, not exact arithmetic. They cannot establish uniqueness for arbitrary real conductances or the infinite-size result; those rely on the proof.

## Conditions and nonclaims

The graph has one hub, \(n\geq4\) cyclic rim vertices, \(n\) spokes, and \(n\) rims. There is no upper bound on any individual conductance, but conductance cannot be negative. The budget is exact. The generator is \(-L\) with uniform vertex masses; only the second-smallest *Laplacian* eigenvalue is maximized. The critical set contains a continuum of nonnegative allocations but no asymmetric point. At no parameter value are all spokes deleted. No extension to nonuniform stationary probabilities, heterogeneously priced individual edges, or discrete-time SLEM follows automatically.
