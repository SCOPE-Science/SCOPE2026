# A sharp three-reading identifiability boundary for an advective tracer pulse

## Finding

Consider a known instantaneous point injection at the origin of an infinite, one-dimensional homogeneous transport medium. Let the unknown injected mass, diffusivity, and positive drift be \(M>0\), \(D>0\), and \(v>0\). At distance \(x>0\) and elapsed time \(t>0\), the ideal concentration is
\[
C(x,t;M,D,v)=\frac{M}{\sqrt{4\pi Dt}}\exp\!\left(-\frac{(x-vt)^2}{4Dt}\right).
\]
Fix \(x_1,x_2>0\) with \(x_1\ne x_2\) and \(0<t_1<t_2\). The **three-reading L-design** observes the concentrations at \((x_1,t_1)\), \((x_2,t_1)\), and \((x_1,t_2)\). Define its geometric indicator (with units of squared speed),
\[
\kappa=\frac{x_1^2}{t_1t_2}-\frac{(x_1+x_2)^2}{4t_1^2}.
\]
The map from the three positive physical parameters to the three strictly positive exact readings is **globally injective if and only if \(\kappa>0\)**. Equivalently, three readings identify all three parameters for every admissible true value exactly when
\[
\boxed{\frac{x_2}{x_1}<2\sqrt{\frac{t_1}{t_2}}-1.}
\]
The repeated station must be farther from the source and the time ratio must be less than four. When \(\kappa<0\), some open set of reading triples corresponds to exactly two distinct physically admissible parameter triples; no reading triple has more than two. When \(\kappa=0\), a positive reading triple exists with a continuous one-parameter family of admissible solutions. This is an exact global-identifiability statement, not a local derivative-rank test.

Adding the fourth, rectangular reading \(C(x_2,t_2)\) makes \((M,D,v)\) globally identifiable for **every** pair of distinct positive stations and distinct positive observation times. Three contemporaneous spatial readings may separately identify parameters; therefore four is not claimed to be the minimum across all imaginable designs. The theorem distinguishes the commonly constrained two-station L-design from the completed rectangle.

## Assumptions and scope

The injection location and injection time are known, the injected mass is unknown, the background concentration is zero, there is no decay or sorption, the medium is spatially unbounded and homogeneous, and drift and diffusion are time independent. Readings are exact concentrations at the specified space-time points. The sign constraint \(v>0\) is essential to the stated physical domain; the proof does not appeal to negative drift. No observation noise, sampling interval, finite-channel boundary condition, uncertain release time, or spatially varying transport coefficient is modeled.

Global injectivity means: if two triples \((M,D,v)\) and \((\widetilde M,\widetilde D,\widetilde v)\), all components strictly positive, produce identical specified readings, the triples must coincide. Noninjectivity means at least two admissible triples produce identical readings; it does not mean a generic numerical optimizer must find both.

## Proof

**1. Exact normalized observation model.** Introduce
\[
p=D^{-1}>0,\quad q=vD^{-1}>0,\quad
A=\log\!\left(\frac{M\sqrt p}{\sqrt{4\pi}}\right),\qquad
Y(x,t)=\log\!\left(C(x,t)\sqrt t\right).
\]
Expanding the Gaussian exponent gives the exact equation
\[
Y(x,t)=A-\frac{x^2p}{4t}+\frac{xq}{2}-\frac{q^2t}{4p}.
\tag{1}
\]
Conversely every \(A\in\mathbb R\), \(p>0\), \(q>0\) determines exactly one admissible physical triple through \(D=1/p\), \(v=q/p\), \(M=e^A\sqrt{4\pi/p}\). Thus no unaccounted normalization or positivity restriction is introduced.

**2. Elimination for three readings.** Write \(Y_{ij}=Y(x_i,t_j)\) when the reading is present, and set
\[
a=\frac{x_1+x_2}{2t_1},\qquad
b=\frac{2(Y_{21}-Y_{11})}{x_2-x_1},\qquad
\gamma=\frac{4(Y_{12}-Y_{11})}{t_2-t_1}.
\]
Subtracting equation (1) at the two stations at time \(t_1\) yields
\[
q=ap+b.
\tag{2}
\]
Subtracting the readings at the repeated station and dividing by the positive time increment gives
\[
\gamma=\frac{x_1^2p}{t_1t_2}-\frac{q^2}{p}
=\kappa p-2ab-\frac{b^2}{p}.
\tag{3}
\]
All possible reconstructed \(p>0\) therefore satisfy the quadratic
\[
\kappa p^2-(\gamma+2ab)p-b^2=0,
\tag{4}
\]
with the additional physical condition \(ap+b>0\). Once \(p\) is fixed, equation (2) fixes \(q\), and the reading \(Y_{11}\) fixes \(A\). Conversely, every positive root of (4) satisfying \(ap+b>0\) gives a valid parameter triple that exactly reproduces all three observations. The quadratic cannot have more than two positive roots unless its coefficients all vanish.

