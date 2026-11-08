# A John-ellipsoid transition and a three-phase local-symmetry plateau for circular frusta

## Finding
For each integer \(d\ge2\) and each \(0\le r\le1\), let the height-one Euclidean circular frustum be
\[
F_{d,r}=\{(u,t)\in\mathbb R^{d-1}\times\mathbb R:0\le t\le1,\ \|u\|_2\le1-(1-r)t\}.
\]
Here \(r=0\) is the cone endpoint and \(r=1\) is the cylinder endpoint. Put \(k=1-r\) and \(r_c=(d-1)/(d+1)\). The **unique John ellipsoid** of \(F_{d,r}\) is
\[
J_{d,r}=\left\{(u,t):\frac{\|u\|_2^2}{a^2}+\frac{(t-b)^2}{b^2}\le1\right\},
\quad
(b,a^2)=\begin{cases}
\big(1/[k(d+1)],\ (d-1)/(d+1)\big),&0\le r\le r_c,\\
\big(1/2,r\big),&r_c\le r\le1.
\end{cases}
\]
The formulas coincide at \(r=r_c\). Its normalized volume is
\[
\frac{\operatorname{vol}_d(J_{d,r})}{\operatorname{vol}_d(B_2^d)}
=\begin{cases}
\dfrac{1}{(d+1)(1-r)}\left(\dfrac{d-1}{d+1}\right)^{(d-1)/2},&0\le r\le r_c,\\
\dfrac12 r^{(d-1)/2},&r_c\le r\le1.
\end{cases}
\]
The ellipsoid always touches the lower cap and the conical side. It also touches the upper cap **if and only if** \(r\ge r_c\). More precisely, all lateral contacts form the orbit
\[
\left\{\left(\frac{a^2}{q}v,\ b+\frac{k b^2}{q}\right):v\in S^{d-2}\right\},
\qquad q=1-kb=\sqrt{a^2+k^2b^2}.
\]
The other contacts are \((0,0)\) and, exactly when \(r\ge r_c\), \((0,1)\).

Define the *reflection coefficient* at a point \(c\in F_{d,r}\) by
\[
\sigma(c;F_{d,r})=\sup\{\alpha\ge0:(1+\alpha)c-\alpha F_{d,r}\subseteq F_{d,r}\},
\]
and the *Minkowski reflection coefficient* by \(\sigma(F_{d,r})=\max_c\sigma(c;F_{d,r})\). These are the reciprocal convention to the usual Minkowski asymmetry \(s=1/\sigma\). The maximizer is unique and is located at
\[
\sigma(F_{d,r})=\frac{1}{2-r},\qquad c_M=\left(0,\frac{1}{3-r}\right).
\]
At the John center \(c_J=(0,b)\), the exact local coefficient has **three regimes** (the first degenerates to the single endpoint when \(d=2\)):
\[
\boxed{\ \sigma(c_J;F_{d,r})=\begin{cases}
\dfrac{1}{(1-r)(d+1)-1},&0\le r\le(d-2)/d,\\[2mm]
\dfrac{d}{d+2},&(d-2)/d\le r\le(d-1)/(d+1),\\[2mm]
\dfrac{1+r}{3-r},&(d-1)/(d+1)\le r\le1.
\end{cases}\ }
\]
The middle phase is a genuine constant plateau for every \(d\ge2\). The John and Minkowski centers coincide precisely at \(r=(d-2)/d\) and at \(r=1\).

## Assumptions and scope
The ambient norm is Euclidean; the horizontal base and top are concentric \((d-1)\)-dimensional balls, and their radii are normalized to \(1\) and \(r\). The frustum is full dimensional even at \(r=0\). The stated radii and center heights are relative to vertical height \(1\); axial and transverse rescaling gives the corresponding formula for any right circular frustum of positive height and positive base radius. The assertion does not concern arbitrary oblique or asymmetric frusta, nor the smallest possible rounding factor among arbitrary ellipsoids.

