# Two incidence maxima before the prevalence apex in an autonomous two-susceptibility SIR epidemic

## Finding

An autonomous, permanently heterogeneous susceptible–infectious–removed (SIR) model with **two fixed susceptibility types**, a single well-mixed infectious population, and a constant recovery rate has at least two distinct strict local maxima of aggregate **incidence** during an interval in which aggregate **infectious prevalence is strictly increasing**. The property persists for an open set of parameters and initial conditions. No intervention, behavior change, delayed infection, varying recovery, subgroup mixing separation, or reinfection is required.

Specifically, for time-independent susceptibilities \(\lambda_1=1\), \(\lambda_2=100\), recovery rate \(\gamma=4/5\), and initial data
\[
 (s_1(0),s_2(0),I(0),R(0))
 =\left(\frac{99999}{100000}\frac{49}{50},
 \frac{99999}{100000}\frac1{50},\frac1{100000},0\right),
\]
there exist times \(0<t_1<t_2<t_3\), before the infectious-prevalence maximum, such that aggregate new-infection incidence is strictly locally maximal at \(t_1,t_3\) and strictly locally minimal at \(t_2\). The corresponding cumulative infection pressures lie, respectively, in \((0,1/50)\), \((1/50,1/20)\), and \((1/20,1/5)\). The total number infectious is increasing throughout the complete pressure interval \([0,1/5]\).

The claim is **existential**: it establishes at least two incidence maxima and makes no assertion that there are exactly two over the full epidemic.

## Assumptions and scope

With population fractions summing to one, the two susceptible fractions \(s_j(t)\), the pooled infectious fraction \(I(t)\), and removed fraction \(R(t)\) solve the classical fixed-heterogeneity mean-field SIR equations
\[
 \dot{s}_j=-\lambda_j s_j I,\qquad
 \dot I=\left(\lambda_1s_1+\lambda_2s_2-\gamma\right)I,\qquad
 \dot R=\gamma I.
\]
Both types of newly infected persons enter the *same* infectious pool and have the same exponential infectious-duration distribution, with rate \(\gamma\). The force of infection on susceptible type \(j\) is \(\lambda_j I\). The aggregate incidence is \(C(t)=-\dot{s}_1(t)-\dot{s}_2(t)\). All stated parameters are positive; group shares and population fractions are admissible. The initial susceptible fractions correspond to a fixed two-point susceptibility distribution with masses \(49/50\) and \(1/50\). The basic reproduction number is \(3.72496275\).

## Proof

