# Irreducible spectral resonance factors of Grassmannian critical-value discriminants

## Finding
For all integers \(n\ge2\) and \(1\le k<n\), there is an exact, irreducible-factor decomposition of the **formal critical squared-distance discriminant** for Euclidean distance to the projection Grassmannian. The factors classify both repeated eigenvalues and coincident critical distances between distinct spectral subspaces. Unlike the familiar ED discriminant, the latter coincidences occur for matrices with simple eigenvalues.

Let \(N=\binom nk\), \(m=\min(k,n-k)\), and write \(\lambda_1,\ldots,\lambda_n\) for the roots of the characteristic polynomial of the symmetric datum. Put
\[
\Delta_n=\prod_{1\le i<j\le n}(\lambda_i-\lambda_j)^2.
\]
For each integer \(2\le r\le m\), let \(\mathcal U_{n,r}\) consist of **unordered** pairs \(\{A,B\}\) of disjoint \(r\)-element subsets of \(\{1,\ldots,n\}\). Orient each pair by choosing the lexicographically smaller ordered tuple first and define
\[
T_{n,r}=\prod_{\{A,B\}\in\mathcal U_{n,r}}
\left(\sum_{a\in A}\lambda_a-\sum_{b\in B}\lambda_b\right).
\]
Then \(T_{n,r}\) is a symmetric polynomial, irreducible as an element of the **universal spectral coefficient ring** \(\mathbb C[e_1,\ldots,e_n]\), and has degree
\[
D_{n,r}=\frac12\binom nr\binom{n-r}r.
\]
The ordinary eigenvalue discriminant \(\Delta_n\) is irreducible in this ring, and the monic critical-value polynomial has discriminant
\[
\boxed{\operatorname{Disc}_t(F_{n,k})=
4^{\binom{N}{2}}\Delta_n^{\binom{n-2}{k-1}}
\prod_{r=2}^{m}T_{n,r}^{2\binom{n-2r}{k-r}}.}
\]
An empty product is \(1\). The reduced locus in spectral coefficient space therefore has exactly \(m\) distinct irreducible hypersurface components. Away from repeated eigenvalues, the component \(T_{n,r}=0\) has, at a generic point, precisely \(\binom{n-2r}{k-r}\) *disjoint double coincidences* among its \(N\) critical values and no other coincidences.

For \((n,k)=(4,2)\), writing \(e_j\) for the elementary symmetric polynomial of spectral roots, the new component is the cubic
\[
T_{4,2}=e_1^3-4e_1e_2+8e_3,
\qquad
\operatorname{Disc}_t(F_{4,2})=4^{15}\Delta_4^2T_{4,2}^2.
\]
For the real diagonal matrix with eigenvalues \((0,1,2,3)\), the eigenvalues are distinct but the six critical squared distances, ordered increasingly, are \((6,8,10,10,12,14)\). Hence the cubic is genuinely distinct from the repeated-eigenvalue locus.

## Assumptions and scope
The ground field is \(\mathbb C\), the matrix \(Q\) is any symmetric \(n\times n\) matrix, and the bilinear Frobenius objective is \(d_Q(P)=\operatorname{tr}((P-Q)^2)\) on
\[
\operatorname{pGr}(k,n)=\{P\in\operatorname{Sym}_n(\mathbb C):P^2=P,\ \operatorname{tr}P=k\}.
\]
For a simple-spectrum \(Q\), its \(N\) critical points are the projections onto the spectral \(k\)-planes. If \(I\) indexes such a point, its value is
\[
v_I=k+\operatorname{tr}(Q^2)-2\sum_{i\in I}\lambda_i.
\]
Define \(F_{n,k}(t;Q)=\prod_{|I|=k}(t-v_I)\), a symmetric expression in the spectral roots, hence a polynomial in \(t\) and the entries of \(Q\). On the repeated-eigenvalue locus this polynomial is its canonical **algebraic continuation**; its roots should not be interpreted as distinct actual critical points there. We work in \(\mathbb C[e_1,\ldots,e_n]\), the polynomial ring of free universal characteristic coefficients. Irreducibility is **not** asserted after specialization or pullback to all symmetric matrix entries.

