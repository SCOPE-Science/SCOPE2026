# Three equilibria below the rumor reproduction threshold in a saturated fact-checking model

## Finding

For the four-compartment model of Mohamed (2026), there is a strictly positive parameter vector for which the reproduction number defined in that article is
\[
\mathcal R_0=\frac{102067}{117000}<1,
\]
yet **exactly two** strictly positive rumor-present equilibria exist in addition to the locally asymptotically stable rumor-free equilibrium. One of the positive equilibria is given entirely by rational numbers and is linearly unstable. The coexistence is robust under sufficiently small positive-parameter perturbations. In particular, the implication from \(\mathcal R_0<1\) to global attraction of the rumor-free equilibrium asserted in Theorem 3.3 of the source does not hold for the printed model.

## Assumptions and scope

The state consists of unaware, spreading, convinced, and debunked densities \((U,S,C,D)\) in the nonnegative orthant. The governing ordinary differential equations, as printed in equations (1)–(4) of the source, are
\[
\begin{aligned}
\dot U&=b-(\alpha _1 S+\alpha _2 C+\alpha _3D)U-dU,\\
\dot S&=(\alpha _1S+\alpha _2C+\alpha _3D)U-(d+h_1+h_2)S-\frac{\sigma _1S}{k_1+r_1S},\\
\dot C&=h_2S-(d+h_3)C-\frac{\sigma _2C}{k_2+r_2C},\\
\dot D&=\frac{\sigma _1S}{k_1+r_1S}+\frac{\sigma _2C}{k_2+r_2C}-dD.
\end{aligned}
\]
All fourteen parameters are positive. Specifically, take
\[
\begin{gathered}
b=28,\quad d=h_1=h_2=h_3=k_1=k_2=r_1=r_2=1,\\
\sigma _1=10,\quad \sigma _2=\frac52,\quad
\alpha _1=\frac{1577}{4000},\quad \alpha _2=\alpha _3=\frac1{1000}.
\end{gathered}
\]
The model's rumor-free equilibrium is \(E_0=(28,0,0,0)\). The total-density bound \(U+S+C+D\le b/d=28\) is satisfied by the explicitly exhibited positive equilibrium. These are illustrative mathematical rates, not calibrated intervention estimates.

## Proof

**Step 1: the published local reproduction number is subunit.** Put
\[
\eta _1=d+h_1+h_2+\frac{\sigma _1}{k_1},\qquad
\eta _2=d+h_3+\frac{\sigma _2}{k_2}.
\]
The next-generation expression from equations (19)–(21) in the source is
\[
\mathcal R_0=\frac{b}{d\eta _1}\left[\alpha _1+
\frac{\alpha _2h_2}{\eta _2}+
\frac{\alpha _3}{d}\left(\frac{\sigma _1}{k_1}+
\frac{\sigma _2h_2}{k_2\eta _2}\right)\right].
\]
Here \(\eta _1=13\), \(\eta _2=9/2\), and direct rational arithmetic gives \(\mathcal R_0=102067/117000\).

**Step 2: a first positive equilibrium.** Set
\[
E_1=\left(20,1,\frac14,\frac{11}{2}\right).
\]
With \(L=\alpha _1 S+\alpha _2C+\alpha _3D\), at \(E_1\) one has \(L=2/5\), \(\sigma _1S/(k_1+r_1S)=5\), and \(\sigma _2C/(k_2+r_2C)=1/2\). Thus the four derivatives equal, respectively,
\[
28-\frac75(20)=0,\quad 8-3-5=0,\quad
1-\frac12-\frac12=0,\quad 5+\frac12-\frac{11}{2}=0.
\]
The total population here is \(107/4<28\), so this equilibrium is in the biologically feasible region.

**Step 3: exact complete equilibrium census.** Every equilibrium with \(S=0\) has \(C=D=0\), and then \(U=28\). Conversely, at any equilibrium with \(S>0\), all four coordinates are positive. Write \(z=C>0\). The \(C\)- and \(D\)-equations and then the \(U\)-equation successively give
\[
S(z)=\frac{z(9+4z)}{2(1+z)},\qquad
D(z)=\frac{10S(z)}{1+S(z)}+\frac{5z}{2(1+z)},
\]
\[
L(z)=\frac{1577}{4000}S(z)+\frac{z+D(z)}{1000},\qquad
U(z)=\frac{28}{1+L(z)}.
\]
The remaining \(S\)-equilibrium equation is exactly \(H(z)=0\), where
\[
H(z):=\frac{28L(z)}{1+L(z)}-3S(z)-\frac{10S(z)}{1+S(z)}
=-\frac{z(4z-1)Q(z)}{P(z)},
\]
\[
\begin{aligned}
Q(z)={}&303168z^6+2586288z^5+8092284z^4+10628853z^3\\
&+3804560z^2-2085860z-477856,\\
P(z)={}&2(z+1)(4z^2+11z+2)\\
&\cdot(25264z^4+158680z^3+290103z^2+133162z+16000).
\end{aligned}
\]
Every factor of \(P(z)\) is positive for \(z>0\), and every positive root of \(H\) gives an admissible positive equilibrium by the displayed reconstruction. Descartes' rule of signs gives at most one positive root of \(Q\), counted with multiplicities. Since
\[
Q(1/4)=-561250<0,\qquad Q(1/2)=10802295/8>0,
\]
there is exactly one simple positive root \(z_\star\in(1/4,1/2)\). The other positive root of \(H\) is precisely \(z=1/4\); they are different. Therefore there are **exactly three nonnegative equilibria**: \(E_0\), \(E_1\), and the positive state reconstructed from \(z_\star\).

