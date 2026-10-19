# Odd-degree spherical-harmonic interpolation on the 24 lines of the normalized \(F_4\) roots

## Finding
Let \(X\) be one unit representative of every antipodal line in the normalized \(F_4\) roots in \(\mathbb R^4\), hence \(|X|=24\). For every **odd** integer \(\ell\ge1\), define \(n=\ell+1\) and
\[
\varepsilon_\ell=\frac{2}{\sqrt3}\sin(n\pi/3)\in\{-1,0,1\},\qquad
\eta_\ell=\sin(n\pi/4)\in\{-1,0,1\}.
\]
The probability-sphere-normalized harmonic-evaluation Gram matrix \(G_\ell\) has the entire eigenvalue multiset
\[
\boxed{n(n-2\varepsilon_\ell)\quad[16],\qquad
n(n+4\varepsilon_\ell+6\eta_\ell)\quad[4],\qquad
n(n+4\varepsilon_\ell-6\eta_\ell)\quad[4].}
\]
Brackets give multiplicities, added when eigenvalues coincide. Its degree-wise rank begins
\[
\boxed{\operatorname{rank}E_1=4,\ \operatorname{rank}E_3=16,\ \operatorname{rank}E_5=20,\ \operatorname{rank}E_7=24,\ \operatorname{rank}E_9=20,\quad \operatorname{rank}E_\ell=24\ (\ell\ge11\ \text{odd}).}
\]
Thus interpolation becomes surjective at degree seven, fails again at degree nine, and is surjective permanently from degree eleven. Moreover
\[
\boxed{G_\ell=n^2I_{24}\iff \ell\equiv11\pmod{12}.}
\]
In these and only these odd degrees, the 24 zonal kernels are mutually orthogonal, each of squared norm \(n^2\). They are not claimed to span the full \(n^2\)-dimensional harmonic space.

## Assumptions and scope
Use the complex vector space \(\mathcal H_\ell\) of restrictions to \(S^3\) of homogeneous harmonic polynomials of degree \(\ell\) on \(\mathbb R^4\). It has dimension \((\ell+1)^2\). Use surface probability measure to define its Hilbert norm. Choose the following unit representatives, ordered by the two twelve-point orbits:
\[
X_s=\{e_i:1\le i\le4\}\ \cup\ \{(1,\sigma_2,\sigma_3,\sigma_4)/2:\sigma_j\in\{-1,1\}\},
\]
\[
X_l=\{(e_i+\sigma e_j)/\sqrt2:1\le i<j\le4,\ \sigma\in\{-1,1\}\},\qquad X=X_s\cup X_l.
\]
The first orbit contains the twelve short-root lines and the second the twelve long-root lines. The evaluation operator \(E_\ell:\mathcal H_\ell\to\mathbb C^X\) sends a harmonic polynomial to its sample values in the fixed representative ordering. For odd degree, changing representative signs applies a diagonal unitary congruence to the Gram matrix and leaves ranks and eigenvalues invariant. The theorem does not concern even degrees, arbitrary rotations between the two root orbits, or arbitrary weighted sampling.

## Proof
**1. Reproducing normalization.** The spherical-harmonic addition formula in dimension four gives the reproducing kernel
\[
K_\ell(x,y)=(\ell+1)U_\ell(x\cdot y),\qquad U_\ell(\cos\theta)=\frac{\sin((\ell+1)\theta)}{\sin\theta}.
\]
In particular \(K_\ell(x,x)=(\ell+1)^2=n^2\). Since \(\ell\) is odd, \(U_\ell\) is odd. For distinct points in either twelve-point orbit, the only nonzero inner products are \(\pm1/2\); across orbits they are \(\pm1/\sqrt2\). The respective signed kernel entries are therefore \(a=n\varepsilon_\ell\) and \(b=n\sqrt2\eta_\ell\).

**2. Exact finite root-incidence identities.** Form the integer matrices \(S,T\in\mathbb Z^{12\times12}\) whose off-diagonal entries are the signs of the pairwise inner products within \(X_s,X_l\) (zero if the inner product vanishes). Form \(B\in\mathbb Z^{12\times12}\) with entries the signs of cross-orbit inner products. Direct substitution of the explicitly displayed coordinate sets and elementary twelve-by-twelve matrix multiplication gives
\[
S^2=2S+8I,\qquad T^2=2T+8I,\qquad
SB=BT=4B,
\]
\[
BB^*=3(S+2I),\qquad B^*B=3(T+2I).
\]
These exact finite identities are additionally checked entrywise by the complete, standalone integer/rational enumeration in `verify.py`; they are not assumed from a numerical graph eigenvalue approximation. Taking traces of \(S,T\) and their quadratic equations shows that each has eigenvalues \(4\) (multiplicity four) and \(-2\) (multiplicity eight). The two products identify \(B\) as a scaled isometry of size \(\sqrt{18}\) between the two four-dimensional \(+4\) eigenspaces; it vanishes between their eight-dimensional \(-2\) complements.

