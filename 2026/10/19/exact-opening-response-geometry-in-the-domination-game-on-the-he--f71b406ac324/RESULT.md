# Exact opening-response geometry in the domination game on the Heawood and Pappus graphs

## Finding

In the standard closed-neighborhood domination game with Dominator minimizing and Staller maximizing the number of turns, the Heawood graph \(H\) and the Pappus graph \(P\) satisfy
\[
\bigl(\gamma_g(H),\gamma'_g(H)\bigr)=(7,6),\qquad
\bigl(\gamma_g(P),\gamma'_g(P)\bigr)=(8,7).
\]
The prime denotes the Staller-start convention. Both graphs are *minus* in the standard terminology: playing first as Dominator costs one more move than playing first as Staller.

More precisely, fix **any** legal opening vertex \(u\), let the other player choose a legal reply \(v\), and let \(d=d_G(u,v)\). The following table gives the **total eventual length**, assuming optimal alternating play **after the first two specified moves**. Each parenthesized multiplicity is the number of legal choices of \(v\) at that distance, for each fixed \(u\).

| Graph | Distance \(d\) | Legal replies at distance \(d\) | First turn Dominator | First turn Staller |
|---|---:|---:|---:|---:|
| Heawood | 1 | 3 | 7 | 6 |
| Heawood | 2 | 6 | 5 | 6 |
| Heawood | 3 | 4 | 5 | 6 |
| Pappus | 1 | 3 | 8 | 8 |
| Pappus | 2 | 6 | 7 | 8 |
| Pappus | 3 | 6 | 7 | 8 |
| Pappus | 4 | 2 | 7 | 7 |

Consequently, after any Dominator opening, Staller can obtain the optimum only by playing an **adjacent** vertex, for either graph. After any Staller opening, **every** legal reply by Dominator is optimal on the Heawood graph, whereas on the Pappus graph **only** its two distance-four replies are optimal. These rules classify all first-two-move optimality choices, not merely the two starting scores.

## Assumptions and scope

All graphs are finite, simple and undirected. Choosing a vertex \(v\) is legal exactly when its closed neighborhood \(N[v]\) contains at least one as-yet-undominated vertex; no passes are allowed. On each turn the acting player chooses optimally against the opponent's optimal later play. The chosen vertices jointly dominate their closed neighborhoods, and the game ends when every vertex is dominated. Counts include both the opening moves and all subsequent turns.

Define the Heawood graph to have points \(p_i\) and lines \(\ell_j\), with \(i,j\in\mathbb Z/7\mathbb Z\), and incidence
\[
p_i\sim\ell_j\quad\Longleftrightarrow\quad i-j\in\{0,1,3\}\pmod 7.
\]
Thus \(H\) has 14 vertices and 21 edges. The set \(\{0,1,3\}\) is the cyclic difference-set presentation of the Fano projective plane.

Define the Pappus graph to have points \(p_{x,y}\) and lines \(\ell_{m,b}\), all four coordinates in \(\mathbb F_3\), and incidence
\[
p_{x,y}\sim\ell_{m,b}\quad\Longleftrightarrow\quad y=mx+b\quad\text{in }\mathbb F_3.
\]
This incidence graph of the affine \(3\)-net with its vertical parallel class omitted has 18 vertices and 27 edges. No assertion is made about a larger infinite family of incidence graphs.

## Proof

**Minimax reduction.** Index the vertices from zero to \(n-1\), use a bitmask \(U\) for the already dominated set, let \(B_v\) be the bitmask of \(N[v]\), and let \(M=2^n-1\). Write \(D(U)\) and \(S(U)\) for the number of additional moves under optimal play when Dominator or Staller moves next, respectively. Then
\[
D(M)=S(M)=0,
\]
and, for every \(U\ne M\),
\[
\begin{aligned}
D(U)&=1+\min_{v:\,B_v\setminus U\ne\varnothing} S(U\cup B_v),\\
S(U)&=1+\max_{v:\,B_v\setminus U\ne\varnothing} D(U\cup B_v).
\end{aligned}
\]
The set difference and union are set operations, implemented as bitmasks. If \(U\ne M\), a legal move exists because any undominated vertex may itself be selected; its closed neighborhood contains that vertex. Every legal transition strictly enlarges \(U\), proving that decreasing integer-mask order computes the unique exact values by backward induction. This is **exhaustive**, not a sampled search. The already dominated mask contains all information relevant to subsequent legality and scores, so the recurrence does not omit history-dependent choices.

The two initial game values are \(D(\varnothing)\) and \(S(\varnothing)\). For an opening at \(u\) and legal reply at \(v\), the game lasts
\[
2+D(B_u\cup B_v)\quad\text{if Dominator opened},
\]
or
\[
2+S(B_u\cup B_v)\quad\text{if Staller opened}.
\]
The identity of the player after the second turn is the opener in each case.

**Independently generated graphs and exhaustive values.** `verify_recursive.py` constructs Heawood using the cyclic difference set and Pappus using the affine equations, and computes only reachable dominated masks through memoized recursion. `verify_tabular.py` constructs Heawood independently from orthogonal nonzero binary vectors, Pappus from parallel classes of affine linear functions, and computes \(D(U),S(U)\) for **every** possible dominated mask. The first approach evaluates 2,216 cached game states for \(H\) and 11,836 for \(P\); the second evaluates all \(2^{14}=16,384\) and \(2^{18}=262,144\) masks, respectively, for both players. The independently generated graphs both have the required vertex degrees, edge counts and distance distributions. Both algorithms return identical starting scores and every entry in the table, explicitly iterating all opening vertices and all legal second vertices.

**Opening-vertex invariance.** In the Fano presentation, simultaneous cyclic translations \(p_i\mapsto p_{i+a}\), \(\ell_j\mapsto\ell_{j+a}\) act transitively separately on points and lines; the incidence-preserving involution \(p_i\leftrightarrow\ell_{-i}\) exchanges the two classes. In the Pappus presentation, affine point translations and corresponding line-label translations act transitively on points, shears \((x,y)\mapsto(x,y+tx)\) act transitively on slopes, and the incidence-preserving duality
\[
p_{x,y}\longleftrightarrow \ell_{x,-y},
\qquad
\ell_{m,b}\longleftrightarrow p_{m,-b}
\]
exchanges the two bipartite classes. Therefore both graphs are vertex-transitive, and the second-move score depends on the first vertex only through an automorphism and is constant for each distance class in the table. This geometric argument agrees with the independent direct check for **every** opening vertex. The tables, the extremal choice at the second turn and backward induction prove all assertions.

## Verification

All code uses Python 3 standard library only. Run `python3 verify_recursive.py` and `python3 verify_tabular.py` from the directory containing those files. Compare the exact output to `verify_recursive.out` and `verify_tabular.out`. The first output ends `VERIFY_OK`; the second ends `INDEPENDENT_VERIFY_OK`. Both directly assert graph cubicity, incidence symmetry, starting values, table multiplicities and the invariance of the table under all opening vertices. In particular, the second enumerator includes unreachable dominated masks: the proof of the recurrence ensures its answers on the reachable masks are exact.

## Relationship to prior work

Brešar, Klavžar and Rall introduced and analyzed this domination-game convention, including general inequalities for the two starting players, but the inspected paper does not contain the exact Heawood/Pappus opening-response table. Brešar, Dorbec, Klavžar and Košmrlj investigated *minus* and *bluff* graphs and tabulated generalized Petersen graphs. Their table does not subsume the present graphs: generalized Petersen graphs with respectively 14 or 18 vertices have an **odd** outer cycle of length 7 or 9, while both incidence graphs here are bipartite. Goldberg, Rajendraprasad and Mathew studied **ordinary** domination in incidence graphs of designs; their domination-number statements do not imply minimax game lengths or optimal second-move distances. The main contribution is the complete two-ply optimality classification on these two natural bipartite incidence geometries, not the definitions, general inequalities or known ordinary domination parameters.

## Limitations

The result is finite and specific to these two named graphs; it is not a theorem about all projective planes or nets. The proof is a reproducible exhaustive finite computation under the stated move convention, supplemented by structural vertex-transitivity arguments, **not** a short symbolic closed form for the minimax values. Similar computations may exist in unindexed sources; searches of accessible records cannot prove unique novelty. No independently commissioned external audit is claimed.

## References

1. B. Brešar, S. Klavžar and D. F. Rall, *Domination Game and an Imagination Strategy*, SIAM Journal on Discrete Mathematics 24 (2010), 979–991. DOI: 10.1137/100786800. Author manuscript: https://users.fmf.uni-lj.si/klavzar/preprints/GameDomFinal.pdf.
2. B. Brešar, P. Dorbec, S. Klavžar and G. Košmrlj, *How Long Can One Bluff in the Domination Game?*, author preprint (2015): https://users.fmf.uni-lj.si/klavzar/preprints/BluffGraphs-Feb-16-2015.pdf. DOI: 10.7151/dmgt.1899.
3. D. Goldberg, S. Rajendraprasad and R. Mathew, *Domination in Designs*, 2014, arXiv:1405.3436v1, https://arxiv.org/html/1405.3436v1.