**3. Sharp identifiability boundary.** If \(\kappa>0\), the function \(p\mapsto\kappa p-2ab-b^2/p\) is strictly increasing on \((0,\infty)\), since its derivative is \(\kappa+b^2/p^2>0\). Hence (3) has at most one positive root, and physical data supply one. This proves global injectivity.

If \(\kappa<0\), choose any \(b>0\) and any distinct positive \(p_1,p_2\) with \(p_1p_2=b^2/(-\kappa)\). Then \(q_j=ap_j+b>0\) because \(a>0\), and
\[
\kappa p_1-2ab-\frac{b^2}{p_1}
=\kappa p_2-2ab-\frac{b^2}{p_2}.
\]
Choose each corresponding intercept \(A_j\) to make \(Y_{11}\) equal. Equations (2) and (3) then make the other two readings equal as well. Distinct roots have nonzero quadratic discriminant, so the two solutions persist under sufficiently small changes of the observation triple: noninjectivity occurs on an open set. The quadratic bounds the number of solutions by two in this case.

If \(\kappa=0\), choose \(b=0\) and set \(q=ap\), which is positive for every \(p>0\). Equation (3) gives \(\gamma=0\) identically. Adjusting \(A\) to match \(Y_{11}\) produces an entire continuous family of indistinguishable positive triples. When \(\kappa=0\) but \(b\ne0\), the remaining positive solution, if physical, is unique; the theorem is about global injectivity of the design, so the existence of the continuum suffices to establish failure at the boundary.

Finally, \(\kappa>0\) is equivalent to \((x_1+x_2)/(2x_1)<\sqrt{t_1/t_2}\), which is the displayed sharp sensor-time inequality. Because \(x_2>0\), it forces \(t_2/t_1<4\), and because \(t_2/t_1>1\), it forces \(x_2<x_1\).

**4. Completing the rectangle.** Suppose all four concentrations \(C(x_i,t_j)\) are observed. Write
\[
d_j=\frac{Y_{2j}-Y_{1j}}{x_2-x_1}
=\frac q2-\frac{(x_1+x_2)p}{4t_j},\qquad j=1,2.
\]
Since \(t_1<t_2\), the difference gives
\[
\boxed{p=\frac{4(d_2-d_1)}{(x_1+x_2)(t_1^{-1}-t_2^{-1})},\qquad
q=2d_1+\frac{(x_1+x_2)p}{2t_1}.}
\]
The denominators are nonzero under the hypotheses. Substituting into (1) at \((x_1,t_1)\) recovers \(A\) and hence \(M,D,v\) uniquely. This proves global injectivity for the four-reading rectangle, with no restriction on \(\kappa\).

**5. Exact nonidentifiable example.** Take \(x_1=t_1=1\), \(x_2=t_2=2\). Then \(a=3/2\), \(\kappa=-7/4\). In transformed coordinates, choose
\[
(p_1,q_1,A_1)=\left(\frac12,\frac74,0\right),\qquad
(p_2,q_2,A_2)=\left(\frac87,\frac{19}7,-\frac{27}{112}\right).
\]
Their physical parameters are \((D_1,v_1,M_1)=(2,7/2,\sqrt{8\pi})\) and
\[
(D_2,v_2,M_2)=\left(\frac78,\frac{19}8,\sqrt{\frac{7\pi}2}\,e^{-27/112}\right).
\]
At the three L-design points both transformed log-concentrations equal, in order, \(-25/32\), \(-9/32\), and \(-9/4\); the actual concentrations are therefore also exactly equal. At the fourth point the transformed log-concentrations are respectively \(-25/16\) and \(-37/28\), so the extra reading distinguishes the two sources. The example has strictly positive mass, velocity, and diffusion throughout.

## Verification

