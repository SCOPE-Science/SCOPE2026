---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For finite n, summing the column equations x_i+e_i+h_i=y_i+2h_{i+1} leaves s₂(n+t)−s₂(n)=3−Σh_{i+1}, since h₀ and the sufficiently high carry vanish. Four outgoing carries rule out success. If a carry is still outgoing at B+3, where B is the highest one of t, then it had to survive B and the three consecutive zero columns above B. Those four carries are too many, so reading B+4 low digits decides success exactly and gives a natural density by periodicity. The same argument after an internal one followed by three zeros shows that each additional zero before the next one only contributes a free input digit: it cannot change the carry, or the success fraction. This proves each gap clips at 4 for every positive shift in scope, including both gaps unbounded. Leading lower zero digits add no carries, giving c_{2t}=c_t. My replay enumerated prescribed supports of 0–3 outgoing carries (checking column-by-column compatibility and counting the corresponding input bits) and separately counted digit sums over the true residue period for each of the 16 cases. The table scaled by 64 was (43,38,41,42); (38,40,40,41); (41,40,40,41); (42,41,41,42). The only minimal actual gaps are (1,2),(2,1), not clipped large-gap cells, giving precisely the two doubling families and F(3)=3/32.

## originality

PASS

The supported distinct contribution at the recorded frozen publication date is the exact all-gap weight-three spectrum and extremizers via finite saturation, not the carry identity, a general fixed-t evaluator or the isolated values c_11 and c_13. Later indexed work materially overlaps: the all-weight clipping theorem and its weight-three minimum subsume that part, and combined with known exact fixed-shift recurrence make the full sixteen-cell table mechanically obtainable. This is real coverage, but not evidence that the stronger result predates the frozen finding.

## value

PASS

The fixed-Hamming-weight extremal question was already posed for a natural digit-sum correlation. Weight three is a meaningful small layer with two interacting gaps; the classification shows that neither full adjacency nor full separation minimizes the bias. A sharp lower bound with all minimizers and an exact saturation scale is useful for comparing small-weight mechanisms and for benchmarking fixed-weight estimates. At the recorded frozen date the inspected earlier recurrences alone did not give the required reduction from unbounded shifts; the later all-weight theorem now supplies a broader route.

The dated certificate retains the supplied scientific assessment, sources and limitations.
