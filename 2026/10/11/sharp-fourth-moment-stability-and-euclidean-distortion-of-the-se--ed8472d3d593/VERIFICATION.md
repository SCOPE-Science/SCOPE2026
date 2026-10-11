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

# Verification details

`python3 verify.py` was executed using the Python standard library, and returned `VERIFY_OK`.

The executable exhaustively constructs the 35 size-three subsets, checks that there are exactly 840 unordered XOR-zero quadruples, and checks the class-wise XOR pair multiplicities and all 1225 entries of the graph identity \(A^2=9(I+J)\). It separately evaluates finite examples on all 128 uniform sign vectors, reproduces their exact fourth-moment expansion, verifies the corresponding stability inequalities using rational arithmetic, and evaluates the flat extremizer fourth moment to exactly \(97/5\).

These exact finite checks establish the combinatorial conditions in the fixed-size statement, not a theorem for all dimensions. The universal coefficient inequality and Banach--Mazur optimization follow from the symbolic arithmetic--geometric mean and group-averaging proof given in `RESULT.md`; checks of sample arrays alone are not presented as an infinite-domain certificate. The coefficient \(14\) is certified as admissible but not optimal. Independent audit has not been performed.
