# Constant equilateral perimeter in every regular \(4n\)-gonal norm

## Result

Let \(H_N=(\mathbb R^2,\|\cdot\|_N)\) be the normed plane whose unit sphere is the regular \(N\)-gon
\[
v_j=\bigl(\cos(2\pi j/N),\sin(2\pi j/N)\bigr),\qquad j\in\mathbb Z/N\mathbb Z.
\]
If \(4\mid N\), then every equilateral triangle in \(\mathcal T_3(H_N)\) has the same side length. Consequently
\[
L_3(H_N)=M_3(H_N).
\]

Thus the numerical conjectures in Alonso--Martín--Papini (2025) are true:
\[
L_3(H_{16})=M_3(H_{16}),\qquad L_3(H_{32})=M_3(H_{32}).
\]
More strongly, the equality holds for every regular polygonal norm with a number of sides divisible by four.

The subcases \(N=4\) and \(N=8\) were already proved in Alonso--Martín--Papini (2025). If \(12\mid N\), the regular \(N\)-gon is invariant under rotation by \(\pi/6\), so Alonso--Martín--Papini (2026), Theorem 20, already gives
\[
L_3(H_N)=M_3(H_N)=3\sqrt3.
\]
The new content is therefore the two infinite residue classes \(N\equiv4,8\pmod {12}\) beyond the previously known \(N=4,8\).

## Exact side lengths

Write \(\theta=2\pi/N\).

If \(N=12m+4\) with \(m\ge1\), put
\[
k=4m+1,\qquad
s=\frac{\sin((m+1)\theta)}{\sin(m\theta)},\qquad
\tau=\frac1{s+2}.
\]
Then every triangle in \(\mathcal T_3(H_N)\) has side length
\[
\lambda_N=
2\Bigl((1-\tau)\sin(k\theta)+\tau\sin((k+1)\theta)\Bigr).
\]

If \(N=12m+8\) with \(m\ge1\), put
\[
k=4m+2,\qquad
s=\frac{\sin(m\theta)}{\sin((m+1)\theta)},\qquad
\tau=\frac1{s+2}.
\]
Then every triangle in \(\mathcal T_3(H_N)\) has side length
\[
\lambda_N=
2\Bigl(\tau\sin(k\theta)+(1-\tau)\sin((k+1)\theta)\Bigr).
\]

Hence \(L_3(H_N)=M_3(H_N)=3\lambda_N\) in these cases. Numerically,
\[
3\lambda_{16}=5.205252779825\ldots,\qquad
3\lambda_{32}=5.195027526095\ldots,
\]
matching the 2025 approximate values \(5.2053\) and \(5.1950\).

## Proof

For \(a\in[0,1]\), write
\[
P_j(a)=(1-a)v_j+a v_{j+1},\qquad e_j=v_{j+1}-v_j,
\]
and let
\[
C_j=\operatorname{pos}\{v_j,v_{j+1}\}.
\]
If \(w=A v_j+Bv_{j+1}\in C_j\), with \(A,B\ge0\), then
\[
\|w\|_N=A+B.
\]
Thus the norm is linear on \(C_j\). In particular:

