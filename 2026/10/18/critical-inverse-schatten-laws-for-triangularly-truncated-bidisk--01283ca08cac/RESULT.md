# Critical inverse-Schatten laws for triangularly truncated bidisk shifts

## Finding

The exact nonzero singular spectrum of total-degree truncations of multiplication by a linear bidisk polynomial yields a **sharp inverse-Schatten transition** at equality of its two coefficient moduli. In the balanced case, inverse moments change from quadratic growth, through quadratic-logarithmic growth, to growth of order \(N^{p+1}\) as the inverse-Schatten exponent passes \(p=1\). A near-balance window of width \(N^{-1}\) has an explicit limiting crossover function.

For \(N\ge1\) and complex \((a,b)\ne(0,0)\), let \(A=|a|\) and \(B=|b|\). The positive singular values, with multiplicity, are
\[
\left\{\sqrt{A^2+B^2+2AB\cos(\pi r/j)}:
 2\le j\le N+1,\quad 1\le r\le j-1\right\}.
\]
There are \(N(N+1)/2\) positive singular values and exactly \(N+1\) zero singular values. The extreme positive singular values are
\[
 s_{\min}=\sqrt{A^2+B^2-2AB\cos\frac{\pi}{N+1}},\qquad
 s_{\max}=\sqrt{A^2+B^2+2AB\cos\frac{\pi}{N+1}}.
\]
When \(A=B=c>0\), the nonzero condition number is exactly
\(\cot(\pi/[2(N+1)])\); when \(A\ne B\), it tends to \((A+B)/|A-B|\).

Write \(Q_{N,p}(a,b)=\operatorname{tr}|T_N(a,b)^\dagger|^p\), for fixed \(p>0\). In the unequal-modulus case,
\[
\lim_{N\to\infty}\frac{Q_{N,p}(a,b)}{N^2}=
\frac1{2\pi}\int_0^\pi(A^2+B^2+2AB\cos\theta)^{-p/2}\,d\theta.
\]
If \(A=B=c>0\), let \(I_p=\int_0^1[2\sin(\pi x/2)]^{-p}\,dx\), finite for \(0<p<1\). Then
\[
Q_{N,p}(c,c)\sim
\begin{cases}
\displaystyle \frac{c^{-p}I_p}{2}N^2,&0<p<1,\\[3pt]
\displaystyle \frac{N^2\log N}{2\pi c},&p=1,\\[3pt]
\displaystyle \frac{c^{-p}\zeta(p)}{\pi^p(p+1)}N^{p+1},&p>1.
\end{cases}
\]
At \(p=2\) there is also the exact identity
\[
Q_{N,2}(c,c)=\frac{N(N+1)(2N+7)}{36c^2}.
\]
For each fixed \(c>0\), \(\tau\ge0\), and \(p>1\), set \(a_N=c+\tau/(2N)\) and \(b_N=c-\tau/(2N)\), which are positive for sufficiently large \(N\). The complete critical window is
\[
\boxed{\lim_{N\to\infty}\frac{Q_{N,p}(a_N,b_N)}{N^{p+1}}
=\Phi_{p,c}(\tau):=\int_0^1\sum_{t=1}^\infty
\left[\tau^2+\left(\frac{\pi ct}{u}\right)^2\right]^{-p/2}\,du.}
\]
In particular \(\Phi_{p,c}(0)=c^{-p}\zeta(p)/[\pi^p(p+1)]\). For \(p=2\), with the integrand continuously extended at \(\tau=0\),
\[
\Phi_{2,c}(\tau)=\int_0^1
\frac{(\tau u/c)\coth(\tau u/c)-1}{2\tau^2}\,du,
\qquad \Phi_{2,c}(0)=\frac1{18c^2}.
\]

## Assumptions and scope

