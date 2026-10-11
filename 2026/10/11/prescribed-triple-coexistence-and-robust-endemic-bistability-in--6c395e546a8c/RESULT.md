# Prescribed triple coexistence and robust endemic bistability in a forest disease–fire system

## Finding
For the undelayed forest disease–fire model of Liu and Zhang [1], arbitrary three distinct positive susceptible-tree densities can be prescribed as **all** of its coexistence equilibria. A positive parameter realization exists for which the lower- and higher-density coexistence states are hyperbolic attracting equilibria while the intermediate coexistence state is a hyperbolic saddle. This bistability persists under sufficiently small independent perturbations of all seven parameters. It occurs even when the disease-free equation has exactly one positive tree-density equilibrium.

Formally, for any \(0<s_1<s_2<s_3\), any \(a>0\), and any \(\omega>0\), the construction and bounds below provide positive \(r,K,\beta,\alpha,\sigma,\mu\) such that precisely these three coexistence equilibria occur. In particular, disjoint nonempty open subsets of strictly positive initial states converge to two different endemic attractors. Neither the location of the entire basin boundary nor the global classification of all solutions is asserted.

## Assumptions and scope
The system is
\[\begin{aligned}
\dot S&=rS\left(1-\frac{S}{K}\right)-\frac{\beta S I}{I+\alpha}-\frac{\sigma S}{1+\omega S},\\
\dot I&=\frac{\beta S I}{I+\alpha}-\mu I,
\end{aligned}\]
where \(S\) denotes susceptible trees, \(I\) infected trees, and \(r,K,\beta,\alpha,\sigma,\omega,\mu>0\). A *coexistence equilibrium* has \(S>0\) and \(I>0\). A *sink* means a hyperbolic equilibrium with both eigenvalues in the open left half-plane; a *saddle* has eigenvalues of opposite sign. The theorem concerns the continuous-time, spatially homogeneous system (3.1) of [1], without diffusion, delays, stochastic forcing, or optimal control.

Fix \(0<s_1<s_2<s_3\) and write
\[e_1=s_1+s_2+s_3,\quad e_2=s_1s_2+s_1s_3+s_2s_3,\quad e_3=s_1s_2s_3,\quad P=\prod_{j=1}^3(1+\omega s_j).\]
Choose arbitrary \(a,\omega>0\), then choose \(K\) satisfying the strict inequalities
\[K>\max\left\{e_1+\frac1\omega+\frac{\omega e_3}{s_1},\ \frac P\omega\right\}.\]
Set
\[r=aK,\quad \beta=a\left(K-e_1-\frac1\omega\right),\quad \sigma=\frac{aP}\omega.\]
For each \(i=1,2,3\), define
\[\tau_i=1-\frac{a\omega e_3}{\beta s_i}>0,\qquad H_i=as_i\left(\frac{P}{(1+\omega s_i)^2}-1\right).\]
Choose
\[\mu>\max_{1\le i\le3}\frac{\max\{H_i,0\}}{\tau_i},\qquad \alpha=\frac{a\omega e_3}\mu.\]
All parameter choices are strictly positive; the inequalities are strict, not limiting equalities.

## Proof
**1. Exact nullcline factorization.** For a coexistence equilibrium, the infected equation gives
\[I(S)=\frac{\beta S}\mu-\alpha.\]
By construction, \(\beta s_i>a\omega e_3=\mu\alpha\) for all three prescribed values, so each \(I(s_i)>0\). Dividing the susceptible equation by \(S>0\) and inserting \(I(S)\) gives
\[F(S)=r\left(1-\frac SK\right)-\beta+\frac{\mu\alpha}S-\frac{\sigma}{1+\omega S}.\]
A direct multiplication by \(S(1+\omega S)\) and expansion of \(\prod(S-s_j)\) establishes the exact identity
\[\boxed{F(S)=-\frac{a\omega(S-s_1)(S-s_2)(S-s_3)}{S(1+\omega S)}.}\]
Indeed, the cubic numerator has coefficients \(-a\omega\), \(+a\omega e_1\), \(-a\omega e_2\), \(+a\omega e_3\), in descending powers; these follow from the displayed choices and \(P=1+\omega e_1+\omega^2e_2+\omega^3e_3\). Hence exactly the three prescribed distinct positive values solve the coexistence equation, and all have \(I>0\). The cubic degree excludes any fourth coexistence equilibrium.

