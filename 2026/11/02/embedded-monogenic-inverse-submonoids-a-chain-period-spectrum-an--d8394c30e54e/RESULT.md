# Embedded monogenic inverse submonoids: a chain-period spectrum and a half-density law

## Finding
For every integer \(n\ge 0\), let \(I_n\) be the symmetric inverse monoid of all partial bijections of \([n]\), with the identity \(1_n\). An **embedded monogenic inverse submonoid** means an actual subset \(\langle1_n,f,f^{-1}\rangle\subseteq I_n\), not an isomorphism class. Every partial bijection decomposes uniquely into disjoint directed cycles and directed chains, with an isolated undefined vertex viewed as a chain of one vertex. Write \(h(f)\) for the largest number of arrows in one chain, or zero if there are no chain arrows. Write \(m(f)\) for the least common multiple of its cycle lengths, taking the empty least common multiple to be \(1\).

**Generator rigidity.** If \(h(f)\ge1\), the only partial bijections generating the same inverse submonoid as \(f\) are \(f\) and \(f^{-1}\), and these are distinct. If \(h(f)=0\), the generator is a permutation of a subset and its inverse submonoid has exactly \(\varphi(m(f))\) generators on that same support.

Define the formal power series
\[
A_j(z)=\exp\!\left(\sum_{r=1}^{j}z^r\right),\qquad
B_m(z)=\sum_{d\mid m}\mu(m/d)\exp\!\left(\sum_{r\mid d}\frac{z^r}{r}\right),
\]
where \(j\ge0\), \(m\ge1\), \(A_0(z)=1\), and \(\mu\) is the number-theoretic Möbius function. For \(h\ge1\), \(m\ge1\), the number \(R_{n,h,m}\) of distinct embedded monogenic inverse submonoids with generator profile \((h,m)\) is exactly
\[
\boxed{R_{n,h,m}=\frac{n!}{2}[z^n]\bigl(A_{h+1}(z)-A_h(z)\bigr)B_m(z).}
\]
For \(h=0\), the corresponding count is
\[
\boxed{R_{n,0,m}=\frac{n!}{\varphi(m)}[z^n]e^z B_m(z).}
\]
In both formulas the result is zero for unrealizable parameters; these formulas distinguish actual subsets, not just abstract isomorphism types.

Let \(N_n\) be the total number of such embedded inverse submonoids and \(c_k\) the number of cyclic subgroups of the symmetric group \(S_k\), with \(c_0=1\). Then
\[
\boxed{N_n=\frac12\!\left(\sum_{k=0}^{n}\binom nk^2 k!-\sum_{k=0}^{n}\binom nk k!\right)
+\sum_{k=0}^{n}\binom nk c_k,}
\qquad
c_k=\sum_{\lambda\vdash k}\frac{k!}{z_\lambda\varphi(\operatorname{lcm}\lambda)}.
\]
Here \(z_\lambda=\prod_{r\ge1}r^{a_r}a_r!\) for a partition with \(a_r\) parts of size \(r\), and \(\operatorname{lcm}(\varnothing)=1\). The first values \(N_n\), for \(n=0,1,\ldots,7\), are
\[
1,\ 2,\ 6,\ 24,\ 126,\ 838,\ 6841,\ 65411.
\]
Furthermore, if \(|I_n|\) denotes the number of partial bijections, then
\[
\boxed{\lim_{n\to\infty}\frac{N_n}{|I_n|}=\frac12,\qquad
\left|\frac{N_n}{|I_n|}-\frac12\right|\le\frac{e}{2(n+1)}.}
\]

## Assumptions and scope
All sets are finite, \(n\ge0\), composition is ordinary composition of partial bijections, and every inverse submonoid contains the ambient identity \(1_n\) even when the generating partial bijection has smaller support. A directed chain of \(r\) vertices has \(r-1\) arrows. For \(h=0\), there may be undefined singleton chains, but no chain arrows, so the generating map is a permutation of its domain/image subset. The constants \(\mu\) and \(\varphi\) are the classical integer Möbius and Euler totient functions. Coefficient extraction refers to formal power series over \(\mathbb Q\); no analytic convergence is presumed.

## Proof
**1. Rank and generators.** Let \(f\) have disjoint cycles of total support size \(c\) and chains of vertex lengths \(\ell_1,\dots,\ell_s\). Then \(\operatorname{rank}(f)=c+\sum_i(\ell_i-1)\). Any nonempty word \(w\) in \(f,f^{-1}\) has signed exponent \(t\in\mathbb Z\). On the cyclic support it acts everywhere by \(f^t\); on each chain it acts as translation by \(t\) on some (possibly empty) interval. If \(t=0\), its action is a partial identity, hence idempotent. If \(|t|\ge2\), its rank is at most \(c+\sum_i\max(\ell_i-|t|,0)\), strictly less than \(\operatorname{rank}(f)\) whenever a chain has at least one arrow. If \(t=1\), the word is a restriction of \(f\); equal rank forces equality with \(f\). Similarly signed exponent \(-1\) and equal rank forces \(f^{-1}\).

