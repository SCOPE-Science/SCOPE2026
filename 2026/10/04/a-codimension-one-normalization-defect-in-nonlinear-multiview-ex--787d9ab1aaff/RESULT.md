# A codimension-one normalization defect in nonlinear multiview Example 6.7

## Finding

Work over an algebraically closed field of characteristic zero. Let
\[
G:\mathbb P^3\dashrightarrow \mathbb P^3\times\mathbb P^3,
\qquad
[x:y:z:w]\longmapsto
([x:y:z:w],[xy^2:xw^2:yzw:z^2w]),
\]
and let \(Y=\overline{\operatorname{im}G}\). Write \([X:Y:Z:W]\) for the first factor and \([A:B:C:D]\) for the second. On the affine chart \(X=D=1\), the graph closure is exactly
\[
Y_{X,D}\cong
\operatorname{Spec} k[Z,A,B,C]/(C^2-ABZ^2).
\]
Consequently \(Y\) is not normal. The normalization of this chart is
\[
\widetilde Y_{X,D}=
\operatorname{Spec} k[Z,A,B,T]/(T^2-AB),
\qquad C=ZT,
\]
and its conductor in \(Y_{X,D}\) is the height-one ideal \((Z,C)\). Thus the codimension-one component \(V(Z,C)\cong\mathbb A^2\) of the singular locus is precisely the nonnormal locus on this chart. The remaining singular component is \(V(A,B,C)\); away from \(Z=0\) it is a normal transverse \(A_1\) stratum because, after setting \(T=C/Z\), the local equation is \(T^2=AB\).

## Assumptions and scope

This is the explicit monomial map of Example 6.7 in Cid-Ruiz--Clarke--Mohammadi. The source computes its image multidegrees
\[
\deg_{(3,0)}(Y)=1,\qquad
\deg_{(2,1)}(Y)=3,\qquad
\deg_{(1,2)}(Y)=5,\qquad
\deg_{(0,3)}(Y)=2.
\]
The source paper has primary MSC 14E05 and first appeared publicly as arXiv:2112.06216 on 2021-12-12. The claim here concerns only the displayed graph chart and the resulting global conclusion that \(Y\) is nonnormal. It does not classify every singular chart of \(Y\), nor does it assert a global description of the full normalization.

## Proof

Introduce an auxiliary variable \(t\). The graph closure is the multiprojective toric image of
\[
X\mapsto x,\quad Y\mapsto y,\quad Z\mapsto z,\quad W\mapsto w,
\]
\[
A\mapsto xy^2t,\quad B\mapsto xw^2t,\quad C\mapsto yzwt,\quad D\mapsto z^2wt.
\]
Therefore its bihomogeneous defining ideal is the elimination kernel of
\[
(X-x,\;Y-y,\;Z-z,\;W-w,\;A-xy^2t,\;B-xw^2t,\;C-yzwt,\;D-z^2wt).
\]
Exact lexicographic elimination gives eight binomial generators. Three of them are
\[
DY-CZ,\qquad DXW-BZ^2,\qquad C^2X-ADW.
\]
Dehomogenizing the complete elimination ideal at \(X=D=1\) and reducing it gives exactly
\[
Y-CZ,\qquad W-BZ^2,\qquad C^2-ABZ^2.
\]
Eliminating \(Y\) and \(W\) proves the asserted hypersurface model
\[
R=k[Z,A,B,C]/(C^2-ABZ^2).
\]
The polynomial \(C^2-ABZ^2\) is irreducible over \(k[Z,A,B,C]\), so \(R\) is a domain.

Now set \(T=C/Z\) in \(\operatorname{Frac}(R)\). It is integral over \(R\) because
\[
T^2-AB=0.
\]
But \(T\notin R\). Indeed, if \(T\in R\), then \(C=ZT\in ZR\). Modulo \(Z\), however,
\[
R/ZR\cong k[A,B,C]/(C^2),
\]
and the class of \(C\) is nonzero. Hence \(C\notin ZR\), a contradiction. This proves that \(R\), and therefore \(Y\), is not normal.

Let
\[
S=k[Z,A,B,T]/(T^2-AB)
\]
with \(R\to S\) given by \(C\mapsto ZT\). The extension is finite because \(T\) is integral, and it is birational because \(T=C/Z\) in the common fraction field. The hypersurface \(S\) is Cohen--Macaulay. Its singular locus is \(A=B=T=0\), with \(Z\) free, hence has codimension two in the threefold \(\operatorname{Spec}S\). Thus \(S\) satisfies Serre's \(R_1\) and \(S_2\) conditions and is normal. Therefore \(S\) is the integral closure of \(R\).

