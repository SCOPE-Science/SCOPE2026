# Exact two-coordinate-face concentration spectrum on Johnson slices

## Finding

Let \(n,k,L\) be integers with \(n\ge 2k\), \(k\ge2\), and \(0\le L\le k-1\). Let \(X=\binom{[n]}{k}\), with the uniform inner product, and let \(P_L\) denote orthogonal projection onto the sum of Johnson harmonic degrees \(0,1,\ldots,L\). For the coordinate face
\[
A=\{S\in X:\{1,2\}\subseteq S\},\qquad C_L=P_LM_{\mathbf1_A}P_L\big|_{\operatorname{ran}P_L},
\]
put \(d_t=\binom{n-2}{t}-\binom{n-2}{t-1}\) and, for \(0\le t\le k-1\),
\[
N_t=n-2t,\qquad K_t=k-t,\qquad
B_t=\frac{K_t(K_t-1)}{N_t(N_t-1)}.
\]
For \(0\le t\le k-2\), also define
\[
A_t=B_t+\frac{2(K_t-1)(N_t-K_t)}{N_t(N_t-2)}.
\]
The full spectrum, **with algebraic multiplicity**, is the following multiset. For \(L=0\), it is the singleton \(\{B_0\}\). For \(1\le L\le k-1\), it is
\[
\boxed{\quad
\{1^{[\binom{n-2}{L-2}]}\}\ \uplus\
\{A_{L-1}^{[d_{L-1}]}\}\ \uplus\
\{B_L^{[d_L]}\}\ \uplus\
\{0^{[\binom nL-\binom{n-2}{L-2}-d_{L-1}-d_L]}\}.
\quad}
\]
Here \(a^{[r]}\) means \(r\) copies of \(a\), \(\uplus\) is multiset union, and \(\binom uv=0\) if \(v<0\) or \(v>u\). In particular, \(B_{k-1}=0\), so copies of zero from different terms are combined. The rank is exactly
\[
\operatorname{rank}(C_L)=\binom{n-2}{\min(L,k-2)}.
\]
Every symmetric functional \(h\) satisfying \(h(0)=h(1)=0\) obeys, for \(L\ge1\),
\[
\operatorname{tr}h(C_L)=d_{L-1}h(A_{L-1})+d_Lh(B_L).
\]
Thus, in particular, the two nontrivial boundary eigenvalues give the entire binary spectral entropy for this face.

## Assumptions and scope

The vertices are \(k\)-subsets of \([n]=\{1,\dots,n\}\). The Johnson adjacency matrix joins two vertices when their symmetric difference has size two; its eigenvalues at degrees \(j=0,\ldots,k\) are \((k-j)(n-k-j)-j\), with degree-\(j\) eigenspace of dimension \(\binom nj-\binom n{j-1}\). The space \(\operatorname{ran}P_L\) consists exactly of restrictions of squarefree polynomials of degree at most \(L\) in the indicator coordinates; it has dimension \(\binom nL\). Multiplication \(M_{\mathbf1_A}\) uses the literal indicator of the two-coordinate face, not a Johnson-distance ball about a reference vertex. No normalization of the counting inner product changes the eigenvalues.

## Proof

**1. Harmonic lifts on the remaining coordinates.** Write \(m=n-2\) and \(Y=[n]\setminus\{1,2\}\). On functions indexed by \(s\)-subsets of \(Y\), define the up operator by \(U_sf(S)=\sum_{i\in S}f(S\setminus\{i\})\) for \(|S|=s+1\), and the down operator by \(D_sf(T)=\sum_{i\notin T}f(T\cup\{i\})\) for \(|T|=s-1\). For each \(0\le t\le\lfloor m/2\rfloor\), let \(\mathcal H_t=\ker D_t\). The up/down commutator at level \(s\) is \(D_{s+1}U_s-U_{s-1}D_s=(m-2s)I\). Therefore the lift
\[
h^{\uparrow\ell}(T)=\sum_{J\subseteq T,\ |J|=t}h(J),\qquad |T|=\ell,
\]
for \(h\in\mathcal H_t\) satisfies
\[
\sum_{|T|=\ell}|h^{\uparrow\ell}(T)|^2
=\binom{m-2t}{\ell-t}\sum_{|J|=t}|h(J)|^2.
\]
Different harmonic degrees give orthogonal lifts on every fixed level; \(\dim\mathcal H_t=\binom mt-\binom m{t-1}=d_t\). Lifts to unavailable levels are understood to be zero. These assertions follow inductively from the displayed commutator and the adjointness of up and down.

