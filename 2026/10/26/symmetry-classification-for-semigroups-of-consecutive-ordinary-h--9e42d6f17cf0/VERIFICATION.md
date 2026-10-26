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

# Verification record

Running `python3 verify.py` from the same directory returns `VERIFY_OK`. All operations use exact Python integers or deterministic graph shortest paths; there are no floating-point approximations or external libraries.

The checker performs a full arithmetic re-evaluation of the twenty-four candidate triple-gluing congruences, tests gcd formulas and all interval restrictions for indices \(2\) through \(121\), computes independent Apéry sets for each of those \(120\) semigroups, and compares their Frobenius numbers and genera with the claimed symmetry classification. All \(29\) published A069758 Frobenius numbers from \(n=2\) through \(n=30\) are checked independently. Additional finite checks at \(122\le n\le2000\) corroborate the cutoff inequality and gcd bounds.

To reproduce manually, for each candidate pair \((u,v)\) with \(d=\gcd(u,v)>1\), put \(x=u/d\), \(y=v/d\), and take the unique \(s_0\in[0,y-1]\) with \(s_0x\equiv z\pmod y\). The sign of \((z-s_0x)/y\) is a necessary and sufficient exact test. The full set of resulting integer pairs is printed in RESULT.md. The infinite cutoff rests on the symbolic polynomial \(2n^2-241n-180>0\) and its monotonicity for \(n\ge122\), not on scanning a finite range.

The mathematical argument uses Fel's established gluing characterization as an external theorem. All independent-audit channels are unperformed; this record is computational corroboration and self-review only.
