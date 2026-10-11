# Symmetric-group cohomology and rationally acyclic quotients of injective-word moment-angle complexes

## Finding

Let \(\Gamma_n\) be the simplicial poset of injective words on \([n]=\{1,\ldots,n\}\), including the empty word, with the face relation given by deleting letters, and let \(Z_n=\mathcal Z_{\Gamma_n}(D^2,S^1)\) be its moment-angle complex. The natural relabeling of words, combined with permutation of disk coordinates, gives a cellular \(S_n\)-action. For each \(2\le k\le n\), put \(D_k=\widetilde H^{k-1}(|\Gamma_k|;\mathbb Q)\), as a rational \(S_k\)-module. Then

\[
H^{2k}(Z_n;\mathbb Q)\cong
\operatorname{Ind}^{S_n}_{S_k\times S_{n-k}}
\bigl((\operatorname{sgn}_k\otimes D_k)\boxtimes\mathbf 1\bigr).
\]

These are isomorphisms of rational representations, not claims of canonical cohomology bases. Also \(H^0(Z_n;\mathbb Q)=\mathbb Q\), and all other rational cohomology vanishes. In particular, the quotient by the full coordinate permutation action is **rationally acyclic**:

\[
\widetilde H^i(Z_n/S_n;\mathbb Q)=0\qquad\text{for every integer }i\text{ and }n\ge2.
\]

The complete character has an explicit cycle-stable-set formula. For \(g\in S_n\), a \(g\)-stable \(k\)-subset \(A\subseteq[n]\), let \(f_A(g)\) be the number of individual elements of \(A\) fixed by \(g\), let \(\varepsilon_A(g)=\operatorname{sgn}(g|_A)\), and define the falling factorial \((f)_j=f(f-1)\cdots(f-j+1)\), with \((f)_0=1\). Then

\[
\operatorname{tr}(g\mid H^{2k}(Z_n;\mathbb Q))=
(-1)^k\!
\sum_{\substack{A\subseteq[n],\,|A|=k\\g(A)=A}}
\varepsilon_A(g)\sum_{j=0}^{k}(-1)^j(f_A(g))_j.
\]

The dimension at the identity equals \(\binom nk\,d_k\), where \(d_k\) is the number of derangements of \(k\) letters. For example, when \(n=2\), the unique degree-four class is negated by transposition; when \(n=3\), degree-four and degree-six cohomology have dimensions three and two, respectively, and neither has a fixed vector under \(S_3\).

## Assumptions and scope

All spaces are the finite CW polyhedral products of the standard pointed CW pair \((D^2,S^1)\); \(S_n\) acts by relabeling word faces and permuting **entire complex disk factors without conjugation**. The theorem holds for every integer \(n\ge2\) and every degree. Coefficients are rational, so finite-group representations are semisimple. The module \(D_k\) is the pre-existing top cohomology representation of the injective-word complex; its definition does not presume a particular irreducible decomposition.

## Proof

**1. Multigraded cellular cochains and concentration.** By the simplicial-poset cell model, a cellular cochain basis consists of pairs \((\sigma,B)\), where \(\sigma\) is an injective word, \(B\) is a subset disjoint from the letters of \(\sigma\), the positions of \(\sigma\) are \(D\)-cells of dimension two, and the positions of \(B\) are \(T\)-cells of dimension one. Other coordinates are zero-cells. The cochain degree is \(2|\sigma|+|B|\). Its support \(A=V(\sigma)\cup B\) is preserved by the differential, giving a direct sum of cellular cochain subcomplexes \(C_A^*\). For \(|A|=k\), the simplicial-poset Hochster formula identifies

\[
H^p(C_A^*;\mathbb Q)\cong\widetilde H^{p-k-1}(|\Gamma_A|;\mathbb Q)
\]

as vector spaces. The injective-word complex on \(A\) is shellable and has reduced cohomology only in degree \(k-1\), with dimension \(d_k\). Thus \(C_A^*\) has cohomology only in degree \(2k\), with that dimension when \(k\ge2\); for \(k=1\), it is acyclic. Empty support contributes only \(H^0=\mathbb Q\). No equivariance of an arbitrary chosen Hochster isomorphism is assumed.

**2. An equivariant signed Euler computation.** Fix \(g\in S_n\) and a support \(A\) preserved by \(g\), of size \(k\). A basis cochain corresponding to a word \(\sigma\) of length \(j\) and \(B=A\setminus V(\sigma)\) is fixed by the permutation precisely if all \(j\) letters of \(\sigma\) are individually fixed by \(g\). Hence there are \((f_A(g))_j\) fixed cells of this form. Permuting the two-dimensional disk-coordinate cells contributes no orientation sign. Permuting the one-dimensional circle-coordinate cells contributes \(\operatorname{sgn}(g|_B)=\varepsilon_A(g)\), since the omitted word letters are pointwise fixed. Each such cell has dimension \(k+j\). Therefore, the alternating cellular-cochain trace on this support is

\[
\sum_{j=0}^{k}(-1)^{k+j}\varepsilon_A(g)(f_A(g))_j.
\]

The equivariant Euler--Poincaré identity equates this to the alternating trace on cohomology. By Step 1 only degree \(2k\) survives, with positive parity, so this is exactly the trace of \(g\) on \(H^{2k}(C_A^*;\mathbb Q)\). Summing over all \(g\)-stable supports gives the character formula in the finding. Supports exchanged by \(g\) contribute zero trace.

