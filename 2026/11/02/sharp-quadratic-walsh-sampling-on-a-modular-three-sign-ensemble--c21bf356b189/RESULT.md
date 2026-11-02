# Sharp quadratic Walsh sampling on a modular-three sign ensemble

## Finding

Let \(n\geq8\), and let \(\Omega_n=\{x\in\{-1,1\}^n:\sum_{i=1}^n x_i\equiv0\pmod3\}\), with normalized counting measure. Restrict the complete Walsh band of degrees zero, one, and two, \(\chi_A(x)=\prod_{i\in A}x_i\) for \(|A|\leq2\), to \(\Omega_n\). Its normalized Gram matrix is positive definite and has exactly the six spectral sectors listed below, counting possible coincident eigenvalues as separate invariant sectors.

Put
\[
\varepsilon=(-1)^n,\quad D=2^n+2\varepsilon,\quad t=6/D,\quad M=\binom n2,\quad c=\frac{(n-2)(3n-13)}2,
\quad h=\frac{\sqrt{c^2+4M}-c}{2}.
\]
The Gram eigenvalues and multiplicities are
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
1+\varepsilon t&n-1\\
1-\varepsilon(n-1)t&1\\
1-\varepsilon(4n-13)t&n-1\\
1+5\varepsilon t&n(n-3)/2\\
1+\varepsilon ct/2+t\sqrt{c^2+4M}/2&1\\
1+\varepsilon ct/2-t\sqrt{c^2+4M}/2&1
\end{array}
\]
The sharp squared singular-value condition number is
\[
\kappa_n^2=
\begin{cases}
\dfrac{1+t(c+h)}{1-t(4n-13)},&n\text{ even},\\[5pt]
\dfrac{1+t(4n-13)}{1-t(c+h)},&n\text{ odd}.
\end{cases}
\]
In particular, the global sharp uniform bound is
\[
\boxed{\sup_{n\geq8}\kappa_n^2=\kappa_8^2=\frac{119+\sqrt{1201}}{48}},
\]
with equality only for \(n=8\). The identity of the least and greatest spectral sectors switches with parity: for even \(n\), the edge-standard sector is least and the upper scalar sector greatest; for odd \(n\), the lower scalar sector is least and the edge-standard sector greatest. Moreover, \(\kappa_n^2=1+9n^2/2^n+O(n/2^n)\). The first possible dimension with injective quadratic Walsh restriction is exactly \(n=8\); smaller positive dimensions admit nonzero quadratic polynomials vanishing on the ensemble.

## Assumptions and scope

All coordinates are real signs \(\{-1,1\}\). The congruence is taken in the integers, not over a characteristic-three coefficient field. The Gram matrix uses uniform *probability* measure on \(\Omega_n\) and orthonormal Walsh coordinates relative to uniform measure on the entire sign cube. The condition number is the quotient of largest to smallest singular value of the restriction map, so its square is the ratio of extremal Gram eigenvalues. No claim is made for a different modulus, degree band, or arbitrary weighting of the sample points. The six formulas are valid algebraically for smaller \(n\geq4\), but the main positive-definiteness and condition-number statements require \(n\geq8\).

## Proof

**Exact moments.** Write \(\omega=e^{2\pi i/3}\) and use \(\mathbf1_{\sum x_i\equiv0}=\frac13\sum_{j=0}^2\omega^{j\sum x_i}\). Since \(\omega+\omega^{-1}=-1\), the number of admissible signs is \(|\Omega_n|=D/3\). If \(A\neq\varnothing\), then \(\mathbb E_{\Omega_n}\chi_A=0\) for odd \(|A|\), by global sign reversal. For \(|A|=2r>0\), separating coordinates in and outside \(A\) in the root-of-unity sum gives
\[
\mathbb E_{\Omega_n}\chi_A=\frac{2\varepsilon(-3)^r}{D}.
\]
In particular, the moments at distances two and four are \(a=-\varepsilon t\) and \(b=3\varepsilon t\), respectively. All Gram entries equal the moment indexed by the symmetric difference of the two Walsh indices.

**Invariant spectral sectors.** Sign reversal splits the band orthogonally into the singleton-character block and the block consisting of the constant and all two-element characters. The singleton block has diagonal one and off-diagonal \(a\); its standard and trivial eigenvalues are \(1-a\) and \(1+(n-1)a\), of multiplicities \(n-1\) and one.

The edge-edge block is indexed by edges of the complete graph. Its diagonal entries are one, entries for intersecting distinct edges equal \(a\), and entries for disjoint edges equal \(b\). The line-graph adjacency has eigenvalues \(2(n-2)\), \(n-4\), and \(-2\), of respective multiplicities one, \(n-1\), and \(n(n-3)/2\). Indeed, the unsigned vertex-edge incidence matrix \(B\) satisfies \(B^TB=2I+A\) and \(BB^T=(n-2)I+J\); these identities give the claimed eigenspaces and multiplicities without an unproved representation-theoretic assertion. Thus the edge-standard and edge-second eigenvalues are \(1+(n-4)a-(n-3)b=1-\varepsilon(4n-13)t\) and \(1-2a+b=1+5\varepsilon t\).

The normalized all-edges vector couples only to the constant character, with coupling \(a\sqrt M\). Their residual Gram block is
\[
\begin{pmatrix}1&-\varepsilon t\sqrt M\\-\varepsilon t\sqrt M&1+\varepsilon ct\end{pmatrix},
\]
where \(c=(n-2)(3n-13)/2\). Its characteristic polynomial gives the two scalar eigenvalues. The multiplicities sum to \(1+n+\binom n2\), so the list is exhaustive.

