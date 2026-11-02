# Arcsine firing fractions and exact two-cycle mass census on complete bipartite sandpiles

## Finding
For all integers \(a,b\ge1\), the synchronous, degree-threshold parallel chip-firing map on the labelled simple complete bipartite graph \(K_{a,b}\) has an exact mass-resolved primitive-two-cycle orbit polynomial. Let \(P_{a,b}(z)\) count each orbit once with weight \(z^M\), where \(M\) is its conserved total number of chips, and write \([k]_z=1+z+\cdots+z^{k-1}\) for positive \(k\). Then
\[
\begin{aligned}
P_{a,b}(z)={}&z^{ab}[b]_z^a[a]_z^b\\
&+\frac12\sum_{i=1}^{a-1}\sum_{j=1}^{b-1}\binom ai\binom bj
z^{ib+ja+2(a-i)(b-j)}
[b-j]_z^i[j]_z^{a-i}[a-i]_z^j[i]_z^{b-j}.
\end{aligned}
\tag{1}
\]
Empty double sums are zero. In particular, \(P_{a,b}(z)=z^{4ab-a-b}P_{a,b}(z^{-1})\).

For balanced bicliques \(a=b=n\), the exact number \(N_n=P_{n,n}(1)\) of primitive two-cycle orbits is
\[
\boxed{N_n=\frac{n^{2n}}2\sum_{k=0}^{n}
\left(\frac{n!}{(n-k)!n^k}\right)^2},\qquad n\ge1,
\tag{2}
\]
with asymptotic
\[
\boxed{N_n\sim\frac{\sqrt{\pi n}}4\,n^{2n}}.
\tag{3}
\]
Choose one of these orbits uniformly, then one of its two temporal phases uniformly. If \(I_n\) is the number of currently firing vertices on one specified shore, then
\[
\boxed{\frac{I_n}{n}\xrightarrow{d}\operatorname{Beta}(\tfrac12,\tfrac12)},
\qquad
\mathbb P\!\left(\frac{I_n}{n}\le t\right)\longrightarrow
\frac2\pi\arcsin\sqrt t\quad(0\le t\le1).
\tag{4}
\]
In particular the firing fraction does not concentrate at one half. The arcsine law and the square-root correction to the orbit count describe an extensive family of coexistence modes invisible to period-existence classifications.

## Assumptions and scope
Vertices carry nonnegative integral chip loads \(x_v\). In a synchronous update, each vertex with at least its graph degree in chips sends one chip to each neighbour; all firing decisions use the pre-update state. Vertices are individually labelled; no graph-automorphism quotient is taken. A primitive two-cycle is an unordered pair \(\{x,F(x)\}\) with \(F^2(x)=x\) and \(F(x)\ne x\). The polynomial (1) and its symmetry concern precisely the states already on such orbits, not their transient basins. The limit (4) concerns only the balanced family and uniform selection among these finite orbits/phases.

## Proof
**Complementary firing phases.** Let \(S\) and \(T\) be the firing sets at the two phases of a primitive two-cycle on any connected graph. The chip-change vector over two updates is minus the graph Laplacian applied to \(\mathbf1_S+\mathbf1_T\). Since it vanishes, this integer vector is constant. Its only possible constant values are zero, one and two. Values zero or two mean no vertex ever fires, or every vertex always fires; either makes the state fixed. Therefore \(T=V\setminus S\).

