# Strict majorization and sharp Crank–Nicolson positivity on anisotropic Boolean cubes

## Finding
For an integer \(d\ge2\), let \(Q_d=\{0,1\}^d\). Give every edge that flips coordinate \(i\) a positive conductance \(a_i\), and write \(S=\sum_{i=1}^d a_i\). The graph Laplacian \(L_{\boldsymbol a}\) has diagonal \(S\) and off-diagonal entries \(-a_i\) on coordinate-\(i\) edges. Define the Crank–Nicolson end-step operator
\[
 C_{\boldsymbol a}(s)=(I+sL_{\boldsymbol a})^{-1}(I-sL_{\boldsymbol a}),\qquad s\ge0.
\]
The physical time step in the trapezoidal-rule convention is \(h=2s\). For every strictly positive \(\boldsymbol a\), the end-step matrix is entrywise nonnegative **exactly** for \(0\le s\le s_*(\boldsymbol a)\), where \(s_*(\boldsymbol a)>0\) is the unique root of
\[
 \boxed{\quad 2^{-d}\sum_{J\subseteq\{1,\ldots,d\}}
 \frac{1}{1+2s\sum_{j\in J}a_j}=\frac12.\quad}
\]

**Strict majorization law.** If two positive vectors \(\boldsymbol a,\boldsymbol b\) have the same sum, and \(\boldsymbol a\) majorizes \(\boldsymbol b\), then
\[
 s_*(\boldsymbol a)\ge s_*(\boldsymbol b),
\]
with equality **if and only if** their coordinates agree up to permutation. Thus, increasing directional anisotropy in the majorization order strictly enlarges the end-step positivity interval, although the largest Laplacian eigenvalue remains \(2S\).

**Complete fixed-budget, lower-cap extremizers.** Fix \(S>0\) and \(0<\varepsilon<S/d\). Among all rate vectors with \(a_i\ge\varepsilon\) and \(\sum_i a_i=S\), the unique minimizer of \(s_*\) is the equal-rate vector \((S/d,\ldots,S/d)\); every maximizer is a permutation of
\[
 (S-(d-1)\varepsilon,\varepsilon,\ldots,\varepsilon).
\]
In particular, the optimizers are classified without imposing coordinate symmetry beforehand.

**Sharp dimension and singular-anisotropy laws.** Put \(\Theta_d=S s_*(S/d,\ldots,S/d)\). Then \(\Theta_2=(1+\sqrt5)/2\), the sequence decreases strictly to \(1\), and
\[
 \boxed{\quad \Theta_d=1+\frac{1}{2d}+\frac{5}{8d^2}+O(d^{-3}).\quad}
\]
At fixed \(d\ge2\) and \(S>0\), the maximal threshold under the lower bound \(\varepsilon\) has the sharp singular behavior
\[
 \boxed{\quad s_*(S-(d-1)\varepsilon,\varepsilon,\ldots,\varepsilon)
 \sim \frac{1}{\sqrt{2(d-1)S\varepsilon}}\quad(\varepsilon\downarrow0).\quad}
\]
For \(d=2\), arbitrary positive rates \(a,b\), and \(S=a+b\), the unique root satisfies the exact cubic
\[
 4abS\,s^3-2S\,s-1=0.
\]
These statements concern the full end-step matrix, not positivity of internal stages.

## Assumptions and scope
All dimensions are finite integers \(d\ge2\). The underlying graph is the unlooped Boolean cube with two vertices per coordinate, and its Laplacian uses the combinatorial (unnormalized) convention. Each of the \(d\) directional rates is positive and is applied to **every** edge in that coordinate direction. The step parameter is \(s=h/2\), where \(h\) is physical time. The budget and lower-rate extremal statement assumes \(0<\varepsilon<S/d\); the degenerate case \(\varepsilon=S/d\) has the single feasible equal-rate vector. The singular limit takes \(d,S\) fixed and \(\varepsilon\) positive before tending to zero.

