# Exact diameter and girth of the 4-regular transvection Cayley graph of PSL(2,13)

## Context

Short diameters of `PSL(2,p)` Cayley graphs lie between elementary finiteness
(Schreier-Sims) and deep asymptotics (Helfgott product growth implying
`O((log p)^c)` diameter, Babai-conjecture polylog bounds for transvection
generating sets). Prime-stratified exact tables remain incomplete and are cited
for diameter benchmarks and Cayley-hash cryptography parameters. The `p=13`
elementary-transvection graph on 1092 vertices is small enough for exhaustive
search replayable by `2x2` matrix multiplication mod 13 in seconds, but its exact
diameter and girth were not in the literature (targeted `arXiv` query
`PSL2+13+Cayley` returns 0 hits).

## Definitions

- `p=13`, `G=PSL(2,13)=SL(2,13)/{+-I}`, `|SL(2,13)|=2184`, `|G|=1092`.
- `a=[[1,1],[0,1]]`, `b=[[1,0],[1,1]]` mod 13,
  `A=a^{-1}=[[1,12],[0,1]]`, `B=b^{-1}=[[1,0],[12,1]]`.
- `S={a,A,b,B}`, `Gamma=Cay(G,S)` undirected (S symmetric).
- Matrices as integer 4-tuples `(x0,x1,x2,x3)=[[x0,x1],[x2,x3]]` mod 13;
  `mm` is `2x2` multiplication mod 13; `neg(M)=-M` mod 13.
- Canonical PSL representative: `canon(M)=min(M,-M)` lexicographically,
  equivalent (13 odd) to first-nonzero-entry in `{1,..,6}`.
- A word over `{a,A,b,B}` is *reduced* if it contains no substring
  `aA,Aa,bB,Bb`. Any unreduced word has a strictly shorter reduced form with
  the same value (cancel one inverse pair), so shortest words and shortest
  identities are reduced.
- Graph girth = length of shortest cycle. Since L=1 has 0 reduced identities
  (no generator is `+-I`, no loops) and L=2 has 0 (no generator squares to
  `+-I`, no two distinct generators coincide mod `+-I`), there are no loops or
  multi-edges beyond backtracking, so girth equals length of shortest
  nontrivial reduced word `=+-I` in `SL(2,13)` (identity in `G`).

## Result

Let `Gamma` be as above. Then:

1. **Order/generation.** `|SL(2,13)|=2184`, `|G|=1092`, `Gamma` is connected
   4-regular on 1092 vertices; i.e. `<a,b>=G`.
2. **Diameter.** `D(Gamma)=10` with distance distribution from identity
   `spheres=[1,4,12,25,48,96,180,279,317,120,10]` for distances `0..10`
   (sum 1092). Exactly 10 vertices attain distance 10. One diametral word is
   `w_D=aaaaabbbba` (length 10), evaluating in `SL(2,13)` raw to `[[8,0],[4,5]]`
   whose canonical class is `(5,0,9,8)`, at distance exactly 10.
   Full diametral set (canonical element -> BFS word, all length 10):
   `(2,0,0,7)->aaBBBBBBAB`, `(2,2,2,9)->aaaBBBABBB`,
   `(2,11,11,9)->aaaaBBBABB`, `(4,2,2,11)->aaabaabaab`,
   `(4,11,11,11)->aaaBBBABBA`, `(5,0,4,8)->aaaBBAABBB`,
   `(5,0,9,8)->aaaaabbbba`, `(5,4,0,8)->AAAAbababb`,
   `(5,9,0,8)->aaaabbabab`, `(6,0,0,11)->aaBBBABBAB`.
