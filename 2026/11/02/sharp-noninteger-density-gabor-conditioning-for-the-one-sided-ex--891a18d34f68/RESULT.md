# Sharp noninteger-density Gabor conditioning for the one-sided exponential

## Finding
Let \(g_\gamma(x)=\sqrt{2\gamma}\,e^{-\gamma x}\mathbf1_{(0,\infty)}(x)\) for \(\gamma>0\). Define \(T_a f(x)=f(x-a)\), \(M_b f(x)=e^{2\pi i bx}f(x)\), and the rectangular Gabor system \(\mathcal G(g_\gamma,a,b)=\{M_{mb}T_{na}g_\gamma:m,n\in\mathbb Z\}\). Suppose \(a,b>0\) and \(ab=2/3\). Its optimal frame bounds are explicitly as follows. Set
\[
\eta=\gamma/b,\quad u=e^{-2\eta/3},\quad h(u)=\frac{4u(1+u^2)(1-u)^2}{(1+u^3)^2},\quad q(u)=\sqrt{1-h(u)},\quad F(u)=\frac{\eta(1+u^3)}{(1-u)(1-u^3)}.
\]
Then \(0<h(u)<1\), and the **sharp lower and upper frame bounds** are
\[
A=F(u)u(1-q(u)),\qquad B=F(u)(1+q(u)).
\]
In particular the squared-analysis/frame-operator condition number is \(K(u)=B/A=(1+q(u))/(u(1-q(u)))\). This has a **unique** minimizer on all positive rectangular lattices of density \(3/2\). Writing
\[
s_*=\frac{3+\sqrt{65}}2,\qquad v_*=\frac{s_*-\sqrt{s_*^2-4}}2,\qquad u_*=\sqrt{v_*},\qquad\eta_*=-\frac34\log v_*,
\]
the sole optimum for fixed \(\gamma\) is
\[
b_*=\gamma/\eta_*,\qquad a_*=2\eta_*/(3\gamma).
\]
Numerically \(\eta_*=1.2569812817600339\ldots\), \(A_*=0.38458255607269\ldots\), \(B_*=4.32192017827218\ldots\), and \(K_*=11.2379516700057\ldots\).

## Assumptions and scope
All functions lie in \(L^2(\mathbb R)\), with the stated Fourier-modulation convention. The window has unit squared norm; the indicator's endpoint convention is immaterial almost everywhere. The frame bounds refer to the best constants in \(A\|f\|_2^2\le\sum_{m,n\in\mathbb Z}|\langle f,M_{mb}T_{na}g_\gamma\rangle|^2\le B\|f\|_2^2\) for every \(f\in L^2(\mathbb R)\). These are operator eigenvalue extrema, not the square roots of the bounds. Exactly \(ab=2/3\) is considered; no general rational-density formula is asserted.

## Proof
**Fiberization and normalization.** The unitary dilation \(U_b f(x)=b^{-1/2}f(x/b)\) conjugates the lattice to \(b=1\), \(a=2/3\), and decay \(\eta=\gamma/b\), without altering frame bounds. Parseval's formula for the modulations \(e^{2\pi imx}\) splits \(L^2(\mathbb R)\) over \(x\in[0,1)\) into sequences \((f(x+k))_{k\in\mathbb Z}\). Sorting translations as \(n=3j+r\), \(r=0,1,2\), and sequence indices as \(k=2\ell+s\), \(s=0,1\), then applying the Fourier series transform in \(\ell\), identifies the frame operator with a positive \(2\times2\) matrix \(S(x,\xi)\). Translation covariance by \(2/3\) makes the matrix eigenvalues periodic under \(x\mapsto x+1/3\) (the matrices are unitarily conjugate, with a possible Fourier gauge). It suffices to consider \(0<x<1/3\).

Put \(t=e^{-\eta/3}\), \(u=t^2\), \(z=e^{-2\pi i\xi}\), and
\[
v_0=(1,t^3)^\mathsf T,\qquad v_1=(t^4z,t)^\mathsf T.
\]
Summing the absolutely convergent geometric Fourier series for the three translated residues gives **exactly**
\[
S(x,\xi)=\frac{2\eta e^{-2\eta x}}{|1-t^6z|^2}\bigl((1+t^4)v_0v_0^*+v_1v_1^*\bigr).
\]
Here \(v^*\) is conjugate transpose. Consequently the bracketed matrix has trace \(T=\sum_{j=0}^5u^j\) and determinant \(u(1+u^2)|1-u^3z|^2\). For \(y=|1-u^3z|^2\), its two eigenvalues are
\[
\lambda_\pm(x,y)=\frac{\eta e^{-2\eta x}}{y}\left(T\pm\sqrt{T^2-4u(1+u^2)y}\right).
\]
Positive definiteness follows from the nonzero determinant, and the discriminant is nonnegative since it comes from a Hermitian Gram matrix.

