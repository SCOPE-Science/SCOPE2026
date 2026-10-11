# Strict Schatten rearrangement for four-site weighted-shift resolvents

## Finding
Let \(N_{a,b,c}\) be the \(4\times4\) weighted nilpotent shift with successive superdiagonal entries \(a,b,c\in\mathbb C\setminus\{0\}\), and set \(R_{a,b,c}=(I-N_{a,b,c})^{-1}\). Fix the multiset of the three positive magnitudes \(\{|a|,|b|,|c|\}\), and permute the weights among the three edges. For every real \(p>0\), the spectral moment
\[
\mathcal M_p(a,b,c)=\operatorname{tr}|R_{a,b,c}|^p=\sum_{j=1}^4s_j(R_{a,b,c})^p
\]
is strictly increasing as the magnitude of the *central* weight increases, provided the two compared central magnitudes are distinct. It depends on a permutation only through the magnitude of its central weight. Consequently, putting a largest-magnitude weight in the middle maximizes \(\mathcal M_p\), while putting a smallest-magnitude weight in the middle minimizes it, simultaneously for all \(p>0\). For \(p\ge1\) the same statement applies to the Schatten norm \(\|R_{a,b,c}\|_{S_p}\); for \(0<p<1\) it applies to the stated positive spectral moment, without claiming it is a norm.

For strictly ordered central magnitudes, the ordered squared singular values display the contrasting pattern: the first and third increase strictly, whereas the second and fourth decrease strictly. Thus this is a *power-moment ordering*, not coordinatewise singular-value ordering. At the operator-norm endpoint \(p=\infty\), the largest singular value also increases strictly. For paths with at most two edges (matrices of order at most three), reversing the edges preserves all singular values, so four sites are the first dimension with a nontrivial placement distinction.

## Assumptions and scope
All three edge weights are nonzero complex numbers. Their phases do not matter: a diagonal unitary conjugates the weighted shift to the shift with successive positive entries \(|a|,|b|,|c|\). Only the relative placement of a fixed multiset of magnitudes is varied. No smallness condition is needed because the shift is nilpotent and \(I-N_{a,b,c}\) is always invertible. The claim concerns finite four-dimensional Hilbert-space singular values; no assertion is made for arbitrary unitary-invariant norms or longer paths.

## Proof
After removing phases, assume \(a,b,c>0\). The resolvent is exactly
\[
R_{a,b,c}=\begin{pmatrix}1&a&ab&abc\\0&1&b&bc\\0&0&1&c\\0&0&0&1\end{pmatrix}.
\]
Put \(x=a^2\), \(y=b^2\), and \(z=c^2\). The four eigenvalues \(\lambda_1>\lambda_2>\lambda_3>\lambda_4>0\) of \(R_{a,b,c}^*R_{a,b,c}\) have characteristic polynomial
\[
P_A(t)=t^4-A t^3+B t^2-Ct+1,
\]
where direct expansion of the elementary symmetric functions gives
\[
\begin{aligned}
A&=4+x+y+z+xy+yz+xyz,\\
B&=6+2(x+y+z)+xy+xz+yz,\\
C&=4+x+y+z.
\end{aligned}
\]
The constant term is one because \(\det R_{a,b,c}=1\). Equivalently, \(C=\operatorname{tr}((R^*R)^{-1})\), since \(R^{-1}=I-N\). For the middle coefficient, write \(J=(R^*R)^{-1}=(I-N)(I-N)^*\): its diagonal is \(1+x,1+y,1+z,1\), and the squared magnitudes of its three nonzero off-diagonal entries are \(x,y,z\). Since \(\det J=1\), the second elementary symmetric function is the same for the eigenvalues of \(J\) and \(J^{-1}\) in dimension four. The sum of the two-by-two principal minors of \(J\) is precisely \(\sum_{i<j}J_{ii}J_{jj}-(x+y+z)=6+2(x+y+z)+xy+xz+yz\), proving the displayed formula for \(B\). For a fixed multiset \(\{x,y,z\}\), only \(A\) changes with edge placement: its variable term is the central squared magnitude times the sum of the two outer squared magnitudes. When central values \(x<y\) are exchanged, with the remaining value \(z>0\), the change in \(A\) is \(z(y-x)>0\). Thus central-magnitude ordering and \(A\)-ordering agree strictly.

We show that every positive spectral moment increases strictly with \(A\) between any two such realizable values. The inverse Gram matrix
\[
(R^*R)^{-1}=(I-N)(I-N)^*
\]
is positive definite and, after a transpose if necessary, an irreducible real symmetric tridiagonal matrix: its three off-diagonal entries have nonzero magnitudes \(a,b,c\). Such a Jacobi matrix has simple eigenvalues, so the four positive roots of \(P_A\) at each realizable endpoint are distinct.

