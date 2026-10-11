# The four-by-four Fourier-minor incidence of the ternary affine plane

## Finding
Let \(V=\mathbb F_3^2\), and let \(\omega=e^{2\pi i/3}\). Define the \(9\times9\) Fourier character matrix \(F=(\omega^{a\cdot b})_{a,b\in V}\), with the standard coordinate dot product. For each four-element \(A,B\subset V\), write \(F[A,B]\) for the corresponding \(4\times4\) minor. Call a four-point set a **cap** if it contains no collinear triple, and **line-rich** otherwise. There are exactly \(54\) caps and \(72\) line-rich sets.

The complete type-refined singular-minor incidence is
\[
\begin{array}{c|cc}
& B\text{ line-rich}&B\text{ cap}\\\hline
 A\text{ line-rich}&18&27\\
 A\text{ cap}&36&9
\end{array}
\]
where each entry is the number of sets \(B\) for **each fixed** row set \(A\) of the indicated type. Consequently, *every* four-element row set has exactly \(45\) singular four-column partners and \(81\) nonsingular partners. The symmetric zero/nonzero incidence relation is a \(45\)-regular relation on the \(126\) four-point subsets, with the two affine-geometric types forming an equitable partition with quotient matrix
\[
\begin{pmatrix}18&27\\36&9\end{pmatrix}.
\]
There are exactly \(5670\) singular **ordered** pairs of four-element row and column subsets, and exactly \(10206\) nonsingular ones. The type-by-type singular ordered-pair counts are \(1296,1944,1944,486\), respectively, in the same row/column order. The result counts all positional minors, not merely their sizes.

## Assumptions and scope
The field is exactly \(\mathbb F_3\); no result is asserted for larger finite planes, for cyclic order-nine Fourier matrices, or for arbitrary four-point matrices. A triple of distinct affine points \(a,b,c\in V\) is collinear exactly when \(\det(b-a,c-a)=0\) in \(\mathbb F_3\). An ordered pair \((A,B)\) is declared singular when \(\det F[A,B]=0\) in \(\mathbb C\); no exact-support assertion requiring nonzero coefficients at every element of \(A\) is inferred from singularity alone. The relation is symmetric because the full Fourier matrix is symmetric.

## Proof
**1. Reduction to two row types.** The affine group \(\operatorname{AGL}(2,3)\) acts transitively on both four-point types: for a line-rich set, send its unique collinear triple to the first coordinate axis and the remaining point to \((0,1)\); for a cap, the four points form an affine parallelogram, so move its vertices to \((0,0),(1,0),(0,1),(1,1)\). Counting affine lines shows that \(12\) lines each admit \(6\) external fourth points, giving \(72\) line-rich sets, while \(\binom94-72=54\) are caps. A translation of \(A\) multiplies Fourier columns by nonzero scalars, and an invertible affine linear change in \(A\) corresponds to an inverse-transpose relabeling of \(B\), also preserving both geometric types. It therefore suffices to compute the number of singular partners of each type for those two row representatives.

**2. Exact algebraic determinant criterion.** Work in the integral domain \(\mathbb Z[\omega]\), with \(\omega^2+\omega+1=0\). Represent every algebraic integer \(a+b\omega\) as the ordered pair \((a,b)\). The complete exact arithmetic is
\[
(a,b)(c,d)=(ac-bd,\;ad+bc-bd),
\]
and the Fourier-entry pairs for exponents \(0,1,2\) are respectively \((1,0),(0,1),(-1,-1)\). For every four-element index pair \((A,B)\), the classical \(24\)-term Leibniz determinant in this ring yields the exact pair \((u,v)\) for \(\det F[A,B]=u+v\omega\). Because \(\omega\) has degree two, singularity holds if and only if both integers vanish. There is no floating-point, modular-lifting, probabilistic, or tolerance step.

**3. Finite exhaustive certificate.** Enumerate the \(\binom94=126\) ordered increasing four-subsets of the nine points encoded by \(3x+y\) for \((x,y)\in\mathbb F_3^2\). The deterministic `checker.py` embedded with this result directly implements the multiplication above, the \(24\) determinant terms, and the three-by-three collinearity test. For the line-rich representative \(A_L=\{(0,0),(1,0),(2,0),(0,1)\}\), the exact \(126\)-set census gives \(18\) singular line-rich and \(27\) singular cap partners. For the cap representative \(A_C=\{(0,0),(1,0),(0,1),(1,1)\}\), the exact census gives \(36\) and \(9\), respectively. The code additionally performs the full, redundant \(126\times126\) determinant census and checks that *every* row has \(45\) singular partners; these are verifications, not needed to extend the two representatives beyond their affine orbits. The finite search is exhaustive over a completely specified set and proves the finite claims, rather than extrapolating from sampled experiments.

**4. Incidence consequences.** The fixed-row counts yield \(18+27=36+9=45\). Multiplication by the \(72\) or \(54\) sets of each row type gives the four ordered-pair counts \(72\cdot18=1296\), \(72\cdot27=1944\), \(54\cdot36=1944\), and \(54\cdot9=486\). Their sum is \(5670\). Subtracting from \(\binom94^2=15876\) gives \(10206\) nonsingular pairs, completing the proof.

## Verification
Run `python3 checker.py`. The standalone program contains the entire \(\mathbb Z[\omega]\) arithmetic, the exact determinant expansion for all \(15876\) minors, both geometric-type classifiers, and assertions of the type matrix and uniform \(45\)-degree. It returns `CHECK_PASS`. The mathematical claim is deliberately finite: all possible configurations are inspected exactly, not numerically sampled.

## Relationship to prior work
Biró and Lev study support-geometry-sensitive Fourier uncertainty in prime affine planes, but their full-text results provide support inequalities and exceptions rather than this positional four-by-four singular-minor incidence. Caragea and Lee study principal minors of cyclic Fourier matrices, not arbitrary row-column minors of the Fourier matrix of \(\mathbb F_3^2\). Other related finite Fourier uncertainty studies give cardinality or existence constraints and do not themselves determine the stated equitable two-type incidence. A prior exact tabulation under an alternative Fourier-frame or affine-design formulation remains possible; a failed search is not a proof of absolute priority.

## Limitations
The classification is for the smallest odd affine plane only. It is a finite exact combinatorial Fourier invariant, not a general inequality for all primes, an assertion of a full positional orbit catalogue, or a guarantee of exact nonvanishing of coefficients of a kernel vector. The proof relies on a small, fully specified and reproducible exhaustive computation for two row representatives, whose finite domain is completely enumerated. No independent mathematical audit has been performed.

## References
1. A. Biró and V. F. Lev, *Uncertainty in finite planes*, arXiv:1808.07424, first publicly submitted 2018-08-22. https://arxiv.org/html/1808.07424v2
2. A. Caragea and D. G. Lee, *On the principal minors of Fourier matrices*, arXiv:2409.09793, first publicly submitted 2024-09-15. https://arxiv.org/abs/2409.09793
