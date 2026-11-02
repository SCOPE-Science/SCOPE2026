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

# Reproducibility and limits

Run `python3 verify_antihole.py` from the directory containing that script (Python 3 standard library only). It independently generates the graph edges, shortest-path distances, all geodesically convex hypotheses, every support trace, the expected independence-polynomial coefficients, and the Littlestone version-space recursion. It is not an infinite-parameter formal verification.

The checked graph orders were \(7\le n\le13\) for all convex subsets and every static support, and \(7\le n\le14\) for online dimensions. The augmented-path online lemma was checked for \(0\le m\le14\). Examples include \(n=7\) with 30 hypotheses and shattered-support polynomial \(1+7z+21z^2+7z^3\), and \(n=8\) with 48 hypotheses and polynomial \(1+8z+28z^2+16z^3+2z^4\). The exact online dimensions for orders seven through fourteen were \(4,4,5,5,6,6,7,7\). Full correctness for all \(n\ge7\) rests on the mathematical proof in `RESULT.md`, not on the finite checker.

The code's final success line is `ALL_ANTIHOLE_GEODESIC_LEARNING_CHECKS_PASS`. No external certificates, libraries, file paths or network access are used. Historical-priority and independent-audit checks are not supplied by numerical tests.
