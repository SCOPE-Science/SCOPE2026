# Product fibers and rank gaps for commuting square-zero partial bijections

## Finding
Let \(\mathcal I_n\) be the symmetric inverse monoid (the monoid of all partial bijections of a labeled \(n\)-element set), with zero the empty map. Put
\[
Z_m=\#\{(a,b)\in\mathcal I_m^2:a^2=b^2=ab=ba=0\},\qquad Z_0=1.
\]
Its exponential generating function is
\[
Z(z)=\sum_{m\ge0}Z_m\frac{z^m}{m!}=\frac{\exp\bigl(z+2z^2/(1-z)\bigr)}{1-z^2}.
\]
For any prescribed partial bijection \(h\in\mathcal I_n\), the exact number \(F_n(h)\) of ordered pairs satisfying \(a^2=b^2=0\), \(ab=ba=h\) is
\[
F_n(h)=\begin{cases}
\displaystyle\frac{(n-2r)!}{(n-4r)!}\,Z_{n-4r},&h^2=0,\quad r=\operatorname{rank}(h),\quad 4r\le n,\\[4pt]
0,&\text{otherwise}.
\end{cases}
\]
In particular, the fiber depends only on the prescribed product's rank. If \(C_{n,r}\) is the number of all such ordered commuting pairs whose product has rank \(r\), then
\[
\sum_{n\ge0}\sum_{r\ge0}C_{n,r}\,t^r\frac{z^n}{n!}
=\frac{\exp\bigl(z+2z^2/(1-z)+tz^4\bigr)}{1-z^2}.
\]
The possible product ranks are exactly \(0,1,\ldots,\lfloor n/4\rfloor\). Thus the sharp bound \(\operatorname{rank}(ab)\le\lfloor n/4\rfloor\) holds for all commuting square-zero partial bijections.

## Assumptions and scope
Here \(n\) ranges over all nonnegative integers. Composition has the functional convention \((ab)(x)=a(b(x))\); reversing this convention leaves the assertions unchanged because the pairs commute. A partial map is undefined outside its domain, and equality of partial maps includes equality of domains. Products, squares and zero are calculated in \(\mathcal I_n\), not in its semigroup algebra. Pairs are ordered. Every asserted generating function is an identity of formal power series over \(\mathbb Q[t]\), with \(z\) an ordinary formal indeterminate.

## Proof
**1. Directed colored graph.** For \(a^2=b^2=0\), depict each arrow of \(a\) in color A and each arrow of \(b\) in color B. Each color separately forms disjoint one-arrow chains: each vertex is incident with at most one arrow of that color, because the map is injective and a vertex cannot simultaneously belong to its domain and image. Parallel arrows of distinct colors are allowed.

**2. Forced diamonds.** Suppose \(ab=ba\) and their common product contains \(s\mapsto t\). There are distinct vertices \(u=a(s)\) and \(v=b(s)\), with \(b(u)=a(v)=t\). Square-zero and injectivity force \(s,u,v,t\) to be pairwise distinct. On these four vertices, the A-arrows are \(s\to u\) and \(v\to t\), and the B-arrows are \(s\to v\) and \(u\to t\). Every vertex is now incident with its unique possible arrow of each color, so this four-vertex diamond has no arrows to any outside vertex. Every nonzero product arrow is obtained from exactly one such diamond. Consequently, \(r=\operatorname{rank}(ab)\) requires \(4r\) disjoint vertices, giving the sharp bound \(4r\le n\); disjoint diamonds and isolated vertices attain every allowed rank.

**3. Zero-product pieces.** Remove all the forced diamonds. On the remaining vertices both mixed products vanish. No vertex there can have an incoming arrow of one color and an outgoing arrow of the other: that would define a nonzero mixed product. The square-zero hypotheses exclude incoming and outgoing arrows of the same color. Thus each nonisolated vertex is either a source of all its incident colored arrows or a sink of all of them. Each color has degree at most one, so every connected component of the underlying colored multigraph is an alternating-color path, an alternating even cycle, or a pair of parallel differently-colored edges (viewed as the length-two cycle). The directed edges on each component run from the source bipartition to the sink bipartition. Conversely, every such colored oriented component defines two injective square-zero maps with both mixed products zero.