**Step 4: local types.** The exact characteristic polynomial at the rumor-free equilibrium is
\[
\det(\lambda I-J(E_0))=
\frac{(\lambda+1)(2000\lambda^3+14922\lambda^2+29955\lambda+14933)}{2000}.
\]
All coefficients of the cubic are positive and
\(14922\cdot29955-2000\cdot14933=417122510>0\).
The cubic Routh–Hurwitz criterion proves local asymptotic stability. At \(E_1\), the characteristic polynomial is
\[
\det(\lambda I-J(E_1))=
\frac{(\lambda+1)(1000\lambda^3+2615\lambda^2-3801\lambda-898)}{1000}.
\]
The cubic has a positive real zero by evaluation at \(0\) and \(2\), so \(E_1\) is unstable. Moreover \(\det J(E_1)=-449/500\ne0\), hence \(E_1\) is nondegenerate.

**Step 5: robustness.** Since \(\mathcal R_0<1\) strictly, the rumor-free equilibrium remains locally stable and subthreshold under sufficiently small parameter changes. By the implicit-function theorem, the nondegenerate positive equilibrium \(E_1\) persists, remaining strictly positive. The second positive equilibrium also persists: its scalar root \(z_\star\) is simple, the reconstruction denominators are positive, and the elimination is reversible. Thus the subthreshold multiplicity holds on an open set of strictly positive parameters, not just at an isolated numerical parameter selection.

## Verification

The accompanying `verify.py` uses only the Python standard library and exact rational arithmetic. It recomputes the source formula for \(\mathcal R_0\), checks all four equilibrium equations, proves the polynomial elimination identity by cross-multiplying rational functions, checks the signs and coefficient pattern of \(Q\), and recomputes both Jacobian characteristic polynomials through determinant evaluations. It prints `VERIFY_OK` when all checks pass. The existence and uniqueness of the second positive root use Descartes' rule plus the intermediate-value theorem; this is an exact infinite statement, not an extrapolation from numerical root-finding.

## Relationship to prior work

Mohamed's 2026 article supplies this exact model and the reproduction-number formula, but its Theorem 3.3 instead claims that the rumor-free equilibrium is globally asymptotically stable whenever \(\mathcal R_0<1\). The positive fixed points above contradict that global conclusion while agreeing with the article's local linear threshold. Earlier work established subthreshold multiple equilibria arising from saturated recovery in other epidemic models; the general phenomenon is not claimed as new here. The contribution is a complete exact subthreshold equilibrium census and robust explicit counterexample **for this four-compartment, dual-saturation, residual-transmission model with every rate strictly positive**.

## Limitations

The two positive equilibria do not establish bistability: \(E_1\) is unstable and no attracting positive state is asserted. Nor is a full global phase portrait proved. This is a statement about the exact published ODE, not an empirical assertion about fact-checking efficacy. Although relevant older saturated-recovery literature was compared by abstract, its full text was not available for exhaustive implication checking; that leaves a residual literature-overlap risk.

## References

1. M. Mohamed, “Dynamics and Control of a Social Rumor Spreading Model with Fact-Checking Strategies,” *Mathematical Structures and Computational Modeling* **2** (2026), 11–20; DOI: `10.65904/3083-1733.2026.2.2`, published April 13, 2026. Equations (1)–(4), (19), and Theorems 3.2–3.3.
2. J. Cui, X. Mu, and H. Wan, “Saturation recovery leads to multiple endemic equilibria and backward bifurcation,” *Journal of Theoretical Biology* **254** (2008), 275–283; DOI: `10.1016/j.jtbi.2008.05.015`.
3. P. van den Driessche and J. Watmough, “Reproduction numbers and sub-threshold endemic equilibria for compartmental models of disease transmission,” *Mathematical Biosciences* **180** (2002), 29–48; DOI: `10.1016/S0025-5564(02)00108-6`.
