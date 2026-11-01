# Cayley-root zero fibres for ball-fibre Hartogs triangles in every dimension

## Finding

For each integer \(n\ge1\) put
\[
\Omega_n=\{(z,w)\in\mathbb C^n\times\mathbb C:\ \|z\|^2<|w|<1\},
\]
and let \(K_n\) be its unweighted Bergman kernel with ordinary Lebesgue volume. Fix \(0<t<1\), and consider the natural radial-product slice \(w\overline\eta=t\). Define \(s=\langle z,\zeta\rangle\), \(y=s/\sqrt t\), and
\[
q_t=\frac{1-\sqrt t}{1+\sqrt t},\qquad C(y)=\frac{1+y}{1-y},\qquad N=n+1.
\]
The complete set of possible \(y\in\mathbb D\) at zeros \(K_n((z,w),(\zeta,\eta))=0\) on this slice is exactly
\[
\mathcal Z_n(t)=\left\{\frac{\rho_t e^{i\theta_j}-1}{\rho_t e^{i\theta_j}+1}:\ 0\le j<N,\ \cos\theta_j>0\right\},
\quad\rho_t=q_t^{2/N},\quad
\theta_j=\frac{(2j+\varepsilon_n)\pi}{N},\quad
\varepsilon_n=\begin{cases}0&n\text{ even},\\1&n\text{ odd}.\end{cases}
\]
Every displayed root is simple as a root of the scalar kernel on the slice, and every one is attained by actual pairs of points of \(\Omega_n\). The number of distinct zero fibres is independent of \(t\) and equals
\[
\#\mathcal Z_n(t)=
\begin{cases}
1+2\lfloor(n+1)/4\rfloor,&n\text{ even},\\
2\lfloor(n+1)/4\rfloor,&n\text{ odd}.
\end{cases}
\]
In particular, no such zeros exist when \(n=1\), whereas every \(n\ge2\) has zeros on every positive radial-product slice, so \(\Omega_n\) is not a Lu Qi-Keng domain for \(n\ge2\). This is only a statement about the positive-product slice, not a zero-freeness assertion for the full \(n=1\) domain.

For each retained index \(j\), the zero approaches \(-1\) at a dimension-dependent sharp rate:
\[
\lim_{t\uparrow1}\frac{y_j(t)+1}{(1-t)^{2/(n+1)}}
=2^{1-4/(n+1)}e^{i\theta_j}.
\]
For \(n=2\), the unique root is explicitly \(y=-\tanh(\tfrac23\operatorname{artanh}\sqrt t)\).

## Assumptions and scope

The Hermitian scalar product is \(\langle z,\zeta\rangle=\sum_{j=1}^n z_j\overline{\zeta_j}\). Only integer dimensions \(n\ge1\), the exponent \(2\), unweighted Bergman space, and \(t\) real strictly between \(0\) and \(1\) are covered. The domain excludes \(w=0\). The zero-fibre count concerns *distinct values of the invariant scalar* \(y\), not the dimension of the full geometric zero set. The boundary limit is for each fixed dimension and retained root index, not uniformly in \(n\).

## Proof

**1. Norms and kernel series.** For \(\alpha\in\mathbb N^n\), \(\ell=|\alpha|\), and \(\beta\in\mathbb Z\), the monomial \(z^\alpha w^\beta\) belongs to \(A^2(\Omega_n)\) precisely when \(2\beta+\ell+n+2>0\). Integrate first over the complex Euclidean ball of radius \(|w|^{1/2}\), then over \(|w|<1\). The exact squared norm is
\[
\|z^\alpha w^\beta\|_2^2=
\frac{2\pi^{n+1}\alpha!}{(\ell+n)!(2\beta+\ell+n+2)}.
\]
Rotational invariance and completeness of the Laurent monomials in this Reinhardt domain give an orthogonal basis. Set \(m_\ell=\lfloor(\ell+n+1)/2\rfloor\) and \(\delta_\ell=\ell+n+2-2m_\ell\in\{1,2\}\). Summing first over \(\beta\ge-m_\ell\) yields, for \(s=\langle z,\zeta\rangle\) and \(t=w\overline\eta\in(0,1)\),
\[
K_n=\frac1{2\pi^{n+1}(1-t)^2}
\sum_{\ell=0}^\infty \frac{(\ell+n)!}{\ell!}
 s^\ell t^{-m_\ell}\big(\delta_\ell+(2-\delta_\ell)t\big).
\tag{1}
\]
This converges absolutely since \(|s|<\sqrt t\) by the strict ball inequalities.

**2. Parity resummation.** Let \(D=(1-y)^{-N}\) and \(E=(1+y)^{-N}\). The binomial identity \(\sum_{\ell\ge0}(\ell+n)!y^\ell/\ell!=n!(1-y)^{-N}\) shows that the even and odd parts are \(n!(D+E)/2\) and \(n!(D-E)/2\). Substituting into (1), for even \(n=2d\) one obtains the exact formula
\[
K_n=\frac{n!}{4\pi^{n+1}t^d(1-t)^2}
\left[\frac{(1+\sqrt t)^2}{\sqrt t}D-
\frac{(1-\sqrt t)^2}{\sqrt t}E\right].
\tag{2}
\]
For odd \(n=2d+1\),
\[
K_n=\frac{n!}{4\pi^{n+1}t^{d+1}(1-t)^2}
\left[(1+\sqrt t)^2D+(1-\sqrt t)^2E\right].
\tag{3}
\]
All prefactors are nonzero for the stated \(t\). Therefore both cases reduce to the single exact zero equation
\[
\left(\frac{1+y}{1-y}\right)^{n+1}
=(-1)^n\left(\frac{1-\sqrt t}{1+\sqrt t}\right)^2.
\tag{4}
\]

