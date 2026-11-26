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

The four edge orbits are exhaustive (within F, F to H, c to H, within H; the last is absent for h=1). For a unit dipole, the row is the gradient of its Laplacian potential. With c grounded for F-to-H injection, the sums of potentials on F and H are 1/h and 0 respectively; for c-to-H injection they are both zero with potential 1/h at c. Substituting verifies the displayed solutions. Summing edge differences by type gives, with n=r+h+1, R_A=2(n-2)/(n-1), R_D=2(n-1)/n, R_B=1+(r-1)/(n-1)+(h-1)/n+2(h-1)/(hn), and R_C=1+(h-1)/n+2r(h-1)/(hn). Their differences give exactly the three stated norm branches and maximizing edge types. A row-sign vector attains the value. The first two branches are below two; the third exceeds it exactly when rh>2(r+h). For n<=9 the product is at most (r+h)^2/4<=2(r+h); for n=10 the (5,4) case gives 41/20, and h=4 gives amplification above two at every larger n as well. The difference of successive third-branch values is [2(n-1)/(h(h+1))-1]/n, giving the weak inequalities for the optimizing integer, including ties. All such integers are in the admissible h range for n>=10. This implies h=sqrt(2(n-1))+O(1), the sharp first-order deficit, and a supremum of three not attained.

## originality

PASS

General graph Hodge/transfer-current theory is credited. No matching prior norm, orbit classification, ten-vertex cutoff or fixed-order optimizer was found on the available evidence. A later exact result on the identical deleted-star family has a different invariant. Same-date general projection bounds were checked against the exact claims rather than excluded on date alone.

## value

PASS

A clique plus one partially connected vertex is a natural defect in a dense network. This result finds when the defect alone causes more than twofold amplification of bounded edge errors, proves a sharp smallest order, and shows that the worst attachment at fixed order is sublinear of scale sqrt(2n), not a constant degree or a fixed fraction of the clique. The change of the norming output from clique edges to the attached edges identifies where errors amplify most.

The dated certificate retains the supplied scientific assessment, sources and limitations.
