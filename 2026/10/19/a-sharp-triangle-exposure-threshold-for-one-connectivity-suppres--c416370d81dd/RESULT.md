# A sharp triangle-exposure threshold for one connectivity-suppression window in signed social contagion

## Finding

In the random-sign mean-field social-contagion model of de Kemmeter, Gallo, Boncoraglio, Latora, and Carletti, increasing the mean number of pairwise contacts while holding the mean number of group contacts fixed can lower the stable positive adoption fraction. The set of distrust fractions for which this counterintuitive effect occurs is **either empty or one open interval**, never two separated intervals. A finite, unique, sharp triangle-exposure threshold determines which case holds. At threshold, the two ends of the interval coalesce; just above threshold, its width grows as the square root of the excess exposure.

Here is an exact all-rate formulation. Let \(\mu,\beta_1,\beta_2,\gamma_1>0\); let \(\gamma_2,\gamma_3,\gamma_4,\gamma_5\geq0\), with the original model's restrictions \(\gamma_1\geq\gamma_2\geq\gamma_3\) and \(\gamma_4\geq\gamma_5\). Fix mean triangle incidence \(\tau\geq0\), distrust fraction \(0<\eta<1\), and mean pairwise degree \(k>0\). Set

\[
U=\beta_1(1-\eta),\quad V=\beta_2\eta,\quad
\Gamma=\gamma_2+2\gamma_3,\quad s=\tau/\mu,
\]
\[
L=s\bigl(\gamma_1(1-\eta)^3+\Gamma\eta(1-\eta)^2\bigr),\quad
R=s\bigl(\gamma_4\eta^2(1-\eta)+\gamma_5\eta^3\bigr).
\]

The mean-field equation is

\[
\dot\rho=\rho\Bigl[-\mu+kU-\bigl(k(U+V)-\mu L\bigr)\rho-\mu(L+R)\rho^2\Bigr].\tag{1}
\]

For every \(k>\mu/U\), equation (1) has a unique equilibrium \(\rho_\star\in(0,1)\), which attracts all initially positive densities. Define, for \(q>0\),

\[
A(q)=(\beta_1+\beta_2q)^2(1+q)^3,
\]
\[
B(q)=\beta_1\beta_2\gamma_1q+
[\beta_1\beta_2\Gamma-\beta_1^2\gamma_4]q^2
-\beta_1^2\gamma_5q^3,
\]
\[
s_c=\min_{q>0:\,B(q)>0}\frac{A(q)}{B(q)}.
\tag{2}
\]

The minimum in (2) is finite, strictly positive, attained at **exactly one** \(q_c>0\), and gives the following complete classification in the supercritical domain \(k>\mu/[\beta_1(1-\eta)]\):

* If \(0\leq s<s_c\), the map \(k\mapsto\rho_\star\) is strictly increasing for every \(0<\eta<1\).
* If \(s=s_c\), it is strictly increasing except at the sole fraction \(\eta_c=q_c/(1+q_c)\), where it is exactly independent of \(k\).
* If \(s>s_c\), there are exactly two fractions \(0<\eta_-(s)<\eta_+(s)<1\). Increasing \(k\) increases \(\rho_\star\) outside the interval \((\eta_-,\eta_+)\), decreases it strictly inside, and leaves it exactly unchanged at both endpoints.

At either zero-response fraction, the common equilibrium for **all supercritical degrees** is

\[
\rho_\star=\frac{\beta_1(1-\eta)}{\beta_1(1-\eta)+\beta_2\eta}.
\tag{3}
\]

Write \(\Phi_s(q)=sB(q)-A(q)\). The two endpoints have the sharp onset law

\[
\eta_+(s)-\eta_-(s)
=\frac{2}{(1+q_c)^2}
\sqrt{\frac{2B(q_c)}{-\Phi_{s_c}''(q_c)}}\,
\sqrt{s-s_c}+O(s-s_c)\quad(s\downarrow s_c).
\tag{4}
\]

In particular, the onset exponent is universally one half, and the leading coefficient is strictly positive and finite.

## Assumptions and scope

Equation (1) is the **one-dimensional homogeneous mean-field closure** of the random, independently signed edge version of the 2023 signed-simplicial contagion model. At fixed \(\eta\), its triangle-class frequencies are proportional to \((1-\eta)^3\), \(3\eta(1-\eta)^2\), \(3\eta^2(1-\eta)\), and \(\eta^3\). The rates and sign restrictions above match that version. Degree comparisons vary \(k\), **not** \(\tau\), \(\eta\), or the rate constants. The theorem compares unique positive attracting equilibria only where the invasion condition \(kU>\mu\) holds. It does not give a uniform conclusion for the bistable or subcritical region, nor for exact stochastic dynamics on a finite simplicial complex.

