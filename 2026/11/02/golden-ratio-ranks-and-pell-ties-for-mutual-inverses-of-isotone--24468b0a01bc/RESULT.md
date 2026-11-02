# Golden-ratio ranks and Pell ties for mutual inverses of isotone maps

## Finding
For every integer \(n\ge 1\), let \(\mathcal O_n\) be the monoid of weakly increasing self-maps of the chain \([n]\), with composition. An **ordered mutual-inverse pair** is \((f,g)\in\mathcal O_n^2\) satisfying \(fgf=f\) and \(gfg=g\). Its rank is \(r=|\operatorname{im}f|=|\operatorname{im}g|\). The exact count of pairs of rank \(r\), for every \(1\le r\le n\), is
\[
I_{n,r}=\binom{n+r-1}{2r-1}^{\!2}.
\]
Consequently the exact total \(I_n\) and the probability that two independent uniform elements of \(\mathcal O_n\) are mutual inverses are
\[
I_n=\sum_{r=1}^n\binom{n+r-1}{2r-1}^{\!2},\qquad
\Pr(fgf=f,\;gfg=g)=\frac{I_n}{\binom{2n-1}{n}^{\!2}}.
\]

For fixed \(n\), the integer sequence \(r\mapsto I_{n,r}\) is strictly unimodal except possibly for two equal adjacent maxima. Put
\[
\tau_n=\frac{\sqrt{1+5n^2}-1}{5}.
\]
If \(\tau_n\) is not an integer, its unique maximizing rank is \(\lfloor\tau_n\rfloor+1\). If \(\tau_n\in\mathbb Z\), the two maximizing ranks are \(\tau_n\) and \(\tau_n+1\). **Ties occur precisely at the infinite Pell family**
\[
(5r+1)+n\sqrt5=(161+72\sqrt5)^j,
\qquad j=1,2,\ldots,
\]
with the two maximizing ranks \(r\) and \(r+1\). The first tie is \(n=72\), at ranks \(32\) and \(33\).

Write \(\varphi=(1+\sqrt5)/2\). As \(n\to\infty\),
\[
I_n\sim\frac{\varphi^{4n}}{2\sqrt{2\pi}\,5^{1/4}\sqrt n},
\qquad
\Pr(fgf=f,\;gfg=g)\sim
\frac{\sqrt{2\pi}}{5^{1/4}}\sqrt n\left(\frac{\varphi^4}{16}\right)^n.
\]
For an ordered mutual-inverse pair chosen uniformly among all such pairs, let \(R_n\) denote its common rank. Then
\[
\frac{R_n-n/\sqrt5}{\sqrt{n/(5\sqrt5)}}\ \xrightarrow{\mathrm d}\ N(0,1).
\]
More precisely, uniformly when \(|r-n/\sqrt5|=o(n^{2/3})\), the local probability is
\[
\Pr(R_n=r)=\sqrt{\frac{5\sqrt5}{2\pi n}}\,
\exp\!\left(-\frac{5\sqrt5\,(r-n/\sqrt5)^2}{2n}\right)(1+o(1)).
\]

## Assumptions and scope
All maps are full self-maps of the labeled finite *linearly ordered* set \([n]\), not partial maps and not merely order-decreasing maps. Composition may be read right-to-left; the reciprocal equations are invariant under this convention. The term 'inverse' is the semigroup inverse relation (both sandwich identities), not a two-sided group inverse. Counts are of **ordered** pairs. The asymptotic probability is for two independently uniform maps from the entire monoid, whereas the central limit law is for a uniformly selected *valid* pair.

