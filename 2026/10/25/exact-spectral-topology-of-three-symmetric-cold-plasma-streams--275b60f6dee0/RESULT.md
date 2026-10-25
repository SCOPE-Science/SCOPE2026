# Exact spectral topology of three symmetric cold plasma streams

## Finding

For three cold electron populations of velocities \(-V,0,+V\), squared plasma frequencies \(a,b,a\), and immobile neutralizing ions, put \(u=b/a>0\) and \(t=(kV)^2/a>0\). The longitudinal temporal dispersion is
\[
1=\frac{a}{(\omega+kV)^2}+\frac{b}{\omega^2}+\frac{a}{(\omega-kV)^2}.
\]
Define
\[
Q_u(t)=4t^3-(15+12u)t^2+(12-78u+12u^2)t+(1-4u)(u+2)^2.
\]
If \(0<u<1/4\), this polynomial has exactly two positive simple zeros \(t_-<t_+\). For \(0<t<t_-\), the six temporal frequencies contain exactly two distinct exponentially growing, *nonoscillatory* frequencies (positive pure imaginary \(\omega\)); for \(t_-<t<t_+\), there are exactly two exponentially growing frequencies with nonzero and opposite real parts; for \(t>t_+\), all six frequencies are real. At \(t=t_-\), the repeated purely imaginary root remains exponentially growing. At \(t=t_+\), the repeated real roots have no positive imaginary part; degeneracy may produce algebraic temporal growth and is not claimed to be Lyapunov stability.

For every \(u\ge1/4\), \(Q_u\) has exactly one positive simple zero \(t_+\). The growth is oscillatory for every \(0<t<t_+\) and absent in the sense of positive imaginary frequency for \(t\ge t_+\). Thus **a stationary-population squared plasma frequency equal to one quarter of that of either travelling population exactly eliminates the finite-wavenumber nonoscillatory-growth interval**.

The two transitions obey exact limiting laws
\[
t_\pm=2\pm2\sqrt6\,\sqrt u+O(u)\quad(u\downarrow0),\qquad
 t_-=3(1/4-u)+O((1/4-u)^2)\quad(u\uparrow1/4).
\]
In particular, the width of the oscillatory-instability interval created by a weak stationary population is \(t_+-t_-=4\sqrt6\sqrt u+O(u)\). At \(u=1/4\), the positive cutoff is \(t_+=(9+6\sqrt3)/4\).

## Assumptions and scope

All three electron populations are collisionless, cold delta functions in longitudinal velocity, spatially homogeneous and unmagnetized. Their charges and masses are equal, the two counterpropagating populations have equal density and opposite velocities, and the third is stationary. Positive ions neutralize the equilibrium charge and do not move. The perturbation is electrostatic, longitudinal and proportional to \(e^{ikx-i\omega t}\), with \(k,V,a,b>0\). The statement classifies *temporal* eigenfrequencies at real nonzero wavenumber, not absolute/convective spatial growth, kinetic finite-temperature stability, or nonlinear saturation. The labels “oscillatory” and “nonoscillatory” refer to the real part of exponentially growing temporal frequencies.

## Proof

Set \(z=\omega^2/a\). Clearing the three denominators gives exactly
\[
P_{u,t}(z)=z^3-(2t+2+u)z^2+[t^2+2(u-1)t]z-ut^2=0.
\]
The roots at \(z=0\) or \(z=t\) cannot occur, because \(P(0)=-ut^2\ne0\) and \(P(t)=-4t^2\ne0\). Thus no roots were introduced by clearing denominators for \(t,u>0\).

Direct expansion gives
\[
\operatorname{disc}_z(P)=4t^2Q_u(t),\qquad
\operatorname{disc}_t(Q_u)=-629856u(2u-1)^3.
\]
For \(0<u<1/4\), \(\operatorname{disc}_t(Q)>0\), so \(Q\) has three distinct real zeros. Since \(Q(0)=(1-4u)(u+2)^2>0\), their product is negative; since their sum is \((15+12u)/4>0\), exactly one is negative and two are positive. The positive zeros bracket \(2(1-u)\):
\[
Q_u(2(1-u))=-27u(4u^2-11u+8)<0,
\]
where the quadratic is strictly positive for every real \(u\). Hence \(0<t_-<2(1-u)<t_+\).

For \(1/4<u<1/2\), the discriminant remains positive, but \(Q(0)<0\). The identities
\[
Q_u(-u)=-4(2u-1)^3>0,\quad
Q_u(-1/2)=-\frac{(2u-1)^2(4u+25)}4<0
\]
force two negative zeros and therefore one positive zero. For \(u=1/2\), \(Q\) has a double negative zero and one positive zero. For \(u>1/2\), its discriminant is negative, so it has only one real zero; \(Q(0)<0\) makes that zero positive. At \(u=1/4\), the zero at \(t=0\) is excluded from the physical wavenumber domain and the remaining zeros comprise one negative and one positive root. This proves the stated positive-zero counts and their sign intervals.

