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
The analytic proof applies to every real \(L_p(\mu)\), \(1<p<\infty\), on a sigma-finite measure space of dimension at least two. The unique support functional gives the zero-mean condition
\[
\mathbb E_\nu T=0,
\qquad
\mathbb E_\nu|T|^p\le1.
\]
For \(p>2\), two applications of conditional and size-biased Jensen inequalities control the scalar moments of orders \(1\), \(p-1\), and \(p\). An explicit two-point law with the same first and \((p-1)\)-st signed moments has no larger \(p\)-th moment. Conditioning away a zero atom gives the sharp scalar envelope. Strict equality yields exactly one positive and one negative ratio level, and disjoint normalized indicators realize the envelope on every admissible measure space. The bijective \(L_p\)--\(L_q\) duality map transports the result to \(1<p<2\).

The scalar Hölder-conjugacy identity \(\Phi_p(t)=\Phi_q(t^{p-1})\) is checked algebraically in the proof and numerically in the bundled checker. Install the declared symbolic-algebra dependency from `requirements.txt` before running `python verify.py`. The bundled standalone `verify.py` checks the cubic formula (including its derivative and exact radical maximum) symbolically. It also executes deterministic rational finite-distribution moment-compression checks and finite-dimensional comparisons with the asserted envelope, including two-coordinate sharp witnesses. These finite computations are supplementary: they do not prove universal quantifiers, optimality, or equality classification. The continuum proof is the exact size-biased compression in RESULT.md.

Independent audit: not performed. Independent validation: not performed.
