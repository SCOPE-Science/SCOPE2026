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

# Verification and limits

The proof reduces the colouring condition at a cell to the exact identity \(2(u_c+\epsilon_i)\ge a+\delta_i\), with every symbol defined in RESULT.md. The row-colour lemma and the consequences of having three row-colours are checked symbolically there, covering arbitrary \(n\ge1\). The four-colour structural theorem is both necessary and sufficient, and the multinomial count accounts for the factor of four from swapping named colours within either layer.

Run `python3 verify.py` from the file directory. The code enumerates every partial set partition for the labelled graphs of orders \(2n\), \(1\le n\le5\), using zero for the uncoloured vertices and canonical positive labels for colour classes. Its neighbourhood checker builds all clique and matching edges directly; it does not assume the classification in the proof. The observed maxima are \(2,2,3,4,4\). The numbers of unlabelled four-colour optimizers at \(n=4,5\) are \(6,30\), corresponding to \(144,720\) four-colour assignments with a palette of four named colours. Explicit four-colour assignments are additionally checked for all \(4\le n\le44\).

Finite enumeration does not establish statements for arbitrary orders, and no independent mathematical audit or independent external certification is claimed. The newest revision's complete text was not accessible for full bibliographic priority comparison; publication priority is not certified.
