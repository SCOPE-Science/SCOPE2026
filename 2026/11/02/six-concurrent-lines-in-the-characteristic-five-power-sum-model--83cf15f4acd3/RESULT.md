# Six concurrent lines in the characteristic-five power-sum model of Bring’s curve

## Finding
Let \(\mathcal B\) be the subscheme of \(\mathbb P^4_{\mathbb Z}\) given by the three homogeneous power sums
\[
P_1=\sum_{i=0}^{4}X_i,\qquad P_2=\sum_{i=0}^{4}X_i^2,\qquad P_3=\sum_{i=0}^{4}X_i^3.
\]
Its characteristic-zero generic fiber is the classical canonical complete-intersection model of Bring’s smooth genus-four curve. The fiber \(\mathcal B_{\mathbb F_5}\) is **exactly the reduced union of six distinct projective lines over \(\mathbb F_5\)**. They all meet at the single point
\[
P=[1:1:1:1:1].
\]
There are no other singular points. At \(P\), the six branches have different tangent directions spanning a three-dimensional tangent space, and the local normalization defect is
\[
\delta_P=9.
\]
The coordinate-permutation action of \(S_5\) on the six components is transitive, with stabilizer \(\operatorname{AGL}_1(\mathbb F_5)\) of order \(20\). Consequently it is the degree-six action of \(S_5\) on its Sylow-five subgroups. For every extension field \(\mathbb F_q/\mathbb F_5\),
\[
\#\mathcal B_{\mathbb F_5}(\mathbb F_q)=6q+1.
\]

## Assumptions and scope
All claims concern **the specified integral power-sum equations and their scheme-theoretic characteristic-five fiber**, not the stable reduction of an arbitrary genus-four curve over a local field. Write \(k=\overline{\mathbb F}_5\). The affine-local embedding dimension is three; the singularity is not an ordinary planar sextuple point. The statements about components and singularities hold after extending the base field to \(k\).

## Proof
**1. Reduction to a homogeneous complete intersection of two equations in three variables.** Every geometric point in the characteristic-five fiber with all five coordinates equal represents \(P\), since \(5=0\). The point \(P\) lies on the three hypersurfaces. Write the fiber in the affine chart \(X_4=1\) using
\[
X_0=1+a,\quad X_1=1+b,\quad X_2=1+c,\quad X_3=1-a-b-c.
\]
The linear power sum vanishes identically. Direct expansion in characteristic five gives
\[
P_2=2Q,\quad Q=a^2+b^2+c^2+ab+ac+bc,\qquad
P_3=-3(a+b)(a+c)(b+c).
\]
These are homogeneous in \((a,b,c)\). Their common projectivized zero scheme in \(\mathbb P^2_k\) describes the possible directions of lines through \(P\) in the chart.

**2. Six transverse directions over the prime field.** The symmetric matrix of \(2Q\) is
\[
\begin{pmatrix}2&1&1\\1&2&1\\1&1&2\end{pmatrix},
\]
with determinant \(4\) in \(\mathbb F_5\); hence \(Q=0\) is a smooth irreducible conic. The cubic is the union of the three distinct lines \(a+b=0\), \(a+c=0\), and \(b+c=0\), none a component of this conic. Every direction is a permutation of the five distinct elements \((0,1,2,3,4)\) modulo projective affine rescaling \(v\sim \lambda v+\mu\mathbf1\), with \(\lambda\in\mathbb F_5^*\) and \(\mu\in\mathbb F_5\). A normalized list with fifth coordinate zero and first coordinate one is
\[
(1,2,3,4,0),\ (1,2,4,3,0),\ (1,3,2,4,0),\
(1,3,4,2,0),\ (1,4,2,3,0),\ (1,4,3,2,0).
\]
Each vector satisfies all three power sums because the power sums of \(\mathbb F_5\) of degrees one, two and three vanish. The six directions are distinct. Bézout's theorem gives total intersection degree six for the conic and cubic; therefore the list exhausts their intersection and all six points are reduced and transverse.

**3. Global decomposition, scheme structure and the unique singular point.** For any listed direction \(v\), set
\[
L_v=\{[s\mathbf1+tv]:[s:t]\in\mathbb P^1_k\}.
\]
All three power sums vanish identically on \(L_v\): after the binomial expansion every term is a product of a binomial coefficient and a power sum of \(1\) or \(v\). In characteristic five, \(\sum_i1=0\) and \(\sum_i v_i^j=0\) for \(1\leq j\leq 3\). Thus the six distinct lines lie in the fiber. Conversely, in the affine chart \(X_4=1\), the ideal is \((Q,(a+b)(a+c)(b+c))\), which is reduced because the conic meets the cubic transversely in six distinct projective points; it is the reduced affine cone over those points. At any point with \(X_4=0\), some other coordinate is nonzero; because the six projective lines already have total degree six, and the defining scheme is a \((1,2,3)\) pure one-dimensional complete intersection of degree six, no additional component or embedded point occurs. The lines have independent directions modulo \(\mathbf1\), and meet pairwise only at \(P\). Hence the fiber is the claimed reduced union and \(P\) is its only singular point.

