# Sharp local Hornich--Hlawka stability at the critical real three-coordinate witness

## Finding
Let \(p_*=\log 3/\log(3/2)\) and let \(X_*=(v_1,v_2,v_3)\), with
\[v_1=(-1,1,1),\qquad v_2=(1,-1,1),\qquad v_3=(1,1,-1).\]
For \(X=(x,y,z)\in(\mathbb R^3)^3\), define the signed Hornich--Hlawka deficit
\[
F_p(X)=\|x\|_p+\|y\|_p+\|z\|_p+\|x+y+z\|_p
       -\|x+y\|_p-\|y+z\|_p-\|z+x\|_p.
\]
The exact real Hessian spectrum at the critical, zero-deficit witness \(X_*\) is
\[
\operatorname{spec} D^2F_{p_*}(X_*)
=\left\{0^{(1)},\ \left(\frac{p_*-1}{2}\right)^{(4)},\
\left((p_*-1)\left(1-\frac{\sqrt6}{3}\right)\right)^{(2)},\
\left((p_*-1)\left(1+\frac{\sqrt6}{3}\right)\right)^{(2)}\right\}.
\]
The nullspace is exactly \(L=\mathbb R X_*\), the scaling direction. Distances below use the ordinary Euclidean norm on the nine real entries. The sharp local stability coefficient is
\[
\boxed{\lim_{\varepsilon\downarrow0}
\inf_{\substack{0<\operatorname{dist}(X,L)\\\|X-X_*\|_2<\varepsilon}}
\frac{F_{p_*}(X)}{\operatorname{dist}(X,L)^2}
=\frac{p_*-1}{2}\left(1-\frac{\sqrt6}{3}\right)>0.}
\]
Thus every sufficiently small non-scaling perturbation has strictly positive deficit; every smaller coefficient is a valid uniform local quadratic lower bound.

There is also a one-sided exponent-persistence statement. On the affine normalization hyperplane
\[H=\{X:\langle X,X_*\rangle=9\},\]
there are an open ball about \(X_*\), a positive \(\eta\), and a unique local minimizer \(X(p)\) of \(F_p|_H\) in that ball for \(|p-p_*|<\eta\). It satisfies \(X(p_*)=X_*\), \(X(p)-X_*=O(|p-p_*|)\), and
\[
\boxed{F_p(X(p))=\frac{6\log 3}{p_*^2}(p_*-p)+O((p_*-p)^2).}
\]
In particular, for \(p<p_*\) sufficiently near \(p_*\), there is a fixed conical neighborhood of the positive ray through \(X_*\) on which the deficit is strictly positive. At \(p=p_*\), equality in that neighborhood holds only on the positive ray.

## Assumptions and scope
The vectors are real and have exactly three coordinates, \(p>2\) in the endpoint neighborhood, and the deficit uses the usual real \(\ell_p^3\) norm. There are no constraints on signs of perturbations. The word local is essential: no global positivity assertion for all triples is made. The parameter \(p_*\) is the established sharp threshold of the classical symmetric *test triple*, not a proved global threshold for the Hornich--Hlawka property.

## Proof
**1. Zero deficit, differentiability and stationarity.** At \(p=p_*\), \(3^{1/p_*}=3/2\), while \(v_1+v_2+v_3=(1,1,1)=u\), and the three pair sums are the coordinate-axis vectors of length \(2\). Consequently \(F_{p_*}(X_*)=4(3/2)-3(2)=0\). Since \(p_*>2\), every norm term is \(C^2\) near its nonzero argument, including terms with some zero coordinates. At any vector \(v\) with coordinates \(\pm1\), differentiation gives
\[
\nabla\|v\|_{p_*}=\frac12v,\qquad
D^2\|v\|_{p_*}=\frac{p_*-1}{2}\left(I_3-\frac{vv^{\mathsf T}}3\right).
\]
At a coordinate-axis vector \(2e_j\), the Hessian vanishes identically for \(p_*>2\). The first derivatives of the four positive norm terms cancel those of the three pair-sum norms, so \(\nabla F_{p_*}(X_*)=0\).

**2. Exact matrix and characteristic polynomial.** Put \(P_v=I_3-vv^{\mathsf T}/3\). In the three-vector, nine-coordinate block decomposition,
\[
D^2F_{p_*}(X_*)=\frac{p_*-1}{2}M,\qquad
M_{ij}=P_u+\delta_{ij}P_{v_i}\quad(1\le i,j\le3).
\]
The matrix \(M\) is symmetric, rational, and positive semidefinite directly from
\[
\langle h,Mh\rangle=\sum_{i=1}^3\|P_{v_i}h_i\|_2^2+
\left\|P_u\sum_{i=1}^3h_i\right\|_2^2.
\]
A rational determinant expansion, independently reproducible by the included exact-arithmetic verifier, yields the identity
\[
\boxed{\det(tI_9-M)=\frac19t(t-1)^4(3t^2-12t+4)^2.}
\]
Thus its eigenvalues are \(0\) once, \(1\) four times, and \(2\pm2\sqrt6/3\) twice each. Since \(M X_*=0\) and the zero eigenvalue is simple, its kernel equals \(L\). Multiplying the eigenvalues by \((p_*-1)/2\) proves the asserted Hessian spectrum.

