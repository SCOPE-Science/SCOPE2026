# Arithmetic resonance and square-lattice discrepancy for digital planar rotations

## Finding

Let \(0<\theta<\pi/2\) and let \(F_\theta:\mathbb Z^2\to\mathbb Z^2\) be the coordinatewise floor of the counterclockwise rotation through \(\theta\). For \(j\in\{0,1,2\}\) and **integer** \(M\ge1\), let \(N_j(M)\) count target points in \([-M,M]^2\cap\mathbb Z^2\) having exactly \(j\) preimages under \(F_\theta\).

**Theorem (rational-angle resonance law).** Suppose
\[
\cos\theta=\frac aq,\qquad \sin\theta=\frac bq,
\]
where \(a,b,q\) are positive integers, \(a^2+b^2=q^2\), and \(\gcd(a,b,q)=1\). Let \(h\in\{0,\ldots,q-1\}\) satisfy \(ah\equiv b\pmod q\), and write \([z]_q\) for the representative of \(z\bmod q\) in \(\{0,\ldots,q-1\}\). Set
\[
H(a,b,q)=\#\{r\in\mathbb Z:0\le r<q-a,\ [hr]_q<q-b\}.
\]
Then the three limits exist and are exactly
\[
\lim_{M\to\infty}\frac{(N_0(M),N_1(M),N_2(M))}{(2M+1)^2}
=\left(\frac{2H-1}{q},\ 1-\frac{2(2H-1)}q,\ \frac{2H-1}{q}\right).
\]
In particular, \(q\) times the missing-image density is a **positive odd integer**. Writing \(\delta=(2H-1)/q\), there is the uniform quantitative comparison
\[
\left|\delta-(\cos\theta+\sin\theta-1)^2\right|
\le \frac{4\sqrt2}{\sqrt q}+\frac4q.
\]
Thus, on primitive Pythagorean angles with hypotenuse \(q\to\infty\), the exceptional density uniformly approaches the nonresonant angular benchmark. At \((a,b,q)=(3,4,5)\) the actual density is \(1/5\), whereas the nonresonant benchmark evaluated at the same angle equals \(4/25\). This is a genuine arithmetic discontinuity at that rational rotation.

## Assumptions and scope

The rotation matrix is \(R_\theta=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}\) and \(F_\theta(x)=\lfloor R_\theta x\rfloor\), with floor taken in both coordinates, including at integer boundaries. Only positive primitive Pythagorean triples are covered by the new rational formula; no claim is made for other quadrants, other quantizers or higher iterates. The natural primary classification is MSC2020 **37M15** (discretization of a dynamical system). The benchmark \((\cos\theta+\sin\theta-1)^2\) for nonresonant angles is a prior result, not claimed as new here.

## Proof

**1. Fibers have size at most two.** If distinct \(x,y\in\mathbb Z^2\) have the same image, the vector \(R_\theta(x-y)\) has both components strictly between \(-1\) and \(1\); therefore \(\|x-y\|_2^2<2\). Thus \(x,y\) are nearest neighbors in the integer grid. Three distinct points cannot be pairwise nearest neighbors because that grid has no triangles. Each double preimage is therefore a unique unordered horizontal or vertical neighboring pair.

**2. Collision rectangles.** Write \((u,v)=\{R_\theta x\}\in[0,1)^2\), \(c=a/q\), \(s=b/q\). For the positively oriented horizontal edge \((x,x+e_1)\), equality of the two images is equivalent to
\[
0\le u<1-c,\qquad0\le v<1-s.
\]
For the vertically oriented edge \((x,x+e_2)\), it is equivalent to
\[
s\le u<1,\qquad0\le v<1-c.
\]
The two phase rectangles do not intersect because \(c+s>1\). If the target is constrained to the centered square of radius \(M\), then the relevant source points lie in a rotated square of area \((2M+1)^2\), up to boundary displacement bounded independently of \(M\). Any lattice-periodic selection of such points can be counted by residue frequencies with an error \(O_{a,b,q}(M)\): tile the plane with squares of side \(q\), and bound those intersecting the boundary of the rotated square. Consequently the target double-hit density equals the sum of the residue frequencies of the two collision rectangles.

**3. The exact rational phase group.** Since the triple is primitive, \(\gcd(a,q)=\gcd(b,q)=1\). For \(x=(X,Y)\), the phase numerators are
\[
(r,t)\equiv(aX-bY,bX+aY)\pmod q.
\]
From \(h\equiv ba^{-1}\pmod q\) and \(a^2+b^2=q^2\), one obtains \(h^2\equiv-1\pmod q\) and \(t\equiv hr\pmod q\). As \(X,Y\) vary modulo \(q\), each of the \(q\) pairs \((r,[hr]_q)\) occurs exactly \(q\) times. Therefore the horizontal collision frequency is \(H/q\), while the vertical frequency is \(V/q\), where
\[
V=\#\{r:b\le r<q,\ [hr]_q<q-a\}.
\]

**4. Odd numerator.** The quarter turn \((r,t)\mapsto(-t,r)\bmod q\) preserves the phase subgroup, since \(h^2\equiv-1\pmod q\). It maps every point of the horizontal collision rectangle other than \((0,0)\) bijectively onto the vertical collision rectangle. For the converse at the endpoint \(r=b\), observe \([hb]_q=q-a\), which is excluded by the strict vertical inequality. Thus \(H=V+1\), so the double-hit density is \((2H-1)/q\). The point \((0,0)\) guarantees \(H\ge1\), hence the numerator is a positive odd integer.

