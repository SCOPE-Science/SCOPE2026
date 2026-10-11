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

The statement is for \(1<p<\infty\), \(a=|t|\in[0,1]\), \(b=(1-a^p)^{1/p}\), and a Daugavet point \(x\in S_Y\). The exact slice-invariant targets are
\[
\operatorname{dc}((t,bx))=\big((1-a)^p+b^p\big)^{1/p},
\qquad
\delta c((t,bx))=2b.
\]

The following continuum steps, not merely samples, are verified in the proof:

1. Every dual slice admits a nearly norming length pair \((u,r)\) with \(|u|^p+r^p=1\), and Daugavet-point witnesses with fiber distance approaching \(b+r\). The sharp scalar comparison is \(|a-u|^p+(b+r)^p\ge (1-a)^p+b^p\).
2. The scalar slice \(u\to1\) forces the matching Daugavet upper bound.
3. Any slice containing \((a,bx)\) contains a scaled far witness in the same fiber, giving Delta lower bound \(2b\).
4. For \(u\ge a\), the function \((u-a)^p+(b+(1-u^p)^{1/p})^p\) is nonincreasing, and its value at \(a\) is \((2b)^p\); nearby scalars \(u<a\) are handled by continuity.

Run the bundled standard-library checker using `python verify.py`. It checks exact rational instances of the reverse-triangle and superadditivity inequalities, supplementary real-exponent grids for the Delta envelope, and the strict separation and endpoints. Finite tests are not used as infinite certificates.

No independent audit or independent validation has been performed.
