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

Run `python3 verify.py` with a standard Python 3 interpreter.

The verifier builds all \(27\) words of \(\{0,1,2\}^3\) and derives the bad four-column configurations directly from the definition: for each four-set it tests all three partitions into two pairs and asks whether some coordinate gives disjoint symbol sets to the two pairs. It then exhausts all \(\binom{27}{5}=80730\) five-subsets and all \(\binom{27}{6}=296010\) six-subsets. The expected exact outcomes are \(54\) admissible five-sets and no admissible six-set.

For every maximum, the verifier checks row multiplicities \((2,2,1)\), coincidence of the three singleton positions, the parity-class description after deleting that column, and the Hamming-distance profile \(2\) with multiplicity \(6\) and \(3\) with multiplicity \(4\). It then constructs all \(1296\) transformations in \((S_3)^3\rtimes S_3\), verifies that the canonical family has orbit size \(54\), that this orbit equals the complete maximum-family census, and that the stabilizer has order \(24\).

The computation is exact integer/set logic. No randomized step, numerical tolerance, external solver, network access, or unproved extrapolation is used. The verification proves only the finite parameter stated in the finding.