**Positivity and extrema.** For \(n\geq8\), \(c>0\), \(h>0\), and \(h<\sqrt M<n<4n-13\). For even \(n\), the six sectors immediately place \(1-(4n-13)t\) lowest and \(1+t(c+h)\) highest. The lowest is positive because \(2^n+2>6(4n-13)\) for every even \(n\geq8\), first at eight and thereafter by induction. For odd \(n\geq9\), \(c>5\) and the extrema are \(1-t(c+h)\) and \(1+(4n-13)t\). At nine, \(c=49\), \(M=36\), \(t=1/85\), so \(t(c+h)<55/85<1\). For all odd \(n\geq11\), \(c<n^2\), \(h<\sqrt M<n\), and \(2^n-2>6(n^2+n)\); induction establishes the last inequality from eleven. Therefore the least eigenvalue is always positive.

**Sharp uniform bound.** At \(n=8\), \(t=1/43\), \(c=33\), and \(M=28\); substitution gives \(\kappa_8^2=(119+\sqrt{1201})/48>19/6\). At \(n=9\), \(t=1/85\), \(c=49\), and \(h<1\), whence \(\kappa_9^2<108/35<19/6\). For even \(n\geq10\), use \(h<\sqrt M\) to bound \(\kappa_n^2\leq(1+t(c+\sqrt M))/(1-t(4n-13))\). Both positive correction fractions decrease when \(n\) rises by two: the denominators \(D\) more than triple, whereas \(c+\sqrt M\) and \(4n-13\) less than triple. At \(n=10\), \(c=68\), \(\sqrt M<7\), and \(t=1/171\), giving \(\kappa_n^2<41/24<19/6\). For odd \(n\geq11\), the analogous bound \((1+t(4n-13))/(1-t(c+\sqrt M))\) also decreases in steps of two; at eleven it is below \(124/81<19/6\). Thus eight is the unique global maximizer.

Since \(c=3n^2/2+O(n)\), \(h=O(1)\), and \(t=6/2^n+O(4^{-n})\), either parity formula gives \(\kappa_n^2=1+9n^2/2^n+O(n/2^n)\).

**Sharp injectivity threshold.** The preceding positivity proves injectivity for all \(n\geq8\). For \(n=7,5,3\), the nonzero quadratic polynomial \((\sum_i x_i)^2-9\) vanishes on every admissible sign vector; for \(n=6\), the polynomial \((\sum_i x_i)(x_1-x_2)\) vanishes there; for \(n=4,2\), the linear polynomial \(\sum_i x_i\) vanishes there. Dimension one has an empty admissible ensemble. Hence dimension eight is the first injective quadratic Walsh case.

## Verification

Run `python checker.py` in an environment with Python 3 and NumPy. The program enumerates the finite sample ensembles for dimensions three through eleven, independently computes all moments of nonempty coordinate sets of sizes at most four with exact rational arithmetic, constructs the full numerical Gram matrices directly from evaluations, and matches all their eigenvalues and multiplicities with the analytic six-sector spectrum. It passed 1,569 exact moment checks and 284 Gram eigenvalue comparisons. These finite experiments corroborate, but do not replace, the all-dimension proof above.

## Relationship to prior work

Harmonic analysis on single Hamming-weight slices and the Johnson adjacency decomposition provide the structural background; see Filmus and the classical Johnson scheme. Bernasconi and Egidi determine the affine Hilbert functions of symmetric Boolean sets, and Venkitesh extends this to unions of layers on finite grids. Those rank results already address whether low-degree restrictions have kernels; **the novelty claim here concerns the specific uniform-probability modular-three ensemble's entire quadratic Walsh Gram spectrum, the parity-dependent extremizing sectors, and the exact sharp conditioning bound across all lengths**, not the abstract rank problem. The finite Fourier-concentration literature for a single Hamming sphere concerns a different sampling measure and cannot by itself supply the off-diagonal cross-layer Gram entries or the present spectral extremizers.

## Limitations

No independent mathematical review has been performed. The near-orthogonality statement is specific to the degree-two band and to congruence modulo three. Similarity with broader association-scheme diagonalizations means an equivalent historical statement may exist; the closest original 1999 Bernasconi–Egidi full text and some third-party research files were not accessible for complete comparison. Its Hilbert-function theorem is treated as covering the **rank** component, not ignored. Positivity does not imply optimality among arbitrary nonuniform weights or different unions of layers.

## References

1. Y. Filmus, *Orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142, first posted 1 June 2014; Sections 2 and 4. https://arxiv.org/abs/1406.0142
2. A. Bernasconi and L. Egidi, *Hilbert Function and Complexity Lower Bounds for Symmetric Boolean Functions*, Information and Computation 153(1), 1–25 (1999). https://dblp.org/rec/journals/iandc/BernasconiE99
3. S. Venkitesh, *Covering Weight-Determined Sets of Uniform Grids by Polynomials*, arXiv:2111.06993, first posted 12 November 2021; Sections 1, 4, and 5. https://arxiv.org/abs/2111.06993
4. S. Venkitesh, *Covering Symmetric Sets of the Boolean Cube by Affine Hyperplanes*, Electronic Journal of Combinatorics 29(2) (2022), P2.22. https://doi.org/10.37236/10600
