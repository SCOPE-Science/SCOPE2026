# Global magnitude stability for complete quadratic Fourier layers on the torus

## Finding

Let \(n\ge5\), \(N=\binom n2\), and let \(P(z)=\sum_{i<j}a_{ij}z_i z_j\) on the probability Haar torus \(\mathbb T^n\), with arbitrary complex coefficients. Set \(x_{ij}=|a_{ij}|^2\), \(S=\sum_{i<j}x_{ij}\), and write \(C_n=(6n^2-22n+22)/(n(n-1))\) for the uniform-coefficient fourth-moment ratio. The quantitative result is
\[
 C_nS^2-\int_{\mathbb T^n}|P|^4\,dz
 \ \ge\ \min\!\left\{3,1+\frac{(n-3)(n-4)}{n-1}\right\}
 \sum_{i<j}(x_{ij}-S/N)^2 .
\]
Thus the global deficit controls dispersion of the squared coefficient magnitudes with coefficient \(3/2\) at \(n=5\), \(11/5\) at \(n=6\), and \(3\) for every \(n\ge7\). The coefficient is not asserted optimal. The sharp unquantified norm and factorized equality phases are context, not separate new claims here.

## Assumptions and scope

The support is the complete degree-two square-free layer on the complex torus, with probability Haar measure. The inequality is homogeneous and includes coefficients equal to zero, including \(S=0\). It estimates squared magnitudes, not distances between phases. No sign-cube or incomplete-graph analogue is asserted.

## Proof

Write \(M=\int|P|^4\), and regard the coefficient indices as edges of the complete graph. In the square of \(P\), there is one unordered pair of edges for each sum of two exponent vectors, except for the character consisting of four distinct indices. For such a quadruple there are three perfect matchings. If their coefficient products are \(X,Y,Z\), Parseval therefore gives
\[
 M=2S^2-\sum_e x_e^2 +8\sum_{\text{quadruples}}\operatorname{Re}(X\overline Y+X\overline Z+Y\overline Z).
\]
Denote the last term by \(T\). The matching magnitudes \(p,q,r\) satisfy \(pq+qr+rp\le p^2+q^2+r^2\), so \(T\le8\sum_{e\perp f}x_e x_f\) over unordered disjoint edge pairs. A complementary bound uses each of the three four-cycles in the quadruple: its product of four edge magnitudes is at most one quarter the sum of the four adjacent-edge products \(x_e x_f\) along the cycle, by AM–GM on the two pairs of opposing such products. Each adjacent pair on the quadruple occurs in exactly one of its three four-cycles. Over the whole graph an adjacent pair belongs to \(n-3\) quadruples; hence \(T\le2(n-3)\sum_{e\sim f}x_e x_f\) over unordered distinct pairs meeting in a vertex. Both estimates are exact on constant positive coefficients.

Let \(L\) be the adjacency matrix for adjacent pairs and \(K=J-I-L\) that for disjoint pairs in edge coordinates, with \(J\) all ones. Combine the bounds, with disjoint-pair weight \(\alpha=(n-4)/(n-1)\), to obtain \(M\le2S^2+x^{\mathsf T}Hx\), where
\[
 H=-I+4\alpha K+(n-3)(1-\alpha)L.
\]
For the unsigned vertex-edge incidence matrix \(B\), \(B^{\mathsf T}B=L+2I\) and \(BB^{\mathsf T}=(n-2)I+J\) (the second identity is in vertex coordinates). Thus the eigenvalues of \(L\) on constants, on \(B^{\mathsf T}(\mathbf 1^\perp)\), and on \(\ker B\) are \(2(n-2), n-4, -2\), respectively. On the latter two spaces \(K=-I-L\). It follows that the eigenvalues of \(H\) are
\[
 h_0=-1+2(n-2)(n-3),\qquad
 h_1=-1-\frac{(n-3)(n-4)}{n-1},\qquad h_2=-3.
\]
Writing \(y=x-(S/N)\mathbf 1\) eliminates the cross term. The constant term is \((2+h_0/N)S^2=C_n S^2\), attained by all equal positive coefficients; on \(\mathbf1^\perp\) the eigenvalues give the claimed remainder. This proof does not assume that any coefficient is nonzero.

## Relationship to the sharp norm

The indexed *Sharp fourth moments and phase rigidity of all square-free Fourier layers* ([RESULT.md](https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-sharp-fourth-moments-and-phase-rigidity-of-all-square-free-fouri--49c8d2da27e1/RESULT.md), Finding and Proof §§2–4) focuses on \(k\ge3\); its proof and scope discussion include degree two as context. Substituting \(k=2\) gives the same sharp normalized constant and the same factorized phases. The catalogue date alone does not resolve historical priority.

The balancing proof there also supplies a unit-coefficient remainder: at the doubled-monomial exponent in its pair-averaging step the gain is at least \((b_U^2-c_U^2)^2/2\), exactly the loss of squared dispersion at that coefficient pair. Iterating coordinate transpositions by averaging squared magnitudes converges to the uniform vector (the common fixed subspace of those orthogonal averaging projections is the constants, by transitivity on two-subsets). Summing the one-step gains gives coefficient \(1\). The remainder above gives a larger global coefficient for every \(n\ge5\) by using both adjacent and disjoint edge pairs and their different incidence eigenspaces. The related complete quadratic Walsh result is for real sign variables, whose extra exponent collisions change the fourth-moment form.

## Reproducibility and limitations

The supplied `checker.py` and `checker_output.txt` remain finite corroboration of the convolution and spectral formulas and the inequality in dimensions 4–9; dimension four is an ancillary check, not part of the new claim. The proof handles all dimensions in the stated range. No optimal stability coefficient, quantitative phase remainder, extension to another Fourier layer, or definitive historical priority is asserted.
