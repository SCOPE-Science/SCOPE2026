# Five minimal-rank fibers and two disjoint Hasse strata in a characteristic-seven genus-four family

## Finding

Let \(k=\overline{\mathbb F}_7\). For \((a,b)\in k^2\), consider the smooth projective model
\[
C_{a,b}:\qquad y^2=x^{10}+x^7+ax^4+bx.
\]
Put
\[
\begin{aligned}
\Delta&=3a^3+a^2-3ab+b^2+3b,\\
L&=a^3-ab+3b^2,\\
R&=3a(a+1)-b,\\
S&=ab^2+(a+1)^7.
\end{aligned}
\]
Exactly the parameters in \(U=\{(a,b):b\Delta\ne0\}\) give smooth genus-four curves. For **every geometric point** of \(U\), with \(a(C)\) the Jacobian \(a\)-number and \(f_7(C)\) its \(7\)-rank,
\[
\boxed{
(a(C_{a,b}),f_7(C_{a,b}))=
\begin{cases}
(0,4),&LR\ne0,\\
(1,3),&L=0,\\
(2,2),&R=0,\ S\ne0,\\
(2,1),&R=0,\ S=0.
\end{cases}}
\]
The conditions are exhaustive and disjoint on \(U\). In particular no smooth member has \(7\)-rank zero, and the **minimal rank one occurs at exactly five coefficient-marked geometric parameters**. They are
\[
(a,b)=(2,4),\quad (3,1),\quad
\left(\alpha,3\alpha(\alpha+1)\right)
\quad\text{for }\alpha^3+3\alpha^2-1=0.
\]
The cubic is irreducible over \(\mathbb F_7\), so the five points form Frobenius orbits of lengths \(1,1,3\). Hence the number of marked rank-one parameters over \(\mathbb F_{7^m}\) is exactly \(2+3\mathbf 1_{3\mid m}\), for every integer \(m\ge1\).

The nonordinary Hasse divisor on \(U\) is the **nonreduced** divisor \(V(L)+2V(R)\); its two reduced, individually smooth components do not meet in \(U\). The projective closure of \(V(L)\) is an irreducible nodal cubic, while \(V(R)\) is a parabola. All geometric intersections of the two affine components lie on the singular-fiber boundary, with contact order two at each of two points.

## Assumptions and scope

All polynomial equalities and factorizations are in characteristic \(7\), and all geometric counts are over the algebraic closure. The coefficients \((a,b)\) are **marked parameters**; distinct parameters are not claimed to define geometrically nonisomorphic curves. The curves have an automorphism of order six; their order-three quotient is the elliptic curve
\[
E_{a,b}:\quad Y^2=X(X^3+X^2+aX+b).
\]
No assertion is made concerning characteristic other than seven or smooth curves outside this coefficient-normalized family.

## Proof

**1. Smoothness and genus.** Writing \(f(x)=xg(x^3)\), where \(g(z)=z^3+z^2+az+b\), shows that \(f\) has ten distinct roots exactly when \(b\ne0\) and \(g\) is separable: the characteristic is prime to three, and \(g(0)=b\). The discriminant of \(g\), reduced modulo seven, is \(\Delta\) as displayed. A separable polynomial of degree ten defines a smooth hyperelliptic curve of genus four.

**2. Cartier matrix and the Hasse divisor.** The standard basis of regular differentials is \(\omega_j=x^{j-1}dx/y\), for \(1\le j\le4\). If \(c_n\) denotes the coefficient of \(x^n\) in \(f(x)^3\), Cartier's action is the inverse-Frobenius-semilinear map whose matrix has entries \(c_{7i-j}^{1/7}\). The coefficient matrix before extracting seventh roots is
\[
H=\begin{pmatrix}
3ab^2&0&0&b^3\\
0&L&0&0\\
0&0&R&0\\
3&0&0&3a+3
\end{pmatrix}.
\]
The \((1,4)\)-block has determinant \(3b^2R\), so
\[
\det H=3b^2LR^2.
\]
The scalar \(L\) is also the elliptic quotient's Hasse invariant: it is the coefficient of \(X^6\) in \(\bigl(X(X^3+X^2+aX+b)\bigr)^3\).

**3. The two Hasse components do not meet on smooth curves.** On \(R=0\), substitute \(b=3a(a+1)\). Direct polynomial reduction gives
\[
L=-a^2(a+2)^2,\qquad \Delta=2a(a+2)^3.
\]
The simultaneous zeros of \(L\) and \(R\) have \(a=0\) or \(a=-2\). The former has \(b=0\), and the latter has \(\Delta=0\). Thus \(V(L)\cap V(R)\cap U=\varnothing\). Along \(R=0\) within \(U\), \(b\ne0\), the \((1,4)\)-block has rank one and \(L\ne0\); on \(L=0\) within \(U\), this block is invertible and \(R\ne0\). The matrix ranks are respectively two and three, giving the stated \(a\)-numbers. Away from both components \(H\) is invertible.

**4. Semilinear stable rank.** In the ordered \((1,4)\)-coordinates, on \(R=0\) write
\[
B=uv^{\mathsf T},\qquad
u=\begin{pmatrix}3ab^2\\3\end{pmatrix},\quad
v=\begin{pmatrix}1\\a+1\end{pmatrix}.
\]
The notation \(H^{[7]}\) means entrywise seventh powers. The square of the Cartier operator, after an entrywise \(49\)-th power, has matrix \(H^{[7]}H\). On this rank-one block,
\[
B^{[7]}B=u^{[7]}(v^{[7]\mathsf T}u)v^{\mathsf T},\qquad
v^{[7]\mathsf T}u=3\bigl(ab^2+(a+1)^7\bigr)=3S.
\]
Thus this block's stable Cartier rank is zero precisely when \(S=0\), and one otherwise: if \(S\ne0\), Cartier acts invertibly on the one-dimensional image, so no later iterate loses rank. On \(R=0\cap U\), the nonzero scalar \(L\) contributes stable rank one, whereas the scalar \(R\) is zero. On \(L=0\cap U\), the two-dimensional block and scalar \(R\) are invertible, contributing stable rank three. Everywhere else all four dimensions survive. The stable Cartier rank equals the Jacobian \(7\)-rank. This proves the classification for **every** algebraically closed-field parameter, without extrapolating from finite fields.

