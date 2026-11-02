---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The shift condition x_i in {x_{i+1},x_{i+3},x_{i+4}} forbids exactly 01011,01111,10000,10100 as length-five blocks. The overlap matrix of all sixteen four-block states has 28 edges and produces a bijection between cyclic words and closed walks, P_n=trace(M^n). Fresh independent exact SymPy determinant agrees with lambda^4(lambda-1)^3(lambda+1)(lambda^2-lambda-1)(lambda^2+lambda+1)(lambda^4+lambda^2-1); determinant identity gives the claimed rational Artin-Mazur zeta at all lengths, not just checked periods. Four strongly connected classes include one primitive twelve-state core, whose Perron root is phi; other classes have spectral radius one, establishing entropy log phi and a unique maximal-entropy measure. Complement symmetry forces binary marginal 1/2. Fresh brute enumeration of all cyclic binary words at n=1..12 agreed with the traces, and graph strongly connected partition was checked independently. Scope is two-sided binary sequences for this exact triple only.

## originality

PASS

The source introducing the fixed pseudoperiod (1,3,4) proves paperfolding-sequence membership, not the entropy and periodic orbit law of the entire binary finite-type shift defined by the triple. General SFT transfer-matrix and zeta methods are background; the explicitly factored determinant, four SCCs and golden-ratio Perron root require a specific computation. No equivalent known forbidden-block shift was identified, with obvious residual alias risk.

## value

PASS

The fixed (1,3,4) pseudoperiod is singled out by the paperfolding theorem. The finite-type shift of every binary word meeting that constraint is a natural global object; exact golden-ratio entropy, full rational zeta, four recurrent components and a unique maximal-entropy measure are meaningful exact invariants, not an arbitrary random finite automaton table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
