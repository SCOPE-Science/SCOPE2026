# Forest incidence algebras have a universal commutator Lie reduct and all-arity centralizer spectra

## Finding
Let \(P\) be any finite poset having no chain of three distinct comparable elements, and suppose its undirected Hasse graph is a forest with \(m\) edges and \(c\) connected components (isolated vertices count as components). Let \(k\) be any field and let \(A=I(P,k)\) be the ordinary incidence algebra. Give \(A\) its commutator Lie bracket \([a,b]=ab-ba\), and let \(\mathfrak b_k\) denote the two-dimensional nonabelian Lie algebra with basis \(h,r\) and \([h,r]=r\). Then
\[
(A,[\ ,\ ])\cong k^{\oplus c}\oplus\mathfrak b_k^{\oplus m}
\]
as Lie algebras, in every characteristic. In particular, the commutator Lie algebra retains only \((c,m)\), even though the associative incidence algebra can retain the entire orientation and shape of the forest.

For \(k=\mathbb F_q\) and an integer \(s\ge1\), let \(\Psi_{\boldsymbol a}:A\to A^s\) be \(b\mapsto([a_1,b],\ldots,[a_s,b])\), and define the complete joint-centralizer codimension enumerator
\[
F_{P,s}(t)=\sum_{\boldsymbol a\in A^s}t^{\operatorname{rank}_k\Psi_{\boldsymbol a}}.
\]
Its exact value is
\[
\boxed{F_{P,s}(t)=q^{cs}\left(1+(q^s-1)(q+1)t+(q^s-1)(q^s-q)t^2\right)^m.}
\]
The common centralizer of \(\boldsymbol a\) has \(k\)-dimension \(2m+c-\operatorname{rank}\Psi_{\boldsymbol a}\), so the formula supplies every common-centralizer dimension and multiplicity at every tuple length. The exact number of pairwise-commuting ordered \(s\)-tuples is
\[
\boxed{q^{cs}\left(1+(q^s-1)(q+1)\right)^m,}
\]
and its probability is
\[
\boxed{\left(\frac{1+(q^s-1)(q+1)}{q^{2s}}\right)^m.}
\]

For every \(m\ge3\), a star poset and an alternating-path poset, each on \(m+1\) vertices with \(m\) cover relations, have isomorphic commutator Lie algebras but associative incidence algebras that are neither isomorphic nor anti-isomorphic. Thus even the entire system of joint-centralizer distributions over all finite fields and all tuple lengths does not distinguish these nonisomorphic associative algebras.

## Assumptions and scope
The height restriction means every strict interval contains exactly its two endpoints. A Hasse edge \(e=(u,v)\) is oriented from its minimal to its maximal endpoint, \(u<v\). The ordinary incidence-algebra basis consists of diagonal idempotents \(e_{vv}\), for \(v\in P\), and radical elements \(e_{uv}\), one for each cover relation. The multiplication is convolution; in particular \(e_{uv}e_{xy}=\delta_{vx}e_{uy}\) whenever defined. Because no strict chain has three vertices, the radical \(J\) satisfies \(J^2=0\). All fields are allowed for the Lie isomorphism. Point counts concern every finite field, of arbitrary characteristic, and all integers \(s\ge1\). No restrictions on a tree's degree sequence or the orientation of its bipartite levels are imposed.

## Proof
Write an element as \(a=D+X\), with \(D=\sum_v d_ve_{vv}\) and \(X=\sum_{e=(u,v)}x_ee_{uv}\). Since diagonal elements commute and \(J^2=0\), the bracket of \(a=D+X\) with \(b=E+Y\) has coefficient
\[
[a,b]_e=(d_u-d_v)y_e-(e_u-e_v)x_e
\]
on each edge \(e=(u,v)\). Distinct edges do not interact.

Consider the linear edge-difference map \(\partial:k^{P}\to k^{E}\), \((d_v)\mapsto(d_u-d_v)_{e=(u,v)}\). On every forest component, fixing a root value and prescribing arbitrary edge differences uniquely determines the remaining vertex values: use the unique simple path from the root to each vertex. Therefore \(\partial\) is surjective and its kernel consists of functions constant on each component, of dimension \(c\). Choose diagonal elements \(h_e\) whose edge-difference vectors form the standard basis of \(k^E\). Let \(r_e=e_{uv}\) be the radical arrow elements, and let \(z_C=\sum_{v\in C}e_{vv}\) for each component \(C\). These form a basis of \(A\), and the only nonzero basic Lie brackets, up to skew symmetry, are \([h_e,r_f]=\delta_{ef}r_f\). In particular every \(z_C\) is central, and every pair of distinct edge summands commutes. This proves the displayed Lie isomorphism over any field, including characteristic two.

Fix \(s\ge1\). In the Lie basis just constructed, every tuple entry has independent coordinates \(\alpha_{i,C}\) on the \(c\) central generators and \(d_{i,e},x_{i,e}\) on each two-dimensional edge summand. The central coordinates contribute \(q^{cs}\) choices and never change the joint commutator map. For a fixed edge, \(\Psi_{\boldsymbol a}\) restricts on the domain \(\operatorname{span}\{h_e,r_e\}\) to an \(s\)-by-\(2\) matrix whose columns, up to a harmless sign, are \((x_{i,e})_{i=1}^s\) and \((d_{i,e})_{i=1}^s\). Different edges act on disjoint domain and codomain summands; consequently their ranks add. There are exactly \(1\) rank-zero matrices, \((q^s-1)(q^2-1)/(q-1)=(q^s-1)(q+1)\) rank-one matrices, and \((q^s-1)(q^s-q)\) rank-two matrices of size \(s\)-by-\(2\). Independence gives the stated polynomial.

