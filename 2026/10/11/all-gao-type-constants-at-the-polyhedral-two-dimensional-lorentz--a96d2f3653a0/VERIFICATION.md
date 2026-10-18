---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The stated N_w has an octagonal unit ball with exactly eight facet normals (±1,±w),(±w,±1) and dual norm max(|a|,|b|,(|a|+|b|)/(1+w)). For unit x,y set u=(x+y)/2,v=(x−y)/2. Selecting their active facets, isometry fixes the first one; exhaustive eight relative facets yield coefficient pairs (1,0),(1,δ),(k,k),(w,1),(0,1),(δ,1),(k,k),(1,w), δ=(1−w)/(1+w), k=max{(1+w)/2,1/(1+w)}. Hölder applied to αN(u)+βN(v)≥1 gives lower bound (α^{p′}+β^{p′})^{1−p}; only A=(1+δ^{p′})^{1−p}, B=(1+w^{p′})^{1−p}, and C=2^{1−p}k^{−p} can dominate. Convexity gives C≥min(A,B). δ=w exactly at w=√2−1; hence formula branches and p-independent boundary. The explicit coordinate-swapped and sign-reflected unit pairs meet equality in their respective regimes, with endpoints 0<w<1 and every p>1. For p=1 triangle inequality plus x=y gives c=1. p=2 reduces to already known quadratic Gao formula.

## originality

PASS

The classical quadratic Gao constant p=2 at this polyhedral Lorentz endpoint was already computed in the 2026-10-04 published finding; the present distinct mathematical statement is its *entire p>1 generalized Gao-type profile* with the same sharp w transition. The 2022 primary article computed Lorentz only at ambient exponent r≥2 and explicitly listed 1≤r<2 as open.

## value

PASS

A natural one-parameter family of polyhedral Lorentz normed planes has an exact generalized Gao-type invariant for every exponent, with an explicit p-independent phase transition and optimized unit-vector pairs. It fills the endpoint of a range explicitly identified as open in the motivating primary literature; not merely a re-evaluation of the known p=2 case. It is a meaningful complete invariant for this natural Banach-plane family, without requiring an unrelated global application.

The dated certificate retains the supplied scientific assessment, sources and limitations.
