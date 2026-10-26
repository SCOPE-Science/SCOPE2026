# Three-stratum Poisson-bracket classification on the characteristic-two truncated plane

## Finding
Let \(k\) be **any field of characteristic two**, and let
\[
A=k[x,y]/(x^2,y^2).
\]
Consider unital Poisson algebra structures whose commutative associative multiplication is the fixed multiplication of \(A\); isomorphisms are unital \(k\)-algebra automorphisms preserving the Poisson bracket. Every Poisson bracket is uniquely determined by
\[
\{x,y\}=a+bx+cy+dxy \qquad(a,b,c,d\in k).
\]
Exactly **three pairwise disjoint families** exhaust its isomorphism classes:
\[
\begin{array}{ll}
\mathrm{I}_d:&\{x,y\}=1+dxy,\\
\mathrm{II}_d:&\{x,y\}=x+dxy,\\
\mathrm{III}_d:&\{x,y\}=dxy,
\end{array}
\qquad d\in k.
\]
Two normal forms in this display are isomorphic **if and only if** they belong to the same family and have the same parameter \(d\). This gives a complete classification over arbitrary (including infinite) characteristic-two fields.

In particular, for \(k=\mathbb F_q\) with \(q=2^e\), the number of brackets on this fixed associative algebra is \(q^4\), distributed into **exactly \(3q\) isomorphism classes**. At each \(d\), the three orbit sizes and the corresponding Poisson automorphism-group orders are, respectively,
\[
\begin{array}{c|c|c}
\text{type}&\text{orbit size}&|\operatorname{Aut}_{\rm Pois}|\\ \hline
\mathrm{I}_d&(q-1)q^2&q(q^2-1)\\
\mathrm{II}_d&q^2-1&q^3(q-1)\\
\mathrm{III}_d&1&q^2(q^2-1)(q^2-q).
\end{array}
\]
The type-III brackets are fixed by every associative algebra automorphism; this is a statement about coordinate changes, not that all distinct \(d\) are isomorphic.

## Assumptions and scope
The Poisson bracket is \(k\)-bilinear, alternating, satisfies Jacobi, and is a derivation in each variable. We do not assume a restricted Poisson structure or any extra \(p\)-operation. The characteristic is exactly two; all field extensions of \(\mathbb F_2\), finite or infinite, are permitted. The associative algebra has the basis \(1,x,y,xy\), with \(x^2=y^2=0\). The classification fixes that associative algebra, not the entire class of four-dimensional commutative algebras.

## Proof
**1. All brackets arise from one arbitrary element.** The derivations \(\partial_x\) and \(\partial_y\) on \(k[x,y]\) descend to \(A\), since \(\partial_x(x^2)=2x=0\) and \(\partial_y(y^2)=2y=0\). For every \(F\in A\), define
\[
\{U,V\}_F=F\bigl((\partial_x U)(\partial_y V)+(\partial_y U)(\partial_x V)\bigr).
\]
This is well-defined, bilinear, alternating, and a biderivation. Its Jacobiator is a derivation in each of its three entries (the usual cancellation using alternation and the Leibniz rule). It vanishes on triples drawn from \(1,x,y\), because triples with repeated entries cancel and \(\{1,-\}=0\). Hence Jacobi holds on all of \(A\). Conversely, Leibniz and \(\{1,-\}=0\) force any Poisson bracket to have exactly this form, with \(F=\{x,y\}\). Thus there are precisely four free scalar coefficients.

**2. All associative automorphisms.** The unique maximal ideal is \(\mathfrak m=(x,y)\), with \(\mathfrak m^2=kxy\). An automorphism necessarily has the form
\[
\phi(x)=ux+vy+sxy=:X,\qquad
\phi(y)=wx+zy+txy=:Y,
\]
where \(u,v,w,z,s,t\in k\) and \(\Delta=uz+vw\ne0\). Conversely every such assignment is an automorphism: \(X^2=Y^2=0\) in characteristic two, and its induced map on \(\mathfrak m/\mathfrak m^2\) is invertible.

