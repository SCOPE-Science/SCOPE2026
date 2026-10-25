# Perfect-matching implication lattices: sharp Horn bases and chessboard topology

## Finding
For every integer \(n\ge2\), take the \(n^2\) positive atoms \(e_{ij}\), indexed by \((i,j)\in[n]\times[n]\), whose models are exactly the permutation matrices \(P_\sigma=\{e_{i,\sigma(i)}:i\in[n]\}\). Their logical consequence operator is
\[
c_n(S)=\bigcap_{\sigma:S\subseteq P_\sigma}P_\sigma,
\]
with the empty intersection (inconsistent premises) defined as the whole atom set \(E_n\). The complete statement is:

1. The closed sets are \(E_n\), the \(n!\) whole permutation matrices, and precisely the partial matchings of size at most \(n-2\). In particular, rank is \(n\), the number of closed sets is \(1+n!+\sum_{k=0}^{n-2}\binom nk^2k!\), and the rank polynomial is
\[
R_n(t)=\sum_{k=0}^{n-2}\binom nk^2k!\,t^k+n!t^{n-1}+t^n.
\]
Every internal coefficient is **strictly log-concave** with its two neighbors.

2. If implications have arbitrary finite (possibly multi-atom) conclusions and their cardinality, not total literal length, is minimized, a smallest complete Horn implication base has exactly four implications for \(n=2\), and, for \(n\ge3\), exactly
\[
\boxed{n^2(n-1)+n\,n!}
\]
implications. For \(n\ge3\), one premise is needed for every pair of conflicting atoms (two cells in the same row or column, with different other coordinate), concluding \(E_n\); one more for every \((n-1)\)-edge partial permutation, concluding its unique missing atom. For \(n=2\), the four singleton atoms imply the two atoms of their unique permutation. These are cardinality-minimal and **one synchronous round suffices for every input**. A smallest maximal premise cardinality among complete bases is \(n-1\) (including the \(n=2\) singleton case).

3. Let \(A\subseteq B\) be closed. The interval Möbius function is:
\[
\mu(A,B)=\begin{cases}
1,&A=B,\\
(-1)^{|B|-|A|},&B\ne E_n,\ |B|\le n-2,\\
(-1)^{m-1}(m-1),&A\text{ is partial},\ B=P_\sigma,\ m=n-|A|,\\
-1,&A=P_\sigma,\ B=E_n,\\
-\displaystyle\sum_{j=0}^{m}(-1)^j\binom mj^2j!,&A\text{ is partial},\ B=E_n,\ m=n-|A|.
\end{cases}
\]
The last case also equals \((-1)^{m+1}m!L_m(1)\) for the ordinary Laguerre polynomial \(L_m\). In particular \(\mu(\varnothing,E_n)=(-1)^{n+1}n!L_n(1)\).

4. For every partial closed matching \(A\) with \(m=n-|A|\ge2\), the interval \([A,E_n]\) is isomorphic to the same construction on the \(m\) unmatched rows and columns. The order complex of its proper open interval \((A,E_n)\) is **simple-homotopy equivalent** to the chessboard complex of matchings of \(K_{m,m}\). Hence existing chessboard-complex integral-homology results transfer directly to these logical consequence lattices, without a new homology computation.

## Assumptions and scope
Here \([n]=\{1,\ldots,n\}\) and all sets, lattices, and complexes are finite. A *partial matching* is a subset of \(E_n\) with no repeated row or column. Permutation matrices have exactly one cell in each row and column. The lattice order is inclusion of **closed atom sets**, not inclusion of permutation-model families; therefore its maximal element is \(E_n\), representing inconsistent premises. A Horn implication \(U\to V\) means that all atoms in \(V\) must be added whenever \(U\) is present. A synchronous round fires all rules whose premises are contained in the **original** input; no sequential derivation is assumed. \(L_m(x)=\sum_{j=0}^{m}\binom mj(-x)^j/j!\). We count each distinct multi-conclusion rule once; minimizing total premise/conclusion occurrences is a different optimization problem.

