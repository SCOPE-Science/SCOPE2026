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

Run `python3 verify.py` in a Python 3 standard-library environment. The checker reconstructs finite unary successor operation tables and tests arbitrary functions against \(fT=Uf\), including idempotence and image cardinalities. It also independently tests the corresponding finite Boolean modal operations under inverse image and compares with the exact generating-function arithmetic.

Replay output:

`VERIFY_OK 56 finite frames; 1262096 brute function tables; 11009 bounded maps; 1343 idempotents; 15 modal-algebra checks (2165 candidate maps); 225 hom-pairs (22183 direct function tables, 531 bounded homomorphisms); 1228 coefficient/reversal assertions; two 9-world normal-form witnesses (1968 maps each)`

The \(56\) full-table frame cases have at most \(6\) worlds, and the separate \(225\) source–target checks have at most \(4\) worlds on each side. The explicit \(9\)-world witnesses are checked by exhaustively generating every map in the proved normal form, not by considering all \(9^9\) functions. This is finite evidence, not a computational proof for arbitrary parameters. The general proof is in `RESULT.md`.
