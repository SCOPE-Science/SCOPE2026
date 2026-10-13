# Signed-frequency resonance and average-mixing rank in products of complete graphs

## Finding

Let \(G=K_{n_1}\square\cdots\square K_{n_d}\), with \(d\ge1\) and each \(n_i\ge2\). Define its continuous-time adjacency walk, instantaneous probability matrix, and time average by
\[
U(t)=e^{itA(G)},\qquad M(t)=U(t)\circ\overline{U(t)},\qquad
\widehat M=\lim_{T\to\infty}\frac1T\int_0^T M(t)\,dt.
\]
Here \(\circ\) denotes entrywise multiplication, and the limit exists entrywise. For each coordinate let \(P_i^0=J_{n_i}/n_i\) and \(P_i^1=I_{n_i}-J_{n_i}/n_i\). For \(S\subseteq[d]\), write \(P_S=\bigotimes_{i=1}^dP_i^{\mathbf1_{i\in S}}\), and interpret empty products as \(1\).

**Theorem (complete indexed spectrum and signed-frequency rank criterion).** The mutually orthogonal projectors \(P_S\) resolve \(\widehat M\) and
\[
\widehat M=\sum_{S\subseteq[d]}\lambda_S P_S,\qquad
\lambda_S=\frac{[z^0]\prod_{i\in S}(n_i-2+z^{n_i}+z^{-n_i})}{\prod_{i\in S} n_i},\qquad
\operatorname{rank}P_S=\prod_{i\in S}(n_i-1).
\]
The coefficient operation \([z^0]\) extracts the constant Laurent coefficient. A coefficient \(\lambda_S\) is strictly positive precisely when a signed balance
\[
\sum_{i\in S}\varepsilon_i n_i=0,\qquad \varepsilon_i\in\{-1,0,1\},
\]
exists with \(\varepsilon_i\ne0\) for every binary coordinate \(n_i=2\). Consequently \(\widehat M\) is positive definite if and only if no Cartesian factor is binary.

The first rank-restoration case involving two distinct nonbinary factors is completely classified. For all \(m,n\ge3\),
\[
\boxed{\operatorname{rank}\widehat M(K_2\square K_m\square K_n)
=mn+(m-1)(n-1)\mathbf1_{\{|m-n|=2\}}.}
\]
Thus the rank on \(2mn\) vertices jumps from \(mn\) to \(mn+(m-1)(n-1)\) exactly at the two-unit alphabet resonance. In particular, \(K_2\square K_3\square K_4\) has rank \(12\) on \(24\) vertices, while \(K_2\square K_3\square K_5\) has rank \(23\) on \(30\) vertices.

## Assumptions and scope

Graphs are finite, undirected, simple and unweighted; \(K_n\) denotes the complete graph of order \(n\), and \(\square\) denotes Cartesian product. The Hamiltonian is the ordinary adjacency matrix, not a Laplacian or a signed/weighted alternative. Every dimension and alphabet size is arbitrary within the displayed integer bounds. The coefficient identity gives an exact closed algorithm for the whole indexed spectrum even when many adjacency eigenvalues coincide. It does not assert that numerically equal indexed eigenvalues are distinct.

## Proof

**1. Tensor dynamics.** The Cartesian adjacency matrix is the Kronecker sum of the factor adjacencies. These summands commute, so \(U(t)=\bigotimes_i U_i(t)\) and, entrywise, \(M(t)=\bigotimes_i M_i(t)\). Since \(A(K_n)=J_n-I_n\),
\[
U_n(t)=e^{-it}\left(I_n+\frac{e^{int}-1}n J_n\right).
\]
A diagonal transition probability is \(1-2(n-1)(1-\cos nt)/n^2\), and an off-diagonal transition probability is \(2(1-\cos nt)/n^2\). Therefore the exact factor probability matrix is
\[
M_n(t)=P_n^0+\frac{n-2+2\cos(nt)}n P_n^1
=P_n^0+\frac{n-2+e^{int}+e^{-int}}nP_n^1.
\]
This identity also holds at the singular boundary \(n=2\), where the constant term vanishes.

**2. Full spectrum.** Taking tensor products of the last decomposition gives
\[
M(t)=\sum_{S\subseteq[d]}\left(\prod_{i\in S}\frac{n_i-2+e^{in_it}+e^{-in_it}}{n_i}\right)P_S.
\]
Every factor is a finite trigonometric polynomial with integer frequencies. The long-time Cesàro mean of \(e^{ikt}\) is \(1\) for \(k=0\), and \(0\) for every other integer \(k\), proving the coefficient formula. The \(P_S\) are pairwise orthogonal idempotents summing to the identity, with rank given by multiplying rank \(1\) of each \(P_i^0\) and rank \(n_i-1\) of each \(P_i^1\). This establishes every eigenvalue and indexed multiplicity.

