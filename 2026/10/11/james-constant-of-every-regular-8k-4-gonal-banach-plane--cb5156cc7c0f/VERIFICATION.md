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
The theorem is proved analytically in `RESULT.md`. The critical chain is
\[
\|z\|_N\le\|z\|_2,
\qquad
\|x\|_2\le\sec\!\left(\frac{\pi}{N}\right)\quad(x\in S_{X_N}),
\]
followed by
\[
\|x+y\|_N^2+\|x-y\|_N^2
\le
2\|x\|_2^2+2\|y\|_2^2
\le
4\sec^2\!\left(\frac{\pi}{N}\right).
\]
This gives the global upper bound for every unit pair.

For \(N=8k+4\), the exact identity
\[
\frac{2k+1}{N}=\frac14
\]
places a unit-ball vertex at angle \(\pi/4\), and \(N/4=2k+1\) makes the coordinate axes facet-normal directions. The explicit right-angle vertex pair therefore gives equality.

`verify.py` checks those integer identities exactly for a large finite range and independently reconstructs the polygonal norm for several representative values of \(N\), including \(4,12,20,28,36\). These numerical checks are reproducibility aids only and are not used to justify the infinite quantifier.

No independent audit or independent validation has been performed.
