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

# Reproducibility and limitations

The exact finite lemma is implemented by the accompanying C++17 source `gapped3_qary_cert.cpp`; compile using `g++ -std=c++17 -O2 gapped3_qary_cert.cpp -o gapped3_qary_cert` and execute `./gapped3_qary_cert`.

The enumerator reads every one of the \(2^{13}=8192\) binary words and every one of the \(3^{13}=1594323\) ternary words of length thirteen. Each signature includes all one-gap-subsequence multiplicities for lengths one, two, and three. It additionally enumerates binary source lengths three to twelve. The program fails unless the binary collisions are exactly the four supplied doubletons and the ternary collisions are exactly the twelve different-symbol relabelings of them. A successful run prints `PASS_BINARY_3_TO_12_INJECTIVE_BINARY_13_FOUR_TERNARY_13_TWELVE_TWO_LETTER_PAIRS`.

The supplementary `independent_deck_check.py` compares explicit three-level index-combination enumeration against independently programmed dynamic-programming signatures, confirming the twelve ternary and four binary candidate pairs and 500 extra reproducibly sampled test words; its expected final message is `INDEPENDENT_DIRECT_AND_DP_PASSED 516`.

The ternary census is exhaustive, while the secondary randomized tests are not and are not used as an exhaustive premise. The general \(q\)-ary conclusion is a proof from the exhaustive ternary premise and the alphabet-map lemma; no finite test of larger alphabets is used as a substitute for that proof. Scientific and literature-access limitations are stated in the main result and scientific review.
