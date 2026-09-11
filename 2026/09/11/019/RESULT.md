# Two-sided Ramanujan signing of the Chvátal graph with rho < 2.57

## Context
For a d-regular graph G and a signing sigma: E(G) -> {+1,-1}, let A_sigma be
the signed adjacency matrix and rho(A_sigma) its spectral radius. The
two-sided Bilu–Linial conjecture asks for a signing with
rho(A_sigma) <= 2*sqrt(d-1). Marcus–Spielman–Srivastava plus Hall–Puder–Sawin
settle one-sided 2-coverings for every graph and two-sided coverings for
bipartite bases; two-sided existence for non-bipartite bases is open
(Belardo et al., Sec 3.5; HPS Sec 1.1). The Chvatal graph — 4-regular on
12 vertices, 24 edges, triangle-free, chromatic number 4, non-bipartite —
is the smallest extremal base of this type (Chvatal 1970).

## Definitions
- G: graph on vertices {0,...,11} with the 24 edges
  (0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),(2,3),(2,6),(2,8),
  (3,4),(3,7),(3,9),(4,5),(4,8),(5,10),(5,11),(6,10),(6,11),
  (7,8),(7,11),(8,10),(9,10),(9,11).
- sigma*: signing equal to -1 on
  (2,3),(2,6),(3,9),(5,10),(7,8),(7,11),(9,10),(9,11) and +1 elsewhere.
  Equivalently, with the BFS spanning-tree gauge (tree edges forced +1),
  the 13 cotree edges
  (2,3),(2,6),(2,8),(3,7),(3,9),(4,5),(5,10),(5,11),(7,8),(7,11),(8,10),
  (9,10),(9,11) carry -, -, +, +, -, +, -, +, -, -, +, -, - (mask 6995).
- In full edge-list order the signs are
  +,+,+,+,+,+,+,-,-,+,+,+,-,+,+,-,+,+,+,-,-,+,-,-.

## Result
The signed matrix A_{sigma*} has exact characteristic polynomial (over ZZ)

  chi(x) = x^12 - 24 x^10 + 226 x^8 - 1056 x^6 + 2549 x^4 - 2976 x^2 + 1280,

all odd coefficients vanish (spectrum symmetric), and

  rho(A_{sigma*}) < sqrt(33/5) < 2.57 <= 2*sqrt(3) ~ 3.4641.

Hence sigma* is an explicit two-sided Ramanujan signing of the Chvatal
graph; its signed 2-lift is Ramanujan in the two-sided sense.
Numerically rho ~ 2.5616, consistent with the enclosure.

## Proof / evidence (exact certificate, no floating point)
1. Base identity: from the edge list, 12 vertices, 24 edges, 4-regular,
   connected, triangle-free (endpoint neighborhoods disjoint), girth
   exactly 4 (witness cycle 0-1-5-4-0), chromatic number exactly 4
   (exhaustive 3^12 backtracking 3-color UNSAT plus explicit 4-coloring).
   Unsigned spectrum {4, 1.56, 1^4, 0^2, -1, -2.56, -3^2} agrees with the
   published Chvatal spectrum.
2. Charpoly: exact Bareiss determinants at 13 integer nodes plus exact
   rational interpolation, re-verified at fresh nodes (-9, 7, 11);
   Newton trace check sum lambda_i^2 = 48 = 2*24; exact integer
   Cayley–Hamilton chi(A) = 0_{12}.
3. LDL leg: M = 33I - 5 A^2 is an exact integer matrix; exact-rational
   LDL^T has all 12 pivots strictly positive (smallest 224/323), so
   M > 0, every eigenvalue of A^2 is < 33/5 = 6.6, and
   rho < sqrt(6.6) < 2.57. Since 33/5 < 12 over ZZ, rho < 2*sqrt(3).
4. Sturm leg (independent): exact Sturm sequence of chi gives variation
   count 0 on [257/100, infinity) and (-infinity, -257/100], so no
   eigenvalue has |x| >= 2.57; 257/100 > sqrt(33/5) is certified by
   257^2*5 = 330245 > 330000 = 100^2*33 over integers.
5. Bracket: chi(2) = -48, chi(3) = 8192 (exact), so a root lies in (2,3):
   the signing is nontrivially expanding.
6. Matching-polynomial log: exact backtracking matching counts
   m = (1,24,204,752,1175,628,52); Heilmann–Lieb bounds the
   matching-polynomial roots by 2*sqrt(3); the signed bound sqrt(6.6)
   sits well under it, consistent with the interlacing picture.

## Limitations
- Graph identity is tied to the archived edge list above (standard Chvatal
  adjacency); isomorphism to other Chvatal labellings is not separately
  certified, though degree/girth/chromatic/spectrum fingerprints agree
  with the published object.
- Existential single-signing claim; the 8192-class numpy scan context
  (minimum rho ~2.5616 at this class) is heuristic evidence, not part of
  the certificate.
- The matching-polynomial largest-root figure (~3.465) is a numeric log;
  only the analytic Heilmann–Lieb bound is certified.

## Reproducibility
Run `python3 output/artifacts/certify.py` (stdlib only) -> `VERIFY_OK`.
It recomputes graph identity, signing, charpoly, Cayley–Hamilton, LDL,
Sturm, and matching counts from the printed edge list and mask, with no
floating-point logic in any certificate step.

## References
- V. Chvatal, The smallest triangle-free 4-chromatic 4-regular graph,
  J. Combinatorial Theory (1970). DOI: 10.1016/S0021-9800(70)80057-6.
- House of Graphs, Chvatal Graph (graphs/972).
  https://houseofgraphs.org/graphs/972
- MathWorld, Chvatal Graph. https://mathworld.wolfram.com/ChvatalGraph.html
- M. Marcus, D. Spielman, N. Srivastava, Interlacing families I:
  Bipartite Ramanujan graphs of all degrees.
- Hall, Puder, Sawin, Ramanujan coverings of graphs.
  https://arxiv.org/html/1506.02335v4
- Belardo, Cioaba, Koolen, Wang, Open problems in the spectral theory of
  signed graphs. https://arxiv.org/html/1907.04349v1
- Y. Bilu, N. Linial, Constructing expander graphs by 2-lifts.
  DOI: 10.1109/FOCS.2004.19
