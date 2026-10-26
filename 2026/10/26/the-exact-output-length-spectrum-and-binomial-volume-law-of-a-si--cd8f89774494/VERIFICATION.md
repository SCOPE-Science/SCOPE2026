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

# Reproducibility and boundaries

Run `python3 substring_ball_verify.py`. It uses only standard Python 3 and no downloads. It independently enumerates every \(d\)-deletion, \(i\)-insertion edit at the same position for \(0\le d,i\le k\), with duplicate outputs merged in sets. For 44 parameter triples on alphabets of size 2, 3 and 4, a total of 17,413 input words were examined, and every output-length layer was checked exactly. For each triple, the complete ball-size histogram was also compared to \(q^k\binom{n-k}{j}(q-1)^j\).

The captured execution record is `substring_ball_verify.stdout`, terminating in `VERIFY_OK`. This is an exhaustive finite cross-check within the stated ranges, not a proof beyond them. All-parameter correctness rests on the rightmost-window counting lemma, the maximal-window representation, the known pure-burst-deletion identity, and the independent-edge counting on residue-class paths. In particular, the variance formula excludes the degenerate \(n=k\) case from Gaussian standardization, and the CLT holds when \(n-k\to\infty\) at fixed \(q\).

Only the self-review described separately has been carried out. No independent audit has been performed.
