---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Reconstructed Lagrange-inversion cherry polynomial A_m(j)=binom(m,j) binom(m-j,j-1) 2^(m-2j+1)/m from F=1+z(F^2+u-1). Conditioned root split gives independent Z_k+Z_(n-1-k). Remy uniform vertex insertion coupling ensures Z_m<=st Z_(m+1)<=st Z_m+1, proving Y(n,0)<=stY(n,1) and Y(n,2)<=stY(n,1). Exact cherry mean f(m)=m(m+1)/(2(2m-1)); strictly increasing increments for m>=2 imply E[Y(n,2)]>E[Y(n,3)] when n>=7. Odd n shows larger max support for k3; even n yields top-point probability ratio (2n-7)/5>1; both directions of stochastic dominance fail for all n>=7. For n<7 no unclassified inward move exists. Independently computed cherry polynomials via recursive tree split through n=23 and explicitly verified n7 distributions (16,12)/28 and (16,8,1)/25.

## originality

PASS

Best-of-knowledge sharp conditional stochastic-order boundary rather than established Catalan cherry enumeration or conditional mean regression. Janson covers uniform full binary/conditioned Galton-Watson trees, Konvalinka–Wagner studies cherry counts in tanglegrams and branch statistics, Remy supplies only uniform growth coupling. No inspected direct theorem forces seven-node stochastic incomparability and the all-size parity top-tail reversal.

## value

PASS

Natural exact boundary in conditional tree-shape statistics, distinguishing mean monotonicity from full stochastic order and exhibiting a sharp smallest structural obstruction with all-size proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
