# Countable Fredholm circles and a dimension-dependent index staircase for coordinate Cesàro operators

## Finding

Let \(d\ge 2\) be an integer and let \(C_j\), \(1\le j\le d\), be Pilla's coordinate Cesàro operator on the Drury–Arveson Hilbert space \(H_d^2(\mathbb B_d)\). For every integer \(r\ge0\), put
\[
\Delta_r=\left\{\lambda\in\mathbb C:\left|\lambda-\frac1{r+1}\right|\le\frac1{r+1}\right\},
\qquad \Gamma_r=\partial\Delta_r.
\]
The **Fredholm essential spectrum** (failure-of-Fredholm spectrum) of each coordinate operator is precisely
\[
\boxed{\sigma_{\mathrm F}(C_j)=\bigcup_{r=0}^{\infty}\Gamma_r.}
\]
This countable union is closed: its only possible new accumulation point is \(0\), which lies on every circle. The ordinary spectrum is the filled disk \(\sigma(C_j)=\Delta_0\), and the point spectrum is empty.

For \(\lambda\ne0\), define \(t(\lambda)=2\operatorname{Re}\lambda/|\lambda|^2\). If \(\lambda\notin\bigcup_r\Gamma_r\), put \(k(\lambda)=\max\{0,\lfloor t(\lambda)\rfloor\}\). (If \(t(\lambda)\) is a positive integer, then \(\lambda\) lies on a circle and this definition is not used.) Then
\[
\boxed{\operatorname{ind}(C_j-\lambda I)=
\begin{cases}
0,&k(\lambda)=0,\\
-\displaystyle\binom{k(\lambda)+d-2}{d-1},&k(\lambda)\ge1.
\end{cases}}
\]
In each such Fredholm region, \(\ker(C_j-\lambda I)=\{0\}\) and the cokernel has dimension \(-\operatorname{ind}(C_j-\lambda I)\). Along positive real \(x\downarrow0\) avoiding the circle intersections,
\[
\left|\operatorname{ind}(C_j-xI)\right|\sim\frac{(2/x)^{d-1}}{(d-1)!}.
\]
Thus the Fredholm index records the ambient complex dimension even though the ordinary spectrum is independent of \(d\). No claim is made about a joint spectrum of the noncommuting coordinate tuple.

## Assumptions and scope

The Drury–Arveson norm is defined by
\[
\left\|\sum_{\alpha\in\mathbb N_0^d}a_\alpha z^\alpha\right\|_{H_d^2}^2
=\sum_\alpha |a_\alpha|^2\frac{\alpha!}{|\alpha|!}.
\]
The bounded operator \(C_j\) is the closure of the monomial action
\[
C_jz^\alpha=\sum_{h=0}^\infty\frac{z^{\alpha+h e_j}}{|\alpha|+h+1};
\]
it is equivalently \((C_jf)(z)=\int_0^1 f(tz)/(1-tz_j)\,dt\). The scalar field is complex; \(d\) is finite; there is no compactness assumption on \(C_j\). Fredholm means closed range with finite kernel and cokernel, and index is kernel dimension minus cokernel dimension.

## Proof

**1. Exact weighted-Bergman reduction.** Fix \(j\) and a transverse multi-index \(\beta\in\mathbb N_0^{d-1}\) of degree \(r=|\beta|\). The mutually orthogonal spaces
\[
M_\beta=\overline{\operatorname{span}}\{z^\beta z_j^n:n\ge0\}
\]
reduce \(C_j\), and their orthogonal sum is all of \(H_d^2\). In \(M_\beta\), the norm of the \(n\)-th monomial has square \(n!\beta!/(n+r)!\). Up to the constant factor \(\beta!/r!\), these are the squared moments \(n!r!/(n+r)!\) of the normalized one-variable weighted Bergman space \(A^2_{r-1}\) when \(r\ge1\); for \(r=0\), these are the Hardy \(H^2\) moments. Under the resulting unitary equivalence, the restricted operator is
\[
(G_rf)(z)=z^{-(r+1)}\int_0^z\frac{t^r f(t)}{1-t}\,dt,
\qquad
[z^n]G_rf=\frac1{n+r+1}\sum_{h=0}^n[z^h]f.
\]
There are exactly \(m_r=\binom{r+d-2}{d-2}\) transverse indices of degree \(r\). Therefore
\[
C_j\cong\bigoplus_{r=0}^\infty G_r^{\oplus m_r}.
\tag{1}
\]
The classical weighted-Bergman theorem (Miller, cited below) supplies, for \(r\ge1\), \(\sigma(G_r)=\Delta_r\), \(\sigma_{\mathrm F}(G_r)=\Gamma_r\), emptiness of the point spectrum, and subnormality. The Hardy case \(r=0\) is the classical Cesàro theorem. Subnormality gives \(\|G_r\|=\max_{\lambda\in\Delta_r}|\lambda|=2/(r+1)\). In particular \(\|G_r\|\to0\), an important uniform fact for the direct sum. The one-variable spectral and subnormality results are inputs, not claimed as new.

**2. One-block Fredholm defect.** Every \(G_r-\lambda I\) is injective. Indeed, if an eigenfunction has a first nonzero Taylor coefficient of degree \(n_0\), the triangular recurrence forces \(\lambda=(r+n_0+1)^{-1}\) and, for \(n>n_0\),
\[
a_n=\frac{n+r}{n-n_0}a_{n-1};
\qquad a_n=a_{n_0}\binom{n+r}{n-n_0}.
\]
The weighted squared-coefficient terms then grow on the order of \(n^{r+2n_0}\), so the function is not in \(A^2_{r-1}\) or \(H^2\). Zero cannot be an eigenvalue because the triangular map has an algebraic left inverse on formal series.