Here \(\boldsymbol a\) majorizes \(\boldsymbol b\) if their sums agree and the sum of the largest \(k\) coordinates of \(\boldsymbol a\) is at least that of \(\boldsymbol b\) for every \(1\le k<d\). Strictness is stated only after excluding permutations.

## Proof
**1. Exact positivity reduction.** Because \(L_{\boldsymbol a}\) has nonpositive off-diagonal entries and zero row sums, \(I+sL_{\boldsymbol a}\) is a nonsingular \(M\)-matrix for \(s\ge0\). Its inverse \(R_s\) is nonnegative and row-stochastic. More explicitly, \(R_s=\int_0^\infty e^{-t}e^{-stL_{\boldsymbol a}}\,dt\), and for \(s>0\) every entry of \(R_s\) is positive because the weighted cube is connected. The exact Cayley identity is
\[
 C_{\boldsymbol a}(s)=2R_s-I.
\]
Hence every off-diagonal entry of \(C_{\boldsymbol a}(s)\) is strictly positive when \(s>0\), and its nonnegativity is equivalent to all diagonal entries of \(R_s\) being at least \(1/2\).

**2. Walsh diagonalization and uniqueness.** For \(J\subseteq\{1,\ldots,d\}\), the Walsh character \(\chi_J(x)=(-1)^{\sum_{j\in J}x_j}\) is an eigenvector of \(L_{\boldsymbol a}\) with eigenvalue \(2\sum_{j\in J}a_j\). Since all normalized Walsh characters have squared coordinate \(2^{-d}\), every diagonal entry of \(R_s\) equals
\[
 F_{\boldsymbol a}(s)=2^{-d}\sum_J\frac{1}{1+2s\sum_{j\in J}a_j}.
\]
For \(d\ge2\) and positive rates, this function decreases strictly and continuously from \(1\) at zero to \(2^{-d}<1/2\) at infinity. It therefore crosses \(1/2\) at exactly one positive number. This proves the positivity criterion, including both endpoints and no later positivity windows.

**3. Strict majorization and all extremizers.** Let \(X_1,\ldots,X_d\) be independent fair Bernoulli variables. For fixed \(s>0\),
\[
 F_{\boldsymbol a}(s)=\mathbb E\left[\frac{1}{1+2s\sum_i a_iX_i}\right].
\]
The function of \(\boldsymbol a\) on the positive orthant is permutation invariant and has Hessian quadratic form
\[
 \boldsymbol v^{\mathsf T}(\nabla^2 F)\boldsymbol v
 =8s^2\mathbb E\left[\frac{(\sum_i v_iX_i)^2}{(1+2s\sum_i a_iX_i)^3}\right]>0
 \quad\text{for every }\boldsymbol v\ne0.
\]
Strict positivity follows from the positive-probability singleton events \((X_1,\ldots,X_d)=\boldsymbol e_i\). Thus \(F\) is strictly convex and symmetric. Applying a nontrivial two-coordinate averaging strictly decreases \(F\), and the elementary averaging characterization of majorization gives
\[
 F_{\boldsymbol a}(s)>F_{\boldsymbol b}(s)
\]
when \(\boldsymbol a\) strictly majorizes \(\boldsymbol b\). Because each \(F\) strictly decreases in \(s\), its \(1/2\)-crossing is strictly larger for \(\boldsymbol a\). Among fixed-sum vectors with all coordinates at least \(\varepsilon\), the equal vector is majorized by every vector and the vector with one coordinate \(S-(d-1)\varepsilon\) and the others \(\varepsilon\) majorizes every vector. This proves the exact minimizer and all maximizers, with uniqueness up to permutation. The Laplacian top eigenvalue is \(2S\) by the Walsh formula, demonstrating that it cannot distinguish these thresholds.

