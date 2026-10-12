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

The proof in `RESULT.md` is universal. It does not infer the theorem from finite computation.

The attached `verify.py` computes the least-prime-factor table through
\[
2{,}000{,}000,
\]
evaluates \(\Omega\) and \(\beta\) exactly, and checks every
\[
1\le n<2{,}000{,}000
\]
satisfying
\[
\Omega(n)\le2,\qquad \Omega(n+1)\le2.
\]
Among these candidates, the equality
\[
\beta(n)=\beta(n+1)
\]
occurs only at
\[
n=1.
\]

The verifier also checks the sharpness witness
\[
\beta(20)=\beta(21)=12,
\]
together with
\[
\Omega(20)=3,\qquad\Omega(21)=2,
\]
and validates the prime-square and squarefree-semiprime formulas used in the proof over many exact instances.

The infinite conclusion rests on the complete symbolic case split in `RESULT.md`; the finite replay is corroborative only.
