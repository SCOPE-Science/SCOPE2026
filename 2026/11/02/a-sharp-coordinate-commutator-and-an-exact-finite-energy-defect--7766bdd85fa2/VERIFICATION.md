---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The Gaussian quasi-radial indicator E={|z1|>|z2|} is diagonal in orthonormal monomials, with eigenvalues binomial CDF lambda_nm=2^-(n+m+1)sum_{j<=n}binom(n+m+1,j). The multiplication commutator has orthogonal shift images with weights sqrt(n+1)*binom(n+m+1,n+1)/2^(n+m+2), so its bounded extension exists. Maximizing over shell levels for a=n+1 gives sqrt(a)*binom(2a,a)/(2*4^a), strictly increasing to 1/(2sqrt(pi)); every weight strictly smaller, giving norm nonattainment, and weakly-null maximizing basis vectors give equal essential norm. The per-shell trace of T(I-T) is (1/2)E|B-Bprime| for independent Bin(k,1/2), namely k*binom(2k,k)/(2*4^k); induction telescopes all shells to the exact total-degree cutoff formula and Stirling yields N^1.5/(3sqrt(pi)). Independent exact Fraction calculations checked 16 trace cutoffs.

## originality

PASS

Dewage–Ólafsson already establish quasi-radial Fock Toeplitz diagonalization/gamma integrals, so neither that general method nor binomial identities are claimed new. No inspected source supplies the sharp bounded unbounded-coordinate commutator norm/essential norm together with a precise finite-energy nonprojection trace for this bisector cone. Priority qualified against other Gaussian interface literature.

## value

PASS

Two independently natural exact operator invariants of a discontinuous, scale-invariant Fock cone quantify persistent interface effects: a noncompact commutator with nonattained sharp norm, and an every-cutoff trace with N^(3/2) edge growth. They characterize more than mere boundedness or a small finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
