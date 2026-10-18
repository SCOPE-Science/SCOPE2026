# A hyperelliptic proof of the ED-degree formula for one-block rank-two Schubert varieties

## Finding
For every integer \(m\geq2\), put \(n=m+2\) and fix an orthogonal decomposition \(\mathbb C^n=E\oplus W\), where \(\dim E=m\) and \(\dim W=2\). Consider the Schubert variety
\[
X_m=\{U\in\operatorname{Gr}(2,n):\dim(U\cap W)\geq1\}.
\]
Realize its nondegenerate planes by their symmetric orthogonal-projector matrices \(P_U\), and take the Zariski closure in the affine projection Grassmannian. Its Euclidean distance degree, counting critical points on the smooth locus for a generic symmetric data matrix, is
\[
\boxed{\operatorname{EDdeg}(X_m)=6m-2=6n-14.}
\]
Equivalently, the rank-two loopless matroid variety whose parallel classes have sizes \((m,1,1)\), or the rank-two Schubert variety \(\mathcal S_{1,n-1}\), has this exact ED degree. This proves the \(j=n-1\), \(i=1\) infinite family of Conjecture 6.5 of Friedman–Rosana–Sturmfels (2026), rather than proposing the already conjectured numerical formula as new.

## Assumptions and scope
The base field is \(\mathbb C\), with its standard non-Hermitian symmetric bilinear form \(\langle u,v\rangle=u^{\mathsf T}v\). The ambient affine Grassmannian consists of symmetric rank-two idempotent matrices of trace two. A plane is represented there precisely when restriction of this bilinear form to the plane is nondegenerate. For \(Q\in\operatorname{Sym}_n(\mathbb C)\), the squared Frobenius-distance critical locus agrees with the critical locus of \(U\mapsto\operatorname{tr}(QP_U)\), since \(P_U^2=P_U\) and \(\operatorname{tr}(P_U)=2\). Here ED degree counts isolated complex critical points on the smooth locus for \(Q\) in a Zariski-open dense subset; it does not assert a count for every data matrix or the number of real critical points. The origin of the Schubert variety \(X_m\) in the projection model is the rank-two matroid family \((m,1,1)\); the point \(U=W\) is its exceptional singular point for \(m\geq2\).

## Proof
### 1. Reduction to a spectral curve
Write the symmetric data matrix in blocks
\[
Q=\begin{pmatrix}A&b_1&b_2\\b_1^{\mathsf T}&c_{11}&c_{12}\\b_2^{\mathsf T}&c_{12}&c_{22}\end{pmatrix},
\qquad A\in\operatorname{Sym}_m(\mathbb C),\quad b_1,b_2\in\mathbb C^m.
\]
A nonexceptional plane \(U\in X_m\), with \(U\ne W\), uniquely determines its line \(L=U\cap W\). Outside the two isotropic lines of \(W\), choose \(q=(1,t)\in W\), \(e=(-t,1)\in W\), and put \(\tau=1+t^2\). Any nondegenerate such \(U\) splits orthogonally as \(L\oplus\langle v\rangle\), with \(v\in E\oplus\mathbb C e\) nonisotropic. On the fibre over \(t\), the objective is the sum of the quotient of \(Q\) on \(q\) and the Rayleigh quotient of \(Q\) restricted to \(E\oplus\mathbb C e\). The latter's complex critical lines are the nonisotropic eigenlines of the restriction; the eigenvalue is \(\mu\). Consequently the critical-value curve over the line parameter is
\[
G(t,\mu)=\bigl(f(t)-\tau\mu\bigr)D(\mu)
-b(t)^{\mathsf T}\operatorname{adj}(A-\mu I)b(t)=0,
\]
where
\[
D(\mu)=\det(A-\mu I),\quad f(t)=c_{11}t^2-2c_{12}t+c_{22},\quad b(t)=b_2-tb_1.
\]
This follows by expanding the characteristic determinant of the \((m+1)\)-dimensional restriction, after multiplying by \(\tau\). Let \(S_Q\) be the projective closure of \(G=0\) in \(\mathbb P^1_t\times\mathbb P^1_\mu\). Its bidegree is \((2,m+1)\), and its meromorphic critical-value function is
\[
h(t,\mu)=\mu+\alpha(t),\qquad
\alpha(t)=\frac{c_{11}+2c_{12}t+c_{22}t^2}{1+t^2}.
\]
At points corresponding to simple, nonisotropic restricted eigenlines with \(\tau\ne0\), the differential of the objective vanishes exactly when \(dh=0\) on \(S_Q\): the fibre derivative vanishes by the eigenvector equation, and the remaining derivative is the derivative of the critical value. Thus these two critical problems have the same points on their common open set.