## Proof
**Closure and lattice.** A set containing two distinct edges sharing a row or a column has no permutation extension, hence closes to \(E_n\). A partial matching of size \(r\le n-2\) leaves at least two rows and two columns unmatched; among its \((n-r)!\) completing permutations, every unmatched cell is missing from at least one completion. Their common intersection is precisely the partial matching. If \(r=n-1\), the last row/column pair is forced, so the closure is its unique complete permutation. A complete permutation closes to itself. These alternatives exhaust every input and establish the listed closed sets. A size-\(k\) matching is chosen by two \(k\)-subsets and a bijection, yielding \(\binom nk^2 k!\). A full permutation covers the rank-\(n-2\) matchings it contains and is covered by \(E_n\); all other covering edges add one matching cell. This establishes grading and the rank counts.

**Sharp one-round implication basis.** For \(n\ge3\), define rules \(\{e_{ij},e_{ik}\}\to E_n\) for \(j\ne k\), and \(\{e_{ij},e_{kj}\}\to E_n\) for \(i\ne k\). There are \(2n\binom n2=n^2(n-1)\) distinct conflicting pairs. Every \((n-1)\)-matching \(F\) has a unique missing cell \(e\), and the rule \(F\to\{e\}\) is sound. There are \(n\,n!\) such distinct premises because each permutation has exactly \(n\) size-\(n-1\) subsets and none has two completions. If input is inconsistent, it contains a conflicting pair, so one round adds all atoms. If consistent, it is a matching: sizes at most \(n-2\) are closed, size \(n-1\) fires its completion rule, and size \(n\) is closed. Thus the base computes closure after one round.

Every listed premise is an *inclusion-minimal nonclosed set*: each proper subset of a conflicting pair is a matching with at most one edge and is closed for \(n\ge3\); each proper subset of a near-complete matching has at most \(n-2\) cells and is closed. A sound implication base deriving a new atom from a minimal nonclosed set must contain a rule whose premise is **exactly that set**, because every smaller premise would be closed and could not soundly add any atom outside it. Distinct minimal nonclosed sets therefore force distinct rules. This proves cardinality optimality. Since a near-complete matching cannot be enlarged from any smaller closed premise, the minimum possible maximum premise arity is at least \(n-1\), achieved above. When \(n=2\), every singleton is minimal nonclosed and determines its unique whole permutation, whereas each conflicting pair is already handled by those implications; exactly four singleton rules are necessary and suffice (again in one round).

**Möbius formulas.** Every interval between two partial matchings is Boolean, giving the stated sign. If a partial matching \(A\) of size \(r\le n-2\) is contained in a full permutation \(P\), with \(m=n-r\), the interval from \(A\) to \(P\) contains exactly the Boolean subsets of the \(m\) new cells except that ranks \(m-1\) and \(m\) have merged at the single top \(P\); all proper elements are subsets of size at most \(m-2\). Therefore the recurrence gives \(\mu(A,P)=-\sum_{j=0}^{m-2}(-1)^j\binom mj=(-1)^{m-1}(m-1)\). A complete permutation is covered only by \(E_n\), so its Möbius value to \(E_n\) is \(-1\). To compute \(\mu(A,E_n)\), the intermediate closed sets are matchings extending \(A\) by \(j\le m-2\) cells, of count \(\binom mj^2j!\), and the \(m!\) complete permutation extensions. The Möbius recurrence gives
\[
\mu(A,E_n)=-\left[\sum_{j=0}^{m-2}(-1)^j\binom mj^2j!+m!(-1)^{m-1}(m-1)\right].
\]
The last contribution is exactly the sum of the missing \(j=m-1\) and \(j=m\) terms of the full alternating rook polynomial, proving the formula. Reindexing this finite sum establishes its Laguerre identity.

**Strict log-concavity.** For \(r_k=\binom nk^2 k!\), the ratios \(r_{k+1}/r_k=(n-k)^2/(k+1)\) are strictly decreasing through \(k=n-3\). The exceptional final ratios are \(r_{n-1}/r_{n-2}=4/[n(n-1)]\) and \(r_n/r_{n-1}=1/n!\); for \(n\ge3\), \(9/(n-2)>4/[n(n-1)]>1/n!\). For \(n=2\), the rank vector is \((1,2,1)\), also strictly log-concave.