**5. Vacancies equal collisions.** The number of source points with image in \([-M,M]^2\cap\mathbb Z^2\) is the number of points of \(\mathbb Z^2\) in the rotated square \(R_\theta^{-1}([-M,M+1)^2)\). That count equals its area \((2M+1)^2\) plus \(O(M)\), by covering its boundary with unit cells. Since every target has zero, one or two preimages, \(N_2(M)-N_0(M)=O(M)\). Together with \(N_0+N_1+N_2=(2M+1)^2\), this proves the displayed limiting distribution.

**6. The sharp arithmetic scale.** The phase subgroup lifts to the planar lattice
\[
\Lambda=\{(r,t)\in\mathbb Z^2:t\equiv hr\pmod q\},\qquad [\mathbb Z^2:\Lambda]=q.
\]
A primitive Pythagorean triple has the Euclidean parametrization \(q=m^2+n^2\) and \(\{a,b\}=\{m^2-n^2,2mn\}\), with coprime \(m>n>0\) of opposite parity. If \(a=m^2-n^2\) then \((m,n)\in\Lambda\); if \(a=2mn\) then \((n,m)\in\Lambda\). These congruences follow on multiplying \(t-hr\) by the invertible integer \(a\) modulo \(q\). Quarter-turn invariance supplies the perpendicular vector of the same length \(\sqrt q\). Their determinant is \(q\), so they form a basis for \(\Lambda\). In particular, its Voronoi cells are square cells of area \(q\) and covering radius \(\rho=\sqrt{q/2}\).

For any axis-parallel rectangle \(Q\) of width and height at most \(q\), union the Voronoi cells whose centers lie in \(Q\). The union lies in the \(\rho\)-enlargement of \(Q\) and contains the \(\rho\)-erosion. Writing the sides as \(w,z\), the elementary enclosing-box estimates give
\[
\left|q\,\#(\Lambda\cap Q)-wz\right|\le 2\rho(w+z)+4\rho^2
\le 2\sqrt2\,q^{3/2}+2q.
\]
Apply this once to each collision rectangle \([0,q-a)\times[0,q-b)\) and \([b,q)\times[0,q-a)\). Their areas both equal \((q-a)(q-b)\), and their lattice-point counts are \(H\) and \(V\), respectively. Divide the sum of the two estimates by \(q^2\) to obtain
\[
\left|\frac{H+V}{q}-\frac{2(q-a)(q-b)}{q^2}\right|
\le \frac{4\sqrt2}{\sqrt q}+\frac4q.
\]
Finally \(2(1-a/q)(1-b/q)=(a/q+b/q-1)^2\), using \(a^2+b^2=q^2\). The example \((3,4,5)\) has \(h=3\), \(H=1\), and so \(\delta=1/5\), while \((3/5+4/5-1)^2=4/25\).

## Verification

The companion script `verify.py` enumerates exact modular phase residues for primitive Pythagorean triples, independently evaluates collisions over a complete \(q\times q\) source period, checks the odd-numerator involution, and verifies exact target multiplicities using integer arithmetic for selected triples and finite windows. It also checks the explicit discrepancy bound and an illustrative irrational-angle numerical approximation. Only the proof above establishes the all-parameter and infinite-window assertions; finite checks are diagnostic.

## Relationship to prior work

Hannusch and Pethő, *Rotation on the digital plane* (first public arXiv preprint 4 September 2021; article 2022), prove positive-density loss of injectivity/surjectivity for floor-quantized rotations, establish the nearest-neighbor reduction, and treat Pythagorean residue structure. Their Theorems 3.1 and 4.2 give positivity rather than the present all-triple exact density, odd numerator, and uniform rational-resonance discrepancy estimate.

Vladimirov, *Quantized linear systems on integer lattices: a frequency-based approach* (1996 reports, arXiv:1501.04237), Theorem 19(d), **already gives the full generic nonresonant preimage distribution** with hole frequency \((\cos\theta+\sin\theta-1)^2\) for a translated (nearest-integer) quantizer. Translating the quantizer's fundamental cell changes phase origin but not the nonresonant density. The present novelty is restricted to **the exceptional rational Pythagorean angles**, excluded by his nonresonance condition, together with their square-lattice structural bound. Defant and Propp (2020) independently motivate inverse-multiplicity distributions as dynamical invariants but study different finite systems.

## Limitations

This is a single-step preimage result, not a classification of orbit lengths or entropy. The uniform \(O(q^{-1/2})\) bound is proved but no optimal error constant or finer Diophantine asymptotic is claimed. The formula is a finite congruence count, not an elementary expression solely in the three integer legs. The nearest-integer and floor quantizers can have different resonant boundary behavior; their resonant distributions must not be identified. Earlier discretization literature could contain an equivalent special-resonance count under different terminology; source comparison is documented in the accompanying review.

## References

1. C. Hannusch and A. Pethő, *Rotation on the digital plane*, arXiv:2109.01828 (first public 2021-09-04), *Periodica Mathematica Hungarica* **86** (2023), 564–577; published online 2022-07-16, DOI: 10.1007/s10998-022-00480-8. https://link.springer.com/article/10.1007/s10998-022-00480-8
2. I. G. Vladimirov, *Quantized linear systems on integer lattices: a frequency-based approach*, original CADSEM reports 1996; arXiv:1501.04237, especially Theorem 19(d) and discussion on pp. 55–58. https://arxiv.org/abs/1501.04237
3. V. Kozyakin, N. Kuznetsov, A. Pokrovskii and I. Vladimirov, *Some problems in analysis of discretizations of continuous dynamical systems*, *Nonlinear Analysis* **30** (1997), 767–778, DOI: 10.1016/S0362-546X(96)00232-5.
4. C. Defant and J. Propp, *Quantifying Noninvertibility in Discrete Dynamical Systems*, *Electronic Journal of Combinatorics* **27** (2020), P3.51, DOI: 10.37236/9475.
