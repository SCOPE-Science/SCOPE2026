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

The mathematical proof uses the exact zero-rank criterion for a target \(0^i1 0^{n-1-i}\). For a host with \(Z\) zeros, a `1` after \(a\) zeros can serve target index \(i\) precisely if \(a\ge i\) and \(Z-a\ge n-1-i\). Thus a marker covers at most \(Z-n+2\) possible indices. The run bound \(Z\le2(K+1)\) and equality cases are proved in `RESULT.md` and do not depend on computational enumeration.

The standalone checker `verify_onehot_rll.py` uses an independent greedy subsequence predicate and directly generates all words avoiding `000` at every host length from \(n\) through \(\lceil3n/2\rceil\), for every integer \(n\in[4,14]\). It compares the full set of minimizers with the constructive formula and checks that they also avoid `111`.

Run:

```bash
python3 verify_onehot_rll.py
```

Expected final line:

```
CHECK_OK total_candidate_hosts_examined=1640493
```

The checker returned this line on the actual standalone file, with the detailed optimal-host counts \(1,5,1,6,1,7,1,8,1,9,1\) for lengths four through fourteen. This is a finite cross-check, not a proof of the infinite classification. No external formal certification or independent mathematical audit has been performed.
