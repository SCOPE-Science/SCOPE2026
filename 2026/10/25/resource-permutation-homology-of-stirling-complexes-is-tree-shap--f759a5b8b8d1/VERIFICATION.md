---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For any m-vertex tree m>=2 and n resource coordinates n>=m, cube condition each vertex appears literally among n entries. A permutation with c cycles fixes cell tuples constant on each cycle; for j edge cycles orientation contributes (-1)^(sum_lengths-j) and alternating cell degree multiplies to (-1)^j. Exact cellular Lefschetz formula L=Σ_j(-1)^j C(c,j)(m-1)^j Surj(c-j,m)=Σ_h(-1)^h C(m,h)(1-h)^c. Kozlov sphere-wedge theorem confines reduced homology to n-m, with dimension F_m(n). Thus trace =sgn(σ)F_m(c(σ)). The averaged signed cycle count is a falling factorial a(a-1)...(a-n+1)=0 for all a∈[1,m-1], proving rational quotient acyclicity even at n=m (discrete m! points). Independent direct oriented cubical-cell enumeration checked all permutations for six small parameter pairs up through (4,4), with complete symbolic all-parameter proof.

## originality

PASS

Kozlov 2022/2023 provides the same cubical construction, shape-independent nonequivariant sphere-wedge rank and a different open question on permutations of star leaves. It does not supply the coordinate-resource S_n character or resource-unlabeled quotient rational homology in the inspected full-text sections. Other Resultary character results concern other complexes or tree-automorphism groups. Best-of-knowledge original refinement of an established family.

## value

PASS

Natural full resource permutation character and rational quotient calculation for an entire infinite family, showing the striking tree-shape independence persists at the representation level while all nonzero reduced homology disappears under unlabeled resource quotient. These invariants are not implied by the known rank F_m(n), although the proof uses standard signed Lefschetz methods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
