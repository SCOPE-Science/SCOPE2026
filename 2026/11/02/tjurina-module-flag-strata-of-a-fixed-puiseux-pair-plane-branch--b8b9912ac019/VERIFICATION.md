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

With weights (m,n), each perturbing term is higher than mn by m(i−1)+1. Substitution x=t^m, y=t^nY gives simple leading roots Y^m=1; the t↦ζt action is transitive on them because gcd(m,n)=1, giving one branch with the stated pair and semigroup. The initial partial derivatives are the coprime pure powers x^(n−1), y^(m−1), giving Milnor colength (m−1)(n−1). For nonzero parameters the weighted Euler remainder is x^v y times a unit, and xf_x then forces x^n into the ideal. Conversely f belongs to (f_x,f_y,x^n) by eliminating y^m and using that xf_x forces x^v y modulo x^n. In the free monic quotient over R/(x^n), the remaining generator is g=x^(v−1)y−c x^(n−1) with c=n/(v a_j); multiplying by x^(n−v) yields x^(n−1)y. Its products by y through y^(m−2) give precisely the extra relations killing x^(v−1)y^k, 2≤k≤m−2. The last reduced product adds no scalar relation since x^(v−1)h is divisible by x^(2v−1) and 2v−1≥n. These products span the whole ideal over R/(x^n), and replacing y by y−c x^(n−v) diagonalizes the module. The stated length and x-adic dimensions follow. At the central point the ideal is (x^(n−1),y^(m−1)); otherwise the defects are positive and pairwise distinct, giving the flag and the quasihomogeneity conclusion by the Milnor–Tjurina criterion. An independently written rational Gröbner check for f=y^5−x^11+x^10y gave leading monomials y^4,x^9y,x^11, colength 38 and the stated profile for that case.

## originality

PASS

The checked general classifications give fixed-principal-part and fixed-Puiseux-pair frameworks, not the explicit module over the fixed x-projection or the first-nonzero-coefficient formula on this slice. The supported distinct result is the exact full coefficient flag and the module, not the existence of Tjurina strata in general, an analytic classification, or a priority claim.

## value

PASS

The semiweighted homogeneous slice varies a natural band of higher terms linear in y while preserving the singularity's topological data. It gives a usable closed formula for every allowed complex coefficient choice, not just a generic or individual Tjurina number. The fixed-projection module strengthens the scalar defect, determines the complete x-adic profile, and detects a positive defect even for the endpoint perturbation lying in the central Jacobian ideal. The resulting coordinate flag describes concrete jumps within a single equisingular family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
