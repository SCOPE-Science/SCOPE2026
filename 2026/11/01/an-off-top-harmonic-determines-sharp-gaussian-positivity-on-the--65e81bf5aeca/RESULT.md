# An off-top harmonic determines sharp Gaussian positivity on the 462-vertex odd graph

## Finding

Let \(X\) be the set of five-element subsets of an eleven-element set. The *odd graph* \(O_6=KG(11,5)\) joins two members precisely when they are disjoint. Write \(d\) for its unweighted shortest-path metric and \(D_p=(d(A,B)^p)_{A,B\in X}\), with \(0^0=0\). Define \(\alpha\) to be the unique positive solution of
\[
2-2\cdot2^\alpha-7\cdot3^\alpha-2\cdot4^\alpha+8\cdot5^\alpha=0.
\]
Then \(0.355<\alpha<0.356\), more precisely \(\alpha\approx0.355636232374143\). For every \(p\ge0\),
\[
D_p\text{ is conditionally negative semidefinite}
\quad\Longleftrightarrow\quad0\le p\le\alpha
\quad\Longleftrightarrow\quad
\exp(-tD_p)\text{ is positive semidefinite for every }t>0.
\]
The exponential is entrywise. For every admissible exponent and every fixed \(t>0\), this Gaussian kernel is strictly positive definite. For every \(p>\alpha\), it is indefinite for all sufficiently small positive \(t\).

At \(p=\alpha\), the centered powered-distance form has nullity exactly \(165\) on the \(461\)-dimensional zero-sum space; the minimum Euclidean dimension for realizing \(d(A,B)^\alpha\) as squared distances is therefore exactly \(296\). Below the threshold, that dimension is \(461\). The *fourth* nonconstant Johnson harmonic is the unique zero mode at the threshold, whereas the top (fifth) harmonic remains strictly negative: the endpoint is not controlled by the top radial harmonic.

## Assumptions and scope

All assertions concern the canonical graph \(KG(11,5)\), with its graph metric and exactly \(462=\binom{11}{5}\) vertices. Conditional negative semidefiniteness means \(u^\top D_pu\le0\) for every real \(u\) with \(\sum_Au_A=0\). At \(p=0\), each off-diagonal entry of \(D_0\) is \(1\). The claim is exact for every real \(p\ge0\); the displayed decimal for \(\alpha\) is explanatory, not a certificate.

## Proof

**1. Distance and adjacency harmonics.** If \(s=|A\cap B|\), then
\[
d(A,B)=\min\{2(5-s),2s+1\}.
\]
Indeed, two disjointness steps can replace at most one member of a five-set, and every such replacement is realized because the ground set has eleven elements; this gives minimal even-walk length \(2(5-s)\). For an odd walk, finish at a neighbor \(T\) of \(B\). A five-set \(T\) disjoint from \(B\) can meet \(A\) in at most \(5-s\) elements, and that maximum is attainable; hence its minimal odd-walk length is \(2s+1\). All minimal walks may be made paths by erasing loops. The five nonzero distance classes correspond respectively to intersection sizes \(0,4,1,3,2\).

Write \(A_i\) for the zero-one matrix of graph-distance \(i\), where \(A_0=I\) and \(A_1\) is the graph adjacency matrix. Elementary counting of neighbors in each distance class gives the intersection array
\[
\{b_0,b_1,b_2,b_3,b_4;c_1,c_2,c_3,c_4,c_5\}
=\{6,5,5,4,4;1,1,2,2,3\}.
\]
With \(b_5=c_0=0\) and \(a_i=6-b_i-c_i\), the resulting exact recurrence is
\[
A_1A_i=b_{i-1}A_{i-1}+a_iA_i+c_{i+1}A_{i+1}
\quad(0\le i\le5),
\]
where absent boundary terms are zero. These relations also follow directly by multiplying the intersection matrices, as independently checked in the accompanying script.

