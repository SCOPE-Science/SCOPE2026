# A sharp relaxation phase transition for two-row reshuffled Kaczmarz

## Finding

For two linearly independent unit row normals \(a,b\in\mathbb R^2\) with \(c=|\langle a,b\rangle|\in(0,1)\), a uniformly reshuffled epoch consists of one relaxed projection on each row, in either order with probability \(1/2\). If \(e\) is the initial error and \(\omega\in\mathbb R\) is the common relaxation, define the sharp one-epoch guarantee

\[
R_c(\omega)=\sup_{e\ne0}\frac{\mathbb E\|e_{\mathrm{new}}\|_2^2}{\|e\|_2^2}.
\]

With

\[
S_c(\omega)=c^2\omega^2(2-\omega)^2+2(\omega-1)^2,\qquad
D_c(\omega)=c\omega(\omega-2)(c^2\omega^2-2\omega+2),
\]

the exact contraction factor is

\[
R_c(\omega)=\frac{S_c(\omega)+|D_c(\omega)|}{2}.
\]

Let \(t_0\in(0,1)\) denote the unique root of \(2t^3+3t^2-2=0\), and let

\[
c_0=\frac{t_0}{1+t_0^2/2}=0.551112405533260\ldots.
\]

There is a sharp change in the geometry of the unique minimizer. When \(0<c\le c_0\), it is the directional-equioscillation point

\[
\omega_*(c)=\frac{2}{1+\sqrt{1-2c^2}}.
\]

When \(c_0<c<1\), it is instead the unique root in \((1,2)\) of

\[
2c^2\omega^3-3c^2\omega^2+3c\omega^2-4c\omega+2\omega-2=0.
\]

The two formulas agree at \(c=c_0\). For every \(0<c<1\), \(1<\omega_*(c)<2\), with a strict improvement over the standard \(\omega=1\). For example, at \(c=1/2\) the optimum is \(4-2\sqrt2\), giving \(R_{1/2}(\omega_*)=0.147186257614\ldots\), compared with \(R_{1/2}(1)=3/16\).

## Assumptions and scope

The two equations are consistent, their unit row normals are linearly independent, all calculations are in exact real arithmetic, the epoch order is uniform over its two permutations, and both row updates have the same fixed relaxation. The expectation is **only over the epoch's random order**; the supremum ranges over every nonzero deterministic initial error. Row signs may be changed without affecting any update, so the positive correlation \(c\) is canonical. No assumptions on the right-hand side are needed after subtraction of the unique exact solution.

## Proof

**1. Exact averaged Gram operator.** Choose orthonormal bisector coordinates, writing

\[
a=(\sqrt p,\sqrt q),\quad b=(\sqrt p,-\sqrt q),\quad p=(1+c)/2,\quad q=(1-c)/2.
\]

Set \(U=I-\omega aa^\top\), \(V=I-\omega bb^\top\). The two possible epoch error matrices are \(VU\) and \(UV\); therefore the conditional mean-square error is \(e^\top Qe\) with

\[
Q=\tfrac12\bigl[(VU)^\top(VU)+(UV)^\top(UV)\bigr].
\]

Conjugating by \(\operatorname{diag}(1,-1)\) interchanges \(U\) and \(V\); hence the off-diagonal entries of \(Q\) vanish. Direct multiplication gives

\[
Q_{11}+Q_{22}=S_c(\omega),\qquad Q_{11}-Q_{22}=D_c(\omega).
\]

The supremum of the Rayleigh quotient is the larger diagonal entry, proving the formula for \(R_c\). This proof covers all real \(\omega\), including the endpoints.

**2. Restricting relaxation.** For \(\omega\le0\) or \(\omega\ge2\), both elementary operators have smallest singular value at least one, so each product has smallest singular value at least one, and \(R_c(\omega)\ge1\). At \(\omega=1\), \(R_c(1)=c^2(1+c)/2<1\). On \(0<\omega\le1\), the polynomial \(c^2\omega^2-2\omega+2\) is positive, so \(Q_{22}\) is the larger directional factor. Its derivative is \((1-c)F_c(\omega)\), where

\[
F_c(\omega)=2c^2\omega^3-3c^2\omega^2+3c\omega^2-4c\omega+2\omega-2.
\]

Indeed \(F_c(\omega)=c^2\omega^2(2\omega-3)+c\omega(3\omega-4)+2(\omega-1)<0\) for \(0<\omega\le1\). Thus no minimizer lies at or below one.

**3. Competing directional optima.** On \(1\le\omega\le2\), the first factor \(Q_{11}\) increases strictly: with \(u=\omega-1\in[0,1]\), direct differentiation gives

\[
Q'_{11}(\omega)=(1+c)G_c(\omega),\quad
G_c(1+u)=(1-c)[c+2u-3cu^2]+2c^2u^3>0.
\]

The bracket is nonnegative because it is affine in \(c\in[0,1]\), taking the nonnegative endpoint values \(2u\) and \((1-u)(1+3u)\). Its total expression is strictly positive for \(c\in(0,1)\).

