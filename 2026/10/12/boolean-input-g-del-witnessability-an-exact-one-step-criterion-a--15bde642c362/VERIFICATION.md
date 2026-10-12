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
# Verification scope and reproducibility

The mathematics is based on the explicit Gödel modal clauses and a symbolic proof. Under Boolean atomic valuations, a nonempty set of positive accessibility grades without a largest member can be selected exactly by an atom, forcing failure of diamond attainment. Conversely, a Boolean modal-free formula has Boolean truth value, so an attained box infimum is automatic; reverse well-ordering of every positive row-grade set makes every depth-one diamond supremum attained. Both directions quantify over all worlds and all Boolean atomic valuations.

The countable counterexample has root grade-one edges to first-layer nodes, and one edge of grade \(1/(n+1)\) from the \(n\)-th first-layer node to its terminal node. All other edges are zero. Each positive row has one distinct grade, but the root outer-box terms for \(\Box\Diamond p\) form a positive sequence converging to zero, with none equal to zero. The negative claim is a direct symbolic infinite proof; neither truncation nor a timeout demonstrates nonattainment.

The standalone standard-library script `verify.py` was run with Python 3 and completed successfully, outputting `VERIFY_OK`. It checks exact-rational evaluations for nine finite restrictions with branch counts 1, 2, 3, 4, 8, 16, 32, 64, and 128, and confirms the finite values \(1/(N+1)\). It also checks increasing-grade subsets for the converse stress case. Finite restrictions are necessarily witnessed and satisfy the witness axiom: this is consistent with the genuine countably infinite failure. The script is not a proof checker and provides no infinite completeness certificate.
