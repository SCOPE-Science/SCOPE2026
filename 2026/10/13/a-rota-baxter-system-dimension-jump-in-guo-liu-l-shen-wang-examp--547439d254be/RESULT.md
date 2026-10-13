# A Rota–Baxter-system dimension jump in Guo–Liu–Lü–Shen–Wang Example 1

## Finding

Let \(K\) be a field, let \(a\in K^\times\), and let \(b\in K\). Consider the two-dimensional BiHom-associative algebra from Example 1 of Guo, Liu, Lü, Shen, and Wang, with basis \(\{e_1,e_2\}\), multiplication
\[
e_1e_1=e_1,
\]
\[
e_1e_2=be_1+(1-a)e_2,
\]
\[
e_2e_1=\frac{b(1-a)}a e_1+ae_2,
\qquad
e_2e_2=\frac ba e_2,
\]
and structure maps
\[
\alpha(e_1)=e_1,
\qquad
\alpha(e_2)=\frac{b(1-a)}a e_1+ae_2,
\]
\[
\beta(e_1)=e_1,
\qquad
\beta(e_2)=be_1+(1-a)e_2.
\]

A Rota–Baxter system is a pair of linear maps \((R,S)\) commuting with \(\alpha\) and \(\beta\) and satisfying
\[
R(x)R(y)=R\bigl(R(x)y+xS(y)\bigr),
\]
\[
S(x)S(y)=S\bigl(R(x)y+xS(y)\bigr)
\]
for all \(x,y\in A\).

Every such pair has the unique form
\[
R=
\begin{pmatrix}
r&\frac ba(r-t)\\
0&t
\end{pmatrix},
\qquad
S=
\begin{pmatrix}
s&\frac ba(s-v)\\
0&v
\end{pmatrix}.
\]

If \(a\ne1\), the complete system locus is exactly six affine lines through the origin:
\[
(u,0,0,0),
\quad
(u,0,0,-u),
\quad
(u,u,0,0),
\]
\[
(0,0,u,0),
\quad
(0,0,u,u),
\quad
(0,-u,u,0),
\qquad u\in K,
\]
where each quadruple records \((r,t,s,v)\).

If \(a=1\), the locus jumps to
\[
\boxed{
\{(r,0,0,v):r,v\in K\}
\cup
\{(0,0,s,v):s,v\in K\}
\cup
\{(u,u,0,0):u\in K\}
\cup
\{(0,-u,u,0):u\in K\}.
}
\]
Thus two affine planes replace four of the generic lines. The parameter \(b\) does not affect the resulting geometry.

Over every finite field \(\mathbf F_q\),
\[
\boxed{|\operatorname{RBS}_{a\ne1}(\mathbf F_q)|=6q-5}
\]
and
\[
\boxed{|\operatorname{RBS}_{a=1}(\mathbf F_q)|=2q^2+q-2}.
\]
The extension-field counts are obtained by replacing \(q\) with \(q^m\), so the reduced zeta functions are
\[
\boxed{Z_{a\ne1}(T)=\frac{(1-T)^5}{(1-qT)^6}}
\]
and
\[
\boxed{Z_{a=1}(T)=\frac{(1-T)^2}{(1-qT)(1-q^2T)^2}}.
\]

## Assumptions and scope

The source works over an arbitrary base field and requires only \(a\ne0\) in Example 1. Its primary Mathematics Subject Classification code is \(17D30\). The article was first publicly published on 6 September 2022.

The result here classifies all Rota–Baxter systems on the exact two-dimensional BiHom-associative family used in that example. It does not classify arbitrary two-dimensional BiHom-associative algebras.

No characteristic restriction is needed beyond the source assumption \(a\ne0\).

## Proof

Write
\[
R=\begin{pmatrix}r_{11}&r_{12}\\r_{21}&r_{22}\end{pmatrix}.
\]
The condition \(R\beta=\beta R\) gives
\[
r_{21}=0,
\qquad
ar_{12}=b(r_{11}-r_{22}).
\]
The same equations follow from simultaneous commutation with the two structure maps. Thus, with \(r=r_{11}\) and \(t=r_{22}\),
\[
R=
\begin{pmatrix}
r&\frac ba(r-t)\\0&t
\end{pmatrix}.
\]
The same argument gives
\[
S=
\begin{pmatrix}
s&\frac ba(s-v)\\0&v
\end{pmatrix}.
\]

