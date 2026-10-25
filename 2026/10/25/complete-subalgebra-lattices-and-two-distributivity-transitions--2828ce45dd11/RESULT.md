# Complete subalgebra lattices and two distributivity transitions in a non-solvable evolution-algebra family
## Finding
Let \(K\) be any field with \(\operatorname{char}K\ne2\), and let \(\lambda\in K^\times\). The evolution algebra \(E_\lambda\) has natural basis \(e_1,e_2,e_3\) satisfying
\[
e_1^2=-e_1-e_3,\qquad e_2^2=-2e_1+\lambda e_2+(\lambda-2)e_3,\qquad e_3^2=e_1+e_3,
\]
and \(e_i e_j=0\) for \(i\ne j\). All subalgebras here are linear subspaces closed under multiplication, including zero and the whole algebra.

Put \(u=e_1+e_3\), \(v=e_2+e_3\), \(w=e_3\), \(t=w-u/2\), \(S=Ku+Kv\), and \(T=Ku+Kw\). The **complete** list of subalgebras, with no repetition, is
\[
0,\quad Ku,\quad Kt,\quad S,\quad T,\quad E_\lambda,
\]
together with \(L_\lambda=K(v+u/(2-\lambda))\) when \(\lambda\ne2\), and, only when \(\lambda=4\), the additional plane
\[
P=K(v-u/2)+K(w-u/2).
\]
In particular, there are exactly \(6\), \(8\), and \(7\) subalgebras when \(\lambda=2\), \(\lambda=4\), and \(\lambda\notin\{2,4\}\), respectively.

The subalgebra lattice is **distributive if and only if** \(\lambda\in\{2,4\}\). At \(\lambda=4\) it is the eight-element Boolean lattice \(B_3\). At \(\lambda=2\) it is the six-element lattice of order ideals of a three-element poset consisting of a two-element chain and one isolated point. At all remaining parameters the lattice is nondistributive. Every \(E_\lambda\) in this family is non-solvable; hence the two distributive instances are non-solvable examples.

## Assumptions and scope
The field is not assumed algebraically closed or finite. No restriction on \(\lambda\) is made beyond nonzero; the cases \(2\) and \(4\) refer to their images in \(K\) and are distinct because the characteristic is not two. The classification concerns all vector-space subalgebras, not only evolution subalgebras, ideals, or associative subalgebras.

The basis \(u,v,w\) yields the multiplication table
\[
u^2=0,\quad uv=uw=vw=w^2=u,\quad v^2=-u+\lambda v.
\]
Consequently \(E_\lambda^2=S\), and \(S\) is a two-dimensional subalgebra. The classification is invariant under extension of the coefficient field within characteristic different from two.

## Proof
**Lines.** For \(x=x_1e_1+x_2e_2+x_3e_3\),
\[
x^2=(x_3^2-x_1^2-2x_2^2)u+\lambda x_2^2v.
\]
If \(x^2=0\), independence of \(u,v\) and \(\lambda\ne0\) imply \(x_2=0\) and \(x_3^2=x_1^2\). As \(\operatorname{char}K\ne2\), the two nonzero square-zero lines are exactly \(Ku=K(e_1+e_3)\) and \(Kt=K(e_1-e_3)\). If \(Kx\) is a one-dimensional subalgebra with \(x^2\ne0\), then \(x^2\in Kx\cap S\), hence \(x\in S\). Write \(x=au+bv\). Its square is \((2ab-b^2)u+\lambda b^2v\). Necessarily \(b\ne0\); comparing with \(x^2=(\lambda b)x\) gives \(b=(2-\lambda)a\). Thus a third line exists precisely when \(\lambda\ne2\), and it is \(L_\lambda=K(v+u/(2-\lambda))\). Conversely these lines are closed.

**Planes containing \(Ku\).** Such a plane is \(Q=Ku+K(bv+cw)\) with \((b,c)\ne(0,0)\). The square of \(y=bv+cw\) is
\[
y^2=(-b^2+2bc+c^2)u+\lambda b^2v.
\]
If \(b\ne0\), closure of \(Q\) forces \(v\in Q\), and therefore \(Q=S\). If \(b=0\), then \(Q=T\). Both \(S\) and \(T\) are closed by the displayed multiplication table.

**Planes not containing \(Ku\).** Such a plane \(Q\) intersects the two-dimensional subalgebra \(S\) in a line: the intersection has dimension at least one by the dimension formula, and cannot equal \(S\) because \(Ku\not\subset Q\). The intersection is a subalgebra, so by the line classification it must be \(L_\lambda\), which requires \(\lambda\ne2\). Let \(a=(2-\lambda)^{-1}\) and \(z=v+au\). After subtracting a multiple of \(z\), the second generator of \(Q\) can be written \(h=w+cu\). Closure requires
\[
zh=(1+a+c)u\in Q,\qquad h^2=(1+2c)u\in Q.
\]
Since \(u\notin Q\), both coefficients vanish, so \(c=-1-a\) and \(1+2c=0\). Equivalently \(a=-1/2\), which in turn is equivalent to \(\lambda=4\). Then \(c=-1/2\) and \(Q=P=K(v-u/2)+K(w-u/2)\). Conversely, direct substitution gives \((v-u/2)(w-u/2)=0\), \((w-u/2)^2=0\), and \((v-u/2)^2=4(v-u/2)\). Hence \(P\) is closed. Finally, dimension zero and dimension three contribute only \(0\) and \(E_\lambda\), completing exhaustiveness.

