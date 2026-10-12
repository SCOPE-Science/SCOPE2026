# A two-sided correction to a relative Rota–Baxter system example

## Finding

Consider the two-dimensional Leibniz algebra
\[
[e_1,e_1]=[e_1,e_2]=0,
\qquad
[e_2,e_1]=[e_2,e_2]=e_1,
\]
and its dual regular representation
\[
(\mathfrak g^\ast,L^\ast,-L^\ast-R^\ast).
\]

For
\[
R=
\begin{pmatrix}
a_{11}&a_{12}\\
a_{21}&a_{22}
\end{pmatrix},
\qquad
S=
\begin{pmatrix}
b_{11}&b_{12}\\
b_{21}&b_{22}
\end{pmatrix},
\]
Example 2.3 of arXiv:2101.04831v1 derives a polynomial system intended to be equivalent to the relative Rota–Baxter identities of Definition 2.1.

That printed system is not equivalent to the definition.

The local source of the discrepancy occurs in the \((e_1^\ast,e_1^\ast)\) equation for \(S\). The vector inside the outer \(S\) is
\[
-a_{21}(e_1^\ast+e_2^\ast)
+
b_{21}(e_1^\ast+e_2^\ast)
+
(b_{11}+b_{21})e_2^\ast.
\]
Definition 2.1 therefore requires applying \(S\) to every term. The displayed computation in the source instead applies \(R\) to the term proportional to
\[
-a_{21}.
\]

This is not a harmless rewriting: it produces both false positives and false negatives.

Over \(\mathbf Q\), let
\[
R=
\begin{pmatrix}
-2&0\\
2&0
\end{pmatrix},
\qquad
S=
\begin{pmatrix}
-1&0\\
2&0
\end{pmatrix}.
\]
These matrices satisfy every polynomial equation printed at the end of Example 2.3, but the actual \(S\)-equation of Definition 2.1 at
\[
(e_1^\ast,e_1^\ast)
\]
has defect
\[
\boxed{2e_1}.
\]
Thus the printed system has a false positive.

Conversely, let
\[
R=
\begin{pmatrix}
-2&-2\\
2&0
\end{pmatrix},
\qquad
S=
\begin{pmatrix}
-2&2\\
2&0
\end{pmatrix}.
\]
Direct substitution into Definition 2.1 gives zero defect for all four ordered basis pairs in both the \(R\)- and \(S\)-identities. Nevertheless, the source's third printed equation, the equation beginning with
\[
b_{21}(b_{11}+b_{21}),
\]
has residual
\[
\boxed{-8}.
\]
Thus the printed system also has a false negative.

There is a clean repair of the nonzero equal-lower-right branch. Over every field \(K\) with
\[
\operatorname{char}K\ne2,
\]
if
\[
a_{22}=b_{22}=t\ne0,
\]
then a pair \((R,S)\) satisfies Definition 2.1 if and only if
\[
\boxed{
R=S=
t
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}.
}
\]

In particular,
\[
a_{21}=b_{21}=-t.
\]
Hence the source summary's simultaneous assumptions
\[
a_{22}=b_{22}\ne0,
\qquad
a_{21}\ne b_{21}
\]
are incompatible with the conclusion printed immediately below them.

Over every odd finite field \(\mathbf F_q\), the repaired branch contains exactly
\[
\boxed{q-1}
\]
relative Rota–Baxter systems, one for each
\[
t\in\mathbf F_q^\times.
\]
Both maps have rank \(1\).

## Assumptions and scope

The correction targets the equations and summary of Example 2.3 in arXiv:2101.04831v1.

The later journal publication has DOI `10.4134/JKMS.j210676`. Its bibliographic metadata was checked, but its complete published full text was not used to establish whether this local computation was changed during publication. Accordingly, no claim is made here that the journal version necessarily contains the same error.

Matrices use columns:
\[
R(e_j^\ast)=\sum_i a_{ij}e_i,
\qquad
S(e_j^\ast)=\sum_i b_{ij}e_i.
\]

The branch classification assumes
\[
2\ne0.
\]
The two rational counterexamples are characteristic-zero statements and therefore do not depend on positive-characteristic subtleties.

## Proof

For
\[
x=x_1e_1+x_2e_2,
\qquad
y=y_1e_1+y_2e_2,
\]
the Leibniz bracket is
\[
[x,y]=x_2(y_1+y_2)e_1.
\]

The dual left and right regular maps are
\[
L_x^\ast=
\begin{pmatrix}
-x_2&0\\
-x_2&0
\end{pmatrix},
\qquad
R_x^\ast=
\begin{pmatrix}
0&0\\
-(x_1+x_2)&0
\end{pmatrix}.
\]
Thus the representation in Example 2.3 is
\[
\rho^L(x)=L_x^\ast,
\qquad
\rho^R(x)=-L_x^\ast-R_x^\ast.
\]

Definition 2.1 requires, for every \(u,v\in\mathfrak g^\ast\),
\[
[Ru,Rv]
=
R\!\left(\rho^L(Ru)v+\rho^R(Sv)u\right),
\]
and
\[
[Su,Sv]
=
S\!\left(\rho^L(Ru)v+\rho^R(Sv)u\right).
\]

