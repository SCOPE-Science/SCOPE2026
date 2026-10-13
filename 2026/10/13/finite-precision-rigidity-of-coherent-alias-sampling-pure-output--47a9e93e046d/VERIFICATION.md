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

The exact arbitrary-size proof is contained in `RESULT.md`. The state is the coherent superposition of \(LB\) input address/random pairs after reversible lookup, comparison and conditional index/alias exchange. Tracing its retained registers gives the Gram sum
\[
\rho=\frac1{LB}\left(\sum_j(B-t_j)|a_j\rangle\langle a_j|+\sum_{a,t}t|v_{a,t}\rangle\langle v_{a,t}|\right).
\]
The proof of the two iff classifications depends on strict \(B-t_j>0\), positive-semidefinite support, and positive flow balance on a finite alias endomap. No exhaustive computation is used as an infinite proof.

The bundled standard-library checker constructs every pretrace branch directly (rather than using the closed formula), traces by retained-register equality, and independently compares the reduced matrix with the theorem. It enumerates small allowed tables, checks the two classifications, the uniform target fidelity, and the non-strict threshold boundary. Run it with `python3 artifacts/verify.py` after extracting that path from the package. Its finite checks corroborate the algebraic theorem only.

Limitations: retaining the specified registers and excluding full-keep values are necessary hypotheses. The result has no implications about the complexity of alternative cleanup circuits or about oracle/inverse use of the complete entangled state.
