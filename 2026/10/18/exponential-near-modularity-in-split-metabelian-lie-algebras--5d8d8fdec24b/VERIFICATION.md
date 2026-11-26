---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Closure partitions the population into arbitrary subspaces of V and coset lifts of T-invariant X; the polynomial spectral projections give precisely the split product of subspace lattices over every admissible F_q. For a mixed pair, fixing W∩X and the invariant image of W modulo X leaves exactly a graph map into X/(W∩X). For two lifts, the only obstruction is an invariant line spanned by their difference modulo X+Y; the difference map is onto and its kernel has dimension n−dim(X∩Y). This confirms the three terms and both orientations. Independent binary full-subspace and bracket enumeration for (2,2) yields (N0,N1,Q01,Q11)=(67,121,5887,12877), 6204 failures, matching independently evaluated quotient counts (python /workspace/reproduce_frozen.py 1). Uniform Gaussian estimates complete squares, giving N1/N0 of order q^((n−S)/2): the extra q^(r/4) is bounded since r≤q, and S≥n from each complementary dimension being at least two. Mixed bad pairs alone suffice for the lower bound. In a balanced X the mixed-eigenspace covectors give a uniformly positive fraction of quotient hyperplanes; the line choice and graph maps give order q^(dx−1) bad W per lift. With x+d=n and |d−x|≤r, the resulting ratio has the claimed exponent. For lattice nonmodularity, take W=span(u+v)≤V with nonzero u,v from two distinct eigenspaces and H=span(h). Then W∨(H∩V)=W, but (W∨H)∩V contains T(u+v) outside W. This supplies the intended modular-identity witness; nonpermutability alone need not be equated with failure of modularity. The finite replay is only binary; the analytic proof handles extension fields and uniformity only at fixed q.

## originality

PASS

The primary comparison defines the same commutativity degree but gives special cases and general bounds, not the two-or-more split-eigenspace all-subalgebra census with sharp fixed-field multiplicity dependence. The inspected exact-count analogues operate in other regimes. The most plausible two-eigenspace catalogue match is later and was not accessible beyond its summary, so formula-level equivalence there is unresolved. No absolute priority is asserted.

## value

PASS

The statistic is over the full subalgebra lattice and preserves a natural distinction: the lattice fails the modular law but the failure density for pair permutability has a sharp, tunable decay. The exact census and matching exponent for arbitrary split multiplicities give more than isolated low-dimensional calculations or a one-sided estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
