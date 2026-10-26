# Rook-Möbius rank–index census of nilpotent multipartite partial isometries

## Finding
For each integer \(k\ge3\) and positive integers \(n_1,\ldots,n_k\), the nilpotent elements of the partial-isometry inverse monoid of the complete multipartite graph \(G=K_{n_1,\ldots,n_k}\) have the following **exact simultaneous rank and nilpotency-index polynomial**. Let \(I_k\) be the set of all partial injective maps from \([k]\) to \([k]\), and put
\[
\mu_h=\sum_{j=0}^{h}(-1)^j\binom hj^2j!,\qquad h\ge0.
\]
For \(\pi\in I_k\) and \(L\ge1\), define the finite polynomial
\[
H_{\pi,L}(\mathbf x,u)=\sum_{a=1}^k\ \sum_{\substack{1\le j\le L\\\pi^0(a),\ldots,\pi^{j-1}(a)\text{ defined}}}u^{j-1}\prod_{s=0}^{j-1}x_{\pi^s(a)}.
\]
Here \(\pi^0(a)=a\), including when \(a\notin\operatorname{dom}\pi\); a positive iterate is defined only when all preceding arrows exist. Set
\[
B_{\mathbf n,L}(u)=\left(\prod_{i=1}^k n_i!\right)
[x_1^{n_1}\cdots x_k^{n_k}]
\sum_{\pi\in I_k}\mu_{k-|\operatorname{dom}\pi|}
\exp(H_{\pi,L}(\mathbf x,u)).
\]
Then \([u^r]B_{\mathbf n,L}(u)\) is exactly the number of nilpotent partial isometries with domain rank \(r\) and nilpotency index **at most** \(L\). Taking \(B_{\mathbf n,0}=0\), the complete joint distribution is
\[
\boxed{\sum_{L=1}^{N}v^L\bigl(B_{\mathbf n,L}(u)-B_{\mathbf n,L-1}(u)\bigr),\quad N=\sum_i n_i.}
\]
This is a finite coefficient formula: \(I_k\) has \(\sum_{j=0}^k\binom kj^2j!\) members, and every coefficient of each exponential only uses finitely many terms.

For \(n_i\ge2\), put \(c_s=|\{i:n_i\ge s\}|\), with \(c_s=0\) beyond the largest part. The largest nilpotency index in this monoid is
\[
\boxed{M(\mathbf n)=\max_{1\le s\le\max n_i}(s c_s+c_{s+1}).}
\]
Moreover, \(M(\mathbf n)=N\) if and only if the part sizes differ by at most one. When this happens, write \(m=\min_i n_i\) and \(h=|\{i:n_i=m+1\}|\); the number of nilpotent partial isometries of index \(N\) is exactly
\[
\boxed{h!(k-h)!\prod_{i=1}^k n_i!.}
\]
For instance, the total nilpotent counts for \(K_{2,2,2}\) and \(K_{3,2,2}\) are respectively \(835\) and \(3089\); their maximum indices are \(6\) and \(7\), with \(48\) elements at the maximum in each case.

## Assumptions and scope
The graph is finite, simple, connected, and equipped with its usual shortest-path metric. Its \(k\ge3\) partite classes are specified and nonempty; for the maximum-index formula and spanning-index criterion, all classes have size at least two. A partial isometry is a bijection between two subsets preserving pairwise graph distances. Its rank is the size of its domain. The empty map is zero. For a nilpotent partial map \(f\), the index \(\nu(f)\) is the least positive \(L\) with \(f^L=0\), so \(\nu(0)=1\). Products are composition of partial maps. All variables in the generating series are formal, and \(\exp\) is its formal power series.

## Proof
**Part-action lemma.** Distinct vertices have distance two precisely when they belong to the same part, and distance one precisely when they belong to different parts. Thus a partial isometry sends every represented source part into a single target part, and different represented source parts go to different target parts. The resulting partial injection \(\theta_f\in I_k\), defined exactly on parts containing a domain point, is unique. Conversely, any partial injection between the parts and any injective partial maps along its arrows give a partial isometry. This remains true if a represented part contributes only one point.

**Cycle-free chains and the exponent.** Every finite partial permutation decomposes uniquely into directed cycles and directed chains (singletons included). It is nilpotent if and only if there are no directed cycles. Fix \(\pi\in I_k\). The nilpotent partial maps whose every vertex arrow follows a color arrow of \(\pi\) are exactly unordered collections of disjoint directed chains with color words \(a,\pi(a),\ldots,\pi^{j-1}(a)\) of length \(j\le L\). A chain of \(j\) vertices has \(j-1\) domain points. The labeled exponential formula therefore gives precisely \(\left(\prod n_i!\right)[\mathbf x^{\mathbf n}]\exp(H_{\pi,L})\), rank-weighted by \(u\). Repeated colors are permitted within a chain; distinct actual vertices are ensured by labeled coefficient extraction.