3. **Girth.** `girth(Gamma)=6`. The word `w_g=aaBaaB` (`a.a.B.a.a.B`) is reduced
   and evaluates to `-I=[[12,0],[0,12]]`, hence identity in `G`.
   No reduced word of length `<=5` is `+-I`. Reduced-word census:
   L=1:4/0, 2:12/0, 3:36/0, 4:108/0, 5:324/0, 6:972/28 hits.
   All 28 length-6 identities (sorted):
   `AAbAAb, ABaBAb, AbAAbA, AbABaB, AbAbAb, AbaBab, AbbAbb, BAbABa, BBaBBa,`
   `BaBAbA, BaBBaB, BaBaBa, BaaBaa, BabAba, aBAbAB, aBBaBB, aBaBaB, aBaaBa,`
   `aBabAb, aaBaaB, abAbaB, bAAbAA, bABaBA, bAbAbA, bAbaBa, bAbbAb, baBabA,`
   `bbAbbA` (12 `+I`, 16 `-I`; both identity in PSL).
   Auxiliary: L=7:2916/0, L=8:8748/120, L=9:26244/0, L=10:78732/536.

Both words replay by pure `2x2` matrix multiplication mod 13 (stdlib only, <1 s).

## Proof / evidence (machine-assisted exhaustive)

- **Order.** Theory: `|SL(2,q)|=q(q^2-1)` for prime `q` (ordered bases:
  `(q^2-1)(q^2-q)` invertible matrices divided by `q-1` determinants).
  For `q=13`: `13*168=2184`. Center `{+-I}` size 2 (`-I!=I`, `det(-I)=1`), so
  `|PSL|=1092`. Independently brute-forced: all `13^4=28561` matrices,
  `det==1` count 2184, canonical classes 1092.
- **BFS diameter.** Single-source BFS from `canon(I)` over canonical classes
  using only `mm`. Visited 1092 vertices => connected => `<a,b>=G`. Frontier
  sizes as above; max depth 10; ball `<=9` has 1082 vertices. Two neighbor
  orders give identical distributions. Independent word-tree search confirms no
  reduced word of length `<=9` evaluates to target class `(5,0,9,8)`; `w_D` of
  length 10 attains it, so distance exactly 10 and diameter exactly 10.
- **Girth.** Two independent codes plus auditor reimplementation enumerate all
  `4*3^{L-1}` reduced words per length, testing `==+I or ==-I`: 0 hits for
  L=1..5 (484 words), 28 hits for L=6 (972 words). Hence shortest reduced
  identity has length 6. Witness `aaBaaB -> -I` verified stepwise:
  `a^2=[[1,2],[0,1]]`, `*B`, `*a`, `*a`, `*B` equals `[[12,0],[0,12]]`.
- **Regularity.** 4 neighbors of identity pairwise distinct; L=2 zero hits
  excludes collapse, so 4-regular.

## Limitations

- Single stratum `(p,S)=(13,{transvection pair})`; no general diameter/girth
  theorem.
- Proof is machine-assisted (short Python programs); trust base is integer
  arithmetic + BFS/DFS logic, cross-checked by two code paths, opposite
  neighbor orders, alternative canonicalization, and from-scratch replay.
  No external CAS or library.
- Conventions fixed: undirected Cayley graph, girth over reduced words,
  PSL identity `=+-I`. Directed or unreduced counts differ trivially.

## Reproducibility

```
python3 output/artifacts/replay.py        # all claims <1 s
python3 output/artifacts/bfs_diameter.py  # census + diametral words
python3 output/artifacts/girth_enum.py 8  # girth census to length 8
```

`replay.py` asserts: SL order; inverses; `w_g->-I` reduced; L<=5 exhaustion;
L=6 census 972/28; BFS coverage 1092 with exact spheres and D=10;
`w_D->(5,0,9,8)` at distance 10; no reduced `<=9` to target; 4-regularity.

## References

- Martino Garonzi, Zoltan Halasi, Gabor Somlai. On the diameter of Cayley
  graphs of classical groups with generating sets containing a transvection.
  https://arxiv.org/abs/2203.03323 — polylog asymptotic bound only, no exact
  p=13 table.
- Zoltan Halasi. Diameter of Cayley graphs of SL(n,p) with generating sets
  containing a transvection. https://arxiv.org/abs/2002.10443 — asymptotic
  bound, no exact census.
- Haimiao Chen. Regular balanced Cayley maps on PSL(2,p).
  https://arxiv.org/abs/1601.05251 — surface-embedding classification, no word
  metric.
- Harald Helfgott. Growth and generation in SL2(Z/pZ).
  https://doi.org/10.4007/annals.2008.167.601 — growth implying O((log p)^c)
  diameter, no small-prime exact tables.
