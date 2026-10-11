# All-feedback endemic uniqueness and separate monotonicity in the prevalence-driven SIRCm system

## Finding

Consider the four-compartment, autonomous, prevalence-driven SIRCm epidemic system [1] on the population simplex \(\Omega=\{(S,I,R,C)\in[0,1]^4:S+I+R+C=1\}\). Let \(\mu,\alpha,\beta,\delta,\gamma>0\), \(\sigma\in[0,1]\), and independently \(\varepsilon_1,\varepsilon_2\in[0,\infty)\). **For every such parameter choice**, there is only the disease-free equilibrium if \(\beta\le\mu+\alpha\). If \(\beta>\mu+\alpha\), the disease-free equilibrium coexists with exactly one endemic equilibrium; the latter is strictly positive in all four coordinates. Its prevalence \(I^*\) is real-analytic in the two feedback coefficients, with

\[
\frac{\partial I^*}{\partial\varepsilon_1}>0,\qquad
\begin{cases}
\displaystyle\frac{\partial I^*}{\partial\varepsilon_2}>0,&0\le\sigma<1,\\
\displaystyle\frac{\partial I^*}{\partial\varepsilon_2}=0,&\sigma=1.
\end{cases}
\]

The inequalities include one-sided derivatives at zero feedback. In particular, equilibrium uniqueness and separate feedback monotonicity hold at intermediate feedback strengths, not only in the small/large regimes or on the diagonal of equal feedback strengths.

## Assumptions and scope

The model is precisely the **prevalence-driven** form of [1], so the feedback function equals the infected population fraction \(g(S,I,R,C)=I\), and the unforced contact parameter is constant. Define \(G_j(I)=1+\varepsilon_j I\), for \(j=1,2\). The equations are

\[
\begin{aligned}
\dot S&=\mu(1-S)-\beta SI+\gamma G_2(I)C,\\
\dot I&=\beta SI+\sigma\beta CI-(\mu+\alpha)I,\\
\dot R&=(1-\sigma)\beta CI+\alpha I-\mu R-\delta G_1(I)R,\\
\dot C&=\delta G_1(I)R-\beta CI-\mu C-\gamma G_2(I)C.
\end{aligned}
\]

No seasonality, time dependence of \(\beta\), or transmission-driven feedback \(g=SI\) is included. The theorem is about equilibria, not their local or global stability. Equilibria are considered only in the nonnegative unit-sum simplex.

## Proof

**Step 1: exclude endemic equilibria at or below threshold.** At any equilibrium with \(I>0\), the infected equation yields \(S+\sigma C=q\), where

\[
q=\frac{\mu+\alpha}{\beta}.
\]

For any point of \(\Omega\) with \(I>0\), \(S+\sigma C\le S+C<1\). Thus \(q<1\), or \(\beta>\mu+\alpha\), is necessary. If \(I=0\), the \(R,C\) subsystem reduces to a strictly dissipative positive linear chain with only \(R=C=0\) at equilibrium; the mass condition gives \(S=1\). Hence the disease-free state is always the unique boundary equilibrium. (The same conclusion for \(I=0\) follows by adding the stationary \(R,C\) equations: \(0=-\mu(R+C)-\gamma C\), so \(R=C=0\).)

**Step 2: solve the linear steady-state equations at fixed prevalence.** Assume \(\beta>\mu+\alpha\), put \(U=1-q>0\), and temporarily fix \(z=I>0\). Denote \(G_j=1+\varepsilon_j z\), and set

\[
\begin{aligned}
D(z)&=(\mu+\delta G_1)(\mu+\gamma G_2)+\beta z(\mu+\sigma\delta G_1),\\
K(z)&=\beta z+\mu+\gamma G_2+(1-\sigma)\delta G_1.
\end{aligned}
\]

All factors in \(D\) are nonnegative and the first product is strictly positive. The two linear equations \(\dot R=\dot C=0\) have the unique solution