Meanwhile \(Q'_{22}(\omega)=(1-c)F_c(\omega)\). On \([1,2]\),

\[
F'_c(\omega)=6c^2\omega(\omega-1)+c(6\omega-4)+2>0,
\]

while \(F_c(1)=-c(c+1)<0\) and \(F_c(2)=4c^2+4c+2>0\). Thus \(Q_{22}\) has a unique minimizer \(v(c)\in(1,2)\) satisfying the displayed cubic equation.

The directional entries can exchange dominance only where

\[
Q_{11}-Q_{22}=-c\omega(2-\omega)[c^2\omega^2-2\omega+2]=0.
\]

For \(0<c<1/\sqrt2\), the sole exchange point in \((1,2)\) is \(r(c)=2/[1+\sqrt{1-2c^2}]\). For \(c\ge1/\sqrt2\), no exchange occurs in that interval: \(Q_{22}\) dominates. The maximum of a strictly increasing \(Q_{11}\) and a function \(Q_{22}\) that decreases then increases is uniquely minimized either at the exchange point \(r(c)\) (when \(r(c)\le v(c)\)), or at \(v(c)\) (otherwise).

**4. Exact transition.** At an exchange point write \(t=\sqrt{2(r-1)}\), so that \(r=1+t^2/2\) and \(c=t/r\). Substitution into the cubic yields the exact identity

\[
F_c(r)=t\bigl(t^3+3t^2/2-1\bigr).
\]

The cubic in parentheses is strictly increasing for \(t>0\), is negative at zero, and is positive at one, hence has exactly one positive root \(t_0\). Moreover \(c=t/(1+t^2/2)\) increases for \(0<t<\sqrt2\). Since \(F_c\) is increasing in \(\omega\), \(r(c)\le v(c)\) holds exactly when \(c\le c_0\). This proves both branches, their agreement at \(c_0\), and uniqueness globally. Strict improvement over \(\omega=1\) follows from the strict negativity of \(Q'_{22}(1)\) and the continuity of the maximum near that point.

**5. Conditional iteration guarantee.** If a fresh independent uniform order is sampled at each epoch and \(\omega=\omega_*(c)\) is held fixed, the one-epoch inequality may be conditioned on the current error and iterated, yielding \(\mathbb E\|e_k\|_2^2\le R_c(\omega_*)^k\|e_0\|_2^2\). No equality for the asymptotic exponential rate is asserted.

## Verification

The accompanying self-contained `verify.py` performs exact rational two-by-two Gram computations for multiple rational pairs of unit row normals and rational relaxation choices, checks trace and discriminant against \(S_c,D_c\), symbolically checks the two derivative identities, verifies the critical-root reduction, and numerically brackets the two branches. Run with `python verify.py` in a Python environment satisfying `requirements.txt`. The proof above, not finite computational tests, supplies the universal quantifiers and uniqueness.

## Relationship to prior work

Han and Xie, *A simple linear convergence analysis of the randomized reshuffling Kaczmarz method*, arXiv:2410.01140, first publicly submitted 2024-10-02, analyzes unrelaxed reshuffled Kaczmarz and proves a deterministic epoch contraction for all permutations. Sections 2–3.3 do not characterize the common-relaxation parameter that optimizes the sharp **conditional expected-square** contraction, nor its change from directional balancing to an interior stationary point. The objective used here differs from their worst-permutation operator bound.

Marshall and Mickelin, arXiv:2202.12224, study optimally scheduled step sizes for independently sampled noisy randomized Kaczmarz and do not supply an exact fixed-relaxation two-row reshuffling frontier. Oswald and Zhou, arXiv:1510.04727, study random reorderings in SOR-type methods and provide earlier context; the present exact minimax phase comparison should be checked against their detailed bounds before asserting broad priority. Published work on two-row averaged Kaczmarz and Kaczmarz–Motzkin addresses different update and sampling operators, not this two-permutation operator.

## Limitations

The exact optimizer is for the strongest **one-epoch** conditional expected squared-error guarantee, not necessarily the smallest asymptotic mean-square Lyapunov exponent over many independent epochs. It assumes two independent nonparallel unit row normals, a consistent planar linear system, uniform reshuffling, common relaxation, and exact arithmetic. It does not quantify wall-clock costs or prove that the resulting closed form extends to three or more rows. An equivalent specialized result in unindexed literature cannot be excluded by the search.

## References

1. D. Han and J. Xie, *A simple linear convergence analysis of the randomized reshuffling Kaczmarz method*, arXiv:2410.01140, first submitted 2024-10-02. Sections 2 and 3. https://arxiv.org/html/2410.01140
2. N. F. Marshall and O. Mickelin, *An optimal scheduled learning rate for a randomized Kaczmarz algorithm*, arXiv:2202.12224, submitted 2022-02-24. https://arxiv.org/abs/2202.12224
3. P. Oswald and W. Zhou, *Random Reordering in SOR-Type Methods*, arXiv:1510.04727, submitted 2015-10-15. https://arxiv.org/abs/1510.04727