The accompanying standard-library-only \(verify.py\) uses exact rational arithmetic for the Gaussian exponent after the logarithmic normalization. It checks all three identical measurements and the distinguishing fourth measurement in the explicit witness, checks the two derived identities for thousands of rational admissible parameter combinations, checks both signs of the geometric threshold, and verifies the four-reading recovery equations. The script also checks the exact critical surface \(\kappa=0\) with two distinct positive points on the continuous solution family. Run \(python3 verify.py\) in the extracted package directory. These finite tests do not establish universal uniqueness; the algebraic monotonicity and explicit constructions above do.

## Relationship to prior work

Ogata and Banks (1961) established classical longitudinal dispersion solutions in porous media under specified boundary conditions. That physical background is different from the infinite-line instantaneous Green kernel used here; the original work does not state a finite L-design inverse injectivity phase boundary in the inspected sections.

El Badia, Ha-Duong and Hamdi (2005) prove source-location and release-function identifiability from continuous-in-time observations at two strategic locations for a bounded-domain advection–dispersion–reaction equation with prescribed transport coefficients. Their full-text statements and constructive recovery (Sections 3–5) concern a different unknown parameter set and measurement operator; they neither dominate nor specialize to global identification of \(M,D,v\) from three exact samples of a known-location pulse.

Han et al. (2014) report numerical inversion accuracy for a wide, shallow river, with an emphasis on release location/intensity and monitoring configurations. A full paper was not materially inspected; its abstract supplies context only. The 2020 open-access study *Influence of the spatial and temporal monitoring design on the identification of an instantaneous pollutant release in a river* analyzes a 2D model, profiles source location/time/mass and studies station placement and measurement frequency with many observations. Its inspected introduction, results, monitoring-design subsections, and conclusions do not give the exact \(\kappa\)-criterion for transport-parameter identification from three readings. Their broader lessons that monitoring geometry controls identifiability are consistent with this result, but do not logically imply the sharp formula.

More general nonlinear inverse-parameter and interpolation methods may contain an abstract theorem from which the algebraic phase boundary follows. No claim of absolute historical uniqueness is made. The originality assessment rests on comparison of actual hypotheses, observables, and conclusions, not on merely differing titles.

## Limitations

This is structural global identifiability with **exact** observations, not a stability or statistical efficiency guarantee. Near \(\kappa=0\), finite-noise inversion may be ill-conditioned even on the injective side. The infinite-line Gaussian kernel assumes an instantaneous impulse and omits the downstream boundary condition considered in Ogata–Banks's semi-infinite problem; applying the theorem directly to finite rivers or groundwater boundaries would be unjustified. The source position/time are known here, unlike in several inverse-source articles. Unknown reaction/decay, uncertain gain calibration between stations, finite-duration sources, and unknown advection sign require separate study. Three same-time spatial measurements or three time observations at one location may have different identifiability properties; the theorem does not rank all sampling designs or prove minimality over arbitrary designs. No independent mathematical audit has been performed.

## References

1. A. Ogata and R. B. Banks, *A Solution of the Differential Equation of Longitudinal Dispersion in Porous Media*, U.S. Geological Survey Professional Paper 411-A (1961), DOI: 10.3133/pp411A. Public full-text transcription: https://www.readkong.com/page/a-solution-of-the-differential-equation-of-longitudinal-6672641 .
2. A. El Badia, T. Ha-Duong and A. Hamdi, *Identification of a point source in a linear advection–dispersion–reaction equation: application to a pollution source problem*, *Inverse Problems* 21 (2005), 1121–1136, DOI: 10.1088/0266-5611/21/3/020; first online publication reported 2005-05-09. Author-uploaded full text: https://www.researchgate.net/publication/230901733_Identification_of_a_point_source_in_a_linear_advection-dispersion-reaction_equation_Application_to_a_pollution_source_problem .
3. L. X. Han, Y. Zhu, W. L. Jin and F. X. Zhang, *Inverse Problem Of An Instantaneous Pollution Source In A Wide And Shallow River And The Analysis On Inversion Accuracy*, WIT Transactions on Ecology and the Environment 182 (2014), DOI: 10.2495/WP140291. https://www.witpress.com/elibrary/wit-transactions-on-ecology-and-the-environment/182/26204 .
4. *Influence of the spatial and temporal monitoring design on the identification of an instantaneous pollutant release in a river*, *Advances in Water Resources* 146 (2020), article 103788, DOI: 10.1016/j.advwatres.2020.103788. https://doi.org/10.1016/j.advwatres.2020.103788 .
