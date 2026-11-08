---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

At every n>=3 with labelled W_n, rim with h=0 has x_i(t+1)=x_(i-1)x_(i+1) and with h=1 OR of the neighbors. The symmetric strict-sign energy implies eventual period <=2. Fixed hub supports only two complemented fixed states or, for even n, two alternating-rim two-cycle orbits. For flipping hub, unique h=0 representative must obey 2A>n, 2B<n and no isolated ones in cyclic step-two order. One odd ring or two even parity rings and the three-state transfer trace give exactly the stated N_n; compositions of runs of >=2 ones give coefficient m/r*binom(a-r-1,r-1)binom(m-a-1,r-1). Block concatenations 110/1110 and rho^4=rho+1 prove the exponential lower liminf (not an exact growth rate). Independent direct synchronous-update enumeration gives (fixed,primitive-orbits): n=3..12: (2,3),(2,2),(2,5),(2,11),(2,21),(2,34),(2,66),(2,77),(2,220),(2,227).

## originality

PASS

The period-at-most-two potential theorem, one-dimensional fixed-point counting and finite automata are prior techniques. The particular wheel hub-switch strict inequalities, parity-ring transfer and closed primitive-orbit binomial census are not implied by the inspected broader convergence theorems or published Resultary matches. Priority is best-of-knowledge, not an exhaustive historical exclusion.

## value

PASS

Counts all labelled primitive two-cycle orbits of a natural family where attracting period-two states are abundant but convergence theory alone does not enumerate them. Distinguishes fixed-hub exceptions, odd/even parity and exponential family; a precise infinite graph dynamical invariant likely useful for studying synchronous majority.

The dated certificate retains the supplied scientific assessment, sources and limitations.
