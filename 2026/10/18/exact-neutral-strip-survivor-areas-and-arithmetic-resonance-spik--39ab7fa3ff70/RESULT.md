# Exact neutral-strip survivor areas and arithmetic resonance spikes in a planar market map

## Finding
At the center bifurcation of the three-partition planar stock-market map studied by Gardini, Radi, Schmitt, Sushko, and Westerhoff [1], the area of all initial states that avoid switching for a prescribed number of visits has an exact closed formula. In the infinite-horizon limit, this area is discontinuous exactly at rational rotation angles, with an explicit positive resonance spike at each such angle. For bounded-type irrational rotation angles, the finite-horizon excess area decays at the sharp order \(m^{-2}\), producing a sharp quadratic tail and an infinite second moment for the first switching time conditional on eventual switching.

For \(0<c<4\), \(h>0\), put
\[
J_c=\begin{pmatrix}2-c&-1\\1&0\end{pmatrix},\qquad
\theta=\arccos(1-c/2)\in(0,\pi),\qquad
\ell(x,y)=x-y.
\]
For every integer \(m\ge2\), define the (strict) neutral-survivor region
\[
K_m(c,h)=\{z\in\mathbb R^2:|\ell(J_c^jz)|<h\text{ for }0\le j<m\},\qquad
K_\infty(c,h)=\bigcap_{m\ge2}K_m(c,h).
\]
Let \(\beta_1<\cdots<\beta_k\) list the distinct residues of \(0,\theta,\ldots,(m-1)\theta\) modulo \(\pi\), all taken in \([0,\pi)\), and set
\[
\delta_i=\beta_{i+1}-\beta_i\ (i<k),\qquad
\delta_k=\pi+\beta_1-\beta_k.
\]
Then the **exact finite-horizon identity** is
\[
\boxed{\operatorname{area}(K_m(c,h))=
 h^2\cot(\theta/2)\sum_{i=1}^{k}\tan(\delta_i/2).} \tag{1}
\]
In particular \(\operatorname{area}(K_2(c,h))=4h^2/c\), so dividing (1) by this quantity gives the exact conditional survival probability for a point sampled uniformly from \(K_2(c,h)\).

If \(\theta/\pi\) is irrational,
\[
\boxed{\operatorname{area}(K_\infty(c,h))=
\frac{\pi h^2}{2}\cot(\theta/2).} \tag{2}
\]
If \(\theta/\pi=p/v\) in lowest terms, where \(1\le p<v\) and \(v\ge2\),
\[
\boxed{\operatorname{area}(K_\infty(c,h))=
 h^2\cot(\theta/2)\,v\tan\!\bigl(\pi/(2v)\bigr).} \tag{3}
\]
Thus the infinite-horizon area, as a function of \(c\in(0,4)\), is continuous at every parameter having irrational \(\theta/\pi\) and discontinuous at every parameter having rational \(\theta/\pi=p/v\). Its positive rational-point spike over the continuous irrational envelope is exactly
\[
\boxed{h^2\cot(\theta/2)\left[v\tan\!\bigl(\pi/(2v)\bigr)-\frac\pi2\right]}
 =h^2\cot(\theta/2)\left[\frac{\pi^3}{24v^2}+O(v^{-4})\right]. \tag{4}
\]
For an irrational \(\theta/\pi\) with bounded continued-fraction coefficients there exist constants \(C_1,C_2>0\), depending on \(c,h\), such that for all sufficiently large \(m\),
\[
\boxed{\frac{C_1}{m^2}\le \operatorname{area}(K_m(c,h))-
\operatorname{area}(K_\infty(c,h))\le\frac{C_2}{m^2}.} \tag{5}
\]

