---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The ordinary Chari--Joswig rooted-forest model is explicitly orientation-reversed to an at-most-one-incoming-arrow forest without changing equivariance. Geometric invariant barycentric faces are unions of admissible arrow-orbits: singleton->singleton and singleton->pair give one choice, pair->distinct pair gives two parallel aligned/crossed choices, and pair->singleton or same-pair is inadmissible. A quotient directed cycle lifts because its pair-block bijections have finite order; an upstairs cycle projects to a quotient cycle, proving exact equivalence. For f>=1 a singleton is a complete source, for f=0,t>=2 any pair is, so Kozlov complete-source shellability (Jojić Section 2) applies to the uncolored quotient. Moradi--Khosh-Ahang vertex expansion Theorem 2.12 preserves pure shellability under two parallel choices, yielding facet dimension f+t-2. Directed matrix--forest determinant of the incoming Laplacian gives (1+fz)^f(1+(f+2t)z)^(t-1) for f>=1, and (1+2tz)^(t-1) for f=0. Evaluating -Phi(-1), with top-dimensional shelling, gives the integral sphere ranks including zero-dimension/empty cases. Independently enumerated every acyclic quotient-arrow selection for 11 (f,t) pairs up to f+t=5 and matched every face-polynomial coefficient against the determinant factors. Infinite conclusion relies on checked shellability and determinant theorems.

## originality

PASS

The earlier all-graph equivariant matrix--forest formula already determines the complete-graph involution face-character/Euler factor; that determinant specialization is covered, not new. A new actual fixed-point orbit-forest complex plus vertex-expansion shellability yields a finer *integral homotopy* classification. Compared also the different product-of-independent-pair-swap fixed action, which forbids aligned/crossed pair-to-pair arrow orbits.

## value

PASS

Every permutation involution cycle type of a natural large family has its *integral geometric fixed-space homotopy type* calculated, including nonempty fixed spaces with no fixed graph labels and explicit torsion-free sphere multiplicities. These are structural data beyond already known Euler traces, with a reusable colored quotient-forest argument; not merely a determinant restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
