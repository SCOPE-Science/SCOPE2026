---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

PASS. At the pinned RESULT.md, write each projection as Bx+V with B=I-uu^T, V=b_Iu/||a_I||, BV=0. Independent Gaussian radial densities have r^(d-1) positive near zero; on sectors s=max_j r_j the singular radial exponent is md-q-1 and angular chosen-radius exponent d+beta-q-1, so E||V||^q finite iff q<min(md,d+beta), equality logarithmically divergent. Independence gives finite/infinite iterate moments at every positive time. Full-support selected directions make E||Bv||^q/||v||^q<1 uniformly on the sphere (d>=2), giving an invariant law and matching moment bounds; d=1 refreshes every step. For centered beta=2, Gamma/Dirichlet decomposition yields exact q-moment ratio and the second-moment recurrence with factor 1-1/d; limiting cases m=1, d=1, beta=0 are handled by these formulas. Finite numerical tests are not substituted for the general proof.

## originality

PASS

PASS (best of knowledge). The claim concerns refreshed independent Gaussian candidate observations and exact unconditional moment integrability, distinct from the fixed noisy-matrix and fixed-system prior results; the general gamma/Dirichlet facts are not claimed as new. No equivalent all-q result found in actual semantic and primary-paper comparisons.

## value

PASS

PASS. Sharp, natural all-order heavy-tail cutoffs and invariant-state moment classification explain when norm-squared sampling removes infinite variance in an online noisy projection method; the simultaneous-origin md obstruction is structurally relevant, and the closed Gaussian moment/equilibrium floor is not an arbitrary narrow instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
