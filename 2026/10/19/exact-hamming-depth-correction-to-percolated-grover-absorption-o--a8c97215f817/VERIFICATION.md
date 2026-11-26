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

The sink projection acts on all arcs originating at 0; it does not change the local d-dimensional coin before the sink is applied. The trapped states have symmetric edge amplitudes and zero vertex sums; amplitudes on sink edges vanish. Switching the sign of one bipartition turns this into signed-incidence conservation on the punctured cube. Duplicated arc amplitudes give the factor 1/2 for projection of one initial arc, and the complementary incidence projection has diagonal R_H(e). As an independent check of the infinite-time reduction, a nonzero limiting surviving trace in the complement would give a positive fixed operator there by Cesàro averaging. Trace equality makes each full-support unitary image sink-free; Hilbert–Schmidt strict convexity then makes the fixed operator invariant under every unitary. Its support is invariant under the empty-configuration coin and each single-edge swap. Any antisymmetric edge component would therefore give an antisymmetric edge basis vector in the support, and applying the coin propagates such components to adjacent edges and ultimately to a sink edge, a contradiction. In the symmetric sector the coin's +1 mode is globally constant and excluded by the sink; its −1 modes are exactly the zero-sum trapped states. Both coin/shift orders have the same dark subspace and asymptotic projection. For the electrical step, L_H is the Kron-reduced cube Laplacian minus the zero-sum neighbor projector P. Coordinate symmetry gives PL_K^+P=κP with κ=g(0)−g(2)=B_1+B_2=(1−2^{1−d})/(d−1)<1. The inverse update contributes ||PL_K^+b||²/(1−κ); taking the Green differences on the three classes of sink neighbors and subtracting their arithmetic mean, B_{k+1} by harmonicity at the sink, gives exactly the three displayed squares. At k=d−1 the last class is empty. The beta integral gives B_h∼(h−1)!d^{−h} with relative O_h(1/d), so for fixed k only the first square contributes at order d^{−2k}. All nine exact grounded-resistance comparisons for d=3,4,5 agreed, and a fresh Q3 channel check distinguished the finite-time step orders but gave the same t=600 survival 0.15 in both.

## originality

PASS

Only the explicit shell-resolved single-vertex-deletion resistance and its fixed-depth absorption correction pass as distinct. The trapping theorem, full-cube resistance and electrical method are antecedents; the closest indexed comparisons address different graph objects or remove different elements and compute a different statistic.

## value

PASS

A vertex sink breaks edge transitivity. An exact closed law by Hamming depth both quantifies this symmetry breaking and predicts how far the sink-induced change penetrates: moving the initial arc one fixed shell outward raises the decay exponent by two powers of dimension. The general transport theorem alone does not distinguish these experimentally or mathematically natural initial arcs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