**Lattice types.** For \(\lambda=4\) the three lines \(Ku\), \(Kt\), and \(L_4\) are independent, and their three pairwise spans are exactly \(T\), \(S\), and \(P\). Along with \(0\) and \(E_4\), these give all eight subsets of three atoms, hence the Boolean lattice \(B_3\). For \(\lambda=2\), the nontrivial inclusions are \(Ku\subset S\), \(Ku\subset T\), and \(Kt\subset T\). The mapping
\[
0\mapsto\varnothing,\quad Ku\mapsto\{a\},\quad Kt\mapsto\{b\},\quad T\mapsto\{a,b\},\quad S\mapsto\{a,c\},\quad E_2\mapsto\{a,b,c\}
\]
is a lattice isomorphism onto the order ideals of the poset with \(a<c\) and \(b\) incomparable to both. Such an order-ideal lattice is distributive. For \(\lambda\notin\{2,4\}\), let \(U=Ku\), \(V=Kt\), and \(W=L_\lambda\). The plane \(V+W\) is not a subalgebra (the plane classification), so \(V\vee W=E_\lambda\), whereas \(U\wedge V=U\wedge W=0\). Thus
\[
U\wedge(V\vee W)=U\ne0=(U\wedge V)\vee(U\wedge W),
\]
exhibiting failure of distributivity.

## Verification
An independent implementation enumerates all row-reduced subspaces of \(\mathbb F_p^3\), tests closure under every basis product, and compares the complete list with the formulas. It checks every \(\lambda\in\mathbb F_p^\times\) for \(p=3,5,7,11\), totaling 22 parameter-field pairs. Running `python verify.py` reports `VERIFY_OK`. The finite check confirms the formulas in these examples, while the preceding classification proof establishes the theorem for all fields of characteristic different from two.

## Relationship to prior work
Hu and Wen introduced this non-solvable three-dimensional family and determined its idempotent behavior; the complete subalgebra lattice and the two distributivity transitions are not stated in their inspected arXiv manuscript. Ladra, Páez-Guillán, and Pérez-Rodríguez study distributivity of subalgebra lattices for **solvable** evolution algebras, so their principal classification does not imply a result for these non-solvable members. Their work nevertheless motivates asking how distributivity behaves beyond solvability. Ladra and Pérez-Rodríguez prove inheritance properties for subalgebras of regular evolution algebras; \(\dim E_\lambda^2=2<3\), so regularity does not hold here.

A published analysis entitled *A single symmetry jump in the \(E_\lambda\) evolution-algebra family* determines automorphisms, with a jump at \(\lambda=4\). That automorphism-group statement does not specify the seven-, eight-, or six-element subalgebra lattices, nor establish the separate distributivity transition at \(\lambda=2\). The earlier classification of all complex three-dimensional evolution-algebra isomorphism types is relevant background, but does not by itself give the parameter-uniform lattice calculations here.

## Limitations
The theorem does not address characteristic two or classify subalgebra lattices of arbitrary three-dimensional evolution algebras. The non-solvability of the family and its idempotent statements belong to the motivating paper, not to this theorem. The older three-dimensional classification and its associated unpublished or implicit stabilizer/subalgebra calculations could contain equivalent special-case information not isolated by title-based search; this remains an originality risk. No claim of independent verification is made.

## References
1. X.-Y. Hu and R. Wen, *Idempotent-free non-solvable evolution algebras over \(\mathbb C\)*, arXiv:2609.25023v1 (first posted 2026-08-12), https://arxiv.org/abs/2609.25023.
2. M. Ladra, P. Páez-Guillán, and A. Pérez-Rodríguez, *On the subalgebra lattice of solvable evolution algebras*, arXiv:2502.05619v1 (2025), https://arxiv.org/abs/2502.05619.
3. M. Ladra and A. Pérez-Rodríguez, *Regular evolution algebras are closed under subalgebras*, arXiv:2503.07187v1 (2025), https://arxiv.org/abs/2503.07187.
4. *A single symmetry jump in the \(E_\lambda\) evolution-algebra family*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-single-symmetry-jump-in-the-e-lambda-evolution-algebra-family--1a1e7e2dd0e3.
5. Y. Cabrera Casado, M. Siles Molina, and M. V. Velasco, *Classification of three-dimensional evolution algebras*, Linear Algebra and its Applications 524 (2017), 68–108; arXiv:1701.07219.
