# Joint-rank enumeration for two commuting idempotent unary functions

## Finding

Let \(\varphi\) be the fixed one-variable first-order sentence over two total unary function symbols:
\[
\varphi :=\forall x\,[f(f(x))=f(x)\ \land\ g(g(x))=g(x)\ \land\ f(g(x))=g(f(x))].
\]
For each \(n\ge1\), interpret \(f,g\) as an **ordered** pair of functions \([n]\to[n]\), and define
\[
C=|\operatorname{Fix}(f)\cap\operatorname{Fix}(g)|,\quad
F=|\operatorname{Fix}(f)|,\quad G=|\operatorname{Fix}(g)|.
\]
Writing \(P_n(u,v,w)\) for the polynomial that sums \(u^Cv^Fw^G\) over all labeled models on \([n]\), and putting \(P_0=1\), the exact identity in formal power series is
\[
\boxed{\sum_{n\ge0} P_n(u,v,w)\frac{z^n}{n!}
=\exp\!\left(uv wz\sum_{p,q\ge0}\frac{(vz)^p(wz)^q}{p!q!}\,
\exp\bigl((p+1)(q+1)z\bigr)\right).}
\]
In particular, setting \(u=v=w=1\) yields the labeled model counts \(A_n=P_n(1,1,1)\):
\[
(A_n)_{n=0}^{10}=(1,1,7,58,601,7616,113989,1963060,38178193,826879312,19727279461).
\]
This is a complete joint distribution by the two individual fixed-point ranks and their common fixed-point intersection, not merely a count of models.

## Assumptions and scope

All sets are finite and labeled, both functions are total, and the order \((f,g)\) matters. Every displayed identity is an equality of formal power series over \(\mathbb Q[u,v,w]\), so no analytic convergence is asserted. A nonempty model always has a common fixed point, whereas the empty structure is included only as a generating-function normalization. No statement here concerns arbitrary pairs of endofunctions, noncommuting idempotents, partial transformations, or unlabeled isomorphism classes.

## Proof

**1. The canonical common retraction.** Set \(h=f\circ g=g\circ f\). Since the functions commute and are idempotent, \(h^2=h\). Moreover \(f\circ h=h\) and \(g\circ h=h\), and for every \(x\), \(f(x)=x=g(x)\) if and only if \(h(x)=x\). Thus
\[
\operatorname{Fix}(h)=\operatorname{Fix}(f)\cap\operatorname{Fix}(g).
\]
Each fiber \(X_c=h^{-1}(\{c\})\) about a common fixed point \(c\) is invariant under both functions: \(h(f(x))=h(x)\), and likewise for \(g\). These fibers partition the domain, with each fiber containing exactly one common fixed point.

**2. Complete classification of a single fiber.** On a fiber rooted at \(c\), partition the other elements into \(P\) fixed by \(f\) only, \(Q\) fixed by \(g\) only, and \(R\) fixed by neither function; write their sizes as \(p,q,r\). For \(x\in P\), necessarily \(f(x)=x\) and \(g(x)=c\), since \(h(x)=c\). Symmetrically for \(x\in Q\), \(g(x)=x\) and \(f(x)=c\). For every \(x\in R\), idempotence forces \(f(x)\in\{c\}\cup P\) and \(g(x)\in\{c\}\cup Q\); conversely *every pair* of these choices works, because both composites return \(c\). All choices for distinct elements of \(R\) are independent. Hence for fixed labeled sets \(P,Q,R\) there are exactly \(((p+1)(q+1))^r\) admissible pairs of restrictions, with no repetitions in this parametrization.

**3. Weighted exponential formula.** A rooted fiber has total size \(1+p+q+r\), and contributes weight \(u v^{p+1}w^{q+1}\): the root is fixed by both functions; the \(p\) elements of \(P\) add only \(f\)-fixed points and the \(q\) of \(Q\) add only \(g\)-fixed points. The exponential generating function of one labeled fiber therefore is
\[
B(z;u,v,w)=uv wz\sum_{p,q,r\ge0}
\frac{(vz)^p(wz)^qz^r}{p!q!r!}((p+1)(q+1))^r
=uv wz\sum_{p,q\ge0}\frac{(vz)^p(wz)^q}{p!q!}
\exp\bigl((p+1)(q+1)z\bigr).
\]
The canonical fibers of \(h\) form an unordered labeled set, so the exponential formula gives \(\sum_n P_n z^n/n!=\exp(B)\). Every model produces exactly one such decomposition, and conversely each unordered family of rooted fibers determines a unique model; thus the equality holds in both directions.

