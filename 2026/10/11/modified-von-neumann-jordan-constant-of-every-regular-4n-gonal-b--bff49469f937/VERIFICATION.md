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
The infinite-family proof is analytic. For the inradius-one regular \(N=4n\) polygon,
\[
\|z\|_N\le\|z\|_2
\]
for every vector, while every polygonal unit vector satisfies
\[
\|x\|_2\le\sec\!\left(\frac{\pi}{N}\right).
\]
Hence the Euclidean parallelogram identity gives
\[
\frac{\|x+y\|_N^2+\|x-y\|_N^2}{4}
\le
\sec^2\!\left(\frac{\pi}{N}\right).
\]

The adjacent vertices
\[
x=R(\cos\alpha,\sin\alpha),
\qquad
y=R(\cos\alpha,-\sin\alpha),
\qquad
R=\sec\alpha,\quad \alpha=\frac{\pi}{N},
\]
give
\[
\|x+y\|_N=2,
\qquad
\|x-y\|_N=2\tan\alpha,
\]
because both coordinate axes are facet-normal rays when \(4\mid N\). Thus the upper bound is attained exactly.

`verify.py` reconstructs the facet representation for representative values \(N=4,8,12,16,20,24,32,40\), verifies the stated extremizers, and performs deterministic boundary sampling as a stress test. These finite checks are reproducibility aids only; they do not replace the symbolic proof.

No independent audit or independent validation has been performed.
