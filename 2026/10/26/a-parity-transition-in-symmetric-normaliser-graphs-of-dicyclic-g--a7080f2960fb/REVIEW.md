# Independent mathematical audit

## correctness

PASS

Write s_j=a^j b, so s_j^2=a^m and s_j^(-1)=s_(j+m). Conjugation by a^i sends s_j to s_(j+2i); conjugation by s_k sends it to s_(2k-j), while s_k inverts every rotation. Membership of these conjugates in the order-four cyclic subgroup is equivalent to displacement 0 or m modulo 2m, and the condition is symmetric since both displacements are self-negative. Thus the universal rotations and each outside clique have the stated sizes 2 for odd m and 4 for even m, with no other cross edges. The nonuniversal rotation clique is nonempty for m>=3; at m=2 all eight vertices are universal. For a join of K_u with a union of cliques, internal zero-sum vectors have eigenvalue u+clique size, differences of component constants have eigenvalue u, and the universal differences and join contrast have eigenvalue 4m. This gives all multiplicities including the collision at m=4. The product of nonzero eigenvalues divided by 4m gives both tree counts; coloring is u plus the largest remaining clique size and independence is the number of remaining cliques. `python3 /workspace/reproduce.py` independently checked adjacency with monomial-matrix group elements and spectra via the first 4m exact Laplacian traces for m=2..7, not as a substitute for the proof.

## originality

PASS

Pass concerns the even-m>=4 structure, with spectrum and tree formula as consequences, exactly the scope of the frozen originality claim. The odd branch and the Q8 observation are existing coverage and receive no separate novelty credit. Bounded searches and the primary theorem comparisons did not establish coverage of the even decomposition.

## value

PASS

The even case is a complete classification for a natural group family under the actual mutual-normaliser predicate. It identifies exactly what changes at parity, including universal vertices and the outside components; knowing only that the graph differs from the commuting graph does not provide this information. Exact spectra and labelled trees are useful consequences of that structural fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