If initial conditions are uniform on \(K_2(c,h)\), define \(\tau=\inf\{j\ge2:|\ell(J_c^jz)|\ge h\}\), with \(\tau=\infty\) when no such time exists. This is the first actual branch-switching time of the full three-zone map from such an initial condition. For every \(m\ge2\),
\[
\boxed{\mathbb P(\tau\ge m\mid\tau<\infty)=
\frac{\operatorname{area}(K_m(c,h))-\operatorname{area}(K_\infty(c,h))}
{\operatorname{area}(K_2(c,h))-\operatorname{area}(K_\infty(c,h))},} \tag{6}
\]
provided the denominator is positive. For **every bounded-type irrational** \(\theta/\pi\), it is positive, and the conditional switching-time tail has order \(m^{-2}\). In particular,
\[
\boxed{\mathbb E[\tau\mid\tau<\infty]<\infty,
\qquad \mathbb E[\tau^2\mid\tau<\infty]=\infty.} \tag{7}
\]
The finite mean and infinite second moment are genuine infinite-horizon conclusions, not finite numerical extrapolations.

## Assumptions and scope
The original three-partition model has a neutral middle branch \(z\mapsto J_cz\) when \(|x-y|\le h\) and nonneutral branches \(z\mapsto J_cz\pm(d,0)\) beyond the switching lines, with \(d>h>0\). We restrict to the center-bifurcation slice where the original memory parameter equals \(1\), and to \(0<c<4\). The precise positive value of \(d>h\) does not affect neutral-survivor sets, since no orbit counted here ever uses a nonneutral branch. We use strict inequalities to avoid ambiguous switching-line assignments; changing finitely or countably many boundary lines does not change planar area. All areas are ordinary Euclidean Lebesgue area in the original \((x,y)\)-plane. These are initial states remaining in the *neutral branch*, not the full bounded basin or a complete characterization of the dynamics after the first switch.

## Proof
**1. Elliptic conjugacy and strip normalization.** Write \(q=\cos\theta=1-c/2\) and
\[
G=\begin{pmatrix}1&-q\\-q&1\end{pmatrix}.
\]
Because \(|q|<1\), the matrix \(G\) is positive definite, \(\det G=1-q^2=\sin^2\theta\), and direct multiplication gives \(J_c^{\mathsf T}GJ_c=G\). The change of variables \(u=G^{1/2}z\) therefore conjugates \(J_c\) to a Euclidean rotation through angle \(\theta\) or \(-\theta\), a sign immaterial for unoriented strip normals. The transformed linear functional \(\ell(z)=(1,-1)z\) has squared dual norm
\[
(1,-1)G^{-1}(1,-1)^{\mathsf T}=\frac{2}{1+q}=\sec^2(\theta/2).
\]
Consequently \(|\ell(J_c^jz)|<h\) becomes a Euclidean strip of inradius \(r=h\cos(\theta/2)\), whose unoriented unit normal makes angle \(j\theta\) modulo \(\pi\) with the first normal. The area change from the \(u\)-plane back to the \(z\)-plane is \(1/\sin\theta\).

**2. Exact finite polygon area.** For \(m\ge2\), the first two normals are nonparallel, so the intersection of all \(m\) centered strips is a bounded convex polygon. It is circumscribed about the radius-\(r\) disk, and each distinct unoriented normal contributes a pair of opposite tangent sides. Given consecutive directed outward normals at angular gap \(\delta\in(0,\pi)\), the two tangent half-segments ending at their intersection have length \(r\tan(\delta/2)\). Thus the entire polygon has area
\[
\frac12\sum_{\text{sides}}r\cdot\text{side length}
 =2r^2\sum_{i=1}^{k}\tan(\delta_i/2).
\]
Multiplication by \(1/\sin\theta\), using \(2r^2/\sin\theta=h^2\cot(\theta/2)\), proves (1). Independently, the determinant of the two row functionals \(\ell\) and \(\ell J_c\) has absolute value \(c\), so the inverse image of the square \((-h,h)^2\) under this two-row map has area \(4h^2/c\), proving the two-visit identity.

