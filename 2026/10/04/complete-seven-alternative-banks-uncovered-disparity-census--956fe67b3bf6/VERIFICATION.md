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
The embedded `verify_banks_uncovered_first_layer.c` performs a complete exact census of labeled tournaments of orders \(1\) through \(7\).

For each tournament:
- the uncovered set is computed from the covering relation;
- transitivity of every vertex subset is computed by a recursive source-deletion dynamic program;
- the Banks set is obtained from inclusion-maximal transitive subsets;
- the inclusion \(BA(T)\subseteq UC(T)\) is checked.

At order \(7\), every divergent tournament is additionally canonicalized under all \(7!\) permutations of the alternatives.

The verifier confirms:
- zero Banks–uncovered disparities for orders \(1,\ldots,6\);
- \(13440\) disparities among the \(2^{21}\) order-seven tournaments;
- exact probability \(105/16384\);
- strict size-pair counts \(1680,5040,5040,1680\) for \((3,4),(4,5),(5,6),(6,7)\);
- exactly four divergent isomorphism classes;
- class orbit sizes \(1680,5040,5040,1680\), one for each strict size pair.

Compile and run:

`cc -O3 -std=c11 verify_banks_uncovered_first_layer.c -o verify_banks_uncovered_first_layer`

`./verify_banks_uncovered_first_layer`

The output must contain:

`VERIFY_OK`

The embedded `verify_banks_uncovered_canons.py` independently reconstructs the Banks and uncovered sets for the four canonical representatives using direct tournament relations and a separate recursive transitivity implementation.

Run:

`python3 verify_banks_uncovered_canons.py`

Its first output line must be:

`VERIFY_OK`

The computation proves the stated first-layer finite classification only.
