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

The proof uses an exact two-step burst-deletion model, survivor positions \((1,2),(1,4),(1,6),(3,4),(3,6),(5,6)\), degree reconstruction on a six-edge ordered-pair relation, and a symbolic alphabet-independent census of equality patterns. These deductions are reproduced in `RESULT.md`.

Run `g++ -O2 -std=c++17 verify_rgs.cpp -o verify_rgs && ./verify_rgs`. This checks the complete list of coordinate pairs via actual index deletion, all 4,213,597 restricted-growth symbol-equality patterns on twelve slots, the five nonzero census coefficients, and the global maximum overlap of five. The expected final line is `VERIFY_RGS_OK patterns=4213597 maximum_overlap=5 C3=210 C4=582 C5=363 C6=71 C7=4`.

Run `python3 verify_direct.py`. This uses a separate direct channel simulator for \(q=2,3,4,5\), independently reconstructs deduplicated outputs under both deletion steps, and exhaustively compares all input pairs by aggregate output masks. The expected counts of unordered maximizing pairs for \(q=3,4,5\) are 630, 9504, and 63000; the binary control has maximum overlap four.

Finite checks of fixed alphabets alone cannot establish the statement for every alphabet size. The unrestricted-alphabet proof instead uses that every pair of length-six words induces one of finitely many equality patterns, that the canonical patterns are exhaustively enumerated, and that each pattern with \(k\) labels has exactly \((q)_k\) labeled realizations. No results about longer words or more than two bursts follow from this verification. Scientific review here does not constitute independent validation.
