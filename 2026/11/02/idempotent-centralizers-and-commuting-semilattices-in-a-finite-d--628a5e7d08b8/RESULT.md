# Idempotent centralizers and commuting semilattices in a finite directed-path monoid

## Finding

For \(n\ge2\), let \(W_n\) be the monoid of full maps \(f:[n]\to[n]\) with \(f(i+1)-f(i)\in\{0,1\}\) for all \(1\le i<n\). This is the weak-endomorphism monoid of the directed path and, equivalently, the monoid of order-preserving full chain maps with interval image.

Every idempotent is a **clamping map**
\[
e_{a,b}(x)=\min\{b,\max\{a,x\}\},\quad 1\le a\le b\le n.
\]
Set \(k=b-a\), \(L=2^{a-1}\) and \(R=2^{n-b}\). The cardinality of the centralizer of this individual idempotent is
\[
\boxed{|C_{W_n}(e_{a,b})|=(k+2)2^{k-1}+(L+R-2)2^k+(L-1)(R-1).}
\]
At \(k=0\), the first term is \(1\), so the formula is integral at every boundary. All constant idempotents have centralizer cardinality \(2^{n-1}\), and the identity has centralizer cardinality \((n+1)2^{n-2}\).

The total number of ordered **idempotent–arbitrary commuting pairs** is
\[
\boxed{A_n:=|\{(e,f)\in E(W_n)\times W_n:ef=fe\}|=(4n-12)2^n+\frac{n^2+9n}{2}+12.}
\]
Consequently, for independent uniformly sampled \(e\in E(W_n)\) and \(f\in W_n\),
\[
\Pr(ef=fe)=\frac{A_n}{\frac{n(n+1)}2\,(n+1)2^{n-2}}=\frac{32}{n^2}+O(n^{-3}).
\]

Two clamps commute precisely when their intervals intersect. With **all** idempotents retained as graph vertices (including any central idempotents), the simple graph joining two distinct commuting idempotents is exactly the interval-intersection graph of all nonempty integer subintervals of \([n]\). The polynomial that counts its cliques, including the empty clique, is
\[
\boxed{\mathcal K_n(t)=\sum_{j=1}^{n}(1+t)^{j(n-j+1)}-\sum_{j=1}^{n-1}(1+t)^{j(n-j)}.}
\]
There are precisely \(n\) maximal commuting idempotent subsemigroups,
\[
H_j=\{e_{a,b}:a\le j\le b\},\quad 1\le j\le n;
\]
they are semilattices of sizes \(j(n-j+1)\), and the largest has size \(\lfloor(n+1)^2/4\rfloor\).

## Assumptions and scope

The vertex set \([n]\) is \(\{1,\ldots,n\}\), and all maps are **full** functions, not partial functions. The oriented path has edges \(i\to i+1\). The monoid operation is composition; all statements about commutativity are independent of the left/right convention for writing compositions. The centralizer is taken **inside \(W_n\)**, not the full transformation monoid. The clique polynomial counts arbitrary unordered subsets of distinct idempotents and includes the empty subset. The integer \(n\ge2\) is arbitrary; no field, regularity, or additional restrictions are assumed.

The standard characterizations of \(W_n\), its size \((n+1)2^{n-2}\), and its \(n(n+1)/2\) interval-clamping idempotents are existing results. The contributions here are the centralizer profile, its aggregate probability, the exact commuting-idempotent graph and clique polynomial, and the maximal semilattice classification.

## Proof

**Step 1: necessary and sufficient commutation conditions.** Fix \(e=e_{a,b}\) and \(f\in W_n\). Write \(u=f(a)\), \(v=f(b)\). From \(ef=fe\) on the fixed interval \([a,b]\), every \(f(x)\) with \(a\le x\le b\) must lie in \([a,b]\); equivalently, by monotonicity, \(a\le u\le v\le b\). Conversely, assume this inequality. At each \(x<a\), the equation \(e(f(x))=f(e(x))=u\) is automatic when \(u=a\), because \(f(x)\le u=a\). When \(u>a\), it forces \(f(x)=u\) (every such \(x\)); similarly, for \(x>b\), the equation is automatic if \(v=b\), and otherwise forces \(f(x)=v\). These conditions plus the interior restriction are necessary and sufficient.

**Step 2: count the maps.** For given \(u,v\) with \(a\le u\le v\le b\), there are \(\binom{k}{v-u}\) valid step sequences along \([a,b]\). On the left there are \(L=2^{a-1}\) valid step sequences if \(u=a\), and exactly one otherwise; every left sequence remains in \([n]\) because the endpoint is at most \(b\). On the right there are \(R=2^{n-b}\) valid sequences if \(v=b\), and exactly one otherwise. These choices are independent. Thus
\[
|C_{W_n}(e)|=\sum_{a\le u\le v\le b}\binom{k}{v-u}\bigl(1+(L-1){\bf1}_{u=a}\bigr)\bigl(1+(R-1){\bf1}_{v=b}\bigr).
\]
The unrestricted term is \(\sum_{d=0}^k(k-d+1)\binom{k}{d}=(k+2)2^{k-1}\). Each single-endpoint enhancement has coefficient \(2^k\), and the double-endpoint enhancement occurs once (the all-increment interior sequence). Expansion yields the boxed centralizer formula, valid also at \(k=0\).

