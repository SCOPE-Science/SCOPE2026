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

# Reproducible checks and limits

Run `python3 check.py` with standard-library Python 3. The supplied `check_output.txt` is the recorded output for the embedded executable.

For \(m=2,3,4,5,6\), the verifier explicitly enumerates all permutations, computes all power images modulo the exponent of \(S_m\), forms centralizer intersections, and tests every ordered exponent-residue pair. The respective numbers are \(4\), \(36\), \(144\), \(3600\) and \(3600\) checked pairs. The checker also tests 10,000 ordinary positive-exponent pairs for the possible least degrees, constructive extremal pairs through prime power \(37\), and seven explicit noncommuting permutation pairs in degrees \(3,4,5,7,8,9,11\). All tests in the recorded execution passed.

A finite permutation enumeration cannot establish the theorem for arbitrarily large degrees. The infinite assertion depends on the normal-subgroup classification of symmetric groups, the characterization of their exponent as \(\operatorname{lcm}(1,\ldots,m)\), and the fact that the exponent jumps exactly at prime powers. The supplied tests cover the algebraic exceptional cases and representative higher degrees but are not an external mathematical audit or a comprehensive publication-priority check.
