# An exact four-person epidemic mixing reversal and its sharp transmission threshold

## Finding

In a two-patch, four-person stochastic SIR epidemic with constant row-stochastic infectivity, increasing cross-patch transmission does **not** always increase the mean final outbreak size. At the completely cross-patch mixing endpoint, the directional derivative changes sign at the unique positive root \(b_*\) of
\[
5b^4-8b^3-32b^2-32b-16=0,
\qquad b_*\approx3.79173150932606.
\]
For \(b>b_*\), adding a small amount of *within-patch* contact while keeping the next-generation spectral radius fixed strictly **increases** mean outbreak size; for \(0<b<b_*\), it strictly decreases mean size. Because the derivative at zero cross-patch mixing is always positive, the mean outbreak size has an interior maximizer whenever \(b>b_*\).

Moreover, for the exact value \(b=4\), the mean final outbreak size has **exactly one** maximizer in the open interval of cross-patch mixing probabilities, at \(\varepsilon_*\approx0.994252187388925\). The maximizer is the unique zero in \((0,1)\) of the explicit degree-eight polynomial in the proof below. This is a finite-population, not a branching-process or deterministic-limit, result.

## Assumptions and scope

There are exactly two patches, each with two individuals. Each individual is susceptible, infected, or permanently removed. Initially all four are susceptible, and one uniformly random individual is infected. By exchange symmetry, it suffices to start from one infected and one susceptible individual in patch 1 and two susceptibles in patch 2.

Infected individuals recover independently at rate \(\gamma=1\). Writing \(b=\beta/\gamma>0\), transmission from an infected individual in patch \(i\) to a susceptible individual in patch \(j\) has rate \(\beta\varepsilon_{ij}/2\), where
\[
E(\varepsilon)=\begin{pmatrix}1-\varepsilon&\varepsilon\\ \varepsilon&1-\varepsilon\end{pmatrix},
\qquad 0\le\varepsilon\le1.
\]
Thus the infection propensity into patch \(i\) is \(bS_i[(1-\varepsilon)I_i+\varepsilon I_{3-i}]/2\), and its recovery propensity is \(I_i\). Contacts to removed or already infected individuals have no effect. The next-generation matrix at the initially susceptible disease-free population is \(bE(\varepsilon)\), whose spectral radius is always \(b\). No claim is made for larger patches, nonlinear incidence, or different recovery distributions.

Let \(G_b(\varepsilon)\) be the expected **total number ever infected**, including the initial infected individual, when the epidemic becomes extinct. Extinction is certain in this finite SIR system.

## Proof

For a transient state \(u=(s_1,i_1,s_2,i_2)\), with \(s_j+i_j\le2\), let \(F(u)\) be the expected number of *additional* infections before extinction. Put
\[
r_j(u)=\frac b2 s_j[(1-\varepsilon)i_j+\varepsilon i_{3-j}],\qquad
T(u)=r_1(u)+r_2(u)+i_1+i_2.
\]
For infection and recovery successor states \(u_j^+\) and \(u_j^-\), respectively, the first-event decomposition gives the exact triangular recursion
\[
F(u)=\frac{\sum_{j=1}^2\bigl[r_j(u)(1+F(u_j^+))+i_jF(u_j^-)\bigr]}{T(u)}
\quad(i_1+i_2>0),
\]
with \(F(u)=0\) when no infectives remain. Each transition decreases the nonnegative integer \(2(s_1+s_2)+(i_1+i_2)\) by exactly one, so this recursion terminates on finitely many states. It yields \(G_b(\varepsilon)=1+F(1,1,2,0)\). Since \(T(u)>0\) in every transient state, all expressions are rational functions with denominators nonzero on the stated physical range.

Exact substitution followed by differentiation (or differentiating the same recurrence at fixed endpoint) gives
\[
G_b(0)=\frac{2(b+1)}{b+2},\qquad
G_b'(0)=\frac{2b(2b^2+4b+1)}{(b+2)^2}>0,
\]
\[
G_b(1)=\frac{4b^4+25b^3+38b^2+28b+8}{(b+1)(b+2)^3},
\]
and
\[
G_b'(1)=-\frac{b\,[5b^4-8b^3-32b^2-32b-16]}{2(b+1)^2(b+2)^4}.
\]
The coefficient sequence of the displayed quartic has exactly one sign change. Descartes' rule of signs, its negative value at \(b=3\), and its positive value at \(b=4\), prove the existence and uniqueness of \(b_*\in(3,4)\) and the stated sharp endpoint sign change. For \(b>b_*\), \(G_b'(0)>0>G_b'(1)\); continuity then places at least one global maximizer in \((0,1)\).

