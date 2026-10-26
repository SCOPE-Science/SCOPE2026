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

# Computational cross-checks

Run `python verify_cycle_squarezero.py` using standard Python 3; the script requires no external packages. It checks the five-state transfer formula and integer recurrence for \(q\in\{2,3,4,5\}\), and the combinatorial top-component count for \(4\le n\le15\). It independently enumerates all length-one and length-two coefficients satisfying the square-zero path-product equations for nine small \((n,q)\) cases; every length-three coefficient is free, providing the exact factor \(q^n\).

The exhaustive counts are: \(N_4(2)=640\), \(N_5(2)=3584\), \(N_6(2)=17408\), \(N_7(2)=88064\), \(N_4(3)=18225\), \(N_5(3)=255879\), \(N_6(3)=2735937\), \(N_4(4)=188416\), \(N_5(4)=4980736\). Additional path-basis multiplication tests compare the extracted equations against literal concatenation. Extension-field arithmetic over \(\mathbb F_4\) is implemented using the irreducible polynomial \(t^2+t+1\). A successful run ends with `VERIFY_OK_CYCLIC_J4_SQUAREZERO`.

The counts are finite checks, not substitutes for the proof of the general rank formula, transfer identity, geometric dimension or top-component classification. No independent audit is asserted.
