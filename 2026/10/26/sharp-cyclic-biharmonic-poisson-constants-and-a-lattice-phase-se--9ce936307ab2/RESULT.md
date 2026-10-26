# Sharp cyclic biharmonic Poisson constants and a lattice-phase second term

## Finding
For each integer \(n\ge3\), let \(C_n\) be the unit-conductance cycle, let \(L_n=2I-S-S^{-1}\) be its **unnormalized** graph Laplacian on \(\mathbb C^n\), and define the mean-zero biharmonic Poisson inverse \(B_n=(L_n^2)^\dagger=(L_n^\dagger)^2\). Here \(\dagger\) means Moore–Penrose pseudoinverse, with the constant mode mapped to zero. Set
\[
t_{n,d}=d(n-d),\qquad A_n=n^4+10n^2-11\qquad(0\le d<n).
\]
Every matrix row of \(B_n\) is a cyclic translate of
\[
b_{n,d}=\frac{A_n-30t_{n,d}(t_{n,d}+2)}{720n}.\tag{1}
\]
Put
\[
T_n=-1+\sqrt{\frac{n^4+10n^2+19}{30}},\qquad
r_n=\frac{n-\sqrt{n^2-4T_n}}{2},\qquad k_n=\lfloor r_n\rfloor.
\]
Then \(0<r_n<n/2\), \(b_{n,d}\ge0\) precisely for \(d\in\{0,\ldots,k_n\}\cup\{n-k_n,\ldots,n-1\}\) (including a possible zero at the cutoff), and the **attained sharp operator norms** are equal:
\[
\boxed{\|B_n\|_{\ell^\infty\to\ell^\infty}=\|B_n\|_{\ell^1\to\ell^1}=\sum_{d=0}^{n-1}|b_{n,d}|.}\tag{2}
\]
They have the exact polynomial-sum form
\[
\boxed{\|B_n\|=\frac{(2k_n+1)A_n-60\bigl[(n^2-2)\Sigma_2(k_n)-2n\Sigma_3(k_n)+\Sigma_4(k_n)+2n\Sigma_1(k_n)\bigr]}{360n},}\tag{3}
\]
where \(\Sigma_j(k)=\sum_{d=1}^k d^j\) and the standard Faulhaber formulas make (3) an explicit rational number for every \(n\).

The second-order asymptotic does **not** have a constant coefficient. Define
\[
\xi=\frac{1-\sqrt{1-4/\sqrt{30}}}{2},\quad
w=\sqrt{1-4/\sqrt{30}},\quad
\vartheta_n=\{r_n\},\quad \mathcal B_2(u)=u^2-u+\frac16,
\]
\[
\mathcal A=\frac\xi{180}-\frac16\left(\frac{\xi^3}{3}-\frac{\xi^4}{2}+\frac{\xi^5}{5}\right),\quad
\mathcal G=\frac{\xi-3\xi^2+2\xi^3}{18},\quad
\mathcal C=-\frac{w}{6\sqrt{30}}<0.
\]
For all integers \(n\to\infty\), uniformly across cutoff phases,
\[
\boxed{\|B_n\|=\mathcal A n^4+n^2\bigl[\mathcal G+\mathcal C\,\mathcal B_2(\vartheta_n)\bigr]+O(n).}\tag{4}
\]
The normalized corrections \(n^{-2}(\|B_n\|-\mathcal A n^4)\) have **exact accumulation set**
\[
\boxed{\left[\mathcal G+\frac{\mathcal C}{6},\quad
\mathcal G-\frac{\mathcal C}{12}\right]},\tag{5}
\]
a nondegenerate interval numerically near \([0.0026337828606,0.0065844571516]\). In particular, there is no constant \(\mathcal D\) for which \(\|B_n\|=\mathcal A n^4+\mathcal D n^2+o(n^2)\).

## Assumptions and scope
The vertex counting measure is **not normalized** when defining the induced \(\ell^1\) and \(\ell^\infty\) norms. All edges have unit conductance, and the Laplacian is \(2I-S-S^{-1}\), rather than the random-walk normalized Laplacian. The inverse acts on zero-mean data, but its endpoint norms here are the operator norms of the canonical zero-on-constants extension on all of \(\ell^1(C_n)\) and all of \(\ell^\infty(C_n)\). No assertion is made about the potentially different quotient-space norm obtained by restricting both domain and codomain to mean-zero vectors.

## Proof
**1. Green kernel.** Put \(t_d=d(n-d)\). For \(1\le d\le n-1\), cyclic second differences give
\[
(2-S-S^{-1})t_d=2,\qquad
(2-S-S^{-1})t_d^2=-2(n^2+1)+12t_d.
\]
At \(d=0\), these left sides instead equal \(-2(n-1)\) and \(-2(n-1)^2\). The first-order mean-zero Green kernel for the cycle is
\[
g_d=\frac{n^2-1}{12n}-\frac{t_d}{2n},\qquad L_ng=\delta_0-\frac1n\mathbf1.
\]
The finite sums \(\sum_{d=0}^{n-1}t_d=n(n^2-1)/6\) and \(\sum_{d=0}^{n-1}t_d^2=n(n^4-1)/30\) show that the vector in (1) has mean zero. Substituting (1) into the cyclic differences gives \(L_nb=g\), including at \(d=0\), so \(L_n^2b=\delta_0-\frac1n\mathbf1\). Because the cycle is connected, \(L_n^2\) is invertible on \(\mathbf1^\perp\), and this uniquely determines its Moore–Penrose inverse row. That proves (1) without assuming a continuum approximation.

