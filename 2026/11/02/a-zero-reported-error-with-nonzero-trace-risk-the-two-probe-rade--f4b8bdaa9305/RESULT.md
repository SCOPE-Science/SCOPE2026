# A zero reported error with nonzero trace risk: the two-probe Rademacher XTrace degeneracy

## Finding

Fix an integer \(n\ge2\) and a nonzero real diagonal matrix \(A=\operatorname{diag}(a_1,\ldots,a_n)\). Draw two independent test vectors \(g,h\in\{-1,1\}^n\), with all coordinates independent and fair, and apply the **unnormalized** leave-one-out XTrace estimator with a nominal four-matrix-vector-product budget (two test vectors). Write \(S_r=\sum_{j=1}^n a_j^r\), so \(S_2>0\). Denote its two leave-one-out trace estimates by \(T_g,T_h\), their average by \(\widehat\tau\), and the squared internal error indicator from equation (3.1) of the motivating paper by \(\widehat e^2\).

**Theorem.** For **every** realization \((g,h)\), the two leave-one-out estimates coincide and consequently
\[
T_g=T_h=\widehat\tau,\qquad \widehat e^2=0.
\]
Nevertheless, with independent signs \(\xi_j=g_jh_j\), the trace error has the exact quadratic Walsh expansion
\[
\widehat\tau-\operatorname{tr}A
 =\frac{2}{S_2^2}\sum_{1\le i<j\le n}a_i a_j\bigl[S_3-S_2(a_i+a_j)\bigr]\xi_i\xi_j,
\]
and hence its **actual mean-squared error** is
\[
\boxed{\displaystyle
\mathbb E\bigl[(\widehat\tau-\operatorname{tr}A)^2\bigr]
 =\frac{4}{S_2^4}\sum_{1\le i<j\le n}
 a_i^2a_j^2\bigl[S_3-S_2(a_i+a_j)\bigr]^2.}
\]
This mean-squared error vanishes **if and only if** \(A\) has rank at most one, or has exactly two nonzero diagonal entries of opposite signs and equal magnitude. In particular, it is strictly positive for every diagonal positive-semidefinite matrix of rank at least two, and for every positive-definite diagonal matrix in dimension \(n\ge2\).

For the natural test matrix \(A=I_n\), the estimate and risk simplify to
\[
\widehat\tau=n+1-\frac1n\biggl(\sum_{j=1}^n\xi_j\biggr)^2,\qquad
\mathbb E\bigl[(\widehat\tau-n)^2\bigr]=2\bigl(1-1/n\bigr),\qquad \widehat e^2=0.
\]
For \(n=2\), the estimate is exactly \(1\) or \(3\), each with probability \(1/2\), although the true trace is \(2\). Thus the absolute error is **always** one while the reported internal error is **always** zero. The same pathology persists with \(n\ge5\), where the four-product budget is smaller than the ambient dimension. In contrast, a single ordinary Rademacher Hutchinson quadratic-form probe yields the exact trace of **every** diagonal matrix.

## Assumptions and scope

The matrix is real, diagonal, and nonzero. Probe vectors are independent Rademacher vectors, **not** Gaussian vectors. The estimator is the *unnormalized* original XTrace formula (equations (1.4)–(1.6)); its optional residual-renormalized modification in section 2.3 is a different estimator and is not covered by this theorem. XTrace's internal indicator here is equation (3.1) with two leave-one-out terms. All equalities are in exact arithmetic. We neither assert the internal diagnostic is a rigorous confidence bound in the source paper nor assume that its practical adaptive implementation always initializes with four matvecs.

## Proof

Set \(v_g=Ag\) and \(v_h=Ah\). Because each coordinate of \(g\) and \(h\) has magnitude one, \(\|v_g\|_2^2=\|v_h\|_2^2=S_2>0\). The two leave-one-out projectors therefore have unit generators \(q_g=v_g/\sqrt{S_2}\) and \(q_h=v_h/\sqrt{S_2}\).

The first basic XTrace estimate is
\[
T_g=q_h^{\mathsf T}Aq_h
 +g^{\mathsf T}(I-q_hq_h^{\mathsf T})A(I-q_hq_h^{\mathsf T})g.
\]
Let \(\xi_j=g_jh_j\) and \(P_r=\sum_{j=1}^n a_j^r\xi_j\). Expanding the residual projector gives
\[
q_h^{\mathsf T}Aq_h=\frac{S_3}{S_2},\quad
g^{\mathsf T}Ag=S_1,\quad
q_h^{\mathsf T}g=\frac{P_1}{\sqrt{S_2}},\quad
q_h^{\mathsf T}Ag=\frac{P_2}{\sqrt{S_2}}.
\]
Consequently
\[
T_g=S_1+\frac{S_3}{S_2}-\frac{2P_1P_2}{S_2}
 +\frac{S_3P_1^2}{S_2^2}.
\]
Interchanging \(g\) and \(h\) leaves every \(\xi_j\), \(S_r\), and \(P_r\) unchanged. Therefore \(T_h=T_g\) **samplewise**. Their empirical sample variance, divided by the two-term factor in the source error indicator, is zero.

