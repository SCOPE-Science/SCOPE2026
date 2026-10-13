# Singularities of the reflection divisor on even-degree Fermat surfaces

## Finding
For every even integer \(d\ge 4\), let \(S_d\subset\mathbb P^3_{\mathbb C}\) be the smooth degree-\(d\) Fermat surface
\[
S_d=V(x_0^d+x_1^d+x_2^d+x_3^d).
\]
Let \(\mu_d\) be the group of \(d\)-th roots of unity. Define the hyperplane family \(\mathcal H_d\) to consist of the four coordinate planes \(V(x_i)\) and the \(6d\) planes \(V(x_j+\zeta x_i)\), one for each \(0\le i<j\le3\) and \(\zeta\in\mu_d\). Let \(D_d=\sum_{H\in\mathcal H_d}(S_d\cap H)\) be the reduced divisor.

**Theorem.** The divisor \(D_d\) has exactly \(4+6d\) smooth irreducible components, each a plane curve of genus \(\frac{(d-1)(d-2)}2\). Its complete singularity basket consists of
\[
\begin{array}{c|c}
\text{ordinary point multiplicity}&\text{number of points}\\\hline
 d+2&6d\\
 3&4d^3\\
 2&12d^2+3d^3.
\end{array}
\]
There are no other singularities and none of these points coincide. Consequently,
\[
\#\operatorname{Sing}(D_d)=7d^3+12d^2+6d,\qquad
\delta(D_d)=18d^3+21d^2+6d,
\]
where \(\delta(D_d)\) denotes the sum of local delta-invariants, and
\[
p_a(D_d)=21d^3+14d^2+1.
\]
For the Fermat quartic, these are precisely the \(28\) fixed-plane sections associated with its \(28\) quasi-Galois points. In this case the singularity basket is \(24\) ordinary sixfold points, \(256\) ordinary triple points, and \(384\) ordinary nodes, or \(664\) distinct singular points in total.

## Assumptions and scope
All schemes and intersections are over \(\mathbb C\); \(d\) is **even** and at least four. A point of an ordinary \(m\)-fold curve singularity has exactly \(m\) smooth local branches with pairwise distinct tangent lines. Its local delta-invariant is \(\binom m2\). The divisor has the reduced scheme structure on the smooth surface. No statement is asserted for odd \(d\), where the paired-coordinate plane sections have a different, reducible form.

## Proof
**1. Distinct smooth components.** There are four coordinate planes and \(d\) paired-coordinate planes for each of six unordered index pairs; these are distinct. In a coordinate plane the section is a smooth Fermat plane curve of degree \(d\). On a plane \(x_j+\zeta x_i=0\), evenness of \(d\) and \(\zeta^d=1\) reduce the equation of the section to \(2x_i^d+x_k^d+x_l^d=0\), with the two unused indices \(k,l\). In characteristic zero, these Fermat-type plane curves are smooth. Thus each is irreducible and has the stated genus; no component is repeated.

**2. Complete list of multiple-plane lines.** Intersect any two distinct planes in \(\mathcal H_d\). Inspection of their supports gives precisely the following rank-two flats, where the multiplicity is the total number of planes containing that projective line:

| Type of line | Number | Plane multiplicity | Restriction of the Fermat equation |
| --- | ---: | ---: | --- |
| \(x_i=x_j=0\) | \(6\) | \(d+2\) | \(s^d+t^d\) |
| three linked coordinates, \(x_j=-\zeta x_i,\ x_k=-\eta x_i\) | \(4d^2\) | \(3\) | \(3s^d+t^d\) |
| one zero coordinate and an unrelated linked pair | \(12d\) | \(2\) | \(2s^d+t^d\) |
| two disjoint linked coordinate pairs | \(3d^2\) | \(2\) | \(2s^d+2t^d\) |

The counts follow from choosing respectively two indices; three indices and two independent roots; one zero index and a pair among the other three with a root; or one of three partitions into two pairs with two roots. There are no other possibilities for two hyperplane supports. For example, two different relations on the same pair force both coordinates to vanish; two overlapping pair relations link three coordinates. As a check, the weighted pair count is
\[
6\binom{d+2}{2}+4d^2\binom32+(12d+3d^2)\binom22=\binom{4+6d}{2}.
\]

**3. Distinct, transverse points and no extra collisions.** Every displayed line is parametrized so that the restriction of \(F_d=\sum x_i^d\) is \(as^d+bt^d\) with \(a,b\) strictly positive integers. It has exactly \(d\) distinct zeros in \(\mathbb P^1_{\mathbb C}\). In particular the line meets \(S_d\) transversely. At each resulting point, the different plane-section curves are smooth and their tangent lines on \(S_d\) are distinct, since their two plane equations restrict independently to the tangent plane \(T_pS_d\). Thus the singularity is an ordinary point with multiplicity equal to the number of planes containing the line.

