# A sharp waning-dependent fairness reversal in disassortative booster allocation

## Finding

In the two-group contact model of Foutel-Rodier, Charpentier and Guérin, periodic boosters and exponential immunity waning produce a **unique resource threshold separating two opposite local allocation regimes** whenever contact is disassortative. Fix an equal-sized two-group population and cross-group contact parameter \(1<\alpha\le2\). Let each individual's susceptibility \(a\) time units after vaccination be \(\sigma(a)=1-e^{-\omega a}\), where \(\omega>0\). Let the mean rate of booster doses per person equal \(\omega u\), with \(u>0\), and let group-specific dimensionless dose rates be \(u(1+b/2)\) and \(u(1-b/2)\), \(-2\le b\le2\). The disease-free invasion eigenvalue \(\rho_\alpha(b)\) is an even function of the imbalance \(b\).

Set
\[
 s(u)=1-u(1-e^{-1/u}),\qquad Q(u)=\frac{s(u)s''(u)}{2[s'(u)]^2}.
\]
The function \(Q:(0,\infty)\to(0,1)\) is strictly increasing and onto. Therefore there is exactly one \(u_c(\alpha)>0\) satisfying
\[
 Q(u_c(\alpha))=\frac{\alpha-1}{\alpha}.
\]
At equal rates \(b=0\) the exact curvature is
\[
 \rho_\alpha''(0)=\frac{u^2}{4}\left(s''(u)-\frac{2(\alpha-1)}{\alpha}\frac{[s'(u)]^2}{s(u)}\right).
\]
Consequently, for every \(0<u<u_c(\alpha)\), fair allocation is a **strict local maximum** of invasion eigenvalue: a sufficiently small nonzero unequal allocation strictly *reduces* \(\rho\). For every \(u>u_c(\alpha)\), fair allocation is a **strict local minimum**: all sufficiently small nonzero unequal allocations strictly *increase* \(\rho\). At the threshold the second derivative vanishes; no assertion is made about its higher-order local geometry. For \(0<\alpha\le1\), fair allocation is a strict local minimum at every \(u>0\), agreeing with the known global assortative-allocation result.

For the maximally cross-group case \(\alpha=2\), \(u_c(2)=0.238036776718270\ldots\). A noninfinitesimal counterexample at \(u=0.1\) has fair \(\rho_2(0)=0.900004539992976\ldots\), whereas spending the same average dose budget entirely in one group gives \(\rho_2(2)=0.895180199401113\ldots\). Hence fair allocation need not minimize invasion in the disassortative regime.

## Assumptions and scope

Each group has population weight \(1/2\), equal total contact activity, and symmetric contact matrix
\[
 \Gamma=\begin{pmatrix}2-\alpha&\alpha\\\alpha&2-\alpha\end{pmatrix},\qquad 0<\alpha\le2.
\]
Vaccines reset susceptibility to zero. Each person is boosted exactly every \(1/(\omega u_i)\) units of time, independently phased across the population, with a uniform disease-free stationary time since last booster. The dimensionless rates \(u_i\) are nonnegative, and zero rate means no further vaccination and stationary susceptibility one. This deterministic-renewal setting is used for the **disease-free next-generation matrix**. The theorem classifies only local curvature around fair rates; the stationary spectral calculation is not a claim about global convergence of nonlinear epidemic trajectories or about finite-population eradication probability. The unvaccinated susceptibility equals one as a limit.

Under periodic boosting with rate \(\omega u_i\), mean disease-free susceptibility is
\[
 \Sigma_i=\omega u_i\int_0^{1/(\omega u_i)}(1-e^{-\omega a})\,da=s(u_i)
\]
for \(u_i>0\), and \(s(0)=1\). The two-group next-generation susceptibility matrix is
\[
 M_\alpha(b)=\begin{pmatrix}
 (1-\alpha/2)s_1&(\alpha/2)s_2\\
 (\alpha/2)s_1&(1-\alpha/2)s_2
 \end{pmatrix},\quad s_1=s(u(1+b/2)),\quad s_2=s(u(1-b/2)).
\]
Its Perron root \(\rho_\alpha(b)\) is the threshold multiplier; in the source epidemic model the formal endemicity criterion is \(R_0\rho_\alpha(b)>1\). For \(\alpha>0\) the matrix is irreducible at strictly positive rates and its Perron root is simple.

## Proof

**Renewal mean and eigenvalue.** Integrating the susceptibility over one deterministic renewal interval gives \(s\) above. With \(A=1-\alpha/2\) and \(B=\alpha/2\), the Perron root is the larger root of the characteristic quadratic, explicitly
\[
 \rho_\alpha(b)=\tfrac12\left(A(s_1+s_2)+\sqrt{A^2(s_1-s_2)^2+\alpha^2s_1s_2}\right).
\]
It is invariant under swapping \(b\) and \(-b\), so \(\rho'_\alpha(0)=0\). Write \(h=ub/2\), and expand \(s(u\pm h)=s\pm hs'+h^2s''/2+O(h^3)\). The sum is \(2s+h^2s''+O(h^4)\), the difference \(2hs'+O(h^3)\), and the product \(s^2+h^2(ss''-s'^2)+O(h^4)\). Expanding the positive square root, using \(A^2-B^2=1-\alpha\) and \(A+B=1\), yields
\[
 \rho_\alpha(b)=s(u)+\frac{u^2b^2}{8}\left[s''(u)-\frac{2(\alpha-1)}{\alpha}\frac{s'(u)^2}{s(u)}\right]+O(b^4).
\]
This gives the stated second derivative. For \(u>0\), direct differentiation yields
\[
 s'(u)=-1+(1+1/u)e^{-1/u}<0,\qquad s''(u)=u^{-3}e^{-1/u}>0.
\]
Thus \(\rho_\alpha''(0)\) has the sign of \(Q(u)-(\alpha-1)/\alpha\).

**Strict monotonicity and limits.** Let \(t=1/u>0\). Elementary algebra gives
\[
 Q(1/t)=\frac{t^2e^{-t}(t-1+e^{-t})}{2[1-(1+t)e^{-t}]^2}.
\]
Differentiating and simplifying gives
\[
 \frac{d}{dt}Q(1/t)=-\frac{tN(t)}{2(e^t-1-t)^3},
\]
where
\[
 N(t)=(t^2-4t+2)e^{2t}+(t^3+t^2+4t-4)e^t+2.
\]
The Maclaurin coefficients through degree five vanish. For every integer \(n\ge6\),
\[
 N^{(n)}(0)=(n-1)\left[2^{n-2}(n-8)+n^2-n+4\right]>0.
\]
At \(n=6\) and \(7\), the bracket equals respectively \(2\) and \(14\); for \(n\ge8\) both summands are nonnegative with a strictly positive polynomial term. Therefore the entire power series of \(N\) has nonnegative coefficients and a positive degree-six coefficient, implying \(N(t)>0\) for \(t>0\). Because \(e^t-1-t>0\), \(Q(1/t)\) strictly decreases with \(t\), hence \(Q(u)\) strictly increases with \(u\). As \(t\to\infty\), the exponential expression tends to zero; as \(t\downarrow0\), Taylor expansion gives limit one. Thus \(Q\) is a continuous strictly increasing bijection from \((0,\infty)\) to \((0,1)\).

For \(1<\alpha\le2\), the target \((\alpha-1)/\alpha\) is strictly between zero and one, giving the unique threshold by the intermediate value theorem. The second-derivative test proves the two strict local assertions. When \(0<\alpha\le1\), the target is nonpositive while \(Q>0\), proving strict positive curvature. No sign conclusion is inferred at equality \(u=u_c\).

**Concrete counterexample.** If \(\alpha=2\), then \(M=\begin{psmallmatrix}0&s_2\\s_1&0\end{psmallmatrix}\) and \(\rho_2(b)=\sqrt{s_1s_2}\). At \(u=1/10\), \(s(1/10)=9/10+e^{-10}/10\), whereas \(s(1/5)=4/5+e^{-5}/5\), and \(s(0)=1\). Squaring the two candidate eigenvalues confirms the strict inequality
\[
 s(1/5)s(0)<[s(1/10)]^2.
\]
Strictness is elementary without numerical approximation: since \(e^5>20\), one has \(s(1/5)<4/5+1/100=81/100\), while \([s(1/10)]^2>(9/10)^2=81/100\).

## Verification

The companion `verify.py` uses exact symbolic differentiation, checks the positive-series formula through order 32, compares the analytic curvature with centered numerical differences on 40 parameter combinations, and evaluates the \(\alpha=2\) boundary example and the unique threshold root. All checks passed. The exact positivity proof applies to every power-series coefficient beyond order five, not only those enumerated computationally. The deterministic renewal construction is analytic; no stochastic particle simulation or assertion of infinite-population dynamics is used as proof.

## Relationship to prior work

Foutel-Rodier, Charpentier and Guérin (2023 preprint; 2024 journal) derive precisely the two-group spectral threshold and fixed-dose allocation family. Their Proposition 6 establishes **global fair optimality only for assortative and well-mixed contacts**, \(0\le\alpha\le1\); it does not classify the disassortative \(\alpha>1\) case. The current theorem specializes the vaccination-period distribution to deterministic intervals and the waning curve to exponential, and supplies an exact unique *local* dose-rate transition for the omitted contact range.

Galeotti and Rogers (2013), *Strategic Immunization and Group Structure*, already show that concentrating **perfect one-shot immunization** in a group can be preferable with disassortative contacts. Delmas, Dronnier and Zitt (2023), *Optimal vaccination: various (counter) intuitive examples*, establish substantial eigenvalue comparisons for permanent perfect vaccination allocations. Neither fixed-coverage optimization directly determines the reversal at a unique **recurring-dose rate** in the present nonlinear waning setting. The discovery that unfair allocation can help is therefore not independently claimed as new; the exact waning-dependent transition is the proposed contribution.

## Limitations

This is a local stability-of-fairness statement for the *next-generation eigenvalue*, not a proof of globally optimal vaccine allocation or epidemic extinction. At the zero-curvature threshold the fourth-order sign is undetermined by this theorem. The populations are equally sized, the contact matrix is symmetric with equal activity, booster times are exactly periodic, vaccine-reset protection is complete, and susceptibility wanes exponentially. Different interval laws or waning curves may exhibit different or multiple transitions. An equivalent analytic threshold may exist in unindexed or inaccessible prior work. The governing epidemic paper describes the population endemicity criterion as heuristic rather than proving full nonlinear global convergence. Deterministic waiting is treated through the stationary renewal criterion, not through a full PDE regularity theorem for point-mass waiting times.

## References

1. F. Foutel-Rodier, A. Charpentier, H. Guérin. *Optimal Vaccination Policy to Prevent Endemicity: A Stochastic Model*. arXiv:2306.13633, version 1 dated 2023-06-23; Journal of Mathematical Biology, https://doi.org/10.1007/s00285-024-02171-z. In particular Sections 4.2, 5.3, 5.4, Proposition 6, and Equation (25).
2. A. Galeotti and B. W. Rogers. *Strategic Immunization and Group Structure*. American Economic Journal: Microeconomics 5(2), 1–32 (2013). https://doi.org/10.1257/mic.5.2.1. In particular Proposition 2 and discussion of disassortative groups.
3. J.-F. Delmas, D. Dronnier, P.-A. Zitt. *Optimal vaccination: various (counter) intuitive examples*. Journal of Mathematical Biology (2023). https://doi.org/10.1007/s00285-022-01858-5. In particular Theorem 4.2.
