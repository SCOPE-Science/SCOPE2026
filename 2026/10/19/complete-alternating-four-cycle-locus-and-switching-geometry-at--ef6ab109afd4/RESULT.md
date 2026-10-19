# Complete alternating four-cycle locus and switching geometry at the flip boundary of a planar border-collision map

## Finding
For the entire two-saddle parameter region of the planar border-collision normal form, an alternating primitive four-cycle exists **if and only if** the branch-alternating period-two orbit has a multiplier \(-1\). On that codimension-one locus, **all** points on weakly alternating orbits whose period divides four form two explicitly parameterized closed line segments, with a sharp switch between two distinct border-clipping mechanisms. The segment is normally attracting when \(de<1\), transversely repelling when \(de>1\), and non-semisimple neutral when \(de=1\).

Write
\[
F(x,y)=\begin{cases}(ax+y+1,-dx),&x\leq0,\\(bx+y+1,-ex),&x\geq0,\end{cases}
\quad a>|1+d|,\quad b<-|1+e|.
\]
The two definitions agree on the switching line, so \(F\) is unambiguous there. Put
\[
\alpha=ab+(d-1)(e-1),\qquad \sigma=a+d(1-e).
\]
An *alternating four-cycle* is a primitive four-orbit with cyclic itinerary \(LRLR\): the two left-phase points have \(x\leq0\) and the intervening right-phase points have \(x\geq0\), allowing equality on the switching line. Such a cycle exists precisely when \(\alpha=0\).

At \(\alpha=0\) one necessarily has \(d,e<1\) and \(de>-1\). Define
\[
p=\frac{b+e+1}{2(1+de)}<0,\quad q=\frac{a+d+1}{2(1+de)}>0,\quad
P=(p,-eq),\quad Q=(q,-dp),
\]
\[
v=\left(1,\frac{ea}{1-e}\right),\quad
w=\left(\frac{a}{1-e},-d\right),\quad
r=\min\left\{-p,\frac{q(1-e)}a\right\}>0.
\]
The entire set of points on alternating orbits of period dividing four is
\[
\{P+tv:-r\leq t\leq r\}\ \cup\ \{Q+tw:-r\leq t\leq r\}.
\]
Here \(F(P+tv)=Q+tw\) and \(F(Q+tw)=P-tv\). Exactly the central pair \(P,Q\), corresponding to \(t=0\), has least period two; all noncentral points with \(t\ne0\) have least period four.

The *sharp clipping law* is
\[
r=\begin{cases}-p,&\sigma\geq0,\\ q(1-e)/a,&\sigma\leq0,\end{cases}
\]
with agreement on \(\sigma=0\). For \(\sigma>0\), the endpoints are limited by a visit to the left-half-plane switching boundary; for \(\sigma<0\), by a visit to the right-half-plane boundary; at \(\sigma=0\), both restrictions become sharp simultaneously. This identifies the geometric degeneracy of the period-four set across the full four-parameter family, rather than only in its symmetric Lozi subfamily.

## Assumptions and scope
All four parameters are real. The strict two-saddle inequalities are \(a>|1+d|\) and \(b<-|1+e|\); no sign restriction is imposed on either determinant \(d,e\), so orientation-preserving, orientation-reversing, and noninvertible cases are included. The statements classify cycles with the alternating itinerary only; they do not classify other symbolic words, all recurrent sets, or global basins. Endpoint points on \(x=0\) are counted because the two affine formulas agree there. Stability is asserted for the local four-step dynamics near the interior of the segments.

