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

# Verification of integral Frobenius trace lattices

The associated source file `VERIFY_W_E6.py` requires Python 3 and SymPy \(1.14.0\), declared in `requirements.txt`. Execute `python VERIFY_W_E6.py` in the same directory.

The source constructs the twenty-seven line classes in a \(7\)-coordinate Picard lattice, explicitly reflects in the six roots, enumerates all \(51840\) Weyl permutations, and partitions them into all \(25\) conjugacy classes. For each class the line-orbit trace matrix has an exact integer Smith form; the product of its nonzero invariant factors is the index of its column lattice in its saturation. An independent integer method takes column Hermite normal form and the gcd of all maximal minors. The two methods agree for all \(25\) classes; only three have index three.

The three exceptional classes have Frobenius orders and fixed Picard ranks \((3,3)\), \((6,2)\), and \((9,1)\), with class sizes \(480\), \(4320\), and \(5760\). A direct vector check verifies that every orbit trace in the order-nine class equals \(3H\). All generators preserve the Picard intersection form, and each representative's integral fixed-matrix nullity agrees with the trace-matrix rank.

The successful exact verifier emits `VERIFY_OK: 51840 Weyl elements; 25 conjugacy classes; index 3 for exactly orders/ranks (3,3), (6,2), (9,1); independent Hermite-minor check`.

**Boundary:** These computations establish a finite group and lattice classification; the application to cubic surfaces uses established identification of their Picard lattices and Galois actions. Neither numerical tests on finitely many surfaces nor timed-out algebra calculations substitute for the argument. Independent scientific verification has not been performed.
