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

The claim was checked from definitions rather than from numerical experiments.

For the arbitrary imprimitivity bimodule, the verification consists of two order calculations. First, \(\langle z,z\rangle_B\le\|z\|_Z^2 1_B\) and positivity of \(\tau\) give the stated upper bound. Second, an identity frame has positive summands totaling \(1_B\), hence each frame vector has module norm at most one; applying \(\tau\) to the sum gives total localization energy exactly \(\tau(1_B)\), so at least one vector witnesses the lower operator-norm bound.

For \(M_{r,s}(\mathbb C)\), the right module norm was independently reduced to matrix operator norm and the localization norm to \(\sqrt c\) times Hilbert--Schmidt norm. The extremal singular-value configuration has exactly \(\min\{r,s\}\) singular values equal to one, giving the exact embedding norm. The lower bound on Parseval-frame length follows because each positive matrix \(X_i^*X_i\) has rank at most \(r\); the matching construction partitions \(\mathbb C^s\) into blocks of dimension at most \(r\) and uses partial isometries with those initial projections.

Checked limits: \(r\ge s\) gives one frame element and equality in the universal upper bound; \(r<s\) gives \(\lceil s/r\rceil\) frame elements. Multiplying the trace by \(c>0\) scales squared localization norms by \(c\) and leaves frame length unchanged, exactly as the formulas require.

No converse outside the rectangular matrix family, no treatment of unbounded traces, and no independent audit are claimed.
