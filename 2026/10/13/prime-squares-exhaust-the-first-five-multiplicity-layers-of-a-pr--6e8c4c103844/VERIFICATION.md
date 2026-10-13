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

The proof in `RESULT.md` is universal and does not infer its conclusion from a bounded enumeration.

The attached `verify.py` constructs a least-prime-factor table through
\[
2{,}000{,}000,
\]
factors every integer in that range, and evaluates
\[
B(n),\qquad \beta(n),\qquad \Omega(n)
\]
with exact integer arithmetic.

It checks that every solution of
\[
B(n)=\beta(n)^2
\]
with
\[
\Omega(n)\le5
\]
is a prime square. It also finds the minimum \(\Omega\) among non-prime-square solutions in the range and confirms that the minimum is \(6\), first attained by \(144\).

Finally, it independently checks
\[
B(144)=25=\beta(144)^2
\]
and
\[
\Omega(144)=6.
\]

The finite replay corroborates the symbolic argument and its sharpness witness. It does not certify any statement about all solutions with \(\Omega(n)\ge6\).
