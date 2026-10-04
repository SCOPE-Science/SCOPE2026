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

The proof has one finite certificate after the published localization reduction. Execute:

`python3 verify.py`

The program uses `fractions.Fraction` only. For every \(3\le L\le7\) and \(2\le s\le L-1\), it brackets the unique positive zero of
\[
M_{L,s}(r)=\sum_{j=1}^{L}(j-s)r^{j-1}
\]
by exact rational bisection. It then bounds the variation of
\[
H_{L,s}(r)=\sum_{j=0}^{s-1}r^j-\sum_{j=s}^{L-1}r^j
\]
over that bracket using an exact rational upper bound on \(\lvert H'_{L,s}\rvert\). Every one of the fifteen required signs is certified positive. The same method certifies a negative sign for \((L,s)=(8,6)\).

The reduction is exhaustive because, after localization to a contiguous log-affine support, only the support length \(L\) and the integer position \(s\) of the mean remain. Mean monotonicity gives a unique positive root for each nontrivial pair. Thus the finite check is not used to extrapolate an infinite pattern.

The verifier also checks the exact coefficient lists for the displayed eight-point mean polynomial and half-mass polynomial. A successful replay ends with `VERIFY_OK`.

Limit: the extreme-point localization theorem is an external published premise, independently inspected in the cited source and its originating paper; the verifier does not reprove it.