**3. Sharp transverse coefficient and actual lower bound.** Taylor's formula gives
\[
F_{p_*}(X_*+h)=\frac{p_*-1}{4}\langle h,Mh\rangle+o(\|h\|_2^2).
\]
Write any sufficiently close \(X\) uniquely as \((1+s)X_*+w\) with \(w\perp X_*\). Positive homogeneity yields
\[
F_{p_*}((1+s)X_*+w)=(1+s)F_{p_*}(X_*+w/(1+s)).
\]
Uniform Taylor control for small \(s,w\) therefore bounds this by the least positive eigenvalue \(2-2\sqrt6/3\) of \(M\), times the factor \((p_*-1)/4\), up to an arbitrarily small relative error. Because \(\operatorname{dist}(X,L)=\|w\|_2\), every coefficient strictly below the displayed value holds in some neighborhood. Along \(X=X_*+tw\) for a nonzero eigenvector \(w\) of the least positive eigenvalue, the quotient tends to the displayed coefficient, proving sharpness and local equality rigidity.

**4. Persistence for nearby exponents.** Restrict \(F_p\) to the affine hyperplane \(H\). Its Hessian at \((p_*,X_*)\) is strictly positive definite on the tangent space \(X_*^\perp\), so the ordinary implicit-function theorem applied to the restricted gradient gives a unique nearby critical point \(X(p)\), depending continuously differentiably on \(p\). By shrinking a common ball and exponent interval, the restricted Hessian is uniformly positive, hence this critical point is the unique local minimizer within that ball. In particular \(X(p)-X_*=O(|p-p_*|)\). Direct substitution gives
\[
F_p(X_*)=4\cdot3^{1/p}-6,
\qquad \left.\frac{d}{dp}F_p(X_*)\right|_{p=p_*}
=-\frac{6\log3}{p_*^2}.
\]
Since the restricted gradient vanishes at the endpoint, replacing \(X_*\) by \(X(p)\) changes the deficit by only \(O((p-p_*)^2)\). This proves the one-sided linear asymptotic. For \(p<p_*\), the positive leading coefficient makes the unique nearby restricted minimum positive. Positive homogeneity extends this statement to the cone around the positive ray.

## Verification
The accompanying standalone script `verify_hlawka.py` uses only Python's standard library. It forms the exact rational \(9\times9\) matrix from the projection formula and recomputes the full monic characteristic polynomial by the Faddeev--LeVerrier recursion over rational numbers, without floating-point linear algebra or a symbolic package. It checks the null vector, least-eigenvalue witness, five finite-difference approaches to the sharp coefficient, 1,200 deterministic generic transverse directions, and the exponent derivative at the witness. The exact characteristic polynomial identity and analytic argument establish the all-direction and all-neighborhood assertions; finite numerical checks alone do not.

Reproduce with `python verify_hlawka.py` in a Python 3 environment. The verifier is included verbatim in the research package and requires no input files, dependencies or network access.

## Relationship to prior work
Marinescu and Niculescu (2025, §3) established the symmetric test triple and its failure for exponents strictly above \(p_*\). Lee (2026, §3.1 and §4) explicitly identifies the unresolved critical range, reduces the general finite-dimensional question to \(\ell_{p_*}^3\), and formulates opposed conjectures concerning that global inequality. Neither inspected primary text determines the Hessian spectrum, local rigidity coefficient, or persistence of positive deficit in a fixed neighborhood below the endpoint. The linear change of variables in Lee's Proposition 4.2 is equivalent to the same inequality, but does not supply these quantitative conclusions. No globally valid Hornich--Hlawka inequality is assumed.

## Limitations
The finding is strictly local around a specified symmetry orbit of a witness in real dimension three. It neither proves nor disproves the global endpoint conjecture; a distant counterexample, or an endpoint equality triple outside this local family, remains possible. Numerical checks supplement rather than replace the proof. Publication priority beyond the checked sources and research index cannot be guaranteed, and no independent scientific audit has been performed.

## References
1. S. Lee, *Constructions and reductions on the Hornich-Hlawka inequality and its generalizations*, arXiv:2610.23785v1 (publicly posted 2026-10-16), https://arxiv.org/html/2610.23785v1. Primary MSC2020: 46B20.
2. D.-Ş. Marinescu and C. P. Niculescu, *A New Look at the Hornich-Hlawka Inequality*, Results in Mathematics 80, article 149 (2025), https://doi.org/10.1007/s00025-025-02464-9.
