# Sharp three-to-one stationary-mode transition for symmetric ternary switching

## Finding
Consider an equal-relaxation, three-environment switching process whose environment \(S_t\in\{-1,0,1\}\) jumps from any state to each of the other two states at rate \(q>0\), while its scalar response obeys \(\dot X_t=k(S_t-X_t)\) with \(k>0\). Define \(a=q/k\). In its unique stationary law, \(X\) has an even density supported on \((-1,1)\):

\[
f_a(x)=\frac{\Gamma(3a)}{2^{2a-1}\Gamma(a)^3}
\int_{|x|}^{1}(u^2-x^2)^{a-1}(1-u)^{a-1}\,du,
\qquad 0<|x|<1.
\]

**Sharp complete classification:** If \(0<a<1/2\), the density diverges at each of the three environmental fixed points \(-1,0,1\), has one strict minimum in \((0,1)\), and by symmetry exactly one other minimum in \((-1,0)\), with no other extrema. If \(a\geq1/2\), it is strictly decreasing on \((0,1)\) and strictly increasing on \((-1,0)\), so the sole (possibly divergent) mode is at \(0\). In particular the complete-graph three-to-one peak transition occurs precisely at \(q=k/2\). At the boundary \(a=1/2\), the central peak diverges logarithmically but the density tends to \(1/(2\sqrt2)\) at each outer endpoint. This is a stationary-density modality theorem, not a finite-population stochastic-bifurcation theorem.

## Assumptions and scope
The three environmental states are symmetric and have **all-to-all**, not nearest-neighbour, switching: the generator is \(Q_{ij}=q\) for distinct \(i,j\), and \(Q_{ii}=-2q\). The relaxation rate \(k\) is common to all environments, the fixed points are equally spaced, no independent additive noise is present, and \(q,k\) are strictly positive. An affine change of position and a common time rescaling extend the statement to any three equally spaced fixed points and common restoring slope. In a large-population noisy-voter PDMP, three equispaced influencer configurations with common spontaneous-noise and herding parameters yield such a restoring flow after affine scaling, provided the influencer environment follows this complete-graph switching law. This is different from the line-graph switching law analyzed numerically in the motivating source.

For \(0<a<1/2\), the outer-edge asymptotic is
\[
f_a(x)\sim \frac{\Gamma(3a)}{2^a\Gamma(a)\Gamma(2a)}(1-|x|)^{2a-1}
\quad (|x|\uparrow1),
\]
and the central asymptotic is
\[
f_a(x)\sim\frac{\Gamma(3a)\Gamma(1/2-a)}{2^{2a}\sqrt\pi\,\Gamma(a)^2}|x|^{2a-1}
\quad (x\to0).
\]
At \(a=1/2\), \(f_{1/2}(x)=(2\pi)^{-1}\log(1/|x|)+O(1)\) as \(x\to0\), and \(f_{1/2}(x)\to1/(2\sqrt2)\) as \(|x|\uparrow1\). For \(a>1/2\), the central density is finite and the outer density vanishes with the displayed power.

## Proof
Introduce the simplex-valued exponentially filtered occupation weights \(W_i(t)\) of the environmental states \(i=1,2,3\), satisfying \(\dot W_i=k(\mathbf1_{\{S=i\}}-W_i)\) and \(\sum_iW_i=1\). The physical stationary coordinate is \(X=W_3-W_1\). The joint measure
\[
\mathbb P(S=i,W\in dw)=w_i\,\mathrm{Dirichlet}(a,a,a)(dw)
\]
is invariant. To check this, for every differentiable test family \(g_i\), the Dirichlet integration-by-parts identity is
\[
\int w_i(e_i-w)\cdot\nabla g_i\,d\mathrm{Dir}_a
=\int(3aw_i-a)g_i\,d\mathrm{Dir}_a.
\]
The switching part of the generator, integrated against the same measure, is \(q\sum_i\int(1-3w_i)g_i\,d\mathrm{Dir}_a\); this cancels the drift contribution because \(ka=q\). There is no residual boundary flux: every face contribution carries the vanishing factor \(w_j^a\) as the corresponding coordinate tends to zero. The autonomous environmental chain is irreducible, and two simplex trajectories subjected to the same environment contract at rate \(e^{-kt}\). The invariant law is therefore unique.

