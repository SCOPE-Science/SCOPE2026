# Exact second-moment spectrum and intermittency in random quadrilateral subdivision

## Finding

Let \(Q_0\) be any strictly convex, counterclockwise-labeled Euclidean quadrilateral of area \(A_0>0\). At each step choose independently one uniformly arclength-distributed point in the relative interior of each current side, join the four chosen points in cyclic order, and call the resulting polygon \(Q_{t+1}\). Define \(A_t=\operatorname{area}(Q_t)\) and the squared opposite-corner imbalance \(D_t\) in the next section. The two statistics close exactly under conditional expectation:

\[
\begin{pmatrix}\mathbb E[A_{t+1}^2]\\\mathbb E[D_{t+1}]\end{pmatrix}
=\begin{pmatrix}\tfrac{37}{144}&\tfrac7{288}\\\tfrac7{72}&\tfrac1{16}\end{pmatrix}
\begin{pmatrix}\mathbb E[A_t^2]\\\mathbb E[D_t]\end{pmatrix}.
\]

In particular, \(\mathbb E A_t=A_0/2^t\). Put \(\delta=D_0/A_0^2\), \(\lambda_\pm=(23\pm7\sqrt5)/144\), and \(C_\pm=\tfrac12\pm\tfrac1{\sqrt5}\pm\tfrac{\delta}{4\sqrt5}\), where the signs are paired. For every integer \(t\ge0\),

\[
\frac{\mathbb E[A_t^2]}{A_0^2}=C_+\lambda_+^t+C_-\lambda_-^t.
\]

For any fixed initial area and every \(t\ge1\), *precisely the parallelograms* minimize the area variance. More sharply, for an arbitrary initial quadrilateral \(Q_0\) and any initial parallelogram of the same area, the normalized variance difference equals

\[
\frac{\operatorname{Var}_Q(A_t)-\operatorname{Var}_{\rm para}(A_t)}{A_0^2}
=\frac{\delta}{4\sqrt5}(\lambda_+^t-\lambda_-^t)\ge0,
\]

with equality for \(t\ge1\) exactly if \(Q_0\) is a parallelogram. Define the mean-normalized area \(W_t=2^tA_t/A_0\). Then \((W_t)_{t\ge0}\) is a nonnegative mean-one martingale,

\[
\mathbb E W_t^2=C_+\left(\frac{23+7\sqrt5}{36}\right)^t+C_-\left(\frac{23-7\sqrt5}{36}\right)^t
\sim C_+\left(\frac{23+7\sqrt5}{36}\right)^t,
\]

and yet \(W_t\to0\) almost surely. Thus the mean-normalized process loses typical mass even while its second moment grows exponentially.

## Assumptions and scope

All polygon vertices are distinct and labeled counterclockwise. For any strictly convex quadrilateral \(Q=(v_0,v_1,v_2,v_3)\), indices are modulo four. Define the nonnegative adjacent-three-vertex triangle areas

\[
c_i(Q)=\frac12\det(v_i-v_{i-1},v_{i+1}-v_i),\qquad
D(Q)=(c_0-c_2)^2+(c_1-c_3)^2.
\]

The two identities \(c_0+c_2=c_1+c_3=\operatorname{area}(Q)\) follow from triangulating along either diagonal. The quantity \(D(Q)\) is nonnegative, scales as squared area, and vanishes exactly on parallelograms. All four sampling parameters \(U_{t,i}\) are mutually independent \(\operatorname{Uniform}(0,1)\) variables over indices and times. The update is \(v_i^{(t+1)}=(1-U_{t,i})v_i^{(t)}+U_{t,i}v_{i+1}^{(t)}\). The new polygon is strictly convex with positive area almost surely; no degeneracy correction or conditional resampling is used. Expected values are over these parameters, without shape conditioning.

## Proof

**Step 1: affine reduction and one-step area mean.** Every strictly convex labeled quadrilateral is a nonsingular orientation-preserving affine image of
\(v_0=(0,0),v_1=(1,0),v_2=(s,h),v_3=(0,1)\), where \(s>0\), \(h>0\), and \(s+h>1\). In this chart the area is \(A=(s+h)/2\), and direct adjacent triangle determinants give
\[
D=\frac{(2-s-h)^2+(h-s)^2}{4}.
\]
Both \(A^2\) and \(D\) transform by the square of the affine determinant, while the edge fractions stay unchanged. Hence it suffices to verify homogeneous degree-two identities in this chart. With independent fractions \(u_0,\ldots,u_3\in[0,1]\), the four new vertices are \(v_i'=v_i+u_i(v_{i+1}-v_i)\); the shoelace area is a polynomial in these variables. Integrating it term-by-term over the unit four-cube gives the exact conditional mean \(\mathbb E[A'\mid Q]=A/2\). Induction gives \(\mathbb E A_t=A_0/2^t\).

