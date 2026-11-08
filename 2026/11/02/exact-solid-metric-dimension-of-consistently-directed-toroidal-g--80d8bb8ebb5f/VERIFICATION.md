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

For any m,n≥3 the forward distance on Z_m×Z_n is d((a,b),(i,j))=(i−a mod m)+(j−b mod n). Solid resolution is the two-sided ordered-pair strict distance condition. Assume m≤n. Pairs (i,j) versus (i,j−1) force at least one landmark in each y-row, |S|≥n. Comparing p=(a−1,j) and q=(a,j−1), d(s,q)−d(s,p) is 0,−m,n,n−m depending on x=a and y=j; resolving q from p forces x=a,y≠j, hence at least two y-locations in every x-column, |S|≥2m. For sufficiency an expanding S occupies all rows and each k-column proper cyclic interval intersects at least k+1 distinct y-rows. Modular difference formula d(s,v)−d(s,u)=Δ+δ−m 1_{X+Δ≥m}−n 1_{Y+δ≥n} resolves all ordered pairs: if Δ+δ≤m, at most δ forbidden rows in an interval of m−Δ columns, so one unobstructed landmark; other cases by a chosen row/column. Explicit S={(j mod m,j)} for n≥2m and diagonal+second-row families for m≤n<2m attain max(n,2m). Coordinate swap handles all. Endpoint n=m included. Note no forced vertices by translation and β<mn.

## originality

PASS

Best-of-knowledge originality is a statement/implication comparison, not a title-match test. The exact established object, parameters, finite tables and known stronger results were cross-checked against published Resultary findings and primary literature; no decisive prior coverage of the final claim was established. Highly plausible inaccessible sources and indirect possible corollaries are disclosed in residual_risks. Searches alone are not novel proof.

## value

PASS

This exact formula settles the canonical source-free strongly connected directed Cartesian cycle products, a family not handled by source-forcing landmark arguments. Interval-expansion constructions and simultaneous n and 2m lower obstructions are mathematically motivated and may serve as a base case for higher directed products.

The dated certificate retains the supplied scientific assessment, sources and limitations.