For each \(j\in\{0,1,2,3,4,5\}\), the standard Boolean inclusion-space filtration gives an adjacency eigenspace of dimension
\[
m_j=\binom{11}{j}-\binom{11}{j-1}
\]
(with \(\binom{11}{-1}=0\)), on which \(A_1\) has eigenvalue \(\theta_j=(-1)^j(6-j)\). To see the eigenvalue rather than merely invoke the known Kneser spectrum, let \(f_T(A)=\mathbf1_{\{T\subseteq A\}}\) for a \(j\)-set \(T\). Summing over five-set neighbors disjoint from \(A\) yields
\[
(A_1f_T)(A)=(6-j)\mathbf1_{\{A\cap T=\varnothing\}}
=(6-j)\sum_{R\subseteq T}(-1)^{|R|}f_R(A).
\]
Thus the operator acts by \((-1)^j(6-j)\) modulo lower inclusion degree. The inclusion matrices have full row rank through degree five (the standard real Boolean-lattice rank identity), so the quotient dimensions are \(m_j\); the symmetric adjacency matrix then diagonalizes orthogonally. The recurrence for \(A_i\) gives its eigenvalue on each harmonic as a polynomial in \(\theta_j\).

The resulting complete radial eigenvalue table is as follows. Each row lists the coefficients \((e_{j,1},\ldots,e_{j,5})\) of \(\lambda_j(p)=\sum_{i=1}^{5}e_{j,i}i^p\). The final column is the multiplicity.

| Harmonic \(j\) | Coefficients | Multiplicity |
|:--:|:--|--:|
| 0 | \((6,30,75,150,200)\) | 1 |
| 1 | \((-5,19,-35,40,-20)\) | 10 |
| 2 | \((4,10,10,-5,-20)\) | 44 |
| 3 | \((-3,3,3,-12,8)\) | 110 |
| 4 | \((2,-2,-7,-2,8)\) | 165 |
| 5 | \((-1,-5,5,10,-10)\) | 132 |

For example, \(A_2=A_1^2-6I\), then \(A_3=(A_1A_2-5A_1)/2\); continuing the recurrence produces every entry displayed. The multiplicities sum to \(462\). The constant eigenvalue \(\lambda_0(p)\) is positive for \(p\ge0\).

**2. The exact critical crossing.** The fourth nonconstant eigenvalue is
\[
F(p):=\lambda_4(p)=2-2\cdot2^p-7\cdot3^p-2\cdot4^p+8\cdot5^p.
\]
For \(p\ge0\), dividing its derivative by \(5^p\) gives
\[
5^{-p}F'(p)=8\log5
-2\log2(2/5)^p-7\log3(3/5)^p-2\log4(4/5)^p
\ge\log\frac{5^8}{2^6 3^7}>0.
\]
The last inequality is the exact integer comparison \(390625>139968\). Moreover \(F(0)=-1\). The accompanying exact rational-power certificate proves \(F(71/200)<0<F(89/250)\); hence \(F\) has exactly one root \(\alpha\), lying strictly between these rational numbers.

**3. Strict negativity of every other nonconstant harmonic at the crossing.** For each integer base \(b=2,3,4,5\), the accompanying certificate constructs rational bounds on \(b^{71/200}\) and \(b^{89/250}\), and certifies them by integer-power comparisons only. Monotonicity of \(b^p\) extends these bounds to every \(p\in[71/200,89/250]\). Applying the appropriate sign to each coefficient in the displayed spectral table produces strict rational upper bounds \(\lambda_j(p)<0\) for \(j=1,2,3,5\) throughout this interval. In particular, the checker proves rational enclosures with upper endpoints below \(-2.26,-12.00,-0.16,-1.32\), respectively. No floating-point evidence is needed for these four strict inequalities. Thus the only zero eigenvalue of \(D_\alpha\) is \(\lambda_4(\alpha)\), of multiplicity \(165\); every other nonconstant eigenvalue is negative.