The ambient Hilbert space is the standard analytic Hardy space \(H^2(\mathbb D^2)\) with orthonormal monomial basis \(z^i w^j\), for nonnegative integers \(i,j\). Let \(\mathcal H_N=\operatorname{span}\{z^i w^j:i+j\le N\}\), let \(P_N\) be its orthogonal projection, and define the finite matrix/operator \(T_N(a,b)=P_NM_{az+bw}|_{\mathcal H_N}\). The dagger denotes its Hilbert-space Moore–Penrose inverse, not an inverse on its kernel. Trace and Schatten powers are finite-dimensional. All limits are as integer \(N\to\infty\), with parameters held fixed except where the near-critical scaling is explicitly specified. The coefficients may be complex, but only their moduli affect singular values.

## Proof

**Exact spectrum.** Decompose \(\mathcal H_N=\bigoplus_{k=0}^N\mathcal D_k\) into homogeneous degrees. The operator sends \(\mathcal D_k\) into \(\mathcal D_{k+1}\) for \(k<N\), and kills \(\mathcal D_N\). In the ordered monomial bases, the degree-\(k\) block is a \((k+2)\times(k+1)\) bidiagonal matrix with two constant diagonals \(a,b\). Its Gram matrix has diagonal entries \(A^2+B^2\) and conjugate off-diagonal entries \(\bar a b\) and \(a\bar b\). A diagonal unitary gauge turns the off-diagonal entries into \(AB\). The standard sine vectors with coordinates \(\sin(\ell r\pi/(k+2))\), indexed by \(1\le \ell\le k+1\) and \(1\le r\le k+1\), diagonalize that Gram matrix, with eigenvalues \(A^2+B^2+2AB\cos(r\pi/(k+2))\). They are strictly positive even when one coefficient is zero. Taking \(j=k+2\) proves the complete multiset and the stated rank and nullity. Since the extreme cosine magnitude increases strictly as \(j\) grows, the stated extremal values follow. The balanced condition-number identity uses \(1-\cos x=2\sin^2(x/2)\) and \(1+\cos x=2\cos^2(x/2)\).

**Unequal-modulus inverse moments.** Write the exact trace as
\[
Q_{N,p}=\sum_{j=2}^{N+1}\sum_{r=1}^{j-1}
(A^2+B^2+2AB\cos(\pi r/j))^{-p/2}.
\]
If \(A\ne B\), the summand is a bounded continuous function of \(r/j\) on the closed unit interval. Hence the inner sum divided by \(j\) converges to its integral on \([0,1]\). Summing with \(\sum_{j=2}^{N+1}j\sim N^2/2\) gives the first limit. This argument also covers a zero coefficient.

**Balanced inverse moments.** For \(A=B=c>0\), set \(t=j-r\); the eigenvalue square root becomes \(2c\sin(\pi t/(2j))\). If \(0<p<1\), the endpoint singularity is integrable and the corresponding increasing positive Riemann sums converge to \(c^{-p}I_p\) after division by \(j\); comparison with the integral on each subinterval controls the singular endpoint. For \(p=1\), the expansion \(2\sin(\pi t/(2j))=\pi t/j+O((t/j)^3)\), together with summation bounds, gives
\(\sum_{t=1}^{j-1}[2c\sin(\pi t/(2j))]^{-1}=(j/(\pi c))\log j+O(j)\). For \(p>1\), the inequalities \(2t/j\le2\sin(\pi t/(2j))\le\pi t/j\) and dominated convergence over \(t\) yield
\[
 j^{-p}\sum_{t=1}^{j-1}[2c\sin(\pi t/(2j))]^{-p}
\longrightarrow c^{-p}\pi^{-p}\zeta(p).
\]
Finally \(\sum_{j\le N+1}j^p\sim N^{p+1}/(p+1)\), and summing the three inner estimates yields the asserted asymptotics. The cosecant identity
\(\sum_{t=1}^{j-1}\csc^2(\pi t/(2j))=2(j^2-1)/3\)
proves the exact \(p=2\) trace by summing \((j^2-1)/(6c^2)\) over \(2\le j\le N+1\).

