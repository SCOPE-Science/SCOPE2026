# Complete nonzero-weight relative Rota–Baxter operators on a central four-dimensional \(3\)-Lie algebra

## Finding

Let \(K\) be any field, let \(\lambda\in K^\times\), and let \(L\) have basis \(e_1,e_2,e_3,e_4\) and alternating ternary bracket determined by
\[
[e_2,e_3,e_4]=e_1.
\]
Its derived ideal and center are \(D=Ke_1\). The adjoint action is a valid action in the sense of Hou–Sheng–Zhou. A relative Rota–Baxter operator of weight \(\lambda\) for that action is a linear map \(R:L\to L\) satisfying
\[
[Rx,Ry,Rz]=R\bigl([Rx,Ry,z]+[Ry,Rz,x]+[Rz,Rx,y]+\lambda[x,y,z]\bigr)
\]
for all \(x,y,z\in L\).

**Every such operator preserves the characteristic derived ideal**:
\[
\boxed{R(D)\subseteq D.}
\]
Writing \(W=\langle e_2,e_3,e_4\rangle\), every solution is therefore **exactly**
\[
\boxed{R=\begin{pmatrix}a&h\\0&A\end{pmatrix},\qquad
 a\in K,\quad h\in K^{1\times3},\quad A\in M_3(K),\quad
 \det A=a\bigl(\sigma_2(A)+\lambda\bigr),}
\]
where \(\sigma_2(A)\) is the sum of the three principal \(2\times2\) minors. There are no other solutions, and the displayed equation is sufficient for every \(h\).

The **reduced** operator variety is a geometrically integral hypersurface of dimension \(12\) in the \(13\)-dimensional derived-preserving endomorphism space, with three free affine coordinates from \(h\).

For \(K=\mathbf F_q\), define \(\chi_q\) to be the quadratic character of \(\mathbf F_q^\times\) when \(q\) is odd, and put \(\chi_q(\lambda)=0\) when \(q\) is even. The complete number of weight-\(\lambda\) relative Rota–Baxter operators is
\[
\boxed{N_q(\lambda)=q^{12}+q^{10}-q^8-\bigl(1+\chi_q(\lambda)\bigr)q^7.}
\]
For odd \(q\), the square and nonsquare weight classes therefore differ by precisely \(2q^7\) operators. In even characteristic the count is independent of the nonzero weight.

The point-count zeta function of the operator variety over \(\mathbf F_q\), for fixed \(\lambda\in\mathbf F_q^\times\), is
\[
\boxed{
 Z_\lambda(T)=
 \begin{cases}
 \displaystyle\frac{(1-q^8T)(1-q^7T)(1-\chi_q(\lambda)q^7T)}{(1-q^{12}T)(1-q^{10}T)},&q\text{ odd},\\[6pt]
 \displaystyle\frac{(1-q^8T)(1-q^7T)}{(1-q^{12}T)(1-q^{10}T)},&q\text{ even}.
 \end{cases}}
\]

## Assumptions and scope

The ternary operation is alternating, so the single displayed nonzero independent bracket determines all products. Since its image is central, the Filippov identity and the source's adjoint-action conditions hold over any coefficient field. The operator definition is **Definition 2.6 of Hou–Sheng–Zhou**, not the distinct nonzero-weight operator identity noted in their Remark 2.7.

The cited paper first appeared publicly as arXiv:2204.02196v1 on **2022-03-22 UTC** and lists primary MSC2020 **17A42**. Its Example 2.14 uses this exact four-dimensional algebra and exhibits one rank-two projection; Proposition 2.13 produces further projections. The present statement classifies *all* linear maps satisfying Definition 2.6 for nonzero weight, over arbitrary fields, including the nonprojection and invertible maps.

The assumption \(\lambda\ne0\) is essential. At zero weight the rank-one map sending \(e_1\mapsto e_2\) and annihilating \(e_2,e_3,e_4\) satisfies the relative identity but does **not** preserve \(D\).

## Proof

Write the alternating bracket as
\[
[x,y,z]=\det(\pi x,\pi y,\pi z)e_1,
\]
where \(\pi:L\to W\) is projection along \(D\). For an arbitrary operator \(R\), set
\[
R(e_1)=ae_1+u,\qquad
R(w)=h(w)e_1+A(w)\quad(w\in W),
\]
with \(u\in W\), \(h\in W^*\), and \(A\in\operatorname{End}(W)\). Let \(Q_R(x,y,z)\) denote the scalar multiplying \(e_1\) inside \(R(\cdots)\) in the defining identity. Then
\[
\det(\pi Rx,\pi Ry,\pi Rz)e_1
  =Q_R(x,y,z)(ae_1+u).
\]