For \(\tau=0\), definition (2) remains available through the positive infection rates, while the case \(s<s_c\) applies. The polynomial formulas concern arbitrary positive rate parameters; a particular finite network may impose additional feasibility restrictions on \(k\) and \(\tau\).

## Proof

**Existence and stability.** Let \(F(\rho)\) denote the bracket in (1). In the stipulated supercritical regime, \(F(0)=kU-\mu>0\) and \(F(1)=-\mu-kV-\mu R<0\). The leading quadratic coefficient is \(-\mu(L+R)<0\) because \(\gamma_1>0\) and \(0<\eta<1\). Therefore \(F\) has exactly one positive zero \(\rho_\star\in(0,1)\), at which \(F'(\rho_\star)<0\). The sign of \(\rho F(\rho)\) proves global attraction on \((0,1]\).

**Exact connectivity sign.** Implicit differentiation of \(F(\rho_\star)=0\) gives

\[
\operatorname{sgn}\frac{\partial\rho_\star}{\partial k}
=\operatorname{sgn}\bigl[U-(U+V)\rho_\star\bigr].
\]

Set \(h=U/(U+V)\). Direct cancellation of all degree-dependent terms yields

\[
\frac{F(h)}{\mu}=\frac{g(\eta)}{(U+V)^2},\qquad
 g(\eta)=-(U+V)^2+UVL-U^2R.
\tag{5}
\]

Because \(F\) is positive below its unique positive zero and negative above it, (5) implies

\[
\operatorname{sgn}\frac{\partial\rho_\star}{\partial k}=-\operatorname{sgn}g(\eta).
\tag{6}
\]

Equality \(g(\eta)=0\) makes \(h\) an equilibrium at **every** admissible degree, proving (3) and exact degree invariance.

**Two-zero bound.** Substitute \(q=\eta/(1-\eta)\). An exact rearrangement gives

\[
(1+q)^5g\Bigl(\frac{q}{1+q}\Bigr)=sB(q)-A(q)=\Phi_s(q).
\tag{7}
\]

The coefficients of \(q^0,q^3,q^4,q^5\) in \(\Phi_s\) are strictly negative (the coefficient of \(q^3\) includes the extra nonpositive term \(-s\beta_1^2\gamma_5\)). Only the coefficients of \(q^1\) and \(q^2\) can have either sign. In ascending-degree order the coefficient signs therefore have the pattern \((- ,*,*,-,-,-)\), with no more than two sign changes. Descartes' rule of signs implies that \(\Phi_s\) has at most **two positive roots counting multiplicity**. Its constant and leading coefficients are strictly negative, so \(\Phi_s\) is negative for \(q\) near zero and for large positive \(q\).

**Sharp exposure threshold.** Since \(B(q)=\beta_1\beta_2\gamma_1q+O(q^2)>0\) for sufficiently small positive \(q\), the domain in (2) is nonempty. The positive function \(A/B\) diverges at every boundary of that domain, including zero and any finite zero of \(B\), and diverges at infinity when the domain extends that far because \(A\) has degree five whereas \(B\) has degree at most three. Thus \(s_c\) is attained in the interior, is positive and finite. If \(s<s_c\), \(\Phi_s<0\) throughout \(q>0\). At \(s=s_c\), the minimizing point is an interior double root of \(\Phi_{s_c}\). Since there are at most two positive roots counted with multiplicity, this double root is unique and has exact multiplicity two. For \(s>s_c\), \(\Phi_s\) becomes positive at the minimizer but is negative near both endpoints, forcing exactly two distinct simple positive roots, with positivity precisely between them. Using (6) proves all three cases. If the minimizer were not unique, it would create four roots at threshold counted with multiplicity, a contradiction.

**Square-root onset.** At the unique double root, \(\Phi_{s_c}''(q_c)<0\), while \(\partial_s\Phi_s(q_c)=B(q_c)>0\). Taylor expansion and the implicit-function theorem after setting \(s-s_c=u^2\) give

\[
q_\pm(s)=q_c\pm\sqrt{\frac{2B(q_c)}{-\Phi_{s_c}''(q_c)}}\sqrt{s-s_c}+O(s-s_c).
\]

Applying the smooth map \(q\mapsto q/(1+q)\) proves (4). This local asymptotic complements, rather than replaces, the global two-zero argument.

**Exact admissible example.** Take \(\mu=\beta_1=\beta_2=\gamma_1=\gamma_2=\gamma_3=1\) and \(\gamma_4=\gamma_5=0\). Then

\[
g(\eta)=-1+s\eta(1-\eta)^3(1+2\eta),\quad
s_c=\frac{2500+3400\sqrt{10}}{2187}=6.059325123\ldots,
\]

with unique critical fraction \(\eta_c=1/\sqrt{10}\). At \(s=8\), the two crossings are \(\eta_-=0.159659252\ldots\) and \(\eta_+=1/2\). Indeed

\[
g(\eta)=-(2\eta-1)(8\eta^4-16\eta^3+4\eta^2+6\eta-1).
\]

The lower root belongs to the rational interval \((159/1000,160/1000)\). For degrees \(k=24\) and \(k=48\), both equilibria are supercritical at each of the fractions \(1/10,3/10,1/2,7/10\): the larger degree respectively gives **more, less, the same, more** equilibrium adoption. At the upper crossing both equilibria equal \(1/2\). The width-opening coefficient in (4) specializes to \(0.2714527704\ldots\).

## Verification

The accompanying `verification.py` uses Python 3 and SymPy. Running `python verification.py` checks (5), (7), the degree derivative, all fixed-sign polynomial coefficients, the exact critical value in the symmetric example, the crossover polynomial factorization, a rational isolating interval for the lower crossing, and degree-order comparisons at four distinct distrust fractions. It also checks the predicted square-root coefficient numerically near the critical exposure. These computations support the algebra and example; the all-parameter result rests on the analytical root-count and bifurcation proof above.

## Relationship to prior work

The exact homogeneous random-sign mean-field equation and the degree-independent *crossing condition* (5) were derived by de Kemmeter et al. (2023 preprint; 2024 journal article), including their Appendix B, Eq. (13). Those are **established inputs, not novel claims**. Their displayed examples exhibit a degree-response reversal at one crossing. The additional contribution proved here is the all-admissible-rate **two-crossing ceiling**, the **unique sharp triangle-exposure onset criterion**, the **square-root opening law**, and a two-crossing realization for the complete supercritical degree comparison. An isolated crossing equation does not by itself establish these quantified global facts.

Iacopini et al. (2019) establish higher-order contagion and bistability without negative-edge recovery; in that trust-only setting, the competing pairwise effects that generate the present intermediate-distrust degree-suppression window are absent. Cinardi and Bertotti (2026) study an irreversible adoption model with external influence and adoption times rather than the reversible signed-distrust equilibrium equation (1). Mueller and Ramkumar (2023) use a different agent-based signed threshold-diffusion mechanism; available abstract-level information does not establish a covering theorem. No matching theorem was identified in the targeted literature and mathematical-record searches, but that is not proof of publication priority.

## Limitations

The theorem concerns a homogeneous deterministic closure, not finite-network stochastic extinction, temporal changes of signed links, or arbitrary correlations in triangle signs. Physical realizability may restrict degree and triangle-density combinations. All degree comparisons require the positive-invasion regime and hold only while varying degree with triangle exposure fixed; they do not imply monotonicity when triangle exposure co-varies with degree. The source's crossing identity makes the result a close structural extension, so independent literature review is still needed to exclude an equivalent published polynomial-root or bifurcation classification. Independent scientific validation has not been performed.

## References

1. J.-F. de Kemmeter, L. Gallo, F. Boncoraglio, V. Latora, T. Carletti, "Complex contagion in social systems with distrust," arXiv:2305.03879v1 (posted 6 May 2023); *Advances in Complex Systems* 27, 2440001 (2024), doi:10.1142/S0219525924400010. Sections III–IV and Appendix B.
2. I. Iacopini, G. Petri, A. Barrat, V. Latora, "Simplicial models of social contagion," *Nature Communications* 10, 2485 (2019), doi:10.1038/s41467-019-10431-6.
3. N. Cinardi, M. L. Bertotti, "Trust, distrust and higher-order interactions. What is needed for ideas adoption in a connected society," *Chaos, Solitons & Fractals* 202, 117584 (2026), doi:10.1016/j.chaos.2025.117584.
4. M. Mueller, S. Ramkumar, "Signed networks — The role of negative links for the diffusion of innovation," *Technological Forecasting and Social Change* 192, 122575 (2023), doi:10.1016/j.techfore.2023.122575.
