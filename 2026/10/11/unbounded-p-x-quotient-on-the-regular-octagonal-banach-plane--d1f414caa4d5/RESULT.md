# Unbounded \(P(X)\) quotient on the regular octagonal Banach plane
## Finding
Let \(X_8=(\mathbb R^2,N)\) be the real regular-octagonal Banach plane with
\[
N(s,t)=\max\!\left\{|s|,|t|,\frac{|s|+|t|}{\sqrt2}\right\}.
\]
For the quantity \(P(X)\) introduced by Zhou, Ni, Liu, and Li,
\[
P(X)=\sup_{x\not\perp_P y}
\frac{\|x\|^2+\|y\|^2-\|x+y\|^2}
{\|x\|^2+\|y\|^2-\|x-y\|^2},
\]
the defining supremum is unbounded above on \(X_8\). Consequently \(P(X_8)\) has no finite value; if the supremum is interpreted in the extended reals, then
\[
P(X_8)=+\infty.
\]

## Assumptions and scope
All scalars are real. Pythagorean orthogonality is the relation
\[
x\perp_P y
\quad\Longleftrightarrow\quad
\|x-y\|^2=\|x\|^2+\|y\|^2.
\]
Thus every pair used below with nonzero denominator is admissible in the displayed supremum. The statement concerns the definition of \(P(X)\) in the cited 2023 paper and the particular regular-octagonal norm above; it does not assert unboundedness for every non-Hilbert space.

## Proof
Write \(r=\sqrt2\) and fix
\[
x=(1,r-1),\qquad y_t=(-t/6,t),\qquad 0<t<12/35.
\]
First, \(N(x)=1\). Also
\[
N(y_t)=t,
\]
because \(7/(6r)<1\).

The inequality \(12/35<r-1\) follows from \(47/35<r\), whose square is \(2209/1225<2\). Hence both coordinates of \(x-y_t\) are positive. On the whole indicated interval,
\[
x-y_t=(1+t/6,r-1-t),
\]
and its first-coordinate support dominates the other supports, so
\[
N(x-y_t)=1+t/6.
\]
Indeed, the diagonal support is \(1-5t/(6r)<1\), whereas the first coordinate is larger than \(1\).

Similarly,
\[
x+y_t=(1-t/6,r-1+t).
\]
The diagonal support is
\[
1+\frac{5t}{6r}>1.
\]
It dominates the first coordinate, which is smaller than \(1\), and it also dominates the second coordinate: since \(r<3/2\) and \(t<1/2\), one has \(r-1+t<1\). Therefore
\[
N(x+y_t)=1+\frac{5t}{6r}.
\]

The denominator in the definition of \(P(X_8)\) is therefore
\[
1+t^2-\left(1+\frac t6\right)^2
=\frac{t(35t-12)}{36}<0,
\]
so \(x\not\perp_P y_t\) for every \(0<t<12/35\). The numerator is
\[
1+t^2-\left(1+\frac{5t}{6r}\right)^2
=\frac{t(47t-60r)}{72}<0.
\]
Consequently the admissible quotient is exactly
\[
R(t)=\frac{47t-60r}{2(35t-12)}.
\]
As \(t\uparrow12/35\), the denominator tends to \(0\) from below while the numerator tends to the strictly negative number \(564/35-60r\). Hence
\[
R(t)\longrightarrow+\infty,
\]
which proves that the supremum is unbounded above.

At the limiting value \(t=12/35\), the pair becomes Pythagorean-orthogonal because
\[
N(x-y_t)=37/35,
\qquad
1+t^2=(37/35)^2,
\]
while the other parallelogram defect remains nonzero. The blow-up is therefore caused by approaching an excluded zero of the denominator from the side on which numerator and denominator have the same sign.

## Verification
The proof uses only exact arithmetic in \(\mathbb Q(\sqrt2)\) and explicit identification of the active supports of the octagonal norm. The critical identities are
\[
1+t^2-N(x-y_t)^2=\frac{t(35t-12)}{36}
\]
and
\[
1+t^2-N(x+y_t)^2=\frac{t(47t-60\sqrt2)}{72}.
\]
Substitution of any increasing sequence \(t_n<12/35\) with \(t_n\to12/35\) gives admissible finite quotients tending to \(+\infty\). No finite enumeration or numerical limiting argument is used as a proof.

## Relationship to prior work
The defining paper introduces \(P(X)\) from the parallelogram law and Pythagorean orthogonality and, for this exact regular-octagonal norm, records only the lower estimate
\[
P(X_8)\ge \frac1{5-4\sqrt2}.
\]
The same paper also proves general lower estimates such as \(P(X)\ge-1\) and \(P(X)\ge1-C_{\mathrm{NJ}}(X)\); none of these bounds controls the denominator near Pythagorean-orthogonal pairs. The explicit one-parameter family above shows that, on the paper's own octagonal benchmark, the quotient is in fact unbounded above.

Targeted statement-level searches for this definition, its DOI, the regular-octagon example, Pythagorean orthogonality, and unboundedness did not locate a published statement giving this blow-up. The closest indexed regular-octagon results compute different invariants, including parameterized von Neumann--Jordan, angle-modulus, \(T_G\), and equilateral-triangle constants; those statements neither imply nor dominate the present denominator-singularity result.

## Limitations
The result is a boundary statement about the displayed definition. It does not alter definitions of other orthogonality constants, and it does not classify the Banach spaces on which \(P(X)\) is finite. Bibliographic searches cannot exclude an obscure or poorly indexed independent observation. The proof establishes unboundedness, not an attained infinite value.

## References
1. Yin Zhou, Qichuan Ni, Qi Liu, and Yongjin Li, “Geometric constants and orthogonality in Banach spaces,” Contributions to Mathematics 8 (2023), 38–47, DOI: 10.47443/cm.2023.045. Published online 11 September 2023; primary MSC 46B20.
2. Yin Zhou, Qichuan Ni, and Qi Liu, “The skew constant and orthogonalities in Banach spaces,” Open Journal of Mathematical Sciences 8 (2024), DOI: 10.30538/oms2024.0219.
