# Reentrant high-frequency trigonometric SBP geometry and exactly three mass-calibrated grids

## Finding
On the interval \([-1,1]\), fix \(\pi<\kappa<2\pi\) and the three-dimensional approximation space
\[
\mathcal F_\kappa=\operatorname{span}\{1,\cos(\kappa x),\sin(\kappa x)\}.
\]
Consider precisely three ordered nodes \((-1,a,1)\), where \(-1<a<1\). Say that a *positive-diagonal trigonometric summation-by-parts (FSBP) pair* consists of a real \(3\times3\) matrix \(D\) and a strictly positive diagonal matrix \(P\) such that
\[
D(f(-1),f(a),f(1))^{\mathsf T}=(f'(-1),f'(a),f'(1))^{\mathsf T}
\quad(f\in\mathcal F_\kappa),\qquad
PD+D^{\mathsf T}P=\operatorname{diag}(-1,0,1).
\]

**Complete second-band geometry law.** Such a pair exists if and only if the interior node and frequency belong to one of the following branches:
\[
\begin{array}{c|c}
\text{interior node}&\text{frequency range}\\\hline
 a=0 & \pi<\kappa<4\pi/3\\
 a=+\pi/\kappa & \pi<\kappa<5\pi/3\\
 a=-\pi/\kappa & \pi<\kappa<5\pi/3.
\end{array}
\]
For each permitted grid \((D,P)\) is unique. Thus the number of feasible interior-node locations, for each fixed \(\kappa\), is exactly three on \((\pi,4\pi/3)\), exactly two on \([4\pi/3,5\pi/3)\), and zero on \([5\pi/3,2\pi)\). In particular, at \(\kappa=3\pi/2\) only the distinct noncentral nodes \(a=\pm2/3\) work; **the midpoint fails**.

Writing \(s=\sin\kappa\), \(c=\cos\kappa\), the forced norms on the two types of branch are
\[
P_0=\operatorname{diag}(q_0,2(1+c)q_0,q_0),\qquad
q_0=\frac{s}{\kappa(1+2c)},
\]
\[
P_1=\operatorname{diag}(q_1,2(1-c)q_1,q_1),\qquad
q_1=\frac{s}{\kappa(2c-1)}.
\]
The norm \(P_1\) and its associated differentiation matrix are identical for the geometrically distinct positions \(a=+\pi/\kappa\) and \(a=-\pi/\kappa\). This is a genuine nodal alias: both the values and derivatives of every element of \(\mathcal F_\kappa\) coincide at these two possible interior sites.

**Exact physical-mass calibration.** Let \(M=\mathbf1^{\mathsf T}P\mathbf1\). Among *all* these second-band positive-diagonal FSBP pairs, imposing the additional requirement \(M=2\), the length of the physical interval, leaves exactly **three frequency/node combinations**: one central pair at the unique root \(\kappa_0\in(\pi,4\pi/3)\) of
\[
\sin\kappa_0(2+\cos\kappa_0)=\kappa_0(1+2\cos\kappa_0),
\qquad \kappa_0=4.0287013220253596\ldots,
\]
and a reflected pair at the unique root \(\kappa_1\in(\pi,5\pi/3)\) of
\[
\sin\kappa_1(2-\cos\kappa_1)=\kappa_1(2\cos\kappa_1-1),
\qquad \kappa_1=5.0667771610702530\ldots,
\]
with \(a=\pm\pi/\kappa_1=\pm0.6200376597825739\ldots\). No other \((\kappa,a)\) in the stated domain meets exact differentiation, strict diagonal positivity, SBP, and exact mass simultaneously.

## Assumptions and scope
The interval is \([-1,1]\), with exact real arithmetic, three **distinct** nodes including both endpoints, and \(\pi<\kappa<2\pi\) strictly. Exactness means differentiation of every member of the displayed three-dimensional function space. The boundary form is \(B=\operatorname{diag}(-1,0,1)\); diagonal positivity means all three entries of \(P\) are strictly greater than zero. Ordinary mass calibration \(M=2\) is **not part of the basic FSBP definition here**; it is a separate physical normalization whose entire solution set is classified. There is no restriction to symmetric interior nodes, and no assumption about stability or convergence of a fully discrete PDE solver. The integer-resonance endpoints \(\pi\) and \(2\pi\) are outside the asserted domain.

## Proof
**1. Exact differentiation forces unisolvence.** With the ordered basis \((1,\cos\kappa x,\sin\kappa x)\), form the nodal matrix
\[
V=\begin{pmatrix}
1&c&-s\\1&\cos(\kappa a)&\sin(\kappa a)\\1&c&s
\end{pmatrix},\qquad
\det V=2s\bigl(\cos(\kappa a)-c\bigr).
\]
Since \(\pi<\kappa<2\pi\), \(s\ne0\). If \(\det V=0\), then the nonzero function \(g(x)=\cos(\kappa x)-c\) vanishes at all three nodes while its endpoint derivatives \(g'(\pm1)=\mp\kappa s\) are nonzero. No matrix can then differentiate all of \(\mathcal F_\kappa\) exactly. Hence exact differentiation requires \(\det V\ne0\), and this uniquely fixes \(D=V'V^{-1}\).

**2. Interior diagonal rigidity and its alias branches.** For every unisolvent triple, the interior cardinal function is
\[
\ell_a(x)=\frac{c-\cos(\kappa x)}{c-\cos(\kappa a)}.
\]
The central diagonal entry of the unique collocation derivative is therefore
\[
D_{11}=\ell'_a(a)=\frac{\kappa\sin(\kappa a)}{c-\cos(\kappa a)},
\]
where indices are \(0,1,2\). The central diagonal entry of the SBP identity is \(2P_{11}D_{11}=0\). Strict positivity of \(P_{11}\) forces \(\sin(\kappa a)=0\). Because \(|\kappa a|<\kappa<2\pi\), the only possibilities are \(a=0\) and \(a=\pm\pi/\kappa\), all distinct and strictly interior in this frequency band. Each is unisolvent because \(c\ne1\) and \(c\ne-1\), respectively.

**3. Exhaustive symmetrizer calculation.** For the central grid, the uniquely fixed differentiation matrix is
\[
D_0=\kappa\begin{pmatrix}
-\frac{1+2c}{2s}&\frac{s}{1-c}&-\frac1{2s}\\
-\frac1{2s}&0&\frac1{2s}\\
\frac1{2s}&-\frac{s}{1-c}&\frac{1+2c}{2s}
\end{pmatrix}.
\]
For either off-center grid, since the interior samples and derivative samples are \((1,-1,0)\) and \((0,0,-\kappa)\), respectively, the *same* differentiation matrix is forced:
\[
D_1=\kappa\begin{pmatrix}
\frac{1-2c}{2s}&-\frac{s}{1+c}&\frac1{2s}\\
\frac1{2s}&0&-\frac1{2s}\\
-\frac1{2s}&\frac{s}{1+c}&\frac{2c-1}{2s}
\end{pmatrix}.
\]
The endpoint diagonal equations \(2P_{00}D_{00}=-1\) and \(2P_{22}D_{22}=1\) force equal endpoint entries \(q_0\) or \(q_1\), respectively. The \((0,1)\) off-diagonal equation forces the middle entries \(2(1+c)q_0\) or \(2(1-c)q_1\). Direct substitution proves *all* entries of
\(P_jD_j+D_j^{\mathsf T}P_j=B\) for \(j=0,1\); no further degrees of freedom remain. If \(1+2c=0\) for the central grid, or \(2c-1=0\) for the off-center grid, the corresponding endpoint derivative diagonal vanishes and the nonzero SBP endpoint diagonal cannot be satisfied. These are genuine exclusion points, not removable limits.

**4. Exact positivity and nodal multiplicity.** In the whole band \(\pi<\kappa<2\pi\), \(s<0\), and both \(1+c\) and \(1-c\) are positive. Thus \(P_0\succ0\) exactly when \(1+2c<0\), equivalent to \(\pi<\kappa<4\pi/3\), and \(P_1\succ0\) exactly when \(2c-1<0\), equivalent to \(\pi<\kappa<5\pi/3\). Combining this with Step 2 gives the exhaustive three/two/zero classification. At \(\kappa=3\pi/2\), the off-center weights are \((1/\kappa,2/\kappa,1/\kappa)\), whereas the forced midpoint endpoint weights are negative.

**5. Exactly three normalized grids.** Sum the weights:
\[
M_0(\kappa)=\frac{2s(2+c)}{\kappa(1+2c)},\qquad
M_1(\kappa)=\frac{2s(2-c)}{\kappa(2c-1)}.
\]
Define
\[
H_0(\kappa)=s(2+c)-\kappa(1+2c),\qquad
H_1(\kappa)=s(2-c)-\kappa(2c-1).
\]
On each respective positivity interval the denominator of \(M_j-2=2H_j/[\kappa\,d_j(\kappa)]\) is strictly negative, and hence exact mass is equivalent to \(H_j=0\). Direct differentiation gives
\[
H_0'(\kappa)=2s(\kappa-s)<0,
\qquad H_1'(\kappa)=2s(\kappa+s)<0,
\]
for all \(\pi<\kappa<2\pi\), since \(\kappa>\pi>1\). The endpoint values are
\[
H_0(\pi)=\pi>0,\quad H_0(4\pi/3)=-\frac{3\sqrt3}{4}<0,
\]
\[
H_1(\pi)=3\pi>0,\quad H_1(5\pi/3)=-\frac{3\sqrt3}{4}<0.
\]
The intermediate value theorem and strict monotonicity therefore give exactly one calibrated \(\kappa_0\) in the central branch and exactly one calibrated \(\kappa_1\) in the off-center branch. There is one central node at the first root and two reflected interior nodes at the second, proving exactly three distinct normalized grids. The quoted decimals are high-precision approximations; the root equations and intervals, not numerical approximations, are the exact characterization.

## Verification
Run `python verify_fsbp.py` using Python with SymPy and mpmath installed. The independent checker reconstructs each matrix by inverting the sampled basis matrix at 65-digit precision, checks every entry of the SBP identity symbolically under \(\sin^2\kappa+\cos^2\kappa=1\), tests feasibility across 149 frequency samples and all three geometries, compares the interior-cardinal obstruction against independently inverted collocation matrices, and checks the two mass-calibration roots and their positivity. It completed **1,319** assertions with output `VERIFY_OK 1319`, along with 45-digit numerical values of the roots and off-center position. The *infinite-frequency-interval and uniqueness statements are proved analytically* in the preceding section; sampled computations alone do not establish them.

## Relationship to prior work
The product-derivative space associated with \(\mathcal F_\kappa\) is \(\mathcal G=\operatorname{span}\{\sin(\kappa x),\cos(\kappa x),\sin(2\kappa x),\cos(2\kappa x)\}\). It is **not a four-dimensional Tchebyshev system** in the present band: \(\sin(2\kappa x)\) vanishes at the five distinct interior points \(0,\pm\pi/(2\kappa),\pm\pi/\kappa\). Thus the Tchebyshev-system condition sufficient for the general optimal-node theorem is not available here, even though the three-node positive-norm configurations explicitly exist. Glaubitz, Nordström, and Öffner (2022/2023) establish the general diagonal-norm FSBP framework and its positive-quadrature equivalence, including trigonometric examples at other node counts. Hale, Harley, Nchupang, and Nordström (2026) develop optimal-node generalized Gauss–Lobatto constructions, and note that optimal nodes need not be unique; their inspected sections do not classify the present second-band fixed-three-node alias branches. Glaubitz, Nordström, and Öffner (2025) additionally motivate **exact integration of constants** as a numerical quadrature constraint, even though it is not an axiom of the basic algebraic FSBP identity. The distinct contribution here is the exhaustive, explicitly parametrized *above-first-resonance* geometry law and the exactly three full-mass grids. General existence and nonuniqueness results are not claimed as new; generic statements that some positive nodes exist do not imply the exact three/two/zero phase diagram or both uniquely calibrated frequencies.

## Limitations
This is an exact finite-dimensional algebraic classification for exactly three nodes, strict **diagonal** positivity, the particular \(\mathcal F_\kappa\), and \(\pi<\kappa<2\pi\). Other node counts, non-diagonal norms, frequency ranges, or inclusion of \(x\) in the approximation space can change the result. Positive \(P\) without \(M=2\) has nonphysical constant-function quadrature; this work identifies the exceptions rather than claiming generic mass preservation. Nodal aliasing may make approximation of functions outside the prescribed space poor, and no PDE stability, conservation, convergence, or accuracy theorem for a full method is asserted. Historical specialized formulas that imply this classification may exist beyond the inspected primary literature; independent mathematical audit has not occurred.

## References
1. N. Hale, C. Harley, P. Nchupang, and J. Nordström, *Summation-by-parts operators for general function spaces: Optimal nodes*, arXiv:2604.23306v1, first posted 2026-04-25, https://arxiv.org/html/2604.23306v1 (Definitions 1–2, Theorem 6, Sections 3.5 and 4.1).
2. J. Glaubitz, J. Nordström, and P. Öffner, *Summation-by-parts operators for general function spaces*, arXiv:2203.05479 (2022), SIAM J. Numer. Anal. 61 (2023), 733–754, https://arxiv.org/abs/2203.05479 (FSBP identity, quadrature equivalence, and trigonometric construction).
3. J. Glaubitz, J. Nordström, and P. Öffner, *An Optimization-Based Construction Procedure for Function Space-Based Summation-by-Parts Operators on Arbitrary Grids*, J. Sci. Comput. 105 (2025), article 83, https://doi.org/10.1007/s10915-025-03062-1 (Sections 2.1–2.3; exact mass condition).