## Proof
**1. Exact reduction of all inscribed ellipsoids.** Every full-dimensional convex body has a unique maximum-volume inscribed ellipsoid. The group of orthogonal transformations of the transverse \(u\)-coordinates preserves \(F_{d,r}\), hence also its John ellipsoid. Thus that ellipsoid has a center on the axis, a common transverse semiaxis \(a>0\), and an axial semiaxis \(b>0\); write its center height as \(s\). It is fully described by
\[
E(a,b,s)=\{(a v,s+b z):\|v\|_2^2+z^2\le1\}.
\]
The two cap constraints are precisely \(s\ge b\) and \(s+b\le1\). For every transverse unit vector \(w\), the lateral halfspace inequality is \(\langle w,u\rangle+k t\le1\). The exact ellipsoidal support function gives
\[
E(a,b,s)\subseteq F_{d,r}\quad\Longleftrightarrow\quad
s\ge b,\ s+b\le1,\ k s+\sqrt{a^2+k^2b^2}\le1.
\tag{1}
\]
When \(k>0\), for fixed \(a,b\) decreasing \(s\) to \(b\) preserves the cap constraints and weakens the last one. At an optimum the lateral inequality must be tight (otherwise \(a\) could increase), and therefore \(s=b\). For \(k=0\) the body is a product cylinder, whose unique John ellipsoid has \(s=b=1/2\) and \(a=1\). Hence it suffices for \(k>0\) to set \(s=b\), \(0<b\le1/2\), and
\[
a^2=(1-kb)^2-k^2b^2=1-2kb.
\tag{2}
\]
Maximizing the ellipsoid volume is equivalent to maximizing \(f(b)=b(1-2kb)^{(d-1)/2}\). The logarithmic derivative is
\[
\frac{f'(b)}{f(b)}=\frac1b-\frac{(d-1)k}{1-2kb}
=\frac{1-(d+1)kb}{b(1-2kb)}.
\]
Thus \(f\) increases until \(b_*=1/[k(d+1)]\), then decreases. If \(b_*\le1/2\), equivalently \(r\le(d-1)/(d+1)\), the optimizer is \(b_*\); otherwise it is the cap endpoint \(b=1/2\). Inserting these into (2) gives the claimed John semiaxes and volume for every \(d\) and \(r\). Strict unimodality and uniqueness of the John ellipsoid exclude all alternative ellipsoids, whether symmetric or not.

**2. Exact contact locus.** The lower cap is tangent at \((0,0)\) because \(s=b\). The upper cap is tangent exactly when \(s+b=2b=1\). For each transverse unit \(v\), the unique support point of \(E(a,b,b)\) with normal \((v,k)\) is \((a^2v/q,b+kb^2/q)\), where \(q=\sqrt{a^2+k^2b^2}\). Since (2) makes \(q=1-kb\), that point lies on the side of the frustum. Conversely, the intersection of two smooth strictly convex ellipsoidal boundary points with any supporting lateral halfspace has that support point. These and the cap contacts exhaust the contacts for all \(r\), including \(k=0\).

**3. Exact reflection constraints.** Let \(c=(v,s)\) be an interior point of the frustum and \(\alpha\ge0\). The inclusion \((1+\alpha)c-\alpha F_{d,r}\subseteq F_{d,r}\) can be tested on the same defining halfspaces. The bottom and top constraints yield
\[
\alpha\le\frac{s}{1-s},\qquad\alpha\le\frac{1-s}{s}.
\tag{3}
\]
For any \(w\in S^{d-2}\), the maximum of \(-\langle w,u\rangle-kt\) over the frustum is exactly \(1\): the maximal value at height \(t\) equals \(1-2kt\), attained at \(t=0\). Therefore the lateral constraints for the reflected copy reduce exactly to
\[
(1+\alpha)(\|v\|_2+ks)+\alpha\le1.
\tag{4}
\]
Combining (3)-(4) gives, in particular, for axial \(c=(0,s)\) with \(0<s\le1/2\),
\[
\sigma((0,s);F_{d,r})
=\min\left\{\frac{s}{1-s},\frac{1-ks}{1+ks}\right\}.
\tag{5}
\]
For arbitrary centers, (3) gives \(s\ge\alpha/(1+\alpha)\) and (4) gives \(ks\le(1-\alpha)/(1+\alpha)\). Hence \((1+k)\alpha\le1\), or \(\alpha\le1/(2-r)\). Taking \(\alpha=1/(1+k)\), \(s=1/(2+k)\), \(v=0\) attains equality in all constraints. Furthermore, equality in the bound forces \(s=1/(2+k)\) and \(\|v\|_2=0\), proving uniqueness of the Minkowski center.

**4. Local-symmetry plateau and center coincidence.** The John-center height satisfies \(b\le1/2\), so (5) applies. If \(r\le r_c\), then \(kb=1/(d+1)\), and the second entry of (5) equals \(d/(d+2)\) independent of \(r\), while the first equals \(1/[k(d+1)-1]\). They cross at \(k=2/d\), i.e. \(r=(d-2)/d\). If \(r\ge r_c\), then \(b=1/2\), and the first entry is \(1\), while the second is \((1+r)/(3-r)\). This gives all three regimes, with matching endpoints. Finally, \(b=1/(3-r)\) in the first phase precisely when \(k=2/d\); in the second phase \(b=1/2\) equals \(1/(3-r)\) only at \(r=1\). This proves the center coincidence statement.

## Verification
The companion `verify.py` uses exact fractions to check parameter identities, phase inequalities, boundary coincidences, and the reflection formula for dimensions \(2\) through \(50\), including all transition ratios. It also compares the claimed John volume to a dense independent one-dimensional sampling of every admissible axial radius and checks points on the ellipsoidal boundary against all frustum constraints. Running `python verify.py` prints `VERIFY_OK checks 971598`. These are finite regression tests only: the theorem for arbitrary integer dimension and every real \(r\) follows from the exact support-function argument and scalar optimization above.

## Relationship to prior work
Xiong and Freund (arXiv:2608.30876v1, submitted 31 August 2026) establish the general symmetry-dependent ellipsoidal-rounding theorem and discuss the gap between local and globally optimized Minkowski symmetry. Their Section 5 explicitly studies a reflected-simplex hull rather than circular frusta; it does not provide the sharp frustum John-center phase diagram.

Güler and Gürtuna (arXiv:0709.0707v1, Section 8 and the introduction) study the covering ellipsoid of a truncated second-order cone. They explicitly leave its **inscribed-ellipsoid** problem untreated; their cone class is affinely equivalent to the frusta studied here. In the publicly available result *Exact John ellipsoid of the Khachiyan half-cone* (2026), the John ellipsoid is evaluated for the single high-phase parameter \(r=d/(d+1)\). The present formulas agree at that parameter, but give all radii, both contact regimes, and the local-Minkowski-symmetry plateau. The related publicly available result *Universal Santaló and volume-product laws for homothetic frusta* studies polar volume rather than John ellipsoids or center reflection coefficients.

Brandenberg and Grundbacher's paper on volume-extremal ellipsoids and asymmetry measures analyzes general differences between John and Minkowski asymmetry, including a separate Example A.1. Its studied body does not give the stated frustum identity or parameter plateau. This comparison establishes a specific difference in implications, not universal historical novelty.

## Limitations
The result does not determine the best possible concentric ellipsoidal rounding factor, nor does it treat cones with non-Euclidean or noncentrally symmetric bases. The relationship to older optimization and geometric-tomography literature might contain previously unrecognized equivalent formulas; literature searches cannot certify absolute historical priority. Independent checking beyond the present analytic derivation and finite regression tests is not claimed.

## References
1. Z. Xiong and R. M. Freund, *Symmetry-dependence in Rounding of a Convex Body*, arXiv:2608.30876v1 (31 August 2026), especially Sections 1 and 5; https://arxiv.org/abs/2608.30876.
2. O. Güler and F. Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, arXiv:0709.0707v1 (5 September 2007), Sections 1 and 8; https://arxiv.org/abs/0709.0707.
3. R. Brandenberg and F. Grundbacher, *Tightening inequalities on volume-extremal k-ellipsoids using asymmetry measures*, arXiv:2501.00653v1 (31 December 2024), Appendix A; https://arxiv.org/abs/2501.00653.
4. *Exact John ellipsoid of the Khachiyan half-cone*, publicly available mathematical note, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-john-ellipsoid-of-the-khachiyan-half-cone--12746f7a27eb.
5. *Universal Santaló and volume-product laws for homothetic frusta*, publicly available mathematical note, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-universal-santal-and-volume-product-laws-for-homothetic-frusta--3dbfdaf0b359.
