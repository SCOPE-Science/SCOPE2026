# Full-diameter exposing slices for the non-elementary projective and symmetric tensors
## Finding
For the explicit projective-tensor construction of Dantas, Mazzitelli and Rodríguez, let \(X\) be the hexagonal two-dimensional space with \(B_X=\operatorname{aco}\{x_1,x_2,x_3\}\), where \(x_1=(1,0)\), \(x_2=(0,1)\), and \(x_3=(-1,-1)\). Let \(Y\) be their equivalent renorming of \(c_0\), formed from vectors
\[
w_{j,n}=r_nP_nz_j,\qquad 0<r_n<1,\qquad r_n\uparrow1,
\]
and let \(\varphi\) be the functional induced by the operator \(A:X\to Y^*\) satisfying \(A(x_j)=f_j\), where \(f_1=e_1^*\), \(f_2=e_2^*\), and \(f_3=-e_1^*-e_2^*\). The source proves that the restriction of \(\varphi\) exposes the rank-two tensor
\[
u=\frac12\bigl(x_1\otimes e_1+x_2\otimes e_2\bigr)
\]
in \(B_{X\widehat{\otimes}_\pi Y}\).

For every \(\alpha>0\), the slice
\[
S_\alpha=\bigl\{v\in B_{X\widehat{\otimes}_\pi Y}:\varphi(v)>1-\alpha\bigr\}
\]
has diameter exactly \(2\).

The same is true after the source's symmetric transfer. If \(J:X\widehat{\otimes}_\pi Y\to\widehat{\otimes}_{\pi_s}^{2,s}Z\) is the isometry, \(M\) is the contractive projection onto \(J(X\widehat{\otimes}_\pi Y)\), \(u_s=J(u)\), and \(\Psi=\varphi\circ J^{-1}\circ M\), then for every \(\alpha>0\),
\[
\operatorname{diam}\bigl\{w\in B_{\widehat{\otimes}_{\pi_s}^{2,s}Z}:\Psi(w)>1-\alpha\bigr\}=2.
\]

## Assumptions and scope
All spaces are real. The statement concerns the concrete spaces, vectors, sequence \((r_n)\), and exposing functionals used in arXiv:2609.01835v1. It does not assert that every exposing functional of every exposed tensor has full-diameter slices. The symmetric conclusion concerns the source's degree-two transfer through the isometric embedding \(J\); no claim is made here for its higher-degree constructions.

## Proof
Write \(t_{j,n}=\|w_{j,n}\|_Y\). Because \(w_{j,n}\in B_Y\), we have \(t_{j,n}\le1\). On the other hand, the source proves \(\|f_j\|_{Y^*}=1\), and directly from the definitions \(f_j(w_{j,n})=r_n\). Hence
\[
r_n\le t_{j,n}\le1.
\]
Define
\[
y_{j,n}=\frac{w_{j,n}}{t_{j,n}}\in S_Y,\qquad v_{j,n}=x_j\otimes y_{j,n}\in S_{X\widehat{\otimes}_\pi Y}.
\]
Since \(\varphi(x_j\otimes y)=f_j(y)\),
\[
\varphi(v_{j,n})=\frac{r_n}{t_{j,n}}\ge r_n\longrightarrow1.
\]
Thus, for every fixed \(\alpha>0\), the points \(v_{1,n}\) and \(v_{2,n}\) both belong to \(S_\alpha\) for all sufficiently large \(n\).

