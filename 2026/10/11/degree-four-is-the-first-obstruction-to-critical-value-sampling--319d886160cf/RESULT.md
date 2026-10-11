# Degree four is the first obstruction to critical-value sampling of polynomial root hulls

## Finding

For any complex polynomial \(p\) of degree \(d\ge2\), write
\[
K_c(p)=\operatorname{conv}\{z\in\mathbb C:p(z)+c=0\},\qquad
K'(p)=\operatorname{conv}\{z\in\mathbb C:p'(z)=0\}.
\]
Here \(\operatorname{conv}\) is the ordinary closed Euclidean convex hull, and repeated roots are counted only once in a hull. The *critical-value sampling hull* is the finite intersection
\[
H_{\mathrm{crit}}(p)=\bigcap_{\zeta:p'(\zeta)=0}K_{-p(\zeta)}(p).
\]
The intersection is over distinct critical points, equivalently distinct critical values (duplicate hulls do not matter).

**Sharp degree threshold.** Every complex polynomial of degree \(2\) or \(3\) satisfies
\[
H_{\mathrm{crit}}(p)=K'(p).
\]
The corresponding assertion fails already in degree \(4\). For the monic rational-coefficient quartic
\[
p_*(z)=z^4+\frac{32}{15}z^3+2z^2+\frac{32}{5}z
\]
the explicitly rational point
\[
w=\frac{2}{21}
\]
satisfies
\[
w\in H_{\mathrm{crit}}(p_*)\setminus K'(p_*).
\]
In particular, no theorem replacing arbitrary shifts by *only critical-value shifts* in the root-hull intersection can hold for all polynomial degrees.

## Assumptions and scope

There are no normalization, genericity, separability, or real-coefficient assumptions for the universal degree-\(2\) and degree-\(3\) assertion. The field is \(\mathbb C\), and all hulls are in its underlying real affine plane. For the degree-\(4\) obstruction, \(p_*\) is the specific polynomial above, not a claim about every quartic. This theorem does not rely on any identity involving intersections over all complex shifts.

## Proof

**Inclusion for all degrees.** The classical Gauss–Lucas theorem applied to \(p(z)+c\) gives \(K'(p)\subseteq K_c(p)\) for every \(c\in\mathbb C\), since differentiation removes the additive constant. Hence \(K'(p)\subseteq H_{\mathrm{crit}}(p)\).

**Quadratics.** Let \(p(z)=a(z-\zeta)^2+b\), where \(a\ne0\). Its unique critical point is \(\zeta\), and the critical-level fiber is the double root \(\zeta\):
\[
p(z)-p(\zeta)=a(z-\zeta)^2.
\]
Therefore both \(H_{\mathrm{crit}}(p)\) and \(K'(p)\) are the singleton \(\{\zeta\}\).

**Cubics with one distinct critical point.** If \(p'\) has a repeated zero \(b\), integration gives \(p(z)=a(z-b)^3+c\) with \(a\ne0\). Then the unique critical-level fiber has just the zero \(b\), so the same singleton identity holds.

**Cubics with distinct critical points.** Write the two critical points as \(b+u\) and \(b-u\), where \(u\in\mathbb C\setminus\{0\}\). Integration and absorption of the leading coefficient give
\[
p(b+t)=a(t^3-3u^2t)+c,\qquad a\ne0.
\]
At the two critical values, the exact factorizations are
\[
\begin{aligned}
p(b+t)-p(b+u)&=a(t-u)^2(t+2u),\\
p(b+t)-p(b-u)&=a(t+u)^2(t-2u).
\end{aligned}
\]
Their root hulls are therefore precisely the affine-line segments
\[
[b-2u,b+u]\quad\text{and}\quad[b-u,b+2u],
\]
where \([v_1,v_2]=\{(1-s)v_1+sv_2:0\le s\le1\}\). Since their coordinate intervals overlap exactly on \([-u,u]\) relative to \(b\),
\[
[b-2u,b+u]\cap[b-u,b+2u]=[b-u,b+u]=K'(p).
\]
This proves the universal statement through degree three.

**Quartic obstruction.** Set
\[
p_*(z)=z^4+\frac{32}{15}z^3+2z^2+\frac{32}{5}z.
\]
Direct differentiation gives the exact factorization
\[
p_*'(z)=4\left(z+\frac85\right)(z^2+1),
\]
so its distinct critical points are \(-8/5\), \(i\), and \(-i\). Their convex hull lies entirely in \(\{z:\operatorname{Re}z\le0\}\), whereas \(w=2/21>0\). Hence \(w\notin K'(p_*)\).

It remains to prove that \(w\) lies in all three critical-level root hulls. At \(-8/5\), exact division yields
\[
p_*(z)-p_*(-8/5)=\left(z+\frac85\right)^2
\left(z^2-\frac{16}{15}z+\frac{214}{75}\right).
\]
The last quadratic has roots
\[
r_{\pm}=\frac8{15}\pm i\frac{\sqrt{578}}{15},
\]
whose midpoint is \(8/15\). Thus the entire real segment \([-8/5,8/15]\) belongs to this fiber hull. In particular,
\[
\frac2{21}=\left(1-\frac{89}{112}\right)\left(-\frac85\right)
+\frac{89}{112}\cdot\frac8{15}
\in K_{-p_*(-8/5)}(p_*).
\]
At \(i\), exact division instead gives
\[
p_*(z)-p_*(i)=(z-i)^2
\left(z-\frac4{15}+\frac{9i}5\right)
\left(z+\frac{12}5+\frac{i}5\right).
\]
The roots include \(i\) and \(4/15-9i/5\), and the exact convex combination
\[
\frac2{21}=\frac9{14}i+\frac5{14}
\left(\frac4{15}-\frac{9i}5\right)
\]
shows \(w\in K_{-p_*(i)}(p_*)\). All coefficients of \(p_*\) are real, so complex conjugation gives the corresponding factorization at \(-i\). In particular,
\[
\frac2{21}=\frac9{14}(-i)+\frac5{14}
\left(\frac4{15}+\frac{9i}5\right)
\in K_{-p_*(-i)}(p_*).
\]
These are all critical points. Thus \(w\) lies in the intersection of their critical-value fiber hulls but outside the critical-point hull. Degree four is the first possible failure. \(\square\)

## Verification

The calculations above are exact. The bundled `checks/verify.py` reproduces the polynomial derivative factorization, the three shifted-fiber factorizations, and the two convex combinations with exact symbolic arithmetic. The checker establishes these finitely many identities; the all-cubic statement is proved symbolically for arbitrary \(b,u,a,c\), not inferred from samples. The human-readable proof also checks \(0<89/112<1\), \(0<5/14<1\), and \(\operatorname{Re}w>0\).

## Relationship to prior work

The classical Gauss–Lucas theorem supplies only the inclusion \(K'(p)\subseteq K_c(p)\). Teng Zhang's January 2026 preprint investigated the intersection of root hulls over *all* shifts and included a proposed full-shift equality (Theorem 1.2 of version 1). The February 2026 replacement **explicitly withdrew** that manuscript because Theorems 1.2 and 2.5 were incorrect and proofs contained gaps. No part of the withdrawn result is assumed or asserted here as established. The present finite critical-value sampling question is different: even a valid result about all shifts would not imply equality for a special finite subset. Zhang's version-1 Theorem 1.3 concerns equality at one fixed shift under multiplicity conditions; it does not address intersections over the finite set of critical values. Older quantitative and geometric Gauss–Lucas refinements address locations of critical points relative to original zeros, not this finite sampling identity. The present degree threshold and quartic witness follow by independent algebra.

## Limitations

The theorem does not establish, deny, or repair the proposed identity for intersections over all \(c\in\mathbb C\). It does not classify all quartics that exhibit the obstruction, the size of the excess intersection, or higher-degree behavior. No inference of publication priority follows from unsuccessful database searches; an unindexed equivalent may exist. The paper motivating the question was withdrawn, which is explicitly part of the provenance and is not concealed.

## References

1. Teng Zhang, *Intersections of Convex Hulls of Polynomial Shifts and Critical Points*, arXiv:2601.16102v1, first posted 2026-01-22. Version 2, 2026-02-25, explicitly withdraws the manuscript after identifying incorrect Theorems 1.2 and 2.5. https://arxiv.org/abs/2601.16102 and https://arxiv.org/html/2601.16102v1 .
2. Andreas Rüdinger, *Strengthening the Gauss-Lucas theorem for polynomials with Zeros in the interior of the convex hull*, arXiv:1405.0689 (2014). https://arxiv.org/abs/1405.0689 .
3. F. Lucas, *Théorèmes concernant les équations algébriques*, C. R. Acad. Sci. Paris 77 (1874), 431–433 (classical Gauss–Lucas result).
