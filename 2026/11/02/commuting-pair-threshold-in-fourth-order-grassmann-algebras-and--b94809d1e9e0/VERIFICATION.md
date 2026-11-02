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

The supplied `verify.py` uses only standard Python and runs with `python3 verify.py` in the same directory. Its bitmask exterior product independently implements monomial signs and square-zero wedge products; finite-field ranks are computed by pivoting, not read from a hard-coded formula.

Four exhaustive odd-component censuses were run: \((n,q)=(2,3),(3,3),(3,5),(4,3)\). The count of commuting pairs obtained by summing raw matrix-kernel sizes matched the stated formula in each case. For five generators, every cubic \(3\)-vector over \(\mathbb F_2\) and \(\mathbb F_3\) was enumerated, producing alternating-form ranks \(0,2,4\) with exact distributions \((1,155,868)\) and \((1,2420,56628)\). Further random-rank checks covered generators \(5,6,7\) and prime fields of orders \(3,5\). For the full five-generator algebra, direct \(32\times32\) associative commutator matrices were computed for forced rank-zero, rank-two and rank-four cubic forms and further random elements over both odd fields. The two independently derived five-generator commuting-pair formulas agreed at three field orders. The program terminated with `VERIFY_OK`.

The exhaustive domains do not certify arbitrary finite extensions or unbounded generator rank; the general proof uses basis extension and finite-dimensional alternating forms. Independent audit has not been performed.
