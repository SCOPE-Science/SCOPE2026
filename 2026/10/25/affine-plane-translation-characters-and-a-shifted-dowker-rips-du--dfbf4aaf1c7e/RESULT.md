# Affine-plane translation characters and a shifted Dowker–Rips duality gap

## Finding
Let \(q\ge2\) be a prime power, \(P=\mathbb F_q^2\), and \(L\) its affine lines. For the incidence relation \(R\subset P\times L\), denote the ordinary Dowker complex on points by \(D_P\). Let \(F_P\) and \(F_L\) be the flagifications of the point and line Dowker complexes: vertices in a simplex of \(F_L\) are affine lines that intersect pairwise. The natural affine group \(\operatorname{AGL}_2(\mathbb F_q)\) acts on these complexes.

The point flagification \(F_P\) is contractible, whereas the line flagification has integral homology only in dimension \(q\), with the **canonical integral affine-group lattice**
\[
\widetilde H_q(F_L;\mathbb Z)\cong
\mathop{\widehat\bigotimes}_{d\in\mathbb P^1(\mathbb F_q)}
 I(\mathcal L_d),\qquad I(S)=\ker(\mathbb Z[S]\xrightarrow{\sum}\mathbb Z).
\]
Here \(\mathcal L_d\) is the set of \(q\) parallel lines in direction \(d\); the hat means that relabeling factors by a direction permutation introduces its sign. The rank is \(N_q=(q-1)^{q+1}\). If \(g\) permutes the direction set by \(\sigma_g\), and for each cycle \(C\) of \(\sigma_g\) the number \(f_C\) counts lines in one representative direction fixed by \(g^{|C|}\), then its full rational character is
\[
 \operatorname{tr}\bigl(g\mid\widetilde H_q(F_L;\mathbb Q)\bigr)
 =\operatorname{sgn}(\sigma_g)\prod_C(f_C-1).
\]

For the translation group \(T=(\mathbb F_q^2,+)\), every nonidentity translation has trace \(c_q=(-1)^q(q-1)\), while the identity has trace \(N_q\). Consequently, over \(\mathbb C\), the trivial additive character has multiplicity
\[
 a_q=\frac{N_q+(q^2-1)c_q}{q^2},
\]
and **each** of the \(q^2-1\) nontrivial additive characters has multiplicity
\[
 b_q=\frac{N_q-c_q}{q^2}.
\]

There is also a different-degree comparison with the ordinary, unflagified point Dowker complex: its integral first homology is canonically the integral cycle lattice of the point–line incidence graph. The translation character is \(\mu_q=(q-1)^2(q+1)\) at the identity and \(1-q\) at each nonidentity translation. In particular, **for every odd prime power \(q\)** there is a noncanonical isomorphism of complex translation representations
\[
\widetilde H_q(F_L;\mathbb C)\cong
\widetilde H_1(D_P;\mathbb C)
\oplus\mathbb C[T]^{\oplus r_q},\qquad
r_q=\frac{(q-1)^{q+1}-(q-1)^2(q+1)}{q^2}.
\]
This is a representation comparison, not an identification of topological spaces or a degree-changing canonical map. At \(q=3\), \(r_q=0\) and the two representations coincide after shifting degree, despite having homology in dimensions \(3\) and \(1\), respectively; at \(q=5\), \(r_q=160\).

## Assumptions and scope
The theorem concerns the standard affine plane over a finite field, not an arbitrary non-Desarguesian plane, because the translation and affine groups are explicitly used. A direction is a one-dimensional \(\mathbb F_q\)-subspace of \(\mathbb F_q^2\), and two lines meet exactly when their directions differ. The *ordinary* point Dowker complex \(D_P\) contains a finite subset of points exactly when they lie together on an affine line. The line Dowker complex consists of subsets of lines incident with one common point. Flagification retains the vertices but fills every pairwise compatible vertex set. These constructions are abstract simplicial complexes, with integral augmented simplicial chains and standard join orientations. The symmetric-group sign convention is the sign of the induced permutation of the direction factors. Nontrivial characters are complex-valued irreducible characters of the finite abelian translation group.

