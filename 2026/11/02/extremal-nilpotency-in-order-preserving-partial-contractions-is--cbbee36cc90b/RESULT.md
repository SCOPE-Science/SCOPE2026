# Extremal nilpotency in order-preserving partial contractions is governed by integer partitions

## Finding
Let \(\mathcal{OCI}_n\) be the semigroup of all order-preserving injective partial contractions of the chain \([n]=\{1,\ldots,n\}\), including the empty map as zero. An element of rank \(k\) has nilpotency index at most \(k+1\). For every \(1\le k<n\), the elements attaining this bound admit an exact classification and count.

Write \(E_{n,k}\) for the number of **nonzero** elements \(\alpha\in\mathcal{OCI}_n\) with rank \(k\) and least positive exponent \(j\) satisfying \(\alpha^j=0\) equal to \(k+1\). Let \(p_k(m)\) be the number of integer partitions of \(m\) into exactly \(k\) positive parts. For all integers \(n\ge0\) and \(k\ge1\), with a zero count when \(k\ge n\),
\[
E_{n,k}=2\sum_{m=k}^{n-1}(n-m)p_k(m).
\]
Its complete rank-and-chain-size generating function is the formal series
\[
\boxed{\displaystyle
\sum_{n\ge0}\sum_{k\ge1}E_{n,k}z^nu^k
=\frac{2z}{(1-z)^2}\left(\prod_{j\ge1}\frac{1}{1-uz^j}-1\right).}
\]
Consequently, writing \(E_n=\sum_{k\ge1}E_{n,k}\) and \(p(m)=\sum_k p_k(m)\),
\[
E_n=2\sum_{m=1}^{n-1}(n-m)p(m),\qquad
E_n\sim\frac{\sqrt3}{\pi^2}\exp\!\left(\pi\sqrt{\frac{2n}{3}}\right).
\]
Thus this maximal-index stratum has partition-type, subexponential growth, whereas the full semigroup has exponential growth. More precisely, if \(\lambda=(3+\sqrt5)/2\), then
\[
\log\frac{E_n}{|\mathcal{OCI}_n|}=-n\log\lambda+O(\sqrt n).
\]
The empty map has rank zero and nilpotency index one, and is excluded from the displayed count.

## Assumptions and scope
For a partial injection \(\alpha\colon D\to[n]\), its rank is \(|D|=|\operatorname{im}\alpha|\). Order preservation means \(x<y\) in \(D\) implies \(\alpha(x)<\alpha(y)\), and contraction means \(|\alpha(y)-\alpha(x)|\le |y-x|\). Composition is ordinary composition where defined; the empty map is the absorbing zero. For nilpotent \(\alpha\), its index is the smallest \(j\ge1\) with \(\alpha^j=0\). The convention \(p_k(m)=0\) for \(m<k\), and the empty sum convention, cover all boundaries.

The count concerns the **extremal index \(k+1\) at each fixed rank \(k\)**. It is not a formula for all nilpotent elements, or for every individual nilpotency index. The all-nilpotent count by rank was already given, in equivalent form, by Ahmed and collaborators (2022), Theorem 2.6 specialized to zero fixed points.

## Proof
**1. Index bound and orbit rigidity.** A partial injection of rank \(k\) has exactly \(k\) directed edges \(x\to\alpha(x)\) on the vertices \([n]\). If it is nilpotent, this directed graph is a disjoint union of finite directed paths, with isolated vertices permitted; cycles are excluded. The longest path has at most \(k\) edges, so the nilpotency index is at most \(k+1\). Equality holds exactly when all \(k\) edges lie on a single directed path of \(k+1\) distinct vertices. Conversely, such a path plainly has index \(k+1\).

An orbit \(x,\alpha(x),\alpha^2(x),\ldots\) of an order-preserving partial injection is strictly monotone until it stops: if \(\alpha(x)>x\) and the second iterate is defined, then \(\alpha^2(x)>\alpha(x)\), by applying order preservation to the domain points \(x<\alpha(x)\); the decreasing case is analogous. Therefore an extremal-index element is obtained from a unique increasing list
\[
t_1<t_2<\cdots<t_{k+1}
\]
by either the forward shift \(t_i\mapsto t_{i+1}\) for \(1\le i\le k\), or the backward shift \(t_{i+1}\mapsto t_i\) for \(1\le i\le k\). There are no other possibilities. The two shifts are distinct for every \(k\ge1\).

**2. Contraction as a partition condition.** Put \(d_i=t_{i+1}-t_i\ge1\) for \(1\le i\le k\). The forward shift is a contraction exactly when the consecutive-domain gap inequalities are
\[
d_{i+1}\le d_i\quad(1\le i<k).
\]
Indeed, because both sequences are increasing, checking consecutive pairs suffices for the Lipschitz condition on all pairs: longer distances are sums of consecutive distances. Likewise the backward shift is a contraction exactly when \(d_i\le d_{i+1}\) for all \(i<k\). Reversing the gap list interchanges these two conditions and preserves the sum.

For a prescribed span \(m=d_1+\cdots+d_k\), weakly decreasing positive gap lists are precisely the \(p_k(m)\) integer partitions of \(m\) into \(k\) positive parts. The first vertex may occupy any of the \(n-m\) positions \(1,\ldots,n-m\), provided \(m\le n-1\). There are the same number of backward shifts, and these are disjoint from the forward shifts. The exact coefficient formula follows:
\[
E_{n,k}=2\sum_{m=k}^{n-1}(n-m)p_k(m).
\]
In particular, for \(1\le k<n\), the choice of \(k+1\) consecutive vertices establishes attainability. For \(k=n-1\) the formula gives exactly two maps, namely the shifts along the entire chain; this boundary specialization is not claimed as independently new.