**3. Infinite horizon.** For rational \(\theta/\pi=p/v\) in lowest terms, the residues of \(j\theta\) modulo \(\pi\) attain exactly \(v\) equally spaced angles (permutation of \(j\pi/v\)), and no new strip occurs after \(m=v\). Equation (3) follows from (1) with \(\delta_i=\pi/v\). For irrational \(\theta/\pi\), those residues are dense modulo \(\pi\); the full intersection in \(u\)-coordinates is exactly the disk of radius \(r\): a point outside this disk violates a tangent strip with normal sufficiently near its radial direction. The disk area \(\pi r^2\), divided by \(\sin\theta\), gives (2). This also identifies the limiting area of the decreasing bounded measurable sets \(K_m\).

**4. Arithmetic discontinuities and spike size.** Let \(H(v)=v\tan(\pi/(2v))\) for integers \(v\ge2\). The strict inequality \(\tan x>x\) on \((0,\pi/2)\) gives \(H(v)>\pi/2\), and Taylor expansion gives \(H(v)=\pi/2+\pi^3/(24v^2)+O(v^{-4})\). Any sequence of *distinct* rationals tending to an irrational has reduced denominators tending to infinity, and the same holds for a sequence of distinct rational values approaching a fixed rational. Since \(c\mapsto\theta\) is continuous and strictly increasing on \((0,4)\), (2)–(3) show continuity exactly at irrational angles and the upward discontinuity (4) at each rational angle.

**5. Sharp finite-horizon order at bounded-type angles.** Suppose \(\alpha=\theta/\pi\) is irrational. Then the first \(m\) normals are distinct. Strict convexity of \(\tan t\) for positive \(t<\pi/2\) and \(\sum_i\delta_i=\pi\) give
\[
\sum_{i=1}^m\tan(\delta_i/2)\ge
m\tan(\pi/(2m))=\frac\pi2+\frac{\pi^3}{24m^2}+O(m^{-4}).
\]
This yields the lower bound in (5). For the upper bound, suppose the continued-fraction partial quotients of \(\alpha\) are at most \(B\). If \(q_k\le m<q_{k+1}\) are consecutive convergent denominators, the \(q_k\) orbit points \(j\alpha\pmod1\), for \(0\le j<q_k\), are within circular distance \(1/q_{k+1}\) of the uniform \(q_k\)-grid in some permutation, because \(|\alpha-p_k/q_k|<1/(q_kq_{k+1})\). Therefore the largest cyclic gap among the first \(m\) angles is at most
\[
\Delta_m\le\pi\left(\frac1{q_k}+\frac2{q_{k+1}}\right)
\le\frac{3\pi(B+1)}m.
\]
For large \(m\), Taylor's inequality \(\tan t-t\le C t^3\) applies uniformly to all \(\delta_i/2\). Hence
\[
0\le\sum_i\tan(\delta_i/2)-\frac\pi2
\le C'\sum_i\delta_i^3
\le C'\pi\Delta_m^2=O(m^{-2}).
\]
Multiplying by the positive fixed factor \(h^2\cot(\theta/2)\) gives (5).

**6. First-switching-time distribution and moment threshold.** Under uniform area measure on \(K_2\), the event \(\{\tau\ge m\}\) coincides with \(K_m\) up to a null boundary set; \(\{\tau=\infty\}\) coincides with \(K_\infty\). Subtracting their probabilities and conditioning on \(\tau<\infty\) gives (6). For irrational \(\theta/\pi\), the limiting neutral area occupies a strict fraction of \(K_2\): equations (2) and the two-visit identity yield \(\operatorname{area}(K_\infty)/\operatorname{area}(K_2)=(\pi/4)\sin\theta<1\). Equation (5) makes the conditional survival tail bounded above and below by positive constants times \(m^{-2}\). The discrete tail-sum formula for positive moments then shows that \(\mathbb E[\tau^s\mid\tau<\infty]\) is finite for \(0<s<2\) and infinite for \(s\ge2\). In particular (7) holds.

