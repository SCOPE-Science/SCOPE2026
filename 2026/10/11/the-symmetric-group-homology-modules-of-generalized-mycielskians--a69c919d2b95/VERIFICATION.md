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

# Verification and scope

The formula is proved for all integers \(n\ge2\) and \(\ell\ge0\) in `RESULT.md`. The proof uses a genuinely equivariant simultaneous fold, a two-simplex-plus-bridges model for \(\operatorname{Ind}(K_n\times P_2)\), the join Künneth isomorphism and the apex Mayer–Vietoris sequence. The only representation splitting invokes Maschke over \(\mathbb Q\); no integral splitting or equivariant wedge splitting is certified.

## Actual finite checks

Run `python3 verify.py` with Python 3 and only its standard library. The file directly constructs the graph using the explicit edge definition, obtains exact independence complex faces, checks the simultaneous fold neighborhood inclusions, evaluates the permutation-invariant independence polynomial at \(-1\) by an orbit graph recurrence for the signed Lefschetz trace, and independently enumerates direct oriented-face traces. For bounded small cases it computes mod-two reduced homology from explicit boundary ranks, retaining the empty simplex in the augmented chain complex. A successful run prints:

`VERIFY_OK folds=76 orbit_characters=1144 direct_traces=112 mod2_homology_cases=16`

Fold tests cover \(2\le n\le5\) and up to \(\ell=10,10,8,6\), respectively. The 1,144 character checks cover every coordinate permutation for these ranges, and 112 direct signed simplicial traces provide a second enumeration. Exact mod-two homology is computed for 16 small cases with \(n\le4\). These tests are finite corroboration, not the basis for the universal homology theorem or the rational representation isomorphisms.

## Review boundary

The lead first public source is arXiv:2601.13432v1 (2026-01-19); the 2019 complete-graph source is historical support only. The mathematical comparison concerns the full rational \(S_n\) action, not merely sphere multiplicity. Other unpublished or unindexed equivalent work remains possible. Independent audit has not been performed.
