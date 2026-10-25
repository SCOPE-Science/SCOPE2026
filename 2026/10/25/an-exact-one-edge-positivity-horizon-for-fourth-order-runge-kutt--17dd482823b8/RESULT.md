# An exact one-edge positivity horizon for fourth-order Runge–Kutta on bidirected stars

## Finding

For every integer \(m\ge1\) and every positive array of directed rates \(a_1,\ldots,a_m,b_1,\ldots,b_m\), the **completed classical fourth-order Runge–Kutta** transition \(P(h)=\sum_{k=0}^{4}h^kQ^k/k!\) for the bidirected-star continuous-time Markov generator defined below is entrywise nonnegative exactly on one closed interval \(0\le h\le H\). Its upper endpoint is the minimum of \(m\) individually and uniquely defined positive cubic roots. Every diagonal and every transition between distinct leaves is strictly positive at **every** positive step; only hub–leaf entries can determine the cutoff. In contrast to an undirected uniformly reversible Laplacian, a three-state reversible but nonuniformly stationary Markov chain can be spectrally stable under RK4 yet have a negative transition. Three states are the smallest possible dimension of such a counterexample.

Write
\[
B=\sum_{i=1}^m b_i,\quad S_1=\sum_{i=1}^m a_i b_i,\quad S_2=\sum_{i=1}^m a_i^2b_i.
\]
For every leaf \(j\), define
\[
\begin{aligned}
A_j&=B+a_j,\\
C_j&=B^2+Ba_j+a_j^2+S_1,\\
D_j&=B^3+B^2a_j+Ba_j^2+a_j^3+(2B+a_j)S_1+S_2,\\
g_j(h)&=1-\tfrac12A_jh+\tfrac16C_jh^2-\tfrac1{24}D_jh^3.
\end{aligned}
\]
Each \(g_j\) is strictly decreasing on \([0,\infty)\), with a single positive zero \(h_j\), and
\[
P(h)\ge0\text{ entrywise}\quad\Longleftrightarrow\quad 0\le h\le H:=\min_{1\le j\le m}h_j.
\]
At \(h=H\), exactly the hub–leaf directions indexed by minimizing \(j\) vanish (besides entries that may be zero at \(h=0\)); beyond \(H\) at least one such entry is strictly negative. This is an exact classification for all positive rates, not a finite-grid conjecture.

## Assumptions and scope

The states are the hub \(0\) and distinct leaves \(1,\ldots,m\). The generator acts on **row distributions** and has \(Q_{0j}=b_j>0\), \(Q_{j0}=a_j>0\), \(Q_{00}=-B\), \(Q_{jj}=-a_j\), with all remaining off-diagonal entries zero. Thus \(Q\mathbf1=0\). There is no restriction on the ratios of rates. The claim concerns the completed linear RK4 step, not the positivity of its internal stages or nonlinear SSP monotonicity. At \(h=0\), \(P(0)=I\).

## Proof

**Matrix-entry factorization.** Direct multiplication of the block generator \(Q=\bigl(\begin{smallmatrix}-B&b^T\\a&-\operatorname{diag}(a)\end{smallmatrix}\bigr)\) yields, for every \(h>0\),
\[
P_{0j}(h)=b_jh\,g_j(h),\qquad P_{j0}(h)=a_jh\,g_j(h).
\]
For distinct leaves \(i\ne j\), writing \(T_{ij}=B+a_i+a_j\) and
\[
U_{ij}=B^2+B(a_i+a_j)+a_i^2+a_j^2+a_ia_j+S_1,
\]
one has
\[
P_{ij}(h)=a_ib_jh^2\left(\tfrac12-\tfrac16T_{ij}h+\tfrac1{24}U_{ij}h^2\right).
\]
Since \(3U_{ij}-T_{ij}^2=2B^2+B(a_i+a_j)+2a_i^2+2a_j^2+a_ia_j+3S_1>0\), the quadratic in parentheses has negative discriminant and positive leading coefficient, hence is strictly positive for all \(h\ge0\).

**Diagonals.** The positive stationary weights are proportional to \(\pi_0=1\) and \(\pi_j=b_j/a_j\). Detailed balance makes \(Q\) diagonally similar to a real symmetric negative-semidefinite matrix. The scalar stability polynomial \(R_4(-z)=\sum_{k=0}^4(-z)^k/k!\) is strictly positive for all \(z\ge0\): Taylor's theorem gives \(R_4(-z)>e^{-z}>0\) for \(z>0\). Spectral decomposition of the symmetrized matrix therefore shows that every \(P_{ii}(h)>0\) for all \(h\ge0\).

