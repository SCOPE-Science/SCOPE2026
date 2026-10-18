# A sharp Crofton transition and diamond law for equilateral three-disk transversals

## Finding

Let three closed Euclidean disks have equal radius \(r\) and equilateral centers of mutual separation \(d\), where \(0<r<d/2\). A random unoriented affine line is sampled with the Euclidean-motion-invariant measure \(d\theta\,dt\), \(0\le\theta<\pi\), conditional on hitting at least one disk. Write \(K\in\{1,2,3\}\) for the number of disks hit, and \(q=2r/d\in(0,1)\). Define

\[
B(q)=2\left[q\arcsin q+\sqrt{1-q^2}-1\right],\qquad q_0=\frac{\sqrt3}{2},
\]
\[
T(q)=\begin{cases}0,&0<q\le q_0,\\6\left[q\left(\frac\pi6-\arccos q\right)+\sqrt{1-q^2}-\frac12\right],&q_0<q<1,\end{cases}
\]
\[
Z(q)=3\pi q-3B(q)+T(q).
\]

**The complete normalized law** is

\[
\boxed{\begin{aligned}
\mathbb P(K=1)&=\frac{3\pi q-6B(q)+3T(q)}{Z(q)},\\
\mathbb P(K=2)&=\frac{3B(q)-3T(q)}{Z(q)},\\
\mathbb P(K=3)&=\frac{T(q)}{Z(q)}.
\end{aligned}}
\]

The triple-hit event has positive probability **exactly when** \(q>q_0\), or \(r/d>\sqrt3/4\). This is also exactly the threshold at which all three orthogonal projection intervals form a connected union **for every line orientation**. In that regime,

\[
Z(q)=3+\pi q,
\]

and, with \(H(q)=\sqrt{1-q^2}-q\arccos q\),

\[
\boxed{\left(\mathbb P(K=1),\mathbb P(K=2),\mathbb P(K=3)\right)
=\frac{\left(3+6H(q),\ 3-12H(q),\ \pi q-3+6H(q)\right)}{3+\pi q}.}
\]

**Sharp onset and conditional geometric limit.** Put \(\varepsilon=r/d-\sqrt3/4>0\). Then

\[
\mathbb P(K=3)=\frac{24}{3+\pi\sqrt3/2}\,\varepsilon^2+O(\varepsilon^3).
\]

There are exactly three critical unoriented line-normal angles \(\theta_j=\pi/6+j\pi/3\), \(j=0,1,2\). Conditional on hitting all three disks and as \(\varepsilon\downarrow0\), the corresponding critical-angle index is asymptotically uniform on these three values. Let \(c_i\) denote the three disk centers and \(n_\theta=(\cos\theta,\sin\theta)\). Define the projection midpoint

\[
m(\theta)=\frac{\max_i\langle n_\theta,c_i\rangle+\min_i\langle n_\theta,c_i\rangle}{2}.
\]

For the unique critical index in whose shrinking neighborhood the normal angle lies, set

\[
s=\frac{\theta-\theta_j}{\varepsilon},\qquad v=\frac{t-m(\theta)}{d\varepsilon}.
\]

Then \((s,v)\) converges weakly to the **uniform area law on the diamond**

\[
\boxed{\mathcal D=\left\{(s,v)\in\mathbb R^2:\frac{|s|}{4}+|v|\le1\right\}.}
\]

The critical index is independent of the limiting diamond coordinates. Moreover \(\mathbb P(K=3)\) is strictly increasing for \(q_0<q<1\). The externally tangent limiting probability vector, as \(q\uparrow1\), is \(\left(3,3,\pi-3\right)/(3+\pi)\).

## Assumptions and scope