**Derived-line rigidity.** Suppose \(u\ne0\). Comparison of the \(W\)-components forces \(Q_R\equiv0\), hence all the determinants on the left vanish. In particular,
\[
\dim\langle u,\operatorname{im}A\rangle\le2.
\]
Define the alternating form \(\beta(w,z)=\det(u,w,z)\) on \(W\), whose radical is \(Ku\). The equations with arguments \((e_1,w,z)\) become
\[
\beta(Aw,z)+\beta(w,Az)=0
\qquad(w,z\in W).
\]
Taking \(w=u\) gives \(Au\in Ku\), so \(A\) induces a map \(B\) on the two-dimensional quotient \(W/Ku\). Its induced nondegenerate alternating form obeys
\[
\beta(B\bar w,\bar z)+\beta(\bar w,B\bar z)
 =\operatorname{tr}(B)\beta(\bar w,\bar z).
\]
Thus \(\operatorname{tr}B=0\). The dimension bound above implies \(\operatorname{rank}B\le1\), so \(\det B=0\). With \(Au=cu\), the characteristic polynomial of \(A\) factors as
\[
(t-c)\bigl(t^2-\operatorname{tr}(B)t+\det B\bigr),
\]
whence
\[
\sigma_2(A)=c\operatorname{tr}B+\det B=0.
\]
But at \((e_2,e_3,e_4)\) the scalar is
\[
Q_R(e_2,e_3,e_4)=\sigma_2(A)+\lambda.
\]
Since \(Q_R=0\), this would give \(\lambda=0\), a contradiction. Therefore \(u=0\) for every nonzero-weight solution. This argument uses no characteristic restriction.

**Complete block equation.** Now \(R(e_1)=ae_1\). The relative identity on any triple containing \(e_1\) is automatically satisfied. On the independent triple \((e_2,e_3,e_4)\), its two sides are respectively
\[
(\det A)e_1\qquad\text{and}\qquad
 a(\sigma_2(A)+\lambda)e_1.
\]
This proves the necessary-and-sufficient block equation. The covector \(h\) drops out because every bracket depends only on \(\pi\).

**Geometric integrality.** In the polynomial ring \(K[A_{ij}]\), the generic determinant \(\det A\) is irreducible. Its degree is \(3\), while \(\sigma_2(A)+\lambda\) has degree \(2\), so these polynomials are coprime. Consequently
\[
F(A,a)=\det A-a(\sigma_2(A)+\lambda)
\]
is primitive and linear in \(a\), hence irreducible in \(K[A_{ij},a]\). This remains true after any extension of \(K\). Including the three free coordinates \(h\) gives the geometrically integral reduced hypersurface of dimension \(12\).

**Finite-field count.** Fix \(q\), put \(s=-\lambda\ne0\), and define
\[
M_q(s)=\#\{A\in M_3(\mathbf F_q):\sigma_2(A)=s\},
\quad
H_q(s)=\#\{A:\sigma_2(A)=s,\ \det A=0\}.
\]
For each \(A\) with \(\sigma_2(A)\ne s\), the block equation fixes \(a\) uniquely. If \(\sigma_2(A)=s\), it permits all \(q\) values of \(a\) exactly when \(\det A=0\). The free \(h\) then gives
\[
N_q(\lambda)=q^3\bigl(q^9-M_q(s)+qH_q(s)\bigr).
\]

For \(s\ne0\), the characteristic polynomial of any matrix counted by \(H_q(s)\) has \(0\) as a simple root. It consequently has a one-dimensional kernel \(L_0\), a complementary two-dimensional image \(U_0\), and an invertible induced endomorphism of \(U_0\) with determinant \(s\). Conversely each such triple determines the matrix. There are \(q^2+q+1\) kernel lines, \(q^2\) complements to each line, and \(q(q^2-1)\) invertible \(2\times2\) maps of prescribed determinant. Therefore
\[
\boxed{H_q(s)=q^3(q^2+q+1)(q^2-1).}
\]

To count \(M_q(s)\), note the explicit quadratic form
\[
\sigma_2(A)
 =A_{11}A_{22}+A_{11}A_{33}+A_{22}A_{33}
  -A_{12}A_{21}-A_{13}A_{31}-A_{23}A_{32}.
\]
For odd \(q\), its symmetric Gram matrix has determinant \(-1/256\), so it is a nondegenerate quadratic form of dimension \(9\). The elementary odd-dimensional quadratic-form fiber formula (obtained by diagonalization and quadratic Gauss sums) yields, for \(s\ne0\),
\[
M_q(s)=q^8+\chi_q(-s)q^4.
\]
For even \(q\), every matrix decomposes uniquely as \(A=B+cI\) with \(\operatorname{tr}B=0\). The identity
\[
\sigma_2(B+cI)=\sigma_2(B)+c^2
\]
shows that for each of the \(q^8\) choices of trace-zero \(B\), there is exactly one \(c\) giving \(\sigma_2(A)=s\), because squaring is bijective on a finite field of characteristic \(2\). Thus \(M_q(s)=q^8\) for even \(q\). Substitution into the counting formula gives the displayed \(N_q(\lambda)\) in all characteristics.

