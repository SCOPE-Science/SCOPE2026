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

The proof reduces the new step to a one-variable extension lemma for a strengthened relation on evaluations \(v:\{x,y,z\}\to C_4\) and \(w:\{x,y,z\}\to C_n\). Besides matching equality and adjacency, every opposite pair in \(C_4\) is required to map to a pair at cycle distance exactly \(2\) in \(C_n\).

The bundled `verify.py` performs three checks.

First, for every \(5\le n\le16\), it exhaustively enumerates all three-variable assignments into \(C_4\) and \(C_n\), retains every tight-alike pair, and verifies that every possible rebinding of every variable in \(C_4\) has a response in \(C_n\) preserving the invariant.

Second, it checks the three canonical configurations of the two fixed values—equal, adjacent, opposite—for every \(5\le n\le1000\). These are exactly the three cases used in the uniform symbolic proof.

Third, it checks that the strictness sentence
\[
\eta=\forall x\forall y\forall z(\neg Rxy\lor x=z\lor y=z\lor Rxz\lor Ryz)
\]
holds on \(C_4\) and fails on every tested longer cycle, with the explicit witness \((0,1,3)\).

Output retained in the original submission:

`VERIFY_OK 217057 exact assertions`

The checker is not an independent audit and the finite range is not used to extrapolate the theorem. The all-\(n\) claim follows from the three-case symbolic extension argument in RESULT.md.

A separately reconstructed finite check reproduced the same 217057 assertion count without executing the uploaded checker. This is finite corroboration, not an independent audit, and does not prove the all-n theorem.
