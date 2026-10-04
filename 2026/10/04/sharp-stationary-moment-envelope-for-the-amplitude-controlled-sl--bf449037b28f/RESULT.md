# Sharp stationary moment envelope for the amplitude-controlled SL8I flow
## Finding
Consider the printed amplitude-controlled SL8I system
\[
\dot x=my-y^2,\qquad
\dot y=az^2+xy,\qquad
\dot z=bx^2+cxy,
\]
with \(a,b,c,m>0\). For every compactly supported invariant Borel probability measure \(\mu\), write \(\langle f\rangle=\int f\,d\mu\). Then
\[
\langle y^2\rangle=m\langle y\rangle,
\qquad
\langle xy\rangle=-a\langle z^2\rangle,
\qquad
\langle x^2\rangle=\frac{ac}{b}\langle z^2\rangle.
\]
Consequently
\[
0\le \langle y\rangle\le m,
\qquad
\langle y^2\rangle\le m^2,
\]
and
\[
\langle z^2\rangle\le \frac{cm^2}{ab},
\qquad
\langle x^2\rangle\le \frac{c^2m^2}{b^2}.
\]
All bounds are sharp, and their equality cases are completely rigid. The lower endpoint \(\langle y\rangle=0\) occurs only for the point mass at the origin. The upper endpoint \(\langle y\rangle=m\), equivalently \(\langle y^2\rangle=m^2\), occurs exactly for invariant measures supported on the three equilibria with \(y=m\). Either outer second-moment bound for \(x\) or \(z\) is attained exactly for invariant measures supported on the two nonzero equilibria
\[
E_\pm=\left(-\frac{cm}b,\ m,\ \pm m\sqrt{\frac c{ab}}\right).
\]
Hence every non-equilibrium ergodic compact recurrent state, including every nonconstant periodic orbit, satisfies the outer amplitude bounds strictly.

At the published parameter values \(a=1/2\), \(b=3/5\), and \(c=6/5\), the exact laws become
\[
\langle x^2\rangle=\langle z^2\rangle,
\qquad
\langle xy\rangle=-\frac12\langle z^2\rangle,
\qquad
\langle y^2\rangle=m\langle y\rangle,
\]
so every non-equilibrium ergodic compact recurrent state obeys the sharp strict RMS envelope
\[
\operatorname{RMS}(y)<m,
\qquad
\operatorname{RMS}(x)=\operatorname{RMS}(z)<2m.
\]
The extremal equilibria are \(E_\pm=(-2m,m,\pm2m)\).

## Assumptions and scope
The statement concerns system (5) exactly as printed in Sheng, Li, Gao, Li, and Chai, with positive parameters. Compact support is assumed so the coordinate polynomials used below are integrable and the invariant-measure generator identities are legitimate. The result applies to every compactly supported invariant probability measure, without assuming ergodicity, chaos, or a numerical attractor. The strict version is asserted only for ergodic measures not supported on an equilibrium.

The theorem does not prove that every trajectory is bounded, that the numerically displayed chaotic set exists for every \(m\), or that the displayed numerical trajectory is ergodic. It gives exact constraints whenever a compact recurrent statistical state exists.

## Proof
For a compactly supported invariant probability measure, invariance gives \(\int L\phi\,d\mu=0\) for every smooth coordinate function used here, where \(L\) is the flow generator. Taking \(\phi=x\), \(y\), and \(z\) yields
\[
0=m\langle y\rangle-\langle y^2\rangle,
\]
\[
0=a\langle z^2\rangle+\langle xy\rangle,
\]
and
\[
0=b\langle x^2\rangle+c\langle xy\rangle.
\]
These are precisely the three stated stationary identities.

Put \(Y_1=\langle y\rangle\), \(Y_2=\langle y^2\rangle\), \(X_2=\langle x^2\rangle\), and \(Z_2=\langle z^2\rangle\). Since \(Y_2=mY_1\), nonnegativity of the variance gives
\[
0\le Y_2-Y_1^2=Y_1(m-Y_1),
\]
so \(0\le Y_1\le m\) and therefore \(Y_2\le m^2\).