**3. Identification of the full module.** The reduced cellular chain complex of \(\Gamma_k\) has a basis of injective words of each length \(j\) and the empty word. Relabeling a word preserves its ordered-cell orientation, so a permutation \(h\in S_k\), with \(f(h)\) fixed labels, has \((f(h))_j\) fixed words of length \(j\). Since only reduced cohomology in degree \(k-1\) survives, Euler--Poincaré gives

\[
\operatorname{tr}(h\mid D_k)=(-1)^k\sum_{j=0}^k(-1)^j(f(h))_j.
\]

Comparing with Step 2, the \(S_A\)-character of \(H^{2k}(C_A^*;\mathbb Q)\) equals that of \(\operatorname{sgn}_A\otimes D_A\). Finite-dimensional rational \(S_A\)-representations are characterized by their characters, giving an abstract module isomorphism. The distinct supports of size \(k\) form one \(S_n\)-orbit, with stabilizer \(S_k\times S_{n-k}\); induction gives the asserted complete \(S_n\)-module.

**4. Vanishing of the rational quotient cohomology.** For a finite group acting cellularly on a finite CW complex, rational cohomology of the orbit space identifies with invariants of rational cohomology (equivalently, the Borel-to-orbit map has rationally acyclic finite-stabilizer fibers). By Frobenius reciprocity, the invariant subspace in degree \(2k\) has dimension \(\langle D_k,\operatorname{sgn}_k\rangle\). Expand the character of \(D_k\) from Step 3. For \(0\le j\le k-2\), the sign-weighted average over \(S_k\) of the number of fixed ordered \(j\)-tuples vanishes: each pointwise stabilizer contains a copy of \(S_2\) and has equal even and odd elements. At \(j=k-1\) and \(j=k\), each normalized sign-weighted sum equals one, since only the identity fixes that many labels. Their coefficients \((-1)^{k-1}\) and \((-1)^k\) cancel, hence \(\langle D_k,\operatorname{sgn}_k\rangle=0\) for every \(k\ge2\). There are no other positive-degree cohomology groups. The degree-zero invariants are one-dimensional because \(Z_n\) is connected. This proves rational acyclicity of \(Z_n/S_n\).

## Verification

The accompanying standalone script `verify.py` uses only the Python standard library. It independently enumerates fixed oriented cellular cochains and evaluates the closed character formula for every permutation of \(S_n\), for \(2\le n\le6\) and every \(2\le k\le n\). It checks the identity ranks against \(\binom nk d_k\), computes each finite-group character average, and verifies that every nonzero-degree invariant multiplicity is zero. Successful replay prints `VERIFY_OK` and reports 4,166 paired character calculations, 20,496 fixed oriented-cell terms, and 15 finite quotient-invariant checks. The \(n=2\) transposition test confirms the crucial negative orientation sign. These finite tests do not constitute the proof for arbitrary \(n\); Steps 1--4 do.

## Relationship to prior work

Pedro Conceição, *The homotopy type of the moment-angle complex associated to the complex of injective words* (first posted 2026-03-10), computes the nonequivariant wedge of spheres and dimensions but not the coordinate-permutation character or quotient rational cohomology (especially Proposition 2.1 and Theorem 2.10). Lü--Panov give the simplicial-poset cellular decomposition and Hochster formula, but no specialization to this relabeling action. Reiner--Webb's injective-word homology representation, as described and generalized by Athanasiadis, concerns \(D_k\), not this moment-angle space and its sign-twisted induction. D'Alì--Delucchi discuss invariant face rings and quotient posets, rather than these quotient moment-angle rational cohomology groups. Li Yu studies torus-subgroup quotients and does not give this finite coordinate-permutation quotient. The signed character and all-degree vanishing combine these ingredients for a distinct natural topological object.

## Limitations

No integral quotient acyclicity, contractibility, equivariant homotopy splitting, or canonical integral module decomposition is claimed. A rationally acyclic quotient may still possess torsion or nontrivial homotopy. The character is for the specified coordinate-permutation action, not the entire torus-semilinear automorphism group. The argument uses already established shellability and simplicial-poset Hochster theorems, and a prior formulation of this particular equivariant specialization outside the inspected literature cannot be categorically excluded.

## References

1. P. Conceição, *The homotopy type of the moment-angle complex associated to the complex of injective words*, arXiv:2603.09491, first public version 2026-03-10, Proposition 2.1 and Theorem 2.10. https://arxiv.org/abs/2603.09491
2. Z. Lü and T. Panov, *Moment-angle complexes from simplicial posets*, arXiv:0912.2219, Construction 3.4, Theorem 3.6, Corollary 3.8. https://arxiv.org/abs/0912.2219
3. C. A. Athanasiadis, *The symmetric group action on rank-selected posets of injective words*, arXiv:1606.03829, introduction and Theorem 1.1 (citing Reiner--Webb). https://arxiv.org/abs/1606.03829
4. A. D'Alì and E. Delucchi, *Stanley--Reisner rings for symmetric simplicial complexes, G-semimatroids and Abelian arrangements*, arXiv:1804.07366, especially introductory theorems. https://arxiv.org/abs/1804.07366
5. L. Yu, *On Hochster's formula for a class of quotient spaces of moment-angle complexes*, arXiv:1406.7392, introduction and quotient construction. https://arxiv.org/abs/1406.7392
