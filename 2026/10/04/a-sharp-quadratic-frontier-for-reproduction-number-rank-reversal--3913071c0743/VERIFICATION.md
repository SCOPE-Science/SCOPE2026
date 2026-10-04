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
The source identities for the individual-based offspring matrix were checked against the primary article: \(R_I\) is the positive root of \(x^2-a x-u^\top v=0\), and the source proof gives \(u^\top v=R_*-a\).

The universal bounds are verified by the exact identities \(p_r(r)=(r-1)(r-a)\) and \(p_r(\sqrt r)=a(1-\sqrt r)\), with \(a>0\) and \(0<a\le r\).

The sharpness construction uses only finite admissible household models. For household size \(n\), the probability of \(n-1\) successive infection events before any recovery is \(\prod_{s=1}^{n-1}\lambda s/(\lambda s+1)\), which tends to one as \(\lambda\to\infty\). This proves, rather than numerically suggests, that the household final-size mean tends to \(n\).

The packaged `verify.py` uses exact rational arithmetic to replay the four-person witness: \(m_4(2)=779/225\), global rate \(675/779\), \(R_*=3\), and \(p_3(2)=104/779>0\), hence \(R_I<2\). The verifier does not certify any claim about outbreak probability, final size ordering, growth rate, or vaccination thresholds.
