# A matching-edge jump and exact preference obstructions in stable graph colouring

## Finding

For integers \(m,r\geq 0\) with \(n=2m+r\geq1\), let
\[
G_{m,r}=\overline{K_2}\vee(mK_2\sqcup rK_1).
\]
The two vertices \(u,v\) in \(\overline{K_2}\) are nonadjacent; every vertex in the opposite part is adjacent to each of them, and the only edges within the opposite part form a matching of size \(m\). For the preference-stable chromatic number,
\[
\boxed{\chi_{\mathrm{stable}}(G_{m,r})=
\begin{cases}
2,&n=1,\\
3,&n\ge2\text{ and }(m=0\text{ or }n=2),\\
4,&n\ge3\text{ and }m\ge1.
\end{cases}}
\]
For \(m\ge1\) and \(n\ge3\), the Grundy number remains \(\Gamma(G_{m,r})=3\), so the stable chromatic number strictly exceeds this standard lower bound.

On the five-vertex graph \(F=G_{1,1}\), exactly \(624\) of the \((3!)^5=7776\) profiles of strict rankings of three named colours admit no stable proper three-colouring. Of these \(624\), exactly \(576\) force a mutually envying adjacent pair in *every* proper three-colouring; the remaining \(48\) allow a proper assignment without any mutually envying pair, but every proper assignment still has a directed blocking cycle. The obstruction proportion is therefore \(13/162\); the two subproportions are \(2/27\) and \(1/162\).

## Assumptions and scope

All graphs are finite, simple, undirected. A proper \(k\)-colouring assigns a colour in \([k]=\{1,\ldots,k\}\) to each vertex, with distinct colours at adjacent vertices. Each vertex strictly ranks the \(k\) named colours. Given a colouring and rankings, the *envy digraph* has an arc \(a\to b\) when \(ab\) is an edge and vertex \(a\) ranks \(b\)'s colour strictly above its own. A proper colouring is *stable* when the envy digraph is acyclic. The number \(\chi_{\mathrm{stable}}(G)\) is the least \(k\) for which a stable \(k\)-colouring exists for every possible ranking profile. The exact profile counts concern a fixed labelled \(F\), with independently named colours; they are not counts modulo automorphisms or palette relabelling.

## Proof

**Reachability upper bounds.** We use the established bound of Koana--Oh--Yoneda (Theorem 3.1 in the reference below): if an acyclic orientation has at most \(q\) reachable vertices (including the starting vertex) from every vertex, then every ranking profile has a stable proper \(q\)-colouring. For \(n\ge3\), orient every join edge from its endpoint in the \(n\)-vertex part toward \(u,v\), and orient each matching edge from one endpoint to the other. This is acyclic. A matched edge's initial endpoint reaches itself, its mate, and \(u,v\); a matched edge's final endpoint reaches itself and \(u,v\); an isolated opposite-part vertex reaches itself and \(u,v\); the vertices \(u,v\) reach only themselves. Thus \(\chi_{\mathrm{stable}}\le4\) if a matching edge exists, and \(\chi_{\mathrm{stable}}\le3\) otherwise. For \(n=1,2\), orient all join edges away from \(u,v\) and each possible matching edge consistently from one endpoint to the other. Reachability is at most \(n+1\), giving upper bounds \(2\) for \(n=1\) and \(3\) for \(n=2\).

**Sharp lower bounds.** If \(n=1\), the graph contains an edge, and the upper bound \(2\) is sharp. If \(m=0\) and \(n\ge2\), the graph is \(K_{2,n}\), whose stable chromatic number is \(3\) by Koana--Oh--Yoneda, Proposition 3.7 (alternatively, it contains a four-vertex path forcing the Grundy lower bound \(3\)). If \(n=2,m=1\), the graph contains a triangle and hence needs \(3\) colours.

For \(n\ge3,m\ge1\), select a matching edge \(xy\) and any other opposite-part vertex \(z\). Together with \(u,v\), these vertices induce \(F=G_{1,1}\), whose edges are \(ux,uy,uz,vx,vy,vz,xy\). Put the following strict rankings on the named colours \(1,2,3\), favourite first:

| Vertex | Ranking |
|---|---|
| \(u\) | \(3\succ2\succ1\) |
| \(v\) | \(1\succ2\succ3\) |
| \(x\) | \(2\succ1\succ3\) |
| \(y\) | \(1\succ3\succ2\) |
| \(z\) | \(3\succ1\succ2\) |

In every proper three-colouring, \(u\) and \(v\) must receive the same colour \(a\); otherwise the adjacent pair \(x,y\) cannot receive two distinct remaining colours. The pair \(x,y\) uses the other two colours in either order; \(z\) uses one of those two, giving exactly \(3\cdot2\cdot2=12\) assignments. Direct comparison of the five rankings shows the following forced mutually envying pair for each possibility for \((a,\phi(x),\phi(y))\), irrespective of the choice of \(\phi(z)\):

