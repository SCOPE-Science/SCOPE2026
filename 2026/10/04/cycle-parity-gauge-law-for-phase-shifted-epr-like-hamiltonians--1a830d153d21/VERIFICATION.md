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
The proof is analytic. The executable artifact is a corroborative finite replay only.

It reconstructs the local operator \(h(se^{i\theta})\) and the cycle Hamiltonian directly from the definition. For \(C_3\), it computes the characteristic polynomial by a standard-library Faddeev-LeVerrier routine for several choices of \(s\) and nontrivial edge phases and compares it with the polynomial determined by the claimed eight eigenvalues. For \(C_4\), it uses exact rational arithmetic at flux \(0\) and \(\pi\) to verify
\[
\operatorname{Tr}(A_s^4;\Phi=0)-\operatorname{Tr}(A_s^4;\Phi=\pi)=96s^4
\]
for several rational values of \(s\), together with the displayed closed fourth-moment formula.

The finite replay does not certify the theorem for all cycle lengths or all phases. Universal correctness rests on the gauge recursion and the trace-monomial/kernel argument in `RESULT.md`.
