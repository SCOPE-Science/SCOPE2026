# Explicit orbit-constant Ramanujan 3-cyclic lift of the Möbius–Kantor graph

## Context

Nearly all explicit Ramanujan lifts use degree-2 signings. Cyclic (shift) lifts
promise a richer covering universe with a different spectral decomposition via
Fourier blocks, but the literature proves existence abstractly (infinite
3-cyclic Ramanujan towers from bipartite Ramanujan bases) without exhibiting a
shift function for any named 16-vertex base. The 16-vertex Möbius–Kantor graph
M, presented as the generalized Petersen graph G(8,3), is cubic, bipartite,
symmetric, and itself Ramanujan (spectrum ±3, ±√3×4, ±1×3), making it a natural
test case for instance-explicit shift-lift technology with applications to codes
and quantum walks.

## Definitions

Let M have vertices {0,…,15}: outer 8-cycle i∼i+1 (mod 8), spokes i∼8+i, inner
edges 8+i∼8+(i+3). The dihedral group D8 of order 16 acting by simultaneous
rotation/reflection of the two rings preserves the edge set and has exactly 3
undirected-edge orbits (outer/spokes/inner, 8 edges each). A Z3-valued shift
function constant on these orbits is a pattern (a,b,c) ∈ Z3³ (27 patterns).
Each undirected base edge {x,y} with shift s lifts to the 3 undirected edges
(x,j)–(y,j+s mod 3), j ∈ Z3, giving a 48-vertex 3-cyclic covering graph G.
Its adjacency spectrum decomposes into Fourier blocks: B_0 (base adjacency)
plus conjugate blocks B_1, B_2 with ω = e^{2πi/3} phases; G is Ramanujan iff
all B_k singular values are ≤ 2√2.

## Result

With shift (outer 1, spokes 0, inner 1), i.e. pattern (1,0,1), the 48-vertex
3-cyclic lift G is cubic, simple, bipartite (24+24), connected, with symmetric
spectrum, trivial eigenvalues +3 and −3 each of multiplicity exactly one, and
every nontrivial eigenvalue λ satisfying |λ| ≤ 2√2. The top Fourier-block
singular value squared is ≈ 6 (largest nontrivial |λ| ≈ √6 ≈ 2.449, margin
≈ 0.38 below 2.828). Moreover all 24 connected orbit-constant patterns are
certified Ramanujan; the 3 patterns (0,b,0) give disconnected lifts (3 disjoint
base copies) excluded from the connected-lift claim.

## Proof / evidence

All certificates are exact integer computations over ℚ and ℚ(ω), replayable
stdlib-only via `python3 output/artifacts/mk_verify.py` → `VERIFY_OK`
(Fraction arithmetic: Bareiss determinants, integer Faddeeva–LeVerrier
characteristic polynomials, Sturm sequences with positive-scaling
normalization; runtime seconds).

1. Full-lift certificate: p(t) = charpoly of the 48×48 lift adjacency A is even
   (symmetric spectrum); p(3) = p(−3) = 0 with p′(3) ≠ 0 (multiplicity one
   each). q(y) = charpoly of A²: q(8) ≠ 0; exactly one distinct root above 8,
   isolated in (17/2, 19/2) with no roots in (8,17/2) or (19/2,B) — that root
   is y = 9 with q(9) = q′(9) = 0, q″(9) ≠ 0 (multiplicity 2, the ±3 pair);
   zero roots below 0. Hence every other A²-eigenvalue is ≤ 8.
2. Fourier-block certificate: for each of the 27 patterns the squared-singular-
   value polynomial q_{a,b,c}(y) = charpoly(B_1 B_1^*) has integer coefficients
   (imaginary parts cancel exactly). Exact Sturm counts: the 3 disconnected
   patterns have one distinct root above 8 (value 9); all other 24 have q(8)≠0,
   zero roots above 8, zero below 0. Witness (1,0,1):
   q(y) = y⁶(y¹⁰−48y⁹+1032y⁸−…+5308416), q(8) = 2³⁴.
3. Consistency: Tr(G^r) = Σ_k Tr(B_k^r) for r = 2,4,6 (144, 720, 4176) with
   vanishing ℚ(ω) imaginary part; base charpoly divides lift charpoly exactly
   over ℤ with quotient t¹²·r(t²) matching the conjugate-pair signature.

## Limitations

Certificates are tied to the stated orientation convention (arcs
(x,j)→(y,j+s)); gauge quotient among the 27 patterns is not classified (only 4
distinct block polynomials; existence needs one witness). Numeric brackets for
the top block root are Sturm enclosure intervals, not closed forms. The three
disconnected-family patterns are excluded as non-connected lifts.

## Reproducibility

`python3 output/artifacts/mk_verify.py` (stdlib only: fractions, json).
Filed data: `block_C_charpolys.json` (27 block polynomials),
`lift48_charpoly.json`, `lift48sq_charpoly.json`, `ledger27.json`,
`witness_cert.json`, `lib.py` (exact linear algebra + Sturm).

## References

- Liu–Peyerimhoff–Vdovina cyclic Ramanujan towers (existence, no MK instance).
- Agarwal–Kolla–Madhu / Chandrasekaran–Velingker shift lifts (method family).
- Hall–Puder–Sawin Ramanujan coverings (structural characterization).
- Brouwer MK census (https://aeb.win.tue.nl/graphs/MoebiusKantor.html):
  unsigned spectrum only; Wikipedia Möbius–Kantor graph (identity only).
