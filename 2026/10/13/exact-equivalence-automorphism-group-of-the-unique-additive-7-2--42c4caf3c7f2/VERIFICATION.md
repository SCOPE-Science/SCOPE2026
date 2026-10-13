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
`artifacts/verify.py` reconstructs the additive code over \(\mathbb F_4\) from the five rows printed in the primary source. It checks that the code has \(32\) words and weight distribution \(1+21z^5+7z^6+3z^7\).

It then verifies that the \(21\) weight-\(5\) words have all \(21\) unordered coordinate pairs as their zero sets and that every nonzero field symbol occurs in every coordinate among those minimum words.

For each of the \(7!=5040\) coordinate permutations, the verifier uses zero-pair uniqueness to force all seven local nonzero-symbol permutations, rejects inconsistent candidates, and directly checks every surviving transformation against all \(32\) codewords. Exactly \(21\) full source-equivalence automorphisms survive. Requiring all local maps to be the identity leaves exactly \(7\) coordinate permutations.

The projected \(21\)-element set is checked for closure and has element-order census \(1^1,3^{14},7^6\). These exhaustive finite checks establish the claimed order and nonabelian \(C_7\rtimes C_3\) structure. No random sampling, floating-point arithmetic, timeout inference, or external algebra system is used.
