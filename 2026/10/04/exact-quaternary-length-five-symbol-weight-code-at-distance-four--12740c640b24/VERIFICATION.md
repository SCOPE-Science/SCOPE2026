---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

Run `python3 verify.py` using the files in this package. The script checks the explicit \(15\)-word code, all pairwise Hamming distances, all ten two-coordinate projections, the symbol-weight condition, and the equality-incidence counts used in the proof. It also verifies that the displayed witness omits \((1,1)\) from every two-coordinate projection.

The analytic upper bound is not inferred from exhaustive search. Its only finite arithmetic inputs are \(\binom{5}{2}=10\), four diagonal pairs per full quaternary two-coordinate projection, and the fact that symbol weight at most \(2\) permits at most two equal-coordinate pairs in a length-five word.

The verifier does not enumerate or classify all maximum codes. The originality assessment depends on the cited literature inspections and targeted searches, not on the verifier.