For each vertex \(v\), put \(d_v=\deg(v)\) and \(c_v=\#\{w\sim v:\mathbf1_S(w)\ne\mathbf1_S(v)\}\). The first update decreases the chip count by \(c_v\) at vertices in \(S\) and increases it by \(c_v\) outside \(S\). Both phase firing tests are satisfied exactly when
\[
 x_v\in\begin{cases}
 \{d_v,\ldots,d_v+c_v-1\},&v\in S,\\
 \{d_v-c_v,\ldots,d_v-1\},&v\notin S.
\end{cases}\tag{5}
\]
Every \(c_v\) must be positive. Conversely every assignment from these intervals gives a genuine two-cycle: the indicated inequalities enforce the complementary second firing set, and two updates then cancel. All intervals contain only nonnegative integers because \(c_v\le d_v\). Every orbit is represented by exactly two choices of its phase state.

**Evaluation on the biclique.** Write \(i=|S\cap A|\) and \(j=|S\cap B|\), where \(|A|=a\), \(|B|=b\). Positivity of all \(c_v\) forces either \((i,j)=(a,0)\), \((0,b)\), or \(1\le i\le a-1\) and \(1\le j\le b-1\). In the mixed case the four vertex categories (firing/nonfiring on each shore) have opposing-neighbour counts \(b-j,j,a-i,i\), respectively, and their minimum loads are \(b,b-j,a,a-i\), respectively. Multiplication of their independent finite geometric series, with \(\binom ai\binom bj\) labelled choices, gives the double sum in (1). The two pure-shore phase families together contribute twice \(z^{ab}[b]_z^a[a]_z^b\); dividing all phased states by two gives (1).

The involution \(x_v\mapsto2d_v-1-x_v\) interchanges the two firing statuses at every vertex and preserves the cycle condition (5). Its effect on the total mass is \(M\mapsto 4ab-a-b-M\), proving the reflection identity.

**Balanced trace and exact sum.** For \(0\le i,j\le n\), define the stochastic matrix
\[
 K_n(i,j)=\binom nj\left(1-\frac in\right)^j\left(\frac in\right)^{n-j},
\tag{6}
\]
with the standard interpretation of zero powers at endpoints. In the above double count, the number of phased two-cycle states having exactly \(i\) firing vertices on the left shore and \(j\) on the right is
\[
 n^{2n}K_n(i,j)K_n(j,i).
\tag{7}
\]
This also includes the two endpoint phase classes \((i,j)=(n,0),(0,n)\), and all other endpoint classes have weight zero. Consequently
\[
 2N_n=n^{2n}\operatorname{tr}(K_n^2).
\tag{8}
\]
Treat \(K_n\) as acting on functions on \(\{0,\ldots,n\}\). If \(J\) has distribution \(\operatorname{Bin}(n,1-i/n)\), its \(k\)-th moment is a polynomial in \(i\) of degree at most \(k\), with coefficient of \(i^k\) equal to \((-1)^k(n)_k/n^k\), where \((n)_k=n!/(n-k)!\). Indeed, write ordinary powers in the falling-factorial basis and use \(\mathbb E(J)_k=(n)_k(1-i/n)^k\). Thus, in the polynomial basis of all functions on these \(n+1\) points, \(K_n\) is triangular with diagonal eigenvalues \((-1)^k(n)_k/n^k\), \(0\le k\le n\). Tracing its square establishes (2).

For \(k\) of order \(\sqrt n\),
\[
\left(\frac{(n)_k}{n^k}\right)^2
=\prod_{h=0}^{k-1}(1-h/n)^2
=\exp\!\left(-\frac{k^2}{n}+o(1)\right).
\]
Moreover \(\prod_{h<k}(1-h/n)^2\le \exp(-k(k-1)/n)\). Dominated Gaussian Riemann summation yields
\[
\frac1{\sqrt n}\operatorname{tr}(K_n^2)
\longrightarrow\int_0^\infty e^{-u^2}\,du=\frac{\sqrt\pi}{2},
\]
which proves (3).

**Arcsine law.** Put \(m_n(i)=\sum_jK_n(i,j)K_n(j,i)\); the law of \(I_n\) is exactly \(m_n(i)/\operatorname{tr}(K_n^2)\). Uniformly for \(r=i/n\) in any compact subinterval of \((0,1)\), two binomial local central limit estimates, centered at \(j=n-i\), give
\[
 m_n(i)=\frac{1+o(1)}{2\sqrt{\pi n r(1-r)}}.
\tag{9}
\]
For completeness, writing \(j=n-i+s\) with \(|s|\le n^{3/5}\), the two binomial masses have the joint asymptotic
\[
 K_n(i,j)K_n(j,i)=
\frac{1+o(1)}{2\pi n r(1-r)}
\exp\!\left(-\frac{s^2}{nr(1-r)}\right),
\]
where the uniformly valid local approximation can first be restricted to \(|s|\le n^{1/2+\epsilon}\), \(0<\epsilon<1/6\); the remaining tails are negligible by binomial concentration. Summing over \(s\) gives (9). At the endpoints \(m_n(0)=m_n(n)=1\). For \(1\le i\le n-1\), the maximum of a binomial point probability at \(i\) is \(\binom ni(i/n)^i(1-i/n)^{n-i}\), so the exact stochastic row sum implies
\[
 m_n(i)\le\binom ni (i/n)^i(1-i/n)^{n-i}
\le\frac{C}{\sqrt{nr(1-r)}}.
\tag{10}
\]
Consequently the two boundary intervals \(r\le\delta\) and \(r\ge1-\delta\) contribute at most \(O(\sqrt\delta)\) of the normalized total, uniformly as \(n\to\infty\). Combining (9), the trace limit, and Riemann sums proves convergence to the density \(1/(\pi\sqrt{r(1-r)})\) on \((0,1)\), i.e. (4).

## Verification
The accompanying standard-library `verify.py` independently enumerates every confined labelled chip configuration for seven small bicliques (including the full \(K_{3,3}\) state space); computes first and second synchronous updates; compares the primitive-cycle mass histograms with (1); checks the polynomial reflection and counting formulas for every \(1\le a,b\le4\); checks the exact spectral expression against the mass polynomial for balanced sizes through four; and checks the independent phased-cut/spectral identity through balanced size fourteen. The exact-arithmetic run reports `BIPARTITE_TWO_CYCLE_EXACT_OK`. It checks finite arithmetic and boundary cases, not the proof of either infinite asymptotic law.

## Relationship to prior work
Jiang's original complete-bipartite chip-firing classification [1], first public on 2010-03-04, establishes the possible period lengths and constructions, not an exact population distribution of primitive period-two orbits or an arcsine phase law. Levine's complete-graph work [2] treats activity and rotation-number staircases, rather than these exact balanced-biclique statistics. Bipartite random mappings have an established component-limit theory [3]. The binomial transition kernel here is related to the classical Wright–Fisher operator; the spectral triangularization itself is not claimed as a new general method. The 2026 complete-bipartite middle-stair theorem [4] establishes eventual period two in a chip-mass interval, a different quantifier from enumerating states *already* on primitive two-cycles. The present result's claimed contribution is the explicit orbit-mass formula and the particular square-root/arcsine statistical law under uniform periodic-orbit sampling.

## Limitations
No statement here enumerates fixed points, other primitive periods, attraction-basin measures or transient entry times. The limiting arcsine law assumes \(a=b=n\to\infty\); no claim of an analogous law for fixed unequal ratios is made. The existence of an earlier unpublished or unindexed equivalent, especially through the bipartite random-mapping correspondence, remains a literature risk. Relevant later preprint [4] was accessible only by its abstract during comparison, not in full text. The calculation and its boundary cases have same-author mathematical and computational checks, not independent external validation.

## References
[1] Tian-Yi Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943, first version 2010-03-04, especially Section 3 and Theorem 3.10. https://arxiv.org/abs/1003.0943

[2] Lionel Levine, *Parallel Chip-Firing on the Complete Graph: Devil's Staircase and Poincaré Rotation Number*, arXiv:0811.2800, first version 2008-11-17. https://arxiv.org/abs/0811.2800

[3] Jennie Hansen and Jerzy Jaworski, *Large components of bipartite random mappings*, Random Structures & Algorithms **17** (2000), 317–342, doi:10.1002/1098-2418(200010/12)17:3/4<317::AID-RSA7>3.0.CO;2-7.

[4] Minkyu Jung, *The Middle Stair for Complete Bipartite Parallel Chip-Firing*, arXiv:2608.01350, first posted 2026-08-02. https://arxiv.org/abs/2608.01350
