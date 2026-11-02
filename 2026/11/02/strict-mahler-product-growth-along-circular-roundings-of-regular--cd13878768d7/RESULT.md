# Strict Mahler-product growth along circular roundings of regular polygons

## Finding
Fix an integer \(n\ge3\). Let \(P_n\subset\mathbb R^2\) be a regular polygon centered at the origin, with Euclidean inradius \(1\), and let \(B\) be the closed unit disk. Set \(K_{n,t}=P_n+tB\) for every real \(t\ge0\), and let \(K_{n,t}^{\circ}\) be the polar about the origin. Write
\[
\alpha=\frac{\pi}{n},\quad R=\sec\alpha,\quad \mu=\frac{\tan\alpha}{\alpha},\quad U\sim\operatorname{Unif}[0,\alpha],\quad Z=R\cos U.
\]
Then the origin is the unique Santaló point of \(K_{n,t}\), and its Mahler product is exactly
\[
\mathcal M_n(t)=\operatorname{area}(K_{n,t})\operatorname{area}(K_{n,t}^{\circ})
=\pi^2(t^2+2\mu t+\mu)\,\mathbb E\big[(t+Z)^{-2}\big]. \tag{1}
\]
For **every** \(n\ge3\) this function is strictly increasing on \([0,\infty)\). Consequently,
\[
\mathcal M_n(0)=n^2\sin^2\!\left(\frac\pi n\right),\quad
n^2\sin^2\!\left(\frac\pi n\right)<\mathcal M_n(t)<\pi^2\quad(t>0),\quad
\lim_{t\to\infty}\mathcal M_n(t)=\pi^2. \tag{2}
\]
The approach to the disk value is sharp: if
\[
\sigma^2=\operatorname{Var}(Z)=\frac{R^2+\mu}{2}-\mu^2,
\qquad C_n=\pi^2\big(\mu(\mu-1)-3\sigma^2\big)>0,
\]
then
\[
\pi^2-\mathcal M_n(t)=C_n t^{-2}+O_n(t^{-3})\qquad(t\to\infty). \tag{3}
\]
For each fixed \(t\ge0\) there is also a polygon-to-disk expansion
\[
\pi^2-\mathcal M_n(t)=\frac{\pi^4}{3n^2(1+t)^2}+O_t(n^{-4})\qquad(n\to\infty). \tag{4}
\]
Here the notation \(O_n\) or \(O_t\) permits a constant depending on the indicated fixed parameter; neither statement asserts uniformity as both parameters diverge.

## Assumptions and scope
All polygons are nondegenerate regular Euclidean \(n\)-gons with an inradius of one, and all roundings use the **Euclidean** disk centered at the origin. The real offset \(t\) is nonnegative; no smoothness assumption is imposed on the polygon. The polarity convention is \(K^{\circ}=\{y:\langle x,y\rangle\le1\text{ for all }x\in K\}\). The volume product is affine invariant, but rounding by a Euclidean disk is not affine equivariant: the theorem does not cover arbitrary affine images of these rounded polygons. The displayed expectation is an ordinary one-dimensional uniform average and is well-defined for every \(t\ge0\), because \(1\le Z\le R\).

## Proof
**1. Exact area and polar area.** The inradius-one regular polygon has area \(n\tan\alpha\) and perimeter \(2n\tan\alpha\). The planar outer-parallel-body (Steiner) formula therefore gives
\[
A_n(t)=\operatorname{area}(K_{n,t})=n\tan\alpha(1+2t)+\pi t^2
=\pi(t^2+2\mu t+\mu). \tag{5}
\]
For a direction making signed angle \(\theta\in[-\alpha,\alpha]\) with a polygon-vertex ray, the support function of \(P_n\) is \(R\cos\theta\). Support functions add under Minkowski sums, hence \(h_{K_{n,t}}(\theta)=t+R\cos\theta\) on each vertex sector. The radial function of the polar is its reciprocal. Using \(\operatorname{area}(K^{\circ})=\tfrac12\int_0^{2\pi}h_K(\theta)^{-2}\,d\theta\),
\[
\operatorname{area}(K_{n,t}^{\circ})
=n\int_0^\alpha\frac{d\theta}{(t+R\cos\theta)^2}
=\pi\mathbb E[(t+Z)^{-2}]. \tag{6}
\]
There are \(n\) equal vertex sectors, and \(n\alpha=\pi\). Equations (5)–(6) give (1). The unique Santaló point must be fixed by the nontrivial \(n\)-fold rotation of \(K_{n,t}\), and hence is the origin (the usual uniqueness of the Santaló point applies also when \(n\) is odd).