It remains to ensure that different rank-two flats never share a point on \(S_d\). Any point at the intersection of three linearly independent hyperplanes from this family has only one free nonzero coordinate parameter: each plane relation either zeroes one coordinate or identifies two coordinates up to multiplication by a \(d\)-th root of unity (and a minus sign, which is itself a \(d\)-th root because \(d\) is even). This follows by making a graph on the four coordinate indices; each connected component of nonzero coordinates contributes one free parameter, so three independent equations and projective dimension zero permit only one nonzero component. Hence at such a point all \(r\in\{1,2,3,4\}\) nonzero coordinates have the same \(d\)-th power \(c^d\). It would give \(F_d=rc^d\ne0\) in characteristic zero. Therefore no rank-three flat lies on \(S_d\), and the intersection points counted above are pairwise distinct. Outside the rank-two flats a single smooth plane-section component passes through each point, so there are no other singularities.

**4. Singularities and genus.** Multiply each flat count by its \(d\) transverse intersection points to obtain the three entries of the basket. The total number of points is \(6d+4d^3+12d^2+3d^3=7d^3+12d^2+6d\). The total local delta-invariant is
\[
6d\binom{d+2}{2}+4d^3\binom32+(12d^2+3d^3)\binom22
=18d^3+21d^2+6d.
\]
If \(H\) is the hyperplane class on \(S_d\), then \(H^2=d\), \(K_{S_d}=(d-4)H\), and \(D_d\sim(4+6d)H\). Adjunction yields
\[
p_a(D_d)=1+\frac{D_d\cdot(D_d+K_{S_d})}{2}=1+21d^3+14d^2.
\]
Independently the normalization is the disjoint union of the smooth components, so
\[
(4+6d)\frac{(d-1)(d-2)}2+\delta(D_d)-(4+6d)+1
=21d^3+14d^2+1.
\]
For \(d=4\), Miura and Taki classify the four coordinate centers and twenty-four two-coordinate centers as all quasi-Galois points of the Fermat quartic. Each coordinate point generates a diagonal automorphism fixing \(x_i=0\), while the nontrivial involution associated to \(P=[e_i+\zeta e_j]\) is represented by \((x_i,x_j)\mapsto(-\zeta^{-1}x_j,-\zeta x_i)\), acting trivially on the other two coordinates. Its fixed plane is \(x_j+\zeta x_i=0\). Therefore all twenty-eight constructed plane sections are exactly the fixed-plane sections claimed.

## Verification
An independent exact-arithmetic program `check_reflection_divisor.py` constructs all \(28\) fixed planes for \(d=4\) over Gaussian rationals. It groups all \(\binom{28}{2}=378\) plane pairs by their intersection lines and verifies the rank-two flat counts \(6,64,96\) of multiplicity \(6,3,2\). For every pair, it restricts the quartic to the line and computes a polynomial gcd to certify four distinct roots over \(\mathbb C\). Symbolic identities check weighted pair counts, number of points, delta-invariants and adjunction for general formal \(d\); several even values are also tabulated. The unlimited-degree assertion follows from the proof's support classification and characteristic-zero transversality, not from finite checks.

## Relationship to prior work
Miura and Taki, *Quasi-Galois points for quartic surfaces* (arXiv:2608.25445v1, Sections 3 and 5), prove that the quartic has exactly four Galois plus twenty-four further quasi-Galois centers; their article does not evaluate the singularities of the union of fixed-plane sections. Miura and Takahashi, *Projective Lifting Theorem, Complex Reflection Groups, and Quasi-Galois Points for Fermat Varieties* (arXiv:2610.09331v1, October 7, 2026, Sections 3 and 4), extend the classification of reflection centers to general Fermat varieties and describe monomial reflections. That stronger center result neither describes the rank-two intersection fibers on the Fermat surface nor implies the ordinary singularity basket without additional geometric arguments. Classical complex-reflection hyperplane-arrangement theory supplies the ambient rank-two combinatorics, but not by itself the noncollision and transverse-restriction properties on \(S_d\).

## Limitations
The assertion holds over \(\mathbb C\) for even \(d\ge4\); analogous counts need not hold in positive characteristic or for odd \(d\). It determines the reduced divisor's ordinary singularities and additive delta invariants, not the global log resolution or the full equisingular deformation space. An earlier equivalent surface-section intersection calculation in the extensive literature on Fermat/reflection arrangements remains a bibliographic risk. The October 2026 reference is contextual, not the initiating source for this research result.

## References
1. K. Miura and S. Taki, *Quasi-Galois points for quartic surfaces*, arXiv:2608.25445v1 (first posted August 26, 2026), especially Proposition 5.2 and Theorem 5.4. https://arxiv.org/html/2608.25445v1
2. K. Miura and T. Takahashi, *Projective Lifting Theorem, Complex Reflection Groups, and Quasi-Galois Points for Fermat Varieties*, arXiv:2610.09331v1 (first posted October 7, 2026), especially Proposition 4.5 and Theorem 1.8. https://arxiv.org/html/2610.09331v1
3. P. Orlik and H. Terao, *Arrangements of Hyperplanes*, Grundlehren der mathematischen Wissenschaften 300, Springer (1992), for general intersection-flat theory of complex reflection arrangements.
