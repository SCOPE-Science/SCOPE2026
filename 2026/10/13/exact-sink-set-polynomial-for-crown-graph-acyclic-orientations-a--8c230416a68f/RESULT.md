# Exact sink-set polynomial for crown-graph acyclic orientations and a cubical nonreal-rootedness obstruction

## Finding

Let \(\operatorname{Cr}_n\) have classes \(\{a_1,\ldots,a_n\}\) and \(\{b_1,\ldots,b_n\}\), with edge \(a_i b_j\) exactly when \(i\ne j\). For any acyclic orientation \(\omega\), its sink set consists of those vertices whose incident edges all point inward. Define its full labeled-sink polynomial by
\[
\mathcal A_n(\mathbf x,\mathbf y)=\sum_{\omega\text{ acyclic}}\prod_{a_i\in\operatorname{Sink}(\omega)}x_i\prod_{b_j\in\operatorname{Sink}(\omega)}y_j.
\]
For integers \(0\le m\le n\), put
\[
B_{m,n}=\sum_{p=0}^m\sum_{k=0}^p(-1)^{m+p}p!\binom{m}{k}R(m-k,p-k)(p+1)^{n-k}p^k,
\]
where \(R(d,e)\) is the number of partitions of a \(d\)-set into \(e\) blocks of cardinality at least two, \(R(0,0)=1\), and \(0^0=1\). Then, for every \(n\ge3\),
\[
\boxed{\mathcal A_n(\mathbf x,\mathbf y)=\sum_{I\subseteq[n]}B_{n-|I|,n}\prod_{i\in I}(x_i-1)+\sum_{J\subseteq[n]}B_{n-|J|,n}\prod_{j\in J}(y_j-1)-B_{n,n}+B_{n-1,n-1}\sum_{i=1}^n(x_i-1)(y_i-1).}
\]
The unlabeled sink-count distribution is therefore
\[
\boxed{\mathcal A_n(t)=2\sum_{s=0}^n\binom ns B_{n-s,n}(t-1)^s-B_{n,n}+nB_{n-1,n-1}(t-1)^2.}
\]
For example,
\[
\mathcal A_3(t)=30t+30t^2+2t^3,\qquad \mathcal A_4(t)=1064t+740t^2+56t^3+2t^4.
\]
The graph \(\operatorname{Cr}_4\) is isomorphic to the three-dimensional cube \(Q_3\). Its polynomial is \(2t(t^3+28t^2+370t+532)\); the discriminant of the cubic factor is \(-50430544<0\), so the cube sink polynomial is not real-rooted.

## Assumptions and scope

All graphs are finite, simple, and labeled. The integer \(n\) ranges over all \(n\ge3\), and variables commute. A sink has outdegree zero; directed cycles of any length disqualify an orientation. In products over the empty set we use \(1\), including \(0^0=1\) when evaluating the explicit finite sum for \(B_{m,n}\). For other entries \(R(d,e)=0\) if no partition of the stipulated type exists, and its values can be computed from
\[
R(d,e)=\sum_{j=0}^d(-1)^j\binom dj S(d-j,e-j),
\]
where \(S(a,b)\) denotes a Stirling number of the second kind under its standard zero conventions. The result supplies the exact number of orientations for any prescribed sink subset by coefficient extraction in the displayed multivariate polynomial. It does not claim any general real-rootedness classification for larger crown graphs.

## Proof

**1. An exact color-class computation.** Let \(H_{m,n}\) be the bipartite graph with \(m\) left vertices \(a_1,\ldots,a_m\), \(n\) right vertices \(b_1,\ldots,b_n\), and edges \(a_i b_j\) when \(i\ne j\). Fix an integer \(q\ge1\) and a proper coloring of the left class. If that coloring uses \(p\) distinct colors, its color classes form a partition into \(p\) blocks. If exactly \(k\) of those blocks are singletons, the number of such partitions is \(\binom mk R(m-k,p-k)\); the number of injective assignments of \(p\) distinct colors to the blocks is the falling factorial \((q)_{\underline p}\). Every right vertex \(b_i\) with \(i\le m\) may use \(q-p+1\) colors if \(\{a_i\}\) is a singleton block, because its matched color occurs on no left neighbor. Otherwise it has \(q-p\) choices. The other \(n-m\) right vertices always have \(q-p\) choices. Therefore the chromatic polynomial is exactly
\[
\chi_{H_{m,n}}(q)=\sum_{p=0}^m\sum_{k=0}^p\binom mk R(m-k,p-k)(q)_{\underline p}(q-p)^{n-k}(q-p+1)^k.
\]
This is a polynomial identity since it holds for all integers \(q\ge1\). Stanley's acyclic-orientation evaluation says that the number of acyclic orientations of a graph on \(m+n\) vertices is \((-1)^{m+n}\chi(-1)\). Substituting \(q=-1\), observing \((-1)_{\underline p}=(-1)^p p!\), yields precisely \(B_{m,n}\). In particular \(B_{0,n}=1\).

