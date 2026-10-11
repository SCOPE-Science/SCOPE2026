# Only endpoint parameters preserve Carathéodory positivity for all convex maps

## Finding

Let \(\mathcal K\) be the normalized univalent holomorphic functions on \(\mathbb D\) with convex image. For the \(\alpha\)-Carathéodory component \(h_\alpha[g]\) defined below, the exact set of parameters for which **every** convex function has strictly positive component real part is
\[
\big\{\alpha\in[0,1]:\operatorname{Re}h_\alpha[g](z)>0\quad\forall g\in\mathcal K,\ \forall z\in\mathbb D\big\}=\{0,1\}.
\]
More sharply, one fixed map
\[
f(z)=\sqrt{\frac{1+z}{1-z}}-1
\]
satisfies
\[
\inf_{z\in\mathbb D}\operatorname{Re}h_\alpha[f](z)=-\infty
\qquad\text{for every }0<\alpha<1.
\]
The square root is the principal holomorphic branch on the right half-plane.

## Assumptions and scope

For \(g\in\mathcal K\) write
\[
A_g(z)=\frac{zg'(z)}{g(z)},\qquad P_g(z)=1+\frac{zg''(z)}{g'(z)},
\]
with the removable value at the origin. The definition used here, exactly as in Grigoriciuc (2026), is
\[
h_\alpha[g](z)=
\frac{\alpha(1-\alpha)A_g(z)^2+(2\alpha^2-\alpha)A_g(z)+(1-\alpha)(\alpha+P_g(z))}
{P_g(z)(1-\alpha+\alpha A_g(z))},\qquad0\le\alpha\le1.
\]
This is a pointwise statement on the open disk. The unbounded-below assertion uses interior points approaching the circle; it is not an assertion that any interior pole exists. Positivity at the endpoints means strictly positive at every interior point, not a positive uniform infimum.

## Proof

