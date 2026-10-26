# Quantitative apex rigidity and a uniform height law for affine projection on solid circular cones

## Finding
For each integer \(d\ge2\), define the **solid** truncated right circular cone
\[
K_d=\{(x,s)\in\mathbb R^d\times[0,1]:\|x\|_2\le s\}
\]
and equip it with **normalized volume**. Let \(P_d\) be the \(L^2\)-orthogonal projector onto the full space of real affine functions restricted to \(K_d\), and write
\[
\Lambda_d(x,s)=\int_{K_d}|\mathcal K_d((x,s),(y,t))|\,d\mu_d(y,t)
\]
for its absolute reproducing-kernel row integral. Put \(m=d+1\) and
\[
A_m=2(m+1)\left(\frac{m+1}{m+2}\right)^m-1,
\qquad B_m=\sqrt{1+\frac{(m+2)^2}{m}}.
\]
For **every** integer \(d\ge2\), every \((x,s)\in K_d\), and no additional limiting assumptions,
\[
\boxed{\left|\Lambda_d(x,s)-(1-s)A_m\right|\le sB_m,
\qquad B_m<A_m.}
\]
In particular,
\[
\boxed{\|P_d\|_{L^\infty\to L^\infty}=A_m,\qquad
\Lambda_d(x,s)<A_m\quad\text{whenever }s>0.}
\]
Thus the apex \((0,0)\) is the **unique exact norming evaluation point**. Quantitatively, the gap from the norm is at least \(s(A_m-B_m)\). The central new statement is this strict, spatially quantitative norming theorem and its uniform dimension-asymptotic consequence, rather than the numerical resemblance of \(A_m\) to an earlier simplex projection formula.

As \(d\to\infty\), the entire row-norm profile obeys
\[
\boxed{\sup_{(x,s)\in K_d}\left|\frac{\Lambda_d(x,s)}d-\frac2e(1-s)\right|=O(d^{-1/2}).}
\]
Consequently, for arbitrary evaluation points \((x_d,s_d)\in K_d\),
\[
\boxed{\frac{\Lambda_d(x_d,s_d)}{\|P_d\|_{\infty\to\infty}}\longrightarrow1
\quad\Longleftrightarrow\quad s_d\longrightarrow0.}
\]
No transverse-direction restriction is needed. This classifies all asymptotically worst-conditioned evaluation sequences by their height alone.

## Assumptions and scope
The measure \(\mu_d\) is Lebesgue volume divided by the volume of \(K_d\); it is not surface measure. The cross-sections are Euclidean balls, and the target space is exactly the \((d+2)\)-dimensional full affine-polynomial space (constants, \(d\) transverse coordinates, and the height coordinate). The ambient dimension is \(d+1\), where \(d\ge2\); the cone has one apex at height zero and a ball-shaped cap at height one. Inputs lie in real or complex \(L^\infty(K_d,\mu_d)\). The operator has the same norm for both scalar fields because its kernel is real; its output is a continuous affine function. All kernel rows are evaluated by the continuous representative.

The notation \(O(d^{-1/2})\) refers to an absolute dimension-independent implied constant; the supremum is taken over **all** points of each cone, including both boundary and interior.

## Proof
**1. Exact affine reproducing kernel.** Sample \((Y,T)\) from \(\mu_d\). Using \(Y=TU\), the variables \(T\) and \(U\) are independent, with \(U\) uniform in the unit ball of \(\mathbb R^d\) and \(T\) having density \(m t^{m-1}\) on \([0,1]\), where \(m=d+1\). Hence
\[
\eta=\mathbb ET=\frac m{m+1},\qquad
\nu=\operatorname{Var}(T)=\frac m{(m+1)^2(m+2)},
\qquad \mathbb ET^2=\frac m{m+2},
\]
\[
\mathbb EU_i=0,\quad \mathbb EU_iU_j=\frac{\delta_{ij}}{d+2},\quad
\mathbb EY_iY_j=\frac{m}{(m+1)(m+2)}\,\delta_{ij},\quad
\operatorname{Cov}(Y_i,T)=0.
\]
It follows by covariance inversion that the reproducing kernel, normalized against \(\mu_d\), is
\[
\mathcal K_d((x,s),(y,t))
=1+\frac{(s-\eta)(t-\eta)}\nu
+\frac{(m+1)(m+2)}m\,x\cdot y.
\tag{1}
\]
Indeed, integrating (1) against each element of the basis \(1,y_1,\ldots,y_d,t\) reproduces its value at \((x,s)\). In particular, every row integrates to one.

