# Exact convexification of Hardy monomial-composition Berezin ranges

## Finding
For every integer \(m\ge2\), consider the Hardy-space composition operator \(C_m f=f\circ(z\mapsto z^m)\). Its Berezin range \(B_m\) has the **exact closed convex hull**
\[
K_m:=\overline{\operatorname{co}}B_m
=\operatorname{co}\left(\{1\}\cup
\overline D\left(\frac1{m+1},\frac1{m+1}\right)\right).
\]
Here \(\overline D(c,R)=\{z\in\mathbb C:|z-c|\le R\}\) is a closed planar disk. This is the convex hull of one point and a tangent disk, with two straight tangent edges and one circular arc. Its support function is
\[
h_m(\theta)=\sup_{z\in B_m}\operatorname{Re}(e^{-i\theta}z)
=\max\left\{\cos\theta,\frac{1+\cos\theta}{m+1}\right\}.
\]
The supremum is attained by a Berezin value if and only if \(\cos\theta\ge 1/m\), in which case the only attaining value is \(1\). The area and perimeter are exactly
\[
\operatorname{Area}(K_m)=
\frac{\pi+\sqrt{m^2-1}-\arccos(1/m)}{(m+1)^2},
\qquad
\operatorname{Perimeter}(K_m)=
\frac{2\{\pi+\sqrt{m^2-1}-\arccos(1/m)\}}{m+1}.
\]
For the interval \(I=[0,1]\subset\mathbb R\), the Hausdorff distance is
\[
d_H(K_m,I)=\frac1{m+1},\qquad
\operatorname{Area}(K_m)\sim\frac1m.
\]
In sharp contrast, the closure of the ordinary numerical range \(W(C_m)\) is the entire closed unit disk for all \(m\ge2\).

## Assumptions and scope
The Hardy space \(H^2(\mathbb D)\) consists of analytic series \(f(z)=\sum_{j\ge0}a_jz^j\) with \(\sum_{j\ge0}|a_j|^2<\infty\). Its normalized Szegő kernel is \(\widehat{k}_w(z)=\sqrt{1-|w|^2}/(1-\bar wz)\) for \(w\in\mathbb D\). The Berezin range is \(B_m=\{\langle C_m\widehat{k}_w,\widehat{k}_w\rangle:w\in\mathbb D\}\). All convex hulls and support functions are in the real Euclidean plane \(\mathbb C\simeq\mathbb R^2\). Degrees \(m\ge2\) are integers; the degenerate \(m=1\) identity operator is not included. Hausdorff distance uses Euclidean distance on nonempty compact subsets. The source paper's first public arXiv date is October 13, 2026.

## Proof
**1. Circular fibers.** Reproduction gives the exact transform
\[
\langle C_m\widehat{k}_w,\widehat{k}_w\rangle
=\frac{1-|w|^2}{1-\overline w w^m}.
\]
Put \(w=re^{i\phi}\), \(n=m+1\), and \(S_n(r)=\sum_{j=0}^{n-1}r^{2j}\). When \(0<r<1\), as \(\phi\) varies the values trace the circle with real center and radius
\[
c_r=\frac{1-r^2}{1-r^{2n}}=\frac1{S_n(r)},
\qquad
R_r=\frac{(1-r^2)r^n}{1-r^{2n}}=\frac{r^n}{S_n(r)}.
\]
At \(r=0\) the Berezin value is \(1\). As \(r\uparrow1\), the circles converge to the circle bounding \(D=\overline D(1/n,1/n)\). In particular \(\{1\}\cup D\subset K_m\), because the whole limiting circle is in \(\overline{B_m}\), and \(K_m\) is closed and convex.

**2. The decisive uniform inclusion.** Set \(H=\operatorname{co}(\{1\}\cup D)\). For any \(r\in(0,1)\), the disk \(D_r=\overline D(c_r,R_r)\) lies inside \(H\). Indeed the convex combination of \(\{1\}\) and \(D\) with weight \(s=n(1-c_r)/(n-1)\in[0,1]\) on \(D\) is a disk centered at \(c_r\) with radius
\[
\frac{s}{n}=\frac{1-c_r}{n-1}.
\]
The requisite comparison is
\[
(n-1)r^n\le r^2+r^4+\cdots+r^{2(n-1)}=S_n(r)-1.
\]
This is the arithmetic-geometric mean inequality: the geometric mean of the \(n-1\) terms on the right is exactly \(r^n\). Since \(n\ge3\), the inequality is strict when \(0<r<1\). Hence \(R_r<(1-c_r)/(n-1)\), so every noncentral Berezin value lies in the interior of \(H\). Consequently \(B_m\subset H\), proving \(K_m=H\).

