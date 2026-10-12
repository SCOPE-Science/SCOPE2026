# Rota–Baxter moduli of the affine two-dimensional Lie triple system

## Finding

Let \(K\) be a field and let
\[
\mathfrak a_K=Ke_1\oplus Ke_2
\]
be the two-dimensional affine Lie algebra
\[
[e_1,e_2]=e_2.
\]
Its associated Lie triple system is
\[
L_K=(\mathfrak a_K,[\, ,\, ,\,]),
\qquad
[x,y,z]=[[x,y],z].
\]
In the chosen basis the only nonzero basic triple products are
\[
[e_1,e_2,e_1]=-e_2,
\qquad
[e_2,e_1,e_1]=e_2.
\]

A weight-zero Rota–Baxter operator on a Lie triple system satisfies
\[
[R(x),R(y),R(z)]
=
R\!\left(
[R(x),R(y),z]
+[R(x),y,R(z)]
+[x,R(y),R(z)]
\right).
\]

Write
\[
R=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix},
\]
with columns \(R(e_1)\) and \(R(e_2)\). The complete basis-triple system is
\[
\boxed{
b(a^2+2ad-bc)=0,
}
\]
\[
\boxed{
b(bc+d^2)=0,
}
\]
\[
\boxed{
b^2(a+d)=0,
}
\]
and
\[
\boxed{
abc+2ad^2-bcd=0.
}
\]

Assume
\[
\operatorname{char}K\ne2.
\]
Then every Rota–Baxter operator lies in exactly one of the following disjoint pieces:
\[
\boxed{
\mathcal A=
\left\{
\begin{pmatrix}
0&0\\
c&d
\end{pmatrix}
:c,d\in K
\right\},
}
\]
\[
\boxed{
\mathcal B\setminus\mathcal A=
\left\{
\begin{pmatrix}
a&0\\
c&0
\end{pmatrix}
:a\in K^\times,\ c\in K
\right\},
}
\]
and
\[
\boxed{
\mathcal C=
\left\{
\begin{pmatrix}
a&b\\
-a^2/b&-a
\end{pmatrix}
:a\in K,\ b\in K^\times
\right\}.
}
\]
Here
\[
\mathcal B=
\left\{
\begin{pmatrix}
a&0\\
c&0
\end{pmatrix}
:a,c\in K
\right\}
\]
meets \(\mathcal A\) in the line
\[
\mathcal A\cap\mathcal B
=
\left\{
\begin{pmatrix}
0&0\\
c&0
\end{pmatrix}
:c\in K
\right\}.
\]

For every odd prime power \(q\),
\[
\boxed{
|\operatorname{RB}_0(L_{\mathbf F_q})|
=
3q^2-2q.
}
\]

The exact rank distribution is
\[
\boxed{
\#\{\operatorname{rank}R=0\}=1,
\qquad
\#\{\operatorname{rank}R=1\}=3q^2-2q-1,
\qquad
\#\{\operatorname{rank}R=2\}=0.
}
\]
Thus no nonzero weight-zero Rota–Baxter operator on this Lie triple system is invertible.

The full automorphism group is
\[
\boxed{
\operatorname{Aut}(L_K)
=
\left\{
\begin{pmatrix}
\varepsilon&0\\
r&s
\end{pmatrix}
:
\varepsilon\in\{1,-1\},\ r\in K,\ s\in K^\times
\right\}.
}
\]

Over \(\mathbf F_q\) with \(q\) odd, the \(3q^2-2q\) operators form exactly
\[
\boxed{2q+1}
\]
automorphism-conjugacy classes. Their orbit-size distribution is
\[
\boxed{
1\text{ orbit of size }1,
}
\]
\[
\boxed{
1\text{ orbit of size }q-1,
}
\]
\[
\boxed{
2(q-1)\text{ orbits of size }q,
}
\]
and
\[
\boxed{
1\text{ orbit of size }q(q-1).
}
\]

There is also a structural separation from the binary Lie-algebra problem. The weight-zero Rota–Baxter operators on the affine Lie algebra itself are precisely
\[
\boxed{\mathcal B\cup\mathcal C.}
\]
Consequently
\[
\boxed{\mathcal A\setminus\mathcal B}
\]
consists of genuinely ternary-only Rota–Baxter operators: they satisfy the Lie triple system identity but do not come from a Rota–Baxter operator on the inducing Lie algebra.

