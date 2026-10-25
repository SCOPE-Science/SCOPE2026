# The exact-degree harmonic sampling spectrum of the 600-cell

## Finding

Let \(X\subset S^3\) be the 120 unit-quaternion vertices of the regular 600-cell, and for every integer \(n\geq0\) let \(U_n\) be the Chebyshev polynomial of the second kind. The spherical-harmonic evaluation Gram matrix is
\[
G_n=\bigl[U_n(\langle x,y\rangle)\bigr]_{x,y\in X}.
\]
Its *complete real spectral multiset* and rank are determined for **every degree** by a nine-term integer recurrence. The rank is always at most 60, because antipodal vertices have redundant evaluations with degree-dependent sign. It is 60 for every odd \(n\ge29\) and for every \(n\ge60\); these are the sharp persistent thresholds within odd and even degrees, respectively. Smaller degrees are not monotone: for example, degrees 13 and 15 have ranks 60 and 52. The degree-59 matrix is exactly \(60(I-P)\), where \(P\) exchanges antipodes, while degree 58 has 59 positive eigenvalues, all equal to 120.

Explicitly, number nine irreducible representations of the binary icosahedral group by the following ordered dimension list and edge list:

- dimensions \((d_i)_{i=0}^8=(1,2,3,4,5,6,4,2,3)\);
- affine-\(E_8\) adjacency edges \((0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(5,8)\).

Let \(A\) be the symmetric \(9\)-by-\(9\) adjacency matrix. Define integer vectors \(m(0)=e_0\), \(m(1)=e_1\), and
\[
m(n+1)=A\,m(n)-m(n-1)\qquad(n\ge1).
\]
For each irreducible \(i\), the number \(120m_i(n)/d_i\) is a Gram eigenvalue, with multiplicity \(d_i^2\). The remaining \(120-\sum_{m_i(n)>0}d_i^2\) eigenvalues are zero. Thus
\[
\operatorname{rank}G_n=\sum_{i:m_i(n)>0}d_i^2.
\]
The convention is that a zero multiplicity contributes no positive eigenvalue. The recurrence is an exact, indefinitely evaluable formula, not an asymptotic approximation.

The first sixty ranks, indexed from degree zero to 59 in six successive rows of ten, are

```text
 1,  4,  9, 16, 25, 36, 25, 40, 41, 52
43, 56, 51, 60, 59, 52, 50, 56, 59, 60
60, 56, 59, 60, 60, 60, 59, 56, 59, 60
60, 60, 60, 60, 59, 60, 60, 60, 59, 60
60, 60, 60, 60, 60, 60, 59, 60, 60, 60
60, 60, 60, 60, 60, 60, 60, 60, 59, 60
```

The all-degree reduction follows from the exact matrix identity
\[
G_{n+60}=G_n+60\bigl(I+(-1)^nP\bigr).
\]

## Assumptions and scope

The vertex configuration is the **full** 120-point 600-cell, normalized to the unit sphere, not merely 60 unoriented vertices. Spherical harmonics are complex-valued, homogeneous, harmonic polynomials restricted to \(S^3\) and of **exact** degree \(n\), a space of dimension \((n+1)^2\). The inner product is the ordinary Euclidean one in \(\mathbb R^4\). The Gram normalization is \(G_n(x,y)=U_n(\langle x,y\rangle)\), whose diagonal equals \(n+1\). The equal-weight reproducing kernel relative to normalized Haar measure on \(S^3\) is \((n+1)G_n\). Changing this convention rescales nonzero eigenvalues but does not change rank.

The binary icosahedral group \(2I\) acts by left multiplication on its 120 unit quaternions; its fundamental two-dimensional complex representation is the defining one inherited from \(SU(2)\). The three representation labels of equal dimensions remain distinct; they are fixed by the **specified McKay adjacency**, not interchangeable by dimension alone.

## Proof

**1. Harmonic kernel and finite-group restriction.** Identify \(S^3\) with \(SU(2)\). The degree-\(n\) Laplace eigenspace is the span of matrix coefficients of the \((n+1)\)-dimensional irreducible \(SU(2)\)-module \(V_n=\operatorname{Sym}^{n}(\mathbb C^2)\). Its character is
\[
\chi_n(g^{-1}h)=U_n\!\left(\frac12\operatorname{tr}(g^{-1}h)\right)=U_n(\langle g,h\rangle).
\]
The addition formula with normalized Haar measure gives reproducing kernel \((n+1)\chi_n(g^{-1}h)\). Consequently, \(G_n\) has exactly the rank of restriction/evaluation of degree-\(n\) harmonics to \(2I\).

Write \(V_n|_{2I}=\bigoplus_i m_i(n)\rho_i\), with dimensions \(d_i\). Convolution on \(\mathbb C[2I]\) by \(\chi_n\) has, by the finite-group character orthogonality relations, scalar \(|2I|m_i(n)/d_i=120m_i(n)/d_i\) on every \(\rho_i\)-matrix coefficient; this is a \(d_i^2\)-dimensional subspace of the regular representation. This proves the claimed complete spectrum, nonnegativity, and rank formula, including the zero eigenspace.

**2. Recurrence.** The binary icosahedral McKay graph for the defining two-dimensional module is affine \(E_8\), with the displayed dimension labels, nodes, and edges (see Dechant, cited below). The Clebsch–Gordan rule \(V_1\otimes V_n\cong V_{n+1}\oplus V_{n-1}\) gives the displayed vector recurrence, initialized by the trivial and defining modules. This determines all integers exactly. Every multiplicity is nonnegative by its representation-theoretic meaning. The dimensions satisfy \(2d_i=\sum_{j\sim i}d_j\), confirming the graph's dimension compatibility.

**3. Sixty-step identity.** The distinct inner products of a fixed vertex with the 600-cell are \(\pm1,0,\pm\frac12,\pm\frac{1+\sqrt5}{4},\pm\frac{\sqrt5-1}{4}\). Write each interior value as \(\cos\alpha\), with \(\alpha\) an integer multiple of \(\pi/2,\pi/3,\pi/5\), respectively. The identity \(U_n(\cos\alpha)=\sin((n+1)\alpha)/\sin\alpha\) shows \(U_{n+60}(t)=U_n(t)\) at every interior inner product. At \(t=1\), the value increases by 60; at \(t=-1\), it increases by \(60(-1)^n\). Hence the exact matrix identity above. The antipodal parity subspace has dimension 60 and receives an eigenvalue shift of 120; the other parity subspace is annihilated for both degrees. Equivalently, for all degrees,
\[
m_i(n+60)=m_i(n)+d_i\,\mathbf 1_{\{(-1)^n=\rho_i(-1)\}},
\]
where the sign of the central element on the nine labels is \((+,-,+,-,+,-,+,-,+)\). This also follows by the character orthogonality formula.

**4. Sharp ranks.** Exact integer recurrence evaluation for the sixty initial degrees produces the table above; the standalone script `verify.py` recomputes it from the nine-node diagram, without preloaded ranks. The shift then proves that every parity-compatible irreducible appears for \(n\ge60\), so the rank is 60 for every such degree. The initial list shows every odd \(n\ge29\) is already full rank, but \(n=27\) has rank 56; it also shows \(n=58\) has rank 59, so **no even eventual-full threshold less than 60** is possible. At \(n=58\), the nonzero representation multiplicities are \((0,0,3,0,5,0,4,0,3)\), and at \(n=59\), they are \((0,2,0,4,0,6,0,2,0)\); the eigenvalue formula gives 120 for every nonzero eigenvalue in these two cases. Together with antipodal parity and spectral rank, this yields \(G_{59}=60(I-P)\) and the claimed degree-58 spectrum.

## Verification

Run `python3 verify.py` using Python 3 (standard library only). It independently constructs a 120-point coordinate model from 8 coordinate-axis vertices, 16 half-sign vertices, and 96 golden-ratio vertices; over the exact finite field \(\mathbf F_{101}\) with \(\sqrt5=45\), it checks that they are distinct, unit norm, and have the prescribed nine distances. It directly forms \(120\)-by-\(120\) Chebyshev Gram matrices, computes exact modular ranks for all \(0\le n\le60\), and checks equality against ranks from the McKay recursion. It also checks dimension identities, multiplicities through degree 120, and the 60-shift recurrence through degree 120. Expected outputs are four `PASS` lines, including the complete rank list.

Finite-field rank agreement is only a *supplementary certificate* for the listed degrees, not a proof over \(\mathbb C\) or of all degrees. The representation-theoretic and Chebyshev steps give the complete characteristic-zero proof for every \(n\ge0\).

## Relationship to prior work

Mamone–Pileio–Levitt (2010) study orientational quadrature on regular four-polytopes and show the 600-cell's vanishing spherical moments (a degree-by-degree **averaging** property) using group symmetry. Boyvalenkov–Danev (2001) prove uniqueness of the 120-point spherical 11-design. Dechant (2013) develops the 600-cell / binary-icosahedral / affine-\(E_8\) relationship. Hirao–Nozaki–Tasaka (2025), Theorem 1.2(iii), give the complete **harmonic-strength** list, detecting the presence of invariant scalar averaging modes; in particular their result already implies vanishing averages at degree 58. None of these examined statements supplies the nine-representation evaluation Gram spectrum, all-degree ranks, or sharp *interpolation* (not quadrature) thresholds. The result uses standard Peter–Weyl and McKay machinery but assembles it into a different sharp sampling classification.

## Limitations

The rank classification is for exact-degree spherical harmonics at the 120 vertices, not a low-pass direct sum, perturbed sites, or a different finite subgroup. It does not assert novelty of the individual design-strength or invariant-harmonic vanishing facts, already known from the cited literature. A claim of priority is necessarily bounded by the sources inspected; an unindexed earlier character-table computation could imply the same rank profile. The supplied checker uses an exact finite field and does not independently prove the representation-theoretic identities. No independent external validation has been performed.

## References

1. S. Mamone, G. Pileio, M. H. Levitt, “Orientational Sampling Schemes Based on Four Dimensional Polytopes,” *Symmetry* **2** (2010), 1423–1449, DOI: `10.3390/sym2031423` (published 2010-07-07).
2. P. Boyvalenkov, D. Danev, “Uniqueness of the 120-point spherical 11-design in four dimensions,” *Archiv der Mathematik* **77** (2001), 360–368, DOI: `10.1007/PL00000504`.
3. P.-P. Dechant, “Platonic solids generate their four-dimensional analogues,” *Acta Crystallographica A* **69** (2013), 592–602; arXiv `1307.6768` (first posted 2013-07-25).
4. M. Hirao, H. Nozaki, K. Tasaka, “Spherical designs for finite quaternionic unit groups and their applications to modular forms,” arXiv `2507.01358` (first posted 2025-07-02), Theorem 1.2(iii).