**3. Support function and attainment.** The support of a point \(1\) in direction \(e^{i\theta}\) is \(\cos\theta\); the support of \(D\) is \((1+\cos\theta)/n\). Taking the larger proves the displayed support identity. The point support dominates exactly when \((n-1)\cos\theta\ge1\). If it does, \(w=0\) attains the support. Otherwise the supporting point lies on the limiting circle and cannot occur for \(0<r<1\) by strict interior inclusion; \(w=0\) does not maximize either. At equality only the actual Berezin value \(1\) attains support.

**4. Sharp planar geometry.** The disk has radius \(R=1/n\) and its center is distance \(d=(n-1)/n=m/n>R\) from the exceptional point \(1\). Let \(\beta=\arccos(R/d)=\arccos(1/m)\); the two tangent segments each have length \(L=\sqrt{d^2-R^2}=\sqrt{m^2-1}/n\). The exposed circular arc has length \(2R(\pi-\beta)\), so \(\operatorname{Perimeter}(K_m)=2L+2R(\pi-\beta)\). Adding the exterior point-to-tangent-chord triangle and subtracting the corresponding disk segment gives \(\operatorname{Area}(K_m)=\pi R^2+RL-R^2\beta\). Substitution yields both exact formulas.

Because \(0\in D\), the whole interval \(I=[0,1]\) lies inside \(K_m\). Every point of \(K_m\) has real part in \([0,1]\) and imaginary part of absolute value at most \(R=1/n\); the top point \(1/n+i/n\) of \(D\) achieves this value. Therefore \(d_H(K_m,I)=1/n\). Expanding the exact area formula gives \(\operatorname{Area}(K_m)=1/m+O(m^{-2})\).

**5. The contrasting numerical range.** The monomial substitution operator \(C_m\) is an isometry because it sends the orthonormal basis \((z^j)_{j\ge0}\) to the orthonormal family \((z^{mj})_{j\ge0}\). In particular \(W(C_m)\subset\overline D(0,1)\). Yet the orbit \((z,z^m,z^{m^2},\ldots)\) is orthonormal and \(C_m\) shifts it forward. Given any \(\lambda\in\mathbb D\), normalized finite geometric combinations of these orbit vectors have numerical expectations tending to \(\lambda\). Thus \(\overline{W(C_m)}=\overline D(0,1)\) for all \(m\ge2\), despite \(K_m\to[0,1]\) with the exact Hausdorff rate above.

## Verification
The reproducing-kernel identity is exact; no finite sampling is used to prove the theorem. The bundled standalone checker verifies the circle and support inequalities at rational radii with exact rational arithmetic, checks the geometry numerically on independent angular grids, and compares sampled convex hull areas/perimeters against the closed formulas. Run `python3 check.py` with the Python standard library. Sampling verifies implementation only; the proof of all degrees and radii is the AM-GM argument and elementary planar geometry above.

## Relationship to prior work
Bourdon, Le, and Thompson (2026) study Berezin ranges of Hardy composition operators; their Proposition 3.7 establishes the **general circle-fiber property** for symbols of the form \(z\psi(z^k)\). The present monomial family is a special case of that preliminary fiber description; no novelty is claimed for the fiber formula or the general Berezin transform. The additional claim is the exact global closed convex hull with its support-attainment transition, metric collapse, area and perimeter, together with its contrast to the fixed ordinary numerical range. Cowen and Felder (2021/2022) treat geometric questions for automorphic symbols. Augustine, Garayev, and Shankar (2023) treat automorphic/elliptic composition symbols, not this exact monomial hull. A separate existing computation of the imaginary Berezin half-width for monomials gives \(1/(m+1)\) at coefficient one; this one-dimensional width is not claimed as new, and does not determine the full support function or planar geometry.

## Limitations
The finding concerns the closed convex hull, not an exact pointwise membership classification of the nonconvex Berezin set. No general statement is asserted for non-monomial symbols or different reproducing-kernel spaces. The proof is analytical, supplemented by finite checks. The full primary literature was compared on the stated object and invariant, but an unindexed equivalent convex-hull calculation is a residual publication-priority risk. No independent audit has been performed.

## References
1. P. Bourdon, T. Le and D. Thompson, *Berezin Ranges of Composition Operators on \(H^2\)*, arXiv:2610.17634v1 (first public October 13, 2026), especially Proposition 3.7 and Section 4. https://arxiv.org/abs/2610.17634
2. C. C. Cowen and C. Felder, *Convexity of the Berezin Range*, arXiv:2109.12095v1 (2021), later in Linear Algebra and its Applications 647 (2022), 47–63. https://arxiv.org/abs/2109.12095
3. A. Augustine, M. Garayev and P. Shankar, *Composition Operators, Convexity of Their Berezin Range and Related Questions*, arXiv:2302.12547 (2023). https://arxiv.org/abs/2302.12547
