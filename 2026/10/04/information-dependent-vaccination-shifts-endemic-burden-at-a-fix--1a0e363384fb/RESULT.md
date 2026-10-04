# Information-dependent vaccination shifts endemic burden at a fixed invasion threshold
## Finding
In the Fang–Liu–Du information-dependent SIRM model, fix the positive demographic, transmission, recovery, baseline-vaccination and vaccine-efficacy parameters with \(R_0>1\). Let \(I^*\) be the unique endemic infected coordinate. Then \(I^*\) is strictly decreasing in the information-dependent vaccination coefficient \(u_0\) and the information growth rate \(a\), and strictly increasing in the saturation coefficient \(u_2\) and the information decay rate \(b\). Moreover, as \(u_0\to\infty\), one has \(I^*\to0\) and \(u_0 I^*\to Cb/(a\sigma)\), where \(C=(p_0\sigma+\mu)(R_0-1)\), while \(R_0\) itself is unchanged. Thus absence of \(u_0,u_2,a,b\) from \(R_0\) does not imply absence of an endemic-burden effect. For every finite positive parameter choice with \(R_0>1\), the endemic infected coordinate remains positive; no monotonicity claim is made for transient peaks, convergence rates, or global-attractor properties.

The source computes
\[
R_0=\frac{\beta\Lambda}{(\gamma+\mu)(p_0\sigma+\mu)}
\]
and observes that the information-dependent parameters \(u_0,u_2,a,b\) do not enter this invasion threshold. Its endemic-equilibrium equation nevertheless contains all four parameters. The exact comparative statics below separate those two facts: they leave the threshold unchanged but move the endemic infected level in strict, parameter-specific directions.

## Assumptions and scope
All parameters satisfy \(\Lambda,\mu,\beta,\gamma,p_0,u_0,u_2,a,b>0\) and \(0<\sigma\le1\). Set \(p=p_0\sigma\) and \(e=a/b\). Assume \(R_0>1\), and define
\[
C=(p+\mu)(R_0-1)=\frac{\beta\Lambda-(p+\mu)(\gamma+\mu)}{\gamma+\mu}>0.
\]
For a constant state, the normalized information kernel has the same value as the infected state, so the delayed and unperturbed formulations have the same equilibrium relation. The statement concerns the endemic infected coordinate only. Stability hypotheses used elsewhere in the source are not needed for the equilibrium comparative statics.

## Proof
At an endemic equilibrium, the infected balance gives \(S^*=(\gamma+\mu)/\beta\), and the information balance gives \(M^*=eI^*\). Substitution into the susceptible balance yields exactly the source's equilibrium equation in the form
\[
F(I;u_0,u_2,e):=\beta I+\frac{e\sigma u_0 I}{1+eu_2I}-C=0.
\]
For \(I\ge0\),
\[
F_I=\beta+\frac{e\sigma u_0}{(1+eu_2I)^2}>0,
\]
while \(F(0)=-C<0\) and \(F(I)\to\infty\) as \(I\to\infty\). Hence there is exactly one positive root \(I^*\).

Implicit differentiation is therefore legitimate. Since
\[
F_{u_0}=\frac{e\sigma I}{1+eu_2I}>0,
\]
one has
\[
\frac{\partial I^*}{\partial u_0}=-\frac{F_{u_0}}{F_I}<0.
\]
Likewise,
\[
F_{u_2}=-\frac{e^2\sigma u_0I^2}{(1+eu_2I)^2}<0,
\qquad
\frac{\partial I^*}{\partial u_2}=-\frac{F_{u_2}}{F_I}>0.
\]
Treating \(e=a/b\) as the information gain-to-decay ratio gives
\[
F_e=\frac{\sigma u_0 I}{(1+eu_2I)^2}>0,
\qquad
\frac{dI^*}{de}=-\frac{F_e}{F_I}<0.
\]
Therefore
\[
\frac{\partial I^*}{\partial a}=\frac1b\frac{dI^*}{de}<0,
\qquad
\frac{\partial I^*}{\partial b}=-\frac{a}{b^2}\frac{dI^*}{de}>0.
\]
These signs are strict for the stated positive parameter range.

