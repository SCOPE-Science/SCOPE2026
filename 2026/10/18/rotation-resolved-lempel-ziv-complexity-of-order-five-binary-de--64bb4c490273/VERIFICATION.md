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

The binary 4-bit de Bruijn digraph has 16 vertices each with two incoming and outgoing 5-bit edges; pairing all incoming to outgoing edges at each vertex gives exactly 2^16 deterministic edge permutations, with a single 32-cycle iff an order-five de Bruijn cycle. Fixing edge 00000 makes a one-to-one rotation class enumeration, and every class has 32 rooted cuts. Independently coded the full 65536 pairings and verified exactly 2048 cycles with distinct 5-bit circular factors, then parsed all 65536 rotations using the explicitly defined overlapping-source longest-previous-factor, final-phrase-included LZ76 convention. Obtained exact c histogram 8:6766, 9:34836, 10:23208, 11:726, exact cycle extrema (8,10):1228,(8,11):502,(9,10):226,(9,11):92; independently computed population mean 303859/32768 and variance 458624343/1073741824. The entire finite universe is exhausted, not estimated by sampling or a timeout.

## originality

PASS

Etzion and Lempel (1984) have a deceptively identical title about de Bruijn sequences of given complexity, but materially read full text explicitly defines LINEAR FEEDBACK recurrence complexity, not Lempel–Ziv exhaustive-history complexity. Szczepański (2000) gives unconditional LZ76 distributions for unrestricted words, not the order-five de Bruijn conditional ensemble, and Nunes et al. (2013) studies globally maximal-complexity strings, not this 2048-cycle and 32-cut census. No equivalent LZ76 conditioned table was established.

## value

PASS

The full-component LZ76 parsing of rooted versus cyclic de Bruijn words is a natural, convention-sensitive combinatorics/information-theory invariant. The exact exhaustive order-five histogram, rotational min/max classifications and universal cut bound 9/10 supply a canonical small-order benchmark; the finite census is complete, not an arbitrary hand-picked subset. It makes no unsupported general-order or compression-ratio claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
