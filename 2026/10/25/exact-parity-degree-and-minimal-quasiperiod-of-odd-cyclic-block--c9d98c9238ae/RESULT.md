# Exact parity degree and minimal quasiperiod of odd cyclic block polytopes

## Finding
For every odd integer \(m\ge3\) and every integer \(a\ge1\), let \(C_{m,a}\subset\mathbb R^{ma}\) consist of nonnegative coordinates \(x_{i,j}\), indexed by \(1\le i\le m\), \(1\le j\le a\), with the cyclic inequalities
\[
\sum_{j=1}^a x_{i,j}+\sum_{j=1}^a x_{i+1,j}\le1 \qquad(1\le i\le m),
\]
where indices \(i+1\) are taken modulo \(m\). For nonnegative integers \(q\), let \(L_{m,a}(q)=\#(qC_{m,a}\cap\mathbb Z^{ma})\). Denote its uniquely determined even and odd constituent polynomials by \(E_{m,a}(t)\) and \(O_{m,a}(t)\), respectively.

**Theorem.** The parity difference \(D_{m,a}(t)=E_{m,a}(t)-O_{m,a}(t)\) has exact degree \(m(a-1)\), and
\[
[t^{m(a-1)}]D_{m,a}(t)=\frac{1}{2^{ma}((a-1)!)^m}>0.
\]
Thus the minimal Ehrhart quasiperiod of \(C_{m,a}\) is exactly \(2\) for every odd \(m\ge3\) and every \(a\ge1\). More sharply, among the \(ma+1\) coefficient functions of its quasipolynomial, the highest \(m\) are parity-independent, while the coefficient of degree \(ma-m\) genuinely alternates with dilation parity. In particular, \(D_{m,1}(t)=2^{-m}\) for every odd \(m\ge3\).

There is also a closed differential-operator expression for the **entire parity difference**. Let \(B\) be the \(m\times m\) matrix \(B_{i,i}=B_{i,i+1}=1\), with cyclic indices, and let \(W_a(u)=\binom{u+a-1}{a-1}\). For independent variables \(s_1,\ldots,s_m\),
\[
D_{m,a}(t)=\left.\left(\prod_{i=1}^{m}W_a(\partial_{s_i})\right)
\left[
\exp\!\left(\frac t2\sum_i s_i\right)
\prod_{j=1}^{m}\frac{1}{1+\exp\!\left(-\sum_i(B^{-1})_{ij}s_i\right)}
\right]\right|_{s=0}.
\]
The expression is an ordinary Taylor evaluation of an analytic germ near \(s=0\), not an unspecified limit of divergent cone series.

## Assumptions and scope
The integer parameters satisfy \(m\ge3\) odd and \(a\ge1\). The polytope has dimension \(ma\), and its dilation parameter \(q\) is a nonnegative integer. A constituent polynomial agrees with \(L_{m,a}(q)\) for all sufficiently large integers of its stated parity (indeed for all nonnegative integers of that parity by rational Ehrhart theory). A quasiperiod is a common period of its coefficient functions, not the period of the sampled numerical sequence. The statement does not address even cycles or different block sizes.

## Proof
**1. Reduction to a weighted odd-cycle relaxation.** For \(x\in qC_{m,a}\cap\mathbb Z^{ma}\), set \(y_i=\sum_j x_{i,j}\). The vector \(y\) ranges over integer points of \(qQ_m\), where
\[
Q_m=\{y\in\mathbb R_{\ge0}^m:y_i+y_{i+1}\le1\text{ cyclically}\}.
\]
Each nonnegative integer height \(y_i\) has precisely \(W_a(y_i)=\binom{y_i+a-1}{a-1}\) ordered nonnegative integer compositions into \(a\) coordinates. Consequently
\[
L_{m,a}(q)=\sum_{y\in qQ_m\cap\mathbb Z^m}\prod_{i=1}^{m}W_a(y_i).
\]
This is a polynomially weighted Ehrhart count, with total weight degree \(m(a-1)\).

**2. All rational-vertex behavior is concentrated at one vertex.** Every vertex of \(Q_m\) having a zero coordinate is integral: deleting that coordinate breaks the odd cycle into paths, and the remaining edge-constraint matrix is totally unimodular (it is the vertex-edge incidence matrix of a bipartite graph, supplemented by unit rows). If a vertex has no zero coordinate, all its active facets must be among the \(m\) inequalities \(y_i+y_{i+1}\le1\); full rank forces all \(m\) to be tight. Their unique solution is \(c=(1/2,\ldots,1/2)\). This proves that \(c\) is the unique nonintegral vertex. It is simple because the \(m\) active inequalities have independent normals.

Write \(B=I+S\), where \(S\) cyclically shifts one coordinate. For odd \(m\), \(\det B=2\), and \(B\mathbb Z^m=\{z\in\mathbb Z^m:\sum_i z_i\text{ is even}\}\). The containment follows by summing the coordinates of \(By\); equality follows from the index \(|\det B|=2\).

**3. Exact parity contribution from the fractional tangent cone.** Choose generic complex \(s=(s_i)\) where the relevant exponential cone sums converge, and then continue them meromorphically. At the unique fractional vertex of \(qQ_m\), the tangent cone consists of
\[
y=qc-B^{-1}\ell,\qquad \ell\in\mathbb R_{\ge0}^{m}.
\]
For lattice points, \(\ell\) must be integer and \(By=q\mathbf1-\ell\) must lie in \(B\mathbb Z^m\); since \(m\) is odd, this holds exactly when \(\sum_j\ell_j\equiv q\pmod2\). Put \(u_j(s)=\exp(-\sum_i(B^{-1})_{ij}s_i)\). The exponential cone generating function at this vertex is
\[
H_{c,q}(s)=e^{(q/2)\sum_i s_i}
\sum_{\ell\in\mathbb Z_{\ge0}^m,\,\sum_j\ell_j\equiv q\;(\mathrm{mod}\,2)}
\prod_j u_j(s)^{\ell_j}.
\]
The even- and odd-parity sums have the same singular part \(\tfrac12\prod_j(1-u_j)^{-1}\). Their **difference**, after factoring out the displayed exponential, is exactly
\[
\frac12\left[\prod_j(1-u_j)^{-1}+\prod_j(1+u_j)^{-1}\right]
-\frac12\left[\prod_j(1-u_j)^{-1}-\prod_j(1+u_j)^{-1}\right]
=\prod_j(1+u_j)^{-1}.
\]
In particular this difference is analytic at \(s=0\), and its value there is \(2^{-m}\).

**4. Vertex localization and extraction of the constituent difference.** Apply Brion's exponential lattice-point cone identity to \(qQ_m\). For every integral vertex \(v\), its cone contribution is \(e^{q\langle v,s\rangle}\) times a meromorphic factor independent of the parity of \(q\), so all such contributions cancel when one subtracts the symbolic even and odd constituent expressions at the same formal variable \(t\). The only remaining term is the fractional-vertex difference in Step 3, multiplied by \(e^{(t/2)\sum_i s_i}\). Applying the commuting constant-coefficient differential operator \(\prod_i W_a(\partial_{s_i})\), then evaluating at \(s=0\), reproduces the weight \(\prod_i W_a(y_i)\) and yields the displayed exact formula for \(D_{m,a}(t)\). Individual vertex cones need not be regular at \(s=0\); their parity **difference** is regular, so this evaluation is legitimate. Polynomiality of constituent expressions follows as well by cancellation of Laurent principal parts for infinitely many dilations in each parity class.

**5. Exact degree and sharpness.** The differential operator has total order \(m(a-1)\), with top term \(\prod_i\partial_{s_i}^{a-1}/((a-1)!)^m\). The only contribution of degree \(m(a-1)\) in \(t\) occurs when all top-order derivatives hit \(e^{(t/2)\sum_i s_i}\). The remaining logistic product then contributes its value \(2^{-m}\) at \(s=0\). Thus the coefficient of the top power is
\[
\frac{2^{-m}2^{-m(a-1)}}{((a-1)!)^m}=\frac{1}{2^{ma}((a-1)!)^m},
\]
which is strictly positive. All higher powers vanish by the differential-order bound. Since the ambient rational-vertex denominator is \(2\), rational Ehrhart theory ensures quasiperiod at most \(2\); the nonzero difference excludes quasiperiod \(1\), proving exact period \(2\) and the asserted coefficient-boundary law. For \(a=1\), the weight operator is the identity, leaving constant \(2^{-m}\).

## Verification
Run `python3 checker.py` with Python 3 and SymPy installed. The checker independently evaluates the lattice-point counts by weighted cyclic transfer-matrix traces and, for smaller parameters, by explicit enumeration of all original block-coordinate vectors. It interpolates both constituent polynomials and separately evaluates the analytic logistic differential expression in a truncated exact-rational multivariate series. The following cases agree exactly: \((m,a)=(3,1),(5,1),(7,1),(3,2),(5,2),(3,3)\). Exact leading coefficients and degrees match the theorem. Example formulas are
\[
D_{3,1}(t)=\frac18,\qquad D_{5,1}(t)=\frac1{32},\qquad
D_{3,2}(t)=\frac{(2t+5)(t^2+5t+7)}{128},
\]
\[
D_{5,2}(t)=\frac{(2t+5)(2t^4+20t^3+80t^2+150t+115)}{4096}.
\]
Finite tests corroborate the proof and do not establish the universally quantified conclusion by themselves.

## Relationship to prior work
Jiang, Yang, and Zhong, *Transfer Matrices and Ehrhart Theory for Path and Cyclic Block Polytopes* (first public preprint July 24, 2026, arXiv:2607.22008), prove that odd cyclic block polytopes have denominator exactly two and Ehrhart quasipolynomial period **dividing** two; this result determines the **minimal** period and exact degree and leading coefficient of its parity discrepancy. The accessible source abstract does not assert those stronger conclusions, although priority must remain provisional because the complete manuscript was not available for direct inspection.

Hamano, Hibi, and Ohsugi, *Ehrhart Series of Fractional Stable Set Polytopes of Finite Graphs* (arXiv:1603.09613, Annals of Combinatorics 22 (2018)), give a general numerator formula for scalar fractional stable-set polytopes and tables for odd cycles. Their formulas include the scalar case \(a=1\) but do not directly supply the weighted block-size degree law for all \(a\). The pertinent proof, theorem and examples were inspected in Ginji Hamano's publicly available 2018 doctoral thesis, Chapter 3, Section 3.3, pages 45–47. General period-collapse theory, such as Woods (2005), provides methodology rather than this family-specific exact discrepancy.

## Limitations
The theorem covers equal block sizes and **odd** cycles only. No coefficientwise positivity claim is made for the full difference \(D_{m,a}(t)\) outside its leading coefficient. The primary 2026 source could be assessed only through its public abstract and secondary technical description; the historical-priority comparison therefore retains risk of an equivalent unpublished or unindexed presentation. Brion's cone identity is a standard external theorem used as an exact algebraic localization step, not an independently formalized proof assistant certificate.

## References
Jiang, Xinru; Yang, Shuai; Zhong, Yueming (2026). *Transfer Matrices and Ehrhart Theory for Path and Cyclic Block Polytopes*. arXiv:2607.22008; initially public July 24, 2026.

Hamano, Ginji; Hibi, Takayuki; Ohsugi, Hidefumi (2018). *Ehrhart Series of Fractional Stable Set Polytopes of Finite Graphs*. Annals of Combinatorics 22, 563–573; arXiv:1603.09613. Full relevant text in Hamano, *Convex polytopes of finite graphs and Ehrhart series*, Osaka University doctoral thesis (2018), Chapter 3, Section 3.3, pages 45–47.

Woods, Kevin (2005). *Computing the Period of an Ehrhart Quasi-Polynomial*. Electronic Journal of Combinatorics 12(1), R34. DOI:10.37236/1931.

Brion, Michel (1988). *Points entiers dans les polyèdres convexes*. Annales scientifiques de l'École Normale Supérieure 21, 653–663.
