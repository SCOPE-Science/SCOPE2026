# Every integer \(-r\), for \(r\ge3\), is a flat band of a connected two-site unweighted periodic graph

## Finding
For every integer \(r\ge3\), there exists a connected, simple, locally finite, unweighted \(\mathbb Z\)-periodic graph with exactly two vertex orbits and no potential, whose adjacency operator has a flat band at energy \(\lambda=-r\). The flat band is the bottom of the spectrum, is the only flat band, and has an explicit nonzero compactly supported eigenfunction. Thus there is no lower bound on the negative flat-band energies attainable with only two vertices in a fundamental cell when finite-range hopping is allowed to depend on \(r\).

An explicit construction, valid for every \(r\ge2\), is given below. Its edge degree is \(2r^2-r\). For \(r=3\), the example has flat-band energy \(-3\), contradicting the possibility—raised as a question, not claimed as a theorem—in Sabri and Youssef, Section 5.2, that two-orbit flat bands might be restricted to \(0,-1,-2\).

## Assumptions and scope
Fix an integer \(r\ge3\), and put
\[
U_r=\{2^j-1:0\le j<r\},\qquad M_r=2^r,\qquad V_r=M_rU_r.
\]
All sets in the following construction are ordinary sets of integers, not multisets. Define
\[
I_{AA}=(U_r-U_r)\setminus\{0\},\qquad
I_{BB}=(V_r-V_r)\setminus\{0\},\qquad
I_{AB}=U_r+V_r,\qquad I_{BA}=-I_{AB}.
\]
The vertex set is \(\{A_n,B_n:n\in\mathbb Z\}\). There is an undirected edge from \(X_n\) to \(Y_{n+k}\) if and only if \(k\in I_{XY}\). Identical undirected edges are included only once. Every edge has hopping weight exactly one; there are no vertex potentials, self-loops, or multiple edges. The adjacency operator \(H_r\) is
\[
(H_r\psi)_X(n)=\sum_{Y\in\{A,B\}}\sum_{k\in I_{XY}}\psi_Y(n+k),\qquad X\in\{A,B\}.
\]
Each hopping set is finite, so this is a bounded self-adjoint operator on \(\ell^2(\mathbb Z)\oplus\ell^2(\mathbb Z)\). The theorem concerns graph adjacency, not a graph Laplacian or an arbitrary weighted tight-binding model. The number of edges and the maximal hopping distance increase with \(r\).

## Proof
**1. Unique differences and sums.** Every positive difference of two distinct elements of \(U_r\) has the form
\[
(2^a-1)-(2^b-1)=2^b(2^{a-b}-1),\quad 0\le b<a<r.
\]
The factor in parentheses is odd. Therefore the exact \(2\)-adic valuation recovers \(b\), and dividing by \(2^b\) recovers \(a-b\); hence all ordered nonzero differences of \(U_r\) are distinct. Scaling by \(M_r\) gives the same property for \(V_r\). Moreover, all differences in \(V_r-V_r\) are divisible by \(M_r\), whereas every nonzero difference in \(U_r-U_r\) has absolute value strictly less than \(M_r\). Consequently
\[
(U_r-U_r)\cap(V_r-V_r)=\{0\}.
\]
If \(u+v=u'+v'\), with \(u,u'\in U_r\) and \(v,v'\in V_r\), then \(u-u'=v'-v\) belongs to this intersection, so \(u=u'\) and \(v=v'\). Thus \(U_r+V_r\) has exactly \(r^2\) distinct elements. It follows that every nonzero difference in either within-orbit set, and every cross-orbit sum, appears with coefficient exactly one in its respective generating polynomial.

**2. The graph is connected, simple, and regular.** The displacement \(1\) belongs to \(I_{AA}\) because \(0,1\in U_r\). Therefore all \(A_n\) lie in a connected infinite path. Also \(0\in I_{AB}\), so every \(B_n\) is joined to \(A_n\). Connectivity follows. The within-orbit displacement sets are symmetric and avoid zero, and the cross-orbit displacement sets are negatives of one another; hence the graph is undirected and loopless. By Step 1, \(|I_{AA}|=|I_{BB}|=r(r-1)\) and \(|I_{AB}|=r^2\), so it is \((2r^2-r)\)-regular. Unique displacement labels preclude parallel edges.