### 2. Smoothness and genus, for general data
Smoothness of \(S_Q\) is a nonempty Zariski-open condition on \(Q\). To exhibit nonemptiness, take \(A=\operatorname{diag}(\lambda_1,\ldots,\lambda_m)\) with pairwise distinct real numbers, \(b_1=0\), \(b_2=b\) with every entry of \(b\) nonzero, and \(c_{12}=0\). Let
\[
B=\begin{pmatrix}A&b\\b^{\mathsf T}&c_{22}\end{pmatrix}.
\]
The equation is exactly
\[
(c_{11}-\mu)D(\mu)t^2+\det(B-\mu I)=0.
\]
For real \(b\), the symmetric arrowhead matrix \(B\) has \(m+1\) distinct real eigenvalues, none equal to any \(\lambda_j\): interlacing follows from its secular equation, whose derivative is strictly nonzero between the \(\lambda_j\). Choose \(c_{11}\) outside this finite spectrum and the \(\lambda_j\). Then projection to \(\mathbb P^1_\mu\) exhibits \(S_Q\) as a connected smooth double cover branched simply at the \(2m+2\) distinct roots of \((c_{11}-\mu)D(\mu)\det(B-\mu I)\). There is no branch at infinity because both numerator and denominator have degree \(m+1\). Thus \(S_Q\) is smooth and, by Riemann–Hurwitz, has genus \(m\). This also follows by adjunction for a smooth curve of bidegree \((2,m+1)\). In particular a generic \(Q\) gives such a smooth connected curve.

### 3. Exact degree of the critical-value map
The two isotropic line parameters are \(t=\pm i\). At either, the polynomial \(G(t,\mu)\) has degree \(m\) in finite \(\mu\), and has \(m\) distinct finite roots for generic data. To see nonemptiness of the simple-root condition, for the preceding real arrowhead choice take \(c_{22}-c_{11}>0\); then the root equation is
\[
(c_{22}-c_{11})-\sum_{j=1}^m\frac{b_j^2}{\lambda_j-\mu}=0,
\]
which has \(m\) distinct simple real roots by strict monotonicity on intervals between its poles (counting the outside interval as appropriate). At each finite root, \(h=\mu+\alpha(t)\) has a simple pole, because \(\alpha\) has a simple pole and \(\mu\) is finite. At each of the two remaining points over \(t=\pm i\), one has \(\mu=\infty\); the defining equation gives
\[
\mu=\frac{f(t)}{1+t^2}+O(1),\qquad
f(t)+c_{11}+2c_{12}t+c_{22}t^2=(c_{11}+c_{22})(1+t^2).
\]
It follows that \(h\) is finite there, with the leading poles cancelling. There are no other poles (the only possible infinite eigenvalues occur above \(t=\pm i\)). Hence the rational map \(h:S_Q\to\mathbb P^1\) has degree exactly \(2m\).

The total ramification degree is therefore
\[
2g(S_Q)-2+2\deg h=2m-2+4m=6m-2.
\]

### 4. None of the generic ramification is lost at the boundary
A simple pole of \(h\) is unramified. At the two \(\mu=\infty\) points, nonramification is a nonempty open condition, verifiable explicitly. Put \(\beta_0(t)=b(t)^{\mathsf T}b(t)\), \(\beta_1(t)=b(t)^{\mathsf T}A b(t)\). Expanding the defining equation for large \(\mu\) at \(\tau=0\) gives
\[
h=c_{11}+c_{22}+\frac{\beta_0}{f}
+\tau\left(\frac{\beta_1}{f^2}-\frac{\beta_0^2}{f^3}\right)+O(\tau^2).
\]
For example, choose \(A=\operatorname{diag}(0,\ldots,m-1)\), \(b_1=0\), \(b_2=(1,\ldots,1)^{\mathsf T}\), \(c_{11}=-3\), \(c_{12}=0\), \(c_{22}=m+4\). At \(t=i\) the first derivative of \(h\) along \(S_Q\) is
\[
\left.\frac{dh}{dt}\right|_{t=i,\mu=\infty}
=\frac{i m(m^2+10m+35)}{(m+7)^3}\ne0;
\]
its conjugate negative occurs at \(t=-i\). Thus generic data have no ramification at either excluded corner.

