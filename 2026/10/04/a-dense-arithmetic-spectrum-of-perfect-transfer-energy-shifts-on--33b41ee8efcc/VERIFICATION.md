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

The proof was reconstructed from the exact three-state symmetry reduction of the shifted complete graph. The critical checks are the leakage condition
\[
\sin(\alpha t/2)=0
\]
and the residual phase congruence
\[
e^{-i\pi k\beta}=(-1)^{k+1}.
\]
Reducing \(\beta=p/q\) proves the opposite-parity criterion and the complete set of transfer times.

`verify_complete_graph_shifts.py` independently evaluates the closed shift parametrization for many graph orders and reduced rational parameters, reconstructs the reduced Hamiltonian evolution at the predicted minimum transfer time, and checks unit transfer with vanishing leakage. It also checks reduced same-parity examples that fail the phase condition at every leakage-free time in the tested range. The replay prints `VERIFY_OK`.

The finite replay is supplementary; the all-parameter theorem is supplied by the exact algebraic proof in `RESULT.md`. The direct source and the closest weighted-join generalization were inspected in full text. No independent audit has been performed.
