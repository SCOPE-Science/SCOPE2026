# Branch-balance variance corridor and extremal rigidity in the Belykh map
## Finding
Consider the Belykh map on
\[
K=[-1,1]^2
\]
with
\[
-1<k<1,\qquad 0<\lambda<1,\qquad 1<\gamma\le \frac{2}{1+|k|}.
\]
Let
\[
K_1=\{(x,y):y>kx\},\qquad K_2=\{(x,y):y<kx\},
\]
and let the map be
\[
f(x,y)=
\begin{cases}
(\lambda x+(1-\lambda),\ \gamma y-(\gamma-1)),&(x,y)\in K_1,\\
(\lambda x-(1-\lambda),\ \gamma y+(\gamma-1)),&(x,y)\in K_2.
\end{cases}
\]
Write \(S=1\) on \(K_1\) and \(S=-1\) on \(K_2\). For every invariant Borel probability measure \(\mu\) satisfying \(\mu(\{y=kx\})=0\), define
\[
m=\mathbb E_\mu S.
\]
Then
\[
\boxed{\mathbb E_\mu X=\mathbb E_\mu Y=\mathbb E_\mu S=m}.
\]
In particular, the upper-branch mass is exactly
\[
\mu(K_1)=\frac{1+m}{2}.
\]

Put
\[
c=\frac{1-\lambda}{1+\lambda},\qquad d=\frac{\gamma-1}{\gamma+1}.
\]
The coordinate variances obey the sharp stationary corridor
\[
\boxed{c^2(1-m^2)\le \operatorname{Var}_\mu(X)\le 1-m^2},
\]
\[
\boxed{d^2(1-m^2)\le \operatorname{Var}_\mu(Y)\le 1-m^2}.
\]

For \(|m|<1\), equality in either upper bound occurs exactly for
\[
\mu=\frac{1+m}{2}\delta_{(1,1)}+\frac{1-m}{2}\delta_{(-1,-1)}.
\]
Equality in either lower bound occurs exactly when
\[
m=0,\qquad d+kc>0,
\]
and \(\mu\) is the uniform probability on the branch-alternating two-cycle
\[
(-c,d)\longleftrightarrow(c,-d).
\]
When \(|m|=1\), the only invariant probability is the corresponding corner Dirac mass. Thus any invariant state that is neither a fixed-corner mixture nor the admissible alternating two-cycle lies strictly inside the relevant variance boundaries.

## Assumptions and scope
The discontinuity line
\[
N=\{(x,y):y=kx\}
\]
is excluded from the map domain. The invariant probabilities considered here satisfy \(\mu(N)=0\), so the branch signal is defined almost surely and \(f_*\mu=\mu\) is meaningful. No ergodicity, absolute continuity, mixing, or existence theorem is assumed.

The public source used to anchor the object is Persson's arXiv version from 31 October 2005. It gives the same normalized Belykh map, parameter range, and primary MSC \(37D50\). A later corrigendum states that the proof of Persson's main absolute-continuity result is incomplete. The present theorem does not use that result: only the explicit branch formulas are used.

## Proof
The branch formulas can be written
\[
X'=\lambda X+(1-\lambda)S,
\qquad
Y'=\gamma Y-(\gamma-1)S.
\]
Invariance gives
\[
\mathbb E X=\lambda\mathbb E X+(1-\lambda)\mathbb E S
\]
and
\[
\mathbb E Y=\gamma\mathbb E Y-(\gamma-1)\mathbb E S,
\]
so
\[
\mathbb E X=\mathbb E Y=\mathbb E S=m.
\]
Since \(S\in\{-1,1\}\),
\[
\operatorname{Var}(S)=1-m^2.
\]
Let
\[
s^2=1-m^2,
\qquad V_X=\operatorname{Var}(X),
\qquad C_X=\operatorname{Cov}(X,S).
\]
After centering the first branch equation and using stationarity,
\[
(1+\lambda)V_X=(1-\lambda)s^2+2\lambda C_X.
\]
Cauchy--Schwarz gives
\[
|C_X|\le \sqrt{V_X}s.
\]
For \(s>0\), put \(t=\sqrt{V_X}/s\). Then
\[
\left|(1+\lambda)t^2-(1-\lambda)\right|\le 2\lambda t.
\]
Factoring the two scalar inequalities yields
\[
\frac{1-\lambda}{1+\lambda}\le t\le1,
\]
which is the stated \(X\)-variance corridor.

