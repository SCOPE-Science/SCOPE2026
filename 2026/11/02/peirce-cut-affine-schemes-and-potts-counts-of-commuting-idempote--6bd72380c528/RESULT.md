# Peirce-cut affine schemes and Potts counts of commuting idempotents

## Finding

**Theorem (commuting-idempotent schemes of split basic algebras).** Let \(k\) be any field and \(A\) a finite-dimensional unital associative split basic \(k\)-algebra: \(J=\operatorname{rad}(A)\) is nilpotent and \(A/J\cong k^n\), with \(n\ge1\). Fix pairwise orthogonal primitive idempotents \(e_1,\ldots,e_n\) summing to \(1\), mapping to the standard coordinates of \(k^n\). Set
\[
 w_{uv}=\dim_k(e_uJe_v)+\dim_k(e_vJe_u)\quad(1\le u<v\le n).
\]
For every \(m\ge0\) put \(H_m=\{0,1\}^m\), and let \(\mathcal I_m(A)\) be the affine **scheme** of ordered pairwise-commuting idempotents, defined by \(x_i^2=x_i\) and \(x_ix_j=x_jx_i\) for all \(i,j\). Then there is a (choice-dependent) \(k\)-scheme isomorphism
\[
 \boxed{\mathcal I_m(A)\ \cong\ \coprod_{\lambda:\{1,\ldots,n\}\to H_m}\mathbb A_k^{\kappa(\lambda)},\qquad
 \kappa(\lambda)=\sum_{1\le u<v\le n}w_{uv}\,\mathbf1_{\lambda(u)\ne\lambda(v)}.}
\]
In particular the actual defining scheme is smooth and reduced over \(k\), with exactly \(2^{mn}\) geometrically irreducible connected components, all defined over \(k\), of the stated dimensions. No restriction on \(\operatorname{char} k\) or on the nilpotency index of \(J\) is made.

For any finite field \(k=\mathbb F_q\), all \(m\ge0\), and the loopless undirected multigraph \(G_A\) with \(w_{uv}\) edges joining \(u\) and \(v\), the point count is
\[
 \boxed{C_m(A;q)=\#\mathcal I_m(A)(\mathbb F_q)
 =\sum_{\lambda:\{1,\ldots,n\}\to H_m}q^{\kappa(\lambda)}
 =q^{E}\,Z_{G_A}(2^m,q^{-1}-1),}
\]
where \(E=\sum_{u<v}w_{uv}\) and \(Z_G(X,Y)=\sum_{F\subseteq E(G)}X^{c(V,F)}Y^{|F|}\) is the spanning-subgraph/random-cluster polynomial. The equality counts elements, **not merely conjugacy orbits**. In the Grothendieck ring the scheme class is \(\sum_\lambda\mathbb L^{\kappa(\lambda)}\), and over \(\mathbb F_q\) its Hasse–Weil zeta function is \(\prod_\lambda(1-q^{\kappa(\lambda)}T)^{-1}\).

The maximum component dimension is the weighted maximum \(2^m\)-cut of \(G_A\). It equals \(E\) precisely when \(2^m\ge\chi(G_A)\), where chromatic number ignores multiplicity (and is \(1\) when \(E=0\)). For \(m\ge1\), the scheme is equidimensional if and only if \(E=0\); the zero-dimensional components are exactly the \((2^m)^{c(G_A)}\) labelings constant on each connected component of \(G_A\).

**Path-algebra corollary and reconstruction.** For any finite quiver \(Q\), including cycles, loops, and parallel arrows, and truncation \(d\ge2\), put \(A_{Q,d}(k)=kQ/J_Q^d\). Here \(G_{Q,d}\) is the loopless multigraph having one edge for every oriented path in \(Q\) of length between \(1\) and \(d-1\) with distinct endpoints (orientation is discarded only *after* all paths have been formed). The displayed formulas determine its commuting-idempotent schemes and counts. For fixed \(Q,d\), the complete counts over all finite fields and all tuple lengths determine, and are determined by, \(Z_{G_{Q,d}}(X,Y)\): assuming \(n\) and \(E\) known, samples at \(m=0,1,\ldots,n\) and at any \(E+1\) distinct prime-power field orders suffice by two-variable interpolation. For each fixed \(q\) the sequence in \(m\) satisfies the annihilating recurrence with shift polynomial \(\prod_{j=1}^{n}(T-2^j)\) (not necessarily the minimal recurrence).

For example, the usual upper-triangular \(3\times3\) matrix algebra and the radical-square-zero algebra of the three-arrow acyclic quiver \(1\to2\), \(2\to3\), \(1\to3\) have different radical nilpotency lengths, but the same \(G_A=K_3\), hence isomorphic commuting-idempotent schemes in every tuple length. Their common finite-field counts include \(C_1=2+6q^2\) and \(C_2=4+36q^2+24q^3\).

## Assumptions and scope