It remains to show that their mutual distance tends to the maximal possible value. Set
\[
g_1=\frac43f_1+\frac23f_2,\qquad
g_2=-\frac23f_1-\frac43f_2,\qquad
g_3=-\frac23f_1+\frac23f_2.
\]
These satisfy \(g_1+g_2+g_3=0\). Because \(B_Y\) is the closed absolutely convex hull of \(\frac14B_{c_0}\) and the vectors \(w_{j,n}\), a functional \(g=af_1+bf_2\) has norm determined on these generators. For the three displayed functionals, the values on \(z_1,z_2,z_3\) are respectively
\[
(g_1(z_1),g_1(z_2),g_1(z_3))=(1,0,-1),
\]
\[
(g_2(z_1),g_2(z_2),g_2(z_3))=(0,-1,1),
\]
and
\[
(g_3(z_1),g_3(z_2),g_3(z_3))=(-1,1,0).
\]
Their norms on \(\frac14B_{c_0}\) are at most \(1/2\), \(1/2\), and \(1/3\), respectively, while \(g_k(w_{j,n})=r_ng_k(z_j)\). Therefore \(\|g_1\|=\|g_2\|=\|g_3\|=1\).

There is consequently a norm-one operator \(C:X\to Y^*\) defined by \(C(x_j)=g_j\): indeed, \(B_X\) is the absolutely convex hull of the three \(x_j\). Let \(\Theta\) be the norm-one bilinear functional on \(X\widehat{\otimes}_\pi Y\) given by
\[
\Theta(x\otimes y)=(Cx)(y).
\]
For \(n\ge3\), the functionals \(g_1,g_2\) see only the first two coordinates, so
\[
\Theta(v_{1,n})=\frac{r_n}{t_{1,n}},\qquad
\Theta(v_{2,n})=-\frac{r_n}{t_{2,n}}.
\]
Hence
\[
\|v_{1,n}-v_{2,n}\|_\pi
\ge r_n\left(\frac1{t_{1,n}}+\frac1{t_{2,n}}\right)
\ge2r_n\longrightarrow2.
\]
Both points have norm one, so their distance is at most \(2\). Given any \(\varepsilon>0\), sufficiently large \(n\) puts both points in \(S_\alpha\) and makes their distance exceed \(2-\varepsilon\). Therefore \(\operatorname{diam}S_\alpha=2\).

For the symmetric construction, the source proves that \(J\) is an isometry and that \(M\) is a contractive projection onto its range. Thus
\[
\Psi(Jv)=\varphi(v)
\]
for every \(v\in X\widehat{\otimes}_\pi Y\), while
\[
\|Jv_{1,n}-Jv_{2,n}\|_{\pi_s}=\|v_{1,n}-v_{2,n}\|_\pi.
\]
The same sequences therefore lie eventually in every \(\Psi\)-slice and have distances tending to \(2\), proving the symmetric statement.

## Verification
The argument is exact and symbolic. The only quantitative ingredients are \(r_n\uparrow1\), the source's generator description of \(B_Y\), and the three rational coefficient vectors defining \(g_1,g_2,g_3\). Their generator values are computed explicitly above, which verifies \(\|C\|=1\). No finite experiment is used for an infinite conclusion.

The focal source was checked at the construction of \(B_Y\), Lemma 3.2, Fact 3.3, Lemma 3.6, Theorem A, and the degree-two symmetric transfer. Its full text contains no occurrence of “diameter” or “slice”. The 2023 paper of García-Lirola, Grelier, Martínez-Cervantes and Rueda Zoca was checked for the slice formulation of strong and weak-strong exposure and for its tensor-product extremality results.

## Relationship to prior work
Dantas, Mazzitelli and Rodríguez prove that \(u\) is a non-elementary exposed point and transfer it to a non-pure exposed symmetric tensor. Their introduction recalls the stronger qualitative facts that strongly exposed and denting points of projective tensor-product balls are elementary. Those qualitative obstructions do not determine the diameter of the slices produced by the particular functional that exposes \(u\).

García-Lirola, Grelier, Martínez-Cervantes and Rueda Zoca characterize strong and weak-strong exposure through shrinking slice neighbourhoods and prove elementary-tensor conclusions under appropriate hypotheses. Their statements distinguish exposure from stronger localization properties but do not supply the full-diameter quantitative behavior proved here.