## Proof
**1. Critical points and values.** The tangent space at \(P\) to the orthogonal orbit of rank-\(k\) projections consists of \([\Omega,P]\) for skew-symmetric \(\Omega\). Differentiation gives \(\operatorname{tr}(Q[\Omega,P])=\operatorname{tr}([P,Q]\Omega)\). Nondegeneracy of the trace form on skew-symmetric matrices shows stationarity exactly when \([P,Q]=0\). When \(Q\) has distinct eigenvalues, its eigenspaces are mutually orthogonal and nonisotropic, so commuting idempotents are precisely the \(N\) spectral \(k\)-plane projectors. As \(P^2=P\), \(\operatorname{tr}(P)=k\), and \(d_Q(P)=k+\operatorname{tr}(Q^2)-2\operatorname{tr}(PQ)\), the stated values follow. The polynomial identity then extends from the open simple-spectrum locus to all coefficient values.

**2. Partition of colliding pairs.** Take an unordered pair \(\{I,J\}\) of different \(k\)-subsets. It has a unique decomposition \(I=A\sqcup C\) and \(J=B\sqcup C\), where \(A,B\) are nonempty disjoint \(r\)-subsets, \(C=I\cap J\), and \(r=|I\setminus J|=|J\setminus I|\le m\). Then
\[
(v_I-v_J)^2=4\left(\sum_{a\in A}\lambda_a-\sum_{b\in B}\lambda_b\right)^2.
\]
For each unordered disjoint pair \(\{A,B\}\), there are exactly \(\binom{n-2r}{k-r}\) choices of \(C\). Because the monic polynomial discriminant is the product of the squared differences over all \(\binom N2\) unordered pairs, the factorization and the full power of \(4\) follow. For \(r=1\), the unordered-pair product squared is exactly \(\Delta_n\). For \(r\ge2\), it is \(T_{n,r}^2\).

**3. The symmetric-factor and irreducibility lemma.** Let \(r\ge2\). Each linear factor defining \(T_{n,r}\) is a distinct linear polynomial up to a sign; a support with \(r\) positive and \(r\) negative coefficients identifies its unordered pair uniquely. The symmetric group \(S_n\) permutes this set transitively. Therefore every permutation sends \(T_{n,r}\) to \(\pm T_{n,r}\), defining a one-dimensional character of \(S_n\). For \(n\ge4\), the only characters are trivial and sign. The sign character would force the polynomial to vanish on \(\lambda_i=\lambda_j\) for every transposition, so every difference \(\lambda_i-\lambda_j\) would divide \(T_{n,r}\). This is impossible: all defining factors have \(2r\ge4\) nonzero variable coefficients. Thus \(T_{n,r}\) is invariant and belongs to \(\mathbb C[e_1,\ldots,e_n]\). If this invariant factored in that coefficient ring, unique factorization in \(\mathbb C[\lambda_1,\ldots,\lambda_n]\) would partition its distinct linear factors into a nonempty proper \(S_n\)-invariant subset, contradicting transitivity. It is irreducible, and has exactly \(D_{n,r}=|\mathcal U_{n,r}|\) factors. The same orbit argument applied to the square of the Vandermonde shows that \(\Delta_n\) is irreducible in \(\mathbb C[e_1,\ldots,e_n]\): a proper invariant factor could only be the Vandermonde to the first power, which transforms by sign. The defining hyperplane supports also show that all \(\Delta_n,T_{n,2},\ldots,T_{n,m}\) are distinct irreducibles.

