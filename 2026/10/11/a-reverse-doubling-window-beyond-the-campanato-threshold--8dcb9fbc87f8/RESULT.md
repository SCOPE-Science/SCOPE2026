# A reverse-doubling window beyond the Campanato threshold
## Finding
Let \((X,d,\mu)\) be a compact \(\eta\)-uniformly perfect metric-measure space with \(\eta\in(0,1)\). Assume that \(\mu\) is Borel regular and doubling, and let \(C_\mu\) be a doubling constant. Define
\[
m=\left\lceil\log_2\!\left(\frac{40}{\eta}\right)\right\rceil,
\qquad c=C_\mu^{-m},
\qquad
\kappa=\frac{\log(1/(1-c))}{\log(20/(3\eta))}>0.
\]
For every \(p\in[1,\infty)\), \(Q>0\), and
\[
Q<\lambda<\min\{Q+p,\,p+\kappa\},
\qquad
\alpha=\frac{\lambda-Q}{p},
\]
the following are equivalent:

1. \(\mu\) is lower \(Q\)-regular, meaning that there is \(A>0\) such that \(\mu(B(x,r))\ge A r^Q\) for every \(x\in X\) and \(0<r<3\operatorname{diam}X\).
2. The radius-normalized Campanato space embeds continuously into the Hölder space,
\[
L_C^{p,\lambda}(X,\mu)\hookrightarrow C^{0,\alpha}(X).
\]

The implication from lower regularity to the embedding is the sufficient direction of Górka--Stępień, Theorem 3.6(ii). The new point is the converse on the reverse-doubling window \(\lambda<p+\kappa\). Since \(\kappa>0\), this reaches strictly beyond the previously proved doubling-only range \(\lambda\le p\) whenever \(Q<p+\kappa\). If \(\kappa\ge Q\), then every \(Q<\lambda<Q+p\) satisfies \(\lambda<p+\kappa\), giving an affirmative answer to their Question 5 for that quantitative subclass.

## Assumptions and scope
The Campanato norm is
\[
\|f\|_{L_C^{p,\lambda}}
=
\|f\|_{L^p}
+
\sup_{x\in X,\,r>0}
\left(
\frac{1}{r^\lambda}
\int_{B(x,r)}|f-f_{B(x,r)}|^p\,d\mu
\right)^{1/p}.
\]
The Hölder norm is the bounded supremum norm plus the seminorm with exponent \(\alpha\). No upper \(Q\)-regularity assumption is made. The setting forces \(C_\mu>1\), so \(0<c<1\) and \(\kappa>0\). The constant \(\kappa\) is an explicit, generally nonoptimal reverse-doubling exponent obtained only from \(\eta\) and \(C_\mu\).

The range \(\lambda<Q+p\) ensures \(0<\alpha<1\). The proof of necessity uses only compactness, uniform perfectness, doubling, and the assumed continuous Campanato-to-Hölder embedding. Borel regularity is needed for the cited sufficient direction.

## Proof
Write \(D=\operatorname{diam}X\), \(\rho=\eta r/20\), and \(\sigma=3\eta/20\). First derive an explicit reverse-doubling estimate. Fix \(x\in X\) and \(0<r<D/2\). Compactness implies that some point of \(X\) lies at distance at least \(D/2\) from \(x\), so \(X\setminus B(x,r)\neq\varnothing\). Lemma 2.1 of Górka--Stępień, applied with its auxiliary point equal to \(x\), produces \(z\in X\) such that
\[
B(z,\rho)\subset B(x,r),
\qquad
x\notin B(z,4\rho).
\]
Thus \(B(x,3\rho)\) and \(B(z,\rho)\) are disjoint subsets of \(B(x,r)\). Since \(z\in B(x,r)\),
\[
B(x,r)\subset B(z,2r)\subset B(z,2^m\rho).
\]
Iterating doubling gives
\[
\mu(B(z,\rho))\ge C_\mu^{-m}\mu(B(x,r))=c\mu(B(x,r)).
\]
Consequently
\[
\mu(B(x,\sigma r))\le(1-c)\mu(B(x,r)).
\]
Iterating this inequality and interpolating between consecutive powers of \(\sigma\) yields, for \(0<s\le r<D/2\),
\[
\mu(B(x,s))
\le
A_0\left(\frac{s}{r}\right)^\kappa\mu(B(x,r)),
\qquad
A_0=(1-c)^{-1},
\]
because \(\sigma^\kappa=1-c\).

Now assume that the embedding \(L_C^{p,\lambda}(X,\mu)\hookrightarrow C^{0,\alpha}(X)\) has norm at most \(E\). Choose
\[
0<R_0<\min\left\{\frac{D}{7},\frac{\eta D}{4}\right\}.
\]
Fix \(x\in X\) and \(0<r<R_0\), and define the Lipschitz cutoff
\[
u(y)=(r-d(x,y))_+.
\]
Let \(M=\mu(B(x,r))\). Uniform perfectness, applied at radius \(r/\eta<D/2\), gives a point \(y\) with \(r\le d(x,y)<r/\eta\). Hence \(u(x)=r\), \(u(y)=0\), and
\[
[u]_{C^{0,\alpha}}
\ge
\eta^\alpha r^{1-\alpha}.
\]

