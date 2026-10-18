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

# Reproducibility
Run `python3 VERIFY.py` using only the Python standard library. For \(1\le r\le6\), the program builds each \(3^r\)-square Cartier matrix over \(\mathbb F_5\) by coefficients in \((x^{2\cdot3^r+1}+x)^2\), extracts its partial-permutation graph, independently enumerates multiplication-by-\(5\) orbits modulo \(4\cdot3^r\), and checks both methods give exactly three surviving labels and rank \(3\). Successful execution prints `VERIFY_OK`.

The proof for all \(r\ge1\) does not depend on the finite checks. The crucial noncomputational fact is that \(5\) generates \((\mathbb Z/3^q\mathbb Z)^\times\) for every \(q\ge1\), shown by its order modulo \(3\) and the valuation \(v_3(5^2-1)=1\). Full orbits with \(q\ge2\) necessarily enter the upper half; those with \(q=1\) give two surviving labels, and the maximally divisible case gives the remaining one. No independent external audit or certification is represented here.
