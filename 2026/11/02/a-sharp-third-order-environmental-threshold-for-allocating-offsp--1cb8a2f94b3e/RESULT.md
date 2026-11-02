# A sharp third-order environmental threshold for allocating offspring to a weaker habitat

## Finding

A three-habitat population's optimal fixed offspring allocation can depend on the third-order joint occurrence of favorable environmental conditions even when all habitat means, variances, and pairwise correlations are identical. More precisely, in the model below there is a **complete sharp threshold** for when the lower-productivity habitat enters the unique growth-optimal allocation:

\[
\boxed{\quad b>\frac{a(3a+4)}{4(a+1)+ta^2}\quad.}
\]

Equality means exclusion. The observed first two joint moments alone cannot decide inclusion precisely when

\[
\frac{a(3a+4)}{(a+2)^2}<b\le\frac{a(3a+4)}{4(a+1)}.
\]

## Assumptions and scope

Let \(a>0\) and \(0<b<a\). At the beginning of each discrete generation, fractions \(w_i\ge0\) of the population are assigned to three habitats, with \(\sum_{i=1}^3w_i=1\). Every generation uses the *same* fractions and is followed by complete mixing. The reproductive multipliers within a generation are

\[
R_1=1+aX_1,\qquad R_2=1+aX_2,\qquad R_3=1+bX_3,
\]

where every environmental indicator \(X_i\) is Bernoulli with probability \(1/2\), and every distinct pair of indicators is independent. Across generations, the environmental triples are independent and identically distributed. Triple independence within a generation is **not** imposed. If \(N_n>0\) is the population at generation \(n\), then

\[
N_{n+1}=N_n\sum_{i=1}^3w_iR_{i,n}.
\]

The strong law of large numbers gives the almost-sure long-run logarithmic growth rate

\[
G(w)=\lim_{n\to\infty}\frac1n\log\frac{N_n}{N_0}
=\mathbb E\log\left(\sum_{i=1}^3w_iR_i\right).
\]

All logarithms are finite because the combined multiplier is at least \(1\). The optimization is over the entire closed allocation simplex, including strategies omitting a habitat. Nothing here asserts optimality under density regulation, migration costs, temporally correlated years, or adaptive annual allocation.

## Proof

**1. The complete moment fiber.** Set \(t=4\Pr(X_1=X_2=X_3=1)\). Marginal fairness and pairwise independence determine all eight state probabilities: states \((0,0,0),(0,1,1),(1,0,1),(1,1,0)\) each have mass \((1-t)/4\), and states \((0,0,1),(0,1,0),(1,0,0),(1,1,1)\) each have mass \(t/4\). Nonnegativity is equivalent to \(0\le t\le1\). Denote the endpoint laws by even parity and odd parity. Both have mean \(1/2\) per indicator and pairwise joint-success probability \(1/4\), so their entire mean vectors and covariance matrices agree.

**2. Strict concavity and symmetry.** For any nonzero tangent direction \(v\) with \(\sum v_i=0\), the second derivative of the objective is

\[
D^2G(w)[v,v]=
-\mathbb E\frac{(v\cdot R)^2}{(w\cdot R)^2}<0.
\]

Strictness follows directly from the four positive-probability states in either endpoint parity law. Under odd parity, the outcomes \((1,0,0),(0,1,0),(0,0,1)\) force \(v_1=v_2=v_3=0\) if \(v\cdot R\) vanishes on all outcomes. Under even parity, the states \((0,1,1),(1,0,1),(1,1,0)\) force \(a v_2+b v_3=a v_1+b v_3=a(v_1+v_2)=0\), again giving \(v=0\). Every mixture of these laws is also strictly concave. Therefore a unique optimum exists. The law is invariant under exchange of the first two habitats, so the unique optimum has \(w_1=w_2=(1-z)/2\), \(w_3=z\), for \(0\le z\le1\).

**3. Exact one-dimensional objective.** For the even and odd endpoint laws respectively, the log-growth functions are

\[
\begin{aligned}
G_E(z)&=\frac14\left[2\log\left(1+\frac a2+\left(b-\frac a2\right)z\right)
+\log(1+a-az)\right],\\
G_O(z)&=\frac14\left[\log(1+bz)
+2\log\left(1+\frac a2-\frac{az}{2}\right)
+\log(1+a+(b-a)z)\right].
\end{aligned}
\]

