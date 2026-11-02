# Independent mathematical audit

## correctness

PASS

Right translations are the diagonal conjugation/coordinate actions T_sigma. Every transposition fixes a label for n>=3, so those actions generate a faithful inner S_n. The characteristic subset D={(i,id)} consists exactly of elements whose right translation is identity; an automorphism induces a permutation on D, removable by the canonical diagonal S_n subgroup. A residual automorphism fixes each permutation label (restriction of right translation to D) and commutes with all diagonal conjugations, hence induces a centralizer-equivariant permutation on the fixed-point fiber of sigma. C_{S_n}(sigma) contains the entire permutation group S_m on m fixed points, whose centralizer in Sym(m) is its center: trivial unless m=2, where there is one swap. Conjugacy equivariance makes the swaps independent precisely by two-fixed-point cycle type; their number is p(n-2)-p(n-3). These swaps commute with diagonal S_n, proving the direct product Aut(P_n)=S_n x (C2)^(p(n-2)-p(n-3)); size n!, Inn=S_n. An independently implemented checker exhaustively counted all 720 maps of P_3 (only six automorphisms) and checked all 48 constructed automorphisms of P_4. This is bounded corroboration; the centralizer proof covers every n>=3.

## originality

PASS

The fixed-point quandle and embedding are established in Kai 2026; the independent full automorphism formula depends on a centralizer-of-fixed-fiber calculation. Public abstracts of Kai and prior automorphism papers do not affirm that specific formula, while the known order-six tables cover n=3. Qualified best-of-knowledge PASS only: Kai is the closest same-object source, its full primary text could not be read during this run, and the Oxford authorized service returned vpn_disconnected, which is a material unresolved priority risk rather than a scientific counterexample.

## value

PASS

The fixed-point quandle is a canonical factorial-size host in a Cayley-type embedding for all n-element quandles. Determining its entire automorphism group and the exact partition-indexed family of exceptional involutions is a natural structural invariant substantially stronger than knowing the inner group or orbit decomposition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
