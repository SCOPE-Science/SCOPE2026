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

The proof is analytic. The exact published band inequality is first normalized, giving the leading periodic term \(2\sin(kL_2)\sin(kL_3)\) plus a uniform \(O(k^{-2})\) remainder. For rational arc ratios, zeros of the leading term have multiplicity at most two, so the lower-order remainder can change the band indicator only on an energy-weighted set of relative measure tending to zero.

The remaining density is an exact square-wave correlation. Coprimality forces common odd Fourier harmonics to be absent when one of \(p,q\) is even and to occur precisely at odd multiples of \(pq\) when both are odd, yielding correlation \(0\) or \(1/(pq)\), respectively.

`verify_density.py` was executed from the packaged path. It exactly checks the one-period sign measure for every coprime \(1\le p,q\le25\) using rational breakpoints, and numerically checks representative convergence of the full exact band inequality. The finite computation is corroborative and is not used to infer the all-parameter theorem.