Finally, over every extension field,
\[
|\operatorname{RB}_0(L_{\mathbf F_q})(\mathbf F_{q^m})|
=
3q^{2m}-2q^m,
\]
so the Hasse–Weil zeta function of the operator variety is
\[
\boxed{
Z(T)=\frac{(1-qT)^2}{(1-q^2T)^3}.
}
\]

## Assumptions and scope

Chen, Lou, and Sun developed the cohomology theory of Rota–Baxter Lie triple systems. A later open treatment of Reynolds Lie triple systems records explicitly that weight \(0\) is the usual Rota–Baxter identity and that a Lie algebra with ternary bracket
\[
[x,y,z]=[[x,y],z]
\]
is a Lie triple system.

The later treatment also records the sufficient passage from a Rota–Baxter or Reynolds Lie algebra to the associated Lie triple system. The theorem above shows that, for the affine two-dimensional example, this passage is not surjective on weight-zero Rota–Baxter operators.

The classification and orbit formulas in this result assume
\[
\operatorname{char}K\ne2.
\]
The finite-field statements therefore concern odd prime powers.

No claim is made here about characteristic \(2\).

## Proof

For vectors
\[
x=x_1e_1+x_2e_2,
\qquad
y=y_1e_1+y_2e_2,
\]
the affine Lie bracket is
\[
[x,y]=(x_1y_2-x_2y_1)e_2.
\]
Hence
\[
[x,y,z]
=
-(x_1y_2-x_2y_1)z_1e_2.
\]

Substitution of
\[
R(e_1)=ae_1+ce_2,
\qquad
R(e_2)=be_1+de_2
\]
into the weight-zero ternary Rota–Baxter identity on all eight ordered basis triples gives, after removing repeated signs, exactly
\[
b(a^2+2ad-bc)=0,
\]
\[
b(bc+d^2)=0,
\]
\[
b^2(a+d)=0,
\]
and
\[
abc+2ad^2-bcd=0.
\]

Suppose first that
\[
b=0.
\]
The last equation becomes
\[
2ad^2=0.
\]
Since \(2\) is invertible and \(K\) is a field,
\[
a=0
\qquad\text{or}\qquad
d=0.
\]
These are exactly the planes \(\mathcal A\) and \(\mathcal B\).

Suppose now that
\[
b\ne0.
\]
The third equation gives
\[
d=-a.
\]
The second then gives
\[
bc=-a^2,
\]
so
\[
c=-a^2/b.
\]
The first and fourth equations are then automatic. This is exactly \(\mathcal C\).

Over \(\mathbf F_q\),
\[
|\mathcal A\cup\mathcal B|
=
q^2+q^2-q
=
2q^2-q,
\]
and
\[
|\mathcal C|=q(q-1).
\]
The pieces are disjoint after replacing \(\mathcal B\) by \(\mathcal B\setminus\mathcal A\), hence
\[
|\operatorname{RB}_0(L_{\mathbf F_q})|
=
3q^2-2q.
\]

Every nonzero matrix in \(\mathcal A\cup\mathcal B\) has one zero column or one-dimensional image, hence rank \(1\). For
\[
R\in\mathcal C,
\]
\[
\det R
=
-a^2-b(-a^2/b)
=
0,
\]
while \(b\ne0\), so again the rank is \(1\). This proves the rank profile.

For automorphisms, let
\[
P=
\begin{pmatrix}
p&u\\
r&s
\end{pmatrix}.
\]
Preservation of all basic triple products gives
\[
u=0,
\qquad
s(p^2-1)=0.
\]
Invertibility forces \(p,s\ne0\), and therefore
\[
p^2=1.
\]
When the characteristic is not \(2\),
\[
p=\varepsilon\in\{1,-1\},
\]
which gives the displayed automorphism group.

For
\[
P=
\begin{pmatrix}
\varepsilon&0\\
r&s
\end{pmatrix},
\]
direct multiplication yields
\[
PRP^{-1}
=
\begin{pmatrix}
a-br/s&b\varepsilon/s\\
\bigl(-r(br+ds)+s(ar+cs)\bigr)/(\varepsilon s)&d+br/s
\end{pmatrix}.
\]

On the locus \(b=0\), the pair \((a,d)\) is invariant. The zero operator is fixed. On the common line
\[
a=d=0,
\]
all nonzero \(c\)'s form one orbit, of size \(q-1\). For each fixed nonzero \(d\) in \(\mathcal A\), the parameter \(r\) acts transitively on \(c\), giving one orbit of size \(q\). Likewise, for each fixed nonzero \(a\) in \(\mathcal B\), all \(c\)'s form one orbit of size \(q\). This gives
\[
2(q-1)
\]
orbits of size \(q\).