**2. A sink-marking identity.** For any simple graph \(G\) and each vertex variable \(z_v\), expand
\[
\prod_{v\in\operatorname{Sink}(\omega)}z_v=\prod_{v\in V(G)}\big(1+(z_v-1)\mathbf1_{v\in\operatorname{Sink}(\omega)}\big).
\]
For any fixed independent subset \(S\subseteq V(G)\), acyclic orientations having every member of \(S\) as a sink correspond bijectively to the acyclic orientations of \(G-S\): orient all edges meeting \(S\) toward \(S\), and orient remaining edges arbitrarily provided they are acyclic. No directed cycle can traverse \(S\). If \(S\) is not independent, it cannot consist of sinks. Summing the product expansion gives the exact universal identity
\[
\sum_{\omega\text{ acyclic}}\prod_{v\in\operatorname{Sink}(\omega)}z_v=\sum_{S\text{ independent}}\operatorname{AO}(G-S)\prod_{v\in S}(z_v-1),
\]
where \(\operatorname{AO}(H)\) is the number of acyclic orientations of \(H\).

**3. Independent subsets in the crown.** Every independent subset of \(\operatorname{Cr}_n\) is contained entirely in one bipartition class, or is a matched pair \(\{a_i,b_i\}\). Indeed any pair of vertices in opposite classes is adjacent unless their indices coincide; a mixed independent set thus cannot contain a third vertex. Subsets lying in one class are counted twice when empty, so we subtract the empty-set term once. If \(I\subseteq[n]\) is removed from the \(a\)-class, the residual graph is \(H_{n-|I|,n}\) after relabeling its matched pairs. Removing both vertices of one pair gives \(H_{n-1,n-1}\). Substituting the exact counts from Step 1 into the identity in Step 2 proves the displayed multivariate formula, without approximation or omitted cases.

**4. Ordinary specialization and the cubical obstruction.** Set all \(2n\) variables to \(t\) and group subsets by cardinality. This proves the second displayed formula. Evaluating the explicit integer sums gives \(\mathcal A_3(t)=30t+30t^2+2t^3\) and \(\mathcal A_4(t)=2t(t^3+28t^2+370t+532)\). A direct cubic discriminant calculation gives \(-50430544\), hence one real and two nonreal roots for that cubic. Since \(\operatorname{Cr}_4\cong Q_3\), the claimed nonreal-rootedness statement follows. This finishes the proof for every stated \(n\).

## Verification

Run `python3 verify.py` using only the Python standard library. The checker compares the restricted-Stirling chromatic formula against direct proper colorings in 72 finite cases, enumerates every orientation bitstring for \(n=2,3,4\), independently rejects directed cycles, checks all sink counts and six multivariate evaluations, verifies formulas through \(n=6\), and evaluates the exact cubic discriminant. Expected output:

`VERIFY_OK color_checks=72 orientation_bitstrings=4164 multivariate_checks=6 cubic_discriminant=-50430544`

The direct finite enumerations are corroboration only. The arbitrary-\(n\) assertion is proved by the exact partition and sink-marking bijections above.

## Relationship to prior work

Gebhard and Sagan's 1999 paper gives proofs of the Greene–Zaslavsky unique-sink theorem and recalls Stanley's acyclic-orientation evaluation; it does not give a crown-specific labeled sink enumerator. Hwang, Jung, Lee, Oh and Yu give general acyclic-orientation sink-polynomial identities and chromatic-symmetric-function connections. Their general framework motivates the present specialization but does not state the restricted-Stirling evaluation for matching-deleted bicliques or the three-cube discriminant. The MathWorld/OEIS crown-graph *chromatic invariant* (A295171) concerns a derivative at \(q=1\), a different scalar invariant from the full sink distribution and its polynomial roots. Prior generic graph algorithms imply computability of every specialization, but do not themselves supply the closed family expression and this explicit non-real-rooted example.

## Limitations

The polynomial counts orientations of the graph \(K_{n,n}-M_n\) only, not orientations of arbitrary complete-bipartite subgraphs; its chromatic intermediate \(H_{m,n}\) handles a specific partial matching deletion. The displayed non-real-rootedness conclusion is proved for the cube \(Q_3\), not for every \(\operatorname{Cr}_n\). Related graph-enumeration literature may contain less readily indexed versions of the crown-specific formulas. No independent mathematical audit is claimed.

## References

1. D. D. Gebhard and B. E. Sagan, *Sinks in Acyclic Orientations of Graphs*, arXiv:math/9907078v1 (first public version 1999-07-12), *Journal of Combinatorial Theory, Series B* 80 (2000), 130–146. https://arxiv.org/abs/math/9907078
2. B.-H. Hwang, W.-S. Jung, K.-J. Lee, J. Oh and S.-H. Yu, *Acyclic orientation polynomials and the sink theorem for chromatic symmetric functions*, arXiv:1910.10920 (first public version 2019-10-24). https://arxiv.org/abs/1910.10920
3. OEIS A295171, *Chromatic invariant of the n-crown graph* (a different invariant), https://oeis.org/A295171; E. W. Weisstein, *Chromatic Invariant*, Wolfram MathWorld, https://mathworld.wolfram.com/ChromaticInvariant.html.
