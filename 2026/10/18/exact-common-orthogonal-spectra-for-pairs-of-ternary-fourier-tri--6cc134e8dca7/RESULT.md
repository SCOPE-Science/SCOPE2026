# Exact common orthogonal spectra for pairs of ternary Fourier triples

## Finding

Let \(d\ge2\), let \(G=\mathbb F_3^d\), and give its character group the standard pairing \(\chi_\xi(x)=\exp(2\pi i\langle x,\xi\rangle/3)\). For two arbitrary, possibly equal, three-element sets \(A_1,A_2\subset G\), call a three-element set \(B\subset G\) a *common orthogonal spectrum* if each of the two matrices \((\chi_\xi(a))_{a\in A_i,\,\xi\in B}\) has pairwise orthogonal columns. Every such matrix is then a scalar multiple of a unitary matrix.

Choose any orderings \(A_i=\{a_i,b_i,c_i\}\), and set
\[
 t_i=a_i+b_i+c_i,\qquad u_i=b_i-a_i,\qquad W=\operatorname{span}_{\mathbb F_3}\{t_1,t_2\},\qquad r=\dim W.
\]
If \(u_1\in W\) or \(u_2\in W\), the number \(\mathcal N(A_1,A_2)\) of common spectra is zero. Otherwise put
\[
 s=\dim\bigl(W+\operatorname{span}\{u_1,u_2\}\bigr)-r\in\{1,2\}.
\]
The exact number of *unordered* common three-frequency spectra is
\[
\boxed{\mathcal N(A_1,A_2)=
\begin{cases}
3^{3d-2r-3},&s=1,\\
6\,3^{3d-2r-6},&s=2.
\end{cases}}
\]
The exponents are nonnegative whenever the corresponding case is possible. This formula is independent of the orderings of either triple.

In particular, in \(G=\mathbb F_3^2\) there are \(84\) three-element sets, and the \(84^2=7056\) ordered pairs have the following exact common-spectrum census: \(4320\) pairs have \(0\) common spectra, \(2592\) have \(3\), \(108\) have \(6\), and \(36\) have \(27\). Thus individual spectrality need not permit simultaneous *orthogonal* exponential sampling: each of the two three-point sets in the following example has its own spectrum, but there is no common one,
\[
A_1=\{(0,0),(1,0),(0,1)\},\qquad
A_2=\{(0,0),(1,1),(2,2)\}.
\]

## Assumptions and scope

The field is \(\mathbb F_3\), not an extension field treated as a single cyclic group. Dimension \(d\) is any integer at least \(2\). All spatial and frequency sets contain exactly three *distinct* points; no weights, repeated points, or approximate orthogonality are allowed. Frequency sets are counted as subsets, without an ordering or quotient by translation. The pairing is the standard nondegenerate bilinear dot product, with counting inner products on each three-point spatial set.

Each vector \(t_i\) is intrinsic to its set: translation by \(v\) changes its sum by \(3v=0\). It vanishes exactly when the triple is an affine line. If an ordering is changed, the class of \(u_i\) modulo \(\operatorname{span}\{t_i\}\) changes at most by sign. Consequently, membership \(u_i\in W\) and the displayed quotient rank \(s\) are well defined.

## Proof

**1. Character-sum rigidity.** Let \(\omega=e^{2\pi i/3}\). Three terms from \(\{1,\omega,\omega^2\}\) sum to zero exactly when each of the three occurs once. For a triple \(A=\{a,b,c\}\), write \(t=a+b+c\) and \(u=b-a\). Because \(3a=0\), the third point is \(c=t+a-u\). Thus, for any \(h\in G\), the three exponents modulo \(3\) of the character evaluations at \(a,b,c\) are
\[
\alpha,\quad \alpha+\langle h,u\rangle,\quad
\alpha-\langle h,u\rangle+\langle h,t\rangle,
\qquad \alpha=\langle h,a\rangle.
\]
They are a permutation of all three residues precisely when
\[
\langle h,t\rangle=0\quad\text{and}\quad\langle h,u\rangle\ne0.
\]
For necessity, distinct exponents have sum zero modulo \(3\), so \(\langle h,t\rangle=0\), while \(\langle h,u\rangle\ne0\) follows because the first two exponents differ. For sufficiency the residues are \(\alpha,\alpha+v,\alpha-v\) with \(v\ne0\), hence distinct. This proves the claimed equivalence without numerical approximation or a classification theorem.

**2. Orthogonality of a three-frequency set.** Two columns indexed by \(\xi\ne\eta\) are orthogonal on \(A_i\) exactly when the character sum for \(h=\xi-\eta\) vanishes. By Step 1, this happens for all three unordered column pairs if and only if the linear functional \(\xi\mapsto\langle t_i,\xi\rangle\) is constant on \(B\), while \(\xi\mapsto\langle u_i,\xi\rangle\) takes the three distinct values of \(\mathbb F_3\) on \(B\). For both spatial sets, the first requirement means that \(B\) lies inside one common fiber of the \(r\) independent linear functionals defining \(W\).

**3. Obstruction.** If \(u_i\in W\), its evaluation is constant on every such fiber, contradicting the requirement that its values on \(B\) be all distinct. Hence no common spectrum exists.

**4. Exact enumeration in the nonobstructed cases.** Suppose \(u_1,u_2\notin W\). The two evaluations descend to nonzero linear functionals on the \((d-r)\)-dimensional quotient determined by fixing the evaluation of \(W\). If their quotient span has dimension \(s=1\), requiring distinct values of the first functional automatically makes the values of the second distinct: over \(\mathbb F_3\) the latter is a nonzero scalar multiple of the former plus a fixed constant. There are \(3^r\) choices for the common evaluation of \(W\); inside each resulting affine fiber, each of the three prescribed values of the first functional has \(3^{d-r-1}\) preimages. Selecting one from each yields \(3^r(3^{d-r-1})^3=3^{3d-2r-3}\) *unordered* spectra.

