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

# Direct finite verification and scope

Run the two self-contained, standard-library Python files as follows:

`python3 verify.py`

`python3 verify_polynomial.py`

The first script constructs the closed neighborhoods of the rook graph and the open neighborhoods of its *complement* directly from the coordinate condition for adjacency. It checks that no subset smaller than the asserted minimum is feasible, and that every subset at the asserted size agrees with both the proposed classification and the exact number. Sixteen parameter pairs were tested, totaling 271,904 examined subsets. The second script independently builds the claimed polynomial from integer polynomial arithmetic and checks each coefficient against brute-force neighborhood tests over all subsets of twelve parameter pairs, totaling 1,435,472 subsets. Both tests passed with assertions enabled.

The finite experiments do not certify parameters beyond those explicitly tested. The infinite-domain assertions are proved combinatorially in `RESULT.md`; no computational oracle, imported search table, or unproved lemma is necessary. Neither independent scientific audit nor independent certification has been performed.