**4. Local normalization and genus.** At \(P\) the completed local ring is the completed graded ring \(k[a,b,c]/(Q,(a+b)(a+c)(b+c))\). Its normalization is the direct product of six power-series rings \(k[[t]]\). Because the six points of the projectivized complete intersection are reduced, the degree-\(n\) dimension in the original graded ring is the Hilbert function of a \((2,3)\) complete intersection in three variables:
\[
\sum_{n\ge0}h_nt^n=\frac{(1-t^2)(1-t^3)}{(1-t)^3};\qquad
(h_0,h_1,h_2,h_n\ (n\ge3))=(1,3,5,6).
\]
Each graded piece of the normalization has dimension six, including degree zero. Thus the length of the normalization quotient is
\[
\delta_P=\sum_{n\ge0}(6-h_n)=(6-1)+(6-3)+(6-5)=9.
\]
The arithmetic genus is \(\delta_P-6+1=4\), also matching the standard adjunction genus of the complete intersection of degrees \(2\) and \(3\) in \(\mathbb P^3\).

**5. The exceptional symmetric-group action.** Coordinate permutations preserve the equations and permute the six direction classes. The stabilizer of the class of \(v=(0,1,2,3,4)\) consists exactly of the affine permutations \(r\mapsto\lambda r+\mu\) of \(\mathbb F_5\), of order \(5\cdot4=20\). Therefore the orbit has \(120/20=6\) elements. This affine subgroup normalizes the five-cycle generated by \(r\mapsto r+1\), hence is the normalizer of a Sylow-five subgroup in \(S_5\). Identifying each component with the subgroup whose normalizer stabilizes it yields the asserted exceptional degree-six action.

Because the six lines are all rational over \(\mathbb F_5\) and have precisely one common rational point, inclusion–exclusion gives \(6(q+1)-5=6q+1\) for every \(q=5^m\), \(m\ge1\).

## Verification
Run the accompanying self-contained \(\texttt{verify.py}\) with Python 3. The script uses exact arithmetic modulo five to independently list the six projective direction classes, check the defining power sums, calculate the initial Hilbert function by evaluation ranks, verify the determinant and the full \(S_5\)-stabilizer, and print \(\texttt{VERIFY\_OK}\). The algebraic Bézout/regular-sequence and normalization arguments above establish the geometric assertions for all field extensions, rather than inferring them from a finite enumeration.

## Relationship to prior work
Braden–Northover (2012) present the classical characteristic-zero model, its symmetries and analytic period data. Braden–Disney-Hogg (2023) explicitly set aside extension to positive characteristic. Korchmáros–Lia–Timpanella (2021) analyze the power-sum generalizations **under the positive-characteristic restriction** \(p\ge7\) and \(m\le p-1\); their theorem does not apply when the number of coordinates and characteristic are both five. The present calculation gives the boundary fiber that the smooth positive-characteristic theorems exclude, and its exact local defect and component permutation action. The assertion is limited to this particular integral model; a search that does not locate an earlier equivalent account does not establish absolute novelty.

## Limitations
No claim is made about the minimal regular model, semistable/stable reduction, component multiplicities in any *different* integral model, Jacobian monodromy, or the relative dualizing sheaf. The arithmetic-genus-four and point-count statements concern the reduced projective fiber of these exact equations. Historic accounts not available in searchable form may already describe the six-line degeneration; independent literature audit remains necessary.

## References
1. H. W. Braden and T. P. Northover, *Bring's Curve: its Period Matrix and the Vector of Riemann Constants*, SIGMA **8** (2012), 065; arXiv:1206.6004. https://arxiv.org/html/1206.6004v2 (first public version 2012-06-26).
2. G. Korchmáros, S. Lia, and M. Timpanella, *A generalization of Bring's curve in any characteristic*, arXiv:2112.10886 (2021). https://arxiv.org/abs/2112.10886.
3. H. W. Braden and L. Disney-Hogg, *Bring’s curve: old and new*, European Journal of Mathematics **10** (2024), article 3 (online 2023-12-18). https://doi.org/10.1007/s40879-023-00706-0.
