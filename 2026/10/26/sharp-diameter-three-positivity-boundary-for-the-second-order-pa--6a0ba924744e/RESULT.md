# Sharp diameter-three positivity boundary for the second-order Padé heat step on trees

## Finding
For **every** finite, simple, connected, unweighted tree \(T\) with at least two vertices, let \(L_T=D_T-A_T\) be its combinatorial Laplacian. The second-order subdiagonal Padé heat update is
\[
P_T(h)=\left(I+hL_T+\tfrac12h^2L_T^2\right)^{-1},\qquad h>0.
\]
Then the following conditions are equivalent:

1. \(P_T(h)\) is entrywise nonnegative for **every** \(h>0\);
2. \(P_T(h)\) is entrywise strictly positive for **every** \(h>0\);
3. \(\operatorname{diam}(T)\le3\).

Consequently this update preserves the positive cone, the discrete maximum principle, and maximum-norm contractivity at every positive step size exactly on trees of diameter at most three. For each tree with diameter at least four, every pair of vertices at distance four has
\[
(P_T(h))_{uv}=-\tfrac14h^4+O_T(h^5)\quad(h\downarrow0),
\]
so this tree cannot have unconditional positivity. The finite-degree algebraic certificate in `certificate.json` proves positivity on **all** double stars, including arbitrary and unequal leaf multiplicities.

## Assumptions and scope
The graph is a finite, simple, undirected, unweighted tree; there is no boundary absorption, mass rescaling, arbitrary edge weight, or directed transition. The Laplacian has zero row sums and nonpositive off-diagonal entries. The update is the exact \([0/2]\) Padé rational function of this Laplacian, not the \([2/2]\) Gauss or \([1/1]\) Crank–Nicolson step. Strict positivity means each matrix entry is \(>0\), not positive definiteness (the matrix also happens to be positive definite). Constants implicit in the small-step remainder may depend on the finite tree.

## Proof
**Spectral and normalization facts.** The scalar function \(r(z)=(1+z+z^2/2)^{-1}\) is strictly positive on \([0,\infty)\). As \(L_T\) is real symmetric positive semidefinite, \(P_T(h)=r(hL_T)\) is symmetric positive definite, so its diagonal entries are positive. Also \(L_T\mathbf1=0\) and \(r(0)=1\), hence \(P_T(h)\mathbf1=\mathbf1\). Therefore entrywise nonnegativity is equivalent to row-wise absolute sums of at most one and to maximum-norm contractivity. The rational function has the exact local expansion
\[
r(z)=1-z+\tfrac12z^2-\tfrac14z^4+O(z^5),
\]
with a zero cubic term.

**Obstruction at distance four.** If \(d_T(u,v)=4\), then \((L_T^j)_{uv}=0\) for \(0\le j<4\), since multiplying once by \(L_T\) changes vertex location by at most one edge. At order four, only nearest-neighbor moves can connect \(u\) and \(v\), and a tree has exactly one shortest four-edge route. Thus \((L_T^4)_{uv}=1\). Substitution into the rational expansion yields the asserted negative \(-h^4/4+O_T(h^5)\). A tree of diameter at least four contains such a pair.

**Trees of diameter one or two.** A two-vertex tree has \(P_T(h)_{12}=(1-r(2h))/2>0\). Every larger tree of diameter two is a star with \(m\ge2\) leaves. Its distinct hub–leaf entry is \((1-r((m+1)h))/(m+1)>0\), and its distinct leaf–leaf entry is
\[
\frac{m+r((m+1)h)-(m+1)r(h)}{m(m+1)}>0.
\]
The last inequality follows from strict convexity, since
\[
r''(z)=\frac{1+3z+\tfrac32z^2}{(1+z+z^2/2)^3}>0\quad(z\ge0),
\]
and \(h=\frac{m}{m+1}\cdot0+\frac1{m+1}(m+1)h\).

**Trees of diameter three (the nontrivial direction).** Any such tree is the double star \(D_{a,b}\) consisting of adjacent hubs, one with \(a\ge1\) leaves and the other with \(b\ge1\) leaves. On vectors constant separately on the four cells (hub \(U\), hub \(V\), the \(a\) leaves of \(U\), the \(b\) leaves of \(V\)), the Laplacian acts by
\[
M=\begin{pmatrix}a+1&-1&-a&0\\-1&b+1&0&-b\\-1&0&1&0\\0&-1&0&1\end{pmatrix}.
\]
Define \(Q=I_4+hM+\frac12h^2M^2\), \(\Delta=\det Q\), \(J=\operatorname{adj}Q\), \(s=h^2+2h+2\). The invariant four-cell subspace is similar to a symmetric positive-semidefinite Laplacian restriction, hence \(\Delta>0\) for \(a,b,h>0\). The orthogonal complements of constant vectors in either leaf class are Laplacian-eigenspaces of eigenvalue one.

