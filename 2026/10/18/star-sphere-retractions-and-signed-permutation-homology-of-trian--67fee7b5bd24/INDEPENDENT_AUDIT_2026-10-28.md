# Independent mathematical audit

## correctness

PASS

For n>=7, the n-1 spoke vertices A_i form an induced boundary of an (n-2)-simplex: omitted spoke neighbors witness each proper subset, while no edge of K_n is adjacent to every spoke. Fixing three anchors outside i, the vertex map r_i sends a nonspoke edge e to the first anchor not incident with e. Every N_{T_n}({u,v}) maps to a proper subset of A_i: if i belongs to center, spoke {i,other endpoint} is omitted; if i avoids center, images use at most five of n-1>=6 possible labels. Thus r_i:X_n->boundary Delta(A_i) fixes its sphere and is simplicial. The image of any other spoke sphere A_j has at most four vertices, a simplex in the target (n-1>=6); its top homology map vanishes. The combined maps yield r_i*[z_j]=delta_ij and a split Z^n injection on H_{n-3}(X_n;Z), not necessarily S_n-equivariantly. The deleted-position orientation identity gives sigma[z_i]=sgn(sigma)(-1)^(i+sigma(i))[z_{sigma(i)}]; w_i=(-1)^i[z_i] is the sign-twisted natural permutation basis. For n=7, independent complete generation of all 18,494 faces produced f-vector (21,210,1190,3780,5187,4410,2520,945,210,21), exact F2 boundary ranks 2534 and 2646 in degrees 4 and 5 and dim H_4(F2)=5187-2534-2646=7. The integral Z^7 lower bound combined with UCT upper bound gives exactly seven rational generators, decomposing as Specht(1^7)+Specht(2,1^5). Independent facet-map checks passed for n=7..11; the unlimited n proof is the two-case argument, not extrapolation.

## originality

PASS

Best-of-knowledge original: a complete earlier triangular-graph computation covers the mod-two dimension seven at n=7, and general duality/clique theorems and the signed block-graph theorem do not imply an explicit Z^n split summand of N(L(K_n)) for every n>=7 or its natural sign-twisted S_n representation. Read the exact closest published RESULT.md, relevant full arXiv theorem/proof and complete open-access neighborhood article. Not a guarantee against unindexed equivalent work.

## value

PASS

L(K_n)=J(n,2) is a canonical symmetric graph family whose n large star cliques suggest natural sphere cycles but do not ensure survival after attaching other high-dimensional faces. Simultaneous explicit simplicial retractions prove all n are primitive independent infinite-order generators for every n>=7, a structural invariant not implied by one-clique nonvanishing or mod-two table. The natural integral signed-permutation module and complete rational S_7 character provide an equivariant refinement useful for comparing topology, representations and further computations. This is a motivated all-parameter structural theorem rather than a mere finite recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
