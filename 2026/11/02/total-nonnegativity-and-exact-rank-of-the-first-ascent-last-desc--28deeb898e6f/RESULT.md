# Total nonnegativity and exact rank of the first-ascent–last-descent Dyck kernel

## Finding

Let \(P\) be uniformly distributed among the \(C_n=\frac{1}{n+1}\binom{2n}{n}\) Dyck paths of semilength \(n\ge1\), where a Dyck path is a nonnegative nearest-neighbor walk with \(n\) up-steps and \(n\) down-steps. Write \(A\in\{1,\ldots,n\}\) for the number of consecutive up-steps at its beginning and \(B\) for the number of consecutive down-steps at its end. Define the unnormalized joint-count kernel
\[
J_n(a,b)=C_n\Pr\{A=a,B=b\},\qquad 1\le a,b\le n.
\]
**Theorem.** For every integer \(n\ge1\), the matrix \(J_n\) is symmetric positive semidefinite and totally nonnegative (every square minor is nonnegative), with exact rank \(\lfloor n/2\rfloor+1\). In particular, for all real functions \(f\) on \(\{1,\ldots,n\}\),
\[
\operatorname{Cov}(f(A),f(B))\ge0.
\]
The conditional laws \(\mathcal L(B\mid A=a)\) are increasing in likelihood-ratio order, understood by nonnegative adjacent \(2\times2\) probability minors. At \(n\ge3\), the conditional laws for \(a=1\) and \(a=2\) are equal; all steps \(a\to a+1\) with \(2\le a<n\) strictly increase in stochastic order. The case \(n=2\) is strict from \(a=1\) to \(a=2\).

## Assumptions and scope

The sample space is all \(C_n\) Dyck paths, equally likely; no asymptotic regime or additional conditioning is assumed. We use \(\binom{N}{r}=0\) when \(N\ge0\) and \(r\) lies outside \(\{0,\ldots,N\}\). Boundary cases are specified separately; for \(a,b<n\),
\[
\boxed{J_n(a,b)=\binom{2n-a-b-2}{n-a-1}-\binom{2n-a-b-2}{n-1}.}
\]
For \(a<n\) or \(b<n\), \(J_n(a,n)=J_n(n,b)=0\); \(J_n(n,n)=1\). For \(n=1\) this is the one-by-one matrix \((1)\).

## Proof

**1. Midpoint Gram representation.** Set \(\mathcal H_n=\{h:0\le h\le n,\ h\equiv n\pmod 2\}\). Let \(T_n(a,h)\) count nonnegative prefixes of length \(n\) with first ascent length exactly \(a\) and endpoint height \(h\). Cutting a Dyck excursion at time \(n\), and reversing the second half while exchanging up/down steps, bijects it with a pair of prefixes of length \(n\), both ending at the same height \(h\). Consequently,
\[
J_n(a,b)=\sum_{h\in\mathcal H_n}T_n(a,h)T_n(b,h),\qquad J_n=T_nT_n^{\mathsf T}.
\]
This immediately proves symmetry and positive semidefiniteness. Reflection at the forbidden level \(-1\) gives, for \(1\le a<n\),
\[
T_n(a,h)=\binom{n-a-1}{(n-2a+h)/2}-\binom{n-a-1}{(n+h)/2},
\]
where each lower index is an integer by parity; for \(a=n\), \(T_n(n,h)=\mathbf1\{h=n\}\). This also makes the construction reproducible. Fixing the first \(a\) up-steps and the next down-step, followed by the last up-step and the last \(b\) down-steps, and applying reflection to the remaining central segment yields the boxed closed form for \(J_n\).

**2. All minors.** The entries \(T_n(a,h)\) count paths with steps \((1,\pm1)\) in the half-plane \(y\ge0\) from source \((a+1,a-1)\) to sink \((n,h)\) (with the zero-length source \((n,n)\) for \(a=n\)). Consider increasing source labels \(a\) and increasing sink heights \(h\). If two paths were connected in crossed order, with \(a<a'\) but the earlier source going to the higher sink, then at horizontal time \(a'+1\) the earlier path is at height at most \(a'-1\), whereas the later path starts at \(a'-1\); at time \(n\) their height order reverses. Their difference changes in multiples of two, so they must intersect at a lattice vertex. By the standard sign-reversing path-swap argument of the Lindström–Gessel–Viennot lemma, every minor of \(T_n\) counts nonintersecting families and is nonnegative. The Cauchy–Binet identity applied to \(J_n=T_nT_n^{\mathsf T}\) proves that **every minor of \(J_n\)** is nonnegative. The general path determinant lemma is prior mathematics, not a new theorem here.

