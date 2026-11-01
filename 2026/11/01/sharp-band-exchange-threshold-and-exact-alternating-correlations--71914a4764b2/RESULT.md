# Sharp band-exchange threshold and exact alternating correlations in a tunable skew tent map

## Finding
For the deterministic generalized skew tent family 
\[
F_{a,b}(x)=\begin{cases}
a+(1-a)x/b,&0\le x\le b,\\
(1-x)/(1-b),&b<x\le1,
\end{cases}
\qquad 0<a<1,\quad0<b<1,
\]
write \(t=(2-b)^{-1}\) and \(I_-=[0,t]\), \(I_+=[t,1]\). There is an exact exchange of these two adjacent intervals, \(F(I_-)=I_+\), \(F(I_+)=I_-\), if and only if \(a\ge t\). Moreover, **any** two nondegenerate closed adjacent intervals partitioning \([0,1]\) that exchange exactly under this map have the same dividing point \(t\). Thus \(a=t\) is the sharp exchange onset in the \((a,b)\) parameter plane.

On the boundary curve \(a=t\), put \(q=b(2-b)\) and \(\lambda=1-2q\). A unique absolutely continuous invariant probability \(\mu_b\) has density
\[
h_b(x)=\begin{cases}(2-b)/2,&0<x<t,\\
(2-b)/[2(1-b)],&t<x<1.
\end{cases}
\]
This measure is ergodic but **not mixing**: the interval indicator centered as \(S(x)=-1\) on \(I_-\) and \(+1\) on \(I_+\) satisfies \(S\circ F=-S\) almost everywhere and
\[
\mathbb E_{\mu_b}[S(X_0)S(X_n)]=(-1)^n.
\]
Nevertheless the two-step map restricted to either interval is exact (indeed measurably isomorphic to a full-branch skew-tent Bernoulli map). Its positive Lyapunov exponent and metric entropy per physical iteration both equal
\[
\frac12[-q\log q-(1-q)\log(1-q)]>0.
\]

The physical coordinate has stationary mean \(\bar x=(1+2t)/4\) and for every \(m\ge0\) the exact one-step-clock covariances are
\[
\begin{aligned}
C_{2m}&=\operatorname{Cov}_{\mu_b}(X_0,X_{2m})
=\frac1{16}+\frac{t^2+(1-t)^2}{24}\lambda^m,\\
C_{2m+1}&=\operatorname{Cov}_{\mu_b}(X_0,X_{2m+1})
=-\frac1{16}+\frac{t(1-t)(q-1)}{12}\lambda^m.
\end{aligned}
\]
Since \(|\lambda|<1\), the coordinate correlation approaches an alternating nonzero value, even while the internal mixing contribution decays exponentially.

## Assumptions and scope
All statements concern the closed unit interval with the above continuous two-branch map and \(0<b<1\), \(0<a<1\). Interval images are set-theoretic images. Endpoints carry zero mass for the stated absolutely continuous invariant measure. The fixed point \(t\) supports the additional invariant Dirac measure \(\delta_t\), so the uniqueness statement is explicitly **only among absolutely continuous invariant probabilities**, not all invariant probabilities. Statements on density, entropy, ergodicity and correlations require \(a=t\); the band-exchange criterion holds on the entire stated parameter domain. The logarithm is natural, and covariances are for the original one-step map, not its squared return alone.

## Proof
**1. The sharp exchange boundary.** If \([0,s]\) and \([s,1]\) are exchanged and \(s<b\), then the upper interval contains the turning point \(b\) with image \(F(b)=1>s\), a contradiction. Therefore \(s\ge b\), where the right branch maps \([s,1]\) onto \([0,(1-s)/(1-b)]\). Equality with \([0,s]\) gives \(s=(1-s)/(1-b)\), hence \(s=t=1/(2-b)\), and indeed \(t>b\). The left interval maps onto \([\min\{a,t\},1]\), because it contains the peak and the segment from \(b\) to \(t\) maps from 1 down to \(t\). Equality with \([t,1]\) is equivalent to \(a\ge t\). Conversely these equalities verify both exchanges.