If \(s=2\), the two quotient functionals are independent. In each of the \(3^r\) fibers of \(W\), each joint evaluation pair in \(\mathbb F_3^2\) has exactly \(3^{d-r-2}\) preimages. The three selected points must have first coordinates \(0,1,2\) and second coordinates in one of their \(3!=6\) permutations. Choosing a representative in each of the corresponding three joint fibers gives \(3^r\cdot6(3^{d-r-2})^3=6\,3^{3d-2r-6}\) spectra. The first coordinate labels the selected points uniquely, so no further division by \(3!\) occurs.

**5. Order invariance.** The ordered differences between points of \(A_i\) are \(u_i\), \(t_i+u_i\), and \(t_i-u_i\), up to sign. Reordering therefore replaces \(u_i\) by \(\pm u_i\) plus a multiple of \(t_i\); the image of each \(u_i\) in \(G/W\) is changed only by a nonzero scalar. All obstruction and rank conditions, and hence the number, are unaffected.

**6. Plane census and sharp incompatibility.** The affine plane \(\mathbb F_3^2\) contains \(\binom93=84\) triples, of which \(4\cdot3=12\) are lines and \(72\) are triangles. The \(72\) triangle sums \(t\ne0\) fall equally into the four projective directions, with \(18\) triangles in each direction, by linear-coordinate symmetry. Every triangle has \(u\) independent of \(t\). Pairs of lines in the same direction number \(4\cdot3^2=36\) and have \(27\) common spectra; line pairs of different directions number \(12^2-36=108\) and have \(6\). For an ordered triangle-line pair, compatibility requires the line direction to differ from the triangle's sum direction. There are \(2\cdot72\cdot9=1296\) such pairs, each with \(3\) common spectra. Triangle pairs with parallel nonzero sums number \(4\cdot18^2=1296\), again each with \(3\). Every other pair is incompatible, so \(7056-36-108-1296-1296=4320\) ordered pairs have none. The displayed example has \(t_1=(1,1)\) and \(u_2=(1,1)\), so it satisfies the Step 3 obstruction. This establishes the counts and incompatibility symbolically, not by extrapolation from finite tests.

## Verification

The accompanying standalone Python program `check.py` implements rank over \(\mathbb F_3\), the displayed formula, and an *independent* exhaustive orthogonality test using only modular character residues. No floating-point comparisons occur. Its output `verification-output.txt` reports a complete test of all \(84^2=7056\) ordered spatial-triple pairs against all \(84\) candidate frequency triples in dimension \(2\), a complete dimension-\(1\) boundary check, and independently sampled pairs in dimensions \(3\) and \(4\) tested against all \(2925\) and \(85320\) frequency triples respectively. The incompatible triangle-line example is checked explicitly. All checks pass. The infinite-dimensional statement follows from Steps 1–5, not the finite tests; Step 6 separately proves the finite plane histogram.

To reproduce: run `python check.py` using Python 3 with only the standard library, from a directory containing the checker. No internet connection, compiled dependency, or private input is required.

## Relationship to prior work

Ferguson, Mayeli, and Sothanaphan (2019), especially their Section 7.1, introduce *simultaneous exponential Riesz bases* and demonstrate nonexistence for sufficiently large families. Their Question 1.8 concerns invertible, not necessarily orthogonal, Fourier restrictions for two sets; the present claim instead classifies **condition-number-one simultaneous orthogonal bases**, with exact counts. Their result that a cyclic group admits common *Riesz* bases does not imply the orthogonality claimed here. Fallon, Kiss, and Somlai (2021), Section 3, develop the finite-group Fourier-vanishing and equidistribution criteria underlying spectral pairs, but do not enumerate common three-character spectra of two arbitrary triples in \(\mathbb F_3^d\). Kiss, Malikiosis, Somlai, and Vizer (2022) establish cyclic squarefree-order spectral/tile results, not pairwise ternary vector-space multiplicities. The new information lies in the quotient-span obstruction, its exact two-case multiplicity, and the complete plane census; the cyclotomic root-sum test itself is classical.

## Limitations

This is a theorem only for three-element sets in elementary Abelian groups of exponent three. It does not classify simultaneous *Riesz* bases, which have weaker invertibility requirements; it makes no claim for cyclic groups of order \(3^d\), unequal-size sampling sets, weighted/redundant frequency designs, or field characteristics other than three. No independent review has been performed. An older result phrased using ternary affine-design coordinates or equivalent Fourier zero-locus conditions could overlap with the counting formula; the comparison reported here is based on inspected accessible primary literature and relevant indexed research records, not exhaustive bibliographic certification.

## References

1. S. Ferguson, A. Mayeli, N. Sothanaphan, *Riesz bases of exponentials and multi-tiling in finite abelian groups*, arXiv:1904.04487 (first public version 2019-04-09), especially Sections 3–4 and 7.1. https://arxiv.org/abs/1904.04487
2. T. Fallon, G. Kiss, G. Somlai, *Spectral sets and tiles in \(\mathbb Z_p^2\times\mathbb Z_q^2\)*, arXiv:2105.10575 (first public version 2021-05-21), especially Sections 1–3. https://arxiv.org/abs/2105.10575
3. G. Kiss, R. D. Malikiosis, G. Somlai, M. Vizer, *Fuglede’s Conjecture Holds for Cyclic Groups of Order pqrs*, Journal of Fourier Analysis and Applications (2022), DOI:10.1007/s00041-022-09972-0. https://doi.org/10.1007/s00041-022-09972-0
