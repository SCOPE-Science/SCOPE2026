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

In the edge-seeded unrooted tree C counts all unordered leaf pairs at a common neighbor, not only centers of degree three. Start the leaf drifts at n=3, with (S,X,C)=(6,4,1), where S=sum d² and X=sum d·ell. Attachment at a nonleaf adds ell pairs and d+ell+1 to X; attachment at a leaf loses ell_w-1 pairs at its old neighbor w and changes X by 2-d_w. Degree-weighted averaging gives E[ΔX|T_n]=1+S_n/[2(n-1)] and (n-1)E[C_(n+1)|T_n]=(n-2)C_n+X_n/2. The S drift is E[S_(n+1)|T_n]=nS_n/(n-1)+2; telescoping these three identities from the deterministic starts reproduces the exact finite mean. With U=sum d³, its expected growth recursion has multiplier 1+3/[2(n-1)] and forcing O(log n); dividing by the product of multipliers, of order n^(3/2), gives E U_n=O(n^(3/2)). The martingale increments of M are (2d_selected-S_n/(n-1))/n, with expected square summable via U. The star and path at n=4 are equiprobable and give M_4=±1/3. The centered X-increment's expected square is O(n^(1/2)): contributions at leaves combine by old neighbor and use ell_w≤d_w, as do the nonleaf degree weights. The C-increment innovation multiplied by n-1 has expected square O(n^(5/2)) by the same bound. Dividing these by n and n² respectively gives square-summable martingale series; Kronecker gives the required almost-sure noise control and orthogonality gives L² control. Cesàro first transfers the limit to centered X_n/n as M∞/2; the weighted sum of those centered X values then transfers it to centered C_n/n as M∞/8. The mean contributes γ/4−1/8 after subtracting (log n)/4, and the limiting variance is at least (1/9)/64. Independent exact-rational enumeration checked 17,757 bounded assertions through n=8; replay with /workspace/branches/4ada986c-83c3-4279-8c37-933b0df8664f/spotcheck.py. The source checker was inspected but not run; its recorded 184,947 assertions through n=9 are finite checks, not an infinite proof.

## originality

PASS

Pass for the exact sibling-leaf pair mean and the strong, nonconstant n-scale correction identified with one eighth of the quadratic-degree limit in the specified model. The degree-square statistic (Zagreb index), its exact mean and conditional drift, and degree-moment bounds have substantial antecedents. The centered degree martingale and its L² convergence are readily obtained from those facts and are not credited as a standalone novelty. The inspected prior work does not supply the corresponding transfer to the unbounded sibling statistic.

## value

PASS

This global leaf-pair statistic counts symmetries at all occupied centers and weights hubs quadratically. The result goes beyond an existence result or a density limit: it separates a deterministic n log n leading term from an order-n, genuinely random limit that can be tracked via quadratic degrees, with an exact finite-size expectation. The moment control that transfers fluctuations to this unbounded observable is substantive, and the statistic and scale are naturally motivated by the heavy-tailed leafdegree law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