The missing fourth term in \(G_E\) is \(\log1=0\). Under the general feasible joint law, \(G_t(z)=(1-t)G_E(z)+tG_O(z)\). Direct differentiation gives

\[
G_t'(0)=\frac{b[4(a+1)+ta^2]-a(3a+4)}{4(a+1)(a+2)},
\qquad
G_t'(1)=\frac{2b-2a-ab}{4(1+b)}<0.
\]

As \(G_t\) is strictly concave, the unique maximizer is \(z=0\) exactly when \(G_t'(0)\le0\); if this derivative is positive, the derivative at \(z=1\) is negative and there is exactly one interior maximizing \(z\). Rearrangement proves the boxed inclusion criterion and its equality boundary. The critical value decreases strictly with \(t\) and ranges from

\[
b_E=\frac{a(3a+4)}{4(a+1)}
\quad\text{to}\quad
b_O=\frac{a(3a+4)}{(a+2)^2},
\]

where \(0<b_O<b_E<a\) for every \(a>0\). Thus below or at \(b_O\), inclusion is never optimal; above \(b_E\), it is always optimal; and in the stated intermediate interval, the unobserved third-order parameter can change the optimal habitat support.

**4. Exact witness.** For \(a=2\), \(b=3/2\), the inclusion criterion becomes \(t>1/3\). At \(t=0\) the maximizing allocation is \((1/2,1/2,0)\). At \(t=1\), differentiation yields the unique positive optimizer

\[
z_*=\frac{15-\sqrt{201}}6\approx0.1370921869,
\]

and the allocation is \(((1-z_*)/2,(1-z_*)/2,z_*)\). These two environments are indistinguishable by their marginal and pairwise productivity moments.

## Verification

The accompanying standard-library program `checker.py` reconstructs the eight shock probabilities, computes the endpoint derivatives directly from the enumerated four-state laws, compares them with the closed formulas for a finite exact-rational grid, checks strict negative one-dimensional curvature on the same grid, and checks the explicit sharp witness. Its exact computations are reproducible with `python3 checker.py`. The analytic proof, not the finite test grid, establishes all real-parameter statements.

## Relationship to prior work

Jansen and Yoshimura (1998) established the ecological importance of geometric-mean growth and risk-spreading between habitats, with a two-habitat offspring-allocation model. Schreiber (2012) analyzed stochastic habitat selection using continuous-time Brownian forcing parameterized by a covariance matrix, including habitat preferences under spatial correlation. Both motivate a higher-order-dependence question, but neither establishes this exact joint-law classification and weak-habitat inclusion threshold for non-Gaussian three-patch shocks. Cohen's foundational 1966 model introduced log-growth-oriented allocation in a variable environment; its general optimization perspective is acknowledged, not claimed as new.

For a related fixed-allocation comparison, an equal-share three-habitat model can have different growth rates under the same first two environmental moments. The **new statement here** is stronger in a different direction: the **support of the unique optimally chosen allocation** changes, and every allowable third-order dependence law has a sharp analytic classification.

## Limitations

This is a discrete-generation, infinitely well-mixed, positive-multiplier model with fair pairwise-independent binary environmental indicators and two equal strong habitats. It is not a theorem about arbitrary marginal probabilities, finite-population demographic extinction, density-dependent equilibrium, or real conservation decisions. The strength of the optimal allocation gain is not quantified statistically, and parameter estimation from finite data is not addressed. Complete historical priority against all portfolio and stochastic-demography literature is not independently established.

## References

1. Jansen, V. A. A. and Yoshimura, J. (1998). "Populations can persist in an environment consisting of sink habitats only." *PNAS* 95, 3696–3698. DOI: 10.1073/pnas.95.7.3696. Public date verified 1998-03-31. https://doi.org/10.1073/pnas.95.7.3696
2. Schreiber, S. J. (2012). "The Evolution of Patch Selection in Stochastic Environments." *The American Naturalist* 180, 17–34. DOI: 10.1086/665655. Electronically published 2012-05-17. https://schreiber.faculty.ucdavis.edu/wp-content/uploads/sites/568/2019/08/2012_schreiber_AmNat.pdf
3. Cohen, D. (1966). "Optimizing reproduction in a randomly varying environment." *Journal of Theoretical Biology* 12, 119–129. DOI: 10.1016/0022-5193(66)90188-3. Full text was not available for complete comparison; this reference establishes the general historical context. https://doi.org/10.1016/0022-5193(66)90188-3