There are precisely three congruent disks, distinct centers at the vertices of an equilateral triangle, and \(0<2r/d<1\), so their interiors are pairwise disjoint. The random line has unoriented normal-angle parameter \(\theta\in[0,\pi)\) and signed offset \(t\in\mathbb R\), invariant measure \(d\theta\,dt\), restricted and renormalized to lines intersecting their union. Tangent lines form a null set; \(K\) counts line/disk intersection events, equivalently components of the line's intersection with the disjoint union. All results are exact for every \(0<q<1\) and do not presume independent disk-hit events. Critical-angle coordinates use angles locally lifted from the quotient modulo \(\pi\).

## Proof

**Interval representation and first factorial measure.** Fix \(\theta\), put \(n=(\cos\theta,\sin\theta)\), and project the three centers to \(p_i=\langle n,c_i\rangle\). A line \(\langle n,x\rangle=t\) meets disk \(i\) if and only if \(t\in[p_i-r,p_i+r]\). Thus the measure of lines meeting a single disk is \(2\pi r=\pi qd\), and the sum of the three single-hit measures is \(3\pi qd\).

**Pairs.** A pair of projected centers has gap \(d|\cos\theta|\) after rotation of angle. Its two radius-\(r\) offset intervals overlap in length \(d(q-|\cos\theta|)_+\). Integrating over \([0,\pi)\) and using symmetry gives

\[
\frac1d\int_0^\pi d(q-|\cos\theta|)_+\,d\theta
=2\int_{\arccos q}^{\pi/2}(q-\cos\theta)\,d\theta=B(q).
\]

There are three congruent center pairs; the sum of all pair-hit measures is \(3dB(q)\).

**Triples and their sharp threshold.** Three equal-length intervals have common overlap length \(d(q-w(\theta)/d)_+\), where \(w(\theta)=\max_i p_i-\min_i p_i\) is the directional width of the center triangle. On each of its six equal angular sectors, the width divided by \(d\) equals \(\cos\delta\) for \(0\le\delta\le\pi/6\). In particular its minimum is \(q_0\). Consequently

\[
\frac1d\mu\{\text{lines meeting all three disks}\}
=6\int_{\arccos q}^{\pi/6}(q-\cos\delta)\,d\delta=T(q)
\]

when \(q>q_0\), and is zero otherwise. The integral is elementary and gives the stated piecewise formula.

**Law and gap closure.** The union measure is, by inclusion-exclusion,
\(dZ(q)=3\pi qd-3dB(q)+dT(q)\). Let \(M_k\) denote the unnormalized line measure with exactly \(k\) hits. Then \(M_1+2M_2+3M_3=3\pi qd\), \(M_2+3M_3=3dB(q)\), and \(M_3=dT(q)\). Solving yields the three stated probabilities after division by \(dZ(q)\). The largest separation between consecutive ordered projected centers is always at most \(\sqrt3 d/2\), with equality for a normal perpendicular to a side. Hence \(q\ge q_0\) if and only if the three projected offset intervals form one interval for every \(\theta\). Once connected, their union length is \(w(\theta)+qd\). Cauchy's width formula \(\int_0^\pi w(\theta)\,d\theta=\operatorname{perimeter}(\operatorname{conv}\{c_i\})=3d\) yields \(Z(q)=3+\pi q\). Substitution and \(\arcsin q+\arccos q=\pi/2\) produce the simplified vector.

**Quadratic onset.** Near a critical angle \(\theta_j\), the center-triangle width has the uniform local expansion

\[
\frac{w(\theta_j+u)}d=\frac{\sqrt3}2+\frac{|u|}{2}+O(u^2).
\]

Writing \(q=q_0+2\varepsilon\), the triple overlap exists only for \(|u|<4\varepsilon+O(\varepsilon^2)\) and its offset length is \(d(2\varepsilon-|u|/2+O(\varepsilon^2))\). Integrating on either side of each of the three critical angles gives \(8d\varepsilon^2+O(d\varepsilon^3)\) per angle and hence \(T(q)=24\varepsilon^2+O(\varepsilon^3)\). Since \(Z(q_0)=3+\pi\sqrt3/2\), the displayed onset follows.