**4. Dimension monotonicity and exact two-dimensional root.** For equal rates let \(K_d\sim\operatorname{Bin}(d,1/2)\), \(Z_d=2K_d/d\), and \(\Theta_d=S s_*\). The scalar equation becomes
\[
 G_d(\theta):=\mathbb E\frac{1}{1+\theta Z_d}=\frac12.
\]
For any strictly convex function \(f\), the sample mean of \(d+1\) i.i.d. Bernoulli variables has a strictly smaller expectation under \(f\) than the mean of \(d\) such variables. Indeed, condition on \(d+1\) variables, omit one uniformly, and apply conditional Jensen; the inequality is strict because the variables are not all equal with positive probability. Applying this to \(f(z)=(1+\theta z)^{-1}\) gives \(G_{d+1}(\theta)<G_d(\theta)\) for every \(\theta>0\), so their decreasing \(1/2\)-crossings satisfy \(\Theta_{d+1}<\Theta_d\). Strict Jensen also gives \(G_d(1)>1/2\), whence \(\Theta_d>1\). The law of large numbers, together with \(0\le(1+\theta Z_d)^{-1}\le1\), yields \(G_d(\theta)\to(1+\theta)^{-1}\) and thus \(\Theta_d\to1\). For \(d=2\), elementary common-denominator elimination gives \(4abS s^3-2Ss-1=0\). Setting \(a=b=S/2\) reduces this to \(\Theta_2^3-2\Theta_2-1=0\), whose unique positive solution is \((1+\sqrt5)/2\).