## Proof
**1. Structure of the inverse relation.** Every rank-\(r\) element is uniquely specified by an ordered partition \(K=(K_1<\cdots<K_r)\) of \([n]\) into nonempty consecutive intervals (its kernel) and an increasing \(r\)-element subset \(B=\{b_1<\cdots<b_r\}\) (its image): the element sends \(K_i\) to \(b_i\). Call \(B\) a transversal of \(K\) when \(b_i\in K_i\) for each \(i\). If \(f\) has kernel \(K\) and image \(B\), and \(g\) has kernel \(L\) and image \(D\), the conditions \(fgf=f\), \(gfg=g\) are equivalent to the two independent conditions that \(D\) is a transversal of \(K\) and \(B\) is a transversal of \(L\). More explicitly, the sandwich identities make the restrictions \(f|_D:D\to B\) and \(g|_B:B\to D\) mutually inverse bijections. Since both maps preserve order, they match the \(i\)-th increasing points, whence \(d_i\in K_i\) and \(b_i\in L_i\). Conversely, these two transversality conditions give \(f(d_i)=b_i\) and \(g(b_i)=d_i\) for every \(i\), so both sandwich identities follow. The sandwich identities force the two ranks to agree, since each is at most the other by the rank inequality.

**2. Exact enumeration.** For kernel block sizes \(a_1,\ldots,a_r\ge1\), summing to \(n\), there are precisely \(\prod_i a_i\) transversals. Therefore the number \(E_{n,r}\) of kernel-transversal incidences is the coefficient
\[
E_{n,r}=[z^n]\left(\frac{z}{(1-z)^2}\right)^r
=[z^{n-r}](1-z)^{-2r}=\binom{n+r-1}{2r-1}.
\]
Each ordered inverse pair is specified by an *independent* choice of the two crossed kernel-transversal incidences \((K,D)\) and \((L,B)\). Hence \(I_{n,r}=E_{n,r}^2\). Stars-and-bars also gives \(|\mathcal O_n|=\binom{2n-1}{n}\), establishing the probability formula. In particular \(E_{n,r}\) is also the number of rank-\(r\) idempotents; this latter classical enumeration is not claimed as new.

**3. Exact modes and exceptional ties.** For \(1\le r<n\), direct factorial cancellation yields
\[
\frac{E_{n,r+1}}{E_{n,r}}=\frac{(n+r)(n-r)}{2r(2r+1)}.
\]
The ratio exceeds, equals, or falls below one according as \(n^2\) exceeds, equals, or falls below \(5r^2+2r\). As the latter polynomial increases strictly with positive \(r\), this proves the complete mode classification. Equal adjacent modes require \(n^2=5r^2+2r\), equivalently \((5r+1)^2-5n^2=1\). The positive solutions of Pell's equation \(x^2-5y^2=1\) are \(x+y\sqrt5=(9+4\sqrt5)^m\), \(m\ge1\). Since \(x\equiv(-1)^m\pmod5\), imposing \(x=5r+1\) forces \(m\) even. Writing \(m=2j\) yields exactly \((161+72\sqrt5)^j\), as claimed.

