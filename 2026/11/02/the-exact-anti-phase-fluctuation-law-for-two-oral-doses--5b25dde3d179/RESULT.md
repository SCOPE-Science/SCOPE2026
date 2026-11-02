# The exact anti-phase fluctuation law for two oral doses

## Finding

Fix a period \(T>0\), positive absorption and elimination rates \(a,b>0\), and positive dose amounts \(w_1,w_2>0\). Deliver the first dose at time \(0\) and the second at time \(\delta\), repeated every \(T\) time units, with \(0\le\delta\le T\). In the linear one-compartment oral-absorption model, the unit-dose concentration impulse response is
\[
h_{a,b}(t)=\begin{cases}
\dfrac{ab}{b-a}(e^{-at}-e^{-bt}),& t\ge0,\ a\ne b,\\
a^2te^{-at},&t\ge0,\ a=b,\\
0,&t<0.
\end{cases}
\]
These expressions are normalized to unit total concentration-time exposure; physical bioavailability and volume scaling can be restored multiplicatively.

Let \(G(t)=\sum_{k\in\mathbb Z}h_{a,b}(t-kT)\), let \(C_\delta(t)=w_1G(t)+w_2G(t-\delta)\), and let
\[
J(\delta)=\int_0^T\left(C_\delta(t)-\frac{w_1+w_2}{T}\right)^2\,dt.
\]
For every choice of the positive parameters, \(J\) has its **unique phase minimum modulo \(T\)** at \(\delta=T/2\). More sharply, \(J(\delta)\) is strictly increasing as the circular distance \(|\delta-T/2|\) increases from zero to \(T/2\), including when the two rates coincide and when dose amounts are unequal.

For distinct rates, put \(L=T/2\), \(d=|\delta-L|\), and
\[
F_r(d)=\frac{\cosh(rd)-1}{r\sinh(rL)}.
\]
The exact global phase-penalty formula is
\[
\boxed{J(\delta)-J(L)=
\frac{w_1w_2a^2b^2}{(a+b)(b-a)}\bigl(F_a(d)-F_b(d)\bigr).}
\]
For equal rates \(a=b\), the right-hand side is defined by its continuous limit, which is explicitly
\[
\boxed{J(\delta)-J(L)=-\frac{w_1w_2a^3}{2}\left.\frac{\partial F_r(d)}{\partial r}\right|_{r=a}.}
\]
In particular, a small displacement \(d\) from the optimal phase has the sharp penalty
\[
J(L+d)-J(L)=K_{a,b,T,w_1,w_2}\,d^2+O(d^4),
\]
where, when \(a\ne b\),
\[
K_{a,b,T,w_1,w_2}=\frac{w_1w_2a^2b^2}{2(a+b)(b-a)}
\left(\frac{a}{\sinh(aT/2)}-\frac{b}{\sinh(bT/2)}\right)>0,
\]
and at \(a=b\) the same coefficient is defined by the corresponding continuous limit. Thus the result provides both a global optimum and an exact local timing-tolerance constant.

## Assumptions and scope

The model is deterministic and time-invariant, with instantaneous amounts entering an absorption compartment, first-order transfer and first-order elimination, a fixed period, two positive dose amounts that are not varied in optimization, and no food, transit delay, saturation, nonlinear clearance, distribution, time-varying rates, or adherence uncertainty. The objective is the integrated squared deviation from the **periodic steady-state mean**, not the maximal concentration, trough, therapeutic-window risk, or transient concentration. The mean is \((w_1+w_2)/T\), independently of phase. The input at \(\delta=0\) or \(T\) represents coincident administrations, allowed as a boundary comparison.

## Proof

**1. Periodic concentration.** Since \(a,b>0\), the response is nonnegative and integrable, and both the periodic sum \(G\) and its derivative converge uniformly between dosing times. Direct integration gives \(\int_0^\infty h_{a,b}(t)\,dt=1\). Periodizing the integral yields \(\int_0^TG(t)\,dt=1\), hence the asserted phase-independent mean.

**2. Correlation reduction.** Define the one-sided autocorrelation \(R(s)=\int_0^\infty h_{a,b}(t)h_{a,b}(t+|s|)\,dt\) and periodic cross-correlation \(H(\delta)=\int_0^T G(t)G(t-\delta)\,dt\). Absolute convergence and partition of the real line imply
\[
H(\delta)=\sum_{k\in\mathbb Z}R(\delta+kT).
\]
Expanding the square in \(J\), all terms except the cross-correlation cancel between phases, so
\[
J(\delta)-J(L)=2w_1w_2[H(\delta)-H(L)].
\]
For \(a\ne b\), multiplication of the two exponentials and integration give, for \(s\in\mathbb R\),
\[
R(s)=\frac{a^2b^2}{2(a+b)(b-a)}
\left(\frac{e^{-a|s|}}a-\frac{e^{-b|s|}}b\right).
\]
For \(r>0\), summing the two geometric tails for \(0\le\delta\le T\) gives
\[
\sum_{k\in\mathbb Z}e^{-r|\delta+kT|}
=\frac{\cosh(r|\delta-T/2|)}{\sinh(rT/2)}.
\]
Substitution proves the displayed exact global phase-penalty formula.

