# Cyclotomic descent and the characteristic-three jump for Rota–Baxter operators on a cyclic evolution algebra

## Finding

Let \(k\) be any field and let \(E=k e_1\oplus k e_2\) have products
\[
e_1^2=e_2,\qquad e_2^2=e_1,\qquad e_1e_2=0.
\]
This is a perfect, nonnilpotent evolution algebra. A weight-\(\lambda\) Rota–Baxter operator is a linear map \(R:E\to E\) satisfying
\[
R(x)R(y)=R\bigl(R(x)y+xR(y)+\lambda xy\bigr)\quad(x,y\in E).
\]
Write its matrix with columns \(R(e_1),R(e_2)\):
\[
[R]=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
\]
For nonzero \(\lambda\), set
\[
T(k)=\{t\in k:t^2-t+1=0,\ t+1\ne0\},\quad
\mu_3(k)=\{u\in k^\times:u^3=1\}.
\]
Then the **complete** set of weight-\(\lambda\) operators is the two scalar maps \(0,-\lambda I\) together with, for each \(t\in T(k)\), the diagonal map
\[
D_t=\operatorname{diag}(td,d),\qquad d=-\frac{\lambda}{1+t},
\]
and, for each \(t\in T(k),u\in\mu_3(k)\), the nondiagonal map
\[
N_{t,u}=\begin{pmatrix}td&(t-1)d\,u^2\\-(t-1)d\,u&d\end{pmatrix},\qquad d=-\frac{\lambda}{1+t}.
\]
If the characteristic is three, then \(T(k)\) is empty, and hence every nonzero-weight operator is \(0\) or \(-\lambda I\). Otherwise \(T(k)\) is empty unless the field contains a primitive cube root of unity; when it does, \(|T(k)|=2\), \(|\mu_3(k)|=3\), and there are exactly ten nonzero-weight operators. Thus there are exactly two or ten operators, never any other number, over every field.

For weight zero, the complete set is \(\{0\}\) if \(\operatorname{char} k\ne3\). **In characteristic three**, however, the weight-zero solutions form the union of two distinct linear spaces of dimension one:
\[
\left\{s\begin{pmatrix}1&0\\0&-1\end{pmatrix}:s\in k\right\}
\ \cup\
\left\{s\begin{pmatrix}1&-1\\1&-1\end{pmatrix}:s\in k\right\}.
\]
They meet only at the zero map. Consequently, for \(k=\mathbb F_q\), the number of weight-zero solutions is \(2q-1\) when \(q\) is a power of three and is one otherwise. For any nonzero weight over \(\mathbb F_q\), it is ten exactly when \(q\equiv1\pmod3\), and two otherwise.

The substantive new boundary is the **positive-characteristic arithmetic phase diagram**, particularly the two positive-dimensional weight-zero branches in characteristic three. The corresponding complex-field operators were already studied in 2019; this is not a first classification over \(\mathbb C\).

## Assumptions and scope

All fields are allowed, including characteristics two and three; no algebraic closure or perfectness of the field is assumed. Weight \(\lambda\) is an arbitrary scalar. A matrix is written using column convention, so the displayed parameters are unambiguous. Results classify actual \(k\)-linear maps, not automorphism orbits or an infinitesimal group scheme. The finite-field counts refer to distinct matrices without quotienting by automorphisms.

## Proof

**Step 1: equations.** Bilinearity makes it sufficient to test the Rota–Baxter identity on the three unordered pairs of natural basis elements. Their two coordinates give precisely
\[
\begin{aligned}
 c^2&=(2a+\lambda)b, &a^2&=(2a+\lambda)d,\\
 d^2&=(2d+\lambda)a, &b^2&=(2d+\lambda)c,\\
 cd&=ca+b^2, &ab&=c^2+bd.
\end{aligned}
\tag{1}
\]
Replacing \(b^2\) and \(c^2\) in the last two equations yields
\[
(a+d+\lambda)b=(a+d+\lambda)c=0.\tag{2}
\]
If one of \(b,c\) vanishes then the first or fourth equation in (1), using that a field has no nonzero square-zero elements, forces the other to vanish. Thus every solution is diagonal or has \(bc\ne0\).

**Step 2: diagonal operators.** Suppose \(b=c=0\). Equations (1) reduce to
\[
a^2=(2a+\lambda)d,\qquad d^2=(2d+\lambda)a.\tag{3}
\]
If either of \(a,d\) is zero, so is the other, giving the zero operator. Otherwise put \(t=a/d\). Eliminating \(\lambda\) from (3) gives
\[
(t-1)(t^2-t+1)=0.\tag{4}
\]
If \(t=1\), then (3) implies \(a=d=-\lambda\); for weight zero this contradicts nonzero \(a\), whereas for nonzero weight it gives \(-\lambda I\). If \(t^2-t+1=0\), equations (3) reduce to
\[
(t+1)d=-\lambda.\tag{5}
\]
When \(\lambda\ne0\), this is possible exactly for \(t\in T(k)\), with the displayed \(D_t\). When \(\lambda=0\) and \(d\ne0\), equation (5) requires \(t=-1\). Combining with the quadratic yields \(3=0\). In characteristic three \(t=-1\) indeed solves (4), and (3) is satisfied for any \(d\), giving the first line of weight-zero solutions after renaming \(s=-d\).

