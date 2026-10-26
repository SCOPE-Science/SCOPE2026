# Sharp two-row catastrophic-tail transition in Gaussian forward-only reconstruction

## Finding

Fix an integer \(q\ge3\). Consider the Gaussian forward-query rowwise least-squares algorithm described below, applied to two rows with known one-dimensional but potentially different row spaces. If the known unit directions \(v_1,v_2\) have correlation \(\rho=v_1^{\mathsf T}v_2\), and the two row residuals share a common unit direction orthogonal to both known directions, then the individual squared reconstruction-coefficient errors \(Y_1,Y_2\) have the same distribution for every \(\rho\), but their simultaneous extreme-event probability undergoes an exact phase transition:

\[
\lim_{t\to\infty}t^q\Pr(Y_1>t,\,Y_2>t)
=\frac{K_q}{(1-\rho^2)^{q/2}},\qquad |\rho|<1,
\]

where

\[
K_q=\frac{4\,\Gamma((q+1)/2)^2\Gamma(3q/2)}
{\pi\,\Gamma(q+1)^2\Gamma(q/2)}>0.
\]

When \(|\rho|=1\), the two errors instead coincide exactly and

\[
\lim_{t\to\infty}t^{q/2}\Pr(Y_1>t,\,Y_2>t)
=C_q,\quad C_q=\frac{\Gamma((q+1)/2)}{\sqrt\pi\,\Gamma(q/2+1)}.
\]

Each marginal has \(\Pr(Y_i>t)\sim C_q t^{-q/2}\) and \(\mathbb E Y_i=1/(q-2)\), irrespective of the row-space angle. For \(|\rho|<1\), the simultaneous upper tail has exponent \(q\), versus exponent \(q/2\) at exact alignment. Moreover, even when \(\rho=0\), the two rare events are not asymptotically independent in the product-probability sense:

\[
\lim_{t\to\infty}\frac{\Pr(Y_1>t,Y_2>t)}{\Pr(Y_1>t)\Pr(Y_2>t)}
=\frac{q^2\Gamma(q/2)\Gamma(3q/2)}{\Gamma(q+1)^2}>1.
\]

For example, when \(q=3\), \(C_3=4/(3\pi)\) and \(K_3=35/(24\pi)\). Thus orthogonal row spaces still carry a joint tail \(35/(24\pi)t^{-3}\), whereas coincident spaces give \(4/(3\pi)t^{-3/2}\). The divergence of the nonaligned leading coefficient as \(|\rho|\uparrow1\) makes the limits in threshold and alignment nonuniform.

## Assumptions and scope

Let \(n\ge3\). Take unit vectors \(v_1,v_2,w\in\mathbb R^n\) with \(w\perp v_1\), \(w\perp v_2\), and \(v_1^{\mathsf T}v_2=\rho\in[-1,1]\). Fix any real \(a_1,a_2\), and form the \(2\times n\) matrix whose row \(i\) is \(a_i v_i^{\mathsf T}+w^{\mathsf T}\). The allowed row space for that row is \(\operatorname{span}\{v_i\}\). Its exact orthogonal projection is \(a_i v_i^{\mathsf T}\), and its unmodeled residual is \(w^{\mathsf T}\) of squared norm one.

Draw one shared \(n\times q\) matrix \(G\) of independent standard real Gaussian entries. Query only the forward action \(AG\). For each row separately, fit its coefficient by least squares against \(G^{\mathsf T}v_i\); the fitted row is \(\widetilde a_i v_i^{\mathsf T}\). Define \(Y_i=(\widetilde a_i-a_i)^2\). Thus \(Y_i\) is exactly the excess squared Euclidean row-approximation error over the optimal squared residual \(1\). All statements concern fixed finite \(q\), fixed \(\rho\), exact arithmetic, and a tail threshold \(t\to\infty\).

## Proof

**1. Reduction to three jointly Gaussian sketch vectors.** Put \(g_i=G^{\mathsf T}v_i\in\mathbb R^q\) for \(i=1,2\), and \(h=G^{\mathsf T}w\). Least squares with its almost-surely nonzero regressor gives

\[
\widetilde a_i-a_i=e_i=\frac{h^{\mathsf T}g_i}{\|g_i\|^2},\qquad Y_i=e_i^2.
\]

The vector \(h\sim N(0,I_q)\) is independent of \((g_1,g_2)\), and the latter is centered Gaussian with block covariance \(\begin{psmallmatrix}I_q&\rho I_q\\\rho I_q&I_q\end{psmallmatrix}\). Hence \(g_2=\pm g_1\) almost surely when \(\rho=\pm1\).

**2. Exact marginal law.** Given \(g_i\), the numerator \(h^{\mathsf T}g_i\) is centered normal with variance \(\|g_i\|^2\). Gaussian rotational symmetry makes its standardization independent of \(\|g_i\|\). Therefore

\[
e_i\ \overset d=\ \frac{Z}{\sqrt U}=\frac{T_q}{\sqrt q},
\]

where \(Z\) is standard normal, \(U\sim\chi_q^2\), they are independent, and \(T_q\) is Student with \(q\) degrees of freedom. Thus \(Y_i\overset d=F_{1,q}/q\), proving \(\mathbb E Y_i=1/(q-2)\). Using the \(\chi_q^2\) distribution near zero, or equivalently the beta-prime tail, proves \(\Pr(Y_i>t)\sim C_q t^{-q/2}\) with the stated \(C_q\).

