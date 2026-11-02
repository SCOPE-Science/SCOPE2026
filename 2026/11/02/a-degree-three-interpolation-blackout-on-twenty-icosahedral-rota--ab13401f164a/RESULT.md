# A degree-three interpolation blackout on twenty icosahedral rotations

## Finding

Let \(I\subset SO(3)\) be the orientation-preserving rotation group of a regular icosahedron, identified with \(A_5\). Let \(X\subset I\) be **all twenty rotations of order three**, each through \(120^\circ\) or \(240^\circ\) around an icosahedral face axis. For each integer \(\ell\ge0\), let \(E_\ell\) evaluate the \((2\ell+1)^2\) matrix coefficients of the irreducible degree-\(\ell\) Wigner representation \(D^\ell\) on \(X\). Its rank is independent of the basis and of a nonzero common normalization.

The complete rank law is
\[
\operatorname{rank}E_\ell=\begin{cases}
1,&\ell=0,\\
8,&\ell=1,\\
20,&\ell=2,\\
16,&\ell=3,\\
20,&\ell\ge4.
\end{cases}
\]
Thus degree two already interpolates **every** complex assignment to the twenty rotations, degree three unexpectedly loses four data directions, and full interpolation resumes **permanently** in degree four. This is a nonmonotone exact-degree sampling phenomenon, not a statement about cumulative band-limited spaces.

For the unnormalized character Gram matrix \(G_\ell=(\chi_\ell(gh^{-1}))_{g,h\in X}\), the complete spectra for the exceptional degrees are
\[
\begin{array}{c|l}
\ell & \text{eigenvalue}^{\text{multiplicity}}\\\hline
0&0^{(19)},20^{(1)}\\
1&0^{(12)},6^{(5)},10^{(3)}\\
2&2^{(6)},4^{(10)},12^{(4)}\\
3&0^{(4)},5^{(4)},7^{(5)},10^{(4)},15^{(3)}
\end{array}
\]
The spectra for degrees four through nine are certified in `verify.py`; all their eigenvalues are positive. For every \(\ell\ge10\), each eigenvalue of \(G_\ell\) exceeds
\[
2\ell+1-13-3\sqrt5>0.
\]
If the columns of \(E_\ell\) are the Haar-probability orthonormal functions \(\sqrt{2\ell+1}D^\ell_{mn}\) and its rows are multiplied by \(20^{-1/2}\), the eigenvalues of \(E_\ell E_\ell^*\) are \((2\ell+1)/20\) times those of \(G_\ell\).

## Assumptions and scope

The group \(A_5\) acts as the standard icosahedral rotation group, and \(X\) is precisely its single class of twenty three-cycles. The degree \(\ell\) is an arbitrary nonnegative **integer**, not a continuous parameter. Wigner matrix coefficients are complex valued; interpolation means surjectivity of the linear evaluation map onto \(\mathbb C^{20}\). The theorem concerns one **fixed** exact degree at a time. The order-five classes may be interchanged by relabeling; this merely permutes the twenty sample nodes.

## Proof

**1. Character Gram reduction.** Unitarity of \(D^\ell\) gives the matrix-coefficient identity
\[
\sum_{m,n=-\ell}^{\ell}D^\ell_{mn}(g)\overline{D^\ell_{mn}(h)}
=\operatorname{tr}(D^\ell(gh^{-1}))=\chi_\ell(gh^{-1}).
\]
Hence \(G_\ell\) is positive semidefinite and \(\operatorname{rank}E_\ell=\operatorname{rank}G_\ell\). The rotation character satisfies
\[
\chi_\ell(\theta)=\frac{\sin((\ell+\tfrac12)\theta)}{\sin(\theta/2)}
\quad(\theta\ne0),\qquad \chi_\ell(0)=2\ell+1.
\]

**2. Finite class algebra.** Represent \(A_5\) by all even permutations of five symbols. Enumerate its twenty three-cycles and form \(gh^{-1}\) for each ordered pair. In **every** row there are one identity, six double transpositions, seven nonidentity three-cycles, and three elements in each of the two twelve-element classes of five-cycles. The associated rotation angles are \(0,\pi,2\pi/3,2\pi/5,4\pi/5\). With \(\varphi=(1+\sqrt5)/2\), the character values are exactly
\[
\begin{array}{c|c}
\text{class}&\chi_\ell\text{ by residue}\\\hline
1&2\ell+1\\
2A&(-1)^\ell\\
3A&(1,0,-1)\quad(\ell\bmod3)\\
5A&(1,\varphi,0,-\varphi,-1)\quad(\ell\bmod5)\\
5B&(1,1-\varphi,0,\varphi-1,-1)\quad(\ell\bmod5).
\end{array}
\]
The interchange of the five-cycle labels corresponds to an outer automorphism and does not affect the spectrum.

