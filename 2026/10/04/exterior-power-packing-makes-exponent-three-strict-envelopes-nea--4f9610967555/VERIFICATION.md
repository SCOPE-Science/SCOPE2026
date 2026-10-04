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

The scientific proof is symbolic and follows the source's graded-Lie-algebra calculations.

For the first repair stage, the source identifies the degree-two part of a free rank-\(q\) factor with \(\Lambda^2(\mathbb F_3^q)\). The injectivity proof of Lemma 4.7 separates the defining relations only through linear independence of their degree-two classes. Hence any \(r\le\binom q2\) independent basic wedges can replace the \(r\) disjoint generator pairs used in the printed lemma.

For the second stage, \(\gamma_3(F_q)\) is central and its graded image is \(\Lambda^3(\mathbb F_3^q)\). Choosing independent basic triple commutators makes the kernel calculation in Lemma 4.9 identical: a product of the selected triple commutators is trivial only when all coefficients vanish. The intersection proof of Lemma 4.10 then carries over verbatim with this packed basis.

The dimension bounds used are
\[
r_2\le n
\]
for the first defect space and
\[
r_3\le\binom N2
\]
after the first repair. They give the definitions of \(q_2(n)\) and \(q_3(N)\).

The final rank-two free factor and existential-closedness transfer are unchanged from Proposition 4.13.

The bundled `verify.py` computes the packing functions and confirms over a finite range that the displayed exact formula is below the source's \(15n^2\) bound and that the substituted Theorem 3.3 bound has quartic rather than octic polynomial scale. This arithmetic replay is corroborative only; the arbitrary-\(n\) result is the proof above.

## Limits

No claim of optimality is verified. The checker does not certify the group-theoretic theorem by enumeration; it only verifies the numerical functions used after the symbolic proof.
