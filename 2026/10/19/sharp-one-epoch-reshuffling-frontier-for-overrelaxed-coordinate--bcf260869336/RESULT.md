# Sharp one-epoch reshuffling frontier for overrelaxed coordinate descent

## Finding

For a strictly convex quadratic in two coordinates, independent sampling with replacement and sampling once without replacement need not be ordered by their expected objective error when the coordinate steps are overrelaxed. The exact frontier is the inverse-conditioned threshold \(\omega_*=1+1/\kappa\), where \(\kappa\) is the condition number of the diagonally normalized Hessian.

More precisely, let \(H\in\mathbb R^{2\times2}\) be real symmetric positive definite. Write \(d_i=H_{ii}\), \(c=H_{12}/\sqrt{d_1d_2}\), and \(r_i=(Hx)_i/\sqrt{d_i}\) for a fixed initial vector \(x\). For \(0<\omega<2\), let \(F(x)=x^{\mathsf T}Hx/2\) and perform two relaxed coordinate steps, once under a uniformly random permutation and once under two independent uniform draws. Then the exact expected-objective gap is
\[
\Delta:=\mathbb E F(x_2^{\mathrm{iid}})-\mathbb E F(x_2^{\mathrm{shuffle}})
=\frac{\omega^2(2-\omega)}8\left[(2-\omega+\omega c^2)(r_1^2+r_2^2)-4cr_1r_2\right].
\]
This gap is nonnegative for every \(x\) if and only if \(\omega\le 2/(1+|c|)\). For \(|c|>0\) and larger admissible relaxation, either sign occurs as the starting vector changes.

## Assumptions and scope

The matrix \(H\) is any fixed real symmetric positive-definite \(2\times2\) matrix with both diagonal entries strictly positive; hence \(|c|<1\). The initial \(x\) is arbitrary and deterministic. Both procedures use exactly two coordinate-gradient evaluations, with the same relaxation \(\omega\in(0,2)\). In the shuffled procedure each coordinate occurs exactly once and both orders have probability \(1/2\). In the independent procedure all four ordered pairs have probability \(1/4\). Expectation is over this finite sampling only. There are no observation noises, nonlinear objectives, or floating-point effects.

The eigenvalues of the normalized Hessian \(\widehat H=D^{-1/2}HD^{-1/2}\), where \(D=\operatorname{diag}(d_1,d_2)\), are \(1\pm|c|\). Thus its condition number is \(\kappa=(1+|c|)/(1-|c|)\) and \(2/(1+|c|)=1+1/\kappa\). The stated \(\kappa\) is not necessarily the condition number of unnormalized \(H\).

## Proof

**1. Normalize the coordinates.** Set \(y=D^{1/2}x\). Then \(F(x)=\tfrac12y^{\mathsf T}\widehat Hy\), \(\widehat H=\begin{pmatrix}1&c\\c&1\end{pmatrix}\), and the relaxed coordinate step becomes \(y_i\leftarrow y_i-\omega(\widehat Hy)_i\). Put \(r=\widehat Hy\), which agrees with \(r_i=(Hx)_i/\sqrt{d_i}\).

**2. Identify each objective decrease.** A step on coordinate \(i\) reduces \(F\) by exactly \(\beta r_i^2/2\), where \(\beta=\omega(2-\omega)>0\). If the first selected coordinate is \(i\) and the other is \(j\), then the updated gradient satisfies \(r_i'= (1-\omega)r_i\) and \(r_j'=r_j-\omega c r_i\). Both sampling schemes select the first coordinate uniformly and so have equal expected first-step decrease.

**3. Compare the second step.** Conditional on first index \(i\), shuffling takes \(j\) with certainty and independent sampling takes \(i\) or \(j\) with equal probabilities. The independent-minus-shuffled final expected energy is therefore
\[
\Delta=\frac{\beta}{8}\sum_{i=1}^2\left[(r_j-\omega c r_i)^2-(1-\omega)^2r_i^2\right],\qquad j=3-i.
\]
Expanding the two terms gives the exact gap stated above. The normalization change is invertible, so this holds for arbitrary positive diagonals.