**Unique hub–leaf zeros.** Fix \(j\) and abbreviate \(A=A_j,C=C_j,D=D_j\). The derivative is \(g'_j(h)=-A/2+Ch/3-Dh^2/8\). Its discriminant is \(C^2/9-AD/4\). Set \(x=a_j/B\), \(u=S_1/B^2\), \(v=S_2/B^3\). Weighted Cauchy–Schwarz gives \(v\ge u^2\). Consequently
\[
\begin{aligned}
\frac{9AD-4C^2}{B^4}&\ge
(9x+5)u^2+(x^2+19x+10)u\\
&\hspace{1em}+5x^4+10x^3+6x^2+10x+5>0.
\end{aligned}
\]
Thus \(g'_j\) has no real zero and is negative everywhere. Since \(g_j(0)=1\) and the cubic leading coefficient is negative, its zero \(h_j\) exists, is unique and positive. Combining all matrix-entry cases proves the iff and boundary assertions. Row sums remain one because \(Q\mathbf1=0\).

**Minimal stable-but-nonpositive example.** For two leaves take \((a_1,a_2)=(1,3)\), \((b_1,b_2)=(2,1)\), \(h=1/2\), and
\[
Q=\begin{pmatrix}-3&2&1\\1&-1&0\\3&0&-3\end{pmatrix},\qquad
P(1/2)=\begin{pmatrix}
17/24&29/96&-1/96\\
29/192&295/384&31/384\\
-1/32&31/64&35/64
\end{pmatrix}.
\]
The generator spectrum is \(\{0,-2,-5\}\), so the nonstationary step multipliers are exactly \(R_4(-1)=3/8\) and \(R_4(-5/2)=83/128\), both strictly inside the unit disk. Nevertheless \(P_{02}=-1/96\) and \(P_{20}=-1/32\). Every irreducible two-state generator has nonzero eigenvalue \(-c\), and its off-diagonal RK4 entries are positive multiples of \(1-R_4(-ch)\), so the scalar absolute-stability condition is equivalent to matrix positivity in dimension two. Hence three states are minimal.

## Verification

The self-contained script `verify_rk4_star.py` constructs the exact matrices and independently checks both one-edge and two-leaf factorizations, positivity of the discriminant certificates, row sums and strict diagonal/leaf-to-leaf signs for 387 rational parameter-step configurations. It also reconstructs the displayed three-state matrix and its exact spectrum. Run with `python verify_rk4_star.py` using Python 3 and SymPy. The infinite-parameter conclusions rest on the displayed algebra and spectral argument, not on this finite sample.

## Relationship to prior work

Strong-stability-preserving Runge–Kutta theory establishes convex-combination sufficient conditions across classes of dynamical systems; see Ketcheson–Gottlieb–Macdonald (2011) and Gottlieb–Grant–Higgs (2014). This result instead computes the **exact end-step entrywise positivity region** on a nonuniformly stationary, reversible family of Markov generators. Its essential distinction from symmetric weighted-star Laplacians is the independent choice of the inward and outward rates. The sharp stable-but-nonpositive example shows that scalar spectral stability cannot replace the entrywise criterion.

## Limitations

No guarantee is asserted for intermediate RK stages, general trees, time-varying generators, zero transition rates, or nonlinear differential equations. The result concerns row-stochastic completed steps; a negative entry invalidates probabilistic propagation even if every eigenvalue is stable. Specialized older positivity literature not located in the documented comparison could contain overlapping statements.

## References

1. D. I. Ketcheson, S. Gottlieb, C. B. Macdonald, *Strong Stability Preserving Two-step Runge–Kutta Methods*, arXiv:1106.3626v1 (public 18 June 2011).
2. S. Gottlieb, Z. J. Grant, D. Higgs, *Optimal Explicit Strong Stability Preserving Runge–Kutta Methods with High Linear Order and Optimal Nonlinear Order*, arXiv:1403.6519v1 (public 25 March 2014).
3. I. Higueras, N. Happenhofer, O. Koch, F. Kupka, *Optimized strong stability preserving IMEX Runge–Kutta methods*, J. Comput. Appl. Math. 272 (2014), 116–140, DOI:10.1016/j.cam.2014.05.011.