For intermediate values of \(A\), positivity and simplicity of the four roots persist. Indeed, for \(t>0\) the equation \(P_A(t)=0\) is equivalent to
\[
A=H(t):=t+\frac B t-\frac C{t^2}+\frac1{t^3}.
\]
The critical points of \(H\) are positive roots of \(t^4-Bt^2+2Ct-3\). Descartes' sign rule bounds their number by three. Since each realizable endpoint has four distinct positive intersections with its horizontal level, Rolle's theorem forces exactly three distinct positive critical points, in the order local minimum, local maximum, local minimum. Four positive simple intersections occur precisely for levels strictly above both local minima and strictly below the local maximum. This set of levels is an interval. Hence all values of \(A\) between the two realizable endpoints have four distinct positive roots.

With \(q=p/2>0\), implicit differentiation of \(P_A(\lambda_j)=0\) gives
\[
\frac{d\lambda_j}{dA}=\frac{\lambda_j^3}{P_A'(\lambda_j)},
\qquad
\frac d{dA}\sum_{j=1}^4\lambda_j^q
=q\sum_{j=1}^4\frac{\lambda_j^{q+2}}{\prod_{k\ne j}(\lambda_j-\lambda_k)}.
\]
The last sum is the third divided difference of the function \(f(t)=t^{q+2}\) on the four positive nodes. The Hermite–Genocchi integral formula makes it strictly positive because
\[
f^{(3)}(t)=q(q+1)(q+2)t^{q-1}>0 \qquad(t>0).
\]
Thus \(\sum_j\lambda_j^q=\operatorname{tr}|R|^p\) is strictly increasing in \(A\), proving the stated full-exponent ordering and its equality cases. Since \(P_A'(\lambda_j)\) alternates in sign as \(j=1,2,3,4\), the individual squared singular values change in the alternating directions claimed above. In particular \(\lambda_1\) increases, proving the operator-norm endpoint.

For matrices of order three, the two possible edge placements are related by transpose and reversal of the coordinate order, both of which preserve singular values. This establishes the minimal-dimensional observation.

## Verification
The accompanying standalone `verify.py` uses only the Python standard library and exact rational arithmetic. Run `python3 verify.py` from the directory containing the file. It checks the Gram characteristic-polynomial coefficients, their permutation invariance except for \(A\), and their strict central-weight ordering on \(216\) rational triples; it prints `WEIGHTED_SHIFT_SCHATTEN_REARRANGEMENT_EXACT_OK 216`. These finite checks do not prove the continuum-in-\(p\) claim; that part is established by the polynomial-level interpolation and positive divided differences proved above.

## Relationship to prior work
Chang and Wang study permutations maximizing the *numerical radius of weighted shift operators*, which is a different optimization functional applied to the shift itself. The present comparison concerns the singular-value power sums of its **inverse perturbation** \((I-N)^{-1}\), in which the complete four-dimensional characteristic polynomial has only one placement-dependent coefficient. Li, Gu and Parlett's early open-access work gives accurate bidiagonal singular-value algorithms, without classifying edge-weight placement. Higham's treatment of inverse triangular-matrix norms provides general inversion bounds and the bidiagonal inverse formula, but does not establish this strict simultaneous Schatten rearrangement. These sources motivate the placement question and its numerical-linear-algebra significance, without implying the proved comparison. The first source's publicly indexed introduction and main-theorem sections were materially inspected; its complete printable article was not accessible, so uninspected historical coverage cannot be ruled out.

## Limitations
No claim is made that all individual singular values increase, that all Ky Fan sums increase, or that the same central-edge rule holds in dimensions above four. The strict order requires distinct magnitudes at the central edge and nonzero remaining magnitudes. The proof establishes the result within the stated elementary finite-dimensional model; it does not establish historical priority against every unindexed publication.

## References
1. C.-T. Chang and K.-Z. Wang, *Maximizing numerical radii of weighted shifts under weight permutations*, Journal of Mathematical Analysis and Applications **394** (2012), 592–602. DOI: https://doi.org/10.1016/j.jmaa.2012.04.039 (bibliographic publication date verified as 2012-10-15).
2. N. J. Higham, *Bounds for the Norm of the Inverse of a Triangular Matrix* (2021-03-30), https://nhigham.com/2021/03/30/bounds-for-the-norm-of-the-inverse-of-a-triangular-matrix/.
3. S. Li, M. Gu, and B. N. Parlett, *An improved dqds algorithm*, arXiv:1209.5462, first publicly submitted 2012-09-25 00:31:17 UTC, https://arxiv.org/abs/1209.5462.
