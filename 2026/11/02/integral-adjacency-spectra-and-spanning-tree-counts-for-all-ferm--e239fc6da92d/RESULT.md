# Integral adjacency spectra and spanning-tree counts for all Fermat-surface line configurations

## Finding

For every integer \(d\geq3\), let \(X_d\subset\mathbb P^3_{\mathbb C}\) be the smooth Fermat surface
\[
 x_0^d+x_1^d+x_2^d+x_3^d=0.
\]
Let \(G_d\) be the simple graph on all \(3d^2\) lines contained in \(X_d\), with distinct vertices adjacent if and only if the corresponding lines meet. Write \(\lambda^m\) for an adjacency eigenvalue with multiplicity \(m\); the formal exponential here denotes multiplicity, not powering an eigenvalue. Then \(G_d\) is connected and \((4d-2)\)-regular, and its **entire integral adjacency spectrum** is as follows.

For odd \(d\geq3\):
\[
\operatorname{Spec}(G_d)=
 (4d-2)^{[1]},\quad (d-2)^{[9d-7]},\quad
 (-2)^{[3(d-1)(d-3)]},\quad (-(d+2))^{[3(d-1)]}.
\]
A zero exponent means the level is absent; in particular the \(-2\) level is absent at \(d=3\).

For even \(d\geq4\):
\[
\operatorname{Spec}(G_d)=
 (4d-2)^{[1]},\quad (d-2)^{[9d-8]},\quad
 (-2)^{[3(d-2)^2]},\quad (-(d+2))^{[3(d-2)]},\quad
 (-(2d+2))^{[1]}.
\]

In particular, a parity-dependent isolated negative eigenvalue \(-(2d+2)\) appears **in every even degree**, coming from a signed three-cycle in the Fourier decomposition. The graph has spectral gap \(3d\). Its number \(\tau(G_d)\) of spanning trees is exactly
\[
 \tau(G_d)=
 \begin{cases}
 \displaystyle \frac{(3d)^{9d-7}(4d)^{3(d-1)(d-3)}(5d)^{3(d-1)}}{3d^2},&d\text{ odd},\\[5pt]
 \displaystyle \frac{(3d)^{9d-8}(4d)^{3(d-2)^2}(5d)^{3(d-2)}(6d)}{3d^2},&d\text{ even}.
 \end{cases}
\]
These formulas count spanning trees of the unweighted geometric line-intersection graph, not intersection-lattice discriminants.

## Assumptions and scope

All varieties and lines are over \(\mathbb C\); \(d\) is an arbitrary integer at least three, not necessarily prime. For a complex Fermat surface of this degree, the complete geometric line set is the classical configuration of three families of \(d^2\) lines [1,2]. A line's self-intersection on \(X_d\) is \(2-d\), but **graph adjacency has zero diagonal**. The theorem asserts the adjacency spectrum and graph complexity only; it neither asserts integral generation of \(\operatorname{NS}(X_d)\) by lines nor their integral saturation. The classical line-span rank, where used for comparison below, is not claimed as new.

For an explicit model let \(\lambda=\exp(\pi i/d)\), \(\zeta=\lambda^2\), so \(\lambda^d=-1\) and \(\zeta\) has order \(d\). All subscripts range over \(\mathbb Z/d\mathbb Z\). The three families are
\[
\begin{aligned}
 A_{a,b}:&\quad x_0=\lambda\zeta^a x_1,\quad x_2=\lambda\zeta^b x_3,\\
 B_{c,e}:&\quad x_0=\lambda\zeta^c x_2,\quad x_1=\lambda\zeta^e x_3,\\
 C_{f,g}:&\quad x_0=\lambda\zeta^f x_3,\quad x_1=\lambda\zeta^g x_2.
\end{aligned}
\]
Each is indeed contained in \(X_d\). The listed projective lines are distinct, and [1, §3] supplies their completeness as the configuration under study.

## Proof

