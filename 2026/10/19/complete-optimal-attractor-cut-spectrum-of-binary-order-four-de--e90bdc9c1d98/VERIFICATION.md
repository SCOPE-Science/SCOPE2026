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

# Exact finite verification

Reproduction requires only Python 3 and the two files `CHECKER.py` and `CUT_CERTIFICATE.tsv` in one directory. Run `python3 CHECKER.py`. It independently enumerates all \(2^{16}=65,536\) labeled binary 16-letter words and all Euler tours of the order-three binary de Bruijn digraph. Both methods, after quotienting by cyclic rotation, give the same 16 representative cycles.

For each cycle and each of its 16 cuts, the verifier builds the linear 19-letter unfolding and its entire set of distinct nonempty contiguous factors. A factor is covered only when an occurrence contains one of the proposed selected positions. It checks the forced four-mark set \(\{4,8,12,16\}\) directly. If that set fails, it exhaustively tests five-position sets until finding the lexicographically first covering set; the provided TSV records this witness. The program requires byte-equivalent rows after parsing, including every proposed witness.

The observed output is:

`ORDER4_DEBRUIJN_ATTRACTOR_PASS cycles=16 cuts=256 min4=192 min5=64`

`cycle_robustness={8:4,12:8,16:4} exhaustive_words=65536`

The logical reason that failure of the specific four-position set excludes **every** four-mark solution is proved in `RESULT.md` via the 16 unique four-grams. Thus this is a finite exhaustive proof for the exactly stated domain, with constructive five-position witnesses for all remaining cases. It is not a general algorithmic or infinite-order theorem; independent audit has not been performed.