At
\[
u=v=e_1^\ast,
\]
the common vector inside the outer map is
\[
(b_{21}-a_{21})e_1^\ast
+
(b_{11}+2b_{21}-a_{21})e_2^\ast.
\]
Therefore the first coordinate of the correct \(S\)-equation is
\[
a_{21}b_{11}
+a_{21}b_{12}
-b_{11}b_{12}
-2b_{12}b_{21}
+b_{21}^2
=
0.
\]

By contrast, the corresponding source equation contains the term
\[
(a_{11}+a_{12})a_{21}
\]
where the correct calculation has
\[
(b_{11}+b_{12})a_{21}.
\]
This is exactly the effect of applying \(R\), rather than \(S\), to the contribution proportional to \(-a_{21}\).

For the first rational witness
\[
(a_{11},a_{12},a_{21},a_{22};
b_{11},b_{12},b_{21},b_{22})
=
(-2,0,2,0;-1,0,2,0),
\]
all fourteen scalar equations printed in Example 2.3 vanish. The correct first-coordinate \(S\)-defect above equals
\[
2,
\]
so Definition 2.1 fails.

For the second rational witness
\[
(-2,-2,2,0;-2,2,2,0),
\]
direct expansion of both defining identities on all four ordered basis pairs gives zero. The source's third printed equation has residual
\[
-8.
\]
This proves that the mismatch goes in both directions.

It remains to repair the branch
\[
a_{22}=b_{22}=t\ne0.
\]

The correct basis equations contain
\[
a_{22}(a_{12}+a_{22})=0,
\qquad
a_{22}(a_{21}+a_{22})=0,
\]
\[
a_{22}(b_{21}+b_{22})=0,
\qquad
b_{22}(b_{12}+b_{22})=0.
\]
Since \(t\ne0\),
\[
a_{12}=a_{21}=b_{12}=b_{21}=-t.
\]

Another correct equation is
\[
a_{22}(2a_{11}+a_{12}+a_{21})=0,
\]
so
\[
2t(a_{11}-t)=0.
\]
When \(2\ne0\),
\[
a_{11}=t.
\]

The remaining \(S\)-equation on this branch reduces to
\[
2t(b_{11}-t)=0,
\]
hence
\[
b_{11}=t.
\]

Therefore
\[
R=S=
t
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}.
\]
Substitution shows that every nonzero \(t\) indeed gives a relative Rota–Baxter system, proving the if-and-only-if statement.

## Verification

The included `artifacts/verify.py` does not assume the corrected equations.

It reconstructs the Leibniz bracket, the dual regular representation, and both identities of Definition 2.1 symbolically. It then:

- derives the direct basis-pair defects;
- encodes the fourteen equations printed in Example 2.3;
- verifies that the false-positive witness satisfies all fourteen printed equations while its true \(S\)-defect is \(2e_1\);
- verifies that the false-negative witness satisfies Definition 2.1 while the source's third printed equation has value \(-8\);
- verifies symbolically that
  \[
  R=S=t
  \begin{pmatrix}
  1&-1\\
  -1&1
  \end{pmatrix}
  \]
  satisfies the definition;
- exhaustively checks the nonzero equal-lower-right branch over
  \[
  \mathbf F_3,\quad \mathbf F_5,\quad \mathbf F_7
  \]
  and finds exactly
  \[
  q-1
  \]
  systems in each field.

The checker returns `VERIFY_OK`.

The finite enumeration is a replay check. The characteristic-not-\(2\) branch theorem follows from the symbolic equations above.

## Relationship to prior work

Das and Guo introduce relative Rota–Baxter systems on Leibniz algebras and use Example 2.3 as their first explicit coordinate calculation for the dual regular representation. The correction here concerns that exact example.

The source's own summary already contains an internal warning sign: its second case assumes
\[
a_{21}\ne b_{21},
\]
while its displayed conclusion forces
\[
a_{21}=-a_{22},
\qquad
b_{21}=-b_{22},
\qquad
a_{22}=b_{22},
\]
and hence
\[
a_{21}=b_{21}.
\]
The direct reconstruction above identifies the earlier algebraic substitution that creates the mismatch and shows that the problem affects the polynomial system itself, not only the final prose summary.

Targeted searches using the article title, arXiv identifier, Example 2.3, the matrix-entry conditions, and correction or erratum terminology did not locate a published repair.

A current independent finite-field Rota–Baxter calculation using the same source concerns a different ordinary Rota–Baxter problem on a different Leibniz algebra; it does not imply or cover this correction.

## Limitations

The correction is established directly for arXiv:2101.04831v1.

The complete journal article text was not inspected, so a publication-stage correction cannot be excluded.

Only the nonzero equal-lower-right branch is fully reclassified here. The result does not claim a complete corrected classification of every possible pair \((R,S)\) in Example 2.3.

The finite-field branch count assumes odd characteristic.

Failed literature searches do not prove absolute novelty.

## References

1. A. Das and S. Guo, “Relative Rota-Baxter systems on Leibniz algebras,” arXiv:2101.04831v1, first public 13 January 2021.
2. A. Das and S. Guo, “Relative Rota-Baxter systems on Leibniz algebras,” *Journal of the Korean Mathematical Society* 60 (2023), 303–325, DOI `10.4134/JKMS.j210676`.
