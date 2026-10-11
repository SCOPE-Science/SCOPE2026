# Hilbert–Schmidt Copson model and Fredholm circle at the logarithmic Hilbert-matrix endpoint

## Finding
For integers \(n,m\ge2\), put \(v_m=(\log m)^2/m\) and \(w_n=1/n\). The classical Hilbert matrix \(H:\ell_v^2\to\ell_w^2\),
\[
(Ha)_n=\sum_{m=2}^{\infty}\frac{a_m}{n+m+1},
\]
is bounded. Its **exact essential norm** is \(2\), with the given norms and weights. The natural diagonal normalization, an operator \(T\) on \(\ell^2(\{2,3,\ldots\})\) with matrix
\[
T_{nm}=\frac{\sqrt{m/n}}{(n+m+1)\log m},
\]
has Fredholm essential spectrum and index
\[
\sigma_{\mathrm{ess},F}(T)=\{\lambda\in\mathbb C:|\lambda-1|=1\},\qquad
\operatorname{ind}(T-\lambda I)=
\begin{cases}1,&|\lambda-1|<1,\\0,&|\lambda-1|>1.\end{cases}
\]
The circle passes through \(0\). All Fredholm assertions concern **this normalized endomorphism**; the raw map between distinct weighted Hilbert spaces has no intrinsic Fredholm spectrum.

More strongly, with an explicit isometry onto a step subspace, the direct extension of \(T\) by zero is a **Hilbert–Schmidt perturbation** of the continuous Copson operator. This structural identification supplies the exact Calkin invariants.

## Assumptions and scope
The scalar field is \(\mathbb C\). The weighted norms are \(\|a\|_{\ell_v^2}^2=\sum_{m\ge2}v_m|a_m|^2\) and \(\|b\|_{\ell_w^2}^2=\sum_{n\ge2}w_n|b_n|^2\). The diagonal isometries are \((D_va)_m=\sqrt{v_m}a_m\) and \((D_wb)_n=\sqrt{w_n}b_n\), and \(T=D_wHD_v^{-1}\). Essential norm means distance to compact operators; Fredholm essential spectrum means the set where \(T-\lambda I\) is not Fredholm, with index \(\dim\ker-\dim\operatorname{coker}\).

Let \(I_n=[\log n,\log(n+1))\), \(h_n=|I_n|=\log(1+1/n)\), \(\phi_n=h_n^{-1/2}\mathbf 1_{I_n}\), and \(\mathcal H=L^2([\log2,\infty),ds)\). Write \(J:\ell^2\to\mathcal H\) for the isometry \(Je_n=\phi_n\) and \(P=JJ^*\) for the orthogonal projection onto the step subspace. Consider \((Af)(s)=\int_s^{\infty}f(t)\,dt/t\).

## Proof
**1. Hilbert–Schmidt reduction from the Hilbert matrix to a triangular matrix.** Set
\[
L_{nm}=\frac{\mathbf1_{\{m>n\}}}{\sqrt{nm}\log m}.
\]
For \(m\le n\),
\[
|T_{nm}-L_{nm}|^2=\frac{m}{n(n+m+1)^2(\log m)^2}.
\]
For \(m>n\), direct subtraction gives
\[
|T_{nm}-L_{nm}|^2=\frac{(n+1)^2}{nm(n+m+1)^2(\log m)^2}.
\]
For each \(m\ge2\), summing the first expression over \(n\ge m\) and the second over \(2\le n<m\) gives at most \(C/[m(\log m)^2]\), where \(C\) is an absolute finite constant. Since \(\sum_{m\ge2}1/[m(\log m)^2]<\infty\), the matrix \(T-L\) is Hilbert–Schmidt. The boundedness of \(T\) will follow from the model below.

