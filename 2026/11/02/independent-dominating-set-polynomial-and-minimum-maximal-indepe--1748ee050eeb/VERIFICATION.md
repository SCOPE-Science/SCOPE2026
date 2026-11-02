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

# Reproducibility
The stand-alone Python script `verify_primary.py` requires Python 3 and NetworkX. It directly builds each two-token graph from unordered pairs and compares every maximal clique of its complement with the closed size enumerator. The C++17 script `verify_alternative.cpp` builds pairwise compatibility masks independently and uses a pivoted Bron–Kerbosch implementation on integer bitmasks; compile with `g++ -std=c++17 -O2`. Both check pairs (2,2), (2,3), (2,5), (3,3), (3,4), (3,5), (3,6), (4,4), (4,5), and (5,5). The tests reproduced all full size distributions, not only total counts, and confirmed the minimum and maximum values. The exact general result follows from the proof in `RESULT.md`, not from finite enumeration. No external independent audit has been performed.
