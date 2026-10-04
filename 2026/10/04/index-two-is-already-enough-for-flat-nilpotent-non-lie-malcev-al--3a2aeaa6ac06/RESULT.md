# Index two is already enough for flat nilpotent non-Lie Malcev algebras
## Finding
Let \(M_{a,b,f}\) be the real vector space with basis \(e,d,e_1,e_2,e_3,e_4\), where \(a,b,f\in\mathbb R\) and \(af\ne0\). Give it the anticommutative product determined by
\[
[d,e_3]=-a e_1,\qquad [d,e_4]=-b e_1-f e_3,\qquad [e_2,e_3]=a e,
\]
\[
[e_2,e_4]=b e,\qquad [e_3,e_4]=f e,
\]
with all remaining basis brackets zero. Give it the symmetric bilinear form whose only nonzero basis pairings are
\[
\langle e,d\rangle=\langle e_1,e_2\rangle=\langle e_3,e_3\rangle=\langle e_4,e_4\rangle=1.
\]
This is the explicit flat non-Lie Malcev family constructed in arXiv:2609.13950v1. The additional structural conclusion is
\[
[M_{a,b,f},M_{a,b,f}]=\operatorname{span}\{e_1,e_3,e\},\qquad
[M_{a,b,f},[M_{a,b,f},M_{a,b,f}]]=\operatorname{span}\{e_1,e\},
\]
and the next lower-central term is zero. Thus the algebra is nilpotent of class exactly \(3\). Its center is
\[
Z(M_{a,b,f})=\operatorname{span}\{e,e_1\},
\]
which is a two-dimensional totally isotropic plane. The metric has four positive and two negative directions, hence index \(2\). Since
\[
J(d,e_4,e_2)=af\,e\ne0,
\]
the algebra is not Lie. Therefore the source theorem saying that every flat Lorentzian, hence index-\(1\), nilpotent Malcev algebra is Lie is sharp in the metric index: the Lie conclusion already fails at index \(2\).

## Assumptions and scope
The field is \(\mathbb R\), matching the pseudo-Euclidean signature discussion. The parameters satisfy \(af\ne0\); \(b\) is arbitrary. Flatness here means flatness for the Malcev curvature introduced in arXiv:2609.13950v1, not vanishing of the classical Lie-algebra curvature formula applied to a non-Lie bracket. The claim concerns this explicit family and the sharpness of the Lorentzian index threshold; it does not classify all index-\(2\) flat nilpotent Malcev algebras.

## Proof
Because \(a\ne0\), the bracket \([d,e_3]=-a e_1\) puts \(e_1\) in \([M,M]\), and \([e_2,e_3]=a e\) puts \(e\) there. Since \(f\ne0\), the relation \([d,e_4]=-b e_1-f e_3\), together with \(e_1\in[M,M]\), also puts \(e_3\) in \([M,M]\). Every displayed bracket lands in \(\operatorname{span}\{e_1,e_3,e}\), so
\[
[M,M]=\operatorname{span}\{e_1,e_3,e\}.
\]
The vectors \(e\) and \(e_1\) are central. Bracketing the derived algebra with \(M\) therefore leaves only brackets involving \(e_3\): \([d,e_3]=-a e_1\), \([e_2,e_3]=a e\), and \([e_4,e_3]=-f e\). Hence
\[
[M,[M,M]]=\operatorname{span}\{e_1,e\},\qquad [M,\operatorname{span}\{e_1,e\}]=0.
\]
Both spans are nonzero under \(af\ne0\), so the nilpotency class is exactly \(3\).

For the center, write a general vector as
\[
x=\alpha e+\beta d+c_1e_1+c_2e_2+c_3e_3+c_4e_4.
\]
The condition \([x,d]=0\) gives \(f c_4=0\) and then \(a c_3=0\), so \(c_4=c_3=0\). The condition \([x,e_3]=0\) then gives \(a\beta=0\) and \(a c_2=0\), so \(\beta=c_2=0\). Thus \(x\in\operatorname{span}\{e,e_1}\), and the reverse inclusion is immediate from the table.

The restriction of the metric to \(\operatorname{span}\{e,e_1}\) is zero, so this center is totally isotropic. The metric matrix is the orthogonal sum of two hyperbolic planes, on \(\operatorname{span}\{e,d}\) and \(\operatorname{span}\{e_1,e_2}\), and two positive lines, \(\mathbb Re_3\) and \(\mathbb Re_4\). It therefore has four positive and two negative eigenvalues and index \(2\).

Finally, with \(J(x,y,z)=[[x,y],z]+[[y,z],x]+[[z,x],y]\),
\[
J(d,e_4,e_2)=[-b e_1-f e_3,e_2]=af\,e\ne0.
\]
The primary source proves that the same family is flat for its Malcev curvature. Its main Lorentzian theorem proves that every flat index-\(1\) nilpotent Malcev algebra is Lie. The present index-\(2\) family is flat, nilpotent, and non-Lie, so the metric-index threshold cannot be extended from \(1\) to \(2\).

## Verification
The accompanying `verify.py` reconstructs the bracket and metric symbolically. It verifies the Malcev identity for generic symbolic vectors, confirms the metric inertia \((4,2)\), reconstructs the five nonzero Levi-Civita products from the Koszul formula, checks the derived and lower-central spans, the totally isotropic center, and the nonzero Jacobiator. Running it produces `CHECK_OK`; the captured output is included in `verify_output.txt`. Flatness itself is cited from the primary source, because that paper uses a Malcev-specific curvature operator rather than the classical Lie curvature formula.

## Relationship to prior work
Boucetta, El Ouali, and Tibssirte introduce flat pseudo-Euclidean Malcev algebras, develop a flat double-extension construction, prove that every flat Lorentzian nilpotent Malcev algebra is Lie, and give the displayed six-dimensional flat non-Lie example. In the inspected full text, the example is used to exhibit flat non-Lie behavior and its Jacobi failure; the lower-central series, center, and index-\(2\) sharpness consequence above are not stated as a result.

Bajo, Benayadi, and Lebzioui classify flat Lorentzian nilpotent Lie algebras. Their work concerns the Lie category and index \(1\), so it does not imply the present non-Lie Malcev boundary example. Semantic and exact-form searches for flat nilpotent non-Lie Malcev algebras at index \(2\), for the displayed bracket table, and for a sharpness statement at metric index \(2\) did not locate a stronger covering result.

## Limitations
The result is a sharp boundary example, not a classification at index \(2\). It does not assert dimension minimality among all flat nilpotent non-Lie Malcev algebras. The only flatness assertion used is the one established for this family in arXiv:2609.13950v1; the accompanying computation verifies the new algebraic deductions and the Malcev identity but does not replace the paper's generalized-curvature calculation. Older pseudo-Euclidean Malcev literature could contain an equivalent index-\(2\) example under different terminology, which remains the main originality risk.

## References
1. Mohamed Boucetta, Hamza El Ouali, Oumaima Tibssirte, *On flat pseudo-Euclidean solvable Malcev algebras*, arXiv:2609.13950v1, 12 September 2026.
2. Ignacio Bajo, Saïd Benayadi, Hicham Lebzioui, *Classification of flat Lorentzian nilpotent Lie algebras*, Bulletin of the London Mathematical Society 56 (2024), 2132--2149, DOI 10.1112/blms.13047.