**4. Labeled connected counts.** An isolated vertex contributes \(z\) to the connected exponential generating series. For each path on \(k\ge2\) vertices, the choice of a starting color and a source/sink parity, modulo reversal, gives exactly \(2k!\) labeled structures; its contribution is \(2z^k\). For every even cycle of length \(2j\ge4\), the two alternating colorings and two source/sink bipartitions give \(2(2j-1)!\) structures, hence contribution \(z^{2j}/j\). The parallel-edge two-cycle similarly contributes \(z^2\). The connected series of all zero-product components is therefore
\[
z+\sum_{k\ge2}2z^k+\sum_{j\ge1}\frac{z^{2j}}j
=z+\frac{2z^2}{1-z}-\log(1-z^2).
\]
The labeled exponential formula yields the asserted \(Z(z)\).

**5. Prescribed product fibers.** If \(h=ab=ba\), then \(h^2=a^2b^2=0\). Let \(h\) have rank \(r\). Its \(r\) arrows have disjoint source and target sets because \(h^2=0\), leaving \(n-2r\) unused vertices. Each prescribed arrow \(s\to t\) forces a diamond, whose ordered two intermediate vertices can be chosen freely subject to all \(2r\) intermediate vertices being distinct. There are \((n-2r)!/(n-4r)!\) choices. The remaining \(n-4r\) vertices can support any of the \(Z_{n-4r}\) zero-product pairs, independently. This gives the fiber formula; if \(4r>n\) there are no such choices.

**6. Rank refinement.** The number of square-zero partial maps \(h\) of rank \(r\) on an \(n\)-set is \(n!/[r!(n-2r)!]\): choose disjoint source and target sets and a bijection. Multiplying by the common fiber gives \(C_{n,r}=n! Z_{n-4r}/[r!(n-4r)!]\) for \(4r\le n\), and zero otherwise. Summing its bivariate exponential generating function is exactly \(Z(z)\exp(tz^4)\).

## Verification
The accompanying standalone `verify.py` enumerates every square-zero partial bijection directly from disjoint source and target sets. For \(0\le n\le7\), it tests every ordered pair for commutation, tabulates every prescribed product, and compares every fiber and product-rank count with an independent integer recurrence derived from the connected-path/cycle species. Run `python3 verify.py` with a standard Python 3 installation. It prints `VERIFY_OK` upon success. Totals for \(n=0,\ldots,7\) are \(1,1,7,31,277,2101,22891,245827\); the nonzero-product rank-one counts for \(n=4,5,6,7\) are \(24,120,2520,26040\). The proof above is valid for every \(n\), whereas exhaustive testing ends at seven.

## Relationship to prior work
Ganyushkin and Mazorchuk, *Combinatorics and distributions of partial injections* (arXiv:math/0511431v1, 2005), develop chain/cycle enumeration for individual partial injections and independent, unrestricted random products (Section 6). Their product probabilities are not the conditional commuting square-zero prescribed-product fibers here. Araújo, Bentz and Konieczny, *The Commuting Graph of the Symmetric Inverse Semigroup* (arXiv:1205.1664v1, 2012), provide the general chain-based commutation criterion (Proposition 2.2), along with maximal commutative nilpotent subsemigroups and commuting-graph results. That criterion is a significant structural antecedent; the present theorem is the closed enumeration of the square-zero commuting-pair product fibers and the resulting rank-refined generating function, not a claim to have invented the general commutation criterion or the underlying partial-injection decomposition.

## Limitations
No claim concerns noninjective partial maps, factors of nilpotency index greater than two, or unordered pairs. The formula is for the symmetric inverse monoid, not its semigroup algebra. Exhaustive finite checks corroborate but do not establish the general enumerative theorem. Searches of published databases and accessible primary literature do not prove worldwide novelty; a specialized equivalent enumeration not identified by those searches remains possible. No independent audit has been performed.

## References
1. O. Ganyushkin and V. Mazorchuk, *Combinatorics and distributions of partial injections*, arXiv:math/0511431v1 (initial public version 17 November 2005), https://arxiv.org/abs/math/0511431.
2. J. Araújo, W. Bentz and J. Konieczny, *The Commuting Graph of the Symmetric Inverse Semigroup*, arXiv:1205.1664v1 (8 May 2012), https://arxiv.org/abs/1205.1664.
