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
# Mathematical verification

The theorem's full proof has been reconstructed independently of decimal computations. The generator is \(A_{N,b}=\operatorname{diag}(b,b^2,\ldots,b^N)\), with \(b>1\), \(1\le r\le\infty\), \(N\ge1\). The positive scalar kernels integrate to one; the convolution norm formula follows from Minkowski and near-Dirac approximate identities. The logarithmic partitions cover \((0,\infty)\) without overlap except null endpoints. The retained \(N+2K\) scales, middle \(N-2K\) scales, and the positive/negative kernel tails give the displayed finite-\(N\) bound whenever \(2K<N\). For fixed spacing, choosing \(K\) logarithmic in \(N\) is admissible for all sufficiently large \(N\).

The exact coefficient integral converges because negative spectral scales have geometric decay while positive scales have exponential decay. For \(r=1\), mass conservation gives norm and coefficient exactly one. For \(r>1\), strictly positive simultaneous kernel coordinates give a coefficient strictly below one. Spacing limits use separately stated limiting orders; uniform convergence of shifted Riemann sums holds for every fixed finite \(r\), while \(r=\infty\) uses a sampled supremum.

A reproducibility script evaluates the \(r=2\), \(b=2\) coefficient using truncated sums and quadrature; computed decimals are not treated as an infinite proof or certified intervals. No certification, independent audit, or finite computation is presented as supporting the analytical inequalities beyond illustrating their values. Potential unseen equivalent results in general vector convolution literature remain an originality limitation.
