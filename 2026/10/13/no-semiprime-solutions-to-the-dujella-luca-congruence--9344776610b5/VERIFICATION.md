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

The attached `verify.py` computes \(\Omega(n)\), \(\varphi(n)\), and \(\sigma(n)\) exactly for every
\[
1\le n\le2{,}000{,}000
\]
with
\[
\Omega(n)\le2.
\]
It checks that every prime in the range satisfies
\[
n\varphi(n)\equiv2\pmod{\sigma(n)},
\]
that \(9\) is the only composite hit, and that there is no squarefree-semiprime hit.

The checker also verifies on finite prime samples the prime-square congruence reduction and the two factor reductions used in the odd-semiprime proof.

These computations are corroborative only. The infinite classification follows from the complete symbolic case split in `RESULT.md`.