Now suppose \(\langle f\rangle_{\mathrm{inv}}=\langle g\rangle_{\mathrm{inv}}\) and \(h(f)\ge1\). Neither \(f\) nor \(g\) is idempotent. Both have rank less than \(n\). Each is a nonempty word in the other and its inverse, so rank submultiplicativity gives \(\operatorname{rank}(f)\le\operatorname{rank}(g)\le\operatorname{rank}(f)\). The preceding paragraph forces \(g=f\) or \(g=f^{-1}\). Those two distinct elements do generate the same inverse submonoid. When \(h(f)=0\), the restriction to the common domain/image subset \(S\) is a permutation of order \(m\); the generated inverse submonoid is the cyclic subgroup \(\langle f\rangle\subseteq S_S\), with ambient \(1_n\) adjoined if necessary. Its generators are precisely the \(\varphi(m)\) generators of that cyclic group. The support \(S\) is recovered as the support of its local group identity, so different supports do not collapse.

**2. Component counting and exact profile.** On \(r\ge1\) labeled vertices, directed chain components have \(r!\) linear orders, hence exponential-generating contribution \(z^r\). Directed cycles have \((r-1)!\) arrangements, hence contribution \(z^r/r\). The exponential formula gives \(A_{h+1}\) for all chain components with at most \(h+1\) vertices, so \(A_{h+1}-A_h\) enforces maximum chain-arrow length exactly \(h\). Cyclic components whose lengths divide \(d\) contribute \(\exp(\sum_{r\mid d}z^r/r)\). Möbius inversion over the divisors of \(m\) imposes least common multiple exactly \(m\), giving \(B_m\). The classes of labeled partial bijections are the product of these two species, so coefficient extraction counts their generators. Divide by two for \(h\ge1\) using Part 1. For \(h=0\), the only chain components allowed have one vertex (contribution \(e^z\)); divide instead by \(\varphi(m)\).

**3. Total and asymptotic.** The rook-monoid cardinality is \(|I_n|=\sum_{k=0}^n\binom nk^2k!\). Exactly \(Q_n=\sum_{k=0}^n\binom nk k!\) partial bijections have equal domain and image, and hence no nontrivial chains. They produce \(\sum_{k=0}^n\binom nk c_k\) embedded inverse submonoids because their supports and cyclic subgroups are uniquely specified. The remaining \(|I_n|-Q_n\) maps occur in inverse pairs and yield the first half of the displayed total. Each cyclic subgroup of order \(d\) in \(S_k\) contributes \(\varphi(d)\) permutations; the symmetric-group cycle-type formula yields the displayed partition sum for \(c_k\).

Lastly, \(Q_n=n!\sum_{j=0}^n1/j!\le e n!\), whereas \(|I_n|/n!=\sum_{j=0}^n\binom nj/j!\ge n+1\). Since the number of monogenic submonoids with \(h=0\) lies between zero and \(Q_n\), the exact total gives the stated error bound and limit.

## Verification
The accompanying standalone `verify.py` exhaustively enumerates all partial bijections for \(0\le n\le5\), constructs their inverse submonoids by genuine closure under composition, checks generator multiplicities and inverse pairing, compares every realizable positive-\(h\) profile with the exact rational coefficient formula, and compares total counts with the independent cyclic-subgroup calculation. Run using `python3 verify.py`; a successful run prints `VERIFY_OK`. These finite computations validate small instances only and do not substitute for Parts 1–3 of the proof.

## Relationship to prior work
Elliott, Levine and Mitchell (arXiv:2303.12387, first public March 22, 2023; *Communications in Algebra*, 2023) enumerate the **isomorphism types** of monogenic inverse submonoids of finite symmetric inverse monoids and classify those types by maximal chain and cyclic period. Their Theorem 10 and Lemma 8 are the structural predecessors of the profile parameters here. The present result instead counts distinct **embedded subsets** on a fixed labeled set, requiring generator-fiber rigidity and component-species multiplicities. Preston's earlier classification of partial-bijection representations of monogenic inverse semigroups is also relevant background. No novelty is asserted for the basic chain-cycle decomposition, the underlying abstract-type classification, or the exponential formula itself.

## Limitations
The numerical table is checked directly only through \(n=5\); values through \(n=7\) are consequences of the proved coefficient formulas, not exhaustive submonoid enumeration. Publication-priority searches are not exhaustive, particularly for older representation literature under alternate terminology; the full Preston (1986) article was not available for inspection. The result concerns embedded inverse **submonoids** with ambient identity, not necessarily nonunital inverse subsemigroups or conjugacy-orbit counts.

## References
1. L. Elliott, A. Levine and J. D. Mitchell, *Counting monogenic monoids and inverse monoids*, arXiv:2303.12387 (2023), https://arxiv.org/abs/2303.12387, DOI: 10.1080/00927872.2023.2214821.
2. G. B. Preston, *Monogenic inverse semigroups*, Journal of the Australian Mathematical Society 40 (1986), 321–342, DOI: 10.1017/S1446788700027543.
3. Y. W. Cho and N. Ruškuc, *On Finite Presentability of Subsemigroups of the Monogenic Free Inverse Semigroup*, arXiv:2404.05244 (2024), https://arxiv.org/abs/2404.05244 (distinct question concerning free inverse semigroups).