**2. Signs and exact endpoint norm.** The polynomial \(t(t+2)\) increases strictly for \(t\ge0\), and \(t_d=d(n-d)\) increases for \(0\le d\le n/2\). The positive root of \(t(t+2)=A_n/30\) is \(T_n\). Since \(b_{n,0}>0\) and \(b_{n,\lfloor n/2\rfloor}<0\) for all \(n\ge3\) (substitution gives a strictly negative numerator, separately for even and odd \(n\)), the crossing radius lies strictly between \(0\) and \(n/2\). Thus (1) changes sign once on each half-cycle and its nonnegative entries occur at precisely the displayed cutoffs. Circulant symmetry and self-adjointness imply equality of the induced \(\ell^1\) and \(\ell^\infty\) norms, each the absolute row sum. The input \(f(j)=\operatorname{sgn}(b_{n,j})\) attains the \(\ell^\infty\) norm at vertex \(0\), and a signed unit impulse attains the \(\ell^1\) norm. The zero row sum yields \(\sum|b|=4[\frac12b_{n,0}+\sum_{d=1}^{k_n}b_{n,d}]\). Expanding the quartic in \(d\) gives (3).

**3. Second term.** Write \(x=d/n\), \(z=x(1-x)\), and
\[
f(x)=\frac{1-30z^2}{720},\qquad h(x)=\frac{1-6z}{72}.
\]
Equation (1) is the exact decomposition
\[
b_{n,d}=n^3f(d/n)+n h(d/n)-\frac{11}{720n}.
\]
Here \(f(\xi)=0\), \(f'(0)=0\), and \(f'(\xi)=-w/(12\sqrt{30})\). The root equation yields \(r_n=n\xi+O(n^{-1})\), hence \(k_n=n\xi-\vartheta_n+O(n^{-1})\). Apply the Euler–Maclaurin trapezoid expansion to \(\frac12b_{n,0}+\sum_{d=1}^{k_n}b_{n,d}\). Since \(f\) and \(h\) are polynomials, its remainder is uniform. Writing \(\delta_n=k_n-n\xi=-\vartheta_n+O(n^{-1})\), the terms of orders \(n^4\) and \(n^2\) are respectively
\[
4n^4\int_0^\xi f(x)\,dx,\quad
4n^2\left[\int_0^\xi h(x)\,dx
+f'(\xi)\left(\frac{\delta_n^2}{2}+\frac{\delta_n}{2}+\frac1{12}\right)\right].
\]
All omitted terms are \(O(n)\), uniformly in the fractional phase. As \(\delta_n=-\vartheta_n+O(n^{-1})\), the quadratic factor becomes \(\mathcal B_2(\vartheta_n)/2+O(n^{-1})\). Evaluating the two integrals gives \(\mathcal A=4\int_0^\xi f\), \(\mathcal G=4\int_0^\xi h\), and \(\mathcal C=2f'(\xi)\). This is (4).

**4. Exact accumulation interval.** If \(\xi\) were rational, then \(\xi(1-\xi)=1/\sqrt{30}\) would be rational, a contradiction. Thus \(\{n\xi\}\) is dense in \([0,1]\); perturbing \(n\xi\) by \(O(n^{-1})\) preserves this density on the circle. The continuous periodic extension of \(\mathcal B_2\) has range \([-1/12,1/6]\) because \(\mathcal B_2(0)=\mathcal B_2(1)=1/6\). With \(\mathcal C<0\), (4) proves precisely (5), not merely a pair of subsequential limits.

## Verification
Run `python3 CHECK.py` with Python 3. The checker independently verifies the exact mean-zero fourth-difference identity, absolute-row sums and sign cutoffs for cycles with \(3\le n\le150\), reconstructs the kernel by an independently implemented Fourier series for \(3\le n\le60\), and tests high-precision asymptotic residuals at several further sizes. It reports 13,604 finite assertions passed. These checks are auxiliary evidence; the universal identities, uniform remainder and exact accumulation set follow from the proof above.

## Relationship to prior work
Zhang and Yang (first publicly available September 5, 2006) study resistance distances and Kirchhoff indices of circulant graphs, involving the first inverse power of the graph Laplacian. Lipman, Rustamov and Funkhouser (2010) introduced biharmonic distance, which uses inverse-squared spectral weights. Wei, Li and Yang (2021) develop graph biharmonic distance and give general spectral representations, including for finite abelian Cayley graphs. These provide motivation and compatible spectral calculus, but do not give the absolute-row endpoint norm (2)–(3) or the nonconstant, sharp order-\(n^2\) lattice phase in (4)–(5). The present statement concerns a stability norm, not pairwise resistance distance, biharmonic distance, or the trace/index.

## Limitations
This is a theorem for the unweighted finite cycle and for the zero-on-constants pseudoinverse. It does not cover paths, inhomogeneous edge conductances, higher-dimensional tori, general fractional powers, or norms restricted to the mean-zero subspace. Published-work comparisons cannot establish absolute priority; a relevant 2010 full paper was not accessible beyond author-posted synopsis and indexed excerpts, and older specialized formulas may exist. No independent verification has been performed.

## References
1. H. Zhang and Y. Yang, “Resistance distance and Kirchhoff index in circulant graphs,” *International Journal of Quantum Chemistry* 107 (2007), 330–339; first available 2006-09-05. DOI: `10.1002/qua.21068`.
2. Y. Lipman, R. M. Rustamov, and T. Funkhouser, “Biharmonic Distance,” *ACM Transactions on Graphics* 29 (2010), article 27. DOI: `10.1145/1805964.1805971`; author manuscript: `https://www.cs.princeton.edu/~funk/biharmonic.pdf`.
3. Y. Wei, R.-h. Li, and W. Yang, “Biharmonic distance of graphs,” arXiv:2110.02656 (initial preprint 2021-10-06). `https://arxiv.org/abs/2110.02656`.