Similarly, with \(V_Y=\operatorname{Var}(Y)\) and \(C_Y=\operatorname{Cov}(Y,S)\), stationarity gives
\[
(\gamma+1)V_Y+(\gamma-1)s^2=2\gamma C_Y.
\]
Cauchy--Schwarz and \(u=\sqrt{V_Y}/s\) give
\[
\frac{\gamma-1}{\gamma+1}\le u\le1,
\]
proving the \(Y\)-corridor.

For the upper boundary, equality in either Cauchy--Schwarz step forces the corresponding centered coordinate to equal the centered branch signal. Thus equality in the \(X\) upper bound gives \(X=S\) almost surely, while equality in the \(Y\) upper bound gives \(Y=S\) almost surely. In either case invariance then gives \(S'=S\) almost surely. The other coordinate defect evolves by a strict scalar multiplier: respectively
\[
Y'-S'=\gamma(Y-S)
\]
or
\[
X'-S'=\lambda(X-S).
\]
Stationarity of its square forces the defect to vanish because \(\gamma>1\) or \(0<\lambda<1\). Hence \((X,Y)=(S,S)\) almost surely, giving exactly the corner mixture with weights determined by \(m\). The cases \(m=\pm1\) reduce to the two corner atoms.

For the lower \(X\)-boundary, equality gives
\[
X-m=-c(S-m).
\]
Applying the same identity one time step later and inserting the branch dynamics gives
\[
S+S'=2m
\]
almost surely. If \(|m|<1\), the left side can take only \(-2,0,2\), while it is almost surely constant; hence \(m=0\) and \(S'=-S\). Therefore
\[
X=-cS.
\]
Set \(W=Y-dS\). Under \(S'=-S\), direct substitution yields
\[
W'=\gamma W.
\]
Stationarity of \(W^2\) and \(\gamma>1\) gives \(W=0\), hence
\[
Y=dS.
\]
So the measure is uniform on \((-c,d)\) and \((c,-d)\). These two points lie in the asserted branches exactly when
\[
d+kc>0.
\]
The map then exchanges them, so the uniform two-cycle measure is invariant and attains the lower bound.

The lower \(Y\)-boundary is analogous: equality gives \(Y-m=d(S-m)\), hence again \(m=0\) and \(S'=-S\). Then \(Z=X+cS\) satisfies \(Z'=\lambda Z\), so stationarity and \(0<\lambda<1\) force \(Z=0\). The same alternating two-cycle is obtained.

## Verification
The bundled `verify.py` checks symbolically the variance identities, factorization of the Cauchy--Schwarz boundaries, the two-cycle equations, and the branch-admissibility condition. It was executed from the packaged path and returned `VERIFY_OK`.

The proof is analytic and applies to every invariant probability satisfying the stated domain condition. No numerical orbit, finite enumeration, or unproved limiting argument is used.

## Relationship to prior work
Persson's 2005 preprint explicitly defines the normalized Belykh branches used here and studies absolute continuity and correlation decay. The later corrigendum reports that the proof of the main absolute-continuity theorem is incomplete; the present result is independent of that theorem.

The Scholarpedia Belykh-map article gives an affinely conjugate unit-square normalization, reviews hyperbolicity and invariant-measure literature, and identifies the two branch fixed corners. The checked sources and semantic searches did not supply the branch-imbalance first-moment identity together with the two sharp variance corridors and their equality classifications.

The closest retrieved research records concern stationary variance laws for other dynamical systems or finite-support rigidity for unrelated maps. Those statements do not imply the Belykh branch-covariance identities because the affine branch signal and its coupling to one contracting and one expanding coordinate are specific here.

## Limitations
The theorem does not prove existence, uniqueness, ergodicity, or absolute continuity of a non-atomic invariant measure. It does not repair or rely on Persson's incomplete absolute-continuity proof.

The lower constants are universally valid, but the lower boundary is dynamically attainable only when \(d+kc>0\), so that the alternating pair stays off the discontinuity in the correct branches. When \(d+kc\le0\), equality in either lower bound cannot occur for an admissible invariant measure.

The originality check is a bounded literature comparison, not a proof that no equivalent statement exists under different terminology.

## References
1. T. Persson, *Absolutely continuous invariant measures for some piecewise hyperbolic affine maps*, arXiv:math/0510673v1, submitted 31 October 2005; later published in *Ergodic Theory and Dynamical Systems* 28 (2008), 211--228.
2. T. Persson, *Absolutely continuous invariant measures for some piecewise hyperbolic affine maps -- Corrigendum*, DOI 10.1017/etds.2021.77, published online 19 July 2021.
3. V. N. Belykh and I. Belykh, *Belykh map*, Scholarpedia 6(10):5545 (2011), DOI 10.4249/scholarpedia.5545.