**Removing multiple potential part actions.** A chain collection with actual part action \(\theta\) is counted under a potential part action \(\pi\) precisely when \(\pi\supseteq\theta\). The incidence-algebra inverse of extension in the partial-injection poset has coefficient \((-1)^{|\pi|-|\theta|}\) for each interval, because the interval is Boolean. Summing over all extensions of a partial injection on a residual \(h\)-set gives \(\mu_h=\sum_j(-1)^j\binom hj^2j!\). Consequently
\[
\sum_{\pi\supseteq\theta}\mu_{k-|\operatorname{dom}\pi|}=1,
\]
by interchanging the two extension sums: every strict interval contributes \((1-1)^t=0\). The displayed \(B_{\mathbf n,L}\) therefore counts every nilpotent partial isometry exactly once, proving the rank–index formula.

**Largest possible chain.** Assume every \(n_i\ge2\). Choosing a cyclic order on all parts and two vertices from each part gives a chain of length \(2k\), so a longest chain repeats a color. Because the induced part map is injective, the first repeated color of any chain must be its initial color: a tail entering a cycle would give two incoming part arrows. Hence its color word is a prefix of a periodic sequence of distinct colors from some cycle of length \(\ell\le k\). Let \(s\) be the smallest capacity among its \(\ell\) colors. During \(s\) full turns all \(\ell\) colors can occur, and thereafter only colors of capacity at least \(s+1\) can occur before reaching one with capacity \(s\). Accordingly, its length is at most \(s\ell+h\), where \(h\) counts the selected colors of capacity above \(s\), and hence at most \(s c_s+c_{s+1}\). If the chain uses fewer than \(s\) full turns, the same upper bound is immediate. Conversely, for each \(s\) choose the \(c_s\) parts of size at least \(s\), place the \(c_{s+1}\) larger parts first in a cyclic order, and form a path of length \(s c_s+c_{s+1}\). This proves the maximum formula.

**Spanning-chain criterion and multiplicity.** Index \(N\) forces a single directed chain containing all \(N\) vertices. Its periodic distinct-color word uses every part and visits each part either \(m\) or \(m+1\) times, for the minimum part size \(m\). Hence all part sizes differ by at most one, which is also sufficient. The \(h\) larger parts occupy the first \(h\) positions of the cyclic color order, in \(h!\) orders, and the other parts occupy the rest in \((k-h)!\) orders. Assign the individual vertices in \(n_i!\) orders within each part. The resulting vertex chain uniquely specifies its partial map and the count follows. For \(h=0\) this gives \(k!\prod_i n_i!\).

## Verification
The accompanying `verify.py` evaluates the coefficient formula through an independent labeled-chain recurrence and separately enumerates all partial injections on the labeled vertices, testing pairwise distances, nilpotency, rank, and index directly. The complete rank–index tables agree for \(K_{2,2}\), \(K_{3,2}\), \(K_{2,2,2}\), and \(K_{3,2,2}\). The two-part cases are regression checks against previously established bipartite formulas, not new claims. The maximum-index and spanning-chain formulas are also checked in the three-part cases. To reproduce, run `python verify.py` with the standard Python library.

## Relationship to prior work
Jajcay, Jajcayová, Szakács, and Szendrei (2018 preprint, 2021 journal) develop the general inverse-monoid theory of partial graph automorphisms, including unique path/cycle decomposition and local rank-two compatibility, but do not derive the present multipartite nilpotent rank–index census. A previously established all-multipartite **square-zero** spectrum is exactly the \(L\le2\) portion of the present theorem, and the previously established complete-bipartite rank–index formula already covers \(k=2\). Neither is claimed as new. The new content is the complete \(k\ge3\) higher-nilpotency distribution obtained from directed part cycles and the rook-extension Möbius coefficients, together with the general sharp maximum-index and spanning-index formulas. Basic exponential enumeration of labeled paths is a standard counting principle, used here with the multipartite compatibility restriction.

## Limitations
The claim is limited to the stated complete multipartite graph family; it does not classify arbitrary graph partial-automorphism monoids. The finite verifier checks only small graphs and does not establish the general theorem by enumeration. The formula is exact but involves finitely many partial injections and coefficient extraction rather than a uniformly short product expression. Equivalent conclusions under alternative colored partial-permutation or inverse-monoid terminology cannot be excluded without further literature comparison. The \(k=2\) and square-zero specializations are prior-covered.

## References
1. R. Jajcay, T. Jajcayová, N. Szakács, M. B. Szendrei, *Inverse monoids of partial graph automorphisms*, arXiv:1809.04422, first posted 12 September 2018; *Journal of Algebraic Combinatorics* **53** (2021), 829–849. https://arxiv.org/abs/1809.04422
2. V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a finite star graph*, arXiv:2203.05504, first posted 10 March 2022. https://arxiv.org/abs/2203.05504
