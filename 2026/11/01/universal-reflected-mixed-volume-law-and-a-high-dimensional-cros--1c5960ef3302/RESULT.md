# Universal reflected mixed-volume law and a high-dimensional crossover for symmetric-base frusta

## Finding
Let \(n\ge2\) and let \(B\subset\mathbb R^{n-1}\) be any full-dimensional centrally symmetric convex body, centered at the origin. For \(0\le a\le1\), set
\[
F_a(B)=\{(x,z):0\le z\le1,\;x\in[1-(1-a)z]B\}.
\]
Writing \(V_n\) for standard symmetric Minkowski mixed volume and \(0\le j\le n\), **every reflected mixed-volume coefficient is independent of the shape of the base**:
\[
\boxed{\frac{V_n(F_a(B)[n-j],[-F_a(B)][j])}{\operatorname{vol}_n(F_a(B))}=\frac{2-a^j-a^{n-j}}{1-a^n}\quad(0\le a<1).}
\tag{1}
\]
At \(a=1\), the quotient is \(1\). At \(a=0\), adopt \(0^0=1\), so the interior coefficients are \(2\) and the two endpoint coefficients are \(1\). In fact the entire reflected Minkowski polynomial is explicit: for \(s\ge0\) and \(0\le a<1\),
\[
\boxed{\operatorname{vol}_n(F_a(B)+s[-F_a(B)])
=\frac{\operatorname{vol}_{n-1}(B)}{n(1-a)}
\left[2(1+s)^n-(1+as)^n-(a+s)^n\right].}
\tag{2}
\]
The \(a=1\) value is \(\operatorname{vol}_{n-1}(B)(1+s)^n\).

For each fixed \(n\ge2\) and interior index \(1\le j\le n-1\), the quotient in (1) is **strictly decreasing** in \(a\), from \(2\) to \(1\). For \(0<a<1\), the coefficients are strictly concave and symmetric as a sequence indexed by \(j\), reaching their maximum at its middle index or middle pair.

Consequently the difference-body volume ratio has the complete sharp profile
\[
\boxed{\frac{\operatorname{vol}_n(F_a(B)-F_a(B))}{\operatorname{vol}_n(F_a(B))}
=\frac{2[2^n-(1+a)^n]}{1-a^n},\qquad 0\le a<1,}
\tag{3}
\]
with the continuous endpoint \(2^n\) at \(a=1\). It is strictly decreasing from \(2^{n+1}-2\) to \(2^n\).

There is an exact high-dimensional crossover. For fixed \(c\ge0\), put \(a_n=e^{-c/n}\). Then, for any sequence of centrally symmetric bases \(B_n\subset\mathbb R^{n-1}\),
\[
\boxed{\lim_{n\to\infty}\frac{\operatorname{vol}_n(F_{a_n}(B_n)-F_{a_n}(B_n))}{2^n\operatorname{vol}_n(F_{a_n}(B_n))}
=\frac{2}{1+e^{-c/2}}.}
\tag{4}
\]
For every fixed \(0\le a<1\), the same normalized ratio instead tends to \(2\) as \(n\to\infty\). The transition thus occurs at taper distance of order \(1/n\) from the symmetric prism endpoint.

## Assumptions and scope
The base is a compact convex subset of \(\mathbb R^{n-1}\) with nonempty interior and central symmetry about the origin; neither polyhedral structure nor a smooth boundary is required. Any originally centered-at-\(u\) base can be put in the stated position by an affine shear. The height \(1\) and centered homothety are fixed by affine normalization. The body \(F_0(B)\) is a pyramid over \(B\), whereas \(F_1(B)=B\times[0,1]\) is a centrally symmetric prism after translation.

The mixed-volume normalization is
\[
\operatorname{vol}_n(K+sL)=\sum_{j=0}^n\binom nj V_n(K[n-j],L[j])s^j\qquad(s\ge0).
\]
The logarithmic/high-dimensional statement involves an arbitrary new centrally symmetric base in each dimension; no assumption of asymptotic convergence of the bases is needed. Formula (1) covers the endpoints \(j=0,n\) as well as the interior indices. Formula (4) includes \(c=0\), interpreted using the \(a=1\) endpoint.

