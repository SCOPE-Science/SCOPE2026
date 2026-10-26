# A unique sixteen-dimensional sextic harmonic sampling resonance on \(D_n\) root shells

## Finding
For each integer \(n\ge5\), the antipodal half of the normalized type-\(D_n\) root system has exactly four (possibly coincident) eigenvalue branches for evaluation of spherical harmonics of *exact degree six*. All are strictly positive except a one-dimensional zero eigenvalue at \(n=16\). Thus sextic evaluation is onto every space of vertex data except at \(n=16\), where its image is exactly the codimension-one mean-zero subspace.

In particular, the full antipodal type-\(D_n\) root set is a spherical design of harmonic index six if and only if \(n=16\) (within \(n\ge5\)). It is not asserted to be a usual spherical six-design.

The following table gives the **entire spectrum**, where \(G_{n,6}=E_{n,6}E_{n,6}^{*}\):

| Eigenvalue | Multiplicity |
| --- | ---: |
| \(A_n=\frac{(n-16)^2(n-2)(n+6)}{16(n-1)(n+1)(n+3)}\) | \(1\) |
| \(B_n=\frac{(n+4)(n^3-18n^2+560n-1536)}{32(n-1)(n+1)(n+3)}\) | \(n-1\) |
| \(C_n=\frac{15(n-4)(n+4)(n+6)}{16(n-1)(n+1)(n+3)}\) | \(\frac{n(n-3)}2\) |
| \(D_n=\frac{(n+4)(n^2-n+3)}{(n-1)(n+1)(n+3)}\) | \(\binom n2\) |

## Assumptions and scope
Let \(e_i\) be standard coordinate vectors of \(\mathbb R^n\), and take \(X_n=\{(e_i+s e_j)/\sqrt2:1\le i<j\le n,\ s\in\{-1,1\}\}\), of cardinality \(N=n(n-1)\). This chooses one point from each antipodal pair of the complete type-\(D_n\) root shell, which contains \(2N\) points. Let \(\mathcal H_6(S^{n-1})\) carry the probability-normalized surface \(L^2\) norm, and let \(h_{n,6}=\dim\mathcal H_6\). Set \(E_{n,6}f=(f(x)/\sqrt{h_{n,6}})_{x\in X_n}\) using an orthonormal harmonic basis. The addition formula makes \(G_{n,6}(x,y)=P^{(n)}_6(\langle x,y\rangle)\), where \(P^{(n)}_6(t)=C_6^{(n-2)/2}(t)/C_6^{(n-2)/2}(1)\) and \(P^{(n)}_6(1)=1\). All statements hold for *every integer* \(n\ge5\).

## Proof
**1. Root inner products.** For two representatives with the same unordered coordinate support \(\{i,j\}\), inner products are \(1\) if the sign labels agree and \(0\) otherwise. For different supports, inner products are \(0\) when disjoint, and either \(1/2\) or \(-1/2\) when sharing one coordinate. Since \(P^{(n)}_6\) is even, only \(u=P^{(n)}_6(1/2)\) and \(v=P^{(n)}_6(0)\) are needed:
\[
u=\frac{n^3-42n^2+224n+672}{64(n-1)(n+1)(n+3)},\qquad
v=-\frac{15}{(n-1)(n+1)(n+3)}.
\]
These follow directly from the degree-six Gegenbauer formula, with its normalization at \(1\).

**2. Four orthogonal sectors.** Index each vertex by an edge \(\{i,j\}\) and a sign \(s\in\{-1,1\}\). First split the vertex-data space orthogonally into its sign-antisymmetric edge subspace (dimension \(\binom n2\)) and sign-symmetric edge subspace (also dimension \(\binom n2\)). The first has scalar Gram eigenvalue \(1-v\), because the off-edge Gram blocks have identical entries in both sign labels.

On the sign-symmetric subspace, use normalized basis vectors \((\delta_{ij,+}+\delta_{ij,-})/\sqrt2\). The Gram matrix has diagonal \(1+v\), entries \(2u\) for two edges sharing one endpoint, and entries \(2v\) for disjoint edges. Thus it equals
\[
(1+v)I+2u A+2v B,
\]
where \(A\) is the adjacency matrix of the Johnson graph \(J(n,2)\), and \(B=J-I-A\) is its disjointness matrix. Elementary incidence linear algebra gives paired eigenvalues
\[
(A,B):\quad (2(n-2),\binom{n-2}{2}),\quad(n-4,-(n-3)),\quad(-2,1)
\]
with multiplicities \(1\), \(n-1\), and \(n(n-3)/2\), respectively. One derivation writes the edge-vertex incidence matrix \(M\) and notes \(M^TM=2I+A\), while \(MM^T=(n-2)I+J\); this yields the three eigenvalues of \(A\), and then \(B=J-I-A\) supplies the others.