## Proof
**Flagified complexes and integral action.** Any two distinct points lie on one affine line, hence every pair is an edge in the point-side flagification; therefore \(F_P=\Delta(P)\). In the line-side flagification, two lines are adjacent if and only if they are nonparallel. The graph is complete multipartite with the \(q+1\) sets \(\mathcal L_d\) as parts, so
\[
F_L=\mathop{*}_{d\in\mathbb P^1(\mathbb F_q)}D(\mathcal L_d),
\]
where \(D(S)\) is the discrete complex on \(S\). The reduced augmented chain complex of a join is the suspended tensor product of its reduced chain complexes. Each discrete factor has reduced homology \(I(\mathcal L_d)\) in degree zero, free of rank \(q-1\). Since all are free, the integral join Künneth theorem gives the stated unique nonzero group in degree \((q+1)-1=q\). Exchanging two augmented degree-zero factors contributes \((-1)^{(0+1)(0+1)}=-1\), yielding the claimed sign-twisted affine action. Thus the isomorphism is natural over \(\mathbb Z\), not only a rational character identity.

**Complete affine character.** Fix an affine map \(g\). Its permutation \(\sigma_g\) of direction classes is a product of disjoint cycles. Within one direction cycle of length \(s\), the cyclically permuted tensor product has trace equal to the trace of the composite \(g^s\) on the representative augmentation lattice. This follows by expanding in any integral basis: only diagonal tensors with indices transported consistently around the cycle contribute. For a permutation of a finite set \(S\), the trace on \(I(S)\) is the number of fixed elements of \(S\) minus one, using the exact sequence \(0\to I(S)\to\mathbb Z[S]\to\mathbb Z\to0\). The graded tensor permutations contribute \(\operatorname{sgn}(\sigma_g)\), proving the product formula.

**Translations and multiplicities.** If \(t\ne0\), the unique direction \(d=\mathbb F_qt\) has all its \(q\) parallel lines individually stabilized by translation by \(t\); in each of the other \(q\) directions, no line is fixed. A translation fixes every direction, so the product-formula trace is \((q-1)(-1)^q\). The identity trace is the rank \(N_q\). Orthogonality of characters of the abelian group of order \(q^2\) gives \(a_q=q^{-2}(N_q+(q^2-1)c_q)\), while every nontrivial character sums to \(-1\) on \(T\setminus\{0\}\) and hence has multiplicity \(b_q=q^{-2}(N_q-c_q)\). These expressions are nonnegative integers because they are actual representation multiplicities.

**Ordinary Dowker cycles, integrally.** The subcomplex \(D_P\) is the union of the full simplices on the \(q\) points of each affine line, intersecting pairwise in at most one vertex. For every dimension at least one, its augmented simplicial chain group splits over lines; thus the relation induced by triangle boundaries within a line identifies its oriented edge chains modulo boundaries with \(I(P(\ell))\). This identification sends an oriented edge \([p,p']\) to \(p'-p\), and follows from the contractibility of each line simplex. Therefore
\[
H_1(D_P;\mathbb Z)\cong
\ker\left(\bigoplus_{\ell\in L} I(P(\ell))
\longrightarrow\mathbb Z[P]\right),
\]
where the map sums the point differences. Orient the edges of the bipartite incidence graph \(G\) from line-vertices toward point-vertices. A graph one-cycle is exactly a collection of integer edge weights with zero sum at every line and zero sum at every point. Identifying the weights at a line with an element of \(I(P(\ell))\) gives the displayed kernel **equivariantly and integrally**. Higher homology of \(D_P\) vanishes because each positive-dimensional simplex is supported in one contractible line simplex; the graph is connected. There are \(q^2(q+1)\) incidence edges and \(2q^2+q\) vertices, so its cycle rank is \(\mu_q=(q-1)^2(q+1)\).

For nonzero translation \(t\), no point vertex or incidence edge of \(G\) is fixed, whereas precisely the \(q\) lines parallel to \(t\) are fixed as vertices. The graph Lefschetz formula (or trace on the cellular chain complex) gives \(\operatorname{tr}(t\mid H_1(G;\mathbb Q))=1-q\). Fourier inversion therefore shows that the translation representation of ordinary Dowker first homology is \((q-1)\) copies of the augmentation representation of \(T\): its trivial-character multiplicity is zero, and every nontrivial-character multiplicity is \(q-1\).

**Odd-characteristic comparison.** For odd \(q\), the two nonidentity traces agree: \(c_q=1-q\). Thus the difference of the two degree-shifted rational translation characters is supported only at the group identity; its identity value is \(N_q-\mu_q\). The regular character equals \(q^2\) at the identity and zero elsewhere. Therefore the difference is exactly \(r_q\) copies of the regular character, and complete reducibility over \(\mathbb C\) proves the asserted noncanonical representation decomposition. The coefficient is a nonnegative integer: for odd \(q\), the trivial-character multiplicity \(a_q=r_q\). The statement does not assert this comparison for even \(q\); for example \(q=2\), the two nonidentity traces are \(+1\) and \(-1\), respectively.

## Verification
Run `python3 verify.py` using Python 3 and no third-party packages. The independent script builds \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\), enumerates affine lines and direction classes, checks their incidence axioms, constructs the line-flagified faces, computes exact reduced mod-two simplicial boundary ranks for \(q=2,3,4\), and checks the character formula for all \(24\) affine transformations at \(q=2\), all \(432\) at \(q=3\), and \(123\) further selected transformations at \(q=4,5\). For \(q=2,3\), the predicted trace is independently reconstructed from signed fixed simplices via the Lefschetz formula. The final line is `VERIFY_OK 579`. These finite checks corroborate the algebraic proof but cannot establish statements for all prime powers or integral representation structure.

