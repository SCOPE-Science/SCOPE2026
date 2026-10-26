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

# Reproducibility and checks

The attached `verify_nilpotent_mutual_zero.py` is a standalone Python 3 program using only the standard library. Run it with `python3 verify_nilpotent_mutual_zero.py`. It enumerates all nilpotent partial injections in sizes \(1\)–\(6\) and checks the theorem at every prescribed rank pair. For sizes through five, both compositions are independently evaluated from the maps; at size six, equivalent independent bitset domain/image conditions are used for speed. In the test environment all checks passed and the program printed `VERIFY_OK_NILPOTENT_MUTUAL_ZERO_RANKS`.

Observed numbers of nilpotent maps at sizes \(1,2,3,4,5,6\) were \(1,3,13,73,501,4051\). Observed numbers of mutually annihilating ordered pairs were \(1,7,55,565,7141,106891\). The program also checks symmetry under exchanging the two ranks and exact integrality of the closed formula.

Mathematical proof checks performed separately: domain/image equivalences, cycle-selection cancellation via \(\sum_{\pi\in S_j}(-1)^{\#\operatorname{cycles}(\pi)}=0\) for \(j\ge2\), singleton marking of Lah-number chain decompositions, factorial cancellation for \(n\ge2\), and degenerate rank boundaries. These establish the claimed all-size result without relying on finite sampling.

The program does not enumerate sizes beyond six. The earlier literature comparison is necessarily bounded and does not constitute proof of absolute priority. Independent mathematical audit: not performed.
