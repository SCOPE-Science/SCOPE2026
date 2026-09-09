# Girth 5, exact chi(B_4)=3 with root 0, and depth-4 spoiler no-go for Cay(F_2,S) with commutator generator

## Context
Borel-versus-measurable chromatic gaps on bounded-degree Schreier graphs and their
transfer to distributed LOCAL complexity (Kechris-Marks program; Marks games;
Bernshteyn transfer) form a recognized frontier. The free-group shift Schreier graph
with symmetric generators S = {a^{±1}, b^{±1}, w^{±1}}, w = aba^{-1}b^{-1}, was proposed
as a candidate separation witness chi_B >= 4 vs chi_mu = 3, with depth/radius 4 fixed by
|w| = 4. The admitted depth-4 spoiler fallback asked for an explicitly tabulated
Player-I winning strategy in the depth-4 rooted Marks coloring game on B_4(e).

## Definitions
- F_2 = <a,b> as reduced words over {a,A,b,B}, A = a^{-1}, B = b^{-1}.
- w = abAB (reduced, length 4, cyclically reduced, nontrivial), w^{-1} = baBA.
- S = {a,A,b,B,w,w^{-1}}: six distinct reduced words, inverse-closed, e not in S.
- G_S = Cay(F_2,S): vertex-transitive, 6-regular Cayley/Schreier graph.
- Tree-metric ball B_r(e): reduced words of length <= r; |B_4(e)| = 1+4+12+36+108 = 161.
- S-ball of radius r: words at S-word-metric distance <= r from e.
- Literal depth-4 rooted game: 4 rounds; each round Player I names v in B_4(e),
  Player II answers a color in {0,1,2}; I wins iff the final partial coloring is
  improper on an internal S-edge or violates c(e) = 0.

## Result
For G_S as above:
1. girth(G_S) = 5 exactly: zero non-backtracking closed walks of length 3 or 4
   (0 closed length-3 products; 66 closed length-4 products, every one containing an
   adjacent inverse pair), and explicit 5-cycle e -> a -> ab -> abA -> w -> e with
   steps a,b,A,B,w^{-1} = baBA in S. Rooted simple-cycle counts through e:
   lengths 3,4,5,6: 0,0,10,0.
2. The tree-metric ball B_4(e) (161 vertices, 177 internal S-edges) has ordinary
   chromatic number exactly 3, with an explicit proper 3-coloring with root color 0
   (class sizes 93/54/14). The 5-cycle lies in B_4, so chi >= 3; the coloring gives
   chi <= 3 with root 0.
3. Consequently no Player-I table T wins the literal depth-4 rooted Marks 3-color
   game on B_4(e) with root constraint c_0 = 0: Player II copies the fixed coloring
   and every 4-move spoiler sequence (including adaptive choices) survives as a
   restriction of a globally proper root-0 coloring.
4. Supporting data: exact 3-colorings of the S-ball of radius 4 (833 vertices,
   953 internal edges; classes 398/319/116) and of tree-ball B_5 (485 vertices,
   537 edges).

## Proof / evidence
- Girth: exhaustive enumeration over all 6^3 = 216 and 6^4 = 1296 generator products
  via reduced-word concatenation (`output/artifacts/girth.py`); non-backtracking
  filter removes trivial backtracks s_{i+1} = s_i^{-1}; vertex-transitivity extends
  from e to all vertices. The 5-tuple has pairwise distinct vertices and consecutive
  differences in S, hence a simple C_5. Replay: `python3 output/artifacts/girth.py`.
- chi(B_4) = 3: internal edge count and coloring conflicts checked by exhaustive edge
  scan (177 edges, 0 monochromatic). Coloring found by exact DSATUR branch-and-bound
  (161 search nodes) and independently re-verified by the checker
  (`output/artifacts/b4_root0.py`, `output/artifacts/verify_emergent.py` item 2).
- No-go: deterministic restriction (mirror/strategy-copy) argument; no search needed.
  A 200-trial randomized simulation over 4-move spoiler sequences confirms all survive
  but is illustrative only.
- S-ball r=4 coloring: exact DSATUR (834 nodes), 0 conflicts over 953 edges
  (`output/artifacts/Sball4_coloring.json`). B_5 3-colorability: exact DSATUR
  (486 nodes), 0 conflicts. Rooted cycle census to length 6 replayed
  (`output/artifacts/verify_final.py` logic).

## Limitations
- Does not prove chi_B(G_S) >= 4 or chi_mu(G_S) = 3; both infinite halves remain open.
  Finite 3-colorability is compatible with both Borel-hard and Borel-easy regimes.
- No measurable-3-coloring construction is claimed.
- The no-go applies only to the literal depth-4 rooted game on B_4(e) with c_0 = 0,
  not to deeper or larger Marks games. Future lifting must use depth >= 5 or a
  larger ball; the C_5 scale is the proved game-horizon lower bound.
- DSATUR/coloring scripts are exact but not formally verified in a proof assistant;
  trust rests on checker re-verification of archived colorings.

## Reproducibility
Python standard library only:
- `python3 output/artifacts/girth.py` — girth certificate.
- `python3 output/artifacts/b4_root0.py` — regenerates B4_coloring.json (DSATUR).
- `python3 output/artifacts/verify_emergent.py` — prints VERIFY_OK
  (paths assume run from the record root with output/artifacts/ present).
- `output/artifacts/verify_final.py` — rooted cycle census + coloring reload + no-go.
- S-ball r=4 coloring archived in `output/artifacts/Sball4_coloring.json`.

## References
- A. Marks, A determinacy approach to Borel combinatorics, arXiv:1304.3830
  (JAMS 2016): general Marks-game method; no table for this S.
- Conley-Jackson-Marks-Seward-Tucker-Drob, arXiv:1611.02204: hyperfinite/acyclic
  setting; G_S here is outside it.
- A. Bernshteyn, arXiv:2004.04905: LOCAL-to-Borel/measurable transfer + measurable
  LLL; states no strategy for this S.
- Grebik-Vidnyanszky, arXiv:2205.01839: Ramsey/expander acyclic witnesses;
  different object.
