# First P/N classification with witnesses for Dawson (.07) and Treblecross (.007) on subdivided stars and bistars (arms <= 6)

## Context
Octal games on heaps are classical (Guy-Smith, Winning Ways). Dailly et al. (arXiv:1612.05772, TCS 746 (2018)) extended octal games to graphs: heaps become connected components, counters become vertices, and a path P_n reproduces the heap game. That paper completely resolves only game 0.33 on subdivided stars and bistars. Heap Grundy records for Dawson's Kayles (.07) and Treblecross (.007) (OEIS A002187, A071426/A395248, Flammenkamp tables to millions / 2^30) are path/heap-only. No prior source classifies .07/.007 on any tree-board family.

## Definitions
- Boards: subdivided 3-stars S(a,b,c) with 0<=a<=b<=c<=6 (84 positions); single-edge bistars B((a,b),(c,d)) with a<=b, c<=d, sides lexicographically ordered (406 positions). Paths P_n occur as components.
- Graph lift (Dailly et al. Def 5): in octal 0.u1u2..., a move deletes a connected i-set Xi with ui!=0. Writing ui=b1+2*b2+4*b3: b1 allows deleting the whole component, b2 allows leaving the remainder connected nonempty, b3 allows disconnecting (arbitrarily many pieces).
- Hence: .07 (u2=7): delete any connected 2-set (any edge's endpoints); remainder arbitrary. .007 (u3=7): delete any connected 3-set (in a tree, a P3: center + two distinct neighbours); remainder arbitrary.
- Position = disjoint sum of components; P iff xor of component Grundy numbers is 0 (Sprague-Grundy).

## Result
From the committed rules above, every position in scope has exactly the P/N label in the committed tables:
- .07: stars P=19/N=65; bistars P=69/N=337.
- .007: stars P=11/N=73; bistars P=40/N=366.
- Every N-position's logged move is a legal connected 2-/3-set with option-xor 0; every P-position has all legal options with xor != 0.
- Star P-sets: .07: S(0,0,0) S(0,0,4) S(0,1,3) S(0,2,2) S(0,2,6) S(0,3,5) S(0,4,4) S(1,1,3) S(1,3,5) S(1,3,6) S(2,2,4) S(2,2,5) S(2,3,4) S(3,3,3) S(3,5,5) S(3,6,6) S(4,4,4) S(4,4,5) S(4,6,6). .007: S(0,0,0) S(0,0,1) S(0,1,6) S(0,2,5) S(0,3,4) S(1,1,5) S(1,2,5) S(2,2,5) S(4,4,6) S(4,5,6) S(5,5,5).
- Lemma A (.07): all 28 symmetric bistars B((a,b),(a,b)) are N; deleting the central bridge {u,v} leaves twin paths Pa+Pb+Pa+Pb (xor 0).
- Lemma B (.007): symmetric bistars B((a,b),(a,b)) are P exactly at (0,0),(0,3),(0,6),(3,3),(3,6),(6,6); other 22 are N with logged bridge-crossing winning moves. P-strategy: side-swap mirror; involution is fixed-point-free on vertices and every connected triple meeting both sides contains both centres (hence bridge-crossing). Bridge-crossing options {u,v,w} (at most 4 per position) are finite-checked N. On (0,0),(0,3),(3,3) pure mirror always leaves xor 0; on (0,6),(3,6),(6,6) mid-arm cuts use one of 4/4/8 logged fallback responses.

## Proof / evidence
Exact finite computation, independently replayed. `solve.py` computes Grundy numbers by memoised canonical DP; `verify.py` is a self-contained reimplementation that recomputes every label from the rules, checks each N witness (legal + connected + option-xor 0) and each P by exhaustion, replays Lemma A twin-copy and Lemma B mirror/fallback responses with bridge-crossing N-checks, checks scope completeness (84+406 keys per game), and path-vs-OEIS prefixes. Run `python3 artifacts/verify.py` gives all 12 checks PASS and VERIFY_OK. Closure: deleting <=3 vertices from a star/bistar never creates degree >3 or a third branch node. Path cross-check (not derivation): .07 matches A002187 to n=35; .007 matches A071426 to n=15.

## Limitations
Finite census block only (arms <= 6); no periodicity or general-n theorem. Grundy numbers are computed but only P/N + witnesses are claimed. Lemma B uses finite-checked fallbacks on 3 of 6 positions rather than a uniform mirror. Heap/path agreement is a cross-check, not a transfer proof.

## Reproducibility
`python3 artifacts/verify.py` -> expect VERIFY_OK (seconds). Artifacts: solve.py (solver), verify.py (independent verifier), tables_07.json, tables_007.json (84 stars + 406 bistars each with Grundy/outcome/witness), responses_007_symP.json (Lemma B responses).

## References
- L. Beaudou et al., Octal Games on Graphs: game 0.33 on subdivided stars and bistars, TCS 746 (2018) 19-35. https://arxiv.org/abs/1612.05772
- OEIS A002187 (Dawson .07 heap values). https://oeis.org/A002187
- OEIS A071426 / A395248 (Treblecross .007 heap values). https://oeis.org/A071426 , https://oeis.org/A395248
- A. Flammenkamp, Sprague-Grundy values of octal games. https://wwwhomes.uni-bielefeld.de/achim/octal.html