**3. Exact rank.** The Gram factor has \(d=\lfloor n/2\rfloor+1\) columns, so its rank is at most \(d\). Select the \(d\) rows with \(a=\lceil n/2\rceil,\ldots,n\), in ascending order, and all the columns with \(h=0,2,\ldots,n\) if \(n\) is even, or \(h=1,3,\ldots,n\) if \(n\) is odd. Every such row has its first possible endpoint at \(h=2a-n\), attained by following the mandatory first descent with all remaining down-steps. Its corresponding entry is one and every entry to its left is zero, making this \(d\times d\) submatrix upper triangular with diagonal one. Thus \(\operatorname{rank}T_n=d\), and the Gram identity gives \(\operatorname{rank}J_n=d\).

**4. All-function covariance and ordering.** Conditional on the midpoint height \(H=h\), the two (reversed) half-paths are independent and identically distributed. Thus, with \(m_f(h)=\mathbb E[f(A)\mid H=h]\),
\[
\operatorname{Cov}(f(A),f(B))=\operatorname{Var}(m_f(H))\ge0.
\]
Every \(2\times2\) minor of \(J_n\) is nonnegative, so conditional likelihood ratios of \(B\mid A=a\) do not decrease when the first-ascent conditioning rank increases. A simple bijection changes the initial three steps \(UDU\) into \(UUD\), proving equality of the entire first two rows when \(n\ge3\). The row sums, known from classical ballot enumeration, are
\[
N_{n,a}=\sum_bJ_n(a,b)=\frac{a}{2n-a}\binom{2n-a}{n-a}.
\]
For \(2\le a<n\),
\[
\frac{N_{n,a+1}}{N_{n,a}}=\frac{(a+1)(n-a)}{a(2n-a-1)}<1.
\]
When \(a<n\), the entry \(J_n(a,n-1)=1\) (for \(n\ge2\)). Hence \(\Pr\{B\ge n-1\mid A=a\}=1/N_{n,a}\) strictly increases with \(a\) after the first step, and likelihood-ratio order upgrades this to stochastic order. At \(a=n\), \(B=n\) almost surely; at \(n=2\), the two conditional laws are point masses at 1 and 2.

## Verification

A standalone standard-library exact-arithmetic program accompanies this result as `verify_dyck_boundary.py`. It independently enumerates all Dyck paths through semilength 11, compares the proposed joint and ballot matrices, checks the exact row sums and determinant-one rank witness, verifies every minor of the Gram matrix and its path-count factor through semilength 8, and checks all adjacent two-by-two minors through semilength 21. Its executed run reported **227,640 exact checks passed**. These finite tests are diagnostics; the all-\(n\) theorem is established by the combinatorial proof above.

## Relationship to prior work

Deutsch (1998) established the marginal first-peak-height/first-ascent distribution and its ballot formula. Jelínek (2015, Fact 2.11) explicitly established symmetry of the joint first-ascent/final-descent distribution, so **neither the marginal count nor joint symmetry is claimed new**. Gessel and Viennot (1985) established the general path determinant lemma used in step 2. Janson's pre-2016 random-tree/conditioned-walk treatment supplies probabilistic context. The contribution assessed here is the combined exact kernel-factorization, all-order minor and Gram positivity law, exact rank, arbitrary-function covariance, and conditional likelihood-ratio behavior of these natural boundary statistics.

## Limitations

The statement is for uniform Dyck excursions only. Likelihood-ratio comparison is made through the cross-product characterization, which handles the deterministic highest row. The result is not an independent audit, a general weighted-path theorem, nor a priority certification: LGV/Cauchy–Binet and existing Catalan joint-statistic identities create a genuine possibility that the all-order result is implicit in older literature. No assertion is made about unrelated tree statistics or generalized excursions.

## References

1. E. Deutsch, *A bijection on Dyck paths and its consequences*, Discrete Mathematics **179** (1998), 253–256, doi:10.1016/S0012-365X(97)00097-6.
2. V. Jelínek, *Catalan Pairs and Fishburn Triples*, first posted 2015-01-21, arXiv:1501.05157v1, especially Fact 2.11.
3. I. Gessel and G. Viennot, *Binomial Determinants, Paths, and Hook Length Formulae*, Advances in Mathematics **58** (1985), 300–321.
4. S. Janson, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*, arXiv:1112.0510v1 (first posted 2011-12-02).
5. B. Hackl, C. Heuberger and H. Prodinger, *Counting Ascents in Generalized Dyck Paths*, AofA (2018), doi:10.4230/LIPIcs.AofA.2018.26.
