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

# Verification instructions and boundary

The exact result concerns the set \(\mathcal S_5=\{uu:u\in\{0,1\}^5\}\), all \(32\) ordinary binary squares of length \(10\), and finite **linear** superstrings. The asserted optimum is \(82\).

Run `python3 VERIFY.py`. Only the Python standard library is required. Its assertions reconstruct all \(32\cdot31\) directed overlap costs, independently form the eight root necklaces, verify the within/cross cost hypotheses, optimize each of the seven-crossing necklace-block orders, check all \(120\) eight-crossing zero-excess cases, and verify every required factor of the \(82\)-symbol witness. Expected output:

```text
Q7_OPT=82
Q8_EQUALITY_CASES=120 Q8_FEASIBLE=0
WITNESS_LENGTH=82 DISTINCT_SQUARES=32
VERIFY_OK
```

The mathematical reason the finite cases are sufficient is the inequality \(L\ge41+5q\), where \(q\ge7\) counts cross-necklace transitions in a Hamiltonian ordering of the required square factors. All \(q\ge9\) already cost at least \(86\). The standard-library verifier checks exact finite subcases, not an unchecked extrapolation.

For an alternative optimization check, run `python3 ALT_MILP.py` in an environment with NumPy and SciPy supporting `scipy.optimize.milp`. It reconstructs a \(33\)-vertex (one dummy) directed tour formulation and iteratively adds violated subtour cuts until a Hamiltonian tour is obtained. The run in the delivered package gave:

```text
MIP_OPT=82 ITERATIONS=6 SUBTOUR_CUTS=17
MIP_OK
```

This additional method uses a general integer solver and is not required for the dependency-free lower proof. The source files contain the full algorithms, not merely test logs. No claim about another root size, a cyclic covering optimum, or external independent audit follows from these checks.
