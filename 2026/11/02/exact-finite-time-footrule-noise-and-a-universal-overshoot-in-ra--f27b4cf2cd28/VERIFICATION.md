---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The one-card permutation representation yields E F_t=(n²-1)(1-a^t)/3 with a=1-2/n. F² lies in the ordered-pair matrix-coefficient module, decomposed as trivial, standard, [n-2,2], [n-2,1,1] with eigenvalues 1,a,a²,c (c=1-4/n). Uniform second moment and exact one- and two-step squared displacement determine the three coefficients algebraically; direct gap-sum identities for 3-cycles/disjoint transpositions are polynomial and were independently checked. Then variance = v+4(n²-1)(n+2)a^t/45 -(n+1)(3n³+9n²-4n+10)a^(2t)/90 +(n²-1)(n²-4)c^t/30. Positive slow mode dominates c and a², proving overshoot. Expansion c/a²=1-4/(n-2)² at t=floor(sn/2) cancels n⁴ terms and gives V(s)=[2+4e^-s-(6+3s)e^-2s]/45; V derivative has unique positive root 4e^s=9+6s. Independent finite transition laws verified n4..6 without assuming the mode formula.

## originality

PASS

Best-of-knowledge qualification: specific evaluated claim is not implied by inspected stronger statements or prior tables. Negative search is not itself proof of novelty. The old theorems support premises (chain eigenvalues, stationary moment), while the computed transient mode coefficients and overshoot are additional mathematical work.

## value

PASS

The exact transient variance of an established ranking-disorder statistic reveals a large nonmonotone noise overshoot at times linear in deck size, distinct from stationary variance and global total-variation cutoff. The universal peak and explicit relaxation-mode coefficients are useful observables in stochastic equilibration, not merely applying a standard spectral gap bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