A broader diameter-two theorem of Abrahamsen, Lima and Nygaard says that \(E\widehat{\otimes}_{\pi}F\) has the local diameter-two property if either factor has it. That result does not cover the focal construction through the \(Y\)-factor: choose \(n\ge3\) with \(r_n>1/2\) and \(B\) with \(3(1-r_n)<B<3r_n\). The functional
\[
h=2e_1^*+e_n^*-Be_{n+1}^*
\]
strongly exposes \(w_{1,n}\) in \(B_Y\). Indeed, \(h(w_{1,n})=3r_n\), whereas the \(rac14B_{c_0}\) part has supremum \((3+B)/4<3r_n\), the other \(w_{1,m}\) have values uniformly below \(3r_n\), and all signed \(w_{2,m},w_{3,m}\) generators also have absolute value strictly below \(3r_n\). Hence \(Y\) has slices of arbitrarily small diameter and fails the local diameter-two property. Thus the known factorwise sufficient theorem does not imply the present projective conclusion.

For symmetric projective tensor powers, Acosta and Becerra Guerrero prove that every slice has diameter two for important global classes, including infinite-dimensional \(C^*\)-algebras and spaces whose dual is an \(L_1\)-space. The latter hypothesis fails for the focal \(Z=X\oplus_\infty Y\): one has \(Z^*=X^*\oplus_1Y^*\), so if \(Z^*\) were an \(L_1\)-space then its \(L\)-summand \(X^*\) would be an \(L_1\)-space. But
\[
B_{X^*}=\{(a,b): |a|\le1,\ |b|\le1,\ |a+b|\le1\}
\]
is a hexagon, whereas a two-dimensional \(L_1\)-space is isometric to \(\ell_1^2\), whose unit ball is a four-vertex diamond. The focal construction also supplies no \(C^*\)-algebra structure on \(Z\) to invoke the other sufficient class. Therefore that global symmetric theorem does not imply the construction-specific statement proved here.

The new point is quantitative and construction-specific: the exact exposing functionals used in the 2026 counterexamples have slices of the largest possible diameter at every positive depth, despite the absence of a global diameter-two hypothesis on the factors used above.

## Limitations
The result is tied to the explicit approximating vectors \(w_{j,n}\) and to the source's exposing functionals. It does not classify all exposing functionals of \(u\) or \(u_s\), and it does not quantify slices associated with the higher-order examples. Search-based originality checks cannot exclude an older equivalent statement under different terminology. The closest inspected literature concerns qualitative strong exposure, weak-strong exposure, denting, preserved extremality, and global diameter-two sufficient hypotheses; none of the inspected statements implies this exact construction-specific diameter formula.

## References
1. S. Dantas, M. Mazzitelli and J. T. Rodríguez, “On Exposed (Symmetric) Tensors,” arXiv:2609.01835v1, 2026.
2. L. C. García-Lirola, G. Grelier, G. Martínez-Cervantes and A. Rueda Zoca, “Extremal Structure of Projective Tensor Products,” Results in Mathematics 78 (2023), Article 196, doi:10.1007/s00025-023-01970-y.
3. W. M. Ruess and C. P. Stegall, “Exposed and denting points in duals of operator spaces,” Israel Journal of Mathematics 53 (1986), 163–190.
4. D. Werner, “Denting points in tensor products of Banach spaces,” Proceedings of the American Mathematical Society 101 (1987), 122–126.
5. T. A. Abrahamsen, V. Lima and O. Nygaard, “Remarks on Diameter 2 Properties,” Journal of Convex Analysis 20 (2013), 439–452, arXiv:1304.7068, doi:10.68381/jca20026.
6. M. D. Acosta and J. Becerra Guerrero, “Slices in the Unit Ball of the Symmetric Tensor Product of a Banach Space,” Journal of Convex Analysis 18 (2011), 513–528, doi:10.68381/jca18033.