**2. Hyperbolicity and stability.** Write \(f=\dot S\), \(g=\dot I\), and \(J\) for their Jacobian. At a coexistence point \((s_i,I(s_i))\),
\[g_I=-\mu\left(1-\frac{\mu\alpha}{\beta s_i}\right)=-\mu\tau_i<0,\qquad g_S+\frac\beta\mu g_I=0.\]
The derivative along the infected nullcline is \(\frac{d}{dS}f(S,I(S))=f_S+(\beta/\mu)f_I=s_iF'(s_i)\), so
\[\det J=g_I\big(f_S+(\beta/\mu)f_I\big)
=\frac{a\mu\omega\tau_i}{1+\omega s_i}\prod_{j\ne i}(s_i-s_j).\]
The determinant is positive for \(i=1,3\) and negative for \(i=2\). At an equilibrium, \(f=0\) also gives
\[f_S=s_i\left(-a+\frac{\sigma\omega}{(1+\omega s_i)^2}\right)=H_i,\quad\operatorname{tr}J=H_i-\mu\tau_i<0.\]
Consequently the first and third equilibria are hyperbolic sinks and the middle equilibrium is a hyperbolic saddle. The sinks have open neighborhoods of initial states with positive coordinates whose trajectories converge to them.

**3. Only one positive disease-free equilibrium.** Since \(K>P/\omega\), we have \(r=aK>\sigma=aP/\omega\). At \(I=0\), the strictly positive susceptible equilibria satisfy
\[Q(S)=r\left(1-\frac SK\right)(1+\omega S)-\sigma=0.\]
This quadratic has negative leading coefficient and positive constant \(r-\sigma\); its two real roots have negative product, so exactly one root is positive. Thus the two endemic sinks are not merely a restatement of alternative positive disease-free tree equilibria.

**4. Persistence.** All three coexistence points are strictly interior and have \(\det J\ne0\); hence the implicit function theorem continues them uniquely for sufficiently small independent changes of each of the seven parameters. Positivity and the strict signs of determinant and trace persist. Every positive coexistence equilibrium still satisfies a cubic obtained from the infected nullcline, so there are no additional positive coexistence equilibria nearby. The strict inequality \(r>\sigma\) also persists. This proves an open region of robust endemic–endemic bistability.

## Verification
The exact rational example is
\[(r,K,\beta,\alpha,\sigma,\omega,\mu)=\left(130,130,106,\frac{20}{53},126,1,106\right).\]
Here \((s_1,s_2,s_3)=(1,2,20)\), \(a=1\), \(P=126\), and the reduced function is identically
\[F(S)=-\frac{(S-1)(S-2)(S-20)}{S(1+S)}.\]
The exact coexistence equilibria are
\[E_1=\left(1,\frac{33}{53}\right),\quad E_2=\left(2,\frac{86}{53}\right),\quad E_3=\left(20,\frac{1040}{53}\right).\]
Their Jacobians, traces, and determinants are
\[\begin{array}{c|c|c|c}
&J&\operatorname{tr}J&\det J\\ \hline
E_1&\begin{pmatrix}61/2&-40\\66&-66\end{pmatrix}&-71/2&627\\
E_2&\begin{pmatrix}26&-20\\86&-86\end{pmatrix}&-60&-516\\
E_3&\begin{pmatrix}-100/7&-2\\104&-104\end{pmatrix}&-828/7&11856/7
\end{array}\]
The disease-free quadratic is \(Q(S)=-S^2+129S+4\), with exactly one positive zero. A self-contained Python 3 checker (`verify.py` in this package) evaluates the original vector field and its analytic Jacobian with exact rational arithmetic, reproduces the three matrices and their signs, and checks the reduced factorization at sample rational points. The general identity and quantifiers are proved algebraically above; finitely many checker evaluations are not substituted for that proof.

## Relationship to prior work
Liu–Zhang [1, Section 3, Lemma 1 and Theorem 4] derive a coexistence cubic, plot its possible turning behavior, and establish sufficient local-stability conditions for a coexistence state. **Neither merely having three algebraic roots nor bistability in other ecological models is claimed as new here.** The new assertion is a constructive realization of **any specified positive triple** as feasible coexistence densities in that unmodified system, with an alternating sink–saddle–sink classification, one positive disease-free equilibrium, and persistence on an open set of all parameters. The displayed exact example has \(r>\sigma\), outside the hypotheses \(r<\sigma\) used in that paper's Theorem 4.

Liu–Zhang [2] analyze a distinct tree–beetle system with fire feedback, not the infection-transfer equations above. Hoyer-Leitzel–Iams [3] obtain multiple stable tree–grass coexistence states in an **impulsive** savanna model, not two endemic sinks of the continuous disease–fire system. Lasslop and collaborators [4] obtain alternative tree-cover states in a global fire–vegetation model and a different conceptual feedback model; their result motivates the ecological question but does not imply the model-specific construction. Previously recorded analysis of the same Liu–Zhang article concerns a diffusion instability threshold at another parameter vector, not the coexistence multiplicity or local stability asserted here.

## Limitations
The construction proves mathematical feasibility for positive parameters, not empirical calibration or ecological realism of the numerical example. It establishes local asymptotic stability and nonempty open basins, but neither a complete basin boundary nor absence of periodic orbits or global convergence for every positive initial state. The theorem concerns the homogeneous ODE; adding diffusion can change spatial stability. Independent assessment has not been performed. Related prior-work searches cannot establish exhaustive absence of equivalent unpublished or unindexed statements.

## References
[1] X. Liu and C. Zhang, “Forest model dynamics analysis and optimal control based on disease and fire interactions,” *AIMS Mathematics* 9 (2024), 3174–3194, DOI: 10.3934/math.2024154, first published 2024-01-03. Full text: https://www.aimspress.com/aimspress-data/math/2024/2/PDF/math-09-02-154.pdf.

[2] X. Liu and C. Zhang, “Stability and Optimal Control of Tree-Insect Model under Forest Fire Disturbance,” *Mathematics* 10 (2022), 2563, DOI: 10.3390/math10152563; full article in *Recent Advances in Theory and Application of Dynamical Systems* (MDPI reprint), https://mdpi-res.com/bookfiles/book/7489/Recent_Advances_in_Theory_and_Application_of_Dynamical_Systems.pdf.

[3] A. Hoyer-Leitzel and S. Iams, “Impulsive fire disturbance in a savanna model: Tree-grass coexistence states, multiple stable system states, and resilience,” arXiv:2103.12132v2 (2021), https://arxiv.org/pdf/2103.12132.

[4] G. Lasslop et al., “Multiple stable states of tree cover in a global land surface model due to a fire–vegetation feedback,” *Geophysical Research Letters* (2016), DOI: 10.1002/2016GL069365, https://doi.org/10.1002/2016GL069365.
