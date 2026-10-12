# Modulo-twelve resonance in quantum average mixing on prisms

## Finding

For each integer \(n\ge 3\), let \(G_n=C_n\square K_2\) be the unweighted prism graph, with vertices \((j,s)\in\mathbb Z/n\mathbb Z\times\mathbb Z/2\mathbb Z\). Set \(A_n=A(G_n)\), let \(U_n(t)=\exp(\mathrm{i}tA_n)\), and define the long-time average mixing matrix
\[
\widehat M_n=\lim_{T\to\infty}\frac1T\int_0^T U_n(t)\circ\overline{U_n(t)}\,\mathrm{d}t.
\]
Every character \(\chi_{a,b}(j,s)=\exp(2\pi\mathrm{i}aj/n)(-1)^{bs}\), with \(a\in\mathbb Z/n\mathbb Z\) and \(b\in\{0,1\}\), is an eigenvector of \(\widehat M_n\). Its eigenvalue \(\mu_{a,b}\) is as follows:
\[
\mu_{a,0}=\begin{cases}
1,&a=0,\\
1/n,&n\text{ odd and }a\ne0,\\
2/n,&n\text{ even and }a\ne0\text{ is even},\\
0,&\text{otherwise}.
\end{cases}
\]
In the odd/even conditions, the representative of \(a\) is taken modulo \(n\), and parity of a residue is well-defined when \(n\) is even. In the antisymmetric layer sector,
\[
\mu_{a,1}=
\begin{cases}2/n,&4\mid n,\quad a\equiv\pm n/4\pmod n,\\0,&\text{otherwise},\end{cases}
\quad+\quad
\begin{cases}1/n,&6\mid n,\quad a\equiv\pm n/6\pmod n,\\0,&\text{otherwise},\end{cases}
\quad+\quad
\begin{cases}2/n,&6\mid n,\quad a\equiv n/2\pmod n,\\0,&\text{otherwise}.\end{cases}
\]
Each of the \(2n\) indexed eigenvalues has Fourier multiplicity one; numerical coincidences are combined to get ordinary multiplicities. In particular,
\[
\boxed{\operatorname{rank}(\widehat M_n)=
\begin{cases}
n,&n\text{ odd},\\
n/2+2\mathbf{1}_{4\mid n}+3\mathbf{1}_{6\mid n},&n\text{ even}.
\end{cases}}
\]
The exceptional extra \(2\) or \(3\) independent mixing modes are spectral resonances between the two transverse layers. Both appear precisely for cycle lengths divisible by \(12\); for example the \(24\)-vertex prism \(G_{12}\) has rank \(11\).

## Assumptions and scope

The graph is finite, connected, simple and unweighted. \(C_3\) is the ordinary triangle; \(n=2\), which would require choosing a multigraph convention, is excluded. The Hamiltonian is the adjacency matrix (not a normalized Laplacian), both transverse edges and rim edges having strength one. There is no disorder, magnetic phase or external potential. The average uses a uniform continuous observation-time interval with its length tending to infinity. The limit always exists by finite spectral expansion. This is an exact statement for every integer \(n\ge3\), not an asymptotic rank estimate.

## Proof

**1. Time averaging in the Fourier basis.** On the Abelian group \(\mathbb Z/n\mathbb Z\times\mathbb Z/2\mathbb Z\), define \(x_k=2\cos(2\pi k/n)\). The characters \(\chi_{k,s}\) diagonalize the adjacency matrix with eigenvalues \(\theta_{k,s}=x_k+(-1)^s\). For any vertices \(u,v\), Fourier inversion gives
\[
U_n(t)_{uv}=\frac1{2n}\sum_{k\in\mathbb Z/n\mathbb Z}\sum_{s\in\{0,1\}}
\exp(\mathrm{i}t\theta_{k,s})\chi_{k,s}(u-v).
\]
The average of \(\exp(\mathrm{i}t\omega)\) over \([0,T]\) tends to one when \(\omega=0\), and zero otherwise. Multiplying the last expansion by its complex conjugate, averaging and Fourier transforming the translation-invariant mixing kernel therefore gives
\[
\mu_{a,b}=\frac1{2n}\#\left\{(k,s,l,t):\; k-l\equiv a\pmod n,\quad s-t\equiv b\pmod2,\quad\theta_{k,s}=\theta_{l,t}\right\}.
\tag{1}
\]
Here \(k,l\in\mathbb Z/n\mathbb Z\) and \(s,t\in\{0,1\}\). This identity also proves every \(\mu_{a,b}\) is nonnegative.

**2. Equal-layer modes.** If \(b=0\), then \(s=t\). The equality of adjacency eigenvalues becomes \(\cos(2\pi k/n)=\cos(2\pi l/n)\), equivalent to \(l\equiv\pm k\pmod n\). At \(a=0\) there are exactly \(2n\) ordered pairs, hence \(\mu_{0,0}=1\). For nonzero \(a\), the only contributing pairs have \(l\equiv-k\) and \(2k\equiv a\pmod n\). The last congruence has one solution when \(n\) is odd, two when \(n\) is even and \(a\) is even, and none otherwise. There are two choices of \(s=t\), so (1) yields exactly the displayed formula for \(\mu_{a,0}\).

**3. The cyclotomic rigidity lemma.** Suppose \(x_k-x_l=2\). Both \(x_k\) and \(x_l\) are algebraic integers because they are each the sum of an \(n\)-th root of unity and its inverse. Every complex field embedding of their common cyclotomic field maps them to real numbers between \(-2\) and \(2\), while preserving \(x_k-x_l=2\). Consequently every conjugate of \(x_k\) lies in \([0,2]\), so the algebraic integer \(y=x_k-1\) has all its conjugates in \([-1,1]\).