**Convexity and normalization.** The Cayley map \(w=(1+z)/(1-z)\) maps \(\mathbb D\) conformally onto \(\operatorname{Re}w>0\). Its principal square root \(t=\sqrt w\) maps onto the open convex sector \(|\arg t|<\pi/4\). Translation by \(-1\) preserves convexity and univalence, while \(f(0)=0\) and \(f'(0)=1\). Thus \(f\in\mathcal K\).

**Exact reduction.** Express \(A_f,P_f\) as functions of \(w\) (with \(t=\sqrt w\)):
\[
A(w)=\frac{(1+w)(1+t)}{4t},\qquad
P(w)=\frac{1+3w^2}{4w}.
\]
These follow by differentiating \(f=t-1\) and using \(dw/dz=(1+w)^2/2\). Put
\[
D_\alpha(w)=1-\alpha+\alpha A(w),\qquad
C_\alpha(w)=\frac{\alpha\big[(1-\alpha)(A(w)^2+1)+(2\alpha-1)A(w)\big]}{D_\alpha(w)}.
\]
A rearrangement of the defining numerator gives the meromorphic identity
\[
h_\alpha[f](z(w))=\frac{1-\alpha}{D_\alpha(w)}+\frac{C_\alpha(w)}{P(w)},\quad z(w)=\frac{w-1}{w+1}.
\]
The apparent singularities of this representation at the chosen boundary point are legitimate for the indicated analytic continuation. There are no denominator zeros inside the disk: convexity implies \(\operatorname{Re}P>0\), and every normalized convex map is starlike, so \(\operatorname{Re}A>0\); hence \(\operatorname{Re}D_\alpha>0\) for \(0\le\alpha\le1\).

**The decisive residue sign.** Set
\[
w_0=\frac{i}{\sqrt3},\qquad
q=\frac{1}{\sqrt{2\sqrt3}},\qquad
A(w_0)=u+iv.
\]
Since \(\sqrt{w_0}=q(1+i)\), direct expansion yields
\[
u=\frac14\left(1+\frac{1+1/\sqrt3}{2q}\right),\qquad
v=\frac{2q+1-\sqrt3}{8q\sqrt3}.
\]
Elementary inequalities \(\frac12<q<\frac35\) and \(\frac32<1+1/\sqrt3\) show \(u>9/16>1/2\). Moreover \(2q>1>\sqrt3-1\) gives \(v>0\). In particular \(D_\alpha(w_0)\ne0\) throughout \(0\le\alpha\le1\). Writing \(a=\alpha\), multiplying numerator and denominator by the conjugate of \(D_\alpha\) yields the exact identity
\[
\operatorname{Im}C_a(w_0)=
\frac{a(1-a)v\big[a((u-1)^2+v^2)+2u-1\big]}
{(1-a+au)^2+a^2v^2}.
\]
For each \(0<a<1\), every factor needed for the strict inequality is positive; therefore \(\operatorname{Im}C_a(w_0)>0\).

**Boundary approach and interior divergence.** On \(w=iy\) for \(0<y<1/\sqrt3\),
\[
P(iy)=i\,p(y),\qquad p(y)=\frac{3y^2-1}{4y}<0,
\quad p(y)\longrightarrow0^-
\quad(y\uparrow1/\sqrt3).
\]
Near \(w_0\) the first term \((1-a)/D_a(iy)\) remains bounded; the second satisfies
\[
\operatorname{Re}\frac{C_a(iy)}{P(iy)}
=\frac{\operatorname{Im}C_a(iy)}{p(y)}\longrightarrow-\infty,
\]
by continuity and the strict positivity established at \(w_0\). The points \(w=iy\) themselves lie on the boundary of the right half-plane. For every negative threshold, choose \(y<1/\sqrt3\) so close to the critical value that the real part of this boundary continuation is below the threshold; then choose sufficiently small \(x>0\). Continuity of the formula at \(w=x+iy\), with \(\operatorname{Re}w>0\), maintains the inequality. The corresponding \(z(w)\) belongs to \(\mathbb D\). As the threshold is arbitrary, \(\inf_{\mathbb D}\operatorname{Re}h_a[f]=-\infty\).

**Endpoints.** For every \(g\in\mathcal K\), direct substitution gives \(h_0[g]\equiv1\) and \(h_1[g]=1/P_g\). Convexity gives \(\operatorname{Re}P_g>0\) on \(\mathbb D\), hence \(\operatorname{Re}(1/P_g)>0\). Combining this with the interior-parameter obstruction proves the stated exact set.

## Verification

The independently readable `verify_pole.py` checks the Cayley and square-root normalization, the derivative formulas, the decomposition of the component, the algebraic formula for the imaginary residue, and sufficiently negative interior values near the boundary for a range of representative parameters. The infinite-parameter quantifier and the divergence are established by the preceding analytic inequalities, not by finite tests. To reproduce, run `python3 verify_pole.py` using only the Python standard library.

## Relationship to prior work

Grigoriciuc (2026, Definition 1, Conjectures 1–3, Remarks 3 and 5) defines this particular component and records positivity at the two endpoints, while positing positivity for all parameters. The present result settles the exact parameter set and strengthens a mere single-parameter sign violation to an unbounded-below obstruction at every interior parameter, using one fixed convex function. The related 2026 work on convex combinations of Graham–Kohr operators studies higher-dimensional extension behavior, not the pointwise scalar \(h_\alpha\) classification; its extension conclusions do not by themselves establish this theorem.

## Limitations

The result concerns the defined \(h_\alpha\) and the normalized convex class on the disk, with \(\alpha\in[0,1]\). It does not establish failure or success of any particular higher-dimensional extension statement, nor an optimal bound for restricted subclasses. The pole is on the boundary, and no pole is asserted inside the disk. An unindexed equivalent argument may exist; originality is judged against inspected sources rather than certified exhaustiveness. No independent audit has been performed.

## References

1. E. Ş. Grigoriciuc, *A conjecture related to convex functions on the unit disc: numerical approach and extension results*, Journal of Analysis **34** (2026), 2013–2037, DOI: 10.1007/s41478-026-01067-z; first published April 20, 2026. In particular Definition 1, Conjectures 1–3 and Remarks 3–5.
2. E. Ş. Grigoriciuc, *Convex Combinations of Graham-Kohr Type Extension Operators*, Complex Analysis and Operator Theory **20** (2026), article 90, DOI: 10.1007/s11785-026-01945-1; first published April 8, 2026. In particular Section 1 and Remark 4.
