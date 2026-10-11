---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reversibility yields \(r_k=\int\lambda^k\nu(d\lambda)\), so pairing gives the pushforward moment measure \(G\) immediately. On each \(x<1\), writing positive and negative branch masses at \(\pm\sqrt{x}\) turns the single equation \(G=(1+\sqrt{x})\alpha+(1-\sqrt{x})\beta\) into the measurable splitting parameter \(\eta\). The +1 atom is fixed by \(G(\{1\})/2\), while -1 is invisible and receives the residual normalization mass. The total mass functional is minimized by the positive branch, yielding the exact compatibility inequality. Equality of that minimum forces uniqueness; otherwise positive slack plus mass in \((0,1)\) permits a nontrivial branch perturbation. The explicit two spectral measures were independently recomputed: they have the same paired moments and normalized asymptotic variance but different \(r_2,r_3\) and three-step variances. The finite-support product of symmetric two-state kernels realizes each required eigenvalue with a reversible eigenfunction.

## originality

PASS

Berg--Song prove the forward spectral-moment representation for the full reversible autocovariance sequence and the Hausdorff-moment representation for Geyer's paired sequence, but the inspected proposition does not invert the weighted squaring map, characterize identifiability, or construct exact finite-state aliasing examples. Geyer's original work introduces the paired sequence and its shape properties. Targeted Resultary search found no prior inverse-fiber theorem. The audited result therefore adds the exact information-loss classification rather than restating the forward moment representation.

## value

PASS

Paired autocovariances are a standard device in reversible-chain variance estimation, so knowing exactly what the complete paired sequence forgets is a natural identifiability question. The theorem gives the full fiber and a sharp uniqueness test, then demonstrates that the ambiguity persists in finite irreducible aperiodic chains and changes finite-horizon behavior even when asymptotic variance is identical.

The dated certificate retains the supplied scientific assessment, sources and limitations.