When \(Q<0\), the real cubic \(P\) has one real root and two nonreal conjugate roots. Its constant term is negative and the sum of roots is positive; moreover \(P(0)<0\) and \(P(z)\to+\infty\) as \(z\to+\infty\), so the unique real root is positive. Square-rooting the two nonreal roots produces exactly two growing complex frequencies with opposite nonzero real parts (and two decaying counterparts). When \(Q>0\), all three \(z\)-roots are real. Their product is \(ut^2>0\) and sum is \(2t+2+u>0\). Either all three are positive, or one is positive and two are negative. In the latter case, writing them \(x,-y,-w\) with \(x>y+w\) gives their pairwise sum \(yw-x(y+w)<0\). Thus the sign of the coefficient \(t[t+2(u-1)]\) separates the cases. On \(0<t<t_-\) (possible only for \(u<1/4\)), this coefficient is negative; on \(t>t_+\) it is positive, using the strict bracketing by \(2(1-u)\) for \(u<1\), and positivity for \(u\ge1\). Therefore two negative \(z\)-roots occur precisely in the stated small-wavenumber region, while all \(z\)-roots are positive above cutoff. At a simple zero of \(Q\), precisely two roots of \(P\) coincide. Continuity determines their negative/positive sign at the lower/upper transition.

Finally, \(Q_0(t)=(t-2)^2(4t+1)\). Its expansion near \((u,t)=(0,2)\) is \(9(t-2)^2-216u+O(|t-2|^3+u|t-2|+u^2)\), giving \(t_\pm=2\pm2\sqrt6\sqrt u+O(u)\). Near \((u,t)=(1/4,0)\), one has \(\partial_tQ=-27/4\) and \(\partial_uQ=-81/4\). The implicit function theorem then gives \(t_-=3(1/4-u)+O((1/4-u)^2)\). Factoring \(Q_{1/4}(t)=t(4t^2-18t-27/4)\) yields the quoted cutoff.

## Verification

The self-contained `check.py` verifies twelve exact discriminant, endpoint, and Taylor identities with symbolic arithmetic; tests the mode-type classification for 2,500 randomly generated positive density ratios (15,000+ mode groups); and checks both asymptotic limits. The exact identities and root-sign proof, rather than finite sampling, establish the claim. Run `python check.py` with Python 3, SymPy and NumPy. No time-domain simulation or finite-temperature calculation is claimed.

## Relationship to prior work

The cold multistream dielectric function is standard. Cuperman, Gomberoff and Roth (1978) study the **same three-electron-population family** in a general nonsymmetric parametrization, including stationary background electrons and standing/travelling modes. Their accessible abstract already establishes qualitative mode changes, which are not claimed new here. The proposed contribution is the exact *symmetric-subfamily density threshold*, complete root-type partition for every positive density and wavenumber, and square-root/linear transition-width laws; these quantitative consequences were not verified as stated in the accessible comparison. The complete 1978 article was inaccessible and may already contain an equivalent treatment; this is a substantial priority risk, not proof of absence.

Bawa'aneh et al. (2009) analyze a related sixth-order cold dispersion numerically, but their three species are **one mobile ion population and two oppositely drifting electron populations**. Their ion pole and current-neutrality parameterization do not imply this stationary-electron three-population discriminant. The earlier exact two-stream peak/cutoff formula has only two electron poles and does not imply the cubic discriminant topology here.

## Limitations

These are algebraic temporal normal modes of the ideal cold longitudinal model. At the real-frequency double-root cutoff, secular growth is not excluded. The cold delta-distribution idealization can change qualitatively at nonzero temperature or with magnetic fields. Historical priority remains uncertain because the complete highly relevant 1978 primary paper could not be inspected. A public online date of 2009-03-13 is used as day-precision documentary evidence for that 1978 paper; it is **not** asserted to be its original publication date.

## References

1. S. Cuperman, L. Gomberoff and I. Roth, “Three component non-symmetric counter-streaming instabilities: longitudinal electron plasma modes,” *Journal of Plasma Physics* **19** (1978), 1–14. DOI: 10.1017/S0022377800023618. Original February 1978 issue; Cambridge's online posting lists 2009-03-13.
2. S. Cuperman, M. Mond, I. Roth and L. Gomberoff, “Temperature effects in non-symmetric three-component counter-streaming electron plasmas,” *Journal of Plasma Physics* **19** (1978), 461–473.
3. M. S. Bawa'aneh, G. Assayed, M. Shatnawi, G. Alna'washi and S. Al-Awfi, “Multistream Instability in Two and Three-Species Plasmas,” *Jordan Journal of Physics* **2** (2009), 113–123.
4. A. Bret, M.-C. Firpo and C. Deutsch, “Collective electromagnetic modes for beam-plasma interaction in the whole k space,” *Physical Review E* **70** (2004), 046401. DOI: 10.1103/PhysRevE.70.046401 (distinct two-population setting).
