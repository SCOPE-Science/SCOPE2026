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
# Verifiable proof dependencies and boundaries

The analytic argument relies on a complete \(2d-1\)-point Fourier inversion of \(|P'|^2\), exact reciprocal-root factorization of the resulting polynomial, absence of aliases in the constant and first Fourier coefficients of \(|P|^2\) when \(d\ge3\), and a nonzero coefficient of \(|c_0|^2\) in each wrong-branch constraint. The zero-flip condition excludes only a real-null set in derivative coefficient space; a finite circle union excludes a null set of integration constants for each good derivative. Tonelli–Fubini promotes this to a full-measure statement in all coefficient variables.

To independently reproduce the finite witnesses, install SymPy with Python 3 and run `python scripts/check.py`. It performs exact Gaussian-rational arithmetic for five degrees and checks every wrong zero-flip branch at each tested degree. Output must exactly match `scripts/check_output.txt`.

Finite witnesses are not proof of all degrees. No numeric error analysis, universal uniqueness, minimum sample count, or classification of nongeneric fibers is claimed. External independent audit has not been performed.
