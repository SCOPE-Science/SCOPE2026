# A sharp reentrant two-peak window for delayed unequal Bateman inputs

## Finding

Consider a linear one-compartment pharmacokinetic model with instantaneous entry into an absorption depot followed by first-order absorption and first-order elimination. A second depot input, of relative amount \(m>0\), enters after a delay \(d>0\), with the same subsequent rate constants as the first. Let \(0<\lambda\leq\kappa\) be the smaller and larger of the absorption and elimination rates. Up to a common positive multiplier, the systemic concentration is

\[
C_{d,m}(t)=g(t)+m g(t-d)\mathbf{1}_{\{t\geq d\}},\qquad
 g(u)=\begin{cases}
 \dfrac{e^{-\lambda u}-e^{-\kappa u}}{\kappa-\lambda},&u>0,\ \lambda<\kappa,\\ u e^{-\lambda u},&u>0,\ \lambda=\kappa,\\ 0,&u\leq 0.
 \end{cases}
\]

In the first case in this display, \(\lambda<\kappa\) is assumed. Define the isolated-response peak time
\[
t_0=\begin{cases}\dfrac{\log(\kappa/\lambda)}{\kappa-\lambda},&\lambda<\kappa,\\\dfrac1\lambda,&\lambda=\kappa,\end{cases}
\]
and, for \(d>t_0\), define \(Q(d)=-g'(d)\) (where the derivative is the right/ordinary derivative for \(d>0\)). Then **the concentration has exactly two strict local maxima if and only if**
\[
\boxed{d>t_0\quad\text{and}\quad m>Q(d).}
\]
In all remaining cases it has exactly one strict local maximum. Equality \(m=Q(d)\) belongs to the one-maximum regime.

The function \(Q\) vanishes at \(t_0\), increases strictly on \((t_0,2t_0)\), decreases strictly on \((2t_0,\infty)\), and tends to zero. Its exact maximum is
\[
\boxed{m_*=Q(2t_0)=\begin{cases}
 (\kappa/\lambda)^{-(\kappa+\lambda)/(\kappa-\lambda)},&\lambda<\kappa,\\e^{-2},&\lambda=\kappa.
\end{cases}}
\]
Thus when \(0<m<m_*\), there exist exactly two delay thresholds \(t_0<d_-<2t_0<d_+\), uniquely defined by \(Q(d_\pm)=m\). The profile has **two peaks** for \(d\in(t_0,d_-)\cup(d_+,\infty)\) and **one peak** for \(d\in(0,t_0]\cup[d_-,d_+]\). In particular, a small second input creates a reentrant **two-peak / one-peak / two-peak** sequence as the delay increases beyond \(t_0\). When \(m=m_*\), the only delay greater than \(t_0\) with one maximum is \(d=2t_0\); when \(m>m_*\), every \(d>t_0\) has two maxima. Furthermore, \(m_*\leq e^{-2}\), with equality only at coincident rate constants.

## Assumptions and scope

The model is linear, starts without residual drug, has no lag in depot activation apart from the specified second onset, uses equal first-order rates for both inputs, and has no nonlinear absorption, saturable elimination, distribution compartments, or measurement noise. The second input may model a deliberately delayed dose or an idealized second release fraction of a single formulation. No patient-specific clinical regimen follows from the theorem. Two peaks means **two strict local maxima of the continuous mathematical concentration trajectory**; it does not impose a minimum prominence or a finite sampling resolution.

With depot amount \(A\), central amount \(X\), rate constants \(k_a,k_e>0\), and two instantaneous depot increments of sizes \(D\) and \(mD\), the governing equations between events are \(A'=-k_a A\), \(X'=k_a A-k_eX\). Taking plasma concentration \(X/V\) for \(V>0\) produces the displayed \(g\) with positive prefactor \(Dk_a/V\) after sorting the two rates. Coincident-rate formulas are genuine limits, not substitutions into the distinct-rate denominator.

## Proof

**1. A single input has one maximum.** For \(\lambda<\kappa\),
\[
 g'(u)=\frac{-\lambda e^{-\lambda u}+\kappa e^{-\kappa u}}{\kappa-\lambda},\qquad g'(0+)=1.
\]
The equation \(g'(u)=0\) is equivalent to \(e^{(\kappa-\lambda)u}=\kappa/\lambda\), giving the unique root \(t_0\). The derivative is positive before that root and negative after it. If \(\lambda=\kappa\), \(g'(u)=(1-\lambda u)e^{-\lambda u}\), giving \(t_0=1/\lambda\) and the same sign pattern.

**2. After the second input, there is at most one maximum.** For \(t>d\) and distinct rates,
\[
 C'_{d,m}(t)=\frac{-\lambda(1+m e^{\lambda d})e^{-\lambda t}+\kappa(1+m e^{\kappa d})e^{-\kappa t}}{\kappa-\lambda}.
\]
The ratio of the two positive exponential terms changes strictly with \(t\), so this derivative has exactly one zero on the whole real line and changes from positive to negative there. In fact its zero is
\[
 t_+(d,m)=\frac{\log\!\left[\kappa(1+m e^{\kappa d})/\{\lambda(1+m e^{\lambda d})\}\right]}{\kappa-\lambda}.
\]
Only zeros with \(t_+>d\) describe a post-input maximum. For equal rates, direct differentiation instead yields
\[
 t_+(d,m)=\lambda^{-1}+\frac{m e^{\lambda d}}{1+m e^{\lambda d}}d
\]
with the same positive-to-negative property. Hence there can never be more than two maxima in total.

**3. Exact mode criterion and equality boundaries.** For \(d\leq t_0\), the pre-input curve has not yet attained a strict maximum, and the right derivative just after the second input is \(g'(d)+m>0\). The single post-input stationary point is therefore the unique maximum. For \(d>t_0\), the first strict maximum occurs at \(t_0\), and the left derivative at \(d\) is strictly negative. The right derivative jumps by exactly \(m g'(0+)=m\); thus
\[
 C'_{d,m}(d+)=g'(d)+m=m-Q(d).
\]
If this is positive, \(d\) is a strict corner minimum and the post-input derivative crosses zero once more, producing the second strict maximum. If it is nonpositive, the concentration decreases after \(d\) and no second maximum exists. In the equality case, the right derivative is zero only at \(d\) and is strictly negative immediately afterward; the corner is not a maximum. This proves the stated necessary and sufficient condition including all boundaries.

**4. Unimodal threshold and the reentrant interval.** For distinct rates,
\[
 Q(d)=\frac{\lambda e^{-\lambda d}-\kappa e^{-\kappa d}}{\kappa-\lambda},\quad
 Q'(d)=\frac{-\lambda^2 e^{-\lambda d}+\kappa^2 e^{-\kappa d}}{\kappa-\lambda}.
\]
The unique zero of \(Q'\) is \(2t_0\), with positive derivative below and negative derivative above; \(Q(t_0)=0\), and \(Q(d)\to0\) as \(d\to\infty\). Substituting \(d=2t_0\), writing \(r=\kappa/\lambda>1\), gives
\[
 Q(2t_0)=r^{-(r+1)/(r-1)}.
\]
If rates coincide, \(Q(d)=(\lambda d-1)e^{-\lambda d}\), with unique maximum \(e^{-2}\) at \(d=2/\lambda\). The intermediate-value theorem and strict monotonicity on either side of \(2t_0\) now give exactly the two roots \(d_-\), \(d_+\) for \(0<m<m_*\), and the stated interval classification for all \(m>0\). Finally, for \(r>1\), \((r+1)\log r>2(r-1)\) (differentiate the difference, or integrate a strictly positive derivative), proving \(m_*<e^{-2}\), while its limit as \(r\downarrow1\) is \(e^{-2}\).

## Verification

The standalone standard-library Python file `verify.py` checks the exact corner-slope criterion, unimodality threshold, crossing equations, and finite-difference derivatives on 2,200 seeded random parameter cases, including coincident rates, together with deterministic boundary and reentrance tests. It prints two PASS messages on successful execution. These finite tests are corroborative only; the general quantifiers and the strict boundary cases are proved analytically above.

For \(\lambda=1\), \(\kappa=3\), and \(m=1/20\), one obtains
\[
 t_0=\tfrac12\log3\approx0.549306144334055,\qquad m_*=1/9.
\]
The two roots of \(Q(d)=1/20\), certified by monotonicity and reproducible numerical bisection, are
\[
 d_-\approx0.656386502314363,\qquad d_+\approx2.270043918454294.
\]
There are two strict peaks at \(d=0.6\), only one at \(d=0.7\), and two again at \(d=3\). All quantities are dimensionless until the rates are specified in inverse-time units.

## Relationship to prior work

The single-dose Bateman kernel and linear superposition of dose responses are standard pharmacokinetic results, **not** claimed as new. Sahin and Benet (2008) study repeated-dose accumulation and dosing half-life; Grover and Benet (2011) analyze absorption-rate effects on repeated dosing and fluctuation. Davies and colleagues (2010) survey multiple peaks from several mechanisms, including fractionated and delayed absorption. Godfrey and colleagues (2011) model double peaks with compartmental absorption pathways. None of the fully inspected source material states the exact **unequal-input reentrant peak-count criterion**, its closed-form critical ratio, or its strict equality cases. More general delayed-input or exponential-mixture theory could in principle imply the result, and one closely related modelling paper was not available in full; this is recorded as an unresolved literature risk, not a proof of exclusivity.

The coincident-rate kernel is the two-stage Erlang response, which is also used in reservoir and transit-chain models. An equal-amplitude two-pulse Erlang peak threshold is a special case, whereas the present result classifies **unequal amplitudes**, especially the intervening one-peak window absent for equal amplitudes, and permits two distinct rates.

## Limitations

The sharp statement concerns two idealized instantaneous depot inputs, their common two-rate linear response, and strict mathematical local maxima. A peak may be too shallow to detect near the transition; the result does not quantify robust peak prominence, sampling resolution, optimal doses, treatment response, or nonlinear multi-compartment kinetics. The equality cases are one-peak profiles and are not structurally stable under arbitrary changes of the input shape. Novelty is bounded by the reviewed sources and subject to possible subsumption by inaccessible or differently named general mixture results; no independent audit or experimental pharmacokinetic validation has been performed.

## References

1. Sahin, S., and Benet, L. Z. (2008), *The Operational Multiple Dosing Half-life: A Key to Defining Drug Accumulation in Patients and to Designing Extended Release Dosage Forms*, *Pharmaceutical Research* 25, 2869–2877, published online 2008-11-18, DOI: 10.1007/s11095-008-9787-9. Full text: https://openaccess.hacettepe.edu.tr/bitstreams/2299af6a-0e4f-4e91-85ac-d0b7a0f0c509/download
2. Davies, N. M., Takemoto, J. K., Brocks, D. R., and Yáñez, J. A. (2010), *Multiple Peaking Phenomena in Pharmacokinetic Disposition*, *Clinical Pharmacokinetics* 49, 351–377, DOI: 10.2165/11319320-000000000-00000.
3. Grover, A., and Benet, L. Z. (2011), *Intermittent Drug Dosing Intervals Guided by the Operational Multiple Dosing Half Lives for Predictable Plasma Accumulation and Fluctuation*, *Journal of Pharmacokinetics and Pharmacodynamics* 38, 369–383, DOI: 10.1007/s10928-011-9198-0. Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC3677834/
4. Godfrey, K. R., Arundel, P. A., Dong, Z., and Bryant, R. A. (2011), *Modelling the Double Peak Phenomenon in Pharmacokinetics*, *Computer Methods and Programs in Biomedicine* 104, 62–69, first published online 2010-04-08, DOI: 10.1016/j.cmpb.2010.03.007. The full text was not accessible in this review.