\[
C(z)=\frac{\alpha\delta G_1 z}{D(z)},\qquad
R(z)=\frac{\alpha z(\beta z+\mu+\gamma G_2)}{D(z)}.
\]

The infected equation requires \(S(z)=q-\sigma C(z)\). The remaining mass condition \(S+z+R+C=1\) is therefore exactly

\[
H(z)=U,\qquad
H(z)=z+\frac{\alpha zK(z)}{D(z)}.
\tag{1}
\]

At a solution of (1), \(\dot I=\dot R=\dot C=0\). Conservation gives \(\dot S=-\dot I-\dot R-\dot C\) on the unit simplex, so the first equation also vanishes. Thus (1) parametrizes **all** endemic equilibria, with no loss of solutions.

**Step 3: prove strict monotonicity of the exact scalar equation.** Expand

\[
\begin{aligned}
D(z)&=d_0+d_1z+d_2z^2,\\
d_0&=(\mu+\delta)(\mu+\gamma),\\
d_1&=\delta\varepsilon_1(\mu+\gamma)+\gamma\varepsilon_2(\mu+\delta)+\beta(\mu+\sigma\delta),\\
d_2&=\delta\gamma\varepsilon_1\varepsilon_2+\beta\sigma\delta\varepsilon_1,\\
K(z)&=k_0+k_1z,\\
k_0&=\mu+\gamma+\delta(1-\sigma),\\
k_1&=\beta+\gamma\varepsilon_2+\delta(1-\sigma)\varepsilon_1.
\end{aligned}
\]

Direct differentiation gives

\[
H'(z)=1+\alpha\,
\frac{k_0d_0+2k_1d_0z+(k_1d_1-k_0d_2)z^2}{D(z)^2}.
\tag{2}
\]

Every displayed coefficient is nonnegative and \(d_0,k_0,k_1>0\). More strongly, the potentially delicate quadratic coefficient equals the following manifestly strictly positive expression:

\[
\begin{aligned}
k_1d_1-k_0d_2={}&\beta^2(\mu+\sigma\delta)\\
&+\beta\varepsilon_1\delta(1-\sigma)(\gamma+2\mu)\\
&+\beta\varepsilon_2\gamma[\delta(1+\sigma)+2\mu]\\
&+\varepsilon_1^2\delta^2(\gamma+\mu)(1-\sigma)\\
&+\varepsilon_1\varepsilon_2\delta\gamma\mu(1-\sigma)\\
&+\varepsilon_2^2\gamma^2(\delta+\mu)>0.
\end{aligned}
\tag{3}
\]

