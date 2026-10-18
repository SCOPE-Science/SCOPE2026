---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Verified Fourier factorization over E_{b,n}=(b/2)Σ ε_j b^j in Z/b^nZ: a character frequency k is an orthogonality zero iff b^r|k and k/b^r odd for some 0<=r<n. For two base-b expansions the least differing digit must have opposite parity, so a full spectral set of cardinality 2^n is exactly a complete binary parity-choice tree; every one of 2^n-1 internal nodes chooses independently among u even and u odd digits, yielding T=u^{2(2^n-1)}. A translation period necessarily has 2-power order dividing 2^n, so stabilizers are nested unique H_s. For b divisible by four, N/2 is not a Fourier zero, forbidding nontrivial H_s. For b=2u with u odd, all differences of distinct elements in H_s have odd quotient after appropriate b-adic factor; each spectrum fixed by H_s chooses a full depth-(n-s) low-prefix tree and one of u^s H_s-cosets above each of its 2^{n-s} leaves, giving F_s=u^{2(2^{n-s}-1)+s2^{n-s}}. Strata F_s-F_{s+1} and orbit lengths b^n/2^s give Burnside total [F0+Σ_{s>=1}2^{s-1}F_s]/b^n. Independently enumerated (b,n)=(6,2): F0=729, strata stabilizer orders 1,2,4 counts 648,72,9 and 23 orbits; b=4,n=2: 64 all aperiodic, 4 orbits. Inspected actual checker.py and optional cyclotomic_check.py (the latter not independently executed). Theory covers all even bases; enumerations are examples only.

## originality

PASS

The parity tree itself and base-four infinite spectral labelings are old and are not claimed novel. In Dutkay–Han–Sun, Theorem 3.3 and Proposition 5.1 concern spectral labelings/maximal orthogonal sets for an INFINITE Cantor measure, especially base four. Malikiosis gives general finite cyclic spectral/tiling structural criteria and cyclotomic theorems (Theorems 1.4–1.5), not a finite E_{b,n} orbit stabilizer and subgroup-fixed census at all even bases. Targeted Resultary semantic search for even-base finite cyclic Cantor spectra, modulo-four period dichotomy, H_s fixed counts and Burnside table yielded only the same assigned result, and the other hits were mathematically different spectral sets/groups. The specific new content isolated is the modulo-four PERIOD dichotomy, complete subgroup-fixed counts F_s, exact stabilizer strata, and quotient orbit counts for every b,n. No inspected stronger paper mathematically implies these exact group-action enumerations; unindexed finite-cyclic tables remain a genuine risk.

## value

PASS

This is a natural group-action refinement of finite spectral-set classification: which Fourier spectra have nontrivial frequency-translation symmetry, how many at every possible period order, and how many inequivalent spectra remain? The sharp b mod4 transition and all-level closed formulas give nontrivial reusable exact data for finite Cantor spectral pairs and Burnside actions, not an arbitrary tiny computation or repetition of the classical parity tree. The exact finite setting is valuable without claiming infinite fractal measure completeness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