**Step 3: off-diagonal operators.** Suppose \(bc\ne0\). By (2), \(a+d+\lambda=0\). Write \(\delta=a-d\). The first and fourth equations in (1) simplify to
\[
c^2=\delta b,\qquad b^2=-\delta c.\tag{6}
\]
Necessarily \(\delta\ne0\). Setting \(u=-c/\delta\), equation (6) gives \(b=\delta u^2\) and \(u^3=1\), so \(u\in\mu_3(k)\). The remaining two square equations reduce to
\[
a^2=\delta d,\qquad d^2=-\delta a.\tag{7}
\]
Both \(a,d\) are nonzero (otherwise (7) forces both to vanish, contrary to \(\delta\ne0\)). Put \(t=a/d\); the first equation in (7) becomes \(t^2=t-1\), and the trace relation yields
\[
t^2-t+1=0,\qquad(t+1)d=-\lambda.\tag{8}
\]
For \(\lambda\ne0\) this yields exactly \(N_{t,u}\) with \(t\in T(k)\). Conversely substituting the displayed parameters into (1) proves every such matrix is a solution.

For \(\lambda=0\), equation (8) gives \(t=-1\) and characteristic three. Then \(a=-d\), \(\delta=2a=-a\), and \(\mu_3(k)=\{1\}\) because \(X^3-1=(X-1)^3\). Therefore \(b=-a,c=a,d=-a\), precisely the second line of weight-zero operators. Direct substitution into (1) verifies the line (including its zero member).

**Step 4: counting.** In characteristic three, \(t^2-t+1=(t+1)^2\), so \(T(k)=\varnothing\). Outside characteristic three, if \(t\in T(k)\), then \((-t)^3=1\) and \(-t\ne1\), giving a primitive cube root. Conversely, a nontrivial cube root \(\zeta\) produces \(t=-\zeta\in T(k)\). Since the polynomial has two distinct roots in this case, \(T(k)\) has exactly two elements; all three cube roots of unity then lie in \(k\). The ten nonzero-weight maps (two scalars, two diagonal, six off-diagonal) are pairwise distinct, since \(t=a/d\) and \(u=-c/(a-d)\) recover their non-scalar parameters. In characteristic three, the two weight-zero lines are distinct and intersect only at zero. For finite fields \(k^\times\) is cyclic of order \(q-1\), giving exactly the claimed congruence criterion and counts.

## Verification

The six polynomial equations were independently enumerated over \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_{11},\mathbb F_{13}\), and \(\mathbb F_4\). For each, the actual complete solution set was compared with the parametrized formulas for weights zero and one. All comparisons passed; the executable supplemental checker is `VERIFY.py`. The symbolic Steps 1–4, rather than finite enumeration, prove the all-field statement. For a nonzero arbitrary weight, scalar rescaling \(R\mapsto\lambda^{-1}R\) reduces to weight one.

## Relationship to prior work

Ladra and Murodov, *On chains and Rota-Baxter operators of evolution algebras* (2019), Section 3 and Theorem 3.3, already treat weight-zero and weight-one operators on every two-dimensional **complex** evolution algebra. Their class \(E_6(0)\) is this cyclic algebra. Therefore the complex specialization of the present theorem is **covered prior work**, not claimed as new. The 2019 result does not cover arbitrary positive characteristic or finite-field solution counts; in particular its characteristic-zero treatment cannot imply the two affine lines that appear for weight zero in characteristic three.

Qaralleh, Mukhamedov and Khakimov (January 2026) study maximal-nilindex **nilpotent** evolution algebras over characteristic-zero fields. Their structural upper-triangularity and recurrences do not apply to this perfect cyclic algebra. Their work and the October 2026 evolution-algebra survey motivate studying new characteristic and structural regimes for Rota–Baxter operators. The main mathematical distinction here is an exact characteristic-three jump coupled to cyclotomic descent for all nonzero weights.

## Limitations

This is a classification for one natural two-dimensional **perfect** evolution algebra, not for every two-dimensional evolution algebra and not for arbitrary nilpotent or higher-dimensional algebras. No scheme-theoretic assertions about nilpotent parameters are made. The complex specialization is known from earlier literature. Originality of the characteristic-three and finite-field arithmetic description is bounded by the inspected sources; an unindexed positive-characteristic treatment cannot be excluded. Finite-field checking is corroborative, not a proof over all fields. No independent external audit has been performed.

## References

1. M. Ladra and Sh. N. Murodov, *On chains and Rota-Baxter operators of evolution algebras*, arXiv:1906.09098v1, 2019; especially Section 3 and Theorem 3.3. https://arxiv.org/html/1906.09098v1
2. I. Qaralleh, F. Mukhamedov and O. Khakimov, *Rota-Baxter operators of nilpotent evolution algebras with maximal nilindex*, arXiv:2601.08669v1, first posted 2026-01-13. https://arxiv.org/html/2601.08669
3. *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1, 2026, particularly the discussion of Rota–Baxter classification. https://arxiv.org/abs/2610.22248
4. I. Qaralleh, F. Mukhamedov and O. Khakimov, *Local Rota-Baxter operators of weight zero on nilpotent evolution algebras with maximal nilindex*, arXiv:2606.22623, 2026. https://arxiv.org/abs/2606.22623
