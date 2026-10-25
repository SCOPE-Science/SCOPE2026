# Review: Paley thirteen-vertex integral systoles

## Correctness (PASS)
The exact Paley graph has 13 vertices, 39 edges, 26 triangular faces, and no tetrahedra. Its triangular-plane covering has deck lattice \(L=\{(a,b):a+3b\equiv0\pmod{13}\}\), and the displayed map \(\Psi\) gives an integral isomorphism \(H_1\cong\mathbb Z^2\). Every simple triangle is a filled face. The 4-cycle count is 78 by the strongly regular common-neighbour parameters; 39 cycles have a chord and bound two faces, leaving 39 induced cycles. Affine translates of three explicit representatives exhaust these and have classes \((0,-1),(1,3),(1,4)\), all primitive, with the first and third determinant one. The verifier independently enumerates every simple 3- and 4-cycle, checks the affine orbit and face constraints, and exactly reproduces the stated output. No finite experiment is used as an infinite-family proof.

## Originality (PASS; unresolved risks noted)
Datta--Upadhyay establish the cyclic torus triangulation; Brehm--Kühnel classify triangular lattice-quotient torus maps and describe straight edge loops. Their inspected primary material does not give a complete enumeration of simple essential length-four cycles, the three primitive integral homology directions, or the integral generation property. Two directly relevant accessible published records were read in full: the cyclic torus flag criterion gives the earliest flag member at order thirteen, whereas the one-direction systolic-shell theorem concerns only \(n\ge17\), explicitly omitting this small exceptional torus. Searches for Paley13, order-thirteen cyclic tori, induced quadrilaterals and systole class profiles found no result logically covering the present statement. Search absence is not proof of uniqueness: an unindexed equivalent treatment of equivelar torus loops is a genuine residual risk.

## Mathematical value (PASS)
The order-thirteen torus is the first flag member of a standard cyclic family and is also a classical Paley graph clique complex. Its 39 shortest loops split equally into three primitive integral directions and generate all of \(H_1\), sharply contrasting with the single shortest homology direction already established in the same cyclic family for \(n\ge17\). A complete integral systolic carrier and direction classification is a natural finite-topological invariant not provided by torus homotopy type or Betti numbers. The exact orbit structure makes the fact useful as a benchmark for systoles in flag triangulations and symmetry actions.

## Boundaries
The result uses combinatorial edge length, not a variable Riemannian metric. Primacy and the triangulated torus's existence are prior work. Bibliographic uncertainty remains; no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
