# Sharp sampling-order reversal for two-coordinate overrelaxed descent

## Finding

Consider one epoch of two exact-coordinate-gradient directions on any two-dimensional strictly convex quadratic, with a common coordinate relaxation \(0<\omega<2\). Compare (i) a uniformly random order using each coordinate exactly once and (ii) two independent, uniformly sampled coordinates with replacement. Each protocol uses exactly two coordinate-gradient evaluations. The exact difference between the expected objective gaps after an epoch has two signed modal components. **Sampling without replacement reduces expected objective from every nonzero initial point if and only if**
\[
0<\omega<\frac{2}{1+c}, \qquad c=\frac{|H_{12}|}{\sqrt{H_{11}H_{22}}}\in[0,1),
\]
where \(H\) is the positive-definite Hessian. At \(\omega=2/(1+c)\) the comparison is non-strict and equality is attained on one nonzero mode. If \(c>0\) and \(2/(1+c)<\omega<2\), neither sampling protocol dominates: each gives smaller expected objective on one of two explicit modes. In particular, the without-replacement protocol can even have a strictly worse *worst-case one-epoch expected contraction factor*, despite both algorithms decreasing objective on every individual coordinate step.

## Assumptions and scope

Let \(H=H^{\mathsf T}\succ0\in\mathbb R^{2\times2}\), \(b\in\mathbb R^2\), and \(f(x)=\frac12 x^{\mathsf T}Hx-b^{\mathsf T}x\), with minimizer \(x_*\). Start at any deterministic \(x_0\). A coordinate update of coordinate \(i\in\{1,2\}\) means
\[
x^+=x-\frac{\omega}{H_{ii}}\bigl( Hx-b\bigr)_i e_i,
\]
for the *same* real \(0<\omega<2\) on both steps. For protocol P (permuted), choose the order \((1,2)\) or \((2,1)\), each with probability \(1/2\). For protocol R (replacement), choose each of the two ordered pairs \((1,1),(1,2),(2,1),(2,2)\) with probability \(1/4\). Expectations are only over these two choices, conditional on the same \(x_0\).

Scale and, if necessary, change the sign of one error coordinate to obtain \(y\in\mathbb R^2\) with
\[
 f(x)-f(x_*)=F(y)=\tfrac12 y^{\mathsf T}Cy,\qquad C=\begin{pmatrix}1&c\\c&1\end{pmatrix},\quad0\le c<1.
\]
Write \(y=y_++y_-\), where \(y_+=\tfrac12(y_1+y_2)(1,1)^{\mathsf T}\) and \(y_-=\tfrac12(y_1-y_2)(1,-1)^{\mathsf T}\). Define \(F_+=F(y_+)\) and \(F_-=F(y_-)\), so \(F(y)=F_++F_-\) and both are nonnegative.

The exact one-epoch identity is
\[
\boxed{\mathbb E_R F(y_2)-\mathbb E_P F(y_2)
=\frac{\omega^2(1-c^2)(2-\omega)}4
\Bigl([2-\omega(1+c)]F_+ + [2-\omega(1-c)]F_-\Bigr).}
\]
Consequently, for \(0<\omega<2/(1+c)\), the advantage for P is strict for every \(y\ne0\); at equality it vanishes exactly on the \((1,1)\) mode; beyond the threshold it reverses on that mode but remains positive on the \((1,-1)\) mode. For \(c=0\) the threshold is \(2\), so reversal does not occur in the admissible open range.

## Proof

Let the two normalized-coordinate error maps be
\[
U=\begin{pmatrix}1-\omega&-\omega c\\0&1\end{pmatrix},\qquad
V=\begin{pmatrix}1&0\\-\omega c&1-\omega\end{pmatrix}.
\]
The first coordinate update is \(U\), the second is \(V\), and the A-energy pullback of any linear map \(M\) is \(M^{\mathsf T}CM\). Hence the exact expectation matrices for final squared \(C\)-norm are
\[
K_P=\tfrac12\bigl[(VU)^{\mathsf T}C(VU)+(UV)^{\mathsf T}C(UV)\bigr],
\]
\[
K_R=\tfrac14\bigl[(UU)^{\mathsf T}C(UU)+(UV)^{\mathsf T}C(UV)
+(VU)^{\mathsf T}C(VU)+(VV)^{\mathsf T}C(VV)\bigr].
\]
Direct matrix multiplication shows that \(K_R-K_P\) has equal diagonal entries and symmetric off-diagonal entries, so it shares the two eigendirections \(e_+=(1,1)^{\mathsf T}\) and \(e_-=(1,-1)^{\mathsf T}\) with \(C\). Its two generalized Rayleigh quotients are **exactly**
\[
\frac{e_\pm^{\mathsf T}(K_R-K_P)e_\pm}{e_\pm^{\mathsf T}Ce_\pm}
=\frac{\omega^2(1-c^2)(2-\omega)}4[2-\omega(1\pm c)].
\]
Orthogonality of the two eigenspaces in the \(C\)-inner product yields the displayed formula for every \(y\). Because \(0\le c<1\) and \(0<\omega<2\), the \(\bigl[2-\omega(1-c)\bigr]\) factor is always strictly positive. The other factor is positive, zero, or negative according as \(\omega\) is below, at, or above \(2/(1+c)\). This proves every quantified dominance, equality and incomparability assertion.

