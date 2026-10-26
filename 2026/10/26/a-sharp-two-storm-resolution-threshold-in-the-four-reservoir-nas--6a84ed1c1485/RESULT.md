# A sharp two-storm resolution threshold in the four-reservoir Nash hydrograph

## Finding

Let \(K>0\) and suppose equal unit-area instantaneous rainfall-excess inputs occur at times \(0\) and \(d>0\) in a Nash cascade of four equal linear reservoirs, each with storage coefficient \(K\). Write \(s=d/K\). The outflow \(Q(t)\) has **two strict local maxima** if and only if \(s>s_*\), where \(s_*\) is the **unique** root in \((2,3)\) of

\[
4(3-s)e^s+s^4-12s^2+24+4(s+3)e^{-s}=0.
\]

Numerically, \(s_*=2.9588081482438789725\ldots\). For \(0<s\le s_*\), there is exactly one strict local maximum (at equality, an additional stationary point is not an extremum). Therefore a four-stage cascade resolves two equal rainfall impulses **before** their separation reaches the isolated-pulse modal delay \(3K\). This is the first possible stage depth for such submodal separation: in the two- and three-reservoir Nash cascades, the exact double-peak thresholds are respectively \(d>K\) and \(d>2K\), coinciding with their isolated-pulse modal delays. For every fixed \(s\in(s_*,3)\), two sufficiently narrow equal rectangular rainfall pulses in place of the instantaneous impulses also produce at least two local discharge maxima.

## Assumptions and scope

The cascade is linear, initially empty and time invariant; its successive reservoir equations are \(K\dot q_1+q_1=I\) and \(K\dot q_j+q_j=q_{j-1}\), \(j=2,\dots,n\). Instantaneous inflow is interpreted as a Dirac mass of equal positive area; the result concerns the last-reservoir discharge, not rainfall infiltration or nonlinear catchment response. For \(n\in\{2,3,4\}\), let \(h_n(x)=x^{n-1}e^{-x}/(n-1)!\) for \(x>0\) and \(h_n(x)=0\) for \(x\le0\). Up to the common positive factor \(1/K\), the dimensionless outflow is

\[
H_{n,s}(x)=h_n(x)+h_n(x-s),\qquad x=t/K\ge0.
\]

The scale \(K\), input mass, and overall multiplicative normalization cannot change the number or locations (in units of \(K\)) of peaks. The coefficient \(s_*\) is universal only within this ideal four-equal-reservoir, equal-impulse model.

## Proof

**The four-reservoir derivative.** Before the second impulse, \(H'_{4,s}(x)=h'_4(x)\), with \(h'_4(x)=e^{-x}x^2(3-x)/6\). For \(x>s\), put \(u=x-s>0\) and \(E=e^s\). Direct differentiation yields

\[
6e^{s+u}H'_{4,s}(s+u)=P_s(u)
=-(1+E)u^3+3(1+E-s)u^2+3s(2-s)u+s^2(3-s).
\]

For every \(s>0\), \(1+e^s>s\). When \(0<s\le2\), the coefficients of \(P_s\), in descending order, have exactly one sign change, and \(P_s(0)>0\). Descartes' rule and the negative leading coefficient give exactly one positive root. There is no earlier maximum, since \(s<3\) and \(h'_4(x)>0\) for \(0<x\le s\).

For \(2<s<3\), the discriminant of the cubic is exactly

\[
\operatorname{disc}_u(P_s)=-27e^ss^2F(s),\quad
F(s)=4(3-s)e^{2s}+(s^4-12s^2+24)e^s+4(s+3).
\]

The four coefficients have signs \((-,+,-,+)\), so \(P_s(0)>0\) and \(P_s(u)\to-\infty\) as \(u\to\infty\). If the discriminant is positive, all three real roots are positive: on dividing \(P_s\) by its negative leading coefficient, Vieta's formulas give positive sum, positive pairwise-product sum, and positive product of the roots. Two negative roots and one positive root cannot have simultaneously positive sum and pairwise-product sum (if the roots are \(-a,-b,c\), \(c>a+b\) would imply \(ab-c(a+b)<0\)). Thus a positive discriminant means three distinct positive roots, and the derivative sign pattern is \(+,-,+,-\), giving two strict maxima. A negative discriminant means one positive real root and one strict maximum. At discriminant zero, the double root does not change derivative sign, and there is still just one strict maximum.

Set \(G(s)=e^{-s}F(s)\). Then

\[
G(s)=4(3-s)e^s+s^4-12s^2+24+4(s+3)e^{-s},
\]
\[
G'(s)=4(2-s)e^s+4s(s^2-6)-4(s+2)e^{-s}.
\]

