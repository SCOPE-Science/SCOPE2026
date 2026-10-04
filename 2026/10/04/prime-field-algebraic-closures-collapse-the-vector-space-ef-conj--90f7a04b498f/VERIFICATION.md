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

The mathematical proof was rechecked against the language actually defined in Scott's paper. In the scalar-free last-round case, closed scalar terms lie in the prime field, so equality of vector terms is exactly a prime-field linear-relation test on the selected vectors. This is the critical point allowing Duplicator to survive \(m+1\) rounds even though the smaller tuple may already be dependent over the full field.

For the upper bound, the coefficients of one dependence relation generate a finite extension of the prime field because the common field is algebraic over that prime field. Such a finite extension is simple in both cases used here: number fields over \(\mathbb Q\), and finite fields over \(\mathbb F_p\). Scott's language includes scalar inverse, so every coefficient in that simple field is represented by a scalar term in the single named primitive element.

`verify.py` was executed from the packaged path before assembly and returned:

`VERIFY_OK m=2..8 qlinear_independence_and_named_scalar_exposure`

That script is only a finite sanity check of the boundary mechanism. It does not certify the all-\(m\) theorem, which rests on the proof in `RESULT.md`.

Source inspection limitations: Scott's standalone PDF was read in full-text extraction around the definition of \(L_{VS}\), Theorems 4.1 and 4.2, and the open-problem statement; a rendered PDF page containing the end of the vector-space argument and open problems was also inspected. Public web and published-finding corpus searches can miss unindexed material.