**3. Block diagonalization.** In the orbit ordering, the evaluation Gram matrix has the exact form
\[
G_\ell=\begin{pmatrix}n^2I+aS&bB\\bB^*&n^2I+aT\end{pmatrix}.
\]
On the two \(-2\) eigenspaces, it acts as the scalar \(n^2-2a=n(n-2\varepsilon_\ell)\), repeated sixteen times. On the paired \(+4\) eigenspaces, its four equivalent two-by-two blocks are
\[
\begin{pmatrix}n^2+4a&\sqrt{18}\,b\\ \sqrt{18}\,b&n^2+4a\end{pmatrix},
\]
with eigenvalues \(n(n+4\varepsilon_\ell\pm6\eta_\ell)\). This proves the spectrum for all odd degrees.

**4. Rank, tightness, and recovery.** For \(n=2,4,6,8,10\), the pairs \((\varepsilon_\ell,\eta_\ell)\) are respectively \((1,1),(-1,0),(0,-1),(1,0),(-1,1)\); inspection yields exactly the five ranks stated above. For \(n\ge12\), all eigenvalues are positive because \(|\varepsilon_\ell|,|\eta_\ell|\le1\) and \(n-10>0\). Thus every odd degree at least eleven has full sampling rank. The Gram matrix is a scalar multiple of the identity if and only if its three eigenvalue sectors coincide, forcing first \(\eta_\ell=0\) and then \(\varepsilon_\ell=0\); for even \(n\), the two conditions are equivalent to \(12\mid n\). The scalar is then the diagonal value \(n^2\).

**5. Interpolation formula.** For any \(y\) in the image of \(E_\ell\), its unique minimum-Hilbert-norm interpolant is
\[
h_y(z)=\sum_{i,j=1}^{24}K_\ell(z,x_i)(G_\ell^\dagger)_{ij}y_j,
\qquad\|h_y\|^2=y^*G_\ell^\dagger y,
\]
where \(G_\ell^\dagger\) is the Moore–Penrose pseudoinverse of the explicit matrix in Step 3. Attainability is equivalent to \(y\in\operatorname{range}G_\ell\), so the spectral formula determines the complete interpolation feasibility and its exact energy. For full-rank degrees the pseudoinverse is the ordinary inverse. The formula follows directly from the reproducing property and orthogonal projection in finite-dimensional Hilbert space.

## Verification
Execute `python verify.py` with Python 3 and SymPy. This independently enumerates every one of the 24 root-line representatives from the coordinate definitions, verifies both twelve-by-twelve signed adjacency equations, both cross-orbit equations, and the complete eigenvalue formula for all 21 odd degrees from 1 through 41. It compares several resulting Gram matrices entrywise with the Chebyshev reproducing kernel, verifies the five exceptional low-degree ranks, and checks arithmetic tightness in sampled degrees. The exact finite matrix identities support the infinite-degree proof because Step 3 uses them symbolically; checking finitely many degrees alone would not prove the theorem.

## Relationship to prior work
De la Harpe, Pache and Venkov (2005 preprint), building on earlier work of Goethals and Seidel and classical cubature, establish that the 48-point union of the two \(D_4\) dual orbits is a spherical 7-design, and provide the reflection-group invariant framework. The 7-design property and the known 24-cell behavior are not claimed as new. Dai and Xu (2013) give the spherical-harmonic reproducing kernel and general interpolation framework used above. Hirao, Nozaki and Tasaka (2025) analyze all odd harmonic-strength moments of the binary octahedral group (the same antipodal point set) and several even harmonic degrees; their harmonic-strength and minimal-design conclusions concern vanishing sums and are distinct from degree-wise interpolation rank and the complete Gram spectrum. The claim here concerns the 24 root lines, including the nonmonotone degree-seven to degree-nine rank change, uniform surjectivity thereafter, and the exact infinite congruence class of orthogonal zonal systems.

## Limitations
This result is an exact specialization to \(F_4\) root lines and odd degrees; it does not imply a generic point-configuration phenomenon or independent certification. Its algebra follows from standard addition theorems plus a finite configuration-specific incidence calculation. An equivalent reformulation may exist in earlier character-theoretic, association-scheme, or quaternionic-frame literature; searches and primary comparisons did not establish publication priority. The degree-three orbit-specific sample rank is explicitly not asserted as new. The orthogonal families live inside higher-dimensional harmonic spaces, and the 24-vector orthogonality statement is not a basis statement for those ambient spaces.

## References
1. P. de la Harpe, C. Pache, B. B. Venkov, *Construction of spherical cubature formulas using lattices*, arXiv:math/0505510v1, initially public 24 May 2005; Theorem \(D_4\) and Section 6.4. https://arxiv.org/abs/math/0505510
2. F. Dai and Y. Xu, *Spherical Harmonics*, arXiv:1304.2585v1 (9 April 2013), Section 2 addition theorem and Section 3 interpolation framework. https://arxiv.org/abs/1304.2585
3. M. Hirao, H. Nozaki and K. Tasaka, *Spherical designs for finite quaternionic unit groups and their applications to modular forms*, arXiv:2507.01358v1 (2 July 2025), Theorems 1.2–1.4. https://arxiv.org/abs/2507.01358
