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

# Reproducibility and verification

The independent-set enumeration and discrete-Morse reduction are exactly specified in the accompanying `verify_nauru.py` (standard-library Python). The verifier constructs the undirected generalized Petersen graph from the explicit formula, independently tests every face extension, performs a 24-stage lexicographic matching on all 35,219 augmented faces, verifies that there are 17,605 pairs and exactly six critical five-simplices and three critical six-simplices, and topologically sorts every one of the 205,680 directed face-cover relations to prove acyclicity.

The same program constructs signed incidences using increasing vertex order, recursively eliminates matched degree-five/six pairs over the integers, recovers the six-by-three Morse boundary matrix and verifies a \(-1\) determinant minor giving a primitive rank-two attaching-image. Successful execution prints `NAURU_INTEGER_VERIFY_OK`.

The companion `check_nauru_mod2.py` independently uses an include/exclude recursion on graph vertices rather than face-extension enumeration. It forms every augmented simplicial boundary over \(\mathbb F_2\) and computes ranks with exact bitset elimination, yielding reduced Betti ranks four in dimension five and one in dimension six. A successful run prints `NAURU_MOD2_VERIFY_OK`.

Both tools enumerate finite objects exhaustively; they do not prove a theorem for infinitely many graphs. The all-degree mod-two computation is only a secondary cross-check, and does not establish integral homotopy by itself. The integral discrete-Morse degree cancellation is the critical step. Independent validation and audit have not been performed.