For the large-response limit, monotonicity in \(u_0\) shows that \(I^*(u_0)\) has a nonnegative limit. If that limit were positive, the term \(e\sigma u_0I^*/(1+eu_2I^*)\) would diverge, contradicting the fixed identity \(F(I^*)=0\). Hence \(I^*\to0\). Rewriting the same equation as
\[
C=\beta I^*+\frac{e\sigma(u_0I^*)}{1+eu_2I^*}
\]
and passing to the limit gives
\[
u_0I^*\longrightarrow\frac{C}{e\sigma}=\frac{Cb}{a\sigma}.
\]
Because \(R_0\) contains none of \(u_0,u_2,a,b\), this entire endemic-burden variation occurs at a fixed invasion threshold.

## Verification
The bundled `verify.py` reconstructs the source's numerical baseline using exact decimal inputs, solves the endemic equation by bracketed bisection, checks the four strict comparative-static directions under one-at-a-time parameter changes, verifies the equilibrium identity, and checks the large-\(u_0\) asymptotic numerically. The computation is only a reproducibility check; the universal signs follow from the analytic derivatives above.

At the source baseline \(\Lambda=22.22\), \(\mu=0.2\), \(\beta=0.003\), \(\gamma=0.1\), \(p_0=0.1\), \(\sigma=0.002\), \(u_0=0.5\), \(u_2=0.01\), \(a=0.2\), and \(b=0.55\), the exact threshold from the printed parameters is \(R_0=101/91\approx1.10989\), consistent with the source's rounded value \(1.11\).

## Relationship to prior work
Fang, Liu, and Du derive the endemic equation and prove existence and uniqueness for \(R_0>1\), and their simulations show that changing \(u_0\) and \(u_2\) changes infection dynamics. Their Remark 3.2 nevertheless infers from the absence of \(u_0,u_2,a,b\) in \(R_0\) that changing those parameters cannot realize disease control. The present statement identifies the exact limitation of that inference: the invasion threshold is unchanged, but the endemic infected coordinate changes strictly with every one of those four parameters, and can be made arbitrarily small by increasing \(u_0\) while keeping \(R_0>1\).

Earlier behavioral-vaccination models already establish the general principle that information can affect endemic behavior. Buonomo, d'Onofrio, and Lacitignola study a different SIR model with information-dependent vaccination and a Michaelis--Menten response, and later work on meningitis reports that information coverage can reduce an endemic infected level. Kumar, Srivastava, and Gupta analyze a different SVIR model with information-induced vaccination and saturated treatment. Those results prevent any claim that behavioral effects on endemicity are new in general. The contribution here is the source-specific four-parameter sign theorem and fixed-\(R_0\) asymptotic extracted from the 2026 SIRM equilibrium equation.

## Limitations
The result is an equilibrium theorem, not an eradication theorem. For every finite positive \(u_0,u_2,a,b\) with \(R_0>1\), the unique endemic root remains strictly positive. The proof does not show that larger \(u_0\) or \(a\) monotonically reduces every transient infection peak, nor that varying \(u_2\) or \(b\) preserves stability of the endemic equilibrium. It also does not compare intervention costs. Older information-vaccination literature contains related qualitative effects, so originality is limited to this exact model, its four simultaneous comparative statics, the asymptotic scaling, and the correction of the source-specific threshold interpretation.

## References
1. J. Fang, J. Liu, and Z. Du, “Dynamics of multiple time scale SIRM model with information-dependent vaccination,” *Discrete and Continuous Dynamical Systems - B* (2026), DOI 10.3934/dcdsb.2026090. Early access June 11, 2026.
2. B. Buonomo, A. d'Onofrio, and D. Lacitignola, “Global stability of an SIR epidemic model with information dependent vaccination,” *Mathematical Biosciences* 216 (2008), 9--16, DOI 10.1016/j.mbs.2008.07.011.
3. A. Kumar, P. K. Srivastava, and R. P. Gupta, “Nonlinear dynamics of infectious diseases via information-induced vaccination and saturated treatment,” *Mathematics and Computers in Simulation* 157 (2019), 77--99, DOI 10.1016/j.matcom.2018.09.024.
4. B. Buonomo et al., “Modeling the effects of information-dependent vaccination behavior on meningitis transmission,” *Mathematical Methods in the Applied Sciences* (2022), DOI 10.1002/mma.7808.
5. F. Centrone, A. Perchiazzo, and E. Salinelli, “Bifurcations in an SIR model with vaccinating behaviour based on lagged information depending on the incidence,” *Far East Journal of Mathematical Sciences* 143 (2026), 2993--3022, DOI 10.17654/0972087126165.
