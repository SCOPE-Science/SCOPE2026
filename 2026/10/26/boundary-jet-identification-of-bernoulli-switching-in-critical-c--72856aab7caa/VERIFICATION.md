---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The exact inverse branches c±u(z)^2 have u(z)^2=O(z^2) and transfer weight 2w(z)=z/K^2-3theta z^2/(4K^4)+5theta^2 z^3/(8K^6)+O(z^4). W2,1 embeds in C1; symmetric evaluations h(c±u^2)=2h(c)+o(u^2) justify o(z^3) without C3. The invariant density is positive at cusp: a zero would propagate under both inverse branches of the p<1 theta0 map, dense by uniformly contracting full branches, contradicting normalization. Therefore alpha=(h(c) A,-3h(c)B/4,5h(c)C/8) with two-point mixture A,B,C; weighted mean B/A recovers p and AC−B²=p(1-p)a0a1(r1−r0)² yields the sharp 45/8 discriminator. Primary Theorem 6.1 confirms stationary W2,1 premise. Independent symbolic series/variance and inverse checks passed.

## originality

PASS

Best-of-knowledge originality PASS for the exact final theorem, not for foundational known ingredients; source and implication comparisons are below, with named residual risks. Analytic response/spectral gap is about existence and perturbative dependence; it does not by itself identify unknown p exactly via second boundary coefficient or force a third-order variance sign. The result uses prior existence as its premise. One must use even cancellation in W2,1 to obtain an actual o(z³) Peano jet, prove cusp positivity, and compute the nontrivial mixture moment inversion; these are not conclusions of the cited existence theorem alone.

## value

PASS

Identifying an unknown Bernoulli mixing probability from local stationary boundary shape without the unknown cusp-density normalization is a natural inverse problem in a well-defined random dynamical family. The third-jet strict variance witness distinguishes genuine switching from a deterministic map with no arbitrary numerical threshold; regularity is handled precisely.

The dated certificate retains the supplied scientific assessment, sources and limitations.