For a nonzero \(\lambda\), write \(w_n=n!r!/(n+r)!\) and use the normalized monomials \(e_n=z^n/\sqrt{w_n}\). An adjoint eigenvector \(g=\sum g_ne_n\), satisfying \(G_r^*g=\overline\lambda g\), must obey
\[
\sqrt{w_{n+1}}g_{n+1}=
\left(1-\frac1{\overline\lambda(n+r+1)}\right)\sqrt{w_n}g_n.
\tag{2}
\]
This leaves at most one free scalar. Away from the values at which a factor vanishes, the resulting squared coefficients decay like \(n^{r-2\operatorname{Re}(1/\lambda)}\). The same condition holds for finite-support solutions when a factor vanishes. Hence
\[
\dim\ker(G_r^*-\overline\lambda I)=
\begin{cases}
1,&\operatorname{Re}(1/\lambda)>(r+1)/2,\\
0,&\operatorname{Re}(1/\lambda)\le(r+1)/2.
\end{cases}
\]
The strict inequality is exactly \(\lambda\in\operatorname{int}\Delta_r\). The weighted-Bergman Fredholm theorem says precisely that \(G_r-\lambda I\) has closed range off \(\Gamma_r\). Thus the defect calculation shows its index is \(-1\) throughout the open disk and \(0\) outside the closed disk.

**3. Passage to the infinite direct sum.** For fixed \(\lambda\ne0\), since \(\|G_r\|\to0\), every sufficiently large \(G_r-\lambda I\) is invertible with \(\|(G_r-\lambda I)^{-1}\|\le(|\lambda|-\|G_r\|)^{-1}\), uniformly on the tail. Therefore (1) is Fredholm exactly when all finitely many remaining block summands are Fredholm. It fails at a point of any \(\Gamma_r\), while \(0\) fails because it belongs to every \(\Gamma_r\). This proves the circle formula, including boundary and accumulation points.

**4. Index counting.** For \(\lambda\ne0\), the condition \(\lambda\in\operatorname{int}\Delta_r\) is equivalent to
\[
r+1<\frac{2\operatorname{Re}\lambda}{|\lambda|^2}=t(\lambda).
\]
Off the circles the eligible degrees are exactly \(r=0,\ldots,k-1\), with \(k=\max\{0,\lfloor t\rfloor\}\). Each such block contributes \(-1\) and occurs \(m_r\) times. The hockey-stick identity gives
\[
-\sum_{r=0}^{k-1}\binom{r+d-2}{d-2}=-\binom{k+d-2}{d-1},
\]
with empty sum zero. The final asymptotic uses \(k(x)=\lfloor2/x\rfloor\sim2/x\) off the circles and fixed dimension \(d\). Injectivity of the total direct sum follows from injectivity on every block.

## Verification

The accompanying standalone `verification.py` checks exact factorial moments, transverse multiplicities, finite-dimensional triangular coefficients, and sample integer-index regions using rational arithmetic. The recorded execution passed 17796 finite checks. The source theorems about infinite weighted-Bergman spectra/Fredholmness and the arguments above—not the finite checker—justify the infinite-dimensional claims.

## Relationship to prior work

Pilla (2026, arXiv:2606.24710, §§2–3.6) defines the coordinate operators and proves boundedness, ordinary disk spectrum, noncompactness, and the monomial-slice decomposition. Miller's 2011 weighted-Bergman lecture, theorem displayed on slide 9 (zero-indexed page 8), states the one-variable essential circle, ordinary disk, and subnormality of the specifically parameterized generalized Cesàro operators. The Hardy \(r=0\) case goes back to classical Cesàro theory. Young (2004) and further general weighted-Bergman work give complementary one-variable Fredholm and spectral context. The present claim is the **global multivariable Fredholm classification** for Pilla's coordinate operator: a countable closed set of nested tangent circles and its exact dimension-sensitive binomial index staircase. Neither the base multivariable result nor the cited one-variable theorem states that full global classification.

## Limitations

This is a statement about each coordinate operator separately, not about a joint Fredholm spectrum of the noncommuting tuple. It uses established one-variable Fredholm and subnormality results rather than reproving them. The case of an infinite number of variables, other multivariable Cesàro constructions, and the behavior under general perturbations are not covered. The search of available literature cannot exclude a previously published equivalent formulation under a different construction; independent validation has not been performed.

## References

1. Michael R. Pilla, *Cesàro-Type Operators Acting on the Drury-Arveson Space*, arXiv:2606.24710, first submitted 2026-06-23. https://arxiv.org/abs/2606.24710
2. Len Miller, *Spectral properties of operators associated with the Cesàro operator on weighted Bergman spaces*, SEAM 27 lecture slides, March 18, 2011; theorem on slide 9. https://people.clas.ufl.edu/sam/files/miller.pdf
3. Scott W. Young, *Generalized Cesàro operators and the Bergman space*, Journal of Operator Theory **52** (2004), 341–351.
4. Michael R. Pilla, *Rhaly-Type Operators in Several Complex Variables*, arXiv:2606.25885, first submitted 2026-06-24. https://arxiv.org/abs/2606.25885
