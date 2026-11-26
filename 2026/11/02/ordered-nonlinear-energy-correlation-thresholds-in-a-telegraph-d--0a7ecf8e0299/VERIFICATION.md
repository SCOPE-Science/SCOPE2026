---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Reassessed the corrected RESULT.md. The frozen scope's independence of the initial oscillator state is misleading in a theorem about the stationary joint law and false if imposed there: E[sigma(0) X(0)]=1/(k+u+u^2)>0 though the two means vanish. The repair specifies the autonomous sign chain and the jointly stationary causal convolution, distinguishes transients, and proves existence, boundedness and uniqueness for k>0. It leaves the crossing theorem unchanged. Independently, in coordinates (sigma X,sigma V) the drift is (v,-v-kx+1), and a flip negates both coordinates; a degree-d homogeneous monomial gains the jump term -u(d mod 2). The resulting degree 1–4 systems are invertible for k,u>0. Running python3 /workspace/evidence/2_moments.py reproduced the moments, three numerator polynomials and both exact sign certificates. Even-degree moments of these coordinates are the original even-degree moments. H>0, P_c(6,u)>0, the positive quadratic root is increasing, and its small-u derivative is 477/57=159/19; its leading large-u coefficient is (26+28)/18=3. P_v has one sign variation even when its k^2 coefficient vanishes; P_x has none at u=4/3 and exactly one for larger u, with the indicated signs on either side. The remainder signs at the positive P_c root place it strictly above k_v and strictly below k_x when k_x exists. The energy rescaling preserves sign and all of k<=1/4 lies below k_c. Frozen verify.py was inspected, not executed.

## originality

PASS

Pass for the repaired claim of strict interlacing as a joint all-parameter inequality. The repaired file explicitly credits the published overlapping claims for the three individual frontiers and the known all-order moment machinery. The exact two comparisons on the covariance root curve, not the moment recurrence or the separate existence of any of the three roots, are the supported distinct contribution. No chronology is inferred from same-date records.

## value

PASS

The point is whether sign changes in two marginal fourth cumulants and a mixed energy covariance are simultaneous or occur in distinct intervals. The global strict ordering makes the intervals explicit and gives a useful diagnostic: at the mixed zero the kinetic cumulant is already positive while the position cumulant is still negative. No collection of separate sign diagrams formally decides that comparison without an inequality on the common scaled variables. The sign boundaries are not dynamical phase transitions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
