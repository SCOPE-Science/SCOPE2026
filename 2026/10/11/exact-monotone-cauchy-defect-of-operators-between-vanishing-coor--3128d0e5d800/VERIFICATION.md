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
# Analytic verification and limits

The proof was checked directly for arbitrary possibly uncountable coordinate index sets. The row functional exists in \(\ell_1(\Gamma)\) and each column belongs to \(c_0(\Lambda)\). The sharp upper bound uses \(0\le x_m-x_n\le\mathbf{1}\) coordinatewise, not an unjustified bound on signed test vectors. The lower bound requires infinitely many rows exceeding every finite-output tail threshold and chooses their maximizing-sign coordinate sets outside the previously selected finite support. Columnwise vanishing makes the old-coordinate contribution smaller than any prescribed error. The resulting single increasing sequence has a nonzero Cauchy tail diameter for every tail, even when the two index sets are uncountable.

The essential-norm equality follows from finite-output truncation and uniform coordinate tails of compact images. For the identity, the row masses are \((1,0)\) and the defect equals the essential norm. For the operator \((Ux)_n=(x_{2n-1}-x_{2n})/2\), the two masses are \((1/2,1/2)\), so the defect is exactly half its essential norm. These are infinite-dimensional symbolic checks, not numerical experiments.

Order Cauchy in a target \(c_0\) implies norm Cauchy because a single lattice regulator controls all but finitely many coordinates and later regulators control those finitely many. Conversely, compactness provides a vanishing row-norm envelope that turns coordinatewise convergence of bounded increasing nets into norm and order convergence. The results do not imply any analogous statement for arbitrary Banach lattices, and absence of equivalent prior work has not been independently certified.
