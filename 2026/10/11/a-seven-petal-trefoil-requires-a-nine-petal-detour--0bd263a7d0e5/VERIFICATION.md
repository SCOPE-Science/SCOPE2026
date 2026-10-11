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

The lower bound and the explicit detour were replayed from the standalone file `artifacts/verify_trefoil_excess.py`. The program uses only exact permutation, set, and integer operations.

For the candidate \(p=(0,2,4,6,1,3,5)\), it checks all \(70\) admissible parameter triples \((b,m,w)\) for the crossing-exchange definition and finds none legal. It separately checks that \(\mathsf R\) and \(\mathsf S\) return the same canonical cyclic word and that no trivial deletion is available. Therefore no sequence confined to seven petals can leave the candidate or reach five petals.

The program then verifies the explicit path through nine petals. The crossing exchange \(\mathsf X(4,2,5)\) is checked against the pair partition and interval condition, and the surrounding addition/deletions are checked by applying the exact inverse deletion rule. The terminal five-petal word is confirmed cyclically equivalent to \((3,1,4,2,0)\), the trefoil word recorded in the primary source.

Finally, it enumerates the two cyclic classes of three-petal words and verifies that each deletes to the one-petal unknot. Together with the displayed five-petal trefoil, this proves \(p(K)=5\) without relying on a database lookup.

Successful replay output:

`VERIFY_OK candidate_x_triples=70 candidate_R=fixed candidate_S=fixed candidate_Tminus=none detour_max_petals=9 trefoil_petals=5 source_X_example=PASS`

No conclusion is drawn for other seven-petal words or other knots. Independent audit has not been performed.