**4. Global asymptotics and Gaussian limit.** For \(x=r/n\) bounded away from \(0\) and \(1\), Stirling's formula applied to \(E_{n,r}=\frac{2r}{n+r}\binom{n+r}{2r}\) gives, uniformly on compact subsets of \((0,1)\),
\[
E_{n,r}=\sqrt{\frac{x}{\pi n(1-x^2)}}\,e^{nh(x)}(1+O(n^{-1})),
\quad h(x)=(1+x)\log(1+x)-(1-x)\log(1-x)-2x\log(2x).
\]
Here \(h'(x)=\log((1-x^2)/(4x^2))\), so \(h\) has its unique interior maximum at \(x_*=1/\sqrt5\). At this point \(h(x_*)=2\log\varphi\) and \((2h)''(x_*)=-5\sqrt5\). The exponential rate is strictly lower on every closed set away from \(x_*\); the endpoint ranges are also exponentially negligible by elementary binomial bounds, so a standard discrete Laplace expansion applies. Squaring the Stirling expression and summing the Gaussian window gives
\[
I_n\sim \frac{x_*}{\pi(1-x_*^2)}\sqrt{\frac{2\pi}{n\cdot5\sqrt5}}\,e^{2nh(x_*)}
=\frac{\varphi^{4n}}{2\sqrt{2\pi}\,5^{1/4}\sqrt n}.
\]
The quadratic Taylor expansion \(2h(x)=2h(x_*)-\frac{5\sqrt5}{2}(x-x_*)^2+O(|x-x_*|^3)\), combined with the same uniform Stirling estimate, proves the stated local central limit formula on the range \(o(n^{2/3})\); exponential tail bounds outside fixed neighborhoods imply weak convergence. Finally, \(\binom{2n-1}{n}\sim4^n/(2\sqrt{\pi n})\), which yields the displayed independent-sampling probability asymptotic.

## Verification
Two independent standalone standard-library Python scripts accompany this manuscript. `verify_direct.py` directly enumerates all pairs of weakly increasing maps through \(n=6\), checks both sandwich identities by actual composition, and independently counts kernel-transversal incidences by integer compositions. `verify_asymptotic.py` enumerates all kernel-transversal incidences through \(n=11\), checks every discrete mode through \(n=150\) including the first Pell tie, and compares the exact total with the asymptotic approximation for \(n=50,100,200,400\). Both generated output files end with `VERIFY_OK`. These finite checks corroborate but do not substitute for the all-\(n\) combinatorial and asymptotic proofs.

## Relationship to prior work
Higgins (2026), arXiv:2610.01912v1, solves the *existence* of permutation matchings in \(\mathcal O_n\) and explicitly describes the kernel-transversal incidence structure and crossed-square inverse relation. This supplies major conceptual prior coverage. It does not give the rank-stratified *number* of ordered inverse pairs, the precise locations of maximizing ranks, the Pell-tie family, the global asymptotic, or the Gaussian inverse-pair rank law. Higgins (2024) posed the existence problem and discussed regular semigroup matchings. The idempotent array \(E_{n,r}\) is classical and appears in OEIS A078812 (and is related to Lavers' Fibonacci work); neither the array itself nor its Fibonacci identities are claimed as new. The contribution isolated here is the complete **inverse-pair rank law together with its exact arithmetic maximizers and asymptotic distribution**, not a new characterization of Green's relations or idempotents.

## Limitations
The mathematical statements concern full monotone maps of a finite **chain**. There is no result for arbitrary posets, partial transformations, all semigroup inverse matchings, or the existence of an involutive matching. The earlier idempotent literature is extensive: Lavers' 1998 chapter *The Fibonacci Pyramid* and Higgins' 1993 combinatorial treatment were identified as comparison risks. The 1998 chapter was accessible only as an abstract and publisher preview in this review, and the 1993 author-uploaded text was in part difficult to read; their complete implications for an inverse-pair central limit theorem were not verified. No absolute historical priority is asserted. The equal-rank modes at Pell sizes are not assertions about the number of distinct matchings; they concern the cardinality of the mutual-inverse relation.

## References
1. P. M. Higgins, *Balanced weightings and permutation matchings applied to the monoid of order-preserving mappings*, arXiv:2610.01912v1, first submitted 2026-10-01. https://arxiv.org/html/2610.01912v1
2. P. M. Higgins, *Finite regular semigroups with permutations that map elements to inverses*, Semigroup Forum 109 (2024), 141–147, DOI:10.1007/s00233-024-10430-0. https://link.springer.com/article/10.1007/s00233-024-10430-0
3. P. M. Higgins, *Combinatorial results for semigroups of order-preserving mappings*, Math. Proc. Camb. Phil. Soc. 113 (1993), 281–296, DOI:10.1017/S0305004100075964.
4. T. G. Lavers, *The Fibonacci Pyramid*, in Applications of Fibonacci Numbers, vol. 7 (1998), 255–263, DOI:10.1007/978-94-011-5020-0_28.
5. OEIS Foundation, A078812, triangular array containing \(\binom{n+r-1}{2r-1}\), https://oeis.org/A078812.
