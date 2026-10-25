---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

PASS: For fixed nonempty forbidden scattered word P, subsequence monotonicity yields the lower bound max_i rho_P(W_i). Greedy matching decomposes each W_i into phases U_{i,j} containing no next desired letter P[j+1]; concat those phase pieces across all inputs and share the marked p_j letters to build S embedding each input and with greedy rank exactly T=max input rank. If T=|P| every common supersequence contains P, otherwise this witnesses feasibility. The left-to-right rightmost-embedding deletion test is equivalent to embeddability of every input in the retained prefix plus remaining suffix; any retained position is irreversibly essential, proving inclusion minimality in O(k N+|P|) time and O(N+|P|) space. The statement handles k=1, empty inputs, repeated symbols and nonempty forbidden P. Independent direct brute check exhaustively compared 3150 binary pairs of lengths <=3 against their phase amalgamation, rank, and independently reduced inclusion-minimal witnesses.

## originality

PASS

PASS best-of-knowledge: Sopp et al. (2026) Theorems 4.1, 6.1 and 6.2 reduce an existing common supersequence to an MCS and section 7 explicitly asks for one avoiding a forbidden scattered subsequence. They neither state the rank-max identity nor construct a pattern-avoiding witness. Dondi constrains multiplicities in a shortest SCS; McDevitt–Ruškuc uses consecutive subwords, different containment. No directly covering Resultary record was located; unindexed related embedding-class results remain a risk.

## value

PASS

PASS: This supplies a closed-form minimum greedy forbidden-pattern rank, an exact feasibility criterion, and an explicit efficient construction for a natural constrained common-supersequence problem explicitly raised by a 2026 primary article. The strict difference between shortest and inclusion-minimal is demonstrated by the infinite 0^m1, 10^m, P=11 family. The single-pattern hypothesis is substantive, and arbitrary k is covered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