**2. Explicit two-step conjugacy at the boundary.** At \(a=t\), introduce lower normalized coordinate \(u=x/t\) and upper coordinate \(v=(x-t)/(1-t)\). The physical one-step transitions are
\[
I_-:\quad u\longmapsto v=T_q(u),\qquad
I_+:\quad v\longmapsto u=1-v,
\]
where \(q=b/t=b(2-b)\), and
\[
T_q(u)=\begin{cases}u/q,&0\le u\le q,\\ (1-u)/(1-q),&q<u\le1.\end{cases}
\]
Direct substitution on the lower rising and falling branches gives exactly these two formulas; for example, \(v=(1-u)/(1-q)\) on the falling branch. The second iterate on the lower normalized interval is \(V_q(u)=1-T_q(u)\); on the upper interval it is \(T_q(1-v)\), conjugate via reflection. Both are full-branch, piecewise-affine expanding maps with inverse-branch lengths \(q\) and \(1-q\). Their Lebesgue preserving property follows by inverse-branch Jacobian summation \(q+(1-q)=1\). Iterated inverse cylinders shrink geometrically, and the corresponding digit process is independent Bernoulli with probabilities \(q,1-q\). Thus each squared restriction is exact, mixing, and has unique absolutely continuous invariant probability: normalized Lebesgue on its interval. The physical map exchanges the two intervals, hence its unique absolutely continuous invariant probability assigns them equal masses and has the displayed piecewise constant density. An invariant set for \(F\) must be invariant for the exact return in each interval and must have equal conditional masses; thus \(F\) is ergodic. The sign \(S\) switches each physical step, proving nonmixing. The return entropy is \(-q\log q-(1-q)\log(1-q)\), and both entropy and Lyapunov exponent of physical time are half of this quantity.

**3. Covariance computation in the physical clock.** Each band has conditional mass \(1/2\), and the conditional coordinate means are \(t/2\) and \((t+1)/2\), differing by exactly \(1/2\). Their between-band covariance contribution is \((-1)^n/16\). Write \(f(u)=u-1/2\) for the centered coordinate. The Perron operator of \(V_q\) acts on this affine function as
\[
P_{V_q}f=(1-2q)f=\lambda f,
\]
which follows directly from its two inverse branches \(q(1-y)\) and \(q+(1-q)y\). Its upper-band conjugate has the same centered-coordinate eigenvalue. Therefore the within-band covariance at lag \(2m\), after weighting both sectors equally, equals \([t^2+(1-t)^2]\lambda^m/24\). For the odd lag, \(\operatorname{Cov}(U,T_q(U))=(2q-1)/12\) and \(\operatorname{Cov}(V,1-V)=-1/12\) for independent separately uniform initial \(U,V\). Multiplying by the original-coordinate scales \(t(1-t)\), by the sector masses \(1/2\), and then by \(\lambda^m\) for the intervening \(2m\) steps gives \(t(1-t)(q-1)\lambda^m/12\). Adding the alternating between-band term proves both formulas for every \(m\ge0\). The stated mean is the average of the two sector means.

## Verification
The accompanying standalone program `checker.py` performs direct exact-rational integration of \((x-\bar x)(F^n(x)-\bar x)\) over all refined affine itinerary intervals with their correct piecewise constant invariant weights. It verifies 55 exact identities for \(b\in\{1/5,1/4,1/3,1/2,3/4\}\) and horizons \(0\le n\le10\). These finite tests verify the branch/integral arithmetic; the unrestricted theorem follows from the above analytic conjugacy and Perron-operator identities, not from enumeration.

## Relationship to prior work
Moysis, Lawnik, Baptista, Goudos and Volos introduced the tunable-endpoint piecewise-map construction in 2023 conference work, with the generalized skew tent map and its numerical analysis developed in the extended Moysis et al. *Symmetry* article in December 2023. The latter describes numerical Lyapunov and mean plots, and discusses solving the Frobenius–Perron equation as an alternative; no sharp band-exchange boundary or physical-clock covariance theorem is stated in the inspected relevant sections. Rogers, Shorten, Heffernan and Naughton (2008) develop general matrix methods to prescribe invariant densities and autocorrelations of piecewise-linear maps; those methods and the classical Bernoulli skew-tent coding preexist this finding. The present contribution is the parameter-exact exchange transition and its deterministic, original-time statistical classification for this specific tunable-endpoint family, not a new general transfer-operator method.

## Limitations
The exact density/correlation/entropy formulas are asserted **only** on \(a=1/(2-b)\), not on the open exchange region \(a>1/(2-b)\). No mixing claim is made for the original physical map; it is provably not mixing. The existence of fixed-point Dirac and other singular invariant measures is not excluded. General piecewise-Markov operator theory may allow alternative derivations; independent priority examination, particularly of inverse Frobenius–Perron and autocorrelation construction literature, has not been performed. Finite checker tests do not certify the infinite result.

## References
1. L. Moysis, M. Lawnik, M. S. Baptista, S. Goudos and C. Volos, *Construction of Piecewise Chaotic Maps With Tunable Statistical Mean*, MOCAST 2023 (publicly catalogued 17 July 2023), doi:10.1109/MOCAST57943.2023.10176612.
2. L. Moysis, M. Lawnik, C. Volos, M. S. Baptista and S. K. Goudos, *Chaotic Maps with Tunable Mean Value—Application to a UAV Surveillance Mission*, Symmetry 15 (2023), 2138, doi:10.3390/sym15122138.
3. A. Rogers, R. Shorten, D. M. Heffernan and T. J. Naughton, *Synthesis of Piecewise-Linear Chaotic Maps: Invariant Densities, Autocorrelations, and Switching*, International Journal of Bifurcation and Chaos 18 (2008), 2169–2189, doi:10.1142/S0218127408021646.
