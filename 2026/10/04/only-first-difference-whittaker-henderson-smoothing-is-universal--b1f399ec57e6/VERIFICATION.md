---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For \(p=1\), \(I+\lambda D_1^{\mathsf T}D_1\) is an irreducible nonsingular M-matrix; its inverse is strictly positive, and annihilation of constants gives unit row sums, hence strict convex-combination range preservation. For \(p\ge2\) at \(n=p+1\), \(D_p\) is one binomial row \(d\) and Sherman--Morrison gives \(S=I-\alpha d^{\mathsf T}d\), \(\alpha=\lambda/(1+\lambda\binom{2p}{p})\). Applying it to the final unit vector makes coordinate \(p-2\) equal \(-\alpha\binom p2<0\). Adding a sufficiently small positive affine sequence preserves this negative output because \(D_p\) annihilates affine data. The finite verifier was read and is consistent with, but not needed for, this analytic proof.

## originality

PASS

Best-of-knowledge originality passes for the all-order range-preservation dichotomy. The author-uploaded full text of Yamada--Tuj Jahra was read: it derives order-one smoother weights and records unit row sums, while the order-two/HP literature supplies exact weights and known sign-changing phenomena. Neither source states that order one is the unique universally range-preserving difference order or gives the uniform minimal-length counterexample for every higher order. Fresh Resultary search returned no implication-equivalent theorem.

## value

PASS

Universal range preservation is a natural qualitative safety property of a linear smoother. The theorem gives a sharp all-order boundary, a minimal-sample obstruction for every higher order, and a robust strictly increasing positive witness; this is more informative than isolated negative HP weights and can guide whether unconstrained smoothing can overshoot.

The dated certificate retains the supplied scientific assessment, sources and limitations.