**Weights and zeta function.** Scaling an operator by \(t\in K^\times\) sends weight \(\lambda\) to weight \(t^2\lambda\), explaining why the odd-characteristic count depends only on the square class and why every nonzero weight is equivalent in even finite characteristic. For odd \(q\), the quadratic character of \(\lambda\) in \(\mathbf F_{q^m}\) is \(\chi_q(\lambda)^m\). Replacing \(q\) by \(q^m\) in the formula therefore gives
\[
N_{q^m}(\lambda)
 =q^{12m}+q^{10m}-q^{8m}-q^{7m}
  -\chi_q(\lambda)^m q^{7m}.
\]
For even \(q\), omit the final character term. Applying
\[
Z_\lambda(T)=\exp\left(\sum_{m\ge1}\frac{N_{q^m}(\lambda)}{m}T^m\right)
\]
gives the displayed rational functions.

## Verification

The standalone file `artifacts/verify.py` reconstructs the complete ternary bracket and defining operator equation from the multiplication table. It checks symbolically that the four independent basis-triple defects for derived-preserving matrices vanish exactly under the single determinant equation and that the general non-derived-preserving defect has the predicted \(W\)-component. It recomputes the quadratic-form Gram determinant \(-1/256\), and verifies the strict zero-weight boundary.

The checker exhaustively inspects all \(2^{16}=65536\) endomorphisms of the four-dimensional algebra over \(\mathbf F_2\), obtaining exactly **4736** nonzero-weight solutions, all preserving the derived line. It exhaustively enumerates all \(3^9\) and \(5^9\) matrices \(A\) to check each odd-characteristic quadratic fiber and singular-fiber count; it obtains respectively **579555** and **583929** solutions for the two nonzero weights over \(\mathbf F_3\), and **253359375** or **253515625** over \(\mathbf F_5\) according to square class. It additionally enumerates all \(4^9\) matrices over \(\mathbf F_4\), obtaining **17743872** solutions for every nonzero weight.

The checker prints `VERIFY_OK`. Finite enumeration is not used as a proof for arbitrary fields; the arbitrary-field classification and finite-field formulas have the independent algebraic proofs above.

## Relationship to prior work

Hou–Sheng–Zhou establish the defining identity, its graph interpretation and deformation theory. Their Proposition 2.13 and Example 2.14 construct projections on the same four-dimensional algebra, whereas the present theorem classifies **all** operators, proves automatic preservation of the derived ideal at nonzero weight, and counts the resulting hypersurface over every finite field. The source does not give the determinant/second-minor equation or the character-sensitive arithmetic.

Teng–Dai study the same isomorphism type of four-dimensional \(3\)-Lie algebra but a **different** nonabelian embedding-tensor identity. Their Definition 2.6 involves only one coherent-action term and a native ternary bracket; it is not the cyclic three-action-term relative Rota–Baxter identity of Hou–Sheng–Zhou. Their Example 2.8 is therefore not a classification of the operators considered here.

The classical nonzero-weight \(3\)-Lie Rota–Baxter convention is also explicitly distinguished from the relative identity in Hou–Sheng–Zhou Remark 2.7. The later Hou–Sheng–Zhou unified approach concerns controlling algebras and cohomologies; its accessible abstract does not claim the present finite-field enumeration. Searches under the source's exact example, equivalent derived-stable block equations, and the numerical square-class formulas did not locate a covering result.

## Limitations

The theorem is for the specific central four-dimensional \(3\)-Lie algebra and the **adjoint-action relative** operator identity at fixed nonzero weight. It does not classify other ternary algebras, the competing nonzero-weight Rota–Baxter convention, or the zero-weight solution locus.

The statement about geometric integrality refers to the **reduced** solution variety; no assertion about absence of nonreduced structure in the unreduced defining equation scheme is made.

The closest broader 2026 source was available as an abstract rather than full text, leaving some literature-coverage risk. Finite experiments independently confirm small-field instances but do not prove the general count. A failed search is not a proof of absolute historical novelty.

## References

1. S. Hou, Y. Sheng, and Y. Zhou, “\(3\)-post-Lie algebras and relative Rota-Baxter operators of nonzero weight on \(3\)-Lie algebras,” *Journal of Algebra* 615 (2023), 103–129, DOI `10.1016/j.jalgebra.2022.10.016`, earliest public version arXiv:2204.02196v1 (2022-03-22).
2. W. Teng and X. Dai, “Nonabelian embedding tensors on \(3\)-Lie algebras and \(3\)-Leibniz-Lie algebras,” *Electronic Research Archive* 33 (2025), 1367–1383, DOI `10.3934/era.2025063`, arXiv:2310.06990v1.
3. S. Hou, Y. Sheng, and Y. Zhou, “A unified approach to controlling algebras and cohomologies of various operators on \(3\)-Lie algebras,” *International Journal of Geometric Methods in Modern Physics* 23 (2026), 2540025, DOI `10.1142/S0219887825400250` (abstract consulted).
