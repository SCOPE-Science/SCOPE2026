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

The unrestricted exact classification is proved in `RESULT.md` from the two
possible base-\(B\) digit lengths of a product of two fixed-length factors.

The asymptotic proof uses the prime number theorem in the form
\[
\pi(x)\sim\frac{x}{\log x}.
\]
For each fixed subinterval of a base-\(B\) digit block, this gives uniform
limiting mass after normalization by the block's prime count. Product measure
therefore gives uniform area on \([1,B]^2\). The boundary \(uv=B\) has area
zero, and direct integration gives
\[
\rho_B=\frac{B(B-1-\log B)}{(B-1)^2}.
\]

The packaged checker independently verifies the exact digit criterion for many
finite prime pairs and counts ordered distinct-prime pairs in equal decimal
digit blocks through six digits. It also checks the numerical value of the
closed-form constant.

Finite prime enumeration is corroborative only. It does not replace the prime
number theorem in the infinite limiting statement.
