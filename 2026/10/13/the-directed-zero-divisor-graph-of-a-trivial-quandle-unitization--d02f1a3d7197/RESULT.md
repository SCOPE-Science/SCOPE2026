# The directed zero-divisor graph of a trivial-quandle unitization

## Finding

Let \(k=\mathbb F_q\) be a finite field of any prime-power order \(q\ge2\), let \(n\ge2\), and let \(Q_n\) be the trivial quandle on \(n\) elements, with \(x*y=x\). Let \(E=k[Q_n]\) and \(S=k\mathbf1\oplus E\) be its formal unitization. The directed zero-divisor graph \(\Gamma(S)\) has as vertices the nonzero nonunits; it has an arrow \(u\to v\) for **distinct** vertices exactly when \(uv=0\). Set \(t=q^{n-1}\) and \(h=q-1\).

**Complete graph description.** Its vertices partition into disjoint sets \(A\), \(B\), \(C\), where \(A=\bigsqcup_{r\in k^{n-1}}A_r\), \(B=\bigsqcup_{r\in k^{n-1}}B_r\), each \(A_r\) and \(B_r\) has \(h\) vertices, and \(|C|=t-1\). All arrows are precisely:

1. Every vertex of \(A_r\) points to every vertex of \(B_r\), for each \(r\), and to no other vertex.
2. Every vertex of \(B\) points to every vertex of \(A\cup C\).
3. Every vertex of \(C\) points to every *distinct* vertex of \(C\) and every vertex of \(A\).

There are no other arrows. Consequently, the bidegrees \((\deg^+,\deg^-)\) are
\[
\begin{array}{c|c|c}
\text{stratum}&\text{size}&(\deg^+,\deg^-)\\ \hline
A&ht&(h,qt-1)\\
B&ht&(qt-1,h)\\
C&t-1&(qt-2,qt-2)
\end{array}
\]
and the number of arrows is
\[
|E(\Gamma(S))|=h^2t+(qt-1)^2-(t-1).
\]
The graph is strongly connected of directed diameter exactly \(3\). Its full directed-graph automorphism group is
\[
\operatorname{Aut}(\Gamma(S))\cong
\Big((\mathfrak S_h\times\mathfrak S_h)\wr\mathfrak S_t\Big)
\times\mathfrak S_{t-1},
\]
where the wreath-product top group permutes the \(t\) matched pairs \((A_r,B_r)\). Finally, \(\Gamma(S)\) determines both \(q\) and \(n\) within this family: the smallest positive outdegree is \(q-1\), and the greatest outdegree is \(q^n-1\). These numbers recover \(q\) and then \(n\).

The formal unitization is associative, although quandle algebras generally need not be. For \(n=2\), the algebra is the ordinary \(2\times2\) upper-triangular matrix ring, a case already treated in earlier literature; the new full-parameter classification is particularly relevant for \(n\ge3\) and \(q>2\).

## Assumptions and scope

The ground field \(k\) has \(q\) elements and arbitrary characteristic. The operation of the trivial quandle is \(x*y=x\); its algebra multiplication is \(uv=\varepsilon(v)u\), where \(\varepsilon:E\to k\) sums the basis coefficients. Unitization means adjoining a new unit \(\mathbf1\), not identifying any quandle basis element with a unit. The graph is a loopless directed graph on nonzero two-sided zero divisors, equivalently on nonzero nonunits for this finite-dimensional algebra. Self-annihilating vertices are counted but their loops are deleted. All formulas include the boundary \(q=2,n=2\); no assertion is made for an infinite coefficient field.

## Proof

Choose one quandle basis element \(e_0\), put \(W=\ker\varepsilon\), and write every element of \(S\) uniquely as \(s\mathbf1+\alpha e_0+w\) with \(w\in W\). Set \(\lambda=s\) and \(\mu=s+\alpha\). Since \(uv=\varepsilon(v)u\) in \(E\), multiplying two elements in these coordinates gives
\[
(\lambda,\mu,w)(\tau,\nu,z)
=(\lambda\tau,\mu\nu,\lambda z+\nu w).
\]
Thus \(S\) is explicitly isomorphic to the triangular algebra
\[
\left\{\begin{pmatrix}\lambda&w\\0&\mu\end{pmatrix}:
\lambda,\mu\in k,\ w\in W\right\},
\]
where the off-diagonal component is a \(k\)-vector space of dimension \(n-1\). A triple is invertible exactly when both diagonal coordinates are nonzero: in that case its inverse is \((\lambda^{-1},\mu^{-1},-\lambda^{-1}\mu^{-1}w)\). Every nonzero nonunit has one of exactly three forms:
\[
A:\lambda\ne0,\mu=0;\qquad
B:\lambda=0,\mu\ne0;\qquad
C:\lambda=\mu=0,\ w\ne0.
\]
For every \(r\in W\), set
\[
A_r=\{(\lambda,0,\lambda r):\lambda\in k^\times\},\quad
B_r=\{(0,\nu,-\nu r):\nu\in k^\times\}.
\]
The product formula shows that the only outgoing arrows from a vertex of \(A_r\) are to vertices of \(B_r\), because \((\lambda,0,\lambda r)(0,\nu,-\nu s)=0\) exactly when \(r=s\). A vertex of \(B\) annihilates on the right every vertex of \(A\cup C\), and no other nonzero nonunit. A vertex of \(C\) annihilates on the right every vertex of \(A\cup C\), and no vertex of \(B\). The last assertion includes self-products, so deleting loops removes exactly \(t-1\) arrows. This proves the complete adjacency description and vertex counts.