**3. The top-degree coefficient is an exact isomorphism invariant.** Set
\[
P=ut+ws,\qquad Q=vt+zs,\qquad B=bu+cw,\qquad C=bv+cz.
\]
Direct differentiation gives
\[
J=\partial_xX\,\partial_yY+\partial_yX\,\partial_xY
=\Delta+Px+Qy.
\]
The bracket associated with \(F'=\{x,y\}'\) makes \(\phi:(A,\{-,-\}_F)\to(A,\{-,-\}_{F'})\) a Poisson isomorphism exactly when \(J F'=\phi(F)\). Since \(J\) has invertible constant term and \((Px+Qy)^2=0\),
\[
J^{-1}=\Delta^{-1}\bigl(1+\Delta^{-1}Px+\Delta^{-1}Qy\bigr).
\]
Writing \(F=a+bx+cy+dxy\), expansion gives
\[
\begin{split}
a'&=a/\Delta,\\
b'&=B/\Delta+aP/\Delta^2,\\
c'&=C/\Delta+aQ/\Delta^2,\\
d'&=d+(bs+ct)/\Delta+(BQ+CP)/\Delta^2.
\end{split}
\]
The elementary identity
\[
BQ+CP=\Delta(bs+ct)
\]
shows **\(d'=d\)** for every automorphism. Moreover \(a=0\) is invariant, and when \(a=0\) the property \((b,c)=(0,0)\) is invariant because \((B,C)=(b,c)\left(\begin{smallmatrix}u&v\\w&z\end{smallmatrix}\right)\) and \(\Delta\ne0\).

**4. Completeness of the three normal forms.** If \(a\ne0\), choose a linear part with \(\Delta=a\). The map from \((s,t)\) to \((P,Q)\) is invertible, as its matrix determinant is \(\Delta\). Thus unique \(s,t\) can make \(b'=c'=0\), giving \(F'=1+dxy\). If \(a=0\) and \((b,c)\ne(0,0)\), choose the linear-part matrix
\[
\begin{pmatrix}u&c\\w&b\end{pmatrix}
\]
with \(ub+cw\ne0\), and choose \(s=t=0\). Then \(\Delta=ub+cw=B\), \(C=bc+cb=0\), so \(F'=x+dxy\). If \(a=b=c=0\), the bracket already has the form \(dxy\). The invariant \(d\) and the invariant three-way distinction prove uniqueness.

**5. Finite-field census.** Over \(\mathbb F_q\), the associative automorphism group has order \(|\mathrm{GL}_2(\mathbb F_q)|q^2=(q^2-1)(q^2-q)q^2\). With \(d\) fixed, the three strata have respectively \((q-1)q^2\), \(q^2-1\), and \(1\) elements, because \(a\) is nonzero/zero and \((b,c)\) is free/nonzero/zero in the respective strata. Step 4 shows each is one orbit. Orbit-stabilizer yields the displayed automorphism orders. The disjoint strata have total \((q-1)q^2+(q^2-1)+1=q^3\) elements at each \(d\), accounting for all \(q^4\) brackets.

## Verification
The standalone `verify.py` implements finite-field arithmetic for \(\mathbb F_2\) and \(\mathbb F_4\) and the quotient algebra directly from its basis multiplication. It checks alternation and Jacobi for **every** coefficient quadruple by evaluating on every basis triple, enumerates **every** associative automorphism, and independently applies each coordinate change by explicitly differentiating \(X,Y\) and inverting its Jacobian in the quotient ring. It computes and compares complete normal-form orbits, including disjointness, sizes, and coverage. Command: `python3 verify.py`. Observed output:

```
char2_GF_2: PASS, all 16 brackets satisfy Jacobi; 24 automorphisms; 6 disjoint exact isomorphism orbits
char2_GF_4: PASS, all 256 brackets satisfy Jacobi; 2880 automorphisms; 12 disjoint exact isomorphism orbits
VERIFY_OK
```

This finite enumeration is a consistency check, not a substitute for the arbitrary-field proof in the preceding section.

## Relationship to prior work
Petrov and Pypka's 2026 arbitrary-field Poisson classification treats dimensions at most three and identifies additional characteristic-two behavior; the fixed unital algebra \(A\) considered here has dimension four. Abdelwahab and Sánchez (2025) classify *complex* four-dimensional Poisson algebras, and Abdelwahab, Barreiro, Calderón, and Fernández Ouaridi (2023) classify nilpotent Poisson algebras in small dimensions under characteristic restrictions different from two. These do not give characteristic-two isomorphism classes for the fixed \(A\). Launois and Richard (2009) study Poisson cohomology on complex truncated polynomial algebras, starting from the specific bracket \(\{x,y\}=xy\); that bracket is an acknowledged special instance of the third family, not the new classification. The present contribution is the complete three-stratum modular orbit classification, its invariant top coefficient and exact finite-field orbit/stabilizer counts.

## Limitations
The result does not classify all four-dimensional Poisson algebras or Poisson group schemes, and no priority claim is made beyond the inspected sources. Earlier unindexed work on modular Poisson structures or equivalent descriptions using a two-generator exterior algebra may exist. It does not cover restricted Poisson operations or deformations of the associative multiplication. A self-review is not independent validation.

## References
1. A. V. Petrov and O. O. Pypka, *On the Structure of Low-Dimensional Poisson Algebras over Arbitrary Fields*, arXiv:2609.13784v1 (first public 2026-09-12), https://arxiv.org/html/2609.13784v1.
2. H. Abdelwahab and J. M. Sánchez, *Classification of Four-Dimensional Complex Poisson Algebras*, Axioms **14** (2025), article 804, https://doi.org/10.3390/axioms14110804.
3. S. Launois and L. Richard, *Poisson (co)homology of truncated polynomial algebras in two variables*, C. R. Math. **347** (2009), 133–138, https://doi.org/10.1016/j.crma.2008.12.005.
4. H. Abdelwahab, E. Barreiro, A. J. Calderón, and A. Fernández Ouaridi, *The algebraic classification and degenerations of nilpotent Poisson algebras*, J. Algebra **615** (2023), 243–277, https://doi.org/10.1016/j.jalgebra.2022.10.018.