Substitute these forms into the two Rota–Baxter-system identities and evaluate on the four ordered basis pairs. Among the resulting scalar equations are
\[
rs=0,
\qquad
tv=0,
\qquad
t(r-s-t)=0.
\]
The remaining independent condition is
\[
(a-1)v(r-s+v)=0.
\]
All other basis defects vanish once these conditions hold.

Suppose first that \(a\ne1\). Then
\[
rs=0,
\qquad
tv=0,
\qquad
t(r-s-t)=0,
\qquad
v(r-s+v)=0.
\]
If \(t=v=0\), the equation \(rs=0\) gives the two coordinate lines
\[
(u,0,0,0),
\qquad
(0,0,u,0).
\]
If \(t=0\) and \(v\ne0\), then \(r-s+v=0\). Together with \(rs=0\), this gives either \(s=0,r=-v\) or \(r=0,s=v\), yielding the lines
\[
(u,0,0,-u),
\qquad
(0,0,u,u).
\]
If \(t\ne0\), then \(v=0\) and \(r-s=t\). Again \(rs=0\), so either \(s=0,r=t\) or \(r=0,s=-t\), yielding
\[
(u,u,0,0),
\qquad
(0,-u,u,0).
\]
These six lines are distinct and meet only at the origin.

Now suppose \(a=1\). The last scalar condition disappears. If \(t=0\), the sole condition involving \(r,s,v\) is \(rs=0\), giving the two planes
\[
\{(r,0,0,v)\},
\qquad
\{(0,0,s,v)\},
\]
which meet in the \(v\)-axis. If \(t\ne0\), then \(v=0\) and the same two one-dimensional branches as above remain:
\[
(u,u,0,0),
\qquad
(0,-u,u,0).
\]
Each additional line meets the plane union only at the origin.

For a finite field with \(q\) elements, six lines through one common point give
\[
1+6(q-1)=6q-5.
\]
At \(a=1\), the two planes contribute \(2q^2-q\), and the two extra lines contribute another \(2(q-1)\), giving
\[
2q^2+q-2.
\]
Replacing \(q\) by \(q^m\) gives the extension-field counts and the stated zeta functions.

## Verification

The bundled checker reconstructs the multiplication and both structure maps symbolically. It derives the simultaneous commutation form for \(R\) and \(S\), reconstructs all basis-pair Rota–Baxter defects, and verifies the two reduced systems of scalar equations.

It then performs direct finite-field enumeration for every \(b\) and every nonzero \(a\) over
\[
\mathbf F_2,
\quad
\mathbf F_3,
\quad
\mathbf F_5,
\quad
\mathbf F_7.
\]
For each parameter pair, the direct Rota–Baxter identities agree exactly with the displayed geometric classification. The checker returns `VERIFY_OK`.

Finite enumeration is replay evidence. The arbitrary-field classification is the symbolic case analysis above.

## Relationship to prior work

Guo, Liu, Lü, Shen, and Wang introduce BiHom Rota–Baxter systems, give the present two-dimensional BiHom-associative family as Example 1, construct one explicit nontrivial Rota–Baxter system on it, and use that system to build a two-dimensional BiHom-dendriform algebra in Example 3. The paper presents concrete examples rather than a complete system locus for Example 1.

Brzeziński introduced Rota–Baxter systems in the associative setting, while Das developed their Hom-associative analogue. Those works provide general constructions and structural theory, not the complete parameter geometry for this BiHom example.

Focused searches for a complete two-dimensional BiHom-associative Rota–Baxter-system classification, the six-line locus, the \(a=1\) dimension jump, and the finite-field polynomials did not locate a covering statement.

## Limitations

The theorem concerns one parameterized two-dimensional BiHom-associative family.

The zeta functions count the reduced solution varieties, not isomorphism classes under BiHom-algebra automorphisms.

Failed searches do not prove absolute historical novelty.

## References

1. Q. Guo, L. Liu, J. Lü, B. Shen, and X. Wang, “Rota-Baxter Systems for BiHom-Type Algebras,” *Mathematics* 10 (2022), 3222, DOI `10.3390/math10183222`.
2. T. Brzeziński, “Rota-Baxter systems, dendriform algebras and covariant bialgebras,” *Journal of Algebra* 460 (2016), 1–25, arXiv `1503.05073`.
3. A. Das, “Rota-Baxter systems on Hom-associative algebras and covariant Hom-bialgebras,” *Journal of Geometry and Physics* 164 (2021), 104163, arXiv `2007.06053`.