**5. Exactly five rank-one points.** Substituting the equation of \(R=0\) into the semilinear scalar gives the exact identity
\[
S\bigl(a,3a(a+1)\bigr)
=(a-2)(a-3)(a+1)^2(a^3+3a^2-1).
\]
The double root \(a=-1\) has \(b=0\) and is excluded. The other five roots are distinct and smooth because the restriction of \(b\Delta\) to \(R=0\) vanishes only at \(a=0,-1,-2\), none of which is a root of the displayed remaining factors. The cubic \(a^3+3a^2-1\) has no root in \(\mathbb F_7\), hence is irreducible and separable of degree three. The two linear roots have \((a,b)=(2,4),(3,1)\). Frobenius-orbit and extension-field counts follow.

**6. Geometry of the divisor.** The cubic \(L=0\) is irreducible over \(k\): regarding \(L\) as quadratic in \(b\), its discriminant is \(a^2(1+2a)\), not a square in \(k(a)\). Its projective closure has a unique singularity at \((a,b)=(0,0)\), with distinct tangent lines \(b=0\) and \(3b-a=0\); the single point at infinity is smooth. The parabola \(R=0\) is smooth. The restriction \(L|_{R=0}=-a^2(a+2)^2\) shows the intersection multiplicity is two at each of the two affine boundary intersections. Finally, \(\det H=3b^2LR^2\) and \(b\ne0\) on \(U\) give the claimed divisor multiplicities.

## Verification

The exact arithmetic programs shipped with this result are independent implementations:

```
python3 verify_symbolic.py
python3 verify_fields.py
```

The first expands \(f^3\) symbolically in characteristic seven, reconstructs the complete Cartier coefficient matrix, verifies the discriminant, determinant, elliptic quotient invariant, boundary intersections, semilinear scalar, and factorization, and enumerates the prime-field marked parameters. It requires SymPy. The second uses only Python's standard library and recomputes \(f^3\), Cartier iterates, and ranks in finite fields via independent polynomial-residue arithmetic. It checks every smooth marked parameter over \(\mathbb F_7\) and \(\mathbb F_{49}\), and the five deep points over \(\mathbb F_{343}\). Its observed distributions \((a\text{-number},7\text{-rank}):\text{count}\) were
\[
\begin{array}{c|rrrr}
& (0,4)&(1,3)&(2,2)&(2,1)\\\hline
\mathbb F_7&29&4&2&2\\
\mathbb F_{49}&2213&46&44&2
\end{array}
\]
These finite checks corroborate the polynomial proof; they do not establish geometric exhaustiveness on their own.

## Relationship to prior work

Kudo--Nakagawa--Takagi (2022 preprint; corrected 2023 journal article) introduced precisely this genus-four order-six family and its elliptic quotient and provided an efficient superspeciality-enumeration algorithm. Their stated results concern superspecial curves, the support pattern of Cartier matrices, automorphism groups, and computation, not the complete characteristic-seven \(a\)-number and stable-rank loci above. The coefficient-matrix method is classical (Yui), and a general nonexistence theorem for superspecial genus-four curves in characteristic seven was already established by Kudo--Harashita; neither is claimed as new. The new assertion is the **full geometric marked-parameter stratification**, the double Hasse component, and the five rank-one fibers with their Frobenius orbits. The formula distinguishes stable Cartier rank from first-iterate rank, which is essential for locating the rank-one points.

## Limitations

The result classifies marked coefficients, not isomorphism classes. It does not determine Newton polygons, Ekedahl--Oort types beyond the displayed invariants, or ranks in other characteristics. Existing indexed literature and accessible historical claims were compared, but an uncatalogued prior equivalent specialization cannot be absolutely excluded. No independent external audit was performed.

## References

1. M. Kudo, T. Nakagawa, T. Takagi, *Efficient search for superspecial hyperelliptic curves of genus four with automorphism group containing* \(\mathbb Z_6\), arXiv:2210.14822 (first publicly posted 26 October 2022); *Mathematics in Computer Science* 17 (2023), Article 21. https://arxiv.org/abs/2210.14822 ; https://doi.org/10.1007/s11786-023-00571-w
2. M. Kudo, S. Harashita, *Superspecial curves of genus 4 in small characteristic*, arXiv:1607.01114 (2016); *Finite Fields and Their Applications* 45 (2017), 131--169. https://arxiv.org/abs/1607.01114
3. N. Yui, *On the Jacobian varieties of hyperelliptic curves over fields of characteristic* \(p>2\), *Journal of Algebra* 52 (1978), 378--410. https://doi.org/10.1016/0021-8693(78)90247-8
4. A. Elkin, *The rank of the Cartier operator on cyclic covers of the projective line*, arXiv:0708.0431; *Journal of Algebra* 327 (2011), 1--12. https://arxiv.org/abs/0708.0431

5. M. Kudo, T. Nakagawa, T. Takagi, *Correction to: Efficient Search for Superspecial Hyperelliptic Curves of Genus Four with Automorphism Group Containing* \(\mathbb Z_6\), *Mathematics in Computer Science* 17 (2023), Article 23. https://doi.org/10.1007/s11786-023-00573-8