The other two identities give \(\langle xy\rangle=-aZ_2\) and \(X_2=(ac/b)Z_2\). Cauchy--Schwarz therefore gives
\[
a^2Z_2^2=\langle xy\rangle^2
\le X_2Y_2
=\frac{ac}b Z_2Y_2.
\]
If \(Z_2=0\), the desired bounds are immediate. Otherwise cancellation gives
\[
Z_2\le \frac c{ab}Y_2\le \frac{cm^2}{ab},
\]
and substitution into \(X_2=(ac/b)Z_2\) gives
\[
X_2\le \frac{c^2m^2}{b^2}.
\]

It remains to identify equality cases. If \(Y_1=0\), then \(Y_2=0\), so \(y=0\) on the support. The support of an invariant measure is flow-invariant. Along it, \(\dot y=az^2\) must vanish, hence \(z=0\); then \(\dot z=bx^2\) must vanish, hence \(x=0\). Thus the measure is the origin point mass.

If \(Y_1=m\), then \(Y_2=m^2\) and \(\operatorname{Var}(y)=0\), so the support lies in \(y=m\). On that invariant support, \(\dot x=0\), so \(x\) is constant along each orbit, while \(\dot y=az^2+mx=0\), so \(z^2\) is constant. If \(z\ne0\), constancy of \(z^2\) forces \(\dot z=0\); if \(z=0\), then \(x=0\) and again \(\dot z=0\). Hence every support point is an equilibrium. Solving the equilibrium equations with \(y=m\) gives exactly
\[
E_1=(0,m,0),
\qquad
E_\pm=\left(-\frac{cm}b,m,\pm m\sqrt{\frac c{ab}}\right).
\]
Thus \(Y_1=m\) holds exactly for invariant measures supported on \(\{E_1,E_+,E_-\}\).

Finally, on those three equilibria the value of \(z^2\) is either \(0\) at \(E_1\) or \(cm^2/(ab)\) at \(E_\pm\). Therefore \(Z_2=cm^2/(ab)\), and equivalently \(X_2=c^2m^2/b^2\), holds exactly when the measure gives full mass to \(\{E_+,E_-\}\). An ergodic invariant measure supported on this finite equilibrium set is a point mass, so every non-equilibrium ergodic invariant measure has strict inequalities.

## Verification
The three generator identities were recomputed directly from the printed vector field. The equilibrium set was independently solved from \(y(m-y)=0\), \(az^2+xy=0\), and \(x(bx+cy)=0\). The sharp bounds then follow from one variance inequality and one Cauchy--Schwarz inequality, and the equality classification uses only invariance of the support and the explicit equilibrium equations.

For \(a=1/2\), \(b=3/5\), and \(c=6/5\), exact rational simplification gives \(ac/b=1\), \(c/(ab)=4\), and \(c^2/b^2=4\), yielding the stated RMS envelope. No floating-point computation, trajectory integration, or finite enumeration is used in the proof.

## Relationship to prior work
Sheng et al. introduce the printed system (5), describe the parameter \(m\) as an amplitude/frequency controller, and demonstrate the scaling numerically through waveforms, spectra, phase portraits, Lyapunov exponents, and average absolute values. Their article does not state the invariant-measure identities above, the sharp global second-moment envelope, or the equality classification.

Li and Sprott's earlier paper introduces the SL8 family and explains how the coefficient of a single nonquadratic term can rescale amplitude and frequency. Its SL8 table and amplitude-control section likewise do not give these stationary moment laws or sharp RMS extremizers. The present result is not a new scaling conjugacy; it is a distribution-free stationary constraint on all compact recurrent statistics of the printed amplitude-controlled flow.

## Limitations
The result is conditional on existence of a compactly supported invariant probability measure and does not establish global boundedness. It does not identify a physical or SRB measure, prove the source's numerical trajectory is chaotic, or determine temporal frequency content. Search and source inspection found no statement covering these exact SL8I stationary identities, but literature searches cannot prove absolute novelty against every unpublished or obscure source.

## References
1. Z. Sheng, C. Li, Y. Gao, Z. Li, and L. Chai, “A Switchable Chaotic Oscillator with Multiscale Amplitude/Frequency Control,” *Mathematics* 11 (2023), 618. DOI: 10.3390/math11030618. Published 26 January 2023.
2. C. Li and J. C. Sprott, “Chaotic flows with a single nonquadratic term,” *Physics Letters A* 378 (2014), 178–183. DOI: 10.1016/j.physleta.2013.11.004.