## Proof
**Exact horizontal sections.** Write \(b=1-a\). For \(s>0\), an element \((y,z)\) of \(F_a(B)+s[-F_a(B)]\) is
\[
(y,z)=(x_0,z_0)-s(x_1,z_1),\quad z_0,z_1\in[0,1],\quad x_i\in(1-bz_i)B.
\]
The allowed heights are precisely \(-s\le z\le1\), with constraint \(z=z_0-sz_1\). Because \(B=-B\) and it is convex, for any fixed pair of heights the horizontal sum is *exactly*
\[
(1-bz_0)B+s[-(1-bz_1)B]=(1+s-b(z_0+sz_1))B.
\]
Inclusion between nonnegative homothetic copies of \(B\) is governed by the scale factor. Since \(z_0+sz_1\ge|z_0-sz_1|=|z|\), every possible slice is contained in \((1+s-b|z|)B\). This upper scale is attained: for \(0\le z\le1\), take \((z_0,z_1)=(z,0)\); for \(-s\le z\le0\), take \((z_0,z_1)=(0,-z/s)\). Consequently the *entire* horizontal section at height \(z\) is exactly
\[
\boxed{(F_a(B)+s[-F_a(B)])_z=(1+s-b|z|)B\quad(-s\le z\le1).}
\tag{5}
\]
The same identity at \(s=0\) follows directly. This argument remains valid if \(a=0\) or the base is nonsmooth: at the apex the scale zero denotes a singleton.

**Volume polynomial and mixed coefficients.** Let \(v=\operatorname{vol}_{n-1}(B)>0\). Using the section formula (5), for \(0\le a<1\),
\[
\begin{aligned}
\frac{\operatorname{vol}_n(F_a+s[-F_a])}{v}
&=\int_{-s}^0(1+s+bz)^{n-1}\,dz
+\int_0^1(1+s-bz)^{n-1}\,dz\\
&=\frac{2(1+s)^n-(1+as)^n-(s+a)^n}{nb}.
\end{aligned}
\]
The integral also holds at \(s=0\), establishing (2). Setting \(s=0\) gives
\[
\operatorname{vol}_n(F_a)=\frac{v(1-a^n)}{n(1-a)}=\frac vn\sum_{i=0}^{n-1}a^i.
\tag{6}
\]
The coefficient of \(s^j\) in the right-hand side of (2) is \(v\binom nj(2-a^j-a^{n-j})/[n(1-a)]\). Comparison with the mixed-volume polynomial and division by (6) proves (1), including the exceptional endpoint cases \(a=0,1\). If \(a=1\), the right-hand side of (5) is constant \((1+s)B\), so direct integration yields \(\operatorname{vol}_n(F_1+s[-F_1])=v(1+s)^n\), recovering the asserted limit without division by zero.

**Strict monotonicity in taper.** For \(1\le j\le n-1\), set \(k=n-j\). Algebraically,
\[
\frac{2-a^j-a^k}{1-a^n}
=1+\frac{(1-a^j)(1-a^k)}{1-a^n}.
\tag{7}
\]
At \(a=e^{-u}\in(0,1)\), \(u>0\), define \(h_u(t)=t/(e^{ut}-1)\) for \(t>0\). This is strictly decreasing: the derivative numerator after clearing positive denominators is \(e^{ut}(1-ut)-1<0\), because its derivative in \(ut>0\) is negative and it vanishes at zero. The logarithmic derivative of the positive quotient in (7), with respect to \(\log a\), is
\[
-h_u(j)-h_u(k)+h_u(n)<0,
\]
because \(n>j,k\). This proves strict decrease in \(a\in(0,1)\), and endpoint continuity gives strict decrease on all of \([0,1]\). The limits from (7) are \(2\) at \(0\) and \(1\) at \(1\).

**Index concavity.** For \(1\le j\le n-1\) and \(0<a<1\), the second difference of the normalized coefficients is
\[
\frac{-\left(1-a\right)^2\left(a^{j-1}+a^{n-j-1}\right)}{1-a^n}<0.
\]
Symmetry under \(j\mapsto n-j\) is explicit in (1), proving the middle-index maximum. Index concavity is not asserted to be strict at every index when \(a=0\).

**Difference-body ratio and crossover.** Set \(s=1\) in (2), divide by (6), and obtain (3). By (1) and the mixed-volume expansion, the same difference-body ratio equals the binomially weighted sum of all normalized coefficients, including the two constant endpoints. Since each interior coefficient decreases strictly, so does the ratio (the index set is nonempty for \(n\ge2\)). The endpoint values follow by continuity and the explicit formula.