**1. Exact geometric incidence.** Two distinct lines in the same family meet precisely when their first labels or their second labels coincide, giving the \(d\)-by-\(d\) rook graph within each family. Eliminating the coordinates in two families gives the following complete cross-family incidence conditions:
\[
\begin{split}
 A_{a,b}\sim B_{c,e}&\iff a+e\equiv b+c\pmod d,\\
 A_{a,b}\sim C_{f,g}&\iff f\equiv a+b+g+1\pmod d,\\
 B_{c,e}\sim C_{f,g}&\iff f+g\equiv c+e\pmod d.
\end{split}
\]
These are the explicit intersection rules of [1, Eq. (5)], with the indicated root-of-unity normalization. For example, on an intersection of \(A_{a,b}\) and \(C_{f,g}\), comparing two expressions for \(x_0/x_3\) gives \(\lambda\zeta^f=\lambda^3\zeta^{a+b+g}\), hence the middle congruence because \(\lambda^2=\zeta\). Each line meets \(2(d-1)\) lines within its own family and \(d\) in each other family; thus every vertex has degree \(4d-2\).

**2. Block Fourier decomposition.** Over \(\mathbb C\) use in each family the orthogonal basis \(\psi_{r,s}(a,b)=\zeta^{ra+sb}\), indexed by \(r,s\in\mathbb Z/d\mathbb Z\). The within-family rook adjacency acts by
\[
 R\psi_{r,s}=\begin{cases}
 (2d-2)\psi_{r,s},&r=s=0,\\
 (d-2)\psi_{r,s},&\text{exactly one of }r,s\text{ is zero},\\
 -2\psi_{r,s},&r\ne0,\ s\ne0.
 \end{cases}
\]
The cross-incidence sums factor into geometric sums \(\sum_{t\bmod d}\zeta^{kt}=d\,\mathbf 1_{k\equiv0}\). Consequently only the following nonconstant interfamily Fourier couplings occur, with a factor of \(d\) in each entry:
\[
 B_{r,-r}\leftrightarrow A_{r,-r},\qquad
 C_{r,-r}\leftrightarrow A_{r,r},\qquad
 C_{r,r}\leftrightarrow B_{r,r}.
\]
In the middle coupling the directed coefficient from \(C_{r,-r}\) to \(A_{r,r}\) is \(d\zeta^r\), and the reverse coefficient is its complex conjugate; the other two pairs have coefficient \(d\). To check the middle one directly, the allowed \(C\)-labels satisfy \(f=a+b+g+1\); hence
\[
 \sum_g\zeta^{r f-rg}=d\zeta^r\zeta^{r(a+b)}.
\]
No axis character is coupled to another family.

**3. Constant and axis modes.** The three constant Fourier modes form the matrix with diagonal \(2d-2\) and off-diagonal \(d\), with spectrum \(4d-2\) once and \(d-2\) twice. The six coordinate-axis families contain \(6(d-1)\) uncoupled modes, all at eigenvalue \(d-2\).

**4. Generic nonzero modes and the parity resonance.** If \(r\ne0\) and \(2r\not\equiv0\pmod d\), then \((r,r)\) and \((r,-r)\) are distinct. The modes for such an \(r\) form **three disjoint Hermitian two-by-two blocks** with diagonal \(-2\) and off-diagonal of absolute value \(d\). Each block has eigenvalues \(d-2\) and \(-(d+2)\).

For odd \(d\), every nonzero \(r\) is generic, giving \(3(d-1)\) copies of each eigenvalue. For even \(d\), exactly \(d-2\) values of \(r\) are generic. There is one remaining nonzero value \(r=d/2\), for which \((r,r)=(r,-r)\) and \(\zeta^r=-1\). Its three formerly separate modes merge into the **signed triangle**
\[
 \begin{pmatrix}-2&d&-d\\ d&-2&d\\ -d&d&-2\end{pmatrix},
\]
whose eigenvalues are \(d-2\) twice and \(-(2d+2)\) once. This explains the unique even-degree exceptional eigenvalue.

**5. Exhaustion and multiplicities.** The nonzero-both-coordinate part of the three Fourier bases contains \(3(d-1)^2\) modes. In odd degree, removing the \(6(d-1)\) modes in the two-by-two blocks leaves \(3(d-1)(d-3)\) uncoupled modes, all at \(-2\). In even degree, removing \(6(d-2)\) generic modes and three signed-triangle modes leaves \(3(d-2)^2\) at \(-2\). Combining these counts with the constant and axis sectors proves both displayed spectra, with total multiplicity \(3d^2\) in either parity. In particular the maximal eigenvalue \(4d-2\) has multiplicity one; since the graph is regular and undirected, it is connected.

