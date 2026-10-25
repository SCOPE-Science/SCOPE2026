---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For every integer m>=5 the canonical root-vector symmetric-edge polytope in zero-sum H has polar the unit-edge Lipschitz polytope. Central symmetry centers a global maximal inscribed Euclidean ball and gives r=1/max_{polar}||y||. The published wheel vertex criterion reduces its vertices to cyclic ternary rim potentials x_i∈{-1,0,1}, excluding adjacent opposite signs and cyclic 000. Subtracting the mean of all m+1 potential values (including hub 0) yields N(p,q)=p+q−(p−q)^2/(m+1). If p,q>0, the two sign transitions on a cycle each require a zero, so s=p+q<=m−2. At fixed s the squared norm is maximized by |p−q|<=1, giving M(s)=s−(s mod 2)/(m+1), strictly increasing with s. Thus m even has max N=m−2 and p=q=(m−2)/2; m odd max N=m−2−1/(m+1) with |p−q|=1. One-sign potentials satisfy N<=floor((m+1)^2/4)/(m+1), strictly smaller: even difference (3m²−6m−8)/(4(m+1))>0 for m>=6, odd difference (3m²−6m−13)/(4(m+1))>0 for m>=5. Equality forces exactly two zeros, one plus and one minus block; all such extremal words satisfy the facet criterion. Counting cyclic rotations and sign reversal gives exactly m tangent facets for even m, 2m for odd m. Inverting sqrt(N) yields the claimed radii and dividing N by m+1 gives the exact spread. The small m=3,4 cases are excluded. The independent exact arithmetic enumeration for m=5..12 reconstructed polar vertices by tight-edge connectivity and independently verified all maxima and maximizer counts, not substituted for the general symbolic proof.

## originality

PASS

Best-of-knowledge original exact metric evaluation: the primary wheel facet classification supplies the word admissibility but no centered Euclidean norm optimization. Fresh semantic searches and full readings of wheel, spread, extremal Lipschitz and nearest published records identified no theorem implying the even/odd wheel inradius, exact tangent-facet orbit list or equivalent wheel spread. Same-graph Löwner-ellipsoid work concerns a different extremal functional; fan, cycle and multipartite formulas do not subsume W_m for m>=5. No claim of absolute historical priority is made.

## value

PASS

An exact Euclidean inradius is a natural metric invariant of the canonically embedded symmetric-edge polytope of an infinite standard graph family. The wheel family is geometrically nontrivial and is studied for graph root/adjacency polytopes and algebraic graph models. The result simultaneously determines every contact facet of the origin-centered maximal ball and the exact maximum 1-Lipschitz variance (wheel graph spread); the parity change is mathematically structural. A researcher needing sharp support geometry, comparison with family members or a wheel-spread benchmark can use the precise formula. This is neither a merely finite check nor a known table copied from the general wheel facet classification; the proof includes a real metric maximization and full equality classification. It does not imply analogous radii under affine changes or beyond wheels.

The dated certificate retains the supplied scientific assessment, sources and limitations.