A vertex of \(A\) has \(h\) outgoing neighbors and receives arrows from all \(ht\) vertices of \(B\) and all \(t-1\) vertices of \(C\), hence has bidegree \((h,qt-1)\). Reversing direction gives \((qt-1,h)\) on \(B\); a vertex of \(C\) has \(ht+t-2=qt-2\) outgoing and incoming neighbors. Counting arrows from the three strata, with loops removed, gives the stated formula.

The displayed directed-graph description supplies paths of length at most three between any two vertices: paths pass through \(B\to A\) and, when necessary, a matching edge \(A_r\to B_r\). For distinct slopes \(r,s\), any path from \(A_r\) to \(B_s\) has length at least three: the first step must land in \(B_r\), which has no arrow to any vertex of \(B\); a length-three path exists through \(A_s\). Since \(t\ge2\), the directed diameter is exactly three.

For automorphisms, the three strata are intrinsic because their ordered bidegree pairs are distinct for every \(q\ge2,n\ge2\). Within \(A\), the nonempty outgoing-neighborhood equivalence classes are exactly the \(A_r\); the corresponding \(B_r\) classes are determined by their incoming-neighborhood sets from \(A\). Thus every automorphism permutes the \(t\) matched block pairs jointly and may independently permute the \(h\) vertices in each \(A_r\) and each \(B_r\). All \(t-1\) vertices of \(C\) are mutually indistinguishable as graph vertices, so they admit an independent full symmetric group. Conversely every such permutation preserves all displayed arrows. This proves the wreath-product description, including the degenerate symmetric groups when \(h=1\) or \(t-1=1\).

Finally \(h\) is the smallest outdegree, while \(qt-1\) is the largest; hence graph isomorphisms preserve \(q=h+1\) and \(q^n=qt\), determining \(n\) uniquely. This also proves the parameter-reconstruction statement.

## Verification

The included `verify.py` separately computes the original unitized quandle multiplication and the triangular model and verifies agreement on every ordered pair of elements for \((q,n)=(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(4,3),(5,2),(5,3)\). The order-four cases use explicit finite-field arithmetic with a quadratic irreducible polynomial. For each case it exhaustively constructs the directed zero-product relation, checks all three vertex classes, the predicted bidegree pairs, the absence or presence of square-zero loops, and the arrow formula. Its terminal success marker is `VERIFY_OK`.

For orientation, the loopless graph at \((q,n)=(3,3)\) has \(44\) vertices and \(704\) arrows, distributed among strata of sizes \(18,18,8\). Additional full graph-automorphism enumeration in the small instances \((2,2),(2,3),(3,2)\) gives group orders \(2,144,768\), respectively, matching the theorem. These finite checks complement, rather than replace, the all-parameter proof.

## Relationship to prior work

Churchill, Churchill, Fernando, and Kousik (2026) introduce the zero-divisor graph of an extended quandle ring, characterize zero divisors of unitized trivial-quandle rings through equations over finite fields, and exhibit explicit binary-field degree data and mirror symmetry (Definition 1.9, Section 6.1). Their finite-field membership criterion and binary examples are credited. They do not state the matched-block decomposition, arbitrary-prime-power bidegree spectrum, complete graph-automorphism group, or graph parameter reconstruction. The present proof makes these consequences exact by identifying the unitization with a two-vertex triangular algebra with an \((n-1)\)-dimensional off-diagonal space.

Li and Tucci (2013) analyze directed zero-divisor graphs of ordinary upper-triangular matrix rings and fully describe the \(2\times2\) case over finite fields, which covers our \(n=2\) boundary. Fenstermacher and Gegner (2014) likewise examine \(2\times2\) triangular matrix rings over residue rings. These results must not be confused with the many-parallel-arrow case \(n\ge3\): the latter is a different triangular algebra and its graph automorphisms need not be matrix-induced. Earlier work on general triangular rings may contain an equivalent formulation; see limitations.

## Limitations

The theorem classifies only **trivial** finite quandles and their **formal unitizations**, with the specified zero-product graph convention. It does not classify arbitrary quandle rings, nontrivial Alexander quandles, or the more general triangular matrix rings with nontrivial diagonal algebras. The computations check fields of orders \(2,3,4,5\) for several small ranks, not every prime power. An older generalized triangular-algebra graph theorem could subsume part of the structure; the 2011 triangular-matrix paper and the complete 2013 paper were not fully accessible during the literature comparison. The originality assessment is therefore not an independent certification.

## References

1. G. Churchill, I. R. Churchill, N. Fernando, B. Kousik, *A further study of quandles and quandle rings*, arXiv:2608.09149v1 (2026), Definition 1.9 and Section 6.1.
2. A. Li, R. P. Tucci, *Zero Divisor Graphs of Upper Triangular Matrix Rings*, Communications in Algebra **41** (2013), 4622–4636, doi:10.1080/00927872.2012.706841.
3. T. Fenstermacher, E. Gegner, *Zero-divisor graphs of 2×2 upper triangular matrix rings over integers modulo n*, Missouri Journal of Mathematical Sciences **26** (2014), 151–167, doi:10.35834/mjms/1418931956.
4. B. Li, *Zero-divisor graph of triangular matrix rings over commutative rings* (2011), bibliographic abstract (possible broader prior coverage not excluded).