**Step 3: sum the centralizers.** Group intervals by \(k=b-a\), with \(m=n-k\) possible positions \(a=1,\ldots,m\). Then \(L=2^{a-1}\), \(R=2^{m-a}\), and
\[
\begin{aligned}
\sum_{a=1}^{m}|C_{W_n}(e_{a,a+k})|={}&m(k+2)2^{k-1}\\
&+2^k\bigl(2(2^m-1)-2m\bigr)\\
&+m2^{m-1}-2(2^m-1)+m.
\end{aligned}
\]
Here we used \(\sum L=\sum R=2^m-1\) and \(LR=2^{m-1}\). Summing this expression over \(0\le k\le n-1\) and evaluating elementary finite geometric and arithmetico-geometric sums gives exactly
\(A_n=(4n-12)2^n+(n^2+9n)/2+12\).
The previously known \(|E(W_n)|=n(n+1)/2\) and \(|W_n|=(n+1)2^{n-2}\) give the probability expression. Since \(A_n=(4n-12)2^n+O(n^2)\), its asymptotic equivalent is \(32/n^2\).

**Step 4: commuting idempotents.** If intervals \(I=[a,b]\) and \(J=[c,d]\) intersect, their clamps commute and their composition is the clamp onto \(I\cap J\), by an elementary three-region check. If, say, \(b<c\), the two compositions are the distinct constant maps at \(b\) and \(c\). This proves the interval-intersection graph characterization.

**Step 5: maximal semilattices and clique polynomial.** Every finite pairwise-intersecting family of intervals in a total order has nonempty common intersection (the interval Helly property). Hence every commuting idempotent family is contained in some \(H_j\). Each \(H_j\) is closed under composition (intersection of intervals), contains all clamps whose intervals pass through \(j\), and is maximal; distinct \(j\) give distinct maximal families. Counting choices of \(a\le j\) and \(b\ge j\) gives size \(j(n-j+1)\).

A subset of intervals is a clique exactly when its common intersection is nonempty; the empty family is a clique by convention. Let \(N_j=j(n-j+1)\) denote the number of available intervals containing \(j\), and \(M_j=j(n-j)\) the number containing both adjacent sites \(j,j+1\). A family with a common intersection of \(\ell\ge1\) consecutive sites appears \(\ell\) times in \(\sum_j(1+t)^{N_j}\) and \(\ell-1\) times in \(\sum_j(1+t)^{M_j}\), so its net contribution is exactly one. For the empty family, the corresponding intersection is all of \([n]\) and the same argument applies. This proves the clique polynomial.

## Verification

The accompanying standalone file `verify_path_centralizers.py` uses only the Python standard library. Execute `python verify_path_centralizers.py`. It independently generates all elements from binary adjacent increments; checks every idempotent and its full multiplication centralizer, not merely the derived formula; tests all pairs of idempotents against interval overlap; and compares aggregate commuting-pair counts against the closed formula for \(1\le n\le10\). It also enumerates all subsets of idempotents and tests every clique and maximal clique for \(1\le n\le5\), including the empty clique. Expected final output: `VERIFY_OK`.

For \(n=4\), there are \(20\) maps, \(10\) idempotents and \(102\) ordered idempotent–arbitrary commuting pairs. For \(n=10\), there are \(2816\) maps, \(55\) idempotents, and \(28779\) such pairs. These finite checks corroborate the proof; the proof, not the enumerations, establishes the all-\(n\) statements.

## Relationship to prior work

Fernandes and Paulista (first public preprint December 26, 2021, arXiv:2112.13427) identify the weak-endomorphism monoid of the directed path, its map structure, cardinality, regularity and idempotents; these are explicitly used as established premises. Fernandes (2024, DOI below) identifies the **same monoid** under the alternative name of order-preserving transformations with interval images and supplies presentations and related rank results. Its introduction and Sections 2–4 were inspected: it does not state a per-idempotent centralizer profile, an idempotent–arbitrary commuting-pair enumerator, or the clique polynomial. The equivalence of these two monoid descriptions is acknowledged rather than treated as new.

Araújo, Bentz and Konieczny study a commuting graph for the symmetric inverse semigroup, which is a distinct transformation monoid. Work on completely simple semigroups' commuting graphs addresses a different structural class. Neither implies the present formula for an interval-image monoid as a direct specialization. Any existing general theorem explicitly computing commuting centralizers in the full order-preserving monoid would require a separate restriction to interval-image maps; no directly covering theorem was identified in the inspected evidence.

## Limitations

This result concerns only centralizers of **idempotents**, not centralizers of arbitrary elements or the full commuting graph of \(W_n\). The clique polynomial is for the induced graph on all idempotents, not the conventional commuting graph with central elements removed. No assertion is made about uniqueness of the formula in all published literature. A broader, not yet identified treatment of idempotent centralizers in chain transformation monoids, or a detailed thesis on commuting graphs of semigroups, could affect publication priority. The exhaustive checks cover bounded \(n\) only. No independent mathematical audit has been performed.

## References

1. V. H. Fernandes and T. Paulista, *On the Rank of Monoids of Endomorphisms of a Finite Directed Path* (first preprint 2021-12-26), arXiv:2112.13427, https://arxiv.org/abs/2112.13427.
2. V. H. Fernandes, *On the monoid of order-preserving transformations of a finite chain whose ranges are intervals*, *Semigroup Forum* 109 (2024), 336–346, https://doi.org/10.1007/s00233-024-10466-2.
3. J. Araújo, W. Bentz and J. Konieczny, *The Commuting Graph of the Symmetric Inverse Semigroup*, arXiv:1205.1664, https://arxiv.org/abs/1205.1664 (distinct-monoid comparison).
4. T. Paulista, *Commuting graphs of completely simple semigroups*, *Communications in Algebra* 53 (2025), 4215–4226, https://doi.org/10.1080/00927872.2025.2481079 (distinct-structural-class comparison).
