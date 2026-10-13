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

The defining PDF was inspected at Eq. (9), where the functional is the average one-particle entropy if all partial entropies are nonzero and is zero otherwise. The surrounding text identifies a zero partial entropy with partial factorization. Eq. (13) was also inspected for the three-term example used as an explicit boundary path.

The proof was checked directly in finite dimension. For each bipartition, product pure states are the rank-one coefficient-flattening locus cut out by all 2-by-2 minors; it is a proper closed set with empty interior. Their finite union is therefore closed and nowhere dense, so genuine states form an open dense set. The average one-qubit entropy is continuous. These facts establish the complete continuity classification without numerical sampling.

For three qubits, any biseparable pure state has one pure isolated qubit and a two-qubit pure factor, so its average one-qubit entropy is at most two thirds. The bound is attained by a Bell pair times a pure qubit. For four or more qubits, a Bell pair tensored with a GHZ state on the remaining qubits is biseparable while every one-qubit marginal is maximally mixed, attaining jump one.

No claim is made about mixed-state extensions or about LOCC monotonicity beyond what follows from the displayed continuity argument. The later 2007 comparison paper was identified but not available in full text, and remains an originality risk.