For \(c>0\) and \(a_n=e^{-c/n}\), division of (3) by \(2^n\) gives
\[
\frac{2\left[1-\left((1+e^{-c/n})/2\right)^n\right]}{1-e^{-c}}.
\]
The numerator exponential term tends to \(e^{-c/2}\), giving \(2(1-e^{-c/2})/(1-e^{-c})=2/(1+e^{-c/2})\). For \(c=0\), each member is the prism \(a_n=1\) and the value is exactly \(1\), agreeing with the formula. For any fixed \(a<1\), the two exponentials \(((1+a)/2)^n\) and \(a^n\) vanish, giving limit \(2\). All statements therefore hold uniformly over choices of bases, because no expression contains the shape of \(B\).

## Verification
The self-contained `verify.py` first evaluates the two slice integrals by separate binomial sums over exact rational parameters. It compares these with the compact polynomial, its binomially expanded mixed-volume coefficients, endpoint normalization, reflection symmetry and strict index concavity for dimensions \(2\) through \(15\), including both degenerate taper endpoints. It then independently builds Minkowski difference-vertex hulls in dimensions \(3\) and \(4\), using a centrally symmetric hexagon and a centrally symmetric box as bases; the convex-hull volumes agree with the analytic formula in each of 24 additional cases. Running `python verify.py` gave `VERIFY_OK 1830 tests`. NumPy/SciPy are required only for the convex-hull diagnostics. These finite computations corroborate the exact proof but do not certify its universal quantifiers.

## Relationship to prior work
Fryš, Kotrbatý, Mouamine and Wang (2026) proved the sharp Godbersen inequality and simplex equality characterization, providing a natural reason to quantify reflected mixed-volume coefficients for explicit non-simplex families. Their Theorems 1.2 and 1.5 establish bounds/equality, not formulas (1)--(4) for centered symmetric-base frusta. Artstein-Avidan and Putterman (2024/2025) study unbalanced difference bodies and weighted combinations of general mixed volumes; their Theorems 3, 4 and 7 likewise do not state the universal shape-independent frustum coefficients or crossover.

The recorded result *Universal Santaló and volume-product laws for homothetic frusta* studies the same geometric deformation, including arbitrary asymmetric bases, but computes polar-volume and Santaló/Mahler invariants rather than reflected mixed volumes. The recorded result *Exact Godbersen mixed-volume profile for one-vertex simplex truncations* concerns a truncated simplex, with an essentially asymmetric base in higher dimension, and a different coefficient formula. Neither statement contains (5), the full universal coefficients, or their high-dimensional boundary layer. Conventional formulas for the volume of a single pyramid or frustum likewise do not compute the reflected Minkowski polynomial.

## Limitations
Central symmetry of the base and a common homothety center for the two faces are essential to the step \(B+(-sB)=(1+s)B\). General noncentrally-symmetric bases, skew frusta and arbitrary prismatoids are not covered. The theorem is not a new universal Godbersen inequality, Rogers--Shephard inequality, or stability theorem for all convex bodies. The sharpness of the endpoint values refers only to the prescribed frustum family. No priority claim is made against inaccessible older literature on truncated cones or frusta; a hidden equivalent classical Minkowski-sum calculation is the main residual originality risk.

## References
1. F. Fryš, J. Kotrbatý, M. A. Mouamine and S. Wang, *Higher-order Godbersen inequality and a characterization of simplices via the face lattice*, arXiv:2610.06806v1, first public 5 October 2026; revised v2, 12 October 2026, especially Theorems 1.2 and 1.5.
2. S. Artstein-Avidan and E. Putterman, *On unbalanced difference bodies and Godbersen's conjecture*, arXiv:2412.05308v1, first public 27 November 2024, and revised v2; Theorems 3, 4 and 7.
3. *Universal Santaló and volume-product laws for homothetic frusta*, public mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-universal-santal-and-volume-product-laws-for-homothetic-frusta--3dbfdaf0b359.
4. *Exact Godbersen mixed-volume profile for one-vertex simplex truncations*, public mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-godbersen-mixed-volume-profile-for-one-vertex-simplex-trun--dda979276949.
5. C. A. Rogers and G. C. Shephard, *The difference body of a convex body*, Archiv der Mathematik 8 (1957), 220--233.
