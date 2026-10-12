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

# Reproduction and verified scope

The claim is \(\mathcal R(K_3\square K_n)=4\) for every integer \(n\ge4\). The only exhaustive obstruction required is the \(12\)-vertex graph \(K_3\square K_4\). A three-uniform candidate has \(36\) occurrences; normalization by cyclic rotation and column relabeling is proved in `RESULT.md`.

Compile `verify_interval_merge.cpp` and `verify_mask_automaton.cpp` independently with `g++ -O3 -std=c++17`. Each constructs the complete two-row candidate space, then tests every compatible merge. The first uses recursive row interleavings and explicit terminal pair tests; the second uses bitmask placement and incremental pair-alternation states. The attached outputs were generated from those exact source files.

The first result has \(354\) surviving two-row projections and \(158,483,130\) fully examined merges; the second independently confirms \(354\) projections and leaves \(238,188\) merges satisfying all four required cross-row matching alternations. Both find zero complete representations. `verify_upper.py` constructs four-uniform words for sizes \(2\) through \(10\); the universal upper bound uses the proven Cartesian-product construction of Broere--Zantema [2], not finite extrapolation.

All outcomes are exact integer counts. There are no random seeds, floating-point tolerances, network dependencies, search timeouts, or unpublished auxiliary certificates. C++17 and Python 3 standard libraries suffice. No expert or independently conducted audit is asserted.