**3. Exact factorization.** Substitution gives
\[
\begin{aligned}
A_n&=1+v+4(n-2)u+(n-2)(n-3)v,\\
B_n&=1+v+2(n-4)u-2(n-3)v,\\
C_n&=1+3v-4u,\\
D_n&=1-v.
\end{aligned}
\]
Expanding and factoring yields exactly the four rational expressions in the finding table. This is an identity in \(\mathbb Q(n)\), not a pattern inferred from dimensions.

**4. No hidden rank losses.** For \(n\ge5\), the factors in \(C_n,D_n\) are positive. The polynomial \(q(n)=n^3-18n^2+560n-1536\) obeys \(q(5)=939>0\) and \(q'(n)=3(n-6)^2+452>0\) for real \(n\), so \(B_n>0\). The factorization shows \(A_n\ge0\), with equality exactly at \(n=16\). The four multiplicities sum to \(n(n-1)\), completing the spectrum and rank assertion. The trivial Johnson sector is the constant vector, proving that its span is precisely the missing output direction at \(n=16\).

**5. Harmonic-index interpretation.** For a finite vertex set, the sum of evaluations of every degree-six harmonic vanishes precisely when the constant vector lies in the left kernel of \(E_{n,6}\). Because the full root shell is an antipodal doubling and the degree is even, the same condition holds for its half shell. The preceding spectrum shows that this happens precisely at \(n=16\).

## Verification
The standalone file `checker.py` recomputes the four rational identities symbolically from the Gegenbauer polynomial, checks exact rational values in a finite range, independently assembles the actual normalized Gram matrix from roots in dimensions \(5,6,7,8,9,12,16,17\), and compares all matrix eigenvalues including multiplicities. The maximum reported absolute difference is below \(6\times10^{-15}\). This numerical agreement is a cross-check only; steps 1–5 provide the infinite proof. Run with `python checker.py` after installing `numpy` and `sympy`. The accompanying `checker_output.txt` records the executed results.

## Relationship to prior work
Bannai–Okuda–Tagami, *Spherical designs of harmonic index t* (arXiv:1308.5101v1, first public 2013-08-23), defines harmonic-index designs and establishes their connection with Gegenbauer addition kernels, with examples from root systems. Zhu–Bannai–Bannai–Kim–Yu, *More on spherical designs of harmonic index t* (arXiv:1507.05373v2), examines tight harmonic-index-six designs and provides the general degree-six Gegenbauer formula (Section 4). The latter is not a classification of the present type-\(D_n\) sampling spectra. Classical Johnson-scheme incidence eigenvalues underpin step 2 and are not new. Earlier exact-degree-four spectra on the same root shells concern a different harmonic degree and do not imply the degree-six factorization. The new claim is the specialized complete sextic spectrum and the unique dimension-sixteen null direction; independent publication-priority verification is outstanding.

## Limitations
The result concerns **one fixed harmonic degree**, degree six, and equal-weight sampling on the precise antipodal half-shell above, for \(n\ge5\). Its result about harmonic-index six does not assert ordinary six-design strength or optimal conditioning. General association-scheme theory may contain an equivalent all-degree formula from which the present spectral expressions can be derived; no independent historical certification is claimed. Floating-point tests are not an infinite proof.

## References
1. E. Bannai, T. Okuda, M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101v1 (2013-08-23), https://arxiv.org/pdf/1308.5101.
2. Y. Zhu, E. Bannai, E. Bannai, K.-T. Kim, W.-H. Yu, *More on spherical designs of harmonic index t*, arXiv:1507.05373v2 (2015-07-21), https://arxiv.org/pdf/1507.05373.
3. P. Delsarte, J.-M. Goethals, J. Seidel, *Spherical codes and designs*, Geometriae Dedicata 6 (1977), 363–388 (general background; primary full text not inspected for this analysis).
