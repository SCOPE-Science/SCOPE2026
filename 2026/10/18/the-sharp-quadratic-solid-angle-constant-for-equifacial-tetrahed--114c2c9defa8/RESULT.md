# The sharp quadratic solid-angle constant for equifacial tetrahedra

## Finding

Let \(T\subset\mathbb R^3\) be any nondegenerate **equifacial tetrahedron** (also called a disphenoid or an isosceles tetrahedron): its four triangular faces are congruent, equivalently its three pairs of opposite edges have equal lengths. Let \(V(T)\) be its volume, \(\delta(T)\) its Euclidean diameter (longest edge), and \(\Omega(T)\) its minimum vertex solid angle, in steradians (the area on the unit sphere). Every vertex of an equifacial tetrahedron has the same solid angle.

Then, for **every** such tetrahedron,
\[
\boxed{\quad 0<\Omega(T)^2<6\,\frac{V(T)}{\delta(T)^3}.\quad}
\]
The constant \(6\) is optimal and is not attained by a nondegenerate tetrahedron. Thus the exact supremum of \(\Omega(T)^2/\mu(T)\), where \(\mu(T)=V(T)/\delta(T)^3\) is fullness, is \(6\) over the entire equifacial class.

Moreover, all sequences approaching that supremum are classified: represent each disphenoid, up to Euclidean similarities and relabeling, by the four even-sign vertices \((x,y,z),(x,-y,-z),(-x,y,-z),(-x,-y,z)\), where \(0<x\le y\le z\). For any sequence \(T_k\) of these tetrahedra,
\[
\frac{\Omega(T_k)^2}{\mu(T_k)}\longrightarrow6
\quad\Longleftrightarrow\quad
\frac{y_k}{z_k}\longrightarrow0
\text{ and }\frac{x_k}{y_k}\longrightarrow1.
\]
In geometric terms, only the balanced two-short-edge sliver degeneration is asymptotically sharp.

## Assumptions and scope

All tetrahedra are nondegenerate Euclidean 3-simplices; no regularity beyond being equifacial is assumed. Solid angles use spherical area, not probability normalized by \(4\pi\). The statement concerns this natural symmetry class only; no universal coefficient \(6\) is asserted for arbitrary tetrahedra. Positive coordinate triples are genuine nondegenerate tetrahedra, and the limit tetrahedra in the sharpness assertion are degenerate.

The even-sign coordinate model is exhaustive. Indeed, for a tetrahedron with vertices \(p_1,p_2,p_3,p_4\) centered so that \(\sum_i p_i=0\), put \(v=p_1+p_2\), \(w=p_1+p_3\), and \(h=p_1+p_4\). Equality of each opposite-edge pair forces \(v,w,h\) to be pairwise perpendicular. The four vertices are precisely the four even-sign combinations of \(v/2,w/2,h/2\); their lengths are positive by nondegeneracy. Renaming the orthogonal axes orders \(0<x\le y\le z\).

## Proof

Fix \(0<x\le y\le z\) in the coordinate representation above, and abbreviate
\[
A=\sqrt{x^2+y^2},\quad B=\sqrt{x^2+z^2},\quad C=\sqrt{y^2+z^2},\quad Q=ABC+x^2C+y^2B+z^2A.
\]
The longest edge has length \(2C\), while the determinant of any three edges from one vertex has absolute value \(16xyz\). Therefore
\[
\delta=2C,\qquad V=\frac{8xyz}{3},\qquad \mu=\frac{xyz}{3C^3}.
\]

At the vertex \((x,y,z)\), the three outgoing edges have lengths \(2A,2B,2C\), pairwise scalar products \(4x^2,4y^2,4z^2\) in the corresponding order, and absolute triple product \(16xyz\). The standard trihedral half-angle formula (van Oosterom--Strackee) for a spherical triangle of these directions thus gives, with its positive denominator,
\[
\tan\frac{\Omega}{2}=\frac{2xyz}{Q},\qquad
\Omega=2\arctan\frac{2xyz}{Q}.
\]
The four vertices are symmetry-equivalent, so this is also the minimum vertex solid angle.

Two inequalities are the core of the argument. Since \(A\le\sqrt2\,y\), \(B\le C\), and \(C\ge\sqrt2\,y\) under the chosen ordering,
\[
\frac{y^2}{A}+\frac{z^2}{B}\ \ge\ \frac{y}{\sqrt2}+\frac{z^2}{C}
\ \ge\ \frac{y^2+z^2}{C}=C.
\]
Consequently \(y^2B+z^2A\ge ABC\) and hence
\[
Q=C(AB+x^2)+y^2B+z^2A\ge C(2AB+x^2)>2ABC.
\]
Independently, the exact nonnegative-square identity
\[
(A B)^2-2xyzC=x^4+(xC-yz)^2>0
\]
shows \(AB>\sqrt{2xyzC}\). Combining yields the strict bound
\[
Q^2>4A^2B^2C^2>8xyzC^3.
\]
Finally, \(\arctan s<s\) for every \(s>0\) gives
\[
\Omega^2<\frac{16x^2y^2z^2}{Q^2}
<\frac{2xyz}{C^3}=6\mu.
\]

