# Singleton vertex-deletion decks of four canonical SRGs: exact card polynomials, persistent Shrikhande/rook card cospectrality, and a clique/Kirchhoff deck separator

## Context

The Shrikhande graph and the 4x4 rook graph (K4 square K4) are the smallest
cospectral pair of strongly regular graphs, both SRG(16,6,2,2) with parent
spectrum 6^1 2^6 (-2)^9. Parent spectra and parent cospectrality are textbook
(Brouwer SRG tables; MathWorld; Brouwer DRG pages; van Dam-Haemers programme).
The natural next reconstruction / spectral-determination question is whether
the vertex-deletion decks resolve the cospectral parents. No vertex-deletion
card spectra, irregular Hoffman ratios, or deck-multiset comparisons for these
graphs appear in the checked sources; Cauchy interlacing constrains cards to
intervals but does not determine exact card values.

## Definitions

- Graphs: Petersen SRG(10,3,0,1) (outer C5 + spokes + inner {i,i+2} star);
  Clebsch SRG(16,5,0,2) (folded 5-cube: u~v iff Hamming distance 1 or 4);
  Shrikhande SRG(16,6,2,2) (Cayley graph of Z4xZ4 with connection set
  {+-(1,0),+-(0,1),+-(1,1)}); Rook(4,4) SRG(16,6,2,2) (K4 square K4:
  same row or same column).
- D(G): multiset of vertex-deleted cards {G-v}, classified up to isomorphism.
- Card polynomial: monic exact characteristic polynomial det(xI - A) of a card.
- General Hoffman ratio: H = 1 - lmax/lmin per (possibly irregular) card.
- Kirchhoff count: number of spanning trees via any cofactor of the Laplacian.

## Result

Let D(G) be as above. Then:

1. **Singleton decks.** D(Petersen) = {P'-card x10}, D(Clebsch) = {C'-card x16},
   D(Shrikhande) = {S'-card x16}, D(Rook) = {R'-card x16}: one isomorphism type
   each (invariant grouping plus exhaustive backtracking isomorphism of every
   card against the representative).
2. **Exact card polynomials (monic, exact integer arithmetic):**
   - Petersen card (n=9):
     x^9 - 12x^7 + 45x^5 - 12x^4 - 66x^3 + 36x^2 + 24x - 16.
   - Clebsch card (n=15):
     x^15 - 35x^13 + 405x^11 - 264x^10 - 2175x^9 + 3240x^8 + 4035x^7
     - 12880x^6 + 6615x^5 + 11600x^4 - 20505x^3 + 14040x^2 - 4725x + 648.
   - Shrikhande card (n=15) = Rook card (n=15), byte-identical:
     x^15 - 42x^13 - 52x^12 + 576x^11 + 1056x^10 - 3680x^9 - 8640x^8
     + 11520x^7 + 35840x^6 - 13824x^5 - 76800x^4 - 8192x^3 + 73728x^2
     + 24576x - 16384.
3. **Spectra and Hoffman ratios (Cauchy interlacing with parent asserted):**
   - Petersen card: lmax ~= 2.7321, lmin = -2, H ~= 2.3660.
   - Clebsch card: lmax ~= 4.7016, lmin = -3, H ~= 2.5672.
   - Shrikhande card: lmax ~= 5.6458, lmin = -2, H ~= 3.8229.
   - Rook card: identical spectrum (<1e-6) and H (equal <1e-9).
4. **Separator (combinatorial, not spectral).** The Shrikhande card has clique
   number 3 (K4-free: 0 K4-subgraphs; exhibited triangle), independence number 4,
   chi = 4, Kirchhoff trees 2177280000 (exact Bareiss cofactor). The Rook card
   has clique number 4 (6 K4-subgraphs; exhibited K4), independence number 4,
   chi = 4, Kirchhoff trees 2176782336. Hence D(Shrikhande) and D(Rook) are
   non-identical as isomorphism multisets although their cards are cospectral
   with equal Hoffman ratios.
5. **Petersen/Clebsch companions.** Petersen card: omega=2, alpha=4, trees=240,
   chi=3. Clebsch card: omega=2, alpha=5, trees=160000000, chi=4. Full exhibits
   (clique/independent sets, colorings) are in deck_table.json.

## Proof / evidence

- **Proved by incidence replay:** SRG parameters of the four committed matrices
  via entrywise A^2 = kI + lA + m(J-I-A); parent spectra match textbook
  multisets (machine-checked rounded multiplicities):
  Petersen 3^1 1^5 (-2)^4; Clebsch 5^1 1^10 (-3)^5;
  Shrikhande and Rook 6^1 2^6 (-2)^9.
- **Computed evidence (exhaustive, replayable):** deck collapse via backtracking
  isomorphism (all cards vs representative); exact charpolys via exact Bareiss
  evaluations + rational interpolation, re-evaluated on extra points
  (byte-identical S/R cards); omega/alpha/K4/chi via exhaustive
  branch-and-bound (n<=15); tree counts via exact Bareiss cofactors;
  interlacing inequalities numerically (<1e-6 tolerance atop exact charpoly
  identity). The auditor re-ran verify_decks.py to VERIFY_OK and independently
  re-derived charpolys (second Bareiss+Vandermonde implementation), Kirchhoff
  counts, brute-force omega/alpha, coloring validity, (k-1)-uncolorability,
  and interlacing.
- **Negative result honestly reported:** no spectrum-level or Hoffman-gap
  separator exists between the Shrikhande and rook cards; separation is at
  clique/Kirchhoff resolution (omega 3 vs 4 already certifies non-isomorphism).

## Limitations

- Isomorphism verification uses purpose-built degree-ordered backtracking
  (n<=15), not nauty; correctness rests on the committed replay script.
- Spectra/Hoffman/interlacing comparisons use double-precision eigvalsh on top
  of byte-identical exact charpolys; charpoly identity itself is exact.
- Chromatic numbers rest on exhaustive backtracking colorability search logged
  in the script (upper bound by exhibited coloring, lower bound by failed search).
- No claim is made about edge-deletion decks, higher distance-regular graphs,
  or a general spectral-vs-combinatorial deck-separation theorem.

## Reproducibility

Run `python3 output/artifacts/verify_decks.py` (stdlib + numpy only). It rebuilds
the four matrices, replays every check above, writes `deck_table.json`, and ends
with `VERIFY_OK` (see `verify.log`). Wall time is a few minutes on one core.

## References

- Brouwer SRG parameter tables. https://www.win.tue.nl/~aeb/graphs/srg/srgtab.html
- MathWorld — Shrikhande Graph. https://mathworld.wolfram.com/ShrikhandeGraph.html
- MathWorld — Rook Graph. https://mathworld.wolfram.com/RookGraph.html
- MathWorld — Cospectral Graphs. https://mathworld.wolfram.com/CospectralGraphs.html
- MathWorld — Clebsch Graph. https://mathworld.wolfram.com/ClebschGraph.html
- Brouwer DRG page — Shrikhande graph. https://aeb.win.tue.nl/drg/graphs/Shrikhande.html
