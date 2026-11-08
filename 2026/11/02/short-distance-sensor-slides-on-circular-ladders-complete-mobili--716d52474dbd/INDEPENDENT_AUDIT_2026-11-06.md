# Independent mathematical audit

## correctness

PASS

For P_n=C_n square K_2, n>=8, use the published prism lemma that exactly vertex pairs at base graph distance <=3 power dominate; no singleton dominates. Those unordered pairs split into S1,S2,S3,O0,O1,O2 with state multiplicities (2,2,2,1,2,2)*n. Explicitly applying the physical one-edge token slide and verifying the result remains distance<=3 gives degrees (4,6,2,4,6,4), total 11n states, 24n edges and degree polynomial 2nt^2+5nt^4+4nt^6. Moves change distance parity, establishing bipartiteness, and constructive S-type/O-type routes show connectedness. The common-neighbor identity for four-cycles gives per-type square incidences (8,7,1,8,12,6); their weighted sum is 76n, hence 19n unoriented squares. The local types remain stable for n>=8 including wraparound threshold; independent power-domination propagation and reconfiguration enumeration over n=8..12 checked counts, square totals, connectivity and degree spectrum. These finite n checks do not replace the uniform local-type argument.

## originality

PASS

Girish–Somasundaram (2024), Lemma 2, already gives the exact 2-vertex static criterion, and hence 11n viable configurations; that numerical state count is not original. Bjorkman et al. (2026) distinguish TS from TAR/TJ and illustrate TS, but the inspected primary HTML focuses TAR/TJ and does not provide the prism six-type adjacent-slide classification, connected bipartition, or 19n four-cycle theorem. The added dynamic invariants are distinct from the static theorem.

## value

PASS

Keeping power domination after each physically adjacent token slide models local sensor relocation without temporary loss of observability. The complete six-type movement table describes feasible moves in every optimal placement; connectivity and bipartiteness describe reachability and parity; 19n squares count alternative two-step relocation loops. These are motivated intrinsic invariants of a natural graph family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
