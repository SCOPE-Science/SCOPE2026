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

Run:

`python3 verify.py`

The script builds the full Parikh signature from scattered occurrences of every consecutive alphabet block. It enumerates every binary word of length at most \(9\) and every ternary word of length at most \(7\), groups words by exact signature, and verifies that the number of singleton fibers is at most both the number of realized signatures and
\[
\prod_{\ell=1}^{s}\left(\binom{n}{\ell}+1\right)^{s-\ell+1}.
\]
For every enumerated word it also checks each length-\(\ell\) entry against the cap \(\binom{n}{\ell}\).

As a separate implementation check, the exact binary number of \(M\)-unambiguous words of length \(m\) is verified to equal \(6m-10\) for \(4\le m\le9\), matching the formula quoted in the 2020 source. The polynomial exponent identity
\[
\sum_{\ell=1}^{s}\ell(s-\ell+1)=\binom{s+2}{3}
\]
is checked for \(2\le s\le50\).

These finite computations do not certify the theorem for unbounded \(n\). The infinite claim is proved by the symbolic matrix-range counting argument in `RESULT.md`.