**2. Exact continuous model modulo Hilbert–Schmidt operators.** For \(m>n\), a direct scalar-product calculation gives
\[
\langle A\phi_m,\phi_n\rangle
=\sqrt{\frac{h_n}{h_m}}\int_{\log m}^{\log(m+1)}\frac{dt}{t}.
\]
Because \(h_k=k^{-1}(1+O(k^{-1}))\) and \(1/t=(\log m)^{-1}(1+O(m^{-1}))\) uniformly on \(I_m\), this matrix entry differs from \(L_{nm}\) by at most
\[
\frac{C}{\sqrt{nm}\log m}\left(\frac1n+\frac1m\right).
\]
The square sum over \(m>n\ge2\) is finite: bound it by
\[
C\sum_{m\ge3}\frac{1}{m(\log m)^2}
\sum_{n=2}^{m-1}\frac1n\left(\frac1n+\frac1m\right)^2<\infty.
\]
For \(m=n\), the entry is bounded by \(h_n/(2\log n)\), whose squares are summable; for \(m<n\), it is zero. Thus \(L-J^*AJ\) is Hilbert–Schmidt.

It remains to compare the full integral operator with its compression. Its kernel is \(k(s,t)=\mathbf1_{\{t>s\}}/t\). The kernel of \(PAP\) is the average of \(k\) over each rectangle \(I_n\times I_m\). On rectangles \(m<n\), both vanish. On \(m>n\), \(k=1/t\), with oscillation at most \(Ch_m/(\log m)^2\) as \(t\) varies in \(I_m\); hence the squared integral of the error on such a rectangle is bounded by \(Ch_nh_m^3/(\log m)^4\). Since \(\sum_{n<m}h_n\le\log m\) and \(h_m\le1/m\), the sum of these bounds is finite. On diagonal rectangles the squared error is bounded by \(Ch_n^2/(\log n)^2\), also summable. Consequently \(A-PAP\) is Hilbert–Schmidt. Combined with the preceding matrix estimates, this proves
\[
A-JTJ^*\in\mathcal S_2(\mathcal H).
\]
Here \(JTJ^*\) is \(T\) on \(P\mathcal H\) and zero on its infinite-dimensional orthogonal complement. In particular, \(A\) and \(T\) are bounded.

**3. Norm and essential norm.** The unitary change of variables
\[
(Uf)(x)=e^{x/2}f(e^x),\qquad x\ge\log(\log2),
\]
transforms \(A\) into
\[
(Bg)(x)=\int_x^\infty e^{-(y-x)/2}g(y)\,dy.
\]
The nonnegative convolution kernel has \(L^1\)-mass \(2\), so \(\|B\|\le2\). If \(g_{R,L}=L^{-1/2}\mathbf1_{[R,R+L]}\) with \(R,L\to\infty\), then \(g_{R,L}\rightharpoonup0\), \(\|g_{R,L}\|_2=1\), and \(\|(B-2I)g_{R,L}\|_2\to0\) (only bounded-length boundary layers contribute). Compact operators send this weakly null sequence to norm-null sequences; hence \(\|B\|_{\rm ess}\ge2\). Therefore \(\|A\|_{\rm ess}=2\). Hilbert–Schmidt perturbation and the orthogonal direct sum with zero preserve essential norms, giving \(\|T\|_{\rm ess}=2\), as asserted for \(H\) under its two weighted norms.

