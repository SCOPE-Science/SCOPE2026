# Complete equilibrium census and unstable-index split for the Chen hyperchaotic benchmark
## Finding
For the Chen hyperchaotic system \(\dot p=-qr+5p\), \(\dot q=pr-10q\), \(\dot r=pq/3-(19/5)r+s/5\), and \(\dot s=p/10+qr/2+(21/20)s\), the real equilibrium set consists exactly of the origin and four nonzero points. Writing \(\varepsilon,\delta\in\{-1,1\}\) and \(q_\delta=(26+\delta\sqrt{70501})/35\), the four nonzero equilibria are \(E_{\varepsilon,\delta}=(\varepsilon\sqrt2\,q_\delta,q_\delta,5\varepsilon\sqrt2,-(52/21)\varepsilon\sqrt2\,q_\delta)\). The origin is hyperbolic with unstable dimension two, while every \(E_{\varepsilon,\delta}\) is hyperbolic with unstable dimension three.

At the parameter values \(f=5\), \(g=-10\), \(j=-19/5\), and \(l=1/10\) used for the Chen system in the 2023 synchronization study, the origin is therefore not the whole equilibrium geometry. There are four additional real hyperbolic equilibria, and their unstable dimension is three rather than the origin's unstable dimension two.

## Assumptions and scope
The statement concerns the exact four-dimensional autonomous vector field
\[
\dot p=-qr+5p,\qquad
\dot q=pr-10q,
\]
\[
\dot r=\frac13pq-\frac{19}{5}r+\frac15s,\qquad
\dot s=\frac1{10}p+\frac12qr+\frac{21}{20}s.
\]
All equilibria are real. The classification is for this parameter vector only. The result concerns equilibria and their linear unstable dimensions; it does not assert existence, uniqueness, or basin structure of any chaotic or hyperchaotic attractor, and it does not invalidate the synchronization constructions merely from the existence of the four additional equilibria.

## Proof
At an equilibrium, suppose first that \(q=0\). The first equation gives \(p=0\); then the fourth gives \(s=0\), and the third gives \(r=0\). Hence the origin is the only equilibrium with \(q=0\).

Now let \(q\ne0\). The first two equilibrium equations give
\[
p=\frac{qr}{5},\qquad pr=10q,
\]
so
\[
r^2=50.
\]
Thus for some \(\varepsilon\in\{-1,1\}\),
\[
r=5\varepsilon\sqrt2,\qquad p=\varepsilon\sqrt2\,q.
\]
Using \(qr=5p\) in the fourth equilibrium equation gives
\[
s=-\frac{52}{21}p.
\]
Substitution into the third equation, followed by multiplication by the nonzero common denominator, reduces exactly to
\[
35q^2-52q-1995=0.
\]
Its discriminant is \(282004=4\cdot70501\), so the two real roots are
\[
q_\delta=\frac{26+\delta\sqrt{70501}}{35},\qquad \delta\in\{-1,1\}.
\]
Each pair \((\varepsilon,\delta)\) determines exactly one equilibrium
\[
E_{\varepsilon,\delta}=
\left(
\varepsilon\sqrt2\,q_\delta,
q_\delta,
5\varepsilon\sqrt2,
-\frac{52}{21}\varepsilon\sqrt2\,q_\delta
\right).
\]
Together with the origin, these are exactly the five real equilibria.

At the origin the Jacobian is diagonal and its eigenvalues are
\[
5,\quad -10,\quad -\frac{19}{5},\quad \frac{21}{20},
\]
so the origin is hyperbolic with unstable dimension two.

For a nonzero equilibrium, elimination with \(35q^2-52q-1995=0\) reduces the characteristic polynomial to
\[
P_q(\lambda)=\lambda^4+\frac{31}{4}\lambda^3+
\left(-\frac{25}{42}q-\frac{231}{25}\right)\lambda^2+
\left(\frac{9896}{525}q+760\right)\lambda-
\frac{52}{5}q-798.
\]
The first column of its Routh array is
\[
1,\quad \frac{31}{4},\quad B(q),\quad C(q),\quad -\frac{52}{5}q-798,
\]
where
\[
B(q)=-\frac{98543}{32550}q-\frac{83161}{775}
\]
and, after the same quadratic reduction,
\[
C(q)=
\frac{2588408117026q+47022920375235}
{1810727625q+64179501750}.
\]
Since \(265^2<70501<266^2\), both roots \(q_\delta\) lie in \((-7,9)\). On this interval, \(B(q)<B(-7)=-400423/4650<0\). Both the numerator and denominator defining \(C(q)\) are increasing affine functions and are already positive at \(q=-7\), where they equal \(28904063556053\) and \(51504408375\), respectively. Finally, \(-52q/5-798<-3626/5<0\). Hence the Routh first-column signs are
\[
+,+,-,+,-,
\]
with three sign changes and no zero entry. Therefore every nonzero equilibrium is hyperbolic and has exactly three eigenvalues in the open right half-plane.

## Verification
The accompanying `verify.py` uses only exact rational arithmetic and an explicit quadratic extension for \(\sqrt2\). It verifies the equilibrium substitutions, derives the characteristic polynomial at both signs of \(r\), reduces all coefficients modulo \(35q^2-52q-1995\), verifies the stated Routh-column formulas, and checks the sign bounds used in the proof. Running `python3 verify.py` returns `VERIFY_OK`.

The computation is a replay of exact symbolic identities, not a numerical search for equilibria or eigenvalues. The exhaustive equilibrium count follows from the algebraic case split \(q=0\) versus \(q\ne0\), and the unstable dimensions follow from the exact Routh sign counts.

## Relationship to prior work
The 2023 synchronization paper writes this Chen system with the stated parameter values and explicitly introduces the origin as a specific equilibrium point before giving its four eigenvalues. Its accessible full text does not provide a complete real-equilibrium census or the unstable-index classification above. Exact-equation, parameter, radical, title, DOI, and implication searches did not locate a published statement equivalent to this five-equilibrium classification.

A particularly close database hit titled “Five-equilibrium correction for a four-dimensional chaos generator” was inspected because its conclusion sounded potentially dominating. Its vector field is instead \(\dot x=-12x+yz+w^2/20-2/5\), \(\dot y=8y-xz+w|y|\), \(\dot z=xy-45z\), \(\dot w=w-10z\), so it is a different model and does not imply the present claim.

The 2009 paper that introduced the Chen hyperchaotic system is the strongest plausible earlier source. Its accessible abstract confirms the same hyperchaotic-system provenance and synchronization theme, but a lawful full-text copy was not available for complete statement-level comparison in this review. That access limitation is retained as an originality risk rather than treated as evidence of novelty.

## Limitations
The theorem is parameter-specific. It does not classify equilibria for arbitrary \((f,g,j,l)\), determine the stable manifolds of the five equilibria, prove whether the numerically studied hyperchaotic set intersects their neighborhoods, or assess the success of any controller or synchronization law. Originality searching cannot exclude an unindexed result or a statement inside the inaccessible 2009 full text.

## References
1. M. M. El-Dessoky, N. Almohammadi, and E. Alzahrani, “Control and adaptive modified function projective synchronization of different hyperchaotic dynamical systems,” *AIMS Mathematics* 8 (2023), 23620–23640, DOI: 10.3934/math.20231201, published 31 July 2023.
2. C.-H. Chen et al., “A new hyper-chaotic system and its synchronization,” *Nonlinear Analysis: Real World Applications* 10 (2009), 2088–2096, DOI: 10.1016/j.nonrwa.2008.03.015.
3. MSC2020, \(37N35\), dynamical systems in engineering.