Two tuple entries commute precisely when, on every edge, the determinant of their corresponding two row vectors vanishes. Thus an entire tuple is pairwise commuting precisely when each associated \(s\)-by-\(2\) matrix has rank at most one. There are \(1+(q^s-1)(q+1)\) matrices of rank at most one on an edge. Multiplying independent factors gives the tuple count; dividing by \(|A|^s=q^{s(2m+c)}\) gives the probability.

For nonisomorphism examples, take the star with one minimal vertex and \(m\) maximal vertices; compare it with the alternatingly oriented path on \(m+1\) vertices. Both are height-one tree posets. For \(m\ge3\), the path has at least two minimal and at least two maximal elements. In any connected height-one incidence algebra, \(\dim_k\operatorname{Ann}_{\ell}(J)=\dim A-\#\operatorname{Min}(P)\) and \(\dim_k\operatorname{Ann}_{r}(J)=\dim A-\#\operatorname{Max}(P)\): multiplication against a radical edge detects exactly the diagonal coefficients at its lower or upper endpoint, respectively. These intrinsic associative invariants are \((2m,\,m+1)\) for the star and are both at most \(2m-1\) for the alternating path. The latter cannot be isomorphic to either the star algebra or its opposite, whose invariants exchange under passage to the opposite. Both Lie reducts are nevertheless \(k\oplus\mathfrak b_k^{\oplus m}\), completing the proof.

## Verification
The standalone file `verify.py` builds commutator matrices in the original incidence-algebra basis, without using the abstract Lie decomposition to compute their ranks. It checks Lie-basis invertibility and brackets for star and fence trees over prime fields of orders \(2,3,5\). Exhaustive checks cover joint rank spectra for the two four-vertex trees at \((q,s)=(2,1),(2,2)\), the three-vertex fork at \((3,2)\) and \((2,3)\), and independently count pairwise-commuting tuples. To run it, use `python3 verify.py` in the directory containing the file. The expected terminal line is `VERIFY_OK`. No finite enumeration is used as an infinite-field proof.

For example, for each of the two nonisomorphic seven-dimensional algebras at \((q,s)=(2,2)\), the joint-rank multiplicities for ranks \(0,1,2,3,4,5,6\) are \(4,108,1044,4212,6264,3888,864\), respectively, and exactly \(4000\) of the \(16384\) ordered pairs commute. The general proof above is independent of these calculations.

## Relationship to prior work
Classical incidence-algebra constructions, including Joseph (2002), provide the algebraic setting. Fornaroli, Khrypchenko and Santulo (2020, 2021 preprints) give a detailed theory of Lie automorphisms of incidence algebras, including the role of cycles and admissible permutations of intervals; their results address automorphisms of a fixed incidence algebra rather than the universal cross-poset Lie-isomorphism normal form and joint-centralizer enumerators established here.

The one-element operator-rank distribution for forest incidence algebras is already a special case of a more general graph/Tutte derivation-rank formula; it is included here as the \(s=1\) boundary of a unified all-arity formula, not as a separate new result. Likewise a general commuting-pair Tutte evaluation for radical-square-zero quiver algebras already implies the \(s=2\) commuting probability. Neither fact supplies the full common-centralizer codimension distribution for every \(s\ge2\), the commuting-tuple counts for every \(s\ge3\), or the stated cross-poset Lie-algebra normal form as its reported conclusion. The substantive assertion here is the universal Lie-type collapse with its complete all-arity consequences, not an isolated two-element probability.

## Limitations
The theorem requires the Hasse graph to be a forest and the poset to have no strict chain of three elements. Cycles impose dependencies among edge differences; longer chains yield nonzero products of radical arrows, so the block decomposition generally fails. The result concerns commutator Lie reducts, common centralizers of arbitrary tuples, and pairwise commuting tuples, not the classification of all associative algebras with those statistics or their unit groups. Existing automorphism/derivation results contain closely related structural ingredients; stronger coverage in literature not located by the inspected searches is a residual originality risk. Independent mathematical validation has not been performed.

## References
- Ancykutty Joseph, “On incidence algebras and directed graphs,” *International Journal of Mathematics and Mathematical Sciences* **31** (2002), 301–305, https://doi.org/10.1155/S0161171202007925 (first published 1 August 2002).
- Érica Z. Fornaroli, Mykola Khrypchenko and Ednei A. Santulo Jr., “Lie automorphisms of incidence algebras,” arXiv:2012.06661 (first version 2020), https://arxiv.org/abs/2012.06661.
- Érica Z. Fornaroli, Mykola Khrypchenko and Ednei A. Santulo Jr., “Proper Lie automorphisms of incidence algebras,” arXiv:2108.03765 (2021), https://arxiv.org/abs/2108.03765.