For nonisotropic \(q\), a simple eigenvalue of a complex symmetric restriction has a nonisotropic eigenvector. At any smooth spectral point with \(\partial G/\partial\mu=0\) and \(\tau\ne0\), one necessarily has \(\partial G/\partial t\ne0\). Therefore \(\mu\) itself is a local coordinate and \(dt/d\mu=0\); hence \(dh/d\mu=1\), so no defective-eigenvalue spectral point contributes ramification. This argument needs only spectral smoothness, not a restriction to simple folds. If \(b_1,b_2\) are linearly independent (possible since \(m\ge2\)), no restricted eigenline supported in \(W\) can occur, so no spectral critical point maps to the singular plane \(U=W\). Finally, standard generic linear-Morse transversality on the smooth embedded projector variety ensures all retained critical points are simple and none lie on its fixed isotropic-line boundary. These conditions define a nonempty Zariski-open set (the explicit smoothness and corner checks give the only possible boundary corrections). Therefore all \(6m-2\) ramification points count exactly once as genuine smooth-locus ED critical points. This proves the formula.

## Verification
The standalone exact-arithmetic program `check_spectral.py` tests the auxiliary spectral construction for \(m=2,3,4,5,6,7\). It constructs the explicit arrowhead specialization, checks distinctness of the \(2m+2\) hyperelliptic branch points algebraically by polynomial gcd, confirms the \(m\) simple poles at each isotropic parameter by squarefreeness, evaluates the nonzero corner-slope expression, and recovers \(6m-2\) from Riemann–Hurwitz. Its outputs for \(m=2,3,4\) are \(10,16,22\), matching independently published numerical tables. The program verifies finite specializations; the general proof is the argument above.

## Relationship to prior work
Friedman–Rosana–Sturmfels, *Distance Optimization in the Grassmannian of Lines* (arXiv:2601.22843v1, January 30, 2026), Conjecture 6.5, already predicts the general formula \(2(n-j+1)^2(j-i)-(n-j+1)(n-i)\). Specializing \((i,j)=(1,n-1)\) gives precisely \(6n-14\). That **prediction and its finite numerical tests are prior work**, not claimed as new. The present finding supplies a proof for this infinite non-product Schubert subfamily. Friedman–Hoşten–Rosana, *Euclidean Distance Optimization Within the Grassmannian* (arXiv:2610.02018v1, October 1, 2026), Table 1, numerically lists the cases \(m=2,3,4\) with ED degrees \(10,16,22\), and its §7 proves corresponding GD-degree results but does not establish this ED formula in arbitrary dimension. Lai–Lim–Ye, *Euclidean distance degree in manifold optimization* (arXiv:2502.10336, 2025), Corollary 4.5, treats a different product-like Schubert family and does not imply the present singular incidence Schubert formula.

## Limitations
The theorem proves one infinite one-block, two-singleton subfamily, not the full two-parameter Schubert Conjecture 6.5. It assumes generic symmetric complex data. The spectral covering and pole analysis require the specified projection-model embedding, not arbitrary Plücker or other Euclidean embeddings; counts of real critical points are not classified. The prior numerical prediction is acknowledged; an undiscovered independent proof of this special case cannot be excluded by finite literature searches.

## References
1. H. Friedman, A. Rosana, B. Sturmfels, *Distance Optimization in the Grassmannian of Lines*, arXiv:2601.22843v1 (2026), §6, Conjecture 6.5; https://arxiv.org/pdf/2601.22843.
2. H. Friedman, S. Hoşten, A. Rosana, *Euclidean Distance Optimization Within the Grassmannian*, arXiv:2610.02018v1 (2026), §§6–7, Table 1; https://arxiv.org/html/2610.02018v1.
3. Z. Lai, L.-H. Lim, K. Ye, *Euclidean distance degree in manifold optimization*, arXiv:2502.10336 (2025), Corollary 4.5; https://arxiv.org/pdf/2502.10336.
4. Classical Riemann–Hurwitz, adjunction on \(\mathbb P^1\times\mathbb P^1\), and generic linear-Morse transversality (used with hypotheses specified above).
