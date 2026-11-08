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

For the Fano-plane incidence Heawood graph, reconstruct 14 vertices and 21 edges, the full Abrams unordered two-particle cubical model C0=91,C1=252,C2=168 with signed boundaries. Independently recomputed every square and obtained d1*d2=0. Exact ranks modulo 3 are rank(d1)=90, rank(d2)=154. The 14 specified signed *integral* top cycles all have zero boundary and are independent modulo 3; hence rational kernel dimension >=14 while mod-3 rank certifies rational rank>=154, forcing rank_Q(d2)=154. Augmentation bounds rank_Q(d1)<=90, so exactly 90. Thus b1=8,b2=14 and top integer homology free Z^14 (no 3-cells). The particle-trace chain map H1(unordered config)->H1(graph) is G-equivariantly surjective using eight graph fundamental cycles of length <=7 leaving another graph vertex unoccupied; equal rational dimensions imply an isomorphism. Independently generated all 168 GL3(F2) matrices plus 168 Fano incidence dualities, evaluated exact signed chain traces t0,t1,t2,tV,tE and H2=t0-t1+t2-tV+tE. Counts (col1:1,H2 14),(col2:21,-2),(col3:56,-1),(col4:42,2),(col7:48,0),(dual2:28,-2),(dual6:56,1),(dual8:84,0) reproduce the complete 336 character; H1 traces 8,0,-1,0,1,-2,1,0. Sum of H2 traces zero, sum of squared traces 672 yields character inner product 2 and two inequivalent irreducible complex constituents, so no positive rational G-invariants. This independent computation validates the actual finite certificates rather than trusting the verifier success line; correct comparison of ordered vs unordered and mod-2 vs rational is central.

## originality

PASS

PASS: Ko–Park already imply nonequivariant H1 rank/torsion and together with Euler characteristic the H2 rank, so ranks are not the novelty. Original additional data are the complete rational 336-element degree-two automorphism character, point-line duality rows, multiplicity-free decomposition criterion and rational quotient. Prior Borel–Moore exchange-sign and ordered mod-two Heawood results are different homology theories/spaces and do not imply this character.

## value

PASS

PASS: The Heawood graph is a canonical highly symmetric 3-regular Fano incidence graph with a full order-336 collineation-plus-duality group; resolving the full rational top-homology character, two irreducibles and the acyclic rational quotient distinguishes symmetry modules with identical non-equivariant rank. A complete exact character is a natural, useful invariant for configuration spaces even without a general graph-family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
