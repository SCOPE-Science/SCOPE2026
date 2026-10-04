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
The central identity is checked in exact integer arithmetic. For \(p=ab\) and \(s=a+b\), the checker evaluates
\[
Q_{a,b}=\frac{p}{24}\left(2p^3-6p^2s+3ps^2+18ps-26p-66s+144\right)
\]
and independently evaluates the Cayley formula after substituting
\[
d=ab,\qquad g=1+\frac{ab(a+b-4)}2.
\]
The values agree throughout the regression range.

The infinite parity reduction is not inferred from that bounded range. The proof in RESULT.md establishes symbolically that \(Q_{a+8,b}\equiv Q_{a,b}\pmod2\) and, by symmetry, \(Q_{a,b+8}\equiv Q_{a,b}\pmod2\). The bundled checker then evaluates all \(64\) residue classes modulo \(8\), which is exhaustive once periodicity has been proved, and verifies exactly \(24\) odd classes.

The real conclusion is scheme-theoretic: a zero-dimensional real scheme of odd degree has a real closed point because non-real points occur in conjugate pairs of even total degree. No reducedness assumption is used for that implication.

Limits: the theorem is restricted to the general \(a,b\ge4\) finite four-secant regime, and does not describe special members with excess-dimensional four-secant loci.