On \(\mathcal C\), one may choose \(r\) so that the transformed upper-left entry is \(0\), and then choose \(s/\varepsilon\) to normalize the nonzero upper-right entry. Thus all of \(\mathcal C\) is one orbit. Its size is
\[
q(q-1).
\]
The orbit count is therefore
\[
1+1+2(q-1)+1
=
2q+1.
\]

For comparison, the binary weight-zero Rota–Baxter identity on the inducing affine Lie algebra reduces to
\[
b(a+d)=0,
\qquad
bc+d^2=0.
\]
Its solutions are exactly \(\mathcal B\cup\mathcal C\). Hence the extra plane
\[
\mathcal A\setminus\mathcal B
\]
is a genuine failure of the converse to the usual Lie-algebra-to-Lie-triple-system construction.

Replacing \(q\) by \(q^m\) in the point count gives
\[
N_m=3q^{2m}-2q^m.
\]
Therefore
\[
\begin{aligned}
Z(T)
&=
\exp\!\left(
\sum_{m\ge1}\frac{N_mT^m}{m}
\right)\\
&=
\frac{(1-qT)^2}{(1-q^2T)^3}.
\end{aligned}
\]

## Verification

The included program `artifacts/verify.py` reconstructs the ternary bracket from the affine Lie bracket and then reconstructs the Rota–Baxter defect on all ordered basis triples.

It symbolically verifies the four polynomial equations used in the proof, derives the automorphism equations, and checks the conjugation formulas.

It independently reconstructs the binary affine-Lie Rota–Baxter equations and verifies that their solution set is exactly
\[
\mathcal B\cup\mathcal C.
\]

Finally, it exhaustively enumerates all \(2\times2\) operators over
\[
\mathbf F_3,\qquad
\mathbf F_5,\qquad
\mathbf F_7.
\]
The total counts are
\[
21,\qquad65,\qquad133,
\]
equal to
\[
3q^2-2q.
\]
The rank profiles are respectively
\[
(1,20,0),\qquad
(1,64,0),\qquad
(1,132,0).
\]
The automorphism-class counts are
\[
7,\qquad11,\qquad15,
\]
with exactly the stated orbit-size distributions.

The checker returns `VERIFY_OK`.

Finite enumeration is a replay check. The arbitrary odd-prime-power formulas are proved by the field-level argument above.

## Relationship to prior work

Chen, Lou, and Sun study representations, cohomology, deformations, and extensions of Rota–Baxter Lie triple systems. Their publisher record gives no low-dimensional classification in its abstract or metadata. Full article text was not available through the accessible public route during this check, so a hidden same-object example inside that article remains a specific residual comparison risk.

Mu and Guo later give the weight-\(\lambda\) Reynolds identity explicitly. They state that weight \(0\) is the usual Rota–Baxter identity, recall the Lie-algebra construction
\[
[x,y,z]=[[x,y],z],
\]
and record that a Reynolds Lie algebra produces a Reynolds Lie triple system. Their explicit two-dimensional example uses the different ternary product
\[
[e_1,e_2,e_2]=e_1,
\]
and therefore does not cover the affine-induced system classified here.

Targeted literature searches for the affine-induced ternary product, two-dimensional Rota–Baxter Lie triple systems, finite-field counts, automorphism conjugacy, and the polynomial
\[
3q^2-2q
\]
did not locate a covering result.

## Limitations

The classification and automorphism quotient are restricted to characteristic different from \(2\).

The full text of the 2023 primary paper was not available through the accessible public route, and institutional retrieval required interactive authorization unavailable during this check. This is retained as an explicit originality risk.

A specialized or differently indexed classification may exist. Failed searches do not prove novelty.

## References

1. S. Chen, Q. Lou, and Q. Sun, “Cohomologies of Rota-Baxter Lie triple systems and applications,” *Communications in Algebra* 51 (2023), 4299–4315, DOI `10.1080/00927872.2023.2205938`, first published online 3 May 2023.
2. Y. Mu and S. Guo, “Cohomology of Reynolds Lie Triple Systems and Applications,” *Axioms* 15 (2026), 616, DOI `10.3390/axioms15080616`.
