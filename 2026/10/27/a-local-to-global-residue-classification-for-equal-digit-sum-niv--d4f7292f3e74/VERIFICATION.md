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
# Arithmetic verification and reproducibility

Run `python3 verify.py` with the standard Python 3 library. The program checks every residue class for \(2\le b\le5\), \(1\le k\le3\), and \(1\le m\le30\). It independently computes the permitted low-prefix classes, constructs high digit exponents via repunit coins, checks the exact modulus conditions using modular exponentiation, and materializes the integers where their bit lengths are modest to recompute both digit sums directly.

The expected output begins `VERIFY_OK parameters= 5278 low_residue_obstruction=PASS modular_digit_construction=PASS`.

For \(b=2\), \(k=2\), and \(m=16\), the permitted classes are exactly \(0,1,4,5\). For example \(21=1+4+16\equiv5\pmod{16}\), its base-four digits are \(111\), its binary expansion has three ones, and \(3\mid21\). The class \(2\pmod{16}\) is forbidden by the low-digit condition.

The finite check cannot establish either the universal quantifiers or novelty. The proof handles all integer parameters and all allowed residue classes by a greedy bound and unbounded digit-sum choices. The reproduced files contain no claims of independent review or external certification.