We bound the Campanato seminorm of \(u\). Let \(B(w,s)\) meet \(B(x,r)\). If \(s\le r\), then \(d(w,x)<2r\), so
\[
B(w,3r)\subset B(x,5r)
\]
and doubling gives \(\mu(B(w,3r))\le C_\mu^3M\). Since \(3r<D/2\), the reverse-doubling estimate at center \(w\) gives
\[
\mu(B(w,s))
\le
A_0C_\mu^3\left(\frac{s}{r}\right)^\kappa M.
\]
Because \(u\) is one-Lipschitz, \(|u-u_{B(w,s)}|\le2s\) on \(B(w,s)\). Therefore
\[
\frac1{s^\lambda}\int_{B(w,s)}|u-u_{B(w,s)}|^p\,d\mu
\le
2^pA_0C_\mu^3 M r^{-\kappa}s^{p+\kappa-\lambda}
\le
2^pA_0C_\mu^3 M r^{p-\lambda},
\]
where the last step uses \(\lambda<p+\kappa\). If \(s>r\), Jensen's inequality, \(0\le u\le r\), and \(u=0\) on \(X\setminus B(x,r)\) give
\[
\int_{B(w,s)}|u-u_{B(w,s)}|^p\,d\mu
\le2^p r^pM,
\]
and therefore the same scale \(M r^{p-\lambda}\) after division by \(s^\lambda\). Balls disjoint from the support contribute zero. Thus, for a constant \(C_1\) depending only on the displayed structural parameters and on \(R_0,p,\lambda\),
\[
\|u\|_{L_C^{p,\lambda}}
\le
C_1 M^{1/p}r^{1-\lambda/p}.
\]

The assumed embedding now yields
\[
\eta^\alpha r^{1-\alpha}
\le
EC_1M^{1/p}r^{1-\lambda/p}.
\]
Since \(1-\alpha=1-\lambda/p+Q/p\), cancellation gives
\[
\mu(B(x,r))=M
\ge
\left(\frac{\eta^\alpha}{EC_1}\right)^p r^Q
\]
for every \(x\in X\) and every \(0<r<R_0\). For \(R_0\le r<3D\), monotonicity of ball measure and the already established bound at one fixed radius below \(R_0\) give the same lower \(Q\)-regular estimate after changing the constant. This proves necessity.

The converse follows directly from Theorem 3.6(ii) of Górka--Stępień, which gives the required Campanato-to-Hölder embedding for every \(\lambda>Q\) under Borel regularity, doubling, and lower \(Q\)-regularity.

## Verification
The proof is symbolic. The critical scale identity is
\[
\sigma^\kappa=1-c,
\]
so the one-step mass loss implies the stated power reverse-doubling estimate. The cutoff estimate was checked separately for small balls meeting its support, large balls, and balls disjoint from its support. The exponent in the small-ball term is \(p+\kappa-\lambda\), which is positive exactly on the new window used in the claim. The final cancellation is
\[
(1-\alpha)-(1-\lambda/p)=Q/p.
\]
No finite experiment, numerical extrapolation, or unproved limiting computation is used.

## Relationship to prior work
Górka--Stępień prove the sufficient embedding for all \(\lambda>Q\), and prove the doubling-only equivalence only for \(Q<\lambda\le p\). Their Question 5 asks whether the equivalence persists throughout \(Q<\lambda<Q+p\). The result above supplies a quantitative positive window past \(p\), controlled by a reverse-doubling exponent forced by uniform perfectness and doubling.

Nakai's 2006 theory gives general equivalences between measure-dependent Campanato gauges and corresponding Hölder gauges on spaces of homogeneous type. It does not identify the lower \(Q\)-regularity of the measure from the specific radius-normalized embedding considered here. The reverse-doubling power law itself is classical in metric-measure analysis; for example, Björn--Björn--Lehrbäck discuss the relevant ball-ratio exponent sets. The new contribution is using that scale decay to obtain the stated necessity window for the explicit open embedding problem.

## Limitations
The exponent \(\kappa\) is a concrete lower bound for an available reverse-doubling exponent and is not claimed optimal. The argument does not settle Question 5 for doubling spaces whose available reverse-doubling exponent is smaller than \(Q\); it only covers \(\lambda<p+\kappa\). No claim is made about the endpoint \(\lambda=Q+p\), about noncompact spaces, or about removing uniform perfectness or doubling.

## References
1. P. Górka and Z. Stępień, *Optimal Embeddings of Campanato and Morrey Spaces*, arXiv:2610.04622v1 (2026), especially Lemma 2.1, Theorems 3.6 and 3.11, and Question 5.
2. E. Nakai, *The Campanato, Morrey and Hölder spaces on spaces of homogeneous type*, Studia Mathematica 176 (2006), 1--19, DOI: 10.4064/sm176-1-1.
3. A. Björn, J. Björn, and J. Lehrbäck, *Sharp capacity estimates for annuli in weighted \(\mathbf{R}^n\) and in metric spaces*, Mathematische Zeitschrift 286 (2017), 1173--1215, DOI: 10.1007/s00209-016-1797-4.
