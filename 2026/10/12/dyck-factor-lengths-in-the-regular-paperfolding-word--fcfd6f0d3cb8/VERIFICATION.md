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
# Verification

Run `python3 verify.py` beside `certificate.json`.

The verifier constructs the regular paperfolding prefix independently from the odd-part rule and from the recursive folding word
\[
W_{r+1}=W_r\,0\,\overline{W_r^R},
\]
checking equality through length \(32767\).

It verifies the exact prefix-balance identity with binary run count for every \(1\le N\le10^6\). It then exhausts endpoint intervals through \(4096\) and confirms that every nonnegative equal-height return has length \(2^k-2^i\) with \(1\le i<k\), and that every such length in range occurs. Canonical witnesses are additionally checked for all \(2\le k\le17\).

The infinite theorem is established by the symbolic proof in `RESULT.md`; finite checks are supplementary.

Independent audit has not been performed.
