# The reciprocal coefficient in generalized Kepler timing

## Finding

In the generalized timing law
\[
nt=\chi-\tilde e\sin\chi,
\]
the coefficient consistent with Lynden-Bell's derived central-orbit timing formula is
\[
\tilde e=\frac{V_2}{V_1}e^*,
\]
not the reciprocal \(\frac{V_1}{V_2}e^*\) printed in the 2014 inversion paper. With the paper's stated definitions, the exact harmonic-orbit case \(k=2\) has \(V_1=1-(e^*)^2\) and \(V_2=0\): the printed coefficient is undefined, whereas the corrected coefficient is zero and gives the exact linear timing \(nt=\chi\). The Kepler case \(k=1\), where \(V_1=V_2=1\), is unchanged.

## Assumptions and scope

Let \(e^*\in(0,1)\) be the orbit-shape parameter used in the 2014 paper (denoted \(e\) in the 2015 derivation), \(k>0\) the radial-variable exponent, \(\chi\) the generalized eccentric anomaly, and \(n=2\pi/T_r\) the radial angular frequency. The coefficient functions are
\[
V_1=\frac{1-(e^*)^2}{2}
\left[(1-e^*)^{1-2/k}+(1+e^*)^{1-2/k}\right],
\]
and
\[
V_2=\frac{[1-(e^*)^2]^2}{2e^*}
\left[(1-e^*)^{-2/k}-(1+e^*)^{-2/k}\right]-V_1.
\]
The claim is a correction to the coefficient in the displayed generalized timing equation, not a claim that the entire approximate timing theory is exact for every central potential. The cited derivation explicitly omits small terms in the general case; it states that those terms vanish in the Kepler and harmonic cases used below.

## Proof

The 2015 derivation gives
\[
t=\frac{T_r}{2\pi}\left[\chi-\frac{V_2}{V_1}e^*\sin\chi\right].
\]
Multiplying by \(n=2\pi/T_r\) yields
\[
nt=\chi-\frac{V_2}{V_1}e^*\sin\chi.
\]
Therefore the coefficient multiplying \(\sin\chi\) in the normalized timing equation is \((V_2/V_1)e^*\), provided \(V_1\ne0\). The 2014 inversion paper instead defines that coefficient as \((V_1/V_2)e^*\), despite giving the same formulas for \(V_1,V_2\).

The discrepancy is hidden in the Kepler case \(k=1\). Substitution gives
\[
V_1=\frac{1-(e^*)^2}{2}
\left[\frac1{1-e^*}+\frac1{1+e^*}\right]=1.
\]
Also,
\[
V_2=\frac{[1-(e^*)^2]^2}{2e^*}
\left[\frac1{(1-e^*)^2}-\frac1{(1+e^*)^2}\right]-1=1.
\]
Thus both ratios equal one for \(k=1\).

The exact central harmonic oscillator has \(k=2\). Then
\[
V_1=\frac{1-(e^*)^2}{2}(1+1)=1-(e^*)^2,
\]
and
\[
\begin{aligned}
V_2
&=\frac{[1-(e^*)^2]^2}{2e^*}
\left[\frac1{1-e^*}-\frac1{1+e^*}\right]-V_1\\
&=[1-(e^*)^2]-[1-(e^*)^2]=0.
\end{aligned}
\]
Since \(e^*\in(0,1)\), \(V_1>0\). The corrected coefficient is therefore \((V_2/V_1)e^*=0\), so \(nt=\chi\), the exact linear timing stated for the harmonic case in the 2015 derivation. The printed reciprocal \((V_1/V_2)e^*\) is undefined. This exact boundary case establishes that the printed ratio cannot be the coefficient in the stated generalized timing equation.

## Verification

The algebra above was checked by symbolic simplification of the displayed definitions for \(k=1\) and \(k=2\), yielding respectively \((V_1,V_2)=(1,1)\) and \((V_1,V_2)=(1-(e^*)^2,0)\). The result is also checked directly against the full-text timing equation and its explicit harmonic-limit statement in the 2015 source. No numerical experiment is used as a proof.

## Relationship to prior work

Lynden-Bell's 2014 paper introduces the cubic inversion method and defines the generalized eccentricity using \(V_1/V_2\). The 2015 paper *Bound central orbits* gives the timing equation with \(V_2/V_1\) and explicitly states that the harmonic oscillator has \(V_2=0\) and \(\chi\propto t\). The definitions of \(V_1,V_2\) match across the two papers, so the discrepancy is a reciprocal-coefficient inconsistency, not a change of notation.

Brown's 2023 *An improved cubic approximation for Kepler's equation* discusses the Lynden-Bell cubic in the classical Kepler problem, where \(V_1=V_2=1\); that treatment does not resolve the non-Keplerian ratio because it considers \(M=E-e\sin E\). Bounded searches of indexed findings and public literature did not surface a matching correction. This absence is not proof that no unindexed correction or correspondence exists.

## Limitations

The finding corrects the coefficient in the stated generalized timing law. It does not rederive all approximations for arbitrary potentials, certify a global error bound for the cubic solver, or claim that the 2014 Kepler-only numerical accuracy figures are false. For general \(k\), the 2015 timing expression itself is presented with omitted small terms; the conclusion here is limited to the coefficient comparison and the exact \(k=1,2\) boundary cases.

## References

1. D. Lynden-Bell, “An approximate analytic inversion of Kepler's equation,” *Monthly Notices of the Royal Astronomical Society* 447 (2015), 363–365; first published 16 December 2014. DOI: 10.1093/mnras/stu2326.
2. D. Lynden-Bell, “Bound central orbits,” *Monthly Notices of the Royal Astronomical Society* 447 (2015), 1962–1972; first published 3 January 2015. DOI: 10.1093/mnras/stu2485.
3. M. T. Brown, “An improved cubic approximation for Kepler's equation,” *Monthly Notices of the Royal Astronomical Society* 525 (2023), 57–66. DOI: 10.1093/mnras/stad2007.