**Critical window.** For large \(N\) the chosen real coefficients satisfy \(A_N-B_N=\tau/N\) and \(A_NB_N=c^2-\tau^2/(4N^2)\). Relabeling \(t=j-r\),
\[
 s_{j,j-t}^2=\frac{\tau^2}{N^2}+
4\left(c^2-\frac{\tau^2}{4N^2}\right)
\sin^2\frac{\pi t}{2j}.
\]
For \(j/N\to u\in(0,1]\) and fixed \(t\ge1\), multiplication by \(N^2\) yields \(\tau^2+(\pi c t/u)^2\). The elementary bound \(\sin(\pi t/(2j))\ge t/j\), combined with \(A_NB_N\ge c^2/2\) for sufficiently large \(N\), gives the summable uniform bound \(N^{-p}s_{j,j-t}^{-p}\le C_{c,p}(j/N)^p t^{-p}\). For \(p>1\), this bound permits dominated convergence in \(t\) and in the rescaled Riemann sum over \(j\), including the integrable endpoint \(u=0\). This proves the critical-window formula. The classical partial fraction identity for \(\coth\) evaluates its \(p=2\) series.

## Verification

Run `python checker.py` with Python 3 and NumPy. The standalone program constructs the full finite complex matrices independently of the block formula, compares all nonzero singular values for dimensions \(N=1\) through \(13\) across five parameter patterns, checks the exact inverse-square trace through \(N=150\), verifies both extremal singular values, and compares finite critical-window moments with the explicit integral. It reports `PASS 549 finite-matrix/moment/endpoint/crossover assertions`. Floating-point checks have stated tolerances; they are independent numerical consistency tests, not the proof of asymptotic or general-dimensional claims.

## Relationship to prior work

The finite-section domain has the triangular monomial geometry studied in Rinkel and Seghier's 2013 work on inverses and trace asymptotics of **positive self-adjoint** truncated Toeplitz symbols. That paper's central theorem assumes a positive symbol with bounded reciprocal and studies the inverse of the compressed symbol, while the present operator is a finite section of **analytic multiplication** and the invariant is the Moore–Penrose inverse of that section. In particular, at balanced moduli the associated \(|az+bw|^2\) symbol vanishes on the torus and fails the bounded-inverse hypothesis. Widom's 1989 work concerns general Toeplitz singular-value distributions under its stated regularity conditions, rather than this total-degree triangular finite-section spectrum or its sharp near-critical inverse-moment crossover. Elementary tridiagonal sine spectra themselves are classical; the claimed additional content is the combined explicit triangular singular multiset, sharp inverse-moment transition, exact inverse-square finite law, and near-balance scaling function.

## Limitations

No claim is made for arbitrary polynomial symbols, arbitrary truncating polygons, or a simultaneous asymptotic regime where \(p\) changes with \(N\). The critical-window formula is proved only for fixed \(p>1\). The results concern the **Moore–Penrose** inverse of a rank-deficient finite section, not the inverse of a different compressed positive Toeplitz operator. Bibliographic comparison does not rule out every historical occurrence of the exact elementary spectrum or its consequences; no independent priority or mathematical verification is claimed.

## References

- J.-M. Rinkel and A. Seghier, *Matrices de Toeplitz tronquées sur des polygones convexes. Cas du triangle*, arXiv:1302.6106v1 (public 25 February 2013), https://arxiv.org/abs/1302.6106.
- H. Widom, *On the Singular Values of Toeplitz Matrices*, Zeitschrift für Analysis und ihre Anwendungen **8** (1989), no. 3, 221–229, https://doi.org/10.4171/ZAA/350.
- J. Demmel and W. Kahan, *Accurate Singular Values of Bidiagonal Matrices*, SIAM Journal on Scientific and Statistical Computing **11** (1990), 873–912, https://doi.org/10.1137/0911052.