**3. Positivity and exact support.** In the Laurent expansion, picking \(z^{\pm n_i}\) contributes weight \(1\), while picking exponent zero contributes weight \(n_i-2\). All weights are nonnegative; the zero choice has positive weight exactly when \(n_i\ge3\). Hence the coefficient is positive if and only if one can select a zero-exponent sum with the stated restriction for binary coordinates. If every \(n_i\ge3\), the all-zero selection gives \(\lambda_S>0\) for every \(S\). Conversely, if \(n_j=2\), select \(S=\{j\}\); its coefficient vanishes, so \(\widehat M\) has a nonzero kernel and cannot be positive definite.

**4. Sharp three-factor resonance.** Set the coordinate sizes to \((2,m,n)\), where \(m,n\ge3\). For the four tensor sectors without the first coordinate, the positivity criterion holds by all-zero selections; their total multiplicity is \(mn\). Among sectors including the binary coordinate, singleton and two-factor subsets have no zero signed balance, since \(m,n>2\). The sole remaining sector includes all three coordinates; its coefficient is
\[
\lambda_{\{1,2,3\}}=\frac{[z^0](z^2+z^{-2})(m-2+z^m+z^{-m})(n-2+z^n+z^{-n})}{2mn}.
\]
For \(m,n\ge3\), this coefficient is \(1/(mn)\) precisely when \(|m-n|=2\), from exactly two balanced sign combinations; otherwise it is zero. The corresponding sector has rank \((m-1)(n-1)\). Summing the strictly positive sector ranks proves the formula, including all symmetric and boundary values allowed by the theorem.

## Verification

Run `python3 verify_hamming.py` with Python 3 and SymPy installed. The program reconstructs the eigenspace projector of the full adjacency matrix at each *distinct* eigenvalue; it computes the usual Schur-square formula \(\widehat M=\sum_\theta E_\theta\circ E_\theta\) by exact rational arithmetic and checks equality entrywise against the independently constructed Laurent-coefficient tensor expression. It also tests stochasticity and the explicit rank formula. The bundled exact test set comprises twelve products (including repeated factors, several binary factors, and unequal nonbinary sizes), representing \(9218\) exact matrix entries. Successful execution prints `VERIFY_OK`; the exhaustive proof is the argument above, not the finite test.

## Relationship to prior work

Coutinho, Godsil, Guo, and Zhan (2017, arXiv:1709.03591) give the complete-graph one-factor average mixing and the general commutant approach, while Godsil (2011, arXiv:1103.2578) establishes foundational spectral-projector formulas. Coutinho et al. (2022, arXiv:2208.08971) provide exact average-mixing methods for integral Hamiltonians. Lo et al. (2005, arXiv:quant-ph/0509059) analyze average mixing on circulants, hypercubes and path–circulant Cartesian bunkbeds; their product setting and near-uniformity criteria do not explicitly evaluate the mixed-alphabet signed-frequency rank law. Chan (2013, arXiv:1305.5811) treats instantaneous mixing on homogeneous Hamming graphs, which is a distinct time observable. The homogeneous-product and binary-hypercube-times-single-clique cases lie within the present expression, but do not imply its two-independent-nonbinary-size resonance criterion. The novelty assertion concerns this exact mixed-alphabet coefficient spectrum and arithmetic rank transition, not the tensor-product identity itself.

## Limitations

A more general, unlocated theorem on coherent algebras, association schemes or Cartesian quantum mixing might imply the coefficient expression; the literature comparison cannot rule that out. The statement concerns uniform unit edge weights and the infinite-time Cesàro mean only. It does not characterize instantaneous mixing, arbitrary observation-time laws, weighted adjacency couplings, or noncomplete factors. Coincident indexed eigenvalues must have their multiplicities combined when writing a set-valued spectrum. Finite exact computation cannot establish novelty or replace the proof for unbounded parameters.

## References

1. C. Godsil, *Average Mixing of Continuous Quantum Walks*, arXiv:1103.2578 (2011).
2. G. Coutinho, C. Godsil, K. Guo, H. Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591 (2017).
3. G. Coutinho, P. Ferreira Baptista, C. Godsil, T. J. Spier, R. Werner, *Irrational quantum walks*, arXiv:2208.08971 (2022), primary MSC2020 81P68.
4. P. Lo, S. Rajaram, D. Schepens, D. Sullivan, C. Tamon, J. Ward, *Mixing of Quantum Walk on Circulant Bunkbeds*, arXiv:quant-ph/0509059 (2005).
5. A. Chan, *Complex Hadamard Matrices, Instantaneous Uniform Mixing and Cubes*, arXiv:1305.5811 (2013).
6. G. Coutinho and K. Guo, *Selected Open Problems in Continuous-Time Quantum Walks*, arXiv:2404.02236 (2024).