**2. The two-coordinate multiplicity space.** For \(S\in X\), set \(R(S)=|S\cap\{1,2\}|\in\{0,1,2\}\), and \(T=S\setminus\{1,2\}\). Fix a harmonic vector \(h\in\mathcal H_t\). The vectors symmetric under interchanging coordinates \(1,2\) have the form \(h^{\uparrow(k-R)}(T)q(R)\). Their squared norm, up to the common factor \(\|h\|^2/\binom nk\), is
\[
\sum_{r=0}^2\binom2r\binom{m-2t}{k-r-t}|q(r)|^2.
\]
By Vandermonde's identity, normalization turns these weights into the hypergeometric law of \(R\): two draws without replacement from a population of size \(N_t=m-2t+2\) with \(K_t=k-t\) marked elements. Multiplicities from distinct \(t\) are orthogonal by Step 1. Antisymmetric vectors under swapping coordinates \(1,2\) live only at \(R=1\); because \(\mathbf1_A=\mathbf1_{\{R=2\}}\), their concentration is zero.

The polynomial filtration and the harmonic lift decomposition give, in this symmetric copy of \(\mathcal H_t\), exactly the polynomials \(q(R)\) of degree at most \(L-t\), evaluated only at levels of positive weight. Indeed, symmetric monomials on the special pair are spanned by \(\binom R s\) for \(s=0,1,2\). A monomial of residual degree \(u\), when decomposed into residual harmonic lifts on level \(\ell=k-R\), has a degree-\(t\) harmonic coefficient polynomial in \(\ell\) of degree at most \(u-t\): this follows by induction on \(u\) using the displayed up/down commutator (the factors produced at each down-step are linear in \(\ell\)). Thus the harmonic degree-\(t\) coefficient of a total-degree-\(L\) monomial is a polynomial in \(R\) of degree at most \(L-t\). Conversely, multiply a harmonic polynomial of degree \(t\) by any polynomial in \(R\) of degree at most \(L-t\); its total degree is at most \(L\). The full degree filtration agrees with the Johnson eigenspace filtration in the assumptions. Consequently, the multiplicity-space calculation below applies independently with multiplicity \(d_t\).

**3. A rank-one compression.** Write \(p_2=\Pr(R=2)=B_t\). On the full scalar \(L^2\) space of this hypergeometric law, multiplication by \(\mathbf1_{\{R=2\}}\) is a rank-one orthogonal projection if \(p_2>0\); its only nonzero eigenvector is \(\mathbf1_{\{R=2\}}/\sqrt{p_2}\). Let \(Q_s\) be projection onto polynomials of degree at most \(s=L-t\). The unique potentially nonzero eigenvalue of its compression is
\[
\lambda_{t,s}=\frac{\|Q_s\mathbf1_{\{R=2\}}\|_{L^2}^2}{p_2}.
\]
For \(s=0\), this equals \(p_2=B_t\). For \(s\ge2\), the indicator is a polynomial of degree at most two on the three possible values \(0,1,2\), so the eigenvalue is \(1\). For \(s=1\), the first two orthogonal polynomials are \(1\) and \(R-\mu\), where
\[
\mu=\frac{2K_t}{N_t},\qquad
\sigma^2=\frac{2K_t(N_t-K_t)(N_t-2)}{N_t^2(N_t-1)}.
\]
Hence
\[
\lambda_{t,1}
=p_2\left(1+\frac{(2-\mu)^2}{\sigma^2}\right)
=B_t+\frac{2(K_t-1)(N_t-K_t)}{N_t(N_t-2)}=A_t.
\]
This last expression is used only at \(t\le L-1\le k-2\), where \(N_t\ge4\) and \(\sigma^2>0\). At \(t=k-1\), \(K_t=1\) and \(p_2=0\), so the compressed operator is zero and \(B_t=0\) directly; no division by \(p_2\) is needed.