For \(b=4\), the complete rational function simplifies to
\[
G_4(z)=\frac{8192z^6+10880z^5-11744z^4-23672z^3-12444z^2-2502z-135}
{9(2z-3)(2z+1)^2(2z+3)(4z+1)^2},\quad 0\le z\le1.
\]
Its derivative has the sign of
\[
Q(z)=22528z^8-17920z^7-74880z^6-68960z^5-11344z^4
+57600z^3+60840z^2+25542z+3969,
\]
because explicitly
\[
G_4'(z)=\frac{2Q(z)}{9(2z-3)^2(2z+1)^3(2z+3)^2(4z+1)^3}.
\]
Set \(t=z/(1-z)\). The transformed polynomial is
\[
(1+t)^8Q\!\left(\frac{t}{1+t}\right)
=-2625t^8+443650t^7+1786290t^6+2794698t^5
+2361056t^4+1181286t^3+350766t^2+57294t+3969.
\]
It has exactly one sign change in descending order, is positive at zero, and tends to negative infinity. Hence it has exactly one positive root; the bijection between \(t>0\) and \(0<z<1\) gives exactly one critical point of \(G_4\) in the physical open interval. As \(Q(0)=3969>0\) and \(Q(1)=-2625<0\), that point is the unique strict global maximum.

For an explicit exact witness, the fully cross-patch endpoint has \(G_4(1)=419/135\) whereas
\[
G_4(99/100)-G_4(1)=\frac{295591073}{32512225144680}>0.
\]
The pair of patches with one person each cannot exhibit this reversal: it has \(G_b(z)=1+bz/(1+bz)\), strictly increasing. Thus four individuals are minimal **within the equal-size two-patch family** for this effect; no stronger population-wide minimality is asserted.

## Verification

The included `verify.py` reconstructs the transient-state expectation by the exact first-event recursion, computes both endpoint derivatives independently by differentiated recursions, checks all rational identities and the Descartes coefficient certificate, and compares four rational mixing points to a separately implemented *individual-labelled* four-person CTMC. Run `python -m pip install -r requirements.txt` and `python verify.py`. The code requires only Python and SymPy. The exact rational difference displayed above is positive; numerical root approximations are illustrative and not used to establish uniqueness.

## Relationship to prior work

Ueki, Thompson, and Banaji (2026, arXiv:2601.13730v2) study stochastic epidemics on networked subpopulations and numerically illustrate increasing mean outbreak sizes with increasing cross-subpopulation leak. Their model's reaction scheme (equation (1)) and Appendix S2's symmetric matrices are used here; Appendix S2 concerns weak-coupling, large-subpopulation approximate final sizes rather than an exact four-person endpoint sign and interior optimum. The full publicly accessible HTML version, including its supporting appendices, was examined. The present result supplies a precise finite-population boundary to the monotonic qualitative trend, without contradicting their reported parameter studies.

Leibenzon and Assaf (2023, arXiv:2306.09024) prove a distinct large-population degree-heterogeneity effect on final epidemic size, not the finite two-patch cross-contact law. Ball, Mollison, and Scalia-Tomba (1997) and Ball and Neal (2002) establish general household/local-global epidemic frameworks and asymptotic theory; the material accessible during comparison did not establish the particular finite-CTMC quartic and unique mixing optimizer. Their broad frameworks are relevant antecedents, not grounds for a claim of general novelty in SIR mixing effects.

## Limitations

The result is an exact mathematical property of a four-person stochastic epidemic, not an empirical estimate of the effects of travel restrictions. At \(b=4\) the gain over fully cross-patch mixing is small (approximately \(1.98\times10^{-5}\) infections), although its sign and the exact uniqueness statement are rigorous. The general threshold controls the **derivative at the fully cross-patch endpoint**; it does not assert that \(G_b\) is globally monotone for every \(b\le b_*\), nor a unique maximizer for every \(b>b_*\). General finite-household final-size formulae may offer alternative derivations. Research priority and generalization beyond this sharply defined model require further independent scrutiny.

## References

1. M. Ueki, R. N. Thompson, M. Banaji, *Outbreak dynamics and population vulnerability in stochastic epidemic models on networks*, arXiv:2601.13730v2 (first publicly submitted 2026-01-20). https://arxiv.org/html/2601.13730v2
2. A. Leibenzon, M. Assaf, *Heterogeneity can markedly increase final outbreak size in the SIR model of epidemics*, arXiv:2306.09024 (2023). https://arxiv.org/abs/2306.09024
3. F. Ball, D. Mollison, G. Scalia-Tomba, *Epidemics with two levels of mixing*, Annals of Applied Probability 7 (1997), 46–89. https://doi.org/10.1214/aoap/1034625252
4. F. Ball, P. Neal, *A general model for stochastic SIR epidemics with two levels of mixing*, Mathematical Biosciences 180 (2002), 73–102. https://doi.org/10.1016/S0025-5564(02)00125-6
