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

# Verification of the theorem

The proof in `RESULT.md` is the complete general argument. The test programs are finite independent consistency checks, not a proof by enumeration of infinitely many groups.

`verify_cyclic.py` uses integer basis commutators and disjoint-set graph components for every cyclic order \(1\) through \(144\). It checks the coset-span rank, incidence image, exact divisor-cycle formula, necessity and sufficiency of the sharp fixed-factor condition, and explicit telescoping preimages. It also tests reductions of the displayed integer equalities modulo \(2,3,5,7\).

`verify_abelian.py` uses the direct group law and a separately written commutator evaluator on 29 finite abelian groups, both cyclic and noncyclic. It independently constructs the commutator-generated equivalence classes and \(-2\) components, and directly verifies integral primitive formulas for positive cases; it constructs a component-sum obstruction in negative cases.

Commands from the directory containing both scripts:

```bash
python3 verify_cyclic.py
python3 verify_abelian.py
```

The results are stored in `verify_cyclic_output.txt` and `verify_abelian_output.txt`; both end in `VERIFY_OK`. Representative cases include cyclic orders \(5,9,12,32,72,128\), and \(C_4\oplus C_4\), \(C_3\oplus C_9\), \(C_2\oplus(C_3)^2\), and \((C_2)^2\oplus(C_3)^2\). No testing establishes absolute novelty, historical priority, or externally validated correctness.