**2. Exact apex row.** Setting \((x,s)=(0,0)\) in (1) gives
\[
\mathcal K_d((0,0),(Y,T))
=(m+1)\big[(m+1)-(m+2)T\big].
\]
This changes sign at \(q=(m+1)/(m+2)\). As its expectation is one,
\[
\begin{aligned}
\Lambda_d(0,0)
&=2m(m+1)\int_0^q\big[(m+1)-(m+2)t\big]t^{m-1}\,dt-1\\
&=2(m+1)q^m-1=A_m.
\end{aligned}
\tag{2}
\]
This is an exact integration, not a finite numerical experiment.

**3. Strict base gap.** At any cap point \((v,1)\) with \(\|v\|_2\le1\), Cauchy--Schwarz and reproducing-kernel orthogonality give
\[
\Lambda_d(v,1)
\le\left(\mathbb E\big[\mathcal K_d((v,1),(Y,T))^2\big]\right)^{1/2}
=\sqrt{\mathcal K_d((v,1),(v,1))}.
\]
From (1),
\[
\mathcal K_d((v,1),(v,1))
=1+\frac{m+2}{m}+\frac{(m+1)(m+2)}m\|v\|_2^2
\le1+\frac{(m+2)^2}m=B_m^2.
\tag{3}
\]
The strict inequality \(B_m<A_m\) holds for all integers \(m\ge3\). At \(m=3,4\), direct rational comparisons are
\[
A_3=\frac{387}{125}>\sqrt{\frac{28}{3}}=B_3,
\qquad A_4=\frac{2477}{648}>\sqrt{10}=B_4.
\]
For \(m\ge5\), the inequality \(\log(1+z)<z\) gives
\[
\left(\frac{m+1}{m+2}\right)^m
=\left(1+\frac1{m+1}\right)^{-m}>e^{-1}>\frac4{11},
\]
where \(e<11/4\). Thus
\[
A_m>\frac{8m-3}{11},\qquad B_m\le\sqrt{m+6}.
\]
Since \(64m^2-169m-717>0\) for every integer \(m\ge5\), the first lower bound exceeds the second upper bound. This proves the strict gap in all dimensions.

**4. Interpolation by height.** For \(0<s\le1\), the vector \(v=x/s\) lies in the unit ball and
\[
(x,s)=(1-s)(0,0)+s(v,1).
\]
The reproducing kernel (1) is affine in the evaluation argument. Therefore the triangle and reverse-triangle inequalities under its absolute row integral yield
\[
(1-s)\Lambda_d(0,0)-s\Lambda_d(v,1)
\le\Lambda_d(x,s)
\le(1-s)\Lambda_d(0,0)+s\Lambda_d(v,1).
\]
Inserting (2) and (3) gives the displayed two-sided spatial inequality. Because \(A_m>B_m\), every positive height satisfies
\[
\Lambda_d(x,s)\le A_m-s(A_m-B_m)<A_m.
\]
At height zero, the cone has only the apex. Hence the apex is the unique maximizer, and \(\|P_d\|=\sup_{K_d}\Lambda_d=A_m\).

**5. Uniform dimension law and near-maximizers.** The elementary expansion
\[
\left(1-\frac1{m+2}\right)^m=e^{-1}\big[1+O(m^{-1})\big]
\]
shows that \(A_m=(2/e)d+O(1)\), while \(B_m=O(\sqrt d)\). Divide the two-sided inequality by \(d\), take a supremum in \((x,s)\), and use \(0\le s\le1\). This gives the stated uniform \(O(d^{-1/2})\) error. Dividing instead by \(A_m\), with \(B_m/A_m\to0\), proves uniformly
\[
\frac{\Lambda_d(x,s)}{A_m}=1-s+O(d^{-1/2}).
\]
Thus an arbitrary sequence of points is asymptotically norming exactly when its height tends to zero, establishing both directions of the rigidity claim.