**2. Strict derivative sign.** Direct differentiation of (1), justified on each compact interval of \(t\ge0\) by the bound \(Z\ge1\), yields
\[
\frac{\mathcal M_n'(t)}{2\pi^2}
=\mathbb E\left[\frac{t(Z-\mu)+\mu(Z-1)}{(t+Z)^3}\right]. \tag{7}
\]
The mean of \(Z\) is \(\mu\), and \(1\le Z\le R\le2\). For \(w_t(z)=(t+z)^{-3}\), the mean-zero identity
\(\mathbb E[(Z-\mu)w_t(Z)]=\mathbb E[(Z-\mu)(w_t(Z)-w_t(\mu))]\)
and \(\lvert w_t'(z)\rvert\le3/(t+1)^4\) give
\[
\mathbb E[(Z-\mu)w_t(Z)]\ge-\frac{3\sigma^2}{(t+1)^4}.
\]
Likewise, since \(Z-1\ge0\),
\(\mathbb E[(Z-1)w_t(Z)]\ge(\mu-1)/(t+R)^3\). Inserting both estimates in (7) gives
\[
\frac{\mathcal M_n'(t)}{2\pi^2}
\ge\frac{\mu(\mu-1)}{(t+R)^3}
-\frac{3t\sigma^2}{(t+1)^4}. \tag{8}
\]
For \(1\le R\le2\), elementary differentiation of \(g(t)=t(t+2)^3/(t+1)^4\) (maximum at \(t=1\)) implies
\[
0\le\frac{t(t+R)^3}{(t+1)^4}\le\frac{27}{16}\qquad(t\ge0). \tag{9}
\]
We now prove, without numerical estimates, the stronger variance inequality
\[
\frac{\mu(\mu-1)}{\sigma^2}>\frac{81}{16}. \tag{10}
\]
Let \(V=U^2\), so \(Z=R\cos\sqrt V\). The map \(v\mapsto R\cos\sqrt v\) is \(R/2\)-Lipschitz on \([0,\alpha^2]\): its derivative has magnitude \(R\sin\sqrt v/(2\sqrt v)\le R/2\), including its continuous value at zero. By the independent-copy variance identity,
\[
\sigma^2\le\frac{R^2}{4}\operatorname{Var}(U^2)
=\frac{R^2\alpha^4}{45}. \tag{11}
\]
For \(0<x<\pi/2\), \(\tan x\ge x+x^3/3+2x^5/15\). One elementary verification first notes \(\tan x\ge x\), then differentiates \(\tan x-x-x^3/3\) to establish its nonnegativity, and finally differentiates the difference from the stated fifth-degree polynomial. Indeed the last derivative is \(\tan^2x-x^2-2x^4/3\ge x^6/9>0\). Thus
\[
\mu-1\ge\frac{\alpha^2}{3}+\frac{2\alpha^4}{15},\qquad
\mu(\mu-1)\ge\frac{\alpha^2}{3}+\frac{11\alpha^4}{45}. \tag{12}
\]
Using \(\alpha\le\pi/3\), \(R\le2\), and the elementary \(\pi^2<10\), (11)–(12) give
\[
\frac{\mu(\mu-1)}{\sigma^2}
\ge\frac{15/\alpha^2+11}{R^2}
\ge\frac{135/\pi^2+11}{4}
>\frac{49}{8}>\frac{81}{16}, \tag{13}
\]
which proves (10). In (8), comparison with (9) now gives \(\mathcal M_n'(t)>0\) for every \(t\ge0\), as required.

**3. Endpoints and rates.** At \(t=0\), integration of \(R^{-2}\sec^2\theta\) in (6) gives \(\operatorname{area}(K_{n,0}^{\circ})=n\sin\alpha\cos\alpha\), hence \(\mathcal M_n(0)=n^2\sin^2\alpha\). Since \(Z\) is bounded and the leading area term is \(\pi t^2\), (1) gives the limit \(\pi^2\). Strict monotonicity yields both sharp bounds in (2). Moreover
\[
\mathbb E Z=\mu,\qquad \mathbb E Z^2=\frac{R^2+\mu}{2}=\mu^2+\sigma^2.
\]
Expanding \((t+Z)^{-2}\) in powers of \(1/t\), uniformly for bounded \(Z\), proves (3) with the coefficient stated there; its positivity follows already from (10). Finally, for \(\alpha=\pi/n\to0\), uniformly in \(U\in[0,\alpha]\), one has \(Z=1+O(\alpha^2)\), \(\mu=1+\alpha^2/3+O(\alpha^4)\), and \(\operatorname{Var}(Z)=O(\alpha^4)\). Taylor expansion of (1) at each fixed \(t\ge0\) gives \(\mathcal M_n(t)=\pi^2[1-\alpha^2/(3(1+t)^2)+O_t(\alpha^4)]\), yielding (4).

## Verification
A standalone Python 3 checker, `checker.py`, independently integrates the polar radial area in two ways: by vertexwise support maxima over the full angular circle, and by a single support-function sector. It tests the derivative identity with exact rational arithmetic, evaluates the numerical derivative against the differentiated integral, checks strict inequalities at finite parameter grids, and verifies both asymptotic formulas. The test is finite corroboration; the inequalities (8)–(13) supply the proof for all \(n\) and all \(t\). Execute `python3 checker.py` in the directory containing this document. No third-party Python packages are required.

## Relationship to prior work
Meyer and Reisner's *On the volume product of polygons* (2011) treats extremal products within fixed-vertex-count polygon classes; for \(t>0\), the present parallel bodies have circular arcs and are not polygons. Böröczky, Makai, Meyer, and Reisner's *On the volume product of planar polar convex bodies—lower estimates with stability* (2013) establishes the sharp lower bound \(n^2\sin^2(\pi/n)\) among \(n\)-fold symmetric planar convex bodies, but that bound by itself does not order the distinct rounded bodies as \(t\) changes. Richter and Saorín Gómez (2021) prove monotonicity of a different functional, the isoperimetric quotient, along parallel bodies; its monotonicity does not determine the polar-area factor in (1). The 2023 survey *Volume Product* reviews global bounds and related methods; no same-family differential ordering is asserted in the sections consulted. Thus the new assertion is the simultaneous strict \(t\)-ordering for every \(n\ge3\) and its explicit rates, not the known endpoint inequalities. Historical priority is not guaranteed by a finite literature search.

## Limitations
Only regular planar polygons and isotropic Euclidean outer parallel offsets are covered. The theorem does not prove the same monotonicity for arbitrary polygons, arbitrary gauges, higher dimensions, or affine images rounded in a fixed Euclidean metric. The error term in (4) is for fixed \(t\); no uniform two-parameter expansion is asserted. The full literature is not exhaustively indexed, and earlier equivalent formulations may exist.

## References
1. M. Meyer and S. Reisner, *On the volume product of polygons*, Abh. Math. Semin. Univ. Hambg. 81 (2011), 93–100, DOI: 10.1007/s12188-011-0054-3; first online publication 2011-04-05.
2. K. J. Böröczky, E. Makai Jr., M. Meyer and S. Reisner, *On the volume product of planar polar convex bodies—lower estimates with stability*, Stud. Sci. Math. Hungar. 50 (2013), 159–198, DOI: 10.1556/SScMath.50.2013.2.1235; lawful full text arXiv:1507.01481.
3. C. Richter and E. Saorín Gómez, *On the Monotonicity of the Isoperimetric Quotient for Parallel Bodies*, J. Geom. Anal. 32 (2022), article 15; first preprint arXiv:2003.14182 (2020-03-31), DOI: 10.1007/s12220-021-00766-2.
4. M. Fradelizi, M. Meyer and A. Zvavitch, *Volume Product*, survey, arXiv:2301.06131v1 (2023-01-15).
