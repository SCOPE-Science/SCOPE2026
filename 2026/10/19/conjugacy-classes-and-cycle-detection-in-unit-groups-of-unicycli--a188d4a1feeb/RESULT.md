# Algebraic unit groups of height-one unicyclic incidence algebras

## Finding

Let \(P\) be a finite height-one poset whose undirected Hasse graph is simple, connected and unicyclic. Write \(m\) for its number of edges and \(c\) for the length of its unique cycle. Over any field \(k\), the algebraic group of units \(U(P)=I(P,k)^\times\), viewed as a group scheme over \(k\), is isomorphic to
\[
\mathbb G_m\times(\mathbb G_a^m\rtimes T_{m,c}),\qquad
T_{m,c}=\{w\in\mathbb G_m^m:w_1w_3\cdots w_{c-1}=w_2w_4\cdots w_c\}.
\]
The torus acts on the additive coordinates by the respective characters \(w_i\). Moreover, **two such algebraic groups over the same field are isomorphic if and only if their pairs \((m,c)\) agree**. The cycle length is recovered from the support of the unique primitive relation among the characters of the quotient torus on the Lie algebra of the unipotent radical.

The algebraic group does not recover the incidence algebra, even up to passage to the opposite algebra. For an example, let \(P_1,P_2\) have vertices \(0,1,2,3,4,5\), with covers directed from the first vertex to the second:
\[
E(P_1)=\{01,21,23,03,04,05\},\qquad
E(P_2)=\{01,21,23,03,04,25\}.
\]
Both have \((m,c)=(6,4)\), but their incidence algebras are neither isomorphic nor anti-isomorphic over any field.

## Assumptions and scope

Height one means there are no strict chains of three elements, and all edges go from minimal to maximal elements. The cycle is even and has length at least four. Connectedness and unicyclicity give \(|P|=m\). The classification is of split algebraic unit groups, not of their abstract groups of rational points over every field. In particular \(c\) need not be visible on \(\mathbb F_2\)-points. The field may have any characteristic.

## Proof

**The weight action.** The Jacobson radical \(J\) of \(I(P,k)\) has basis the edge matrix units and satisfies \(J^2=0\). The diagonal gives a split torus \(D=(\mathbb G_m)^m\). Every unit factors uniquely as \((1+x)d\) for \(x\in J\), \(d\in D\), also over any commutative \(k\)-algebra. Thus \(U(P)=(1+J)\rtimes D\) with \(1+J\simeq\mathbb G_a^m\) and \(d\) acting on edge \(a\prec b\) by the character \(d_a/d_b\).

**A normal form.** Delete one cycle edge and root the spanning tree. Its edge ratios and the root value recover all vertex values by multiplication and inversion. These are inverse monomial coordinate maps, not only maps on field-valued points. The kernel of all edge ratios is the scalar diagonal. Number the cycle edges in cyclic order; traversal alternates between the edge direction and its reverse, so the omitted edge ratio is determined by the displayed alternating product equation. All other edge ratios are free. This realizes the weight image as \(T_{m,c}\) and splits the scalar kernel by taking the root vertex value to be one. The scalar factor acts trivially; the resulting normal form proves sufficiency of \((m,c)\).

**An intrinsic cycle invariant.** The subgroup \(V=1+J\) is the unipotent radical: it is connected normal unipotent and \(U(P)/V=D\) is a torus, which has no nontrivial connected unipotent subgroup. This description can also be made after scalar extension to an algebraic closure. Because \(V\) is abelian, the conjugation representation on \(\operatorname{Lie}V\) factors through \(U(P)/V\). An algebraic group isomorphism carries the radical to the radical and gives an isomorphism of the quotient tori intertwining the Lie algebra representations. It therefore preserves \(m=\dim V\) and the multiset of character weights up to an isomorphism of character lattices. Taking this differential works in positive characteristic as well: the differential of an isomorphism has an inverse.

The weights are the \(m\) edge characters, each occurring once. The spanning-tree characters are independent: with the root fixed to one, they are coordinates on a torus of rank \(m-1\). The kernel of the integral map from \(\mathbb Z^m\) sending its basis vectors to the weights has rank one. The alternating relation has coefficients \(\pm1\) on exactly the cycle edges and zero elsewhere. Since that vector is primitive, it generates the kernel. Its support cardinality is invariant under permuting the weights and changing the basis of the quotient torus character lattice. It is \(c\), which proves necessity without counting finite-field points.

**Nonreconstruction.** The two undirected degree multisets are \((4,2,2,2,1,1)\) and \((3,3,2,2,1,1)\). In the height-one case the graph can be recovered from the algebra: viewing \(J\) as an \((I(P,k)/J)\)-bimodule is well-defined since \(J^2=0\). The nonzero edge spaces are detected by \(\bar e_a J\bar e_b\ne0\) for the primitive coordinate idempotents of \(I(P,k)/J\simeq k^m\). Reversing multiplication transposes this incidence data and leaves the undirected degree multiset unchanged. The displayed algebras are therefore neither isomorphic nor anti-isomorphic, while their unit groups have the same normal form.

## Relation to prior results and verification

The numerical class count is not part of the structural contribution. The earlier general class-number identity for radical-square-zero quiver units, \((q-1)^{\kappa(G)}T_G(q,q)\), specializes here to \(q^m+(q-2)q^{m-c+1}\): the \(m-c\) bridges contribute \(q^{m-c}\) and \((q-1)T_{C_c}(q,q)=q^c+q^2-2q\). Together with group order, this known invariant also distinguishes \((m,c)\) for abstract unit groups at fixed \(q>2\). At \(q=2\) the rational points of the diagonal torus are trivial. The classification above instead gives the all-field classification as algebraic groups, including an intrinsic character-lattice mechanism for necessity and explicit isomorphisms for sufficiency. Class spectra alone do not construct such isomorphisms.

The original `verify.py` provides finite checks of the edge ratio change of coordinates for the displayed pair, and also tests the known finite-field class-count identity. These checks do not prove the character-lattice necessity or the classification over arbitrary fields. The spanning-tree and representation arguments give these conclusions exactly.

## References

1. *Tutte evaluations and full inner conjugacy spectra of radical-square-zero quiver unit groups*, Resultary record [`f79766dd4bb5`](https://github.com/Resultary/2026/tree/main/2026/10/12/SCOPE-tutte-evaluations-and-full-inner-conjugacy-spectra-of-radical-sq--f79766dd4bb5), general class-number formula.
2. *Conjugacy class size spectrum of radical-square-zero quiver unit groups*, Resultary record [`17f3f95e6cb8`](https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-conjugacy-class-size-spectrum-of-radical-square-zero-quiver-unit--17f3f95e6cb8).
3. R. P. Stanley, *Structure of incidence algebras and their automorphism groups*, Bull. Amer. Math. Soc. **76** (1970), 1236–1239, Theorem 1 (general incidence-algebra reconstruction).