**Step 2: second-moment closure.** The same explicit determinant expansion, now integrating the polynomials \((A')^2\) and \(D(Q')\), uses only
\(\mathbb E[u_i^k]=1/(k+1)\) and independence. On exact simplification the two conditional identities are
\[
\mathbb E[(A')^2\mid Q]=\frac{37}{144}A^2+\frac7{288}D,\qquad
\mathbb E[D(Q')\mid Q]=\frac7{72}A^2+\frac1{16}D.
\]
These polynomial identities hold for all admissible \((s,h)\), hence by affine naturality for every strictly convex quadrilateral. The standalone checker reproduces the complete symbolic integrations; its input contains the four vertices and four independent variables, rather than using the displayed matrix as an input assumption. Taking expectations proves the stated recurrence. Subtracting \((A/2)^2\) gives the useful conditional variance identity
\[
\operatorname{Var}(A'\mid Q)=\frac1{144}A^2+\frac7{288}D.
\]

**Step 3: eigenvalues, exact solution, and rigidity.** The matrix in Step 2 has characteristic polynomial
\(z^2-(23/72)z+71/5184\), hence distinct positive eigenvalues \(\lambda_\pm=(23\pm7\sqrt5)/144\). The initial state is \((A_0^2,D_0)\), and spectral decomposition of its first coordinate gives the displayed \(C_\pm\) formula, valid for every nonnegative integer \(t\). The affine chart shows \(D=0\) if and only if \(s=h=1\), i.e. precisely the parallelograms. Since \(\lambda_+>\lambda_->0\), the \(D_0\)-coefficient in the second moment is strictly positive at every \(t\ge1\). The mean depends only on initial area, so the same strictly positive coefficient proves both the sharp fixed-area variance minimization and its equality characterization.

**Step 4: exponential second moment and almost-sure collapse.** The sequence \(W_t=2^tA_t/A_0\) is a nonnegative martingale by Step 1. Its exact second moment follows from Step 3. Because \(C_+=\tfrac12+1/\sqrt5+\delta/(4\sqrt5)>0\) and \((23+7\sqrt5)/36>1\), its second moment grows at the stated sharp geometric rate. To prove almost-sure collapse without assuming uniform integrability, set \(Y_t=2A_{t+1}/A_t\). Since nested strict convex polygons have \(0<Y_t<2\), the conditional first and second moments imply
\[
\mathbb E[Y_t\mid Q_t]=1,\qquad
\operatorname{Var}(Y_t\mid Q_t)=\frac1{36}+\frac7{72}\frac{D_t}{A_t^2}\ge\frac1{36}.
\]
For all \(y\in[0,2]\), the elementary identity
\[
\frac{1+y}{2}-\sqrt y=\frac{(y-1)^2}{2(1+\sqrt y)^2}
\ge\frac{(y-1)^2}{2(1+\sqrt2)^2}
\]
implies \(\mathbb E[\sqrt{Y_t}\mid Q_t]\le 1-\varepsilon\), where \(\varepsilon=1/[72(1+\sqrt2)^2]>0\). Consequently \(\mathbb E\sqrt{W_t}\le(1-\varepsilon)^t\). For every \(a>0\), Markov's inequality makes \(\sum_{t\ge0}\mathbb P(W_t>a)\) finite; Borel–Cantelli gives \(W_t\to0\) almost surely. This does not contradict \(\mathbb E W_t=1\), because the family is not uniformly integrable. QED.

## Verification

The self-contained file `verify.py` (Python 3; requires SymPy) constructs the affine-normal-form vertices, symbolic shoelace area and all four corner triangle determinants. It integrates the exact polynomials using \(\prod_i1/(k_i+1)\) for each monomial, verifies both conditional moments and the eigenvalues, and tests the closed formulas against the matrix powers. Independent stochastic trajectories from a parallelogram check finite-step first and second moments for three different step counts. Execute `python verify.py` in the extracted directory. Its final line is `ALL_QUADRILATERAL_MOMENT_CHECKS_PASSED`. Symbolic identities establish universal polynomial equalities; Monte Carlo checks are supplementary only.

## Relationship to prior work

Maesumi (2018) evaluates moments and distribution of the *one-step randomly inscribed triangle* on the three sides of a fixed triangle; its nine-page primary paper does not contain this quadrilateral moment closure, fixed-area minimization or iterated normalized-area limit. Nguyen and Volkov (first public 2015, subsequent version 2016) study precisely the general repeated random edgewise-subdivision mechanism through products of random matrices and limit-shape flatness, with substantially more general side-fraction laws. Their available primary paper's theorems concern projective contraction, shape degeneration, and Lyapunov exponents rather than the exact area second-moment operator here; the model itself is not claimed new. Volkov (2011 preprint, journal 2013) analyzes a different quadrilateral process that selects one of four midpoint-created subquadrilaterals at random; that is not the present four-independent-side-points construction. The classical Varignon half-area formula concerns deterministic side midpoints, not the fluctuating iterated process. This claim is about the explicit shape-sensitive second-moment closure and its consequences, not the previously introduced random subdivision procedure or the elementary expected half-area identity.

## Limitations

The quantitative formulas depend on independent uniform fractions and four convex planar sides. No result is claimed for arbitrary nonuniform fractions, concave polygons, higher dimensions, or full finite-time distributions. The almost-sure collapse is for area divided by its *mean*, not a claim about the exact almost-sure Lyapunov exponent, the angular limit shape, or the distribution of any rescaled longest edge. Historical priority of the exact moment matrix remains subject to wider specialist literature review; no independent audit has occurred.

## References

1. A. Maesumi, *Triangle Inscribed-Triangle Picking*, arXiv:1804.11007, first public 2018-04-30. https://arxiv.org/abs/1804.11007
2. T.-M. Nguyen and S. Volkov, *A universal result for consecutive random subdivision of polygons*, arXiv:1506.04942, first public 2015-06-16; journal edition 2017. https://arxiv.org/abs/1506.04942
3. S. Volkov, *Random geometric subdivisions*, arXiv:1112.0932, first public 2011-12-05, journal edition 2013. https://arxiv.org/abs/1112.0932
4. P. Varignon's midpoint-quadrilateral theorem (classical; half-area property), for background. https://en.wikipedia.org/wiki/Varignon%27s_theorem