Consequently \(H'(z)>1\) for all \(z\ge0\), including arbitrary independent feedback coefficients. Since \(H(0)=0\) and \(H(U)>U\), continuity and strict monotonicity imply a unique \(z^*\in(0,U)\) satisfying (1). The formulas above give \(R(z^*)>0\), \(C(z^*)>0\), and \(z^*>0\). If \(\sigma=0\), then \(S=q>0\). If \(\sigma>0\), using \(D>\beta z\sigma\delta G_1\) gives \(\sigma C<\alpha/\beta\), so \(S=q-\sigma C>\mu/\beta>0\). Thus the unique solution is a strictly positive equilibrium. This proves the classification.

**Step 4: differentiate with respect to each feedback parameter.** For this step regard \(G_1,G_2\) as independent positive variables at a fixed \(z>0\). A direct quotient-rule calculation gives the **exact factorizations**

\[
\begin{aligned}
\frac{\partial}{\partial G_1}\frac KD
&=-\frac{\delta(\beta z+\gamma G_2+\mu)(\sigma\beta z+\gamma G_2+\sigma\mu)}{D^2}<0,\\[3pt]
\frac{\partial}{\partial G_2}\frac KD
&=-\frac{\delta\gamma G_1(1-\sigma)(\beta z+\delta G_1+\mu)}{D^2}\le0.
\end{aligned}
\tag{4}
\]

The second derivative is strictly negative exactly when \(\sigma<1\). Since \(\partial G_j/\partial\varepsilon_j=z\), one has \(\partial H/\partial\varepsilon_j=\alpha z^2\,\partial(K/D)/\partial G_j\). Because (2) establishes \(H_z>0\), implicit differentiation of \(H(I^*,\varepsilon_1,\varepsilon_2)=U\) yields

\[
\frac{\partial I^*}{\partial\varepsilon_j}
=-\frac{H_{\varepsilon_j}}{H_z},
\]

which proves every stated sign. For \(\sigma=1\), (4) shows \(H\) is independent of \(G_2\) at fixed \(z\), hence its uniquely determined root \(I^*\) is exactly independent of \(\varepsilon_2\). The root is simple for every finite parameter pair; the real-analytic implicit function theorem, including analytic extension to small negative feedback about each boundary point while retaining \(G_j>0\), proves the asserted analytic dependence on \(\varepsilon_1,\varepsilon_2\). \(\square\)

## Verification

`verify.py` is a standalone Python 3 and SymPy reproduction script in this package, with requirements recorded in `requirements.txt`. Run `python verify.py` from a directory containing the two files. It checks the stationary reconstruction, the exact quadratic coefficients in (2)–(3), both factorizations in (4), and 80 rational parameter tuples spanning all allowed endpoint cases for \(\sigma\), including zero and large independent feedback. Its output is `EXACT_SYMBOLIC_IDENTITIES=11`, `EXACT_RATIONAL_CASES= 80`, and `ALL_CHECKS_PASS`. The assertions over symbolic parameters are algebraic identity checks; the positivity arguments and universal quantifiers rest on (2)–(4), not on finite examples.

## Relationship to prior work

Ramírez-Gutiérrez, Lóczi, Muñoz-Moncayo and Ketcheson [1] introduced these two feedback mechanisms, proved endemic existence for general feedback, proved uniqueness in the weak and strong regimes, and obtained a diagonal common-feedback sufficient uniqueness bound for the prevalence-driven case (Section 4.1, Remark 4.4). Those results do not state unconditional, independent-two-parameter uniqueness or strict separate monotonicity. The identity (3) removes the possible nonmonotonicity of the scalar equilibrium equation in the intermediate regime; the factorizations (4) control distinct feedback channels.

The original SIRC model [2] is the \(\varepsilon_1=\varepsilon_2=0\) special case. The network SIRS theorem of Gatti and Como [3] addresses different, fixed-rate transitions without an infection-responsive intermediate cross-immune compartment. Classical monotone scalar implicit-function reasoning is used here but only after the SIRCm-specific positive-coefficient and factorization identities have been established. This comparison does not establish exhaustive priority over all potentially related epidemiological literature.

## Limitations

The theorem concerns existence, uniqueness, and equilibrium parameter dependence alone. It **does not assert local stability, global attraction, or absence of Hopf bifurcations**. It does not apply to transmission-driven \(g=SI\), time-dependent contact rates, nonpositive rate parameters, negative feedback coefficients, or additional infection compartments. Strict increase in \(\varepsilon_2\) fails at the permitted endpoint \(\sigma=1\); exact independence replaces it. Theoretical monotonicity is not a clinical or causal inference about real mutation rates. Independent scientific validation has not been performed.

## References

1. D. R. Ramírez-Gutiérrez, L. Lóczi, C. Muñoz-Moncayo, D. I. Ketcheson, *Compartmental epidemiological models with infection-driven immune escape*, arXiv:2610.01111v1 (first posted 2026-10-01), especially model (1), Section 4, Remark 4.4 and Appendix 8. https://arxiv.org/html/2610.01111v1
2. R. Casagrandi, L. Bolzoni, S. A. Levin, V. Andreasen, *The SIRC model and influenza A*, Mathematical Biosciences 200 (2006), 152–169. DOI:10.1016/j.mbs.2005.12.029.
3. G. Gatti, G. Como, *On the dynamic behavior of the network SIRS epidemic model*, arXiv:2604.21065 (2026). https://arxiv.org/abs/2604.21065