**4. All exponents and Gaussian kernels.** Schoenberg's theorem identifies conditional negative semidefiniteness of \(D_p\) with positive semidefiniteness of \(\exp(-tD_p)\) for every positive \(t\). Since \(D_\alpha\) is conditionally negative semidefinite, all \(D_p\) with \(0<p\le\alpha\) are likewise conditionally negative semidefinite by the standard fractional-power closure of negative-type kernels (apply the integral representation of \(z^\gamma\) for \(0<\gamma\le1\) to \(z=d^\alpha\)); \(D_0=J-I\) is immediate. Moreover, for \(0<p<\alpha\), the integral is **strict** on every nonzero zero-sum vector because \(e^{-tD_\alpha}\) is strictly positive definite for each \(t>0\) (proved below); therefore \(D_p\) has no nonconstant null modes below the endpoint. For \(p>\alpha\), strict increase of \(F(p)\) gives a positive eigenvalue on a zero-sum eigenspace, so negative type fails. Its quadratic form also makes the Gaussian indefinite for sufficiently small \(t>0\) by the expansion \(e^{-td^p}=1-td^p+O(t^2)\).

Finally, finite negative-type metrics have squared-Euclidean realizations with centered Gram matrix \(-\tfrac12 HD_pH\), where \(H=I-J/462\). Its rank is \(461\) below the threshold and \(461-165=296\) at the threshold. All distances between distinct vertices remain positive, so their realized Euclidean points are distinct. A Gaussian of squared Euclidean distances on pairwise distinct finite points is strictly positive definite for every positive bandwidth (e.g., by the positive Gaussian Fourier integral and linear independence of distinct exponentials). This also covers the discrete metric at \(p=0\).

## Verification

Run `python3 check_odd6.py` with Python 3 and NumPy. It builds the \(462\)-vertex Kneser graph, independently computes all graph distances by breadth-first search, checks every pair against the intersection formula, verifies all distance-class matrix recurrences by integer matrix multiplication, reproduces each row of the spectral table from the polynomial recurrence, and compares direct symmetric-matrix eigenvalues with the table at three exponents.

The exact critical check does **not** rely on the numerical eigensolver. It uses the rational brackets \(71/200\) and \(89/250\), certified integer comparisons for each exponential \(b^{a/c}\), and rational interval arithmetic to establish the signs in steps 2–3. This finite certificate plus the analytic monotonicity and Schoenberg argument proves the statement for **every real** \(p\ge0\). Computations are reproducibility checks and finite exact sign certificates, not a claim of a computer proof for arbitrary parameters.

## Relationship to prior work

Murugan's work on generalized roundness of vertex-transitive graphs supplies a general characterization by zeros of distance-power determinants, but does not identify the critical harmonic or exact exponent for \(KG(11,5)\). Aalipour and collaborators establish the Kneser/Johnson association-scheme distance spectra and the distance formula, including the ordinary \(p=1\) case. Those general algebraic ingredients explain why the radial spectrum is computable, but they do not resolve which of the five nonconstant powered-distance branches first vanishes or establish a sharp all-bandwidth Gaussian positivity frontier. Here the obstructing level is \(j=4\), not the top \(j=5\), and a certified strict comparison proves the distinction. The table and root should not be mistaken for a new association-scheme construction.

## Limitations

This is an exact theorem for the one canonical odd graph \(O_6\), not an assertion that harmonic level four controls all larger odd graphs. The first root has no claimed elementary radical form, and decimal values are not proof. The originality assessment is bounded by the accessible primary literature; an equivalent older calculation using Eberlein eigenvalues and generalized roundness may exist. Independent mathematical validation has not been performed.

## References

1. M. K. Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657, first posted 2011-12-23, especially Theorem 3.1 and Sections 2–4. https://arxiv.org/abs/1112.5657
2. G. Aalipour et al., *On the distance spectra of graphs*, arXiv:1509.01196, first posted 2015-09-03, especially Section 3.2, Theorems 3.9–3.10 and Remark 3.11. https://arxiv.org/abs/1509.01196
3. I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society 44 (1938), 522–536 (classical negative-type/Gaussian correspondence; cited as background).
