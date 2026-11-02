---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

PASS: Distinctly colored markers a,b∈Q_d at distance t give orbit coordinates (i,j), 0≤i≤t,0≤j≤d-t, with distances p=i+j,q=t-i+j. Reconstructed induction: initial colors are F_1=(min(p,1),min(q,1)); count of neighbors at a marked distance R-1 reveals any new truncation at R+1, while known Hamming neighbor multiplicities i,t-i,j,d-t-j prevent further splits. Thus after r rounds colors are F_{r+1} exactly. The full distance pair is a complete orbit invariant for pointwise stabilizer S_t×S_{d-t}; cell size binom(t,i)binom(d-t,j). Sharp noninjectivity/injectivity thresholds yield d-1 for adjacent, d-2 for 2≤t<d and floor((d-1)/2) for antipodal, with d=1,2 boundary checks. Independently implemented direct synchronous vertex refinement of Q_d for every 1≤d≤6, 1≤t≤d (21 configurations), checking every intermediate partition and stopping depth; matches the theorem. Finite checks do not prove unrestricted d, for which the counting induction does.

## originality

PASS

PASS (qualified): the binary two-distinct-marker clipped-distance refinement filtration and separation-dependent exact first stable rounds are not implied by the inspected general 1-WL and perfect Hamming coloring works, or by different-marker/alphabet analogues; an unindexed general distance-regular marked-pair theorem could cover it.

## value

PASS

PASS: Exact number of synchronous 1-WL iterations after individualizing two vertices is a natural graph-algorithm complexity statistic, with marker distance causing a sharp three-regime speedup. Complete roundwise filtration and orbit census illuminate 1-WL sensitivity to initial colors; not merely a numerical run on one cube.

The dated certificate retains the supplied scientific assessment, sources and limitations.
