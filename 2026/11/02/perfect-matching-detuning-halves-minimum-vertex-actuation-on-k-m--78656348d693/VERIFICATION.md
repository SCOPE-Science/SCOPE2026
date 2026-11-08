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

The weighted graph Laplacian is exactly [[dI,-J-(t-1)I],[-J-(t-1)I,dI]] with d=m-1+t. The orthogonal invariant spaces E0=(c1,c1), Ec=(c1,-c1), E+=(x,x), E-=(x,-x), x·1=0, have eigenvalues 0,2d,m,m-2+2t and dimensions 1,1,m-1,m-1. With m>=2,t>0, the only eigenvalue collision is E+ with E- at t=1. For every nonempty coordinate actuator set, both constant eigenspaces have rank-one nonzero projection. The projections to E± are copies of v_i=e_i-1/m·1 with span dimension min(|T|,m-1); at the collision t=1 side-specific projections instead span independent zero-sum axes. Spectral Lagrange interpolation proves the reachable space equals the sum of distinct-eigenvalue projection ranges (Kalman rank, not just eigenvalue multiplicity). This yields rank=2+min(|A|,m-1)+min(|D|,m-1) at t=1, and 2+2min(|A∪D|,m-1) otherwise; rho(empty)=0. Full-rank min actuator cardinalities 2m-2 vs m-1 and placements m^2 vs m2^(m-1). Independent exact SymPy Kalman matrix ranks covered 999 nonempty sets for m=2..4,t=1,2,1/2; modular verifier read separately. The algebra, rather than finite checks, supports real t>0.

## originality

PASS

General PBH spectral-mode controllability, maximum eigenvalue multiplicity and qualitative zero forcing are prior art. The claimed result is an evaluated all-vertex-placement rank function for one natural dense graph with matched-edge detuning, a singular positive conductance and exact minimum input-set multiplicities. Matched biclique/crown graph aliases and the broad PBH texts were compared; no exact all-placement formula was identified. This is a modest but motivated special-family specialization of well-known linear algebra, qualified against specialized controllability catalogues.

## value

PASS

A natural matched-edge perturbation of a maximally symmetric control network has a sharp exactly-one-parameter controllability phase boundary. Every site subset has a closed Kalman-rank formula, optimal-actuator count falls by half (2m−2 to m−1) away from t=1, and all minimum placements are enumerated. This is a reusable graph-specific control-design invariant, notwithstanding known general PBH methods; it makes no unsupported robustness/energy claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