Next, by direct expansion,
\[
P_1P_2=S_3+\sum_{i<j}a_i a_j(a_i+a_j)\xi_i\xi_j,
\qquad
P_1^2=S_2+2\sum_{i<j}a_i a_j\xi_i\xi_j.
\]
Substituting cancels the constants beyond \(S_1\) and proves the claimed Walsh expansion. The random products \(\{\xi_i\xi_j:i<j\}\) have mean zero and are pairwise orthogonal in \(L^2\), since the \(\xi_j\) are independent fair signs. Squaring and averaging gives the displayed exact mean-squared error. In particular, the trace estimator is unbiased.

The risk is zero precisely when \(S_3=S_2(a_i+a_j)\) holds for **every** pair of nonzero diagonal entries. If there is only one nonzero entry, there are no such pairs. If there are exactly two, writing them as \(a,b\ne0\), this condition reduces to \(ab(a+b)=0\), so \(a=-b\). With at least three nonzero entries, comparing the conditions for pairs sharing one index shows all nonzero entries must equal a common \(a\ne0\); but then \(S_3/S_2=a\), while every pair sums to \(2a\), a contradiction. This completes the classification.

Finally, when all \(a_j=1\), the Walsh expansion equals \(-\tfrac2n\sum_{i<j}\xi_i\xi_j=1-(\sum_j\xi_j)^2/n\). Since \(\mathbb E(\sum_j\xi_j)^4=3n^2-2n\), its squared mean is \(2(n-1)/n\). For two coordinates the sum is either zero or has absolute value two, yielding the stated exact two-point distribution. Ordinary Hutchinson returns \(g^{\mathsf T}Ag=S_1\) for every diagonal matrix, proving the final comparison.

## Verification

The standalone file `verify.py` performs independent exact rational evaluations of the two residual-projector estimates and of the derived Walsh polynomial. It exhaustively evaluates 7,168 ordered Rademacher probe pairs across thirteen nonzero example diagonals in dimensions two through six, comparing the exact brute-force mean and squared error with the symbolic finite-sum formula. Additional exact checks cover the scalar-identity formula and the rank-based zero-risk criterion. Expected outcome: `VERIFY_OK 7168 exhaustive ordered probe pairs; exact mean, variance, equality, and classification checks`. This finite testing is supplementary; the all-dimensions result follows from the proof above.

## Relationship to prior work

Epperly, Tropp, and Webber introduce XTrace and its leave-one-out construction in equations (1.4)–(1.6), and derive a general relationship between the expected internal variance indicator and the pairwise correlation of basic estimates in Proposition 3.1. Their discussion acknowledges possible underestimation when the estimates are positively correlated. The present result identifies an explicit, entire diagonal-matrix class on which that correlation is **perfect**, gives the exact true risk and its complete zero-risk classification, and shows why the internal diagnostic is identically zero despite actual stochastic error. The source's general correlation relation is fully consistent with the result but does not itself exhibit or classify this samplewise-degenerate family. The Rademacher Hutchinson comparison uses the standard quadratic-form trace identity and does not claim any new property of Hutchinson's estimator.

## Limitations

The result concerns the minimal two-probe, four-matvec unnormalized XTrace estimator. It does not assert this pathology for more leave-one-out probes, non-diagonal inputs, Gaussian probes, residual-renormalized XTrace, XNysTrace, or arbitrary adaptive implementations. A zero internal indicator is not itself a formal probabilistic coverage guarantee; the contribution is the samplewise failure mode and exact actual risk. An equivalent specialized derivation elsewhere in the trace-estimation literature remains a priority risk; no independent audit has been performed.

## References

1. E. N. Epperly, J. A. Tropp, and R. J. Webber, *XTrace: Making the Most of Every Sample in Stochastic Trace Estimation*, arXiv:2301.07825, first posted 2023-01-19; equations (1.4)–(1.6), (3.1), Proposition 3.1, sections 2.3 and 5.6. https://arxiv.org/abs/2301.07825
2. E. N. Epperly, *Don't Use Gaussians in Stochastic Trace Estimation*, 2024-01-28, explanation of Rademacher, spherical, and Gaussian probe distributions. https://www.ethanepperly.com/index.php/2024/01/28/dont-use-gaussians-in-stochastic-trace-estimation/
3. A. Al Nahid, L. Serafin, and N. Mancuso, *traceax: a JAX-based framework for stochastic trace estimation*, preprint (2025), discussion of XTrace and supported probe distributions. https://pmc.ncbi.nlm.nih.gov/articles/PMC12338724/
