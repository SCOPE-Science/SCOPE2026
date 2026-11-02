# Bargmann-phase reversal in sharp Schatten envelopes of three equiangular projections

## Finding
Let \(H\) be a complex Hilbert space of dimension at least three. Fix \(0<t<1\). For triples of unit vectors \(u_1,u_2,u_3\in H\) satisfying \(|\langle u_i,u_j\rangle|=t\) for \(i\ne j\), put
\[
P_i=u_i\otimes u_i^*,\qquad X=P_1+P_2+P_3,
\qquad c=\frac{\operatorname{Re}(\langle u_1,u_2\rangle\langle u_2,u_3\rangle\langle u_3,u_1\rangle)}{t^3}.
\]
For finite \(p>0\), write \(N_p(X)=(\operatorname{tr}X^p)^{1/p}\), the Schatten norm when \(p\ge1\) and its standard quasi-norm when \(0<p<1\). Define
\[
A_p(t)=\big[(1+2t)^p+2(1-t)^p\big]^{1/p}
\]
and, with \(d(t)=\sqrt{12t^2-3}\),
\[
B_p(t)=\begin{cases}
\big[(1-2t)^p+2(1+t)^p\big]^{1/p},&0<t\le\tfrac12,\\
\big[((3+d(t))/2)^p+((3-d(t))/2)^p\big]^{1/p},&\tfrac12\le t<1.
\end{cases}
\]
Then the **exact attainable interval** of \(N_p(X)\), as the triple varies, is
\[
\boxed{[B_p(t),A_p(t)]\quad\text{if }0<p<1\text{ or }2<p<\infty,}
\]
\[
\boxed{[A_p(t),B_p(t)]\quad\text{if }1<p<2.}
\]
At \(p=1\), the value is always \(3\); at \(p=2\), it is always \(\sqrt{3+6t^2}\). For the operator norm \(N_\infty(X)=\|X\|\), the attained interval is \([B_\infty(t),A_\infty(t)]\), where
\[
A_\infty(t)=1+2t,\qquad
B_\infty(t)=\begin{cases}1+t,&t\le\tfrac12,\\(3+\sqrt{12t^2-3})/2,&t\ge\tfrac12.\end{cases}
\]

For every finite \(p\notin\{1,2\}\), and for \(p=\infty\), the endpoints are characterized **exactly** by the normalized real Bargmann invariant. The \(A\)-endpoint occurs precisely at \(c=1\); the \(B\)-endpoint occurs precisely at
\[
c=c_{\min}(t)=\max\left\{-1,\frac{3t^2-1}{2t^3}\right\}.
\]
The location of the maximal endpoint therefore reverses at the Schatten exponent \(p=2\), and the least-phase configuration changes type at overlap \(t=1/2\): a negative real triangle phase for \(t\le1/2\), but a rank-two Gram boundary for \(t>1/2\).

In particular, the entire phase profile is specified by the three eigenvalues (counting zeros) of the polynomial
\[
\lambda^3-3\lambda^2+3(1-t^2)\lambda-(1-3t^2+2t^3c)=0.
\]
For example, the exact fourth Schatten moment is
\[
\operatorname{tr}(X^4)=3+36t^2+18t^4+24t^3c.
\]
At the degenerate overlap boundaries, \(t=0\) gives three mutually orthogonal projections and \(t=1\) gives a single projection repeated three times; the respective finite-\(p\) values are \(3^{1/p}\) and \(3\), with operator norms \(1\) and \(3\).

## Assumptions and scope
All Hilbert spaces and inner products are complex; all triples have three unit vectors with a **common modulus** \(t\) of their pairwise inner products, and all projections are rank one. The ambient dimension at least three makes every positive-semidefinite three-by-three Gram matrix with diagonal one realizable. The phase invariant \(c\) is meaningful only for \(0<t<1\). Norm ranges are for a fixed \(t\), not optimized over \(t\). At \(0<p<1\), no triangle inequality for \(N_p\) is assumed.

