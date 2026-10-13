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

Execute `python3 verify.py` (Python 3 standard library only). Its assertions check field arithmetic in \(\mathbb F_{16}\) using `0x13`, uniqueness of the 17 spread directions, all 255 generator columns, rank 12, and the weight enumerator of 4096 codewords, including minimum positive weight 60. The program enumerates all potential three-column dependencies among distinct positions, obtaining exactly 635 and the 255-position histogram `{3:30,4:30,6:60,7:15,8:30,9:30,12:60}`. It verifies every corresponding recovery pair and pairwise disjointness of helpers. Separately, enumerating 680 spread-index triples from four-bit labels yields 33 zero-sum triples, four zero-labelled spread members, and the same local recovery counts; the resulting independent identity is \(33\cdot15+4\cdot35=635\). Its terminal success marker is `VERIFY_OK`.

The executable gives a complete finite check only for the displayed Desarguesian four-spread. The written proof establishes the stronger spread-independent statement and the distance from character sums; the computation by itself does not enumerate all possible full spreads or other labels. The published source's parameters are not assumed when verifying its explicit index sets. No independent audit was performed.
