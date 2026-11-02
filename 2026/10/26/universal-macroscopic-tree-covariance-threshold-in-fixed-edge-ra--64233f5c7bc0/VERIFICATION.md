---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For uniform G(n,m) with n>=r+3, 3<=k<=n-r, k-1<=m<=P=C(n-r,2), the exact chance of specified e=k-1 tree edges is (m)_e/(N)_e; conditioning on an ordered r-tuple of isolated vertices yields uniform G(n-r,m). Dividing the exact mixed moment by positive marginal expectations proves R(n,r,k)=((n-k)_r/(n)_r)*((N)_{k-1}/(P)_{k-1}), independent of tree automorphisms, shape and edge count m. Direct cancellation gives adjacent ratio (n-k-r)/(n-k)*(N-k+1)/(P-k+1), whose comparison with 1 has numerator (r/2)[n²-nr-2-k(2n-r-3)], decreasing in k; R(2)=1 and R(3)>1, giving the one-positive-block, optional zero, terminal-negative finite classification. For fixed r and k/n=x in compact interior, logarithmic expansion of the two products gives r[log(1-x)+2x]+(r/n)[-2+(r+1)x+2x²-(r-1)x/(2(1-x))]+O_r(n^-2), whence rho solves (1-rho)e^(2rho)=1, rho=0.796812130020..., with unique interpolated branch crossing rho*n+kappa_r+O_r(n^-1). Independent-edge conditioning drops the hypergeometric factor and leaves a strictly negative normalized covariance. Independently enumerated all 32,768 labeled simple n=6 graphs, built distinct path/star edge masks, and checked 52 exact Fraction mixed-moment cases across admissible m,k,r. Analytic count and expansion, not the finite enumeration, prove the entire theorem.

## originality

PASS

Best-of-knowledge PASS for the exact all-m, all-shapes mixed factorial isolate/tree ratio, finite unimodality sign law and sharp macroscopic threshold with order-one correction. The hypergeometric edge-inclusion probability and subgraph expectation are standard and explicitly credited; older random-graph fluctuation and upper-tail papers were compared by mathematical statements, not titles. The threshold is not covered by fixed-small-subgraph CLTs or upper-tail bounds for rooted fixed graphs. Earlier general mixed factorial moment formulas may imply the ratio with an extra asymptotic calculation; genuine priority risk remains.

## value

PASS

The universal m-independent, tree-shape-independent covariance sign is a structural property of sampling graphs with exactly m edges. Unlike a routine fixed-motif expectation, it has a nontrivial sign transition for macroscopic tree size near rho*n≈0.7968n, a sharp order-one finite-size correction, and a contrasting strictly negative independent-edge ensemble. Such an exact dependence classification is a natural useful invariant for large subgraph statistics and conditioning effects, even without a separate downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