**Self-similarity and topology.** Fix a partial closed matching \(A\). Deleting its used row/column pairs identifies every extension within \([A,E_n]\) with a closed subset of the same construction on the remaining \(m\) rows and columns; in particular \([A,E_n]\cong L_m\). Let \(X\) be the poset of **nonempty** matchings of \(K_{m,m}\), ordered by inclusion, and \(Y=(\varnothing,E_m)\) the poset of nontrivial proper closed sets. The map \(f:X\to Y\), \(F\mapsto c_m(F)\), is well-defined, monotone and onto. For every \(C\in Y\), its principal-ideal inverse image is
\[
f^{-1}(Y_{\le C})=\{F:\varnothing\ne F\text{ is a matching},\ F\subseteq C\}.
\]
Since every \(C\in Y\) itself is a matching and is the maximum of this fiber, that fiber has a contractible order complex. McCord–Quillen's poset theorem, in its simple-homotopy strengthening, proves \(\Delta(X)\simeq_s\Delta(Y)\). The order complex \(\Delta(X)\) is the barycentric subdivision of the chessboard complex, which is simple-homotopy equivalent to that complex. All conclusions follow for \((A,E_n)\) by the interval isomorphism. This proves a transfer mechanism; the known homology of chessboard complexes is not reproved or claimed as new.

## Verification
The standalone `verify.py` enumerates the formal-context intersections from **all permutation models** independently of the classification. For \(n=2,3,4\) it checks that actual closed sets equal the claimed sets, evaluates **all 798** comparable ordered pairs by the defining Möbius recurrence, and verifies every displayed number and strict log-concavity. On all \(16+512+65536=66064\) raw atom subsets it independently computes model-intersection closure and the proposed one-round Horn closure, and checks minimal nonclosed premises. It also compares the exact reduced Euler characteristic of the chessboard complex with the bottom-to-top Möbius value. The completed run reports `VERIFY_OK`; general validity is proved above, not inferred from finite enumeration.

## Relationship to prior work
Rawson–Myers–Green–Robinson–Joslyn (2023) identify the general hypergraph intersection-complex/formal-concept-lattice relationship, motivating the explicit permutation-model incidence system but not supplying its specific implication base, Möbius formula, or topology. Bichoupan (2022) describes general implication-basis optimization and cites the canonical Guigues–Duquenne theorem, but its convex-geometry context does not classify this non-anti-exchange closure family. Barmak (2010) proves the general simple-homotopy poset fiber lemma applied here. Shareshian–Wachs (2004) give nontrivial chessboard-complex integral homology, which this theorem **imports** rather than extends. The identity with classical Laguerre polynomials and standard matching-complex Euler sums is acknowledged; the finite all-interval lattice and optimal Horn presentation constitute the evaluated combined claim.

## Limitations
The statement concerns positive atomic consequences of permutation models, not implications with negated atoms or arbitrary conjunctive/disjunctive formulas. Minimum implication *count* does not imply minimum total symbol length. The topological assertion is simple-homotopy equivalence, not simplicial isomorphism or a fresh integral-homology calculation. Literature searches cannot exclude an equivalent result expressed in rook monoids, permutation intersection lattices, functional-dependency theory, or implicational systems, particularly in non-indexed sources; independent publication-priority verification is outstanding.

## References
1. M. G. Rawson, A. Myers, R. Green, M. Robinson, C. Joslyn, *Formal Concept Lattice Representations and Algorithms for Hypergraphs*, arXiv:2307.11681v1 (2023), https://arxiv.org/abs/2307.11681.
2. T. Bichoupan, *Complexity Results for Implication Bases of Convex Geometries*, arXiv:2211.08524v1 (2022), https://arxiv.org/abs/2211.08524.
3. J. A. Barmak, *On Quillen's Theorem A for Posets*, arXiv:1005.0538v1 (2010), https://arxiv.org/abs/1005.0538.
4. J. Shareshian, M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054v1 (2004), https://arxiv.org/abs/math/0409054.
