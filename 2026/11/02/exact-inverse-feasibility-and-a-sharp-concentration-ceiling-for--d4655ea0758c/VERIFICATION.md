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

With columns as senders, the arrival mass is the unique solution u=1+Q(I−D)u, because the induced column norm is less than one. For a target w set u=D⁻¹w; the induced edge flow must have receiver demands r_i=u_i−1 and sender supplies c_j=(1−τ_j)u_j. The total margin difference is Σw_i−n. If w satisfies the stated normalization and lower bounds then r_i≥0 and c_j>0. In the bipartite construction, a cut crossing an allowed internal arc already costs at least C=Σc_j; otherwise, if S denotes receivers on the sink side, all their neighboring senders must also lie there. The cut costs at least c(Γ⁻(S))+r(V∖S)≥C, with that lower bound attained by the minimal sender choice for each S. A C-flow thus exists and division by the positive c_j gives exactly the required stochastic columns and target resolvent, including exact rational witnesses by scaling capacities to integers. A missing outgoing arc at a sender violates the S=V cut. On a complete loopless graph every cut with |S|≥2 is automatic, yielding precisely the box intersected with the normalized hyperplane; singleton cuts give w_i−τ≤(1−τ)(n−w_i). When every other vertex sends only to the hub this inequality is an equality, whatever admissible split the hub uses; the recorded equal split is a valid witness. The bound equals n/2 only at n=2 for τ>0 and tends to n/2 as τ decreases to zero. The disconnected-triangle example has all singleton inequalities, but violates the first component cut by 18/5−33/10=3/10.

## originality

PASS

The strongest inspected comparison, Berend's inverse PageRank, asks a mathematically equivalent common-retention target question when teleportation is uniform, but its stated exact case uses full support with self-transitions and its sparse discussion provides limited obstructions rather than the exact cuts. The frozen result's supported distinct content is the explicit cut characterization and construction for fixed heterogeneous retention on a fixed graph, and the sharp complete-loopless attainable polytope as a consequence. The underlying max-flow criterion itself is classical, and this is not a claim to have originated prescribed PageRank or flow-based delegation.

## value

PASS

An inverse target on a fixed trust graph is a natural design and obstruction question. The exact polytope replaces an apparent nonlinear inverse problem by one flow test that gives either a realizable delegation or a concrete obstructing group. The disconnected example makes the collective limitation real, and the sharp complete-network box quantifies the loss of concentration caused by forbidding self-arcs. The general solution and its witnesses, rather than the short cap derivation in isolation, justify the value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
