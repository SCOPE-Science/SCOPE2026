---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For any prime power q and n>=2, count nonzero rank-one square-zero X,Y with X+Y=B, ordered. Rank>=3 or tr B!=0 impossible; B=0 count |C|=(q^n-1)(q^(n-1)-1)/(q-1). Rank-one B is the exhaustive common-image/common-row dichotomy; each branch q^(n-1)-2, overlap q-2, yielding 2q^(n-1)-q-2. Rank-two B: identify rank-one projection P on E=V/ker B and impose lambda(v)=1,lambda((pi L)v)=0. For each eigenline of S=pi L, nonzero eigenvalue yields none, eigenvalue zero yields q, and non-eigenlines yield one; gives q e0(T)+q+1-e(T) including characteristic 2. Independent complete q=2,3 n=2 full-target matrix enumeration matches; general proof does not rely on finite tests.

## originality

PASS

Best-of-knowledge statement/implication-level comparison for Exact fibers of sums of two rank-one square-zero matrices over finite fields: precise new invariant not located as prior theorem; accessible direct sources and nearest indexed records compared, with explicit access and alias risks. A failed index search alone does not establish originality.

## value

PASS

Targetwise additive convolution coefficients of the nonzero minimal nilpotent orbit for ALL finite fields and dimensions are natural representation counts, refining mere feasibility and exposing e0/eigenline dependence including characteristic-two exceptional nonrepresentability. A mathematician studying nilpotent-orbit convolution or fixed-rank decompositions needs this precise multiplicity, not merely existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