## Verification
The standalone `CHECK.py` implements the Beta-ball moment identities and tests \(A_m^2>B_m^2\) with exact rational arithmetic for \(2\le d\le160\), together with covariance and polynomial-reproduction identities. It also evaluates \(\Lambda_d\) by a two-dimensional Gauss--Jacobi quadrature reduced by rotational symmetry, checking six apex integrals and 72 interior/cap row inequalities in dimensions \(2,3,4,5,8,12\). Invoke `python CHECK.py` with Python, NumPy, and SciPy installed. Those finite diagnostics do **not** prove any universal claim; all quantified statements follow from steps 1--5.

## Relationship to prior work
Li and Xu (2013, arXiv:1310.2283) study multivariate polynomial/spectral approximation on the unit ball and provide an early approximation-theory starting point; their sphere/ball Sobolev results do not give cone endpoint row norms. Figueroa (2016, arXiv:1607.00930) likewise treats weighted ball projectors and Sobolev errors, not the full affine cone amplification profile.

The particularly close cone source is Xu (2019, arXiv:1905.07587), whose Sections 3--6 construct Jacobi polynomial systems, derive cone reproducing kernels and a convolution translation, and give general \(L^p\) norm inequalities (especially Lemma 5.2 and Proposition 6.1). Formula (6.2) describes the apex kernel in Jacobi form. These formulas subsume background kernel construction but do not state the exact global affine projector norm, prove a strict positive-height gap, or obtain a uniform height-profile asymptotic. Crucially, the general convolution bound \(\|Tg\|_1\le\|g\|_1\) is not an equality claim for the apex row; it cannot by itself certify the sharp norm or uniqueness. Olver and Xu (2019, arXiv:1906.12305) give broad cone orthogonal bases and cubature, but not the claimed quantitative endpoint localization. Xu (2020, arXiv:2011.14180) gives localizable kernels and approximation results for conic domains; its abstract and stated estimates are not an exact affine-degree height norming theorem, although full equivalence elsewhere has not been excluded.

A publicly available 2026 calculation, *Exact positivity defect and max norm of the affine least-squares projector on a simplex* (identifier below), gives the **identical scalar expression** \(A_m\) for the affine projector on an \(m\)-dimensional simplex. The numerical coincidence arises because the apex height complement of the cone and a simplex barycentric coordinate both have the same Beta law. The simplex is not an affine image of a solid circular cone in dimension at least three, so its result does not imply operator-norm maximization or height rigidity on \(K_d\). This precise overlap is acknowledged: the present finding is the **cone-specific quantitative strictness and uniform spatial profile**, not novelty of the scalar expression alone.

## Limitations
The geometry is a solid circular cone with normalized volume and the target consists only of affine functions. The proof does not cover general nonsymmetric cone cross-sections, differently weighted densities, higher polynomial degrees, the lateral conic surface with Hausdorff measure, or exact finite-dimensional norms on arbitrary conical domains. The \(O(d^{-1/2})\) rate is an upper bound, not claimed optimal. Broader unindexed equivalent strict-localization theorems remain an originality risk; independent scientific audit has not yet been performed.

## References
1. H. Li and Y. Xu, *Spectral approximation on the unit ball*, first publicly posted 2013-10-08, arXiv:1310.2283, https://arxiv.org/abs/1310.2283.
2. L. E. Figueroa, *Orthogonal polynomial projection error measured in Sobolev norms in the unit ball*, first publicly posted 2016-07-04, arXiv:1607.00930, https://arxiv.org/abs/1607.00930.
3. Y. Xu, *Orthogonal polynomials and Fourier orthogonal series on a cone*, first publicly posted 2019-05-18, arXiv:1905.07587, https://arxiv.org/html/1905.07587v2, especially Lemma 5.2 and Proposition 6.1.
4. S. Olver and Y. Xu, *Orthogonal polynomials in and on a quadratic surface of revolution*, first publicly posted 2019-06-25, arXiv:1906.12305, https://arxiv.org/abs/1906.12305.
5. Y. Xu, *Approximation and localized polynomial frame on conic domains*, first publicly posted 2020-11-28, arXiv:2011.14180, https://arxiv.org/abs/2011.14180.
6. *Exact positivity defect and max norm of the affine least-squares projector on a simplex*, public result and proof (2026), https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-exact-positivity-defect-and-max-norm-of-the-affine-least-squares--99c2b9dd9b34/RESULT.md.
