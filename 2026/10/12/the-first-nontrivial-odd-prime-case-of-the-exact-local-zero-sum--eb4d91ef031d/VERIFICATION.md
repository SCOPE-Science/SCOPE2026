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

# Verification of the exact prime-five local zero-sum constant

To reproduce, compile `artifacts/verify.cpp` with `g++ -std=c++17 -O2` and run the resulting executable; independently run `python3 artifacts/verify.py`. No external mathematical package is required. Actual outputs are recorded in `artifacts/replay.txt`.

Both implementations enumerate nondecreasing multisets of the twenty residues not divisible by five, using the exact recurrence for residues of subsets of exactly zero through five positions. A prefix is discarded only upon acquiring a five-subset sum in residues \(5,10,15,20\pmod{25}\); any extension then also contains that subset. Each algorithm therefore exhausts all witness-free multisets through length eleven.

The two enumeration outputs agree: numbers of witness-free multisets at each length 0 through 11 are 1, 20, 210, 1540, 8855, 35700, 78700, 89100, 58350, 21600, 3900, 0. The ten-element obstruction is checked independently by enumerating its 252 five-position choices. There are no witness-free eleven-element multisets. This is an exhaustive finite computation supported by a proved recurrence, not statistical sampling. No independent external audit has been performed.
