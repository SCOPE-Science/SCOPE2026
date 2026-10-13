---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification
The analytic proof has four critical checks.

1. **Support propagation.** In one edge-local layer, every site newly entering the Heisenberg support is adjacent to the previous support. Induction confines \(UZ_vU^\dagger\) to \(B_G(v,L)\).
2. **Projector factorization.** The Pauli sum defining the fourth-order Clifford projector factors over any qubit bipartition, not only a contiguous one-dimensional cut.
3. **Exact target count.** Uniform Clifford conjugation sends a fixed nonidentity Pauli uniformly over the \(4^n-1\) nonidentity Pauli classes. Exactly \(4^s-1\) are supported inside a chosen \(s\)-qubit graph ball.
4. **Threshold inversion.** Diamond distance at most \(\varepsilon\) forces \(4^{b_G(L)}\ge1+(1-\varepsilon)(4^n-1)\). For \(\varepsilon<3/4\), this quantity is strictly larger than \(4^{n-1}\), so the integer ball size is \(n\), for every center, and \(L\ge\operatorname{diam}(G)\).

The accompanying checker confirms the algebraic inversion and representative finite graph specializations. Those computations are sanity checks only; the all-graph statement follows from the analytic support and counting proof.

No independent audit has been performed, and no claim is made that the graph-diameter lower bound is tight on arbitrary architectures.
