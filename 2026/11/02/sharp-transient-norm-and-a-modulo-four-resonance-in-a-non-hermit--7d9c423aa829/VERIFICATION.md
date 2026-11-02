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

# Verification of the transient-gain theorem

The exact proof is supplied in `RESULT.md`. Its critical nonstandard ingredients are the source-specific \(3\times3\) Bloch matrix, chiral reciprocal singular-value argument, explicit Frobenius trace, and strict global optimization over \(s\in[0,1]\) and the cyclic momenta. All are proved there for every allowed parameter, including \(h=0\), \(N=2\), and all boundary time values.

To independently reproduce supporting finite diagnostics, run `python3 verify_gain.py` using the Python standard library. The verifier checks the cubic identity, Frobenius norm identities, exact time-dependent trace, sharp global bound and its attainment, residue-class grid minima, independent power-method estimates of the maximal singular value, and the Hermitian limit. In the current package these checks completed with `PASS: 35620 finite numerical checks`.

Numerical power iteration and finite parameter grids cannot prove a universal theorem. They check implementation against the explicit analytic identities; no formal proof assistant, expert certification, external reproducibility study, or independent scientific audit is claimed.