**4. Sharp local collision portrait.** Fix an oriented disjoint pair \(A,B\) of cardinality \(r\ge2\). Its linear equation \(\sum_A\lambda=\sum_B\lambda\) is distinct from every other resonance and eigenvalue-equality hyperplane. A real point on this hyperplane can therefore be chosen outside their finite union; the corresponding spectrum is simple. At that point the *only* coincident \(k\)-subset sums are those attached to the chosen \(\{A,B\}\), obtained by adjoining a common \(C\) of size \(k-r\) from the complement. These yield \(\binom{n-2r}{k-r}\) disjoint pairs; all other subset sums are distinct. The same holds on a dense open subset of the irreducible quotient hypersurface \(T_{n,r}=0\). This proves that every factor represents genuine distinct-critical-point collisions and explains its discriminant exponent.

**5. Four-dimensional cubic.** The three factors of \(T_{4,2}\) are \((\lambda_1+\lambda_2-\lambda_3-\lambda_4)\), \((\lambda_1+\lambda_3-\lambda_2-\lambda_4)\), and \((\lambda_1+\lambda_4-\lambda_2-\lambda_3)\). Expanding gives \(e_1^3-4e_1e_2+8e_3\). The asserted six distances follow by evaluating all two-subset sums of \((0,1,2,3)\).

## Verification
Run \(\texttt{python3 verify.py}\) using a standard Python 3 interpreter. The exact-arithmetic program checks all \((n,k)\) with \(4\le n\le7\) and \(1\le k<n\), using both powers-of-two and consecutive-integer spectra; it compares both sides of the full discriminant identity, checks factor counts, checks the four-root cubic at an additional rational specialization, and checks the distinct-spectrum collision example. It reports `VERIFY_OK`. A separate symbolic expansion independently establishes the cubic identity, and the general theorem is proved in Steps 1–5 rather than inferred from these finite tests.

## Relationship to prior work
Friedman–Hoşten–Rosana, *Euclidean Distance Optimization Within the Grassmannian* (arXiv:2610.02018v1, first public October 1, 2026), characterize the **ED discriminant**, where the number of stationary points ceases to be generic. Their Section 3 treats the repeated-eigenvalue equation \(\Delta_n=0\). The present result concerns the distinct invariant: **discriminant of the critical-value polynomial**, and classifies all additional irreducible spectral resonance factors, including their degrees, multiplicities, and generic coincidence counts. The earlier Friedman–Rosana–Sturmfels manuscript (arXiv:2601.22843v1) develops chordal distance and GD degree for lines but does not give this decomposition.

Breiding–Kohn–Sturmfels, *Metric Algebraic Geometry*, Chapter 7, especially Definition 7.18 and Theorem 7.20 (2024), establish the general offset-discriminant and bisector framework. In particular, separating critical-point degeneration from equal critical distances is **not** new. What is computed here is the complete explicit specialization to projection Grassmannians in the spectral coefficient ring and its irreducible, multiplicity-refined form. A related earlier result determines irreducibility of the eigenvalue-collision hypersurface in the full symmetric-matrix space, not these additional spectral-coefficient factors.

## Limitations
The scheme-theoretic factorization is in the universal coefficient ring \(\mathbb C[e_1,\ldots,e_n]\). No assertion is made that the pullback of each \(T_{n,r}\) to the affine space of matrix entries remains irreducible. No full classification of singular points of the resulting hypersurfaces is asserted. A collision of two stationary values need not be a tie between **global minima**; this is not a classification of the real medial axis. At matrices with repeated eigenvalues, formal roots of \(F_{n,k}\) need not be distinct actual stationary points. General resolvent/invariant theory could contain this factorization in a different vocabulary; this is the principal remaining bibliographic risk.

## References
1. H. Friedman, S. Hoşten, A. Rosana, *Euclidean Distance Optimization Within the Grassmannian*, arXiv:2610.02018v1 (2026), https://arxiv.org/html/2610.02018v1.
2. H. Friedman, A. Rosana, B. Sturmfels, *Distance Optimization in the Grassmannian of Lines*, arXiv:2601.22843v1 (2026), https://arxiv.org/html/2601.22843v1.
3. P. Breiding, K. Kohn, B. Sturmfels, *Metric Algebraic Geometry*, Chapter 7, *Reach and Offset* (2024), https://doi.org/10.1007/978-3-031-51462-3_7.