## Proof
Let \(V:\mathbb C^3\to H\) send \(e_j\) to \(u_j\). Then \(X=VV^*\) and the positive Gram matrix \(G=V^*V\) have the same nonzero eigenvalues, including multiplicity; zeros do not affect the displayed finite Schatten moments. Multiplication of individual vectors by unimodular scalars fixes their projections and permits the Gram gauge
\[
G=\begin{pmatrix}
1&t&t e^{-i\theta}\\
t&1&t\\
t e^{i\theta}&t&1
\end{pmatrix},\qquad c=\cos\theta.
\]
Direct determinant calculation gives
\[
\operatorname{tr}G=3,\quad
\operatorname{tr}G^2=3+6t^2,\quad
\det G=1-3t^2+2t^3c.
\]
For \(0<t<1\), its one-by-one and leading two-by-two principal minors are positive, so Sylvester's criterion shows that \(G\ge0\) precisely when \(-1\le c\le1\) and \(c\ge(3t^2-1)/(2t^3)\). This proves the full feasibility interval \([c_{\min}(t),1]\). Every feasible \(G\) has a Gram factorization in \(\mathbb C^3\) and therefore is realized by vectors in \(H\). Its characteristic polynomial is exactly the cubic in the Finding.

At \(c=1\), the Gram eigenvalues are \(1+2t,1-t,1-t\), giving \(A_p\). If \(t\le1/2\), the lower endpoint is \(c=-1\), at which the eigenvalues are \(1-2t,1+t,1+t\). If \(t\ge1/2\), its lower endpoint is characterized by \(\det G=0\); the eigenvalues are \(0,(3+d(t))/2,(3-d(t))/2\). This proves the two formulas for \(B_p\), including continuity at \(t=1/2\), and the operator-norm endpoint formulas.

It remains to prove that no intermediate phase gives a more extreme norm, and that all nonconstant cases have strict endpoint uniqueness. For \(c\) in the interior of the feasible interval the three eigenvalues \(\lambda_1,\lambda_2,\lambda_3\) are positive and distinct. Indeed the cubic is Hermitian-real-rooted, and a repeated eigenvalue for a matrix with three equal nonzero off-diagonal moduli forces a phase \(\theta\) equal to \(0\) or \(\pi\), which occurs only at a phase endpoint. Differentiating the characteristic polynomial while its other coefficients are fixed gives
\[
\frac{d\lambda_i}{dc}=\frac{2t^3}{\prod_{j\ne i}(\lambda_i-\lambda_j)}.
\]
Consequently
\[
\frac{d}{dc}\operatorname{tr}G^p
=2pt^3\sum_{i=1}^3\frac{\lambda_i^{p-1}}{\prod_{j\ne i}(\lambda_i-\lambda_j)}
=2pt^3[\lambda_1,\lambda_2,\lambda_3](s\mapsto s^{p-1}).
\]
The final term is the second divided difference. The Hermite–Genocchi identity represents it as
\[
[\lambda_1,\lambda_2,\lambda_3]f
=\int_{\substack{a,b\ge0\\a+b\le1}}
f''\big(a\lambda_1+b\lambda_2+(1-a-b)\lambda_3\big)\,da\,db.
\]
For \(f(s)=s^{p-1}\), one has \(f''(s)=(p-1)(p-2)s^{p-3}\). The integrand is strictly positive for \(0<p<1\) or \(p>2\), strictly negative for \(1<p<2\), and identically zero at \(p=1,2\). Since \(p,t>0\), this determines the strict phase monotonicity of \(\operatorname{tr}G^p\) and hence of \(N_p\) in all asserted ranges. Continuity at the positive-semidefinite boundary supplies the extrema even when an endpoint has a zero eigenvalue.