For the conductor, first note
\[
ZT=C\in R,\qquad CT=ZAB\in R,
\]
so \((Z,C)\) lies in the conductor. Conversely, if \(r\) is in the conductor, then \(rT\in R\). Reducing the inclusion \(R\subset S\) modulo \(Z\), the image of \(R\) is \(k[A,B]\), whereas
\[
S/(Z)\cong k[A,B,T]/(T^2-AB).
\]
Write the image of \(r\) as \(f(A,B)\). The condition \(rT\in R\) forces \(f(A,B)T\in k[A,B]\). Since \(1,T\) are linearly independent over the fraction field of \(k[A,B]\), this implies \(f=0\). Hence \(r\in(Z,C)\), proving that the conductor is exactly \((Z,C)\).

Finally, for
\[
f=C^2-ABZ^2,
\]
the Jacobian equations are
\[
2C=0,\qquad BZ^2=0,\qquad AZ^2=0,\qquad 2ABZ=0.
\]
In characteristic zero the singular locus is therefore
\[
V(Z,C)\cup V(A,B,C).
\]
The first component has codimension one in \(Y_{X,D}\) and is exactly the conductor support, hence the nonnormal locus. On the second component with \(Z\ne0\), the coordinate change \(T=C/Z\) turns the equation into \(T^2=AB\), the standard \(A_1\) surface singularity times the smooth \(Z\)-direction.

## Verification

The accompanying `verify_example67_nonnormal.py` reconstructs the graph kernel from the monomial parametrization using exact SymPy Gröbner-basis arithmetic. It verifies that the complete elimination ideal has eight generators, checks the three relations used in the proof, proves equality of the dehomogenized chart ideal with
\[
(Y-CZ,\;W-BZ^2,\;C^2-ABZ^2),
\]
checks that \(C\notin(Z,C^2-ABZ^2)\), verifies the normalization equation \(T^2=AB\), and confirms the two Jacobian strata. Running the packaged script prints `VERIFY_OK`.

## Relationship to prior work

Cid-Ruiz--Clarke--Mohammadi introduce this exact map in Example 6.7 to illustrate their mixed-volume formula and record the four multidegrees above. In their discussion of nonlinear multiview varieties, they emphasize that their method computes multidegrees even when familiar radical/generic-initial-ideal behavior from the linear case is unavailable. The inspected Example 6.7 and its surrounding section do not state the affine equation \(C^2=ABZ^2\), nonnormality, normalization, conductor, or the separation between the codimension-one defect and the normal \(A_1\) stratum.

Exact-object searches using the monomial quadruple \((xy^2,xw^2,yzw,z^2w)\), graph/Rees-algebra terminology, nonnormality, normalization, and conductor language returned the source paper or unrelated monomial/Rees examples, but no inspected publication asserting the present chart-level statement. General results on normal Rees algebras of squarefree or Ferrers-type monomial ideals do not apply directly because this base ideal is neither squarefree nor one of those stated families. Negative search evidence is not a novelty proof; it only reduces overlap risk.

## Limitations

Only one affine chart is classified in full. That is sufficient to prove global nonnormality, but no claim is made here about the complete global conductor, the entire singular locus of \(Y\), or a projective construction of the full normalization. The argument assumes characteristic zero; characteristic two requires a separate singularity analysis. An equivalent computation may exist under different toric or Rees-algebra notation despite the searches recorded in the audit.

## References

1. Y. Cid-Ruiz, O. Clarke, F. Mohammadi, *A study of nonlinear multiview varieties*, arXiv:2112.06216, first public 2021-12-12; Journal of Algebra 620 (2023), 363--391, DOI 10.1016/j.jalgebra.2022.12.036.
2. S. Moradi, *Normal Rees algebras arising from vertex decomposable simplicial complexes*, arXiv:2311.15135 (2023). This gives broad normality results for squarefree families and is cited here only as a non-covering comparison.
3. K.-N. Lin, Y.-H. Shen, *Koszul blowup algebras associated to three-dimensional Ferrers diagrams*, arXiv:1709.03251 (2017). This treats a different squarefree Ferrers class.