**3. Exact rank-one Floquet factorization.** Put
\[
u_r(z)=\sum_{u\in U_r}z^u,\qquad v_r(z)=\sum_{v\in V_r}z^v.
\]
Write \(f_A(z)=\sum_{k\in I_{AA}}z^k\), \(f_B(z)=\sum_{k\in I_{BB}}z^k\), and \(g(z)=\sum_{k\in I_{AB}}z^k\). Step 1 proves the exact Laurent identities
\[
f_A(z)+r=u_r(z)u_r(z^{-1}),\quad
f_B(z)+r=v_r(z)v_r(z^{-1}),\quad
g(z)=u_r(z)v_r(z).
\]
For \(|z|=1\), the Hermitian Floquet adjacency matrix is therefore
\[
\begin{aligned}
H_r(z)+rI_2
&=\begin{pmatrix}u_r(z)u_r(z^{-1})&u_r(z)v_r(z)\\
u_r(z^{-1})v_r(z^{-1})&v_r(z)v_r(z^{-1})\end{pmatrix}\\
&=\begin{pmatrix}u_r(z)\\v_r(z^{-1})\end{pmatrix}
\begin{pmatrix}u_r(z^{-1})&v_r(z)\end{pmatrix}.
\end{aligned}
\]
This matrix is positive semidefinite and has rank at most one for every quasimomentum. Thus \(-r\) is an eigenvalue at every quasimomentum, and no spectral energy lies below \(-r\). The nonzero Laurent-polynomial vector
\[
\Phi_r(z)=\begin{pmatrix}v_r(z)\\-u_r(z^{-1})\end{pmatrix}
\]
is annihilated by the second rank-one factor. Inverse Fourier transformation gives a compactly supported eigenvector. In the convention \(\widehat\psi(z)=\sum_n z^{-n}\psi(n)\), one may take
\[
\psi_A(n)=\mathbf1_{\{-v:v\in V_r\}}(n),\qquad
\psi_B(n)=-\mathbf1_{U_r}(n).
\]
This is nonzero and finitely supported. Translates with sufficiently separated supports are linearly independent, proving infinite eigenvalue multiplicity on the infinite graph.

**4. Uniqueness of the flat band.** The other fiber eigenvalue is
\[
\mu_r(z)=|u_r(z)|^2+|v_r(z)|^2-r\quad(|z|=1).
\]
At \(z=1\), \(\mu_r(1)=2r^2-r\). At every \(z\ne1\) on the unit circle, the terms \(1\) and \(z\) both occur in \(u_r(z)\), so \(|u_r(z)|<r\). Since \(|v_r(z)|\le r\), \(\mu_r(z)<2r^2-r\). Therefore the second band is nonconstant. No other energy is a flat band.

**5. The first new energy.** For \(r=3\),
\[
U_3=\{0,1,3\},\quad V_3=\{0,8,24\},\quad
I_{AA}=\{\pm1,\pm2,\pm3\},\quad
I_{BB}=\{\pm8,\pm16,\pm24\},
\]
\[
I_{AB}=\{0,1,3,8,9,11,24,25,27\}.
\]
This connected simple \(15\)-regular graph has a bottom flat band at \(-3\) with a compact eigenvector on six vertices. The same proof works for every larger \(r\). Because the induced two-vertex cell graph has spectrum contained in \(\{-1,0,1\}\), the flat band at \(-r\) cannot be realized by an eigenfunction supported on one cell when \(r\ge3\).

## Verification
The self-contained standard-library program `artifacts/verify.py` reproduces the integer set construction for \(2\le r\le8\), checks uniqueness of differences and sums, verifies the exact Laurent-polynomial determinant identity, and checks the compact eigenvector directly against the finite-support adjacency recurrence. On execution with Python 3 it returns `VERIFY_OK exact_Laurent_and_compact_eigenvector r=2..8`. The universal result is proved by the valuation and factorization arguments above, not inferred from these finite checks.

## Relationship to prior work
Sabri and Youssef, *Flat bands of periodic graphs*, arXiv:2304.06465, Section 5, show that every two-orbit unweighted adjacency flat band must be an integer and ask explicitly whether energies other than \(0,-1,-2\) can arise. Their Section 3 generation theorem uses more vertices per fundamental cell; it does not provide the present two-orbit construction. The rank-one factorization here exploits unique-difference sets to make every nonconstant coefficient exactly zero or one, as required for a simple unweighted graph. Their Section 5 coefficient identities give \(\lambda^2=|I_{AB}|-|I_{AA}\cap I_{BB}|\); this construction has \(|I_{AB}|=r^2\) and an empty intersection, consistently yielding \(\lambda=-r\).

Faust and Kachkovskiy, arXiv:2509.01927, Theorem 1.4, establish generic absence of flat bands under variation of onsite potentials on fixed connected periodic graphs. Generic absence neither excludes nor determines flat bands for the specified zero potential, so it does not cover the present explicit family. The result is also distinct from weighted multi-band engineering constructions, which do not impose simple-graph zero-one coefficients and a two-vertex motif.

## Limitations
This is an existence theorem, not a characterization of every flat-band energy attainable with two vertex orbits. It does not show whether positive integers can occur. Hopping distances grow exponentially in \(r\); the graphs are not constrained to nearest-neighbor hopping, planarity, or uniformly bounded degree. Although \(-r\) is the spectral bottom, no positive gap above it is asserted. Literature searches cannot rule out a differently indexed equivalent family, and no independent external validation has been performed.

## References
1. M. Sabri and P. Youssef, *Flat bands of periodic graphs*, arXiv:2304.06465 (first version 13 April 2023), especially Sections 1.2, 3 and 5, and Section 5.2's two-orbit question; https://arxiv.org/pdf/2304.06465.
2. M. Faust and I. Kachkovskiy, *Absence of flat bands for discrete periodic graph operators with generic potentials*, arXiv:2509.01927 (2025), Theorem 1.4; https://arxiv.org/pdf/2509.01927.
3. A. Graf and F. Piéchon, *Designing flat-band tight-binding models with tunable multifold band touching points*, Physical Review B 104, 195128 (2021), DOI:10.1103/PhysRevB.104.195128 (different, weighted-model design scope).