**3. Exact finite spectral certificates.** The accompanying `verify.py` constructs those twenty permutations without relying on a precomputed class or matrix. Every entry of \(G_\ell\) is stored as an integer pair representing an element of \(\mathbb Z[\varphi]\), with \(\varphi^2=\varphi+1\). For each degree \(0\le\ell\le9\), it verifies the **matrix** identity
\[
\prod_{\lambda\in S_\ell}(G_\ell-\lambda I)=0
\]
for the displayed set \(S_\ell\) of proposed distinct eigenvalues, and also verifies \(\operatorname{tr}(G_\ell^k)=\sum_{\lambda\in S_\ell}m_\lambda\lambda^k\) for every integer \(0\le k<|S_\ell|\). Since \(G_\ell\) is real symmetric, the first identity restricts its possible eigenvalues, while the Vandermonde invertibility for distinct \(S_\ell\) makes the multiplicities \(m_\lambda\) unique. These **integer-arithmetic identities**, rather than floating-point approximations, establish the displayed exceptional spectra and strict positivity for degrees four through nine.

**4. Structural continuation and infinite range.** The five-dimensional irreducible character of \(A_5\) has values \((5,1,-1,0,0)\) on the five classes \((1,2A,3A,5A,5B)\). Its multiplicity in the restriction of the degree-\(\ell\) rotation representation is therefore
\[
m_5(\ell)=\frac{2\ell+1+3(-1)^\ell-4c_\ell}{12},
\quad c_\ell=(1,0,-1)_{\ell\bmod3}.
\]
This positive integer is at least one for degrees four, five, and six by direct substitution, and for all degrees seven and above because its numerator is at least \(2\ell-6>0\). Since the degree-two representation **is** this irreducible five-dimensional module and its matrix coefficients already interpolate all twenty samples, every higher degree containing that module also interpolates. This supplies a representation-theoretic explanation of permanent surjectivity from degree four onward, independently of the finite checks for degrees four through nine.

For an additional quantitative bound, the two order-five character values have sum of absolute values at most \(\sqrt5\), independently of \(\ell\); the order-three and order-two values have absolute value at most one. Consequently every row has off-diagonal absolute sum at most
\[
7+6+3\sqrt5=13+3\sqrt5<21.
\]
For \(\ell\ge10\), the diagonal entry \(2\ell+1\ge21\) strictly dominates that sum. Gershgorin's theorem proves the asserted strict eigenvalue lower bound. Together these arguments prove the complete rank law.

## Verification

Run `python3 verify.py` from this directory (Python standard library only). Its final line must be `ALL_EXACT_CHECKS_PASSED`. It independently constructs the even permutations and the class-product table, checks every row count, verifies exact annihilating polynomials and traces for all degrees zero through nine, and verifies the elementary integer inequality used by the infinite-range diagonal-dominance argument. The complete spectral dictionaries are part of the checker, so each finite computation is directly reproducible.

## Relationship to prior work

McEwen, Büttner, Leistedt, Peiris and Wiaux (2015) develop equiangular **cumulative-bandlimit** sampling and fast Wigner transforms on \(SO(3)\), rather than exact-degree interpolation on an icosahedral conjugacy class. Fan, Chen and Draayer (1999) provide algebraic icosahedral symmetry-adapted spherical-harmonic bases and finite-group projection operators based on an order-five subgroup; their group tables and representation methods do not state the twenty-node Wigner evaluation ranks above. In particular, knowing subduction multiplicities of a single \(SO(3)\) representation is not by itself the singular-value spectrum of matrix-coefficient evaluation on the order-three class. A published three-cycle restriction theorem for the complete standard-representation Fourier block of \(S_n\) specializes at \(n=5\) to a rank-sixteen sampling operator on twenty three-cycles. Together with the degree-three icosahedral branching this covers the standard-block component of the degree-three deficit, but does not imply the present all-degree rank law: in particular, it does not establish full interpolation by the distinct five-dimensional degree-two block or permanent recovery for \(\ell\ge4\). The related twelve-node order-five class has a different exact-degree rank law and does not imply this order-three class classification.

## Limitations

The interpolation theorem does **not** assert invertible reconstruction of the full \((2\ell+1)^2\)-dimensional coefficient vector from twenty measurements: for \(\ell\ge2\), there are generally more coefficients than samples. It gives surjectivity onto sample data and Gram eigenvalues/bounds, not an optimal node placement theorem. The general lower bound for \(\ell\ge10\) is not claimed sharp. The literature comparison is bounded: earlier unindexed icosahedral representation or sampling tables could contain an equivalent specialization. No independent mathematical audit or independent validation has been performed.

## References

1. P.-D. Fan, J.-Q. Chen, J. P. Draayer, *Reduced projection operators and algebraic expressions for the symmetry-adapted functions of the icosahedral group*, Acta Crystallographica A55 (1999), 871–883, DOI 10.1107/S010876739900330X. Public first issue date: 1999-09-01.
2. J. D. McEwen, M. Büttner, B. Leistedt, H. V. Peiris, Y. Wiaux, *A novel sampling theorem on the rotation group*, arXiv:1508.03101 (submitted 2015-08-13), IEEE Signal Processing Letters 22 (2015), 2425–2429.
3. *Four-level three-cycle sampling spectrum for the symmetric-group standard Fourier block*, published research result (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-four-level-three-cycle-sampling-spectrum-for-the-symmetric-group--12437f259044.