## Proof
**1. Necessity of the flip condition.** Let
\[
A_L=\begin{pmatrix}a&1\\-d&0\end{pmatrix},\quad
A_R=\begin{pmatrix}b&1\\-e&0\end{pmatrix},\quad
B=A_RA_L=\begin{pmatrix}ab-d&b\\-ea&-e\end{pmatrix}.
\]
For a weakly alternating orbit, \(F^2\) on the even-phase points is the affine map \(z\mapsto Bz+c\), \(c=(b+1,-e)\). If an even-phase point \(z\) has least period four, its distinct partner \(z'=F^2(z)\) satisfies \(B(z'-z)=-(z'-z)\). Hence \(\det(B+I)=0\), equivalent to \(\alpha=0\). No periodicity inference from finite simulation is used.

**2. Parameter geometry on the flip hypersurface.** Write \(A=a>0\) and \(C=-b>0\). On \(\alpha=0\), \(AC=(1-d)(1-e)>0\); thus either both \(d,e<1\) or both \(d,e>1\). The latter would imply \(AC=(d-1)(e-1)<(d+1)(e+1)<AC\), impossible by the two-saddle inequalities. So \(d,e<1\). Furthermore
\[
(1-d)(1-e)=AC>|1+d||1+e|\geq-(1+d)(1+e),
\]
so \(2(1+de)>0\). Thus all denominators above are nonzero, \(p<0\), \(q>0\), and \(r>0\).

**3. The entire four-cycle set.** The unique fixed point of the affine two-step \(LR\) map is \(P=(p,-eq)\), and \(F(P)=Q=(q,-dp)\). Direct substitution in the displayed matrices gives
\[
Bv=-v,\qquad A_Lv=w.
\]
The alternative eigenvalue of \(B\) is \(-de\). Also
\[
\det(B-I)=(1+d)(1+e)-ab>0
\]
under the two-saddle inequalities, so \(B-I\) is invertible. Consequently the complete fixed-point set of the affine fourth iterate (before enforcing branch constraints) is
\[
\ker(B^2-I)+P=P+\ker(B+I)=P+\mathbb Rv.
\]
This remains true at \(de=1\): then \(B+I\) has rank one, since its upper-right entry is \(b\ne0\).

A candidate \(P+tv\) follows the \(LRLR\) itinerary for all four steps exactly when both \(P\pm tv\) lie in \(x\leq0\) and both \(Q\pm tw\) lie in \(x\geq0\). These four conditions are equivalent to
\[
|t|\leq-p,\qquad |t|\leq\frac{q(1-e)}a,
\]
thus to \(|t|\leq r\). On this interval the identities \(F(P+tv)=Q+tw\) and \(F(Q+tw)=P-tv\) follow directly. They prove period four for \(t\ne0\), period two for \(t=0\), and exhaustive classification. No extra points can appear on switching boundaries, because the map is continuous there and the same affine fourth-iterate equations apply.

**4. Competing border mechanisms.** Elementary algebra using \(ab=-(1-d)(1-e)\) gives
\[
\frac{q(1-e)}a+p=\frac{a+d(1-e)}{a(1+de)}=\frac\sigma{a(1+de)}.
\]
The denominator is positive, proving the sharp piecewise formula for \(r\) and the three clipping regimes. Both strict regimes and equality occur for admissible rational parameters (see the accompanying checker).

**5. Local transverse classification.** The two-step matrix \(B\) has eigenvalues \(-1\) and \(-de\). If \(de\ne1\), a second eigenvector is \(w_s=(1,-a/(1-d))\), linearly independent of \(v\). For any interior \(t\), any transverse amplitude \(u\), and every integer \(n\geq0\) for which the first \(4n\) iterates preserve the alternating itinerary, the exact affine recurrence gives
\[
F^{4n}(P+tv+u w_s)=P+tv+u(de)^{2n}w_s.
\]
When \(de<1\), a sufficiently small neighborhood of each interior segment point preserves the itinerary for all future steps and, because \(de>-1\), the segments are locally normally attracting, and transversely repelling when \(de>1\). If \(de=1\), \(B\) has a repeated eigenvalue \(-1\) and is not \(-I\) (because \(b\ne0\)); hence \(B^2\) is a nontrivial unipotent shear. This is a non-semisimple neutral boundary, not an attracting case.

## Verification
The standalone Python 3 program `check.py` uses exact rational arithmetic, without external packages. It verifies the parameter restrictions, matrix/eigenvector identities, both clipping formulas, all five representative values of the period-four coordinate, and local fourth-iterate transverse identities for **156** admissible rational parameter triples chosen from a fixed grid. Its output is `PASS` with that count. This is a reproducibility check, not the proof for arbitrary real parameters, which is given above.

## Relationship to prior work
Ghosh, McLachlan and Simpson (2024), §4, identify the multiplier \(-1\) boundary \(\alpha=0\) and its role in the stability of the \(LR\) two-cycle. Their paper's treatment of that boundary does not state the complete \(LRLR\) continuum, its two clipping mechanisms, or its three transverse types. The symmetric Lozi restriction has a **previously known** attracting period-four continuum: Botella-Soler et al. (2011), §3.2, give a parametrization when the Lozi parameters satisfy \(a=1+b_{\mathrm{Lozi}}\), \(0<b_{\mathrm{Lozi}}<1\). The present claim is **not** that the symmetric Lozi continuum is newly discovered. It is the classification across the four-parameter two-saddle border-collision family, including mixed-determinant and non-invertible cases, the exact parameter-dependent clipping switch, and the nonattracting Jordan/expanding transverse regimes. General affine-matrix arguments underlie the proof.

## Limitations
The classification does not address nonalternating period-four orbits or global attractor uniqueness. The result is derived in the exact piecewise-affine normal form; persistence of the continuum under nonlinear perturbations is not established. The Lozi special case was known. A thematically relevant 2023 paper of Sushko, Avrutin and Gardini on embedding the Lozi map in the full normal form was located, but its full text was inaccessible; its abstract concerns boundaries of period-\(n\) regions with rotation number \(1/n\), \(n\ge3\). This leaves a residual priority risk for equivalent formulations, though it does not directly establish the claimed alternating-four-cycle classification. No independent scientific audit has been performed.

## References
1. I. Ghosh, R. I. McLachlan, D. J. W. Simpson, *The bifurcation structure within robust chaos for two-dimensional piecewise-linear maps*, arXiv:2402.05393v1 (first public 2024-02-08), especially §§3–4, 7–10; https://arxiv.org/html/2402.05393v1.
2. V. Botella-Soler, J. M. Castelo, J. A. Oteo, J. Ros, *Bifurcations in the Lozi map*, arXiv:1102.0034v2 (2011), especially §3.2; https://arxiv.org/html/1102.0034v2.
3. I. Sushko, V. Avrutin, L. Gardini, *Lozi map embedded into the 2D border collision normal form*, J. Difference Equations Appl. 29 (2023), 965–981, DOI:10.1080/10236198.2023.2205960 (abstract examined; full text unavailable).