Every off-diagonal entry joining different cells is a positive class-size multiple of one of \(J_{01},J_{02},J_{03},J_{12},J_{13},J_{23}\), divided by \(\Delta\). For two distinct leaves on the first hub, the entry is exactly
\[
\frac{(sJ_{22}-2\Delta)/a}{s\Delta},
\]
and the other hub gives \((sJ_{33}-2\Delta)/(bs\Delta)\). These are all possible types of distinct matrix entries.

Here is a finite **exact** algebraic sign certificate. Expand the following eight expressions as polynomials in \(a,b,h\), with rational coefficients:
\[
J_{01},\ J_{02},\ J_{03},\ J_{12},\ J_{13},\ J_{23},\quad
\frac{sJ_{22}-2\Delta}{a},\quad\frac{sJ_{33}-2\Delta}{b}.
\]
They have respectively \(18,22,15,15,22,10,28,28\) **strictly positive, nonzero coefficients**, with respective lowest powers of \(h\) equal to \(1,1,2,2,1,4,2,2\). Their complete coefficient tables, including all rational numerators and denominators, are provided in `certificate.json`. The standalone `verify.py` recomputes each polynomial directly from the four displayed matrices, compares **every coefficient** with the tables, and checks every coefficient's exact sign. This finite identity is a proof for the entire unbounded integer range \(a,b\ge1\), not a numerical sampling argument. Since \(a,b,h>0\), all eight expressions are strictly positive. With positive diagonals, \(P_T(h)\) is entrywise strictly positive.

The preceding cases exhaust all trees with diameter at most three, completing all equivalences.

## Verification
Run `python verify.py --check` from the extracted package directory with SymPy installed. This independently reconstructs the quotient matrix and eight numerator polynomials, compares their full rational-coefficient expansions against `certificate.json`, and tests positivity of every coefficient. It additionally checks 12 direct exact-rational inverses of independently constructed double-star Laplacians, the negative fourth-distance coefficient and a small-step negative entry on the five-vertex path, the zero cubic term, and the strict-convexity derivative identity. The exact output from the run is in `verification-output.txt`. Computational spot checks are ancillary; the algebraic coefficient identity and graph-distance argument establish the infinite-family result.

## Relationship to prior work
Schatz, Thomée and Wahlbin study precisely this \([0/2]\) Padé function for a uniform one-dimensional lumped-mass finite-element discretization of the heat equation. Their Theorem 6.7 establishes small-step negativity of a fourth-diagonal entry whenever the discrete interval has more than four interior vertices; their formula for the scalar Padé function and its non-positive-type integral kernel is also directly pertinent. Their Theorems 6.8–6.9 establish eventual contractivity and positivity at large time steps for that different Dirichlet operator. The fourth-distance Taylor coefficient and its path-specific obstruction are **already part of prior theory** and are not asserted to be new here. The contribution assessed here is the global classification for every finite **Neumann/combinatorial tree Laplacian**, especially all unequal double stars at every step size, and the exact iff diameter boundary. Thomée and Wahlbin's earlier work on discrete parabolic maximum principles motivates the positivity question but does not classify this Padé tree update. No claim is made that the general positivity/non-complete-monotonicity principles are new.

## Limitations
The theorem does not cover weighted trees, graphs with cycles, nonsymmetric generators, alternative boundary conditions, or Padé formulas of other orders. For trees of diameter at least four, it proves failure at sufficiently small steps, **not** negativity at every step; the large-step matrix may become positive. The exhaustive positive-coefficient proof uses a finite symbolic algebra certificate that readers may replay or manually inspect. Originality is assessed against the inspected primary source and available similarity searches; specialized unindexed historical literature may contain equivalent statements. No independent mathematical audit has been carried out.

## References
1. A. H. Schatz, V. Thomée and L. B. Wahlbin, *On positivity and maximum-norm contractivity in time stepping methods for parabolic equations*, Computational Methods in Applied Mathematics **10** (2010), 421–443, DOI: 10.2478/cmam-2010-0025, particularly Section 2 and Theorems 6.7–6.9.
2. V. Thomée and L. B. Wahlbin, *On the existence of maximum principles in parabolic finite element equations*, Mathematics of Computation **77** (2008), 11–19; first electronically public May 14, 2007; DOI: 10.1090/S0025-5718-07-02021-2.
