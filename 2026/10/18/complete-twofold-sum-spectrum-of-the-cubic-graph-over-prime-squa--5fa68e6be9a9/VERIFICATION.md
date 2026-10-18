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

The proof is algebraic for every prime \(p\ge5\). The standalone program `verify.py` uses only Python's standard library and no floating-point arithmetic. Run `python3 verify.py` from the directory containing that file. It exhausts all \(p^4\) ordered pairs \((a,b)\) for each tested prime \(p\in\{5,7,11,13,17\}\), constructs the exact multiplicity histogram on the entire ambient target group, and verifies the claimed formulas for sum multiplicity total and additive energy. The actual matching output is embedded as `verification_output.txt`.

The critical proof check is the equation \(3xu^2=4y-x^3\) in \(\mathbb Z/p^2\mathbb Z\), with \(u=2a-x\), followed by the exhaustive valuation classes \(x\) unit, \(x\) nonzero divisible by \(p\), and \(x=0\). In the unit case nonzero quadratic residues have two unique Hensel lifts while zero has \(p\) roots; in the nonunit case each root modulo \(p\) has \(p\) lifts. None of the finite checks proves an unbounded-prime statement by itself; that statement follows from the algebraic argument. The sharp unrestricted extension norm has not been determined here.