- \(A\) is unital, associative, finite-dimensional, and **split basic**, so \(A/J\cong k^n\); a matrix-factor semisimple quotient is not included.
- \(m\) counts ordered commuting idempotents. For \(m=0\) the empty tuple scheme is one point; \(H_0\) has one element.
- \(e_uJe_v\) denotes a vector-space Peirce block and \(w_{uv}\) its symmetrized off-diagonal dimension; the diagonal blocks \(e_uJe_u\) are deliberately excluded.
- All geometric assertions concern the full scheme cut out by the given equations, not only its reduced locus, and remain valid after any field extension.
- \(Z_G\) is an already-known graph polynomial. The proposed contribution is the algebraic scheme/count identification and its all-nilpotency consequences, not a discovery of that polynomial or of classical idempotent conjugacy.

## Proof

**1. Split the scheme into discrete diagonal-label fibers.** For any commutative \(k\)-algebra \(R\), reduction modulo \(J_R=J\otimes_k R\) sends a commuting-idempotent tuple in \(A_R=A\otimes_kR\) to a tuple in \(R^n\). Each scalar diagonal coordinate obeys \(t^2-t=0\). Since \(k[t]/(t^2-t)\cong k\times k\) (also in characteristic two), the quotient-label scheme is the disjoint union of the \(2^{mn}\) reduced rational points labeled by maps \(\lambda:\{1,\ldots,n\}\to H_m\). It remains to identify the scheme-theoretic fiber over an arbitrary such \(\lambda\).

**2. Turn a commuting tuple into an orthogonal idempotent system.** For \(\alpha\in H_m\) set \(d_\alpha=\sum_{\lambda(v)=\alpha}e_v\). For a tuple \((x_1,\ldots,x_m)\) in this fiber set
\[
 p_\alpha=\prod_{i=1}^{m}\bigl(\alpha_i x_i+(1-\alpha_i)(1-x_i)\bigr).
\]
The factors commute, so the \(p_\alpha\) are mutually orthogonal idempotents with sum \(1\), and \(p_\alpha\equiv d_\alpha\pmod{J_R}\). Define \(w=\sum_\alpha p_\alpha d_\alpha\). Then \(w\equiv1\pmod{J_R}\); because \(J_R\) is nilpotent, \(w\) is invertible by a finite geometric series. Moreover \(p_\alpha w=w d_\alpha\), hence \(p_\alpha=w d_\alpha w^{-1}\) for every \(\alpha\).

**3. Normalize the conjugator by a polynomial, without logarithms or division.** Decompose
\[
 J=H_\lambda\oplus N_\lambda,\qquad
 H_\lambda=\bigoplus_\alpha d_\alpha Jd_\alpha,\quad
 N_\lambda=\bigoplus_{\alpha\ne\beta}d_\alpha Jd_\beta.
\]
Here \(H_\lambda\) is a nilpotent subalgebra, \(N_\lambda H_\lambda\subseteq N_\lambda\), and \(1+H_\lambda\) is exactly the centralizer of all \(d_\alpha\) inside \(1+J\). If \(w=1+h+n\) with \(h\in H_{\lambda,R}\) and \(n\in N_{\lambda,R}\), then
\[
 w=(1+x)(1+h),\qquad x=n(1+h)^{-1}\in N_{\lambda,R}.
\]
The inverse \((1+h)^{-1}\) is a finite polynomial because \(h\) is nilpotent. This factorization is unique: its \(H\)-part must be \(h\), and then its \(N\)-part fixes \(x\). Thus the fiber tuple equals \(( (1+x)D_i(1+x)^{-1})_{i=1}^m\), where \(D_i=\sum_v\lambda(v)_i e_v\).

Conversely each \(x\in N_{\lambda,R}\) defines such a tuple. Its recovered \(p_\alpha\) and \(w\) give the same normalized \(x\), because the conjugator \(1+x\) differs from \(w\) by an element of \(1+H_{\lambda,R}\). These formulas are polynomial and mutually inverse for every \(R\), establishing an isomorphism of functors, hence of schemes: the fiber is \(\mathbb A_k^{\dim N_\lambda}\), not just a bijection on algebraically closed points. This simultaneously verifies smoothness and reducedness in arbitrary characteristic.

**4. Compute the fiber dimension and the arithmetic formulas.** Since \(e_uJe_v\) is in \(N_\lambda\) exactly when \(\lambda(u)\ne\lambda(v)\),
\[
 \dim N_\lambda=\sum_{u,v:\lambda(u)\ne\lambda(v)}\dim e_uJe_v
 =\sum_{u<v}w_{uv}\mathbf1_{\lambda(u)\ne\lambda(v)}=\kappa(\lambda).
\]
Each affine fiber has \(q^{\kappa(\lambda)}\) rational points. Write \(h=2^m\); then \(q^{\kappa(\lambda)}=q^E\prod_{a\in E(G_A)}(1+(q^{-1}-1)\mathbf1_{\lambda(s(a))=\lambda(t(a))})\). Expanding the product over chosen edges \(F\), the number of labelings constant on every connected component of \((V,F)\) is \(h^{c(V,F)}\). This gives the random-cluster expression exactly, even with parallel edges, and gives the Grothendieck-class and zeta formulas from the affine decomposition.