For completeness, the elementary Kronecker lemma used here states that an algebraic integer with all conjugates of absolute value at most one is either zero or a root of unity. If it is nonzero, its absolute norm is a positive integer at most one, forcing every conjugate to have absolute value exactly one. All powers are algebraic integers with conjugates on the unit circle; their monic integer minimal polynomials have uniformly bounded coefficients (by elementary symmetric sums). Therefore the powers lie in a finite set of complex algebraic values and two powers coincide, proving the root-of-unity assertion. Since \(y\) is real, \(y\in\{-1,0,1\}\); hence
\[
(x_k,x_l)\in\{(0,-2),(1,-1),(2,0)\}.
\tag{2}
\]
These are the *only* ways two cyclic adjacency eigenvalues can differ by the fixed rung splitting \(2\); no unsearched trigonometric coincidences remain.

**4. Opposite-layer resonance counts.** If \(b=1\), then \(s\ne t\), so the eigenvalue equality demands \(x_k-x_l=2\) for one choice of the ordered layers, or the reversed equality for the other. The counts at difference \(a=k-l\) are equal for the two layer orientations, because reversing the pair and applying \((k,l)\mapsto(-k,-l)\) preserves the required difference.

The cases in (2) give all ordered pairs with \(x_k-x_l=2\):

- \((x_k,x_l)=(2,0)\) gives \(k=0\), \(l=\pm n/4\), requiring \(4\mid n\).
- \((x_k,x_l)=(0,-2)\) gives \(k=\pm n/4\), \(l=n/2\), requiring \(4\mid n\).
- \((x_k,x_l)=(1,-1)\) gives \(k=\pm n/6\), \(l=\pm n/3\), requiring \(6\mid n\), with independent signs.

Consequently, for each of \(a\equiv\pm n/4\) there are exactly two ordered pairs in the first two cases; for each of \(a\equiv\pm n/6\) there is exactly one; and for \(a\equiv n/2\) there are exactly two. When \(12\mid n\), these five residues are pairwise distinct. Doubling for the two layer orientations and dividing by \(2n\) as in (1) gives the stated antisymmetric-sector eigenvalues.

**5. Rank.** Every nonzero eigenvalue counted above is strictly positive. For odd \(n\), all \(n\) equal-layer characters survive and no opposite-layer character does. For even \(n\), exactly \(n/2\) equal-layer characters survive. The opposite-layer sector gains two independent modes when \(4\mid n\), three when \(6\mid n\), and none otherwise; the two sets are disjoint when both divisibilities hold. Orthogonality and completeness of the \(2n\) Fourier characters now yield the rank formula.

## Verification

The standalone `verifier.py` requires Python 3 and NumPy. Execute `python3 verifier.py` in the directory containing it. It independently constructs unweighted prism adjacency matrices and their real-symmetric eigenspace projectors, obtains the average matrix from entrywise projector squares, and compares its Fourier spectrum and rank with the theorem for each \(3\le n\le24\). For \(3\le n\le18\), it separately enumerates all ordered equal-energy Fourier pairs and checks (1). It tests stochasticity, positive semidefiniteness and the \(n=12\) resonance boundary. The theorem for all orders is proved in the preceding sections; these finite numerical checks only corroborate calculations and normalize the implementation.

## Relationship to prior work

The standard formula expressing the average mixing matrix as the sum of Schur squares of spectral projectors, and the connection to the commutant of the adjacency matrix, were established by Coutinho, Godsil, Guo and Zhan [2]. Godsil, Guo and Sobchuk [3, Section 4.2] give a positive-semidefinite lower bound for a Cartesian product in terms of the tensor product of the individual average mixing matrices; this guarantees the baseline modes but does not identify the extra opposite-layer resonances. The cycle average-mixing spectrum itself appears in [5, Section 15.10]. Baptista, Coutinho and Marques [4, Section 5] discuss Cartesian products and a trace/covariance formula under more general time distributions, not this prism rank classification. The motivating exact-spectral computation framework [1] handles general adjacency quantum walks but does not state the present cyclotomic resonance classification. The present result adds a complete Fourier-indexed prism spectrum and uses the rigidity of algebraic integers to show that the only additional rank contributions are the displayed modulo-four and modulo-six modes.

## Limitations

The claim concerns *uniform Cesàro* observation-time averaging, not instantaneous mixing, arbitrary sampling laws, mixing times, or Laplacian dynamics. It fixes the rung coupling at unity; changing that coupling changes the cyclotomic difference equation and can create other exceptional values. Distinct indexed eigenvalues may coincide numerically, and the statement correctly accounts for such multiplicities by Fourier labels. The literature comparison cannot exclude an equivalent formula buried in a broader unpublished or differently indexed treatment; no claim of independent audit is made.

## References

[1] G. Coutinho, P. F. Baptista, C. Godsil, T. J. Spier, and R. Werner, *Irrational quantum walks*, arXiv:2208.08971v1 (first publicly posted 2022-08-18), https://arxiv.org/abs/2208.08971. DOI:10.1137/22M1521262. Primary MSC2020 81P68.

[2] G. Coutinho, C. Godsil, K. Guo, and H. Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591v1 (2017), https://arxiv.org/abs/1709.03591.

[3] C. Godsil, K. Guo, and M. Sobchuk, *Diagonal entries of the average mixing matrix*, arXiv:1910.02039 (2019), https://arxiv.org/abs/1910.02039.

[4] P. Baptista, G. Coutinho, and V. Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378v1 (2023), https://arxiv.org/abs/2308.16378.

[5] G. Coutinho and C. Godsil, *Graph Spectra and Continuous Quantum Walks*, lecture notes (2021), Chapter 15, https://www.math.uwaterloo.ca/~cgodsil/quagmire/QuantumWalks/pdfs/GrfSpc3.pdf.
