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

# Verification procedures and boundaries

Run `python3 verify.py` with a standard Python 3 interpreter. The program separately constructs generalized paperfolding words by the two-adic valuation equation and by iterated folding. It verifies their agreement for all instruction strings through depth ten and deterministic larger samples. It independently checks all possible three-state greedy-arch transitions through an eight-symbol block, all \(2^{k+1}\) instruction prefixes for each \(3\le k\le10\), and sampled cases at \(k=11,13,16,19\). It also enumerates actual scattered subsequences for \(k=3,4\).

The completed finite check ended with `instruction_words_checked 4252` and `VERIFY_OK`. This provides reproducible checks of the transition algebra and small cases. The proof in `RESULT.md`, rather than finite execution or uninspected external validation, establishes the universal quantifiers over all binary instruction streams and every \(k\ge3\). No independent scientific audit or external certification was conducted.