| \((a,\phi(x),\phi(y))\) | Forced pair |
|---|---|
| \((1,2,3)\) | \(u,y\) |
| \((1,3,2)\) | \(u,x\) |
| \((2,1,3)\) | \(v,x\) |
| \((2,3,1)\) | \(u,x\) |
| \((3,1,2)\) | \(v,y\) |
| \((3,2,1)\) | \(v,z\) |

Therefore no proper three-colouring of \(F\) is stable. Extend the ranking profile arbitrarily to additional vertices of \(G_{m,r}\). Restricting a stable colouring to \(F\) would give a stable colouring of \(F\), contradicting the obstruction. This also uses the standard subgraph monotonicity of the invariant (Koana--Oh--Yoneda, Proposition 3.4). Hence the upper bound \(4\) is sharp.

**Grundy number.** A triangle gives \(\Gamma(G_{m,r})\ge3\). In any Grundy colouring, \(u,v\) have the same colour \(a\): if they had colours \(a<b\), the vertex with colour \(b\) would need a neighbour with colour \(a\), which is impossible because \(u,v\) are nonadjacent and every opposite-part vertex is adjacent to both. Every opposite-part vertex has at most one neighbour within its part and sees only colour \(a\) among its neighbours in \(\{u,v\}\), so it has at most two distinct neighbour colours and can use Grundy colour at most \(3\). If \(a\ge4\), the vertices \(u,v\) would require an opposite-part neighbour of colour \(3\), but that vertex could not see both lower colours \(1,2\): its two hub-neighbours have colour \(a\ge4\), and it has at most one other neighbour. Thus \(a\le3\) as well. Consequently \(\Gamma(G_{m,r})=3\).

**Exact obstruction census.** On \(F\), each vertex has \(3!=6\) strict rankings; hence there are exactly \(6^5=7776\) complete profiles. For each profile enumerate the \(12\) proper colour assignments above, form each envy digraph from the edge definition, and test directed acyclicity. To subdivide the profiles with no stable assignments, test whether at least one proper assignment avoids all mutually envying adjacent pairs. A finite exhaustive checker implements this algorithm in `verify.py`. Two separate cycle criteria, a three-state depth-first search and Boolean transitive closure, agree on every enumerated profile and return respectively \(624\) with no stable three-colouring, \(576\) with an unavoidable mutual pair, and \(48\) obstructed only by longer cycles. Exhaustiveness follows from enumerating all \(6^5\) rankings and all \(12\) proper assignments; these are finite exact counts, not statistical estimates.

## Verification

Run `python3 verify.py` with Python 3 and no external packages. It rederives proper assignments from the edge list, tests the explicit obstruction on all \(12\) assignments, independently compares depth-first search and Boolean-closure cycle detection on every one of the \(7776\) profiles, and directly checks the acyclic-orientation reachability bound for a finite range of \(m,r\). The unrestricted structural theorem follows from the proof above; finite orientation checks are corroboration only. The complete finite obstruction census follows from exhaustive enumeration, subject to ordinary executable-implementation verification; no independent mathematical audit has been performed.

## Relationship to prior work

Koana, Oh and Yoneda introduced this stable-colouring invariant, proved its acyclic-orientation reachability upper bound and subgraph monotonicity, proved the Grundy lower bound, and computed the invariant for \(K_{a,b}\), paths and cycles. Their result for \(K_{2,n}\) supplies the zero-matching baseline \(3\), but it does not imply the jump to \(4\) from a single added matching edge: the Grundy lower bound remains \(3\), while the new explicit five-vertex preference profile forces \(4\). The present theorem combines that obstruction with a uniform matching orientation and an exact census for the minimal obstruction. Previously published results for a particular complete tripartite graph concern different graphs, and no covering statement was identified in the checked literature or mathematical records. This is not a proof of historical uniqueness.

## Limitations

The formula requires two independent universal-to-the-other-part vertices and maximum degree one inside that part. It does not characterize arbitrary split, multipartite or near-bipartite graphs. The exact profile census is only for \(F=G_{1,1}\) and exactly three named colours; it is not a universal profile census for all \(G_{m,r}\). Full historical priority remains provisional, and the checks are not independent certification.

## References

1. T. Koana, Y. Oh, and H. Yoneda, *Graph Coloring with Color Preferences*, arXiv:2609.00569, first public 2026-09-01, https://arxiv.org/abs/2609.00569. Used for definitions, Theorems 3.1 and 3.3, Propositions 3.4 and 3.7.
2. *Stable chromatic number of the complete tripartite graph* \(K_{2,3,3}\), mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-stable-chromatic-number-of-the-complete-tripartite-graph-k-2-3-3--b34a81e3d305. Closest semantically indexed comparison, distinct graph family and proof requirements; only the public summary was available for comparison.