**Diamond limit.** Every triple-hit line belongs to one of the three shrinking critical-angle neighborhoods. Centering its offset by \(m(\theta)\) changes its admissible interval exactly to the interval of half-length \(d(q-w(\theta)/d)/2\). Under \(s=(\theta-\theta_j)/\varepsilon\), \(v=(t-m(\theta))/(d\varepsilon)\), the admissible sets converge (in area and away from null boundaries) to \(\mathcal D\), since \(|v|\le1-|s|/4+O(\varepsilon)\). The invariant measure becomes \(d\varepsilon^2\,ds\,dv\); the diamond has area \(8\). Bounded convergence on these uniformly bounded supports proves conditional uniform convergence on \(\mathcal D\) and equiprobability of the three equal-area components; symmetry gives index/coordinate independence in the limit.

**Strict monotonicity of triple-hit probability.** Above threshold, \(T(q)=\pi q-3+6H(q)\), \(H'(q)=-\arccos q\), \(Z(q)=3+\pi q\). Therefore the sign of \(d(T/Z)/dq\) is the sign of \(6[\pi(1-\sqrt{1-q^2})-3\arccos q]\). This expression vanishes at \(q=q_0\) and has strictly positive derivative \([\pi q+3]/\sqrt{1-q^2}\) thereafter, proving strict increase. Taking \(q\uparrow1\) gives the limiting vector.

## Verification

The independent numerical checker `check_triple_disks.py` computes offset-hit multiplicities by an interval-breakpoint sweep independent of the analytic formulas, integrates them over angle at nine distinct radii, compares against the closed forms, and performs three independent simulation checks. It checks the critical quadratic coefficient using high-precision arithmetic and the external-tangency limit. Run `python check_triple_disks.py` with Python, NumPy, SciPy, and mpmath. Reported success: `TRIPLE_DISK_TRANSVERSAL_OK quadrature_cases=9 monte_carlo=3 critical_tests=4`. These finite checks are corroborative only; the all-parameter formulas and the weak limit follow from the proof above.

## Relationship to prior work

The line-transversal literature develops topological, combinatorial, and Helly-type **existence** results for transversals of convex families, notably the work of Bracho--Montejano--Oliveros and Montejano--Karasev. Their inspected statements do not imply a motion-invariant complete three-disk hit-count law, its coincident projection-gap transition, or the conditional diamond limit. Existence of a common line at the critical radius follows from elementary geometry and is not claimed as new. Classical Crofton/Cauchy integration and pairwise interval overlaps are likewise not claimed as new: the contribution is the combined exact three-way probability law and its critical geometric scaling. A prior inverse result about pairwise distances from line sections of perforated convex windows concerns second factorial moments and does not establish the third-order line-incidence probability or its conditional local shape.

## Limitations

The sampling model is motion-invariant affine **unoriented** lines conditioned on meeting the union; choosing chords by endpoints or midpoints gives different laws. The disks are congruent, equilateral, pairwise interior-disjoint, and planar. This does not classify arbitrary triples of convex bodies, derive noisy-data bounds, or prove historical uniqueness. The critical limit is weak convergence after centering and scaling, not a uniform finite-\(\varepsilon\) approximation theorem. Independent mathematical audit remains unperformed.

## References

1. L. Montejano and R. N. Karasev, *Topological transversals to a family of convex sets*, arXiv:1006.0104v1, first publicly posted 2010-06-01. https://arxiv.org/abs/1006.0104
2. J. Bracho, L. Montejano, and D. Oliveros, *The Topology of the Space of Transversals Through the Space of Configurations*, preprint of a 2002 article, lawful manuscript https://www.matem.unam.mx/~luis/pdfs/transconfigura.pdf
3. T. Bisztriczky, F. Fodor, and D. Oliveros, *The T(4) property of families of unit disks*, 2008. https://www.researchgate.net/publication/225792415_The_T4_property_of_families_of_unit_disks