**3. Geometric admissibility and counting.** The Cayley map \(C(y)=(1+y)/(1-y)\) is a biholomorphism from \(\mathbb D\) onto the right half-plane. The \(N\) roots of (4) have common radius \(q_t^{2/N}\) and angles \(\theta_j\); exactly those with positive cosine correspond to \(|y|<1\). Counting evenly spaced angles in the open right semicircle gives \(1+2\lfloor N/4\rfloor\) for odd \(N\) (even \(n\)), and \(2\lfloor N/4\rfloor\) for even \(N\) (odd \(n\)). Nonadmissible roots lie in the left half-plane or on its boundary. All admissible roots are simple because \(C'(y)=2/(1-y)^2\ne0\) and the polynomial \(C^N-(-1)^nq_t^2\) has simple nonzero roots.

Every \(y\in\mathbb D\) is realized: choose \(w=\eta=\sqrt t\), and pick \(z,\zeta\) supported in one coordinate, of norm \(t^{1/4}\sqrt{|y|}\), with relative phase chosen to give \(\langle z,\zeta\rangle=\sqrt t\,y\). Strict admissibility follows from \(|y|<1\). Thus the scalar root list is both necessary and sufficient on actual domain pairs.

**4. Boundary asymptotics.** Since \(q_t\sim(1-t)/4\) as \(t\uparrow1\), we have \(C_j=q_t^{2/N}e^{i\theta_j}\) and \(y_j+1=2C_j/(1+C_j)\); division by \((1-t)^{2/N}\) gives the stated limit. For \(n=2\), \(C=q_t^{2/3}\) is the sole admissible positive real root, and \(y=(C-1)/(C+1)=-\tanh(\tfrac23\operatorname{artanh}\sqrt t)\).

## Verification

The attached standard-library Python program `check_hartogs.py` verifies admissible Laurent indices, the parity decomposition, root counts and numerical kernel cancellations in dimensions \(1\) through \(14\), agreement with independently summed convergent Laurent series in selected dimensions, and the boundary scaling in four dimensions. It completed **12,766 checks**. The proof of the infinite family and the limit is analytical above; numerical tests are corroboration, not a substitute for it.

## Relationship to prior work

Fu, Deng and Cao (arXiv:2203.06938, first submitted 2022-03-14) derive an explicit general Bergman kernel for \(\Omega^{n+1}_k\) and investigate \(L^p\) regularity; the present \(k=2\) theorem starts from the same known kernel family but classifies a geometric zero slice, its dimension-dependent count, and the sharp boundary fan. Edholm's earlier two-dimensional generalised Hartogs-triangle work studies other exponent/zero phenomena for \(n=1\), which is not claimed new here. Park's 3-dimensional Hartogs domains have *nested coordinate inequalities*, rather than the Euclidean ball fibres considered here. Other Hartogs/quotient-domain zero results concern different parameter geometries. Full historical priority is not established by these comparisons.

## Limitations

Only the positive real product \(w\overline\eta=t\), exponent \(k=2\), Euclidean ball fibres, and unweighted Bergman kernels are treated. No assertion is made about the entire zero locus off this slice, about all real/complex \(t\), or uniform dimension limits. The general kernel formula is already known; the claim is the exact scalar zero-fibre classification, not a new general kernel construction. A plausible older Park article was not available in full text, and further indirect coverage through earlier explicit kernel formulas cannot be excluded. No independent validation is claimed.

## References

1. Q. Fu, G.-T. Deng and H. Cao, *\(L^p\) regularity of the Bergman projection on generalizations of the Hartogs triangle in \(\mathbb C^{n+1}\)*, arXiv:2203.06938 (first publicly submitted 2022-03-14), https://arxiv.org/abs/2203.06938.
2. Q. Fu and G.-T. Deng, *\(L^p\) boundedness of the Bergman Projection on generalizations of the Hartogs triangle in \(\mathbb C^{n+1}\)*, arXiv:2204.08715 (2022), https://arxiv.org/abs/2204.08715.
3. L. D. Edholm, *Bergman theory of certain generalized Hartogs triangles*, Pacific J. Math. 284 (2016), 327–343, arXiv:1504.07914.
4. J.-D. Park, *The explicit forms and zeros of the Bergman kernel for 3-dimensional Hartogs triangles*, J. Math. Anal. Appl. 460 (2018), DOI:10.1016/j.jmaa.2017.12.002.
5. J.-D. Park, *The Zeros of the Bergman Kernel for Some Reinhardt Domains*, Journal of Function Spaces 2016, article 3856096, DOI:10.1155/2016/3856096 (different Cartan–Hartogs domain).