## Relationship to prior work
Huber and Schnider's 2025 *Flagifying the Dowker Complex* introduces the flagified Dowker–Rips comparison and identifies low-dimensional homology ranges; its finite tetrahedral example already exhibits a failure of full unshifted duality at four points. Thus **the existence of a duality gap, and the four-point boundary example, are not claimed as new here**. The present contribution concerns the exact affine-group integral lattice, full character formula and arithmetic shifted comparison between two different homology degrees for an infinite finite-field family.

The publicly available *Mixed-dimensional Vietoris–Rips homotopy of affine-plane incidence graphs* and *Affine-plane incidence Rips complexes have two sphere dimensions* establish, via a point/line join decomposition, the previously known nonequivariant sphere multiplicities for the line-only complex within the scale-two Rips complex of the affine Levi graph; **the join description and its wedge rank are likewise not claimed as new**. Their results give neither affine-group characters of the line flagification nor the comparison with ordinary Dowker first homology. The publicly available *Complete Rips barcodes and top-dimensional symmetry of multipartite prisms* proves augmentation-tensor representations for a different graph-prism metric; the general join orientation rule is shared, but it does not determine finite-affine translation signs or the odd-characteristic regular-representation difference. The present formulas use incidence-specific fixed-line geometry and a separate integral cycle-lattice analysis of ordinary Dowker homology.

## Limitations
The claim holds for Desarguesian finite affine planes over fields. It makes no existence assertion for arbitrary orders and no corresponding representation claim for non-Desarguesian planes lacking the specified affine translation group. The shifted comparison is over complex coefficients and is not a canonical map of complexes or an integral splitting. The nonequivariant homotopy ranks and basic tensor-join tools are previously known, and unindexed equivalent equivariant calculations cannot be ruled out. The verifier covers only four small prime powers; the displayed all-order proofs rely on chain decompositions and finite-group character theory, not extrapolation. No independent scientific review is claimed.

## References
1. M. Huber and P. Schnider, *Flagifying the Dowker Complex*, arXiv:2508.08025v1, first publicly posted 2025-08-11; see Definition 1.5, Theorem 1.10 and Proposition 3.4. https://arxiv.org/abs/2508.08025.
2. *Mixed-dimensional Vietoris–Rips homotopy of affine-plane incidence graphs*, publicly available mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-mixed-dimensional-vietoris-rips-homotopy-of-affine-plane-inciden--721bc8ceb957.
3. *Affine-plane incidence Rips complexes have two sphere dimensions*, publicly available mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-affine-plane-incidence-rips-complexes-have-two-sphere-dimensions--3087baeea0a4.
4. *Complete Rips barcodes and top-dimensional symmetry of multipartite prisms*, publicly available mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-rips-barcodes-and-top-dimensional-symmetry-of-multipart--8573c09b40de.
