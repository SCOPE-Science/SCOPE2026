# Scientific audit — 2026-09-30

## Final claim

Among all covering triangle-family complexes on six vertices, there are 2102 isomorphism types and exactly one has integral homology torsion: the classical six-vertex real-projective-plane triangulation with first homology Z/2; exhaustive scans below six vertices have no torsion.

## Correctness — PASS

The exact source CSV was re-read from its assigned Git blob. A separate BigInt Smith-normal-form implementation reconstructed the boundary matrix for every one of the 2102 listed representatives and found exactly one torsion row, mask 242467 with invariant factor 2, with zero discrepancies against the table. Independent exhaustive Smith-form scans of all triangle families on 3, 4 and 5 vertices found no torsion. The witness identities and closed-surface structure in the package are consistent with the classical six-vertex real-projective-plane triangulation.

## Originality — PASS

The six-vertex triangulation of the real projective plane and its Z/2 first homology are classical, and surface censuses cover the manifold case. Searches did not locate an exhaustive homology table over all pure triangle-family complexes on six vertices or a prior theorem that manifold uniqueness alone implies torsion uniqueness among nonmanifold complexes. The original content is therefore the exhaustive all-complex uniqueness/minimality census, not discovery of the RP2 triangulation itself.

The originality comparison explicitly checked equivalent formulations, broader coverage, exact databases/tables, and implication from prior results. See `INDEPENDENT_AUDIT_2026-09-30.json` for the structured searches, source inspections, checked sources, and residual risks.

## Scientific value — PASS

Six vertices are the classical minimum for the real-projective-plane triangulation and hence a natural extremal boundary for torsion. Showing that the classical witness is the only torsion type among every pure 2-complex in that full boundary universe is a meaningful exact classification rather than a routine arbitrary slice.

## Disposition

PASSED. This assessment records the mathematical status of the claim. It is not an external attestation or formal-proof certificate.
