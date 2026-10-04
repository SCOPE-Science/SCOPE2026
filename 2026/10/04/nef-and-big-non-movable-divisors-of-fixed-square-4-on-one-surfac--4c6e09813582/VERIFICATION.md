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

The quantified statement is proved symbolically in `RESULT.md`. Simultaneous genericity uses a countable intersection of dense open conditions in \(|2R|\cong\mathbf P^3\) over \(\mathbf C\), and nefness uses intersection theory on the fixed blown-up double cover. No finite computation is used to infer those general facts.

The bundled `verify.py` is a regression check. For odd integers \(n\) through \(999\) it recomputes
\[
A_n^2=8,\qquad B\cdot F=2,\qquad B\cdot\Gamma_n=2(n^2+4),
\]
\[
g(C_F)=2,\qquad g(C_n)=n^2+5,
\]
\[
\widetilde C_F^2=\widetilde C_n^2=-3,\qquad \widetilde C_F\cdot\widetilde C_n=5,
\]
\[
D_n\cdot\widetilde C_F=D_n\cdot\widetilde C_n=2,\qquad D_n^2=4.
\]
It also checks the positive-integer range satisfying \(1\le m<n^2/4+1\) for representative odd \(n\).

The replay output stored in `verification_output.txt` must end in `VERIFY_OK`.

Unproved limits: the verifier does not establish the source cohomology theorem, Bertini's theorem, the uncountability argument, or literature originality. Those are handled by the mathematical proof and source inspection.