For \(p=\infty\), the top Gram eigenvalue is simple and differentiable in the open phase interval. Because it is the largest real root, \(\prod_{j\ne\max}(\lambda_{\max}-\lambda_j)>0\), so its derivative with respect to \(c\) is strictly positive. Continuity gives the operator-norm claim. At \(p=1\), trace is three; at \(p=2\), the squared Hilbert–Schmidt norm is \(3+6t^2\). Since the admissible \(c\)-interval is connected and the moments are continuous and strictly monotone away from those two exponents, every intermediate norm occurs and only the stated phase endpoints attain the extrema.

Lastly, cyclic trace expansion, or Newton's identities using \(\operatorname{tr}G\), \(\operatorname{tr}G^2\), and \(\det G\), gives
\(\operatorname{tr}G^3=3+18t^2+6t^3c\) and \(\operatorname{tr}G^4=3+36t^2+18t^4+24t^3c\). This establishes the explicit fourth-moment formula. All steps concern actual finite-rank operators in arbitrary complex Hilbert dimension at least three.

## Verification
The reproducible companion program `verify.py` constructs Hermitian Gram matrices from feasible parameters, checks the determinant and the second through fourth trace identities, tests the predicted strict ordering for eleven finite exponents across six overlap values, and checks both closed-form endpoint spectra. It reports 2,154 supplementary checks passed. These finite samples are not used to establish phase monotonicity or universal quantification; those follow from the analytic divided-difference proof above. Run using Python 3 with NumPy: `python verify.py`.

## Relationship to prior work
Chen, Ivanisvili, Madrid, and Wang (arXiv:2606.04116, first public June 2, 2026) prove a sharp general Carbery almost-orthogonality **upper inequality** for Schatten \(p\ge2\). For the present rank-one projections, their pairwise coefficient can be taken \(\alpha_{ij}=\sqrt{t}\). Their theorem gives the valid but not phase-resolved bound \(N_p(X)\le 3^{1/p}(1+2t^{p/(2(p-1))})^{(p-1)/p}\). At \(p=4,t=1/2\) the sharp upper bound above is \((129/8)^{1/4}\), smaller than that general bound; no contradiction is involved. The present claim is the *complete sharp feasible range*, its global phase extremizers, and a sign reversal across \(p=2\), not the published general upper inequality.

Oszmaniec, Brod, and Galvão (arXiv:2109.10006; New Journal of Physics 26 (2024), 013053) establish that Bargmann invariants determine the Gram geometry of a collection of pure states. Their Gram reconstruction and the determinant criterion are credited as known premises; they do not assert the all-exponent extremal Schatten interval proved here. Qiu (arXiv:2608.17565) gives a sharp different reverse-Minkowski comparison for **two** arbitrary matrices, not the three equal-overlap projection phase optimization. Related qutrit off-diagonal Schatten results optimize a different operator and constraint (off-diagonal part at fixed purity), not the full positive sum at fixed three pairwise overlaps. A stronger unnoticed classical fixed-moment spectral inequality could imply part of the phase monotonicity; see Limitations.

## Limitations
This is an explicit three-projection, equal-overlap theorem. It does not classify unequal overlaps, weights, or four or more projections, nor does it claim a new proof of Carbery's general inequality or new Gram/Bargmann reconstruction. The proof is self-contained but rests on standard matrix spectral calculus and the classical Hermite–Genocchi identity. Full publication-priority certainty against every classical fixed-moment matrix inequality is not established. Independent expert verification has not been performed.

## References
1. Z. Chen, P. Ivanisvili, J. Madrid, H. Wang, *Carbery's inequality in the Schatten–von Neumann classes*, arXiv:2606.04116 (first public 2026-06-02).
2. M. Oszmaniec, D. J. Brod, E. F. Galvão, *Measuring relational information between quantum states, and applications*, arXiv:2109.10006; New J. Phys. 26 (2024), 013053, DOI:10.1088/1367-2630/ad1a27.
3. H. Qiu, *Sharp Quasi-Reverse Minkowski Inequality for Schatten Norms*, arXiv:2608.17565 (first public 2026-08-18).
4. C. de Boor, *Divided Differences*, Surv. Approx. Theory 1 (2005), 46–69; classical Hermite–Genocchi formula.