**Exact extrema.** For fixed \(x\), \(\lambda_+\) is strictly decreasing in \(y\), whereas \(\lambda_-\) is strictly increasing in \(y\): for the latter, rationalize it as \(4\eta e^{-2\eta x}u(1+u^2)/(T+\sqrt{T^2-4u(1+u^2)y})\). Since \((1-u^3)^2\le y\le(1+u^3)^2\), the largest and smallest eigenvalues both occur at \(\xi=0\). The common factor \(e^{-2\eta x}\) then places the essential maximum at \(x\downarrow0\) and the essential minimum at \(x\uparrow1/3\). Simplifying their eigenvalue formulas yields the claimed \(B\) and \(A\). The endpoint limits are sharp essential extrema because every neighborhood of either endpoint has positive measure. This also proves the asserted frame property, since \(A>0\) and \(B<\infty\).

**Unique global optimizer.** Differentiation of \(K=(1+q)/(u(1-q))\), with \(E=-uh'/h\), gives
\[
\frac{d}{du}\log K=\frac{E-q}{uq}.
\]
An exact polynomial identity is
\[
E^2-(1-h)=-\frac{4u^2\left(u^8-3u^6-12u^4-3u^2+1\right)}{(u-1)^2(u+1)^2(u^2+1)^2(u^2-u+1)^2}.
\]
Thus any critical point must solve \(u^8-3u^6-12u^4-3u^2+1=0\). Setting \(v=u^2\), division by \(v^2\) reduces this equation to \(s^2-3s-14=0\) for \(s=v+v^{-1}>2\). Precisely one such \(s\) exists, namely \(s_*\), and precisely one \(v\in(0,1)\) corresponds to it, namely \(v_*\). On the other hand, \(K(u)\to\infty\) as \(u\downarrow0\) and as \(u\uparrow1\), so a global minimum exists at an interior critical point. Since there can be at most one, that point is the unique global minimizer. The formulas for \(a_*\) and \(b_*\) follow from \(ab=2/3\) and \(\eta=\gamma/b\).

## Verification
The standalone `check_gabor.py` uses exact symbolic simplification to verify the fiber trace/determinant and the critical polynomial identity. It independently recomputes fibers by direct geometric Fourier sums across all three \(x\)-intervals, samples spectrum and extremal limits, and compares the analytic minimum to a dense parameter grid. Run `python -m pip install -r requirements.txt` and `python check_gabor.py` from the extracted package directory. These finite checks supplement the proof, rather than establishing any universal bound by enumeration.

## Relationship to prior work
Janssen's 1995 rational-density Zibulski–Zeevi theory gives the general finite-matrix framework, and Janssen's 1996 frame-bound calculations address one-sided exponentials at **integer** oversampling. Faulhuber and Shafkulovska (first public 2022-04-06) explicitly analyze optimal one-sided exponential frame bounds and conditioning at **integer** oversampling, including a unique optimizer depending on that integer; their Theorem 2.6 does not state the noninteger-density \(3/2\) formula here. The finding supplies a noninteger rational oversampling instance in this line, with explicit two-dimensional fiber extrema and a radical solution for the optimal aspect ratio. General Gabor-frame criteria and totally positive-window frame-set results imply existence but not this exact quantitative formula. The literature comparison is evidence of a gap, not a claim of exhaustive historical priority.

## Limitations
The result treats the one-sided exponential only, fixed density \(3/2\), and exact idealized frame measurements. It does not cover general noninteger rational densities, arbitrary windows, other lattice shapes, or noisy frame estimation. An uncatalogued explicit computation from the general rational fiber formula could cover this particular special case. Independent mathematical validation has not been performed.

## References
1. M. Faulhuber and I. Shafkulovska, *Gabor frame bound optimizations*, arXiv:2204.02917, first public 2022-04-06, Theorem 2.6 and §7. https://arxiv.org/abs/2204.02917 ; https://arxiv.org/pdf/2204.02917
2. A. J. E. M. Janssen, *Some Weyl–Heisenberg frame bound calculations*, 1996, §4, https://nuhagphp.univie.ac.at/janssen/data/p071.pdf
3. A. J. E. M. Janssen, *On rationally oversampled Weyl–Heisenberg frames*, Signal Processing 47 (1995), 239–245, https://nuhagphp.univie.ac.at/janssen/data/p074.pdf
4. H. Bölcskei and A. J. E. M. Janssen, *Gabor frames, unimodularity, and window decay*, J. Fourier Anal. Appl. 6 (2000), 255–276, https://doi.org/10.1007/BF02511155
5. K. Gröchenig, J. L. Romero, and J. Stöckler, *Sampling theorems for shift-invariant spaces, Gabor frames, and totally positive functions*, Invent. Math., https://doi.org/10.1007/s00222-017-0760-2