**3. Strict sign and monotonicity.** For \(0\le d\le L\),
\[
F_r(d)=\int_0^d\frac{\sinh(ry)}{\sinh(rL)}\,dy.
\]
For every \(0<y<L\), the ratio in the integrand is strictly decreasing in \(r>0\): its logarithmic derivative is
\[
y\coth(ry)-L\coth(rL)<0,
\]
since \(x\mapsto x\coth x\) is strictly increasing for positive \(x\), as follows from \(\sinh(2x)>2x\). Therefore, whenever \(0<a<b\), \(F_a(d)>F_b(d)\) for \(d>0\), and \(F_a(d)-F_b(d)\) is strictly increasing in \(d\). Interchanging \(a,b\) handles \(a>b\) without changing the physical model. Multiplication by positive \(w_1w_2\) proves strict minimization at \(d=0\). Taking the smooth limit \(b\to a\), the strict negative derivative of \(F_r(d)\) for \(d>0\) gives the equal-rate formula and strict ordering also when \(a=b\).

**4. Local penalty.** The Taylor expansion \(\cosh(rd)-1=r^2d^2/2+O(d^4)\), at fixed positive model parameters, gives the stated \(K>0\) and remainder. The sign also follows from strict decrease of \(r/\sinh(rL)\), and smooth passage to coincident rates.

These steps prove the global result for the full continuous parameter domain; no finite computation is used to extend a finite enumeration to infinitely many rates or phases.

## Verification

The standalone standard-library program `checker.py` constructs the periodic Bateman profile directly by geometric summation, integrates the squared-deviation objective over one period using composite Simpson quadrature, and compares it with the separately derived closed-form phase penalty. It tests distinct and coincident rates, swapped rate order, strongly separated rates, unequal dose amounts, phase reflection, and time-rescaling. Executing `python checker.py` produced `VERIFY_OK assertions=247`. The program includes a finite-difference approximation only to the equal-rate analytic limit as a numerical diagnostic; the mathematical proof uses the exact derivative limit.

For instance, at \((a,b,T,w_1,w_2)=(1,4,1,1,2)\), the integrated squared-deviation costs are approximately \(J(0)=0.1421987211\), \(J(1/4)=0.0746319628\), and \(J(1/2)=0.0258891245\). The exact formula gives the strict inequalities independent of this example.

## Relationship to prior work

Repeated-dose linear pharmacokinetics and invariant mean exposure are established background, not claimed here. Plusquellec, De Biasi and Souhait (1999) derive steady-state concentration for periodic nonuniform drug administration in a related two-compartment setting; the accessible abstract does not describe optimization of integrated squared fluctuation. Sahin and Benet (2008) analyze operational multiple-dosing half-lives and exposure accumulation, including first-order oral absorption; their available full text treats peak/trough and dosing-interval quantities rather than a two-dose phase penalty. Evans (2011) studies fixed-point formulations for choosing oral doses to attain AUC or prescribed time-series values, a different objective. Grover and Benet (2011) study operational half-lives and fluctuation through simulations, not this exact two-dose phase ordering. The assessed mathematical contribution is the exact phase-dependent quadratic cost, global strict anti-phase minimum for unequal positive doses and all positive rates, and the sharp local penalty. No broader literature-exhaustiveness or independent priority certification is claimed.

## Limitations

The exact theorem optimizes only a squared steady-state fluctuation functional under fixed periodic doses, not a clinical dosing regimen. It does not assert safety, efficacy, compliance, peak/trough optimality, or dominance under nonlinear or time-varying pharmacokinetics. Full text of the highly pertinent 1999 nonuniform-dosing article could not be inspected; the possibility of an earlier equivalent fluctuation-optimality statement remains a historical-priority risk. The local asymptotic expansion is for fixed positive model parameters as the phase error approaches zero; it is not uniform over degenerate parameter limits.

## References

- Plusquellec, Y., De Biasi, J., and Souhait, J. (1999), *Concentration at steady-state after periodic and non-uniform administration of drug*, European Journal of Pharmaceutics and Biopharmaceutics 47, 305–307, DOI: https://doi.org/10.1016/S0939-6411(99)00017-X, PMID: 10382117 (abstract and bibliographic record inspected).
- Sahin, S., and Benet, L. Z. (2008), *The Operational Multiple Dosing Half-life: A Key to Defining Drug Accumulation in Patients and to Designing Extended Release Dosage Forms*, Pharmaceutical Research 25, 2869–2877, first publicly online 2008-11-18, DOI: https://doi.org/10.1007/s11095-008-9787-9, lawful full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC3581066/.
- Evans, N. D. (2011), *Optimal oral drug dosing via application of the contraction mapping theorem*, Biomedical Signal Processing and Control 6, 55–65, DOI: https://doi.org/10.1016/j.bspc.2010.06.006, accepted-manuscript full text: https://wrap.warwick.ac.uk/id/eprint/37150/1/WRAP_Evans_9871863-es-081211-paper.pdf.
- Grover, A., and Benet, L. Z. (2011), *Intermittent Drug Dosing Intervals Guided by the Operational Multiple Dosing Half Lives for Predictable Plasma Accumulation and Fluctuation*, Journal of Pharmacokinetics and Pharmacodynamics 38, 369–383, DOI: https://doi.org/10.1007/s10928-011-9198-0, lawful full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC3677834/.