**3. Nonaligned joint limit.** Assume \(|\rho|<1\), and set \(u_i=\sqrt t\,g_i\). Given \(h\), the two strict exceedance conditions are exactly

\[
|h^{\mathsf T}u_i|>\|u_i\|^2\quad(i=1,2).
\]

They force \(\|u_i\|<\|h\|\) by Cauchy--Schwarz. The joint \(2q\)-dimensional Gaussian density of \((g_1,g_2)\) gives, after this change of variables, an integral multiplied by

\[
t^{-q}(2\pi)^{-q}(1-\rho^2)^{-q/2}
\]

and an exponential factor bounded above by one, converging pointwise to one. The remaining integration domain is inside two balls of radius \(\|h\|\). Its volume is bounded by a constant times \(\|h\|^{2q}\), which is integrable for Gaussian \(h\). Dominated convergence therefore gives

\[
\lim_{t\to\infty}t^q\Pr(Y_1>t,Y_2>t)
=(2\pi)^{-q}(1-\rho^2)^{-q/2}\,\mathbb E[J_q(h)^2],
\]

where \(J_q(h)=\int_{\mathbb R^q}\mathbf1\{|h^{\mathsf T}u|>\|u\|^2\}\,du\). In polar coordinates, the permitted radius in direction \(\theta\in S^{q-1}\) is \(|h^{\mathsf T}\theta|\). Hence

\[
J_q(h)=\frac{\|h\|^q}{q}\int_{S^{q-1}}|\theta_1|^q\,d\theta
=\frac{2\pi^{(q-1)/2}\Gamma((q+1)/2)}{q\Gamma(q)}\|h\|^q.
\]

The radial moment \(\mathbb E\|h\|^{2q}=2^q\Gamma(3q/2)/\Gamma(q/2)\) yields the explicit \(K_q\) above. All interchange steps have an integrable dominating function for every integer \(q\ge3\).

**4. Aligned boundary and non-product dependence.** At \(|\rho|=1\), \(g_2=\pm g_1\), so \(e_2=\pm e_1\) and \(Y_2=Y_1\), giving the different tail exponent \(q/2\). For \(|\rho|<1\), division by both marginal tails produces the stated ratio. At \(\rho=0\) this ratio is strictly greater than one because, conditional on \(h\), the two events are independent but their conditional leading coefficient is a positive constant times \(\|h\|^q\), a nonconstant random variable. Its second moment is strictly larger than the square of its first moment.

## Verification

Run `python verify_joint.py` with NumPy and SciPy installed. The script reconstructs the rowwise least-squares outputs directly from shared Gaussian queries, checks the marginal beta-prime representation against an independent \(F\)-distribution implementation, tests the aligned equality, and uses an importance-sampled small-ball integral to compare the nonaligned joint tail against the analytical coefficient. In the recorded run, 2,759 assertions passed, including 450,000 importance-sampling draws per grouped parameter calculation. These finite numerical checks supplement but do not replace the proof.

## Relationship to prior work

Gallmeier and Otto [1], Algorithm 1 and Theorem 1, develop the forward-only known-row-subspace Gaussian reconstruction and prove an expected squared Frobenius-error bound; they do not state this two-row joint-tail phase transition. Amsel and collaborators [2] analyze the earlier coordinate-sparsity version and derive an expected-error result and Markov high-probability guarantee, without the shared-residual, heterogeneous-row-space joint exponent. Browne and Andrews [3], following Ahfock and collaborators, derive Student-family laws for Gaussian-sketch regression estimators; the one-row marginal Student law here is therefore classical and is not claimed as original. The claim here is the *joint* fixed-angle asymptotic, exact coefficient, aligned singular boundary, and surviving excess joint risk even at orthogonal row spaces. General multivariate Student and Gaussian small-ball probability results inform the proof but were not identified as containing the same algorithm-specific sharp two-row comparison.

## Limitations

The theorem is deliberately restricted to two rows, one known direction per row, identical unit residual directions perpendicular to both known directions, one shared Gaussian sketch, and exact arithmetic. The constants are fixed-angle asymptotics, not nonasymptotic error guarantees uniform as \(|\rho|\uparrow1\). A result for arbitrary residual correlations, higher-dimensional known row spaces, non-Gaussian queries or full operator-learning dynamics is not proved. Earlier work in specialized multivariate ratio-tail theory may contain broader coverage; historical novelty remains a separate risk and independent validation has not been performed.

## References

1. Esther Gallmeier and Samuel E. Otto, *Efficient Approximation of Structured Linear Operators using Randomized One-Sided Queries*, arXiv:2610.07513v1, first posted 2026-10-05. https://arxiv.org/html/2610.07513v1
2. N. Amsel and collaborators, *Fixed-sparsity matrix approximation from matrix-vector products*, arXiv:2402.09379, 2024. https://arxiv.org/abs/2402.09379
3. Ryan P. Browne and Jeffrey L. Andrews, *Statistical inference for sketching algorithms*, arXiv:2306.03593, 2023. https://arxiv.org/abs/2306.03593