**4. Exact recurrence and effective computation.** Let \(B_m(u,v,w)=m![z^m]B(z;u,v,w)\). The previous classification gives
\[
B_m(u,v,w)=m\sum_{p+q+r=m-1}
\binom{m-1}{p,q,r}\big((p+1)(q+1)\big)^r \,u v^{p+1}w^{q+1}.
\]
By choosing the fiber containing label \(1\),
\[
P_0=1,\qquad P_n=\sum_{m=1}^n\binom{n-1}{m-1}B_m(u,v,w)P_{n-m}(u,v,w).
\]
After setting \(u=v=w=1\), this is the stated recurrence for \(A_n\). The sums defining all scalar \(B_m\) through \(n\) contain \(O(n^3)\) triples, and the recurrence has \(O(n^2)\) terms. All integers have at most \(O(n\log n)\) bits because \(A_n\le n^{2n}\). The weighted polynomials have degree at most \(n\) in each of three variables, so even naive polynomial multiplication yields an algorithm polynomial in \(n\) and in the bit lengths of coefficients. These are exact finite calculations, not asymptotic claims.

## Verification

The accompanying `checker.py` independently enumerates all idempotent maps of \([n]\), tests every ordered pair for commutation, and compares the entire \((C,F,G)\)-distribution with the rooted-fiber recurrence for every \(1\le n\le5\). It also calculates the unweighted totals through \(n=10\). The computation returned `FULL_PROFILE_CHECK_OK`. The finite brute force is a consistency check only; the all-\(n\) identity follows from the bijective fiber proof above.

## Relationship to prior work

Kuželka, *Unary Functions, Automorphisms, and Unlabeled First-Order Model Counting* (arXiv:2608.30580v1, first posted 31 August 2026), proves polynomial-time counting for the one-function one-variable fragment and demonstrates hardness for a fixed one-variable sentence with two functions and unary predicates. The present sentence lies in the latter two-function syntax but imposes specific commuting-idempotent identities and gives an explicit rank-refined enumeration, neither supplied by the general hardness theorem nor by the one-function tractability theorem.

Paulista's *Characterizing the largest commutative (full and partial) transformation semigroups of certain types* (arXiv:2511.09495) examines largest commutative subsemigroups of transformations, including those consisting of idempotents; those extremal subsemigroup questions are not an exact count of all ordered commuting-idempotent pairs by ranks. A recent graph study of semigroup idempotents (Mathematics 2026, 14(5), 891) depicts the finite commuting graph for the small transformation monoid of size three, but is not evidence for an arbitrary-order joint EGF. These comparisons concern the mathematical statements, not a claim that all transformation-semigroup literature has been exhausted.

## Limitations

This result counts *labeled* structures satisfying exactly the displayed identities; it does not establish a tractable classification for all two-function first-order sentences, does not enumerate isomorphism classes, and does not give asymptotic probabilities. The general formula may be obtainable as a specialization of a broader action-counting result in historical semigroup literature not located in the targeted searches. The transformation-semigroup and graph sources were not all available for full-text comparison, leaving a specific priority risk. No external proof audit is asserted.

## References

1. O. Kuželka, *Unary Functions, Automorphisms, and Unlabeled First-Order Model Counting*, arXiv:2608.30580v1 (2026), https://arxiv.org/abs/2608.30580 .
2. T. Paulista, *Characterizing the largest commutative (full and partial) transformation semigroups of certain types*, arXiv:2511.09495 (2025), https://arxiv.org/abs/2511.09495 .
3. *Graph-Theoretic Idealization of Semigroups via Bruck-Reilly Extensions*, *Mathematics* 14 (2026), article 891, https://www.mdpi.com/2227-7390/14/5/891 .
4. *MSC2020: Mathematical Subject Classification*, American Mathematical Society, classification 03C13 (model theory of finite structures), https://mathscinet.ams.org/msc/msc2020.html?btn=Current&t=03C13 .