Projecting the Dirichlet density with \(u=W_1+W_3\), \(x=W_3-W_1\), \(W_2=1-u\), whose Jacobian is \(1/2\), gives the displayed integral and its normalization. Evenness is immediate. For \(x\in(0,1)\), write
\[
f_a(x)=C_a(1-x)^{2a-1}H_a(x),\qquad
H_a(x)=\int_0^1 t^{a-1}(1-t)^{a-1}
[t+(2-t)x]^{a-1}\,dt,
\]
with \(C_a=\Gamma(3a)/(2^{2a-1}\Gamma(a)^3)>0\). If \(1/2\le a<1\), both factors in this product are nonincreasing, and \(H_a\) is strictly decreasing, hence \(f_a\) is strictly decreasing. For \(a=1\) the density is \(1-x\); for \(a>1\), the original integral decreases strictly as \(x\) grows because the integration interval shrinks and its positive integrand decreases pointwise.

If \(0<a<1/2\), the function \(x\mapsto[t+(2-t)x]^{a-1}\) is log-convex on \((0,1)\) for every \(0<t<1\). Its positive weighted integral \(H_a\) is log-convex by Hölder's inequality. Since \((2a-1)\log(1-x)\) is strictly convex, \(\log f_a\) is strictly convex on \((0,1)\). The central and outer-edge asymptotics both diverge when \(a<1/2\), forcing a unique interior minimizer; strict log-convexity excludes all additional extrema. The edge asymptotic follows by setting \(u=x+(1-x)t\), and the center asymptotic by setting \(u=xs\) and evaluating a beta integral. At \(a=1/2\), the lower endpoint has an integrable logarithmic singularity. These calculations establish the sharp boundary and every stated equality case.

## Verification
The standalone `checker.py` independently evaluates rational stationary generator identities for six concentrations and all monomial multiindices of degree at most fifteen within coordinatewise limits, verifies the exact position variance \(\operatorname{Var}(X)=2/[3(3a+1)]\), checks the explicit triangular law \(f_1(x)=1-|x|\), and samples finite grids on either side of the modality transition. It passed 4677 assertions in the packaged run. Finite numerical grids are only supplementary diagnostics: uniqueness and the sharp threshold follow from the Dirichlet identity and strict log-convexity proof above.

## Relationship to prior work
Caligiuri and Galla (2023, arXiv:2305.19096v1, Sections III.3 and V.2 and Appendix A) derive the noisy-voter PDMP, treat an environmental **line** \(0\leftrightarrow1\leftrightarrow2\), report three-to-one multi-peak changes and numerically integrate the coupled stationary equations; they explicitly identify analytic multi-environment stationary laws as a further question. The present theorem does **not** claim novelty for those qualitative changes or for the standard Dirichlet distribution. It gives the exact stationary law, endpoint exponents, and proof of an exhaustive sharp modality threshold for the distinct symmetric **complete-graph** environment. General literature on Dirichlet random means explains why the law is structurally plausible; no priority claim is made for the Dirichlet-family identity itself.

## Limitations
The line-graph environmental chain in the motivating paper is not solved here. No theorem about arbitrary three-state switching matrices, nonequispaced attractors, finite-population demographic fluctuations, transient relaxation, or higher-dimensional nonlinear flow is asserted. Classical Dirichlet-mean theory may contain an implicit equivalent result for the projected density; publication-priority assessment requires further specialist verification. The independent audit of this claim has not been performed.

## References
1. A. Caligiuri and T. Galla, “Noisy voter models in switching environments,” arXiv:2305.19096v1 (first public 2023-05-30), https://arxiv.org/abs/2305.19096 ; full open text https://arxiv.org/html/2305.19096v2 .
2. S. F. Jarner and R. L. Tweedie, “Convergence rates and moments of Markov chains associated with the mean of Dirichlet processes,” *Stochastic Processes and their Applications* 101 (2002), 257–271, https://doi.org/10.1016/S0304-4149(02)00139-4 . Related Dirichlet-mean framework; not asserted to contain this modality classification.
3. I. Di Matteo and E. Orsingher, “Detailed probabilistic analysis of the integrated three-valued telegraph signal,” *Journal of Applied Probability* (2016), https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/detailed-probabilistic-analysis-of-the-integrated-threevalued-telegraph-signal/6F91D8D9727A2AE811B1F49BC82A579A . Different unweighted time-integral observable.