**Edge-cone lemma.** If an affine path \(w(t)\) remains in \(C_j\) and \(w'(t)\) is parallel to \(e_j\), then \(\|w(t)\|_N\) is constant.

We also use the elementary identity
\[
e_p-c e_q\parallel e_r
\quad\Longleftrightarrow\quad
c=\frac{\sin((r-p)\theta)}{\sin((r-q)\theta)}
\]
whenever the denominator is nonzero. It follows immediately by taking determinants with \(e_r\), since all edge vectors are rotations of one another.

By dihedral symmetry, it is enough to construct, for every
\[
x=P_0(t),\qquad 0\le t\le\frac12,
\]
an equilateral inscribed triangle whose side length is independent of \(t\). For every \(N>4\), the regular \(N\)-gon is not a parallelogram; by Theorem 2 and Proposition 7 of Alonso--Martín--Papini (2025), such an inscribed equilateral triangle lies in \(\mathcal T_3\), and the side length of a \(\mathcal T_3\)-triangle through a prescribed vertex \(x\) is uniquely determined by \(x\). Therefore a fixed-length construction through every boundary point proves the theorem.

### Case 1: \(N=12m+4\), \(m\ge1\)

Set
\[
q=\frac N4=3m+1,\qquad k=4m+1,\qquad
\alpha=m\theta,
\]
so that \(q\theta=\pi/2\) and \(N=3k+1\). Let
\[
s=\frac{\sin(\alpha+\theta)}{\sin\alpha}>1,\qquad
\tau=\frac1{s+2}.
\]

For \(0\le t\le\tau\), define
\[
\begin{aligned}
x&=P_0(t),\\
y&=P_k(\tau+s t),\\
z&=P_{N-k-1}(1-\tau+t).
\end{aligned}
\]
Put
\[
A=x-y,\qquad B=x-z,\qquad C=y-z.
\]
The edge-vector identity gives
\[
A'\parallel e_{N-m-1},\qquad
B'\parallel e_m,\qquad
C'\parallel e_q.
\]

We verify the corresponding cone memberships. At \(t=0\), \(y\) and \(z\) are reflections in the \(v_0\)-axis. For \(j=N-m-1\),
\[
\det(v_j,A)
=
[\sin(\alpha+\theta)-\sin\alpha]
+\tau[\sin\alpha-\sin(\alpha-\theta)]>0,
\]
and
\[
\det(A,v_{j+1})
=
(1-\tau)[\sin(\alpha+\theta)-\sin\alpha]>0.
\]
Hence \(A(0)\in C_j\), and reflection gives \(B(0)\in C_m\); also \(C(0)\) lies on the ray \(v_q\).

At \(t=\tau\), the relation \(\tau(1+s)=1-\tau\) gives
\[
y=P_k(1-\tau),\qquad z=v_{N-k}.
\]
Because \(N=3k+1\), \(x\) and \(y\) are reflections in the axis through \(v_{N-k}\). Thus \(A(\tau)\) lies on the ray \(v_{N-m}\). Directly,
\[
\det(v_m,B(\tau))
=
[\sin(\alpha+\theta)-\sin\alpha]
+\tau[\sin\alpha-\sin(\alpha-\theta)]>0,
\]
\[
\det(B(\tau),v_{m+1})
=
(1-\tau)[\sin(\alpha+\theta)-\sin\alpha]>0.
\]
So \(B(\tau)\in C_m\). Reflection in the \(v_{N-k}\)-axis sends \(B(\tau)\) into \(C_q\), hence \(C(\tau)\in C_q\).

Each of \(C_{N-m-1},C_m,C_q\) is convex. The paths \(A,B,C\) are affine, so the endpoint checks place the full paths in their stated cones. The edge-cone lemma shows that all three side norms are separately constant on \([0,\tau]\). At \(t=0\), reflection gives \(\|A\|=\|B\|\); at \(t=\tau\), the second reflection gives \(\|B\|=\|C\|\). Therefore all three constant values are equal.

For \(\tau\le t\le1/2\), continue with
\[
\begin{aligned}
x&=P_0(t),\\
y&=P_k\!\left(1-\tau+\frac{t-\tau}{s}\right),\\
z&=P_{N-k}\!\left(\frac{t-\tau}{s}\right).
\end{aligned}
\]
Now
\[
A'\parallel e_{N-m},\qquad
B'\parallel e_m,\qquad
C'\parallel e_q.
\]
At \(t=\tau\), the three difference vectors are already in
\[
C_{N-m},\qquad C_m,\qquad C_q,
\]
with \(A(\tau)\) on their relevant boundary ray \(v_{N-m}\).

At \(t=1/2\), the identity
\[
\frac{1/2-\tau}{s}=\frac{\tau}{2}
\]
implies that \(y\) and \(z\) are reflections in the symmetry axis through the midpoint of \(P_0([0,1])\). For \(j=N-m\),
\[
\det(v_j,A(1/2))
=
\frac{1-\tau}{2}
[\sin(\alpha+\theta)-\sin\alpha]>0,
\]
while
\[
\begin{aligned}
\det(A(1/2),v_{j+1})
&=
\frac12\bigl(2\sin(\alpha+\theta)-\sin(\alpha-\theta)-\sin\alpha\bigr)\\
&\quad+\frac{\tau}{2}
[\sin(\alpha+2\theta)-\sin(\alpha+\theta)]>0.
\end{aligned}
\]
Thus \(A(1/2)\in C_{N-m}\); reflection gives \(B(1/2)\in C_m\), and \(C(1/2)\) points along the normal to that symmetry axis, which lies in \(C_q\). Convexity again keeps all three affine paths in the stated cones, so the edge-cone lemma preserves the common side length through \(t=1/2\).

### Case 2: \(N=12m+8\), \(m\ge1\)

Set
\[
q=\frac N4=3m+2,\qquad k=4m+2,\qquad
\alpha=m\theta,
\]
so that \(q\theta=\pi/2\) and \(N=3k+2\). Let
\[
s=\frac{\sin\alpha}{\sin(\alpha+\theta)}<1,\qquad
\tau=\frac1{s+2}.
\]

For \(0\le t\le\tau\), set
\[
\begin{aligned}
x&=P_0(t),\\
y&=P_k(1-\tau+t),\\
z&=P_{N-k-1}(\tau+s t).
\end{aligned}
\]
Again let \(A=x-y\), \(B=x-z\), \(C=y-z\). Then
\[
A'\parallel e_{N-m-1},\qquad
B'\parallel e_m,\qquad
C'\parallel e_q.
\]

At \(t=0\), \(y\) and \(z\) are reflections in the \(v_0\)-axis. For \(j=N-m-1\),
\[
\det(v_j,A(0))
=
(1-\tau)[\sin(\alpha+\theta)-\sin\alpha]>0,
\]
\[
\det(A(0),v_{j+1})
=
[\sin(\alpha+\theta)-\sin\alpha]
+\tau[\sin(\alpha+2\theta)-\sin(\alpha+\theta)]>0.
\]
Thus \(A(0)\in C_j\), reflection gives \(B(0)\in C_m\), and \(C(0)\) lies on the ray \(v_q\).

At \(t=\tau\), \(y=v_{k+1}\), and because \(N=3k+2\), \(x\) and \(z\) are reflections in the axis through \(v_{k+1}\). Also
\[
\det(v_j,A(\tau))
=
[\sin(\alpha+\theta)-\sin\alpha]
+\tau[\sin(\alpha+2\theta)-\sin(\alpha+\theta)]>0,
\]
\[
\det(A(\tau),v_{j+1})
=
(1-\tau)[\sin(\alpha+\theta)-\sin\alpha]>0.
\]
Hence \(A(\tau)\in C_j\). The vector \(B(\tau)\) lies on the ray \(v_{m+1}\), hence belongs to \(C_m\); the same reflection places \(C(\tau)\) in \(C_q\). The edge-cone lemma therefore makes all three side norms constant on \([0,\tau]\). The two endpoint reflections give \(\|A\|=\|B\|\) at \(0\) and \(\|A\|=\|C\|\) at \(\tau\), so the three constants are equal.

For \(\tau\le t\le1/2\), set
\[
\begin{aligned}
x&=P_0(t),\\
y&=P_{k+1}\!\left(\frac{t-\tau}{s}\right),\\
z&=P_{N-k-1}\!\left(1-\tau+\frac{t-\tau}{s}\right).
\end{aligned}
\]
Then
\[
A'\parallel e_{N-m-1},\qquad
B'\parallel e_{m+1},\qquad
C'\parallel e_q.
\]
At \(t=\tau\), the vectors lie respectively in
\[
C_{N-m-1},\qquad C_{m+1},\qquad C_q,
\]
with \(B(\tau)\) on the common boundary ray \(v_{m+1}\).

At \(t=1/2\), again \((1/2-\tau)/s=\tau/2\), so \(y,z\) are reflected across the edge-midpoint axis. For \(j=N-m-1\),
\[
\begin{aligned}
\det(v_j,A(1/2))
&=
\frac12[\sin(\alpha+\theta)-\sin\alpha]
+\frac12[\sin(\alpha+2\theta)-\sin\alpha]\\
&\quad+\frac{\tau}{2}[\sin\alpha-\sin(\alpha-\theta)]>0,
\end{aligned}
\]
and
\[
\det(A(1/2),v_{j+1})
=
\frac{1-\tau}{2}
[\sin(\alpha+\theta)-\sin\alpha]>0.
\]
Thus \(A(1/2)\in C_{N-m-1}\); reflection gives \(B(1/2)\in C_{m+1}\), while \(C(1/2)\in C_q\). The edge-cone lemma preserves the common side length on the second interval.

In both residue classes, all sine inequalities used above are strict because
\[
0\le\alpha-\theta<\alpha<\alpha+\theta<\alpha+2\theta<\frac{\pi}{2}
\]
for \(m\ge1\).

Dihedral symmetry covers the whole unit sphere. Proposition 7 of Alonso--Martín--Papini (2025) now implies that every \(\mathcal T_3\)-triangle through each boundary point has the constructed side length. Hence all triangles in \(\mathcal T_3(H_N)\) have one common side length.

Finally, at \(t=0\), \(y\) and \(z\) are reflections in the horizontal axis and \(v_q=(0,1)\). Therefore \(\|y-z\|_N\) is just the vertical coefficient of \(y-z\), which gives the two displayed formulas for \(\lambda_N\). \(\square\)

## Verification

The accompanying script evaluates the regular-polygon gauge directly and samples the two explicit constructions. It checks the equality of all three side norms and their constancy for representative values from both residue classes, including \(N=16\) and \(N=32\). This numerical check is supplementary; the theorem is established by the analytic proof above.

## Context and literature

Fabińska and Lassak (2004) studied large equilateral triangles in Minkowski unit disks, part of the older literature on equilateral configurations in normed planes.

Alonso, Martín and Papini (2025) introduced the perimeter parameters used here, proved the equality \(L_3=M_3\) for \(H_4\) and \(H_8\), and reported approximate computations suggesting the same equality for \(H_{16}\) and \(H_{32}\). Their Problem 1 asks about the condition \(L_3=M_3\).

Alonso, Martín and Papini (2026), Theorem 20, proved \(L_3=M_3=3\sqrt3\) whenever the unit sphere is invariant under rotations by \(\pi/6\). For regular \(4n\)-gons this covers exactly the subfamily whose number of sides is divisible by \(12\), but it does not cover \(H_{16}\), \(H_{20}\), \(H_{28}\), \(H_{32}\), and the other \(N\equiv4,8\pmod{12}\) cases.

## Limitations

The literature search found no exact or stronger theorem covering the two new regular-polygon residue classes, but originality is necessarily to the best of current knowledge. The proof concerns regular polygonal unit spheres; it does not characterize all normed planes satisfying \(L_3=M_3\), and the broader characterization questions remain open.

## References

1. E. Fabińska and M. Lassak, *Large equilateral triangles inscribed in the unit disk of a Minkowski plane*, Beiträge Algebra Geom. 45 (2004), 517–525. https://eudml.org/doc/233407
2. J. Alonso and P. Martín, *Moving triangles over a sphere*, Math. Nachr. 279 (2006), 1735–1738. https://doi.org/10.1002/mana.200510450
3. J. Alonso, P. Martín and P. L. Papini, *Perimeter of Triangles Inscribed in the Unit Ball of Normed Planes*, Mediterr. J. Math. 22, 46 (2025). https://doi.org/10.1007/s00009-025-02805-6
4. J. Alonso, P. Martín and P. L. Papini, *Wheeling around Chebyshev centers and Jung constant in normed planes*, Rend. Circ. Mat. Palermo (2) 75, 131 (2026). https://doi.org/10.1007/s12215-026-01436-4