## Verification
The standalone pure-Python script `verification/neutral_strip_check.py` clips planar polygons directly by the inequalities \(\pm\ell J_c^jz\le h\), computes areas with the shoelace formula, and compares those *independent* areas with (1). With rational arithmetic it verifies the exact saturated areas \(3\), \(2\), and \(1\) for \(h=1\) and \(c=1,2,3\) respectively, including further periods, as well as the exact two-visit values \(4\) and \(4/3\) for \(c=1,3\). Floating-point clipping checks multiple finite horizons for an irrational rotation and a rational rotation of denominator \(11\). The executable prints `NEUTRAL_STRIP_POLYGON_AREA_CHECKS_OK` when all assertions pass. These finite checks validate normalizations and representative cases; the proof above establishes all parameters and all horizons, not an exhaustive numerical experiment.

## Relationship to prior work
Gardini, Radi, Schmitt, Sushko, and Westerhoff [1, §4.7] already establish the central qualitative dichotomy: a tangent invariant ellipse for irrational angles and a larger invariant polygon for rational angles. Equations (1)–(5) quantify this *known* geometry through an exact area at every finite horizon, an explicit complete infinite-horizon area function, its dense arithmetic spikes, and sharp convergence order at bounded-type angles, and the finite-mean/infinite-second-moment switching-time law. Sushko and Gardini [2,3] establish related earlier center-bifurcation polygon/ellipse mechanisms for different one-switch maps; none of their inspected center-bifurcation statements supplies these quantitative neutral-strip survivor areas for the present three-zone map. Gardini et al. [4] analyze homogeneous piecewise-linear maps sharing a fixed point across branches; this does not cover the nonhomogeneous three-partition neutral-strip calculation here.

## Limitations
The result is a center-slice statement (memory parameter equal to \(1\)), not a theorem for contraction or expansion away from that slice. The area counts trajectories that remain in the neutral strip, not all bounded trajectories or all points attracted to any cycle. The irrational-rate estimate assumes bounded continued-fraction coefficients and does not supply a uniform rate for arbitrary irrational angles. The arithmetic spike reflects exact rational resonance and may be fragile under parameter uncertainty or perturbations away from the piecewise-affine center slice. Bibliographic searches cannot establish absolute priority, and the elementary underlying tangent-polygon formula may occur in broader convex-geometric literature.

## References
[1] L. Gardini, D. Radi, N. Schmitt, I. Sushko, F. Westerhoff, “A 2D piecewise-linear discontinuous map arising in stock market modeling: Two overlapping period-adding bifurcation structures,” *Chaos, Solitons & Fractals* 176 (2023), 114143. DOI: 10.1016/j.chaos.2023.114143. Public publisher version available October 12, 2023. Author-institution OA PDF: https://fis.uni-bamberg.de/bitstreams/f7cf86a1-3705-49f7-aba3-a1829808b077/download.

[2] I. Sushko and L. Gardini, “Center Bifurcation for a Two-Dimensional Piecewise Linear Map,” 2006, chapter 2, especially §2.3.2. Author-posted chapter: https://www.mdef.it/public/fileadmin/whoiswho/gardini/Publications/Contributions_in_Multiauthor_Books_and_Proceedings/Ch2-SG-06.pdf.

[3] I. Sushko and L. Gardini, “Center Bifurcation for Two-Dimensional Border-Collision Normal Form,” *International Journal of Bifurcation and Chaos* 18 (2008). DOI: 10.1142/S0218127408020823. Author-posted article: https://www.mdef.it/public/fileadmin/whoiswho/gardini/Publications/Journals/SG_CenterBif_08.pdf.

[4] L. Gardini, D. Radi, N. Schmitt, I. Sushko, F. Westerhoff, “Abundance of weird quasiperiodic attractors in piecewise linear discontinuous maps,” arXiv:2504.04778 (2025), especially Definition 1 and §2.