For the stronger worst-case assertion, take \(H=C\) with \(c=1/2\), \(\omega=19/10\). Both expectation matrices commute with \(C\), so the exact worst-case expected-energy ratios are the larger of their Rayleigh quotients on \(e_+\) and \(e_-\). In the order \((e_+,e_-)\) these are
\[
 P:\quad \left(\frac{137143}{160000},\frac{123501}{160000}\right),\qquad
 R:\quad \left(\frac{2047}{2560},\frac{53949}{64000}\right).
\]
Thus the worst-case ratio for P is \(137143/160000\), strictly larger than the worst-case ratio \(53949/64000\) for R, with identical two-evaluation budgets.

Finally, for either coordinate \(i\),
\[
F(y^+)-F(y)=-\frac{\omega(2-\omega)}2\bigl[(Cy)_i\bigr]^2\le0.
\]
So no individual update increases objective. The advantage reversal is genuinely an ordering-distribution effect, not instability of an individual step. These are finite-step statements, not a claim that one protocol must have a better asymptotic rate at all later epochs.

## Verification

The self-contained Python/SymPy program `checks/check.py` symbolically verifies both generalized Rayleigh-quotient identities, both single-step energy identities, the strict sign classification on a rational parameter grid, and the two exact worst-case fractions. With SymPy installed, execute `python checks/check.py` after extracting the embedded files into their relative paths. The general proof relies on exact identities and inequalities, not on the finite test grid.

## Relationship to prior work

Recht and Ré (2012) formulated without- versus with-replacement matrix-product comparisons and proved two-matrix norm inequalities for *positive-semidefinite* factors, but not this exact statewise energy ordering for overrelaxed coordinate transformations whose nontrivial eigenvalue is negative when \(\omega>1\). Oswald and Zhou (2015 preprint, 2016 revision) established general shuffled SOR energy convergence bounds for \(0<\omega<2\), without an exact two-variable comparison against independent replacement sampling. Sun, Luo and Ye (2015) developed expected-iterate results for randomized permutation block coordinate descent, not this mean-objective threshold for overrelaxed updates. Gürbüzbalaban, Ozdaglar, Vanli and Wright (2018) compared random permutations and independent sampling for exact-coordinate minimization, corresponding to \(\omega=1\), and examined expected objective rates. The present theorem pinpoints the maximal relaxation range of statewise expected-energy dominance and the onset of its failure in dimension two. It does not claim that random reshuffling generally lacks asymptotic benefit.

## Limitations

The theorem is for two real coordinates, common fixed relaxation, a strictly convex quadratic, uniform sampling, and exactly one two-step epoch. It does not classify unequal relaxation parameters, nonuniform sampling, nonlinear objectives, higher dimensions, or the full multiepoch asymptotic mean-square operator. It makes no claim of universal priority against all unpublished or inaccessible literature; exact-equivalence searches remain fallible. The displayed worst-case example is exact, not a statistical simulation.

## References

1. B. Recht and C. Ré, *Beneath the Valley of the Noncommutative Arithmetic-Geometric Mean Inequality*, arXiv:1202.4184 (first submitted 2012-02-19), Sections 1 and 3.1. https://arxiv.org/abs/1202.4184
2. R. Sun, Z.-Q. Luo and Y. Ye, *On the Efficiency of Random Permutation for ADMM and Coordinate Descent*, arXiv:1503.06387 (first submitted 2015-03-22). https://arxiv.org/abs/1503.06387
3. P. Oswald and W. Zhou, *Random Reordering in SOR-Type Methods*, arXiv:1510.04727 (first submitted 2015-10-15), Sections 1 and 3; original MSC 65F10. https://arxiv.org/abs/1510.04727
4. M. Gürbüzbalaban, A. Ozdaglar, N. D. Vanli and S. J. Wright, *Randomness and Permutations in Coordinate Descent Methods*, arXiv:1803.08200 (submitted 2018-03-22), Sections 1–4. https://arxiv.org/abs/1803.08200
