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

`python verify.py`

Expected output:

`VERIFY_OK pairs=33 subset_checks=30736 paired_sets=8446 structural_checks=30736 coefficient_checks=134 max_order=12`

The verifier constructs \(D_{r,s}\) directly for \(2\le r,s\le7\) with \(r+s\le12\). For every vertex subset it checks domination from the adjacency relation and perfect matching by a generic recursive matching search. It independently compares that result with the proved parity-and-bridge criterion, then compares the coefficient counts with
\[
E_r(x)E_s(x)+x^2Q_{r-1}(x)Q_{s-1}(x).
\]
It also checks that the minimum paired-dominating set is uniquely the bridge pair and that evaluation at \(x=1\) agrees with
\[
\bigl(2^{r-1}-1\bigr)\bigl(2^{s-1}-1\bigr)+2^{r+s-4}.
\]

The computation is finite and is not evidence for untested orders by itself. The infinite statement rests on the symbolic proof in `RESULT.md`.