**4. Fredholm index and essential boundary.** Fix \(\lambda\ne0\) and put \(a_\lambda=\lambda^{-1}-1/2\). If \((B-\lambda I)g=h\) and \(u=Bg\), then \(u'=u/2-g\), and the equation is equivalent to
\[
u'+a_\lambda u=h/\lambda.
\]
Conversely, every \(L^2\) solution \(u\) of this equation with \(u'\in L^2\), and \(g=(u-h)/\lambda\), satisfies \(u=Bg\): the only possible homogeneous difference in \(u'=u/2-g\) is a multiple of \(e^{x/2}\), which is not square-integrable on the half-line.

If \(\operatorname{Re}a_\lambda>0\), the inhomogeneous equation has a one-parameter family of \(L^2\) solutions, by convolution from the finite left endpoint with \(e^{-a_\lambda x}\). It is surjective and has one-dimensional kernel; thus \(\operatorname{ind}(B-\lambda I)=1\). If \(\operatorname{Re}a_\lambda<0\), integrate backward from infinity to obtain a unique \(L^2\) solution and a bounded inverse; the index is \(0\). The first case is exactly \(|\lambda-1|<1\), the second \(|\lambda-1|>1\).

If \(\operatorname{Re}a_\lambda=0\) and \(\lambda\ne0\), write \(\lambda=(1/2-i\xi)^{-1}\) and take normalized long oscillatory packets \(L^{-1/2}e^{i\xi x}\mathbf1_{[R,R+L]}\). These converge weakly to zero while \((B-\lambda I)g\to0\) in norm, so \(B-\lambda I\) is not Fredholm. As \(JTJ^*\) differs compactly from \(A\), its Fredholm behavior agrees. For \(\lambda\ne0\), adding the zero summand on \((P\mathcal H)^\perp\) preserves Fredholmness and index of \(T-\lambda I\).

At the remaining boundary point \(\lambda=0\), the coordinate unit vectors form a weakly null sequence and obey
\[
\|Te_m\|_2^2=\frac{m}{(\log m)^2}
\sum_{n\ge2}\frac{1}{n(n+m+1)^2}
=O\left(\frac{1}{m\log m}\right)\to0.
\]
A Fredholm operator cannot have a weakly null unit sequence mapped to norm zero, by a bounded left inverse modulo compact operators. Thus \(T\) is not Fredholm at \(0\). The circle and both index regions are proved.

## Verification
Every critical estimate is an explicit convergent square sum or a scalar first-order resolvent equation; no finite truncation is used as evidence of an infinite-dimensional assertion. The discrete-to-continuous perturbation is Hilbert–Schmidt, stronger than compact. The weakly null packets certify the essential norm and non-Fredholm circle; the separate coordinate-vector estimate handles \(\lambda=0\), which cannot be inferred from the zero-extended operator alone.

## Relationship to prior work
Norrbo, *The Hilbert matrix operator into the Bergman space* (arXiv:2610.00252v1), establishes the critical bounded map between weighted sequence spaces and the logarithmically weighted Bergman endpoint. In particular, its Theorem 3.4 concerns boundedness, not the exact essential norm or the Fredholm spectrum of the diagonal normalization. Bellavita–Daskalogiannis–Miihkinen–Norrbo–Stylogiannis–Virtanen (arXiv:2407.13569) compute essential norms for generalized Hilbert matrix endomorphisms on standard Bergman spaces; those have a different domain/codomain, and no logarithmic two-weight normalization. Lindström–Miihkinen–Norrbo (arXiv:2201.09591) calculate essential norms on classical analytic function spaces, not this critical coefficient-to-coefficient map. Standard Wiener–Hopf/Copson half-line resolvent theory supplies the *model* spectral circle, whereas the Hilbert–Schmidt identification of the critical discrete matrix with that model is the substantive bridge proved here.

## Limitations
The exact essential-norm value \(2\) is with the **stated coefficient weights**, not the original integral norm of the logarithmically weighted Bergman space, which is only equivalent to a coefficient norm. The Fredholm spectrum requires the **specified diagonal identification** of two different sequence spaces. This result does not determine the ordinary spectrum, singular-value distribution of the Hilbert–Schmidt defect, or a sharp formula for the full operator norm.

## References
1. D. Norrbo, *The Hilbert matrix operator into the Bergman space*, arXiv:2610.00252v1 (first publicly available 2026-09-23). https://arxiv.org/abs/2610.00252
2. C. Bellavita, V. Daskalogiannis, S. Miihkinen, D. Norrbo, G. Stylogiannis, J. A. Virtanen, *Generalized Hilbert matrix operators acting on Bergman spaces*, arXiv:2407.13569v1 (2024). https://arxiv.org/abs/2407.13569
3. M. Lindström, S. Miihkinen, D. Norrbo, *Exact essential norm of generalized Hilbert matrix operators on classical analytic function spaces*, arXiv:2201.09591v1 (2022). https://arxiv.org/abs/2201.09591