**5. Two-term dimension expansion.** Write \(\eta_d=Z_d-1\) and \(\delta=\theta/(1+\theta)\). For \(1\le\theta\le(1+\sqrt5)/2\), \(0<\delta<1\), so the geometric series of \((1+\delta\eta_d)^{-1}\) converges uniformly. Symmetry about zero makes the odd moments of \(\eta_d\) vanish. Its second and fourth moments are exactly \(1/d\) and \(3/d^2-2/d^3\), and the sixth moment is \(O(d^{-3})\). Expanding through the fifth term with a uniformly controlled sixth-order remainder gives
\[
 G_d(\theta)=\frac{1}{1+\theta}
 \left(1+\frac{\delta^2}{d}+\frac{3\delta^4}{d^2}+O(d^{-3})\right)
\]
uniformly in that interval. Substituting \(\theta=1+A/d+B/d^2\) and equating the coefficient of each power of \(1/d\) in \(G_d(\theta)=1/2\) yields \(A=1/2\) and \(B=5/8\). Since \(-G_d'(\theta)\) is bounded below by a positive constant on a neighborhood of \(1\), the residual \(O(d^{-3})\) transfers to the root and proves the stated expansion.

**6. Sharp lower-rate singularity.** Set \(m=d-1\), \(\boldsymbol a_\varepsilon=(S-m\varepsilon,\varepsilon,\ldots,\varepsilon)\), and let \(Y\sim\operatorname{Bin}(m,1/2)\). Splitting the Bernoulli expectation according to its first coordinate gives the exact identity
\[
 F_{\boldsymbol a_\varepsilon}(s)=\frac12\mathbb E\frac{1}{1+2s\varepsilon Y}
 +\frac12\mathbb E\frac{1}{1+2s(S-m\varepsilon+\varepsilon Y)}.
\]
For any fixed \(c>0\), put \(s=c/\sqrt\varepsilon\). The two terms expand uniformly for \(c\) on compact positive intervals, yielding
\[
 F_{\boldsymbol a_\varepsilon}(c/\sqrt\varepsilon)-\frac12
 =\sqrt\varepsilon\left(\frac{1}{4cS}-\frac{mc}{2}\right)+O(\varepsilon).
\]
The continuous coefficient has exactly one positive zero \(c_*=[2mS]^{-1/2}\), is positive below it, and negative above it. Strict decrease of \(F\) then sandwiches the unique crossing between \((c_*\pm\delta)/\sqrt\varepsilon\) for every fixed small \(\delta>0\) and all sufficiently small \(\varepsilon\). This proves the sharp asymptotic.

## Verification
The standalone standard-library checker `verify.py` reconstructs the weighted Boolean-cube Laplacians, computes exact rational resolvent inverses by Gaussian elimination, and checks the Walsh diagonal formula and off-diagonal positivity on cubes of dimensions two through four. It checks randomized rational pair averaging, the exact two-direction cubic, strict finite-dimension inequalities through dimension 128, the two-term asymptotic on selected dimensions, and the singular prefactor in selected dimensions. A replay produced **3,474 successful supplementary checks**. These finite computations do not replace the analytic Hessian, convex-order, and asymptotic arguments above.

To reproduce, place `verify.py` next to this file and run `python3 verify.py` using an ordinary Python 3 installation; no third-party dependencies are used.

## Relationship to prior work
The general identity \(C=2(I+sL)^{-1}-I\) and the consequent diagonal-resolvent positivity criterion for finite Markov generators are prior results, including *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains* (2026). They alone do not provide the new all-rate strict majorization comparison, the exact fixed-sum extremizers, or either sharp asymptotic for weighted cubes.

Karlin, Lindqvist, and Yao (1993) give spectral representations and majorization relations for different Hamming-distance hypercube random walks. Their publicly accessible abstract formulates majorization between spectra of different Hamming-distance graphs; this differs from comparing the **directional conductance vectors of one cube** and their positivity horizons. Their complete article could not be accessed, so possible additional coverage inside it remains a priority risk.

Sharma and Hammett (2007) establish monotonicity difficulties for explicit anisotropic thermal-diffusion flux schemes; the full accessible paper uses centered spatial fluxes and limiters, not the exact Crank–Nicolson matrix of a Boolean product graph. Higueras and Roldán (2023) obtain sharp Crank–Nicolson positivity bounds for homogeneous Dirichlet one-dimensional heat discretizations; their full paper does not formulate this anisotropic-cube directional majorization problem.

The contribution asserted here is the combined exact threshold for the weighted Boolean cube, the **strict** comparison and global fixed-sum extremizers, and the two distinct quantified limits. Standard convexity, the Cayley identity, the Walsh basis, and general Markov-resolvent results are used as tools rather than claimed as discoveries.

## Limitations
Each coordinate is restricted to a uniform positive edge rate; the theorem does not extend directly to arbitrary independent cube-edge weights or nonreversible generators. The asymptotic \(d\to\infty\) fixes equal total rate \(S\), whereas \(\varepsilon\to0\) fixes dimension and total rate; the two limits are not interchangeable without further analysis. The singular limit approaches a disconnected chain, but the theorem requires positivity of all rates before taking the limit.

Entrywise positivity is not the same as numerical accuracy, the largest stable step size, or unconditional monotonicity for nonlinear spatial schemes. A specialist priority question remains due to inaccessible full text of Karlin–Lindqvist–Yao (1993); abstract-level topic comparisons cannot certify the absence of an equivalent internal theorem.

## References
1. Prateek Sharma and Gregory W. Hammett, *Preserving Monotonicity in Anisotropic Diffusion*, initial public preprint July 18, 2007, arXiv:0707.2616, https://arxiv.org/abs/0707.2616.
2. Samuel Karlin, Bo Lindqvist, and Yi-Ching Yao, *Markov chains on hypercubes: Spectral representations and several majorization relations*, Random Structures & Algorithms **4** (1993), 1–36, DOI:10.1002/rsa.3240040102, https://doi.org/10.1002/rsa.3240040102.
3. I. Higueras and T. Roldán, *A new insight on positivity and contractivity of the Crank–Nicolson scheme for the heat equation*, initial public preprint January 3, 2023, arXiv:2301.01066, https://arxiv.org/abs/2301.01066.
4. *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains*, public mathematical research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a.