On \((2,\sqrt6]\), all three terms in the derivative are nonpositive and the first and last are strictly negative. On \([\sqrt6,3)\), the function \(s(s^2-6)/(s-2)=s^2+2s-2-4/(s-2)\) is strictly increasing and bounded by its value \(9\) at \(s=3\); but \(e^s\ge e^{\sqrt6}>9\) (for instance, the first five terms of the exponential series already exceed \(9\)). Thus \((s-2)e^s>s(s^2-6)\) and \(G'(s)<0\) throughout \((2,3)\). Moreover, \(G(2)=4e^2-8+20e^{-2}>0\) and \(G(3)=-3+24e^{-3}<0\). Consequently \(G\) has precisely one zero \(s_*\in(2,3)\); \(F\) has the same sign. The discriminant is negative below that zero and positive above it, giving the claimed exact classification for \(2<s<3\).

At \(s=3\), the first component peaks exactly at the second impulse time \(x=3\); immediately afterward, \(P_3(u)<0\) for small positive \(u\), so \(x=3\) is a strict local maximum. For every \(s\ge3\),

\[
P_s(2)=4e^s-(s+2)^2(s-1)>0.
\]

The inequality holds at \(s=3\); for larger \(s\), the ratio \(e^s/((s+2)^2(s-1))\) strictly increases because its logarithmic derivative is \(1-2/(s+2)-1/(s-1)>0\). Meanwhile \(P_s(u)\to-\infty\). If \(s>3\), \(P_s(0)<0\), so there are two positive roots, and no more: a negative-leading cubic with a negative constant cannot have three positive real roots. The first isolated pulse has already peaked at \(x=3<s\), and the two post-impulse roots give a minimum followed by a second strict maximum. At \(s=3\), the zero root \(u=0\) is the first maximum and the same sign calculation yields the later minimum and maximum.

**Lower-depth comparison.** For two reservoirs, \(h'_2(x)=e^{-x}(1-x)\), and after the second pulse the derivative, multiplied by \(e^x\), equals \((1-s-u)+e^s(1-u)\): a strictly decreasing affine function that is positive at \(u=0\), because \(e^s+1>s\). There is one post-impulse maximum, plus a pre-impulse maximum at \(x=1\) exactly when \(s>1\). For three reservoirs, after the second impulse the derivative, multiplied by \(2e^x\), equals

\[
-(1+e^s)u^2+2(1+e^s-s)u+s(2-s).
\]

For \(s\le2\), there is one positive post-impulse root and no prior strict maximum. For \(s>2\), the quadratic is negative at \(u=0\), positive at \(u=1\) since \(e^s>s^2-1\) for all \(s\ge2\), and tends to minus infinity. It therefore has two positive roots. The isolated first pulse already peaked at \(x=2<s\), so there are exactly two maxima. This proves that the four-stage submodal split is the first among stage counts \(2,3,4\).

**Finite-width physical approximation.** For a fixed \(s\in(s_*,3)\), the three positive roots of \(P_s\) are simple and their corresponding times strictly exceed \(s\). Replace each unit Dirac input by a unit-area rectangular input of width \(\varepsilon\) beginning at the same start time. On compact intervals containing small disjoint neighborhoods of the three stationary points, the rectangular-pulse output and its derivative converge uniformly to the Dirac-output counterparts as \(\varepsilon\downarrow0\). The derivative's alternating signs persist, so for sufficiently small positive \(\varepsilon\) there remain two strict local maxima separated by a strict local minimum. No assertion is made about a universal allowable width.

## Verification

An independent symbolic expansion (standard polynomial algebra) gives the displayed cubic and discriminant. The standalone standard-library program `VERIFY.py` recomputes the unique zero of \(G\) by 50-digit decimal bisection, checks the expanded derivative identity at 1,500 pseudorandom points, checks the cubic discriminant factorization against the classical discriminant formula at 1,500 points, and verifies representative root-count regimes. Output:

```
critical_dimensionless_separation= 2.9588081482438789725439156947328446553820823364814
1500 identity checks; 1500 discriminant checks; 4 mode-count checks PASSED
```

These finite checks are reproducibility aids; the proof of uniqueness and the continuous-parameter classification is analytical.

## Relationship to prior work

Nash (1957), printed pages 114–121, derives the gamma impulse-response law for successive linear reservoirs and considers complex rainfall and hydrographs; its original article and appended discussion do not state a sharp equal-two-impulse modality threshold. Ponce (1980, online 2016) develops the cascade's routing and numerical diffusion meaning but does not classify coalescence of two equal translated gamma responses. Došlá (2009) gives a powerful general derivative-ratio criterion for unimodality/bimodality of mixtures of two unimodal densities. Her explicit gamma propositions compare **different rates** or **different shapes**, rather than identical-shape, identical-rate gamma profiles with **translated locations**. Her abstract criterion can be specialized to this problem but does not provide the unique transcendental separation cutoff or the stage-depth comparison; the calculation and global single-crossing proof above supply that specialization. This prior framework is an important originality limitation, not a claim of independence from general mixture theory.

## Limitations

The theorem requires equal positive impulse areas and equal reservoir storage coefficients, with zero initial storage and linear routing; it does not classify unequal pulses, more than two storms, other stage counts, nonlinear runoff generation, or a universal finite-storm-width threshold. Two mathematical peaks need not be practically distinguishable in noisy discharge measurements, especially near \(s_*\), where the new peak is shallow. The literature comparison is based on the accessible principal works and targeted searches, not a claim of exhaustive coverage of all probability-mixture or hydrology literature. Nash's original paper is bibliographically dated **1957** without a verifiable day of print release; the exact day-level provenance available from the NERC archive is its record's public date of **2014-12-09**, not a claim that the model first existed then.

## References

- Nash, J. E. (1957), “The Form of the Instantaneous Unit Hydrograph,” *IAHS Publication 45*, pp. 114–121. Full public PDF: https://iahs.info/uploads/dms/045011.pdf ; NERC bibliographic record (digitally public 2014-12-09): https://nora.nerc.ac.uk/id/eprint/508550/ .
- Ponce, V. M. (1980), “Linear Reservoirs and Numerical Diffusion,” online transcription (2016): https://ponce.sdsu.edu/linear_reservoirs_and_numerical_diffusion.html .
- Došlá, Š. (2009), “Conditions for Bimodality and Multimodality of a Mixture of Two Unimodal Densities,” *Kybernetika* 45(2), 279–292. https://www.kybernetika.cz/content/2009/2/279/paper.pdf .
- AMS/zbMATH, *Mathematics Subject Classification 2020*, entry 86A05 (hydrology): https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=86-10 .
