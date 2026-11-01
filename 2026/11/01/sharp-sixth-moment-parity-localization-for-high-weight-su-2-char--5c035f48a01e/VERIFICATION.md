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

# Reproduction checks

Run `python3 verify.py` with standard Python 3. The standalone program uses only the standard library; it constructs character-product multiplicities with the classical \(SU(2)\) fusion rule, calculates exact integer/Gaussian-integer sixth moments, checks the exact single-character formula for the 29 positive weights \(1\) through \(29\), follows seven explicit finite-offset coefficient families through four growing weights, and verifies that the proposed positive optimizer dominates 101 mesh values for every ordered pair of parity counts in \(\{1,\ldots,12\}^2\). The program completed with 14,766 successful deterministic assertions.

The exact coefficient \(1/4\), the uniform \(O_S((m+1)^2)\) bound and the continuous maximizer classification are justified by the mathematical proof in `RESULT.md`. The finite checker cannot establish an unbounded-\(m\) limit, a global novelty certificate or independent correctness. The corresponding theoretical assumptions require fixed, finite offset support and ordinary non-dimension-normalized \(SU(2)\) characters.
