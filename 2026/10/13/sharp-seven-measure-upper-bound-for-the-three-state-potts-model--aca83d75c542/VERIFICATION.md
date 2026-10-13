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

The proof is analytic. The bundled `verify.py` replays the two exact polynomial factorizations used in the new step with integer-coefficient bivariate polynomial arithmetic and performs supplementary rational checks of the quadratic endpoint identities. It is not used to infer the global root count.

The critical identities are
\[
L(v;\theta)=(v+1)(\theta v-v^2-1)
\]
and, after substituting \(q=3\), \(k=3\), \(m=1\) into the source derivative formula (6.23),
\[
N(v;\theta)=(\theta+2)(v-1)(v+1)v^2R_\theta(v+v^{-1}),
\]
where
\[
R_\theta(x)=-2x^2+(2\theta-6)x+5\theta-1.
\]
The global argument is independent of computation: \(R_\theta(2)=3(3\theta-7)\), \(R_\theta(\theta)=-(\theta+1)\), and the vertex \(x_0=(\theta-3)/2\) give the complete zero count on \(2<x<\theta\).

To replay the supplementary checker, run `python3 verify.py`. A successful replay prints `VERIFY_OK`.

No claim is made that finite checks certify an infinite parameter domain; the displayed algebra and sign argument are the proof.
