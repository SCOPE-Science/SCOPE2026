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
Run `python3 verify.py`.

For each
\[
2\le m\le12,
\]
the checker builds \(g_m\) and \(f_m\) from the definitions in `RESULT.md`.

It verifies the exact two-chain evolution on a large tail window, checks that
\[
g_m^{(m)}(e)=0
\]
there, and replays the global failure witness numerically through many multipliers:
\[
f_m^{(m)}(2^{2m-1}n)=f_m^{(m)}(2^{2m}n).
\]

For each earlier iterate and every tested nonzero shift, the checker also finds a large square exponent whose shifted partner is not a square and confirms that the two \(g_m\)-iterate states differ. Finally it tests bounded scaling signatures for pairwise distinction.

The finite replay is not the proof for arbitrary \(m\). The all-parameter argument is symbolic and appears in `RESULT.md`.

A successful replay prints `VERIFY_OK`.