**5. Dimensions, chromatic cutoff, and reconstruction.** A component's dimension equals the total multiplicity of edges joining differently labeled vertices, so its maximum is the weighted maximum \(h\)-cut. Every edge can be cut simultaneously precisely when the underlying simple graph has a proper \(h\)-coloring. The constant labeling gives dimension zero, while an edge and \(h\ge2\) give a positive-dimensional labeling. Exactly the labelings constant on each graph component give dimension zero.

For a truncated quiver algebra, the surviving nontrivial paths form a basis for \(J\), with \(e_uJe_v\) indexed by paths with endpoints \(u,v\). Thus \(w_{uv}\) counts all nonconstant paths between distinct endpoints, proving the path claim. At fixed \(Q,d\), \(Z_G(X,Y)\) has degree at most \(n\) in \(X\) and at most \(E\) in \(Y\). Since \(2^0,\ldots,2^n\) are distinct, as are \(q^{-1}-1\) for distinct finite-field orders, Lagrange interpolation from the claimed samples recovers \(Z_G\). Conversely the counting formula evaluates it. Finally expanding the polynomial in \(X\) into powers \(X^1,\ldots,X^n\) gives \(C_m(q)\) as a sum of terms proportional to \(2^{jm}\); the stated annihilating recurrence follows.

## Verification

The standalone `CHECKER.py` builds actual truncated path algebras from path concatenation (not from the claimed Peirce formula), enumerates idempotents by the original product equations, tests pairwise commutation for all ordered tuples in the selected small fields, and independently compares both the coloring sum and spanning-subgraph expression. It tests genuine \(\mathbb F_4\) arithmetic, cycles, loops, parallel and opposite arrows, and nilpotency beyond radical square zero. Its complete output is `VERIFY_OUTPUT.txt`: `PEIRCE_POTTS_COMMUTING_IDEMPOTENTS_OK 31`. This finite evidence is corroboration, not a replacement for Steps 1–5.

A particularly informative consistency test compares the upper-triangular \(3\times3\) algebra (radical cube zero) with the radical-square-zero transitive three-arrow algebra. Both give \(26\) idempotents and \(340\) commuting ordered pairs over \(\mathbb F_2\), despite distinct multiplication laws.

## Relationship to prior work

The orthogonal-idempotent conjugacy argument uses a classical lifting principle and Peirce blocks, rather than claiming those tools are new. Zhang's 2012 study of radical-square-zero algebras concerns \(\tau\)-rigid modules. Schaps's 2014 study concerns Peirce/basis graphs for monoid algebras. Anh–Birkenmeier–van Wyk's work on Peirce decompositions includes conjugacy of orthogonal idempotent systems (Lemma 2.18) but not this all-arity affine-scheme census. Sokal's 2005 survey gives the existing Potts/random-cluster expansion; the formula here interprets it through commuting idempotents in split basic algebras.

The previously recorded radical-square-zero quiver results for commuting-tuple **conjugacy-orbit counts** concern a narrower family and count orbits, not these actual points and smooth schemes in arbitrary radical nilpotency. Their diagonal-label conjugacy mechanism is related, and its radical-square-zero specialization is not independently claimed as a fresh discovery. The assessed contribution is the all-nilpotency scheme decomposition, symmetrized Peirce-dimension invariance, and the resulting exact all-arity arithmetic/graph reconstruction.

## Limitations

The split basic hypothesis is essential: arbitrary semisimple matrix factors have non-discrete projector varieties. The formula does not distinguish multiplication structures with the same symmetrized off-diagonal Peirce dimensions, and it cannot reconstruct quiver orientation or diagonal radical blocks. The Tutte reconstruction statement uses a fixed truncated-quiver family across finite fields, not unrelated algebras over varying fields. The recurrence displayed is annihilating but is not asserted to be minimal. This is a mathematical proof with finite computational checks, not independent validation; unlocated equivalent earlier geometric treatments remain a priority risk.

## References

1. X. Zhang, *\(\tau\)-rigid modules for algebras with radical square zero*, arXiv:1211.5622v1, first public 2012-11-23, primary MSC 16G10. https://arxiv.org/abs/1211.5622
2. M. Schaps, *The Coarse Structure of the Representation Algebra of a Finite Monoid*, Journal of Discrete Mathematics (2014), DOI:10.1155/2014/529804. https://doi.org/10.1155/2014/529804
3. P. N. Anh, G. F. Birkenmeier, L. van Wyk, *Peirce decompositions, idempotents and rings*, arXiv:1702.05261v1 (2017), notably Lemma 2.18. https://arxiv.org/abs/1702.05261
4. A. D. Sokal, *The multivariate Tutte polynomial (alias Potts model) for graphs and matroids*, arXiv:math/0503607v1 (2005), Section 2.2 and Theorem 2.3. https://arxiv.org/abs/math/0503607
