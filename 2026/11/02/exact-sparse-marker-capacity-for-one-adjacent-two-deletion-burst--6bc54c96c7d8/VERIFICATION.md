---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Input is weight-two binary words length n≥2 and exactly two consecutive deletions. Nonadjacent ones (i,j), gap≥2, map bijectively to marker edge {i,j−2} on m=n−2 vertices (loops allowed). Each such word produces weight-one outputs at both endpoints, so selected marker edges are vertex-disjoint; loops at positions distance two share a weight-two output. Loop bound is alpha_m=ceil(ceil(m/2)/2)+ceil(floor(m/2)/2); with l loops,e ordinary edges, l+2e≤m, hence l+e≤f(m)=3 floor(m/4)+min(m mod4,2). At most one adjacent-ones word, because adjacent parents all have zero output. Interior adjacent consumes two markers; a boundary adjacent consumes one and leaves f(m−1) nonadjacent slots, giving upper 1+f(m−1)=floor(3(n−1)/4). A closed 4-periodic family with boundary adjacent (0,1), two local loops plus a disjoint ordinary edge per marker block and at most two tail loops achieves the bound, with no shared weight-one or translated-by-two weight-two outputs. n=2 singleton. The proof explicitly handles the exact-burst, not arbitrary two-deletion channel.

## originality

PASS

Best-of-knowledge originality is a statement/implication comparison, not a title-match test. The exact established object, parameters, finite tables and known stronger results were cross-checked against published Resultary findings and primary literature; no decisive prior coverage of the final claim was established. Highly plausible inaccessible sources and indirect possible corollaries are disclosed in residual_risks. Searches alone are not novel proof.

## value

PASS

A natural constant-composition synchronization channel has an exact all-length zero-error packing number, with a genuinely structural marker matching and congruence-four construction. This is useful when sparse event markers, not arbitrary binary inputs, are constrained; it does not depend on a paper-sized larger theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