**4. Multiplicities and endpoints.** For \(t=0,\ldots,L-2\), the nonzero eigenvalue is \(1\), giving \(\sum_{t=0}^{L-2}d_t=\binom{n-2}{L-2}\) copies. At \(t=L-1\) it is \(A_{L-1}\), repeated \(d_{L-1}\) times. At \(t=L\) it is \(B_L\), repeated \(d_L\) times. All other dimensions carry eigenvalue \(0\). The ambient low-pass dimension is \(\binom nL\), which proves the displayed multiset. The rank is \(\sum_{t=0}^{\min(L,k-2)}d_t=\binom{n-2}{\min(L,k-2)}\). The trace identity for \(h(0)=h(1)=0\) follows immediately. For \(L=0\), constants give \(|A|/|X|=B_0\).

## Verification

A standalone standard-library verifier, `verify.py`, independently constructs the Johnson adjacency matrix, its exact rational spectral projectors by Lagrange interpolation, and the face compression. For every \(4\le n\le8\), \(2\le k\le\lfloor n/2\rfloor\), and \(0\le L<k\), it checks exact projection idempotence, spectral polynomial annihilation, and spectral moments of orders \(1\) through \(4\) against the claimed eigenvalue multiset. The run completed \(23\) parameter triples covering \(773\) full matrix rows, with no floating-point arithmetic. The analytic argument, not finite enumeration, proves the statement for all permitted integers.

## Relationship to prior work

The harmonic-degree decomposition comes from the classical Johnson scheme; Scarabotti--Tolli [1] develops the general finite-homogeneous representation framework and Filmus [2] constructs an explicit orthogonal basis for Boolean slices. Neither inspected result states the present compressed two-coordinate-face spectrum. Bernard--Crampé--Vinet [3] studies Johnson-graph spatio-spectral concentration on unions of **distance neighborhoods of a single reference vertex**, not the face defined by containing two prescribed elements. The latter is not a union of those neighborhoods for general \(k\). The closed two-boundary-eigenvalue spectrum above therefore requires an additional coordinate-branching and hypergeometric compression calculation.

## Limitations

The theorem assumes \(n\ge2k\), \(k\ge2\), the single face requiring **both** specified coordinates, and a **cumulative** degree cutoff. It does not treat arbitrary unions of faces, larger prescribed coordinate sets, or arbitrary masks of Johnson degrees. The originality comparison covers the most closely identified Johnson harmonic and spatial-concentration sources, not all historical association-scheme literature; an equivalent special-case formula hidden in that literature remains a residual possibility. No independent mathematical audit has been performed.

## References

[1] F. Scarabotti and F. Tolli, *Harmonic analysis on a finite homogeneous space*, arXiv:math/0701533 (first public 19 January 2007; primary MSC 43A95). https://arxiv.org/pdf/math/0701533

[2] Y. Filmus, *Orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142 (first public 1 June 2014), *Electronic Journal of Combinatorics* **23** (2016), P1.23. https://arxiv.org/pdf/1406.0142

[3] P.-A. Bernard, N. Crampé and L. Vinet, *Entanglement of free fermions on Johnson graphs*, arXiv:2104.11581 (2021), especially §3 and the single-neighborhood formula (78). https://arxiv.org/pdf/2104.11581

[4] C. F. Dunkl, *An addition theorem for Hahn polynomials: the spherical functions*, *SIAM Journal on Mathematical Analysis* **9** (1978), 627–637. https://doi.org/10.1137/0509043 (related historical spherical-function source; complete text not available in the initial comparison).