**6. Corollaries and boundaries.** The second-largest eigenvalue is \(d-2\), giving adjacency spectral gap \((4d-2)-(d-2)=3d\). The Laplacian eigenvalues are obtained by subtracting each adjacency eigenvalue from \(4d-2\). Kirchhoff's matrix-tree theorem, dividing the product of all nonzero Laplacian eigenvalues by \(3d^2\), gives the stated spanning-tree formulas. For comparison, adjunction yields the line intersection matrix \(M_d=A(G_d)+(2-d)I\). Its nonzero eigenvalues are \(3d\) once, \(-d\) with multiplicity equal to the \(-2\) adjacency multiplicity, \(-2d\) with multiplicity equal to that of \(-(d+2)\), and also \(-3d\) once in even degree. Hence
\[
 \operatorname{rank}_{\mathbb Q}M_d=3(d-1)(d-2)+1+\mathbf1_{2\mid d},
\]
reobtaining the previously known rank [1,2]; this rank is **not an independent novelty assertion**.

## Verification

The standalone standard-library script `verify_fermat_spectrum.py` builds the exact binary adjacency matrix from the congruences, independently of Fourier diagonalization. For each degree \(d=3,4,5,6,7,8,9\), it checks regularity, the sum of multiplicities, the exact polynomial identity \(\prod_{\lambda\in\operatorname{Spec}}(A-\lambda I)=0\), and the first \(r\) integral spectral moments, where \(r\) is the number of distinct eigenvalues. Together the latter two facts uniquely fix all spectral multiplicities in a given finite case. It also checks the shifted Gram-rank formula. The reproducible output is in `verify_output.txt` and terminates with `VERIFY_OK`. These seven degree checks are **corroboration only**; the all-integer-degree theorem is proved by the Fourier argument above, not inferred from these computations.

## Relationship to prior work

The three line families, their exhaustive geometric incidence, and the line-class rank are classical data developed explicitly in Schütt–Shioda–van Luijk [1], especially its Section 3, equation (5), and Section 4. Degtyarev [2] extends integral line generation and analyzes the same lattice, but not this graph's full all-degree adjacency spectrum. Andria–Rojas–Mangueira [3] use the same pairwise intersection relations to investigate maximal pairwise-skew collections, an independence-number problem rather than an adjacency spectrum or spanning-tree formula. Thus the **new claim is a closed, parity-sensitive spectral classification of the entire graph for every integer degree** and its exact graph complexity, not discovery of the lines, their incidence predicates, the known Gram rank, or a special-degree numeric spectrum. Previously published complete incidence formulas logically permit reconstruction of the graph and make historical priority provisional; none of the inspected material states or proves the all-degree eigenvalue/multiplicity formula or signed-triangle parity effect. A 2026 manuscript on line-lattice discriminants in prime degrees uses related Fourier pairings; its prime-degree setting and lattice determinant do not provide the composite/even-degree graph spectra as stated. This comparison is a scoped search assessment, not a claim of worldwide uniqueness.

## Limitations

The graph is over the complex numbers: extensions to positive characteristic or additional exceptional lines in special characteristics are not asserted. The formulas are for all **geometric** lines in the characteristic-zero Fermat configuration, not only lines defined over a particular number field. They do not give the Smith normal form, integral saturation, or discriminant group of the divisor lattice. The exact line-adjacency predicates in the proof were already known, so an implicit derivation from established matrix descriptions is a genuine originality risk. Independent mathematical validation has not been performed.

## References

[1] M. Schütt, T. Shioda and R. van Luijk, *Lines on Fermat surfaces*, arXiv:0812.2377, first posted 2008-12-12. https://arxiv.org/abs/0812.2377 . See Section 3, Eq. (5), and Section 4.

[2] A. Degtyarev, *Lines generate the Picard groups of certain Fermat surfaces*, arXiv:1305.3073, first posted 2013-05-14. https://arxiv.org/abs/1305.3073 .

[3] S. Andria, J. Rojas and W. Mangueira, *Maximal number of skew lines on Fermat surfaces*, arXiv:2403.15666, 2024. https://arxiv.org/abs/2403.15666 .

[4] *The Watermark Theorem: the discriminant of the line lattice of Fermat surfaces of prime degree*, public manuscript, 2026, `THE_WATERMARK_THEOREM.md` in https://github.com/tretoef-estrella/fermat-hodge-primitivity . Compared for its related Fourier pairings and restricted odd-prime scope.
