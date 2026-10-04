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

The proof was reconstructed from the normalized geometry rather than inferred from numerical experiments.

For \(A=D\) and \(B=c+TD\), the cap fraction in the halfspace \(u\cdot x\ge t\) is obtained by substituting \(x=c+Ty\), giving the normalized threshold \((t-c\cdot u)/\|T^{\mathsf T}u\|\). Nesting gives \(c\cdot u+\|T^{\mathsf T}u\|\ge1\). For a chosen normal with \(c\cdot u\ge0\) and \(0\le t\le1\), the exact identity
\[
(c\cdot u)+t\|T^{\mathsf T}u\|-t
=t\bigl((c\cdot u)+\|T^{\mathsf T}u\|-1\bigr)+(1-t)(c\cdot u)
\]
has a nonnegative right-hand side. This proves the threshold order required by the decreasing unit-ball cap function.

The included `verify.py` checks the scalar identity and implication exactly over a rational stress grid and prints `VERIFY_OK`. This diagnostic check is not used to promote finite testing into a proof; the displayed factorization is the proof for all admissible real parameters.

No claim is made beyond nested ellipsoids or beyond the stated one-sided cap-fraction comparison.