**4. Determine the sharp sign frontier.** The bracket is the quadratic form \(r^{\mathsf T}Kr\) with
\[
K=\begin{pmatrix}a&-2c\\-2c&a\end{pmatrix},\qquad a=2-\omega+\omega c^2.
\]
Its eigenvalues are \(a+2|c|>0\) and
\[
a-2|c|=(1-|c|)\bigl(2-\omega(1+|c|)\bigr).
\]
Since \(|c|<1\), this form is positive semidefinite exactly when \(\omega\le 2/(1+|c|)\). It is positive definite strictly below that threshold, proving strict improvement for every nonzero \(x\) because \(r=\widehat Hy\ne0\). If \(0<|c|<1\) and \(\omega>2/(1+|c|)\), the gradient choices \(r=(1,\operatorname{sgn}c)\) and \(r=(1,-\operatorname{sgn}c)\) give opposite signs. Every such gradient arises from exactly one initial vector \(x\) because \(H\) is invertible. At equality the first choice gives a zero gap and the second a positive gap. If \(c=0\), the threshold is \(2\), outside the allowed open interval, and the gap is strictly positive for every nonzero start.

**5. Exact counterexample.** With \(H=\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}\), \(\omega=3/2\), and normalized gradient \(r=(1,1)\), the initial vector is \(x=(2/3,2/3)\). Direct substitution yields \(\Delta=-9/256\). With the same Hessian and stepsize but gradient \(r=(1,-1)\), the gap is \(135/256>0\). The crossover occurs at \(\omega_*=4/3\).

## Verification

Execute `python verify.py` using Python 3's standard library. This script independently constructs all four ordered two-step trajectories, computes their exact rational quadratic energies, and checks the closed formula for several rational Hessian couplings, relaxation parameters and arbitrary gradients. It also tests rescaling to a Hessian with diagonal \((4,9)\), the explicit sharp counterexample, and equality at the threshold. All assertions use exact rational arithmetic. The analytical proof above, not these finite tests, establishes the universal quantifiers.

## Relationship to prior work

Gürbüzbalaban, Ozdaglar, Vanli, and Wright study random permutations versus with-replacement coordinate descent for strictly convex quadratic objectives, using exact coordinate minimization. Their analysis does not compare the same algorithms across \(\omega\in(1,2)\) or prove the sharp \(2/(1+|c|)\) reversal frontier. Oswald and Zhou study shuffled SOR for general relaxations and prove convergence bounds, and discuss independent sampling, but do not establish an exact, samplewise two-coordinate expected-energy ordering against independent draws. The result here sharpens this specific comparison in the smallest nontrivial SPD system, without overturning either paper's convergence guarantees. Sun, Luo, and Ye examine random permutation in coordinate descent and ADMM with different iteration operators and asymptotic performance criteria.

## Limitations

The classification compares expected objective after exactly two coordinate evaluations from one deterministic start. It is not an assertion about every realized pair of trajectories, arbitrary-dimensional matrices, later epochs, expected iterate norms, or their asymptotic convergence factors. Shuffling can be worse than independent sampling after two steps even though each individual relaxed step decreases the quadratic objective when \(0<\omega<2\). The threshold uses diagonal-normalized condition number. An equivalent comparison hidden in an alternative SOR or randomized splitting formulation remains a possible literature-priority risk.

## References

1. M. Gürbüzbalaban, A. Ozdaglar, N. D. Vanli, S. J. Wright, *Randomness and Permutations in Coordinate Descent Methods*, arXiv:1803.08200, first posted 2018-03-22; *Mathematical Programming* 181 (2020), 349–376, DOI:10.1007/s10107-019-01438-4.
2. P. Oswald, W. Zhou, *Random reordering in SOR-type methods*, *Numerische Mathematik* (2016), DOI:10.1007/s00211-016-0829-7. Author-hosted full text: https://zhou.ac.cn/articles/shuffling.pdf.
3. R. Sun, Z.-Q. Luo, Y. Ye, *On the Efficiency of Random Permutation for ADMM and Coordinate Descent*, arXiv:1503.06387, first posted 2015-03-22.
