# All-period orbit lifting and two distinct chaotic statistical phases of a switched logistic map

## Finding
For the switched-logistic interval family of Cassal-Quiroga, Gilardi-Velázquez and Campos-Cantón, changing the sign of its one parameter leaves every orbit of the *absolute-value* dynamics unchanged but reorganizes **every nonzero primitive periodic orbit** and the ergodic components. The exact rearrangement is as follows. Every primitive logistic orbit of length \(p\) lifts to two primitive length-\(p\) orbits for negative parameter. For positive parameter it lifts to one length-\(2p\) orbit when \(p\) is odd, or to two length-\(p\) orbits when \(p\) is even. The zero fixed point is counted just once.

With \(P_n(a)=\#\operatorname{Fix}(L_a^n)\), the fixed-point counts are
\[
\#\operatorname{Fix}(F_{-a}^{n})=2P_n(a)-1,
\qquad
\#\operatorname{Fix}(F_{a}^{n})=
\begin{cases}1,&n\text{ odd},\\2P_n(a)-1,&n\text{ even}.
\end{cases}
\]
The entire Artin–Mazur zeta functions obey the identities
\[
\boxed{\zeta_{F_{-a}}(t)=(1-t)\zeta_{L_a}(t)^2,\qquad
\zeta_{F_a}(t)=(1+t)\zeta_{L_a}(t)\zeta_{L_a}(-t).}
\]
At the two fully chaotic endpoints,
\[
\boxed{\zeta_{F_{-4}}(t)=\frac{1-t}{(1-2t)^2},\qquad
\zeta_{F_4}(t)=\frac{1+t}{1-4t^2}.}
\]
Although both endpoint maps have topological entropy \(\log 2\), their absolutely continuous invariant probability measures behave differently. The negative-endpoint map has two mixing ergodic measures on disjoint sign halves. The positive-endpoint map has one ergodic absolutely continuous invariant measure but is not mixing: its sign function oscillates with period two.

## Assumptions and scope
Let \(0<a\le4\) be arbitrary, not necessarily rational. Set
\[
F_\alpha(x)=\begin{cases}-\alpha x(1+x),&-1\le x\le0,\\
\alpha x(x-1),&0<x\le1,\end{cases}
\qquad L_a(r)=a r(1-r),\quad 0\le r\le1.
\]
The interval \([-1,1]\) is forward invariant for both \(\alpha=a\) and \(\alpha=-a\). Let \(\operatorname{Fix}(G^n)\) mean all distinct fixed points of the \(n\)-fold iterate, including shorter periods, and let \(\zeta_G(t)=\exp(\sum_{n\ge1}\#\operatorname{Fix}(G^n)t^n/n)\), interpreted as a formal power series. Every count is finite because the logistic iterates are nonidentity polynomials. The measure-theoretic statements below concern **only \(a=4\)** and absolutely continuous invariant probability measures (ACIPs). Measure-theoretic mixing is with respect to each specified ACIP.

## Proof
**1. Signed-amplitude decomposition and exact orbit lifting.** For every \(x\ne0\), define \(r=|x|\) and \(s=\operatorname{sgn}(x)\). Direct substitution in the two branches gives
\[
|F_{\pm a}(x)|=L_a(r),\qquad
F_{-a}(x)=sL_a(r),\qquad F_a(x)=-sL_a(r).
\]
A periodic orbit with \(r>0\) cannot pass through \(r=0\), for it would then remain at the absorbing fixed point zero. Therefore, on each nonzero periodic orbit, the sign is preserved by \(F_{-a}\) and reversed at every step by \(F_a\). Let the amplitude have least period \(p\). The first map gives two separate signed cycles, each of period \(p\). For the second, simultaneous return of sign and amplitude requires the least positive multiple of \(p\) that is even: this is \(2p\) for odd \(p\), giving a single signed cycle covering both signs, and \(p\) for even \(p\), giving two disjoint signed cycles. Distinct amplitude orbits lift disjointly. This proves the primitive-orbit assertion without assuming hyperbolicity or excluding nonzero critical points.

**2. Fixed points and zeta products.** The amplitude of a fixed point of the \(n\)-iterate must be fixed by \(L_a^n\). Every nonzero amplitude fixed point gives two points for \(F_{-a}^n\). For \(F_a^n\), these two lifts return only when \(n\) is even. Accounting for the single shared zero yields the displayed fixed-point formulas. Writing \(P_n=P_n(a)\) and using formal logarithms,
\[
\log\zeta_{F_{-a}}(t)=\sum_{n\ge1}(2P_n-1)\frac{t^n}{n}
=2\log\zeta_{L_a}(t)+\log(1-t).
\]
For the positive parameter, the fixed count is \(1+(1+(-1)^n)(P_n-1)\). Thus
\[
\begin{aligned}
\log\zeta_{F_a}(t)
&=\sum_{n\ge1}\frac{t^n}{n}
+\sum_{n\ge1}(1+(-1)^n)(P_n-1)\frac{t^n}{n}\\
&=\log(1+t)+\log\zeta_{L_a}(t)+\log\zeta_{L_a}(-t).
\end{aligned}
\]
Exponentiating establishes the universal identities. There are at most \(2^n\) logistic fixed points, so all displayed series also converge for sufficiently small \(|t|\).

**3. Exact chaotic-endpoint counts.** The homeomorphism \(h:[0,1]\to[0,1]\), \(h(u)=\sin^2(\pi u/2)\), conjugates \(L_4\) to the full tent map \(T(u)=2u\) on \([0,1/2]\), and \(T(u)=2(1-u)\) on \([1/2,1]\). The \(n\)-fold tent iterate has exactly \(2^n\) monotone full branches of slope \(\pm2^n\). Each inverse branch is a contraction of \([0,1]\) into itself, hence possesses exactly one fixed point. Distinct inverse branches cannot share a periodic boundary point: all nontrivial branch boundaries eventually reach \(1/2\), then \(1\), then \(0\), never to return to themselves; the endpoint \(0\) belongs to a unique periodic itinerary. Consequently \(P_n(4)=2^n\). It follows that \(\zeta_{L_4}(t)=(1-2t)^{-1}\), and substituting this into the universal identities gives both asserted rational functions.

**4. Absolutely continuous endpoint measures.** The tent map preserves Lebesgue measure, and its \(2^n\) inverse branches at level \(n\) map \([0,1]\) onto the dyadic intervals of length \(2^{-n}\). Its Perron–Frobenius operator \(P\) acts by taking the average over these inverses. For every continuous test density \(g\), the function \(P^n g(y)\) is a Riemann sum with one point in each dyadic interval and hence converges uniformly in \(y\) to \(\int_0^1 g\). Because \(P\) is an \(L^1\)-contraction, density of continuous functions extends convergence to all \(L^1\) functions. This is exactness of \(T\), implying that all positive powers are mixing and each has a unique ACIP. Conjugating by \(h\) yields the unique ACIP of \(L_4\), with density
\[
\rho(r)=\frac1{\pi\sqrt{r(1-r)}},\qquad 0<r<1,
\]
whose total mass is one (the arcsine integral). Its positive iterates are mixing. Define \(\mu_+\) and \(\mu_-\) by pushing this logistic measure onto the positive and negative half-intervals, respectively. For \(F_{-4}\) both are invariant, mixing and ergodic. Any ACIP of \(F_{-4}\) restricts to ACIPs of \(L_4\) on the two invariant halves and is therefore exactly \(c\mu_++(1-c)\mu_-\), \(0\le c\le1\).

For \(F_4\), the map swaps the two nonzero half-intervals; \(\nu=(\mu_++\mu_-)/2\) is invariant, with density \(\rho(|x|)/2\) on each half. If an ACIP of \(F_4\) exists, its two half-interval restrictions have equal mass \(1/2\), and the normalized restrictions are ACIPs of \(L_4^2\). Uniqueness for \(L_4^2\) forces both to be \(\mu_+\) or \(\mu_-\) respectively. Hence \(\nu\) is the unique ACIP. An invariant set for \(F_4\) intersects each half in an \(L_4^2\)-invariant set, so exactness of \(L_4^2\) proves ergodicity of \(\nu\). But \(\operatorname{sgn}(F_4(x))=-\operatorname{sgn}(x)\) away from the zero-mass origin, so the sign observable has Koopman eigenvalue \(-1\) and correlations \((-1)^n\); therefore \(F_4\) is not mixing. Its square is mixing on each half with normalized restriction \(\mu_\pm\).

**5. Entropy.** Both endpoint maps factor onto \(L_4\) by \(x\mapsto|x|\). For \(F_{-4}\), each invariant half is conjugate to \(L_4\), so the topological entropy is \(\log2\). For \(F_4^2\), the two invariant halves are conjugate to \(L_4^2\), hence its entropy is \(2\log2\). The identity \(h_{\mathrm{top}}(G^2)=2h_{\mathrm{top}}(G)\) for a continuous compact-space map gives \(h_{\mathrm{top}}(F_4)=\log2\).

## Verification
The accompanying `verify_signed_logistic.py` enumerates every inverse affine branch of the full tent map for \(1\le n\le12\), solves its fixed-point equation using exact fractions, checks each solution under \(n\) exact forward iterations, and confirms that there are exactly \(2^n\) distinct solutions. It then reproduces the two signed fixed-point sequences and tests the absence of nonzero odd-period cycles for positive parameter. These are finite sanity checks; the all-parameter and all-period conclusions follow from the proof, not from enumeration.

## Relationship to prior work
Cassal-Quiroga, Gilardi-Velázquez and Campos-Cantón introduced and investigated this exact piecewise logistic map and its coexisting fixed points, low-period bifurcations and chaotic behavior. Their complete accessible author manuscript contains the signed branch equations, a short-period analysis and numerical bifurcation studies. The new content here is the **exact global orbit-lifting law for every period and every nonzero parameter**, both full zeta identities, and the sharp endpoint contrast between two mixing ergodic ACIPs and one ergodic but nonmixing ACIP.

The conjugacy of the full logistic map to a full tent map, exact arcsine invariant density, the abstract Artin–Mazur formalism, finite-fiber extension methods, and general dynamical-zeta results are classical and are **not** claimed as new. In particular, standard finite-extension theory accounts for why sign flipping can produce a period-two ergodic decomposition. The explicit complete applications to this parameter family and the resulting paired exact invariants are the point of the finding.

## Limitations
This is not a classification of the invariant measures of general logistic parameters, not a statement of uniqueness among *all* invariant probability measures, and not a new theory of zeta functions or exact dynamical systems. Unindexed earlier exact calculations for this signed family may exist. The paper's printed 2022 journal year and the December 30, 2022 online record are distinguished from its September 2022 internal manuscript timestamp and January 2023 author upload; the earliest publicly verified date used here is December 30, 2022. Exact arithmetic verification covers only the finite stated range, although the proof applies to every positive integer period.

## References
1. B. B. Cassal-Quiroga, H. E. Gilardi-Velázquez and E. Campos-Cantón, “Multistability Analysis of a Piecewise Map via Bifurcations,” *International Journal of Bifurcation and Chaos* **32** (2022), 2250241. DOI: 10.1142/S0218127422502418. Full author manuscript: https://www.researchgate.net/publication/367158595_Multistability_Analysis_of_a_Piecewise_Map_via_Bifurcations.
2. K. Scheicher, V. F. Sirvent and P. Surer, “Dynamical properties of the tent map,” *Journal of the London Mathematical Society* (2016). DOI: 10.1112/jlms/jdv071.
3. D. Galli and M. Lenci, “Extensions of exact and K-mixing dynamical systems” (2022). arXiv:2203.11822. The general finite-fiber ergodic decomposition is prior work.
4. D. Ruelle, “Dynamical zeta functions for maps of the interval,” *Bulletin of the American Mathematical Society* **30** (1994), 212–214. General zeta-function framework.
5. A. Pakapongpun and T. Ward, “Orbits for products of maps,” *Thai Journal of Mathematics* **12** (2014), 33–44. Product-map comparisons, not a theorem concerning this switched logistic map.
