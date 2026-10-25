---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Reconstructed the recursive block-deletion encoding on S_n=[1,n-1]. For any block B containing n-1, C=S_n\B, m=|C|+1, recursively construct the top m-element algebra, adjoin x_m as a new smallest invariant, and use strictly increasing row-output indices b in B\{n-1} in the UNIQUE published extension formula. Inverting via the maximal non-unit invariant m, its strict row-output set A and compressed top algebra proves a bijection for all n by induction. Every appended block adds exactly one non-unit invariant; Properzi–Qin Theorem 4.3 makes its upper-set a distinct proper nonempty ideal. Thus the ideal histogram is S(n-1,k), including n=1 and k=0. The source verify.py actual recursion, L-cycloid check, direct raw-table comparison n<=5, ideal-axiom subset enumeration n<=6 and partition tests n<=8 were read; these bounded scripts are corroboration, not the universal proof. Essential published hypotheses and extension lemma were checked in Dietzel–Menchón–Vendramin Prop4.4/Theorem4.5 and ideal theorem in Properzi–Qin.

## originality

PASS

Best-of-knowledge PASS for the fully specified inverse partition code and resulting Stirling ideal distribution, not for the established Bell B_(n-1) count, chain extension/decomposition, or the known ideal/invariant classification. Published Problem4.6 explicitly asks for a partition code but prints the inconsistent n labels; this resolves the cardinality-consistent n-1-label question only. Rump is plausible inaccessible overlap; recorded rather than assumed disproven.

## value

PASS

A natural explicit coding addresses a published combinatorial enumeration problem and refines the classification by a structurally meaningful algebraic invariant: number of proper ideals, with full Stirling law. Researchers can reconstruct multiplication tables and separate ideal strata; this is not an arbitrary statistic or a retelling of the known Bell count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