**3. Generating function.** Holding \(m\) fixed,
\[
\sum_{n\ge m+1}(n-m)z^n=\frac{z^{m+1}}{(1-z)^2}.
\]
The ordinary bivariate generating series for integer partitions by sum and number of parts is
\[
\sum_{m\ge0}\sum_{k\ge0}p_k(m)z^mu^k
=\prod_{j\ge1}\frac{1}{1-uz^j},
\]
where \(p_0(0)=1\). Removing the empty partition and multiplying by the position-and-orientation factor \(2z/(1-z)^2\) yields the boxed formula. Summing over \(k\) gives \(E_n=2\sum_{m=1}^{n-1}(n-m)p(m)\).

**4. Sharp asymptotic.** Let \(c=\pi\sqrt{2/3}\) and \(a=c/2=\pi/\sqrt6\). The classical Hardy–Ramanujan theorem gives \(p(n)\sim e^{c\sqrt n}/(4\sqrt3\,n)\). Rewrite the count as
\[
E_n=2\sum_{j=1}^{n-1}j\,p(n-j).
\]
For each fixed \(t\ge0\), the same asymptotic implies \(p(n-\lfloor t\sqrt n\rfloor)/p(n)\to e^{-at}\). For \(1\le j\le n/2\), its uniform upper and lower estimates imply a constant multiple of \(e^{-aj/\sqrt n}\) bounds the ratio; for \(j>n/2\), monotonicity gives a negligible contribution bounded by \(n^2p(\lfloor n/2\rfloor)=o(np(n))\). Dominated Riemann summation therefore yields
\[
\frac{E_n}{np(n)}\longrightarrow2\int_0^{\infty}t e^{-at}\,dt
=\frac{2}{a^2}=\frac{12}{\pi^2}.
\]
Substitution of the Hardy–Ramanujan estimate gives the claimed constant \(\sqrt3/\pi^2\). The established Fibonacci-type enumeration of \(|\mathcal{OCI}_n|\) in Ahmed and collaborators, Theorem 2.9, implies \(\log|\mathcal{OCI}_n|=n\log\lambda+O(\log n)\). Together these establish the stated logarithmic rarity law.

## Verification
A standalone Python 3 standard-library checker, `verify.py`, iterates over **all** pairs of equal-size subsets of \([n]\), tests the contraction inequalities directly, computes the nilpotency index by iterating the actual partial map rather than by using the proof's path classification, and compares the resulting rank distribution with the independently computed integer-partition expression and Euler-product coefficients. Every case for \(0\le n\le12\) passed. Examples include the complete rank profiles \([0,12,6,2,0]\) at \(n=4\), \([0,56,68,50,28,14,6,2,0]\) at \(n=8\), and \([0,132,250,272,218,148,90,52,28,14,6,2,0]\) at \(n=12\), totaling \(20\), \(224\), and \(1212\), respectively. These finite tests corroborate, but do not replace, the all-\(n\) proof.

## Relationship to prior work
Ahmed, AlDhamri, Al-Kharousi, Klein and Umar (arXiv:2203.06417v1, March 12, 2022, especially Theorems 2.6 and 2.9) enumerate all maps by rank and number of fixed points, and the full semigroup. **Their specialization \(m=0\) already counts every nilpotent by rank**, since strictly order-preserving partial injections have no nontrivial cycles. The present result neither reclaims nor needs to reprove that broader count: it refines the nilpotent stratum by the **largest possible nilpotency index**, a statistic not specified by fixed-point number or rank alone, with its own partition-product series and asymptotics.

Zubairu and Ali (2024, Section 4 and Theorem 4.13) count a restricted domain-gap family of nilpotents in the same semigroup, and treat rank-\(n-1\) nilpotents in the larger partial contraction semigroup. Their specialized count does not determine the unrestricted rank-by-extremal-index series here. Al-Kharousi and collaborators (2025) establish Green's relations and generating rank of the same monoid, without an index-refined nilpotent enumerator. The Hardy–Ramanujan partition asymptotic is used as established prior mathematics, not presented as new.

## Limitations
No claim is made to count nilpotents at all intermediate indices, or to characterize the multiplication of the extremal-index locus (which need not be a subsemigroup). The generating function is an identity of formal power series and the asymptotic is for \(n\to\infty\); the formula does not imply that a random nilpotent typically has maximal index relative to its rank. Publication-priority assessment is necessarily conditional on accessible sources, including the possibility of implicit index-refined consequences of older semigroup results. Independent mathematical audit has not been performed.

## References
1. B. M. Ahmed, N. AlDhamri, F. Al-Kharousi, G. Klein, and A. Umar, *Combinatorial results for order-preserving partial injective contraction mappings*, arXiv:2203.06417v1, first public March 12, 2022; Contributions to Discrete Mathematics 19(2) (2024), 1–19. https://arxiv.org/abs/2203.06417
2. M. M. Zubairu and B. Ali, *On the nilpotents of the semigroup of partial contractions of a finite chain*, International Journal of Mathematical Analysis and Modelling 7(2) (2024), 144–152; published September 25, 2024. https://journal.tnsmb.org/index.php/ijmam/article/view/158
3. F. Al-Kharousi, G. U. Garba, M. J. Ibrahim, A. T. Imam, and A. Umar, *On the semigroup of finite order-preserving partial injective contraction mappings*, Afrika Matematika 36 (2025), article 48. https://doi.org/10.1007/s13370-025-01259-z
4. G. H. Hardy and S. Ramanujan, *Asymptotic Formulae in Combinatory Analysis*, Proceedings of the London Mathematical Society s2-17 (1918), 75–115. https://doi.org/10.1112/plms/s2-17.1.75
