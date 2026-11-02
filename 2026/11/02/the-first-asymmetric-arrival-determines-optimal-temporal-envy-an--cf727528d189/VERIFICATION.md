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

# Computational verification and scope

Running `python3 verify_binary.py` with ordinary Python 3 standard-library modules `itertools` and `fractions` enumerates all four binary valuation vectors in every ordered profile of length \(0\) through \(8\). This is \(1+4+16+64+256+1024+4096+16384+65536=87381\) input profiles. A dynamic program over signed own-minus-other utilities minimizes exact cumulative maximum envy without using the paper's parity construction. Its optimum agrees on every profile with both the closed formula and the explicit allocation's simulated cost. The script further checks the two oblivious-adversary valuation sequences for horizons \(2\) through \(30\), their offline costs, the wrong-first-choice costs, and the rational expected bound \((m+1)/2\).

Expected final output: `VERIFY_OK exhaustive_binary_profiles=87381 horizon_family=2..30 worst_deterministic_ratio=m worst_randomized_minimax=(m+1)/2`.

The general theorem and competitive bounds are justified analytically in `RESULT.md`. Finite exhaustive experiments do not constitute a universal proof; the deterministic and randomized minimax equalities are deliberately restricted to two specified inputs. The external independent audit status is unperformed.
