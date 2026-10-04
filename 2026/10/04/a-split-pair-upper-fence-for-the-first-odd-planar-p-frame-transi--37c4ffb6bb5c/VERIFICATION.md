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
The analytic verification uses the exact unordered-pair count for the split-pair configuration. The key scalar difference is
\[
F_k(p;\alpha)=2(k-1)\cos^p\alpha+2k\sin^p\alpha+\cos^p(2\alpha)-(2k-1).
\]
For \(0<\alpha<\pi/4\), every exponential base lies in \((0,1)\), so \(F_k\) is strictly decreasing. Its \(p\downarrow0\) limit is positive, and
\[
F_k(2;\alpha)=2\sin^2\alpha\bigl(2\sin^2\alpha-1\bigr)<0.
\]
This proves existence and uniqueness of the root used in the claim without numerical computation.

The asymptotic check rewrites the root equation as \(2kA(q_k)+B(q_k)=0\), where \(A(p)=\cos^p\alpha+\sin^p\alpha-1\) and \(B(p)=1-2\cos^p\alpha+\cos^p(2\alpha)\). For fixed \(p<2\), \(A(p)>0\), hence \(q_k\to2\). The mean-value theorem then yields the displayed limit.

The bundled `verify.py` is a finite replay only. It checks pair counts directly from angle multisets, scalar-root signs, the \(\pi/8\) asymptotic constant, and the \(k=2\), \(\pi/7\) decimal. It does not certify global optimality or replace the all-\(k\) proof.