Introduce cumulative infection pressure \(x(t)=\int_0^t I(u)\,du\), so \(\dot x=I\). Along any solution with \(I>0\), the susceptible fractions are exactly
\[
 s_1(x)=\frac{99999}{100000}\frac{49}{50}e^{-x},\qquad
 s_2(x)=\frac{99999}{100000}\frac1{50}e^{-100x}.
\]
By conservation of population and \(\dot R=\gamma\dot x\), one has \(R(x)=\gamma x\) and
\[
 I(x)=1-s_1(x)-s_2(x)-\gamma x.
\]
Define the decreasing effective susceptibility and its derivative magnitude by
\[
 H(x)=s_1(x)+100s_2(x),\qquad K(x)=s_1(x)+10000s_2(x),\qquad H'(x)=-K(x)<0.
\]
Since \(I'(x)=H(x)-\gamma\), aggregate incidence is \(C(x)=I(x)H(x)\), and its derivative with respect to elapsed time is
\[
 \frac{dC}{dt}=I(x)Q(x),\qquad
 Q(x):=H(x)(H(x)-\gamma)-I(x)K(x).
\]
The sign of incidence growth therefore equals the sign of \(Q\) wherever \(I>0\).

The accompanying exact-rational interval program verifies the following **outward-enclosed values**. Each displayed numerator is divided by \(10^8\); the exact unrounded values lie inside the printed closed intervals. The four rows correspond, in order, to \(x=0,1/50,1/20,1/5\):

| Pressure | Interval enclosing \(I\), times \(10^8\) | Interval enclosing \(H\), times \(10^8\) | Interval enclosing \(Q\), times \(10^8\) |
|---|---:|---:|---:|
| \(0\) | \([1000,1000]\) | \([297997020,297997020]\) | \([649423645,649423646]\) |
| \(1/50\) | \([2070822,2070823]\) | \([123125295,123125296]\) | \([-4941571,-4941570]\) |
| \(1/20\) | \([2766972,2766973]\) | \([94567127,94567128]\) | \([7467648,7467649]\) |
| \(1/5\) | \([3765188,3765189]\) | \([80234811,80234812]\) | \([-2832593,-2832592]\) |

In particular, \(Q\) has signs \(+,-,+,-\) at these four consecutive pressures. Also \(H\) decreases and \(H(1/5)>4/5\), so \(I'(x)=H(x)-4/5>0\) throughout \([0,1/5]\). Thus \(I(x)\ge I(0)>0\) there. Since \(\dot x=I\) is bounded below by \(I(0)\) on this interval, the solution reaches all four pressures at finite, strictly ordered times, while infectious prevalence is strictly increasing.

The function \(Q\) is real analytic and not identically zero. Its alternating endpoint signs force, in the three disjoint open pressure intervals, respectively, at least one strict \(+\)-to-\(-\) crossing, one strict \(-\)-to-\(+\) crossing, and one strict \(+\)-to-\(-\) crossing. These yield a strict incidence maximum, a strict minimum, and another strict maximum in chronological order. Strict inequalities are stable under sufficiently small parameter and initial-data perturbations, so the same argument gives an open neighborhood of such epidemics. This proves the claim.

## Verification

The included standalone `verify.py` (Python 3 standard library) recomputes \(I,H,K,Q\) with `fractions.Fraction` and outward interval arithmetic. To enclose \(e^{-z}\) for rational \(z\ge0\), the program calculates a positive Taylor partial sum for \(e^z\), adds a rational geometric-series bound for the remaining positive tail, and reciprocates both positive endpoints. Consequently no floating-point approximation enters any asserted sign. Execute `python3 verify.py` from the extracted package; the expected terminal marker is `VERIFY_OK: exact rational four-point sign certificate and increasing prevalence`. The elementary analytic argument above extends these *four exact checks* to the existence of strict local extrema without numerical ODE integration.

## Relationship to prior work

Izyumtseva, KhudaBukhsh, Gomes, and Rempala (2026, arXiv:2608.22122v1, sections 3.1 and 4.4) rigorously derive the fixed-susceptibility SIR equations and their Laplace-transform representation, including discrete susceptibility laws. Their phrase “arbitrary multimodality” refers to the initial *trait distribution*; it does not establish multimodal *time-dependent incidence*. The reduction used above follows from their framework; the exact two-type incidence sign certificate and its location entirely before the prevalence apex do not appear in the inspected primary text.

Multiple epidemic peaks arising from heterogeneity have been demonstrated previously. Bootsma, Chan, Diekmann, and Inaba (2024, section 10.1) explicitly display double-peaked incidence under heterogeneous **latent periods**, and discuss weakly coupled subpopulations. Siegenfeld and collaborators (2022, section 3.2 and Figure 5) show multiple epidemic peaks in a five-group model with strongly **separated connectivity and heterogeneity in both transmission traits**; their section 3.2.1 also discusses susceptibility-only models, but their multiple-peak example does not establish the present two-type, single-infectious-pool, susceptibility-only, increasing-prevalence statement. These earlier works establish the general possibility of multiple epidemic peaks and are not claimed as new here.

## Limitations

This is an explicit constructive example plus a neighborhood result, not a necessary-and-sufficient classification of susceptibility laws supporting several incidence maxima. It does not establish exactly two peaks during a whole epidemic, nor does it claim an additional prevalence peak or a literal second outbreak. The intermediate drop between peaks is modest and may be obscured by surveillance smoothing or noise. It concerns deterministic mean-field limits with a shared exponential infectious duration and fixed susceptibilities; it is not a stochastic finite-population guarantee. Earlier general heterogeneous epidemic mathematics may imply some qualitative aspects under different terminology, so comprehensive literature originality remains a risk despite the direct comparisons above.

## References

1. O. Izyumtseva, W. R. KhudaBukhsh, M. G. M. Gomes, and G. A. Rempala. *From Individual-Based Stochastic Epidemics to Heterogeneous SIR Equations*. arXiv:2608.22122v1 (first posted 2026-08-22). https://arxiv.org/html/2608.22122v1
2. M. C. J. Bootsma, K. M. D. Chan, O. Diekmann, and H. Inaba. *The Effect of Host Population Heterogeneity on Epidemic Outbreaks* (2024). https://arxiv.org/search/?query=The+Effect+of+Host+Population+Heterogeneity+on+Epidemic+Outbreaks&searchtype=all
3. A. Siegenfeld and collaborators. *Modeling Complex Systems: A Case Study of Compartmental Models in Epidemiology*. *Complexity* (2022), article 3007864. https://doi.org/10.1155/2022/3007864
4. H. Berestycki and collaborators. *Epidemic modeling with heterogeneity and social diffusion* (2023). Prior example with evolving trait distribution.
5. S. Mukherjee, S. Mondal, and B. Bagchi. *Stochastic formulation of multiwave pandemic: decomposition of growth into inherent susceptibility and external infectivity distributions* (2021). Distinct spatial stochastic mechanism; only preview and abstract inspected.