For sharpness, set \(z=1\) and \(x=y=\varepsilon\downarrow0\). Directly from the formulas,
\[
A=\sqrt2\varepsilon,\quad B=C=\sqrt{1+\varepsilon^2},\quad
\tan\frac\Omega2=\frac{2\varepsilon}{\sqrt2(2+\varepsilon^2)+2\varepsilon\sqrt{1+\varepsilon^2}}.
\]
Thus \(\Omega\sim\sqrt2\varepsilon\) and \(\mu\sim\varepsilon^2/3\), yielding \(\Omega^2/\mu\to6\).

It remains to prove that these are the **only** asymptotically sharp degenerations. Write \(s=2xyz/Q>0\) and factor the normalized ratio exactly as
\[
\frac{\Omega^2}{6\mu}
=\left(\frac{\arctan s}{s}\right)^2
\left(\frac{2ABC}{Q}\right)^2
\left(\frac{2xyzC}{A^2B^2}\right).
\]
All three factors belong to \((0,1]\). If their product tends to \(1\), the third does, forcing
\[
\frac{x^4+(xC-yz)^2}{2xyzC}\longrightarrow0.
\]
Scale \(z=1\); now \(x\le y\le1\) and \(1\le C\le\sqrt2\). The term \(x^4/(2xyC)=x^3/(2yC)\ge x^3/(2\sqrt2)\) forces \(x\to0\). The other term equals \((r-1)^2/(2r)\) for \(r=xC/y\), so it forces \(r\to1\). Thus \(y\to0\), \(C\to1\), and \(x/y\to1\). Conversely these two limiting ratios imply \(A\sim\sqrt2y\), \(B\sim C\sim z\), \(Q\sim2\sqrt2yz^2\), \(s\to0\); all three factors tend to \(1\). This proves the equivalence.

## Verification

The standalone `verify.py` reconstructs the tetrahedron from actual vertex coordinates, checks its determinant normalization, evaluates the exact algebraic identity on rational coordinate samples, tests the analytic inequalities over an ordered integer grid, and tests convergence of the sharpness family. Run it with `python3 verify.py`; expected output is `DISPHENOID_SHARP_SOLID_ANGLE_CHECKS_OK`. These finite checks are regression checks only. The proof above establishes the universal inequalities and the complete limiting classification without enumeration or floating-point assumptions.

## Relationship to prior work

Martin W. Licht, *On solid angles and simplex shape measures*, arXiv:2610.05883v1 (first posted October 5, 2026), proves \(\Omega(T)^2/(12+3\pi)\le\mu(T)\) for **all** tetrahedra and exhibits a balanced sliver sequence showing that a universal coefficient must be at least \(6\). That source does **not** assert the coefficient \(6\) for the full equifacial class, nor classify every asymptotically sharp disphenoid sequence. The present theorem supplies both of those statements on that canonical class; it does not improve the established all-tetrahedron estimate.

Hidefumi Katsuura, *Angles of Isosceles Tetrahedra* (2021), establishes and characterizes equality of the four solid angles and maximization of the angle itself at the regular tetrahedron. Its full nine-page text does not give a diameter-normalized volume/solid-angle-square bound. Kabluchko--Schange's angle formulas treat **orthocentric** simplices; a nonregular generic disphenoid need not be orthocentric, and those formulas do not provide the sharp fullness inequality. The trihedral formula used above is the standard 1983 van Oosterom--Strackee identity.

## Limitations

No result is claimed for tetrahedra without congruent faces, no positive stability remainder away from the limiting family is proved, and the sharp constant is a nonattained supremum. Even a thorough literature comparison cannot exclude all unindexed earlier calculations of this precise invariant. The verification script does not certify infinitely many tetrahedra; all universal steps are in the mathematical argument.

## References

1. M. W. Licht, *On solid angles and simplex shape measures*, arXiv:2610.05883v1 (2026), https://arxiv.org/html/2610.05883v1, especially Theorem 4.1 and Example 4.3.
2. H. Katsuura, *Angles of Isosceles Tetrahedra*, Journal for Geometry and Graphics **25** (2021), 243--251, https://www.heldermann-verlag.de/jgg/jgg25/j25h2kat2.pdf.
3. A. van Oosterom and J. Strackee, *The solid angle of a plane triangle*, IEEE Transactions on Biomedical Engineering **30** (1983), 125--126, DOI:10.1109/TBME.1983.325207.
4. Z. Kabluchko and P. Schange, *Angles of orthocentric simplices*, arXiv:2505.05048v1 (2025), https://arxiv.org/html/2505.05048v1.
