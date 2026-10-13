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

The universal claim is proved symbolically in `RESULT.md`; finite computation is not used as an infinite proof.

The proof-critical checks are:

1. For \(S=\sigma(q^b)\) and \(H=\sigma(q^{b+1})\), exact algebra gives
\[
\frac{(S+1)/q^b}{H/q^{b+1}}=1+\frac{q-1}{H}.
\]
2. A two-prime host in the minimal layer is a square of the form \(q^{b+1}p^{2a}\), and comparison with the divisor \(q^bp\) gives \(p\ge S\).
3. The exact identity then forces \(p^{2a}\mid H\), because \(p>q\) and \(\sigma(p^{2a-1})\equiv1\pmod p\).
4. The elementary inequality \(S^2>H\) contradicts \(p^{2a}\ge S^2\).

`verify.py` checks the exact rational identity, the inequality, and direct small forbidden cases. `verification_output.txt` records its successful output. The finite checks are regression evidence only.
