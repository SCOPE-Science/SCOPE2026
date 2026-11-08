# Independent mathematical audit

## correctness

PASS

For k>=3, admissible length-k binary target edges are exactly words with no 000/111. The directed de Bruijn graph out-minus-in imbalance at a length-(k-1) vertex is 1_{first pair equal}-1_{last pair equal}. Duplicating precisely those admissible words whose first/last adjacent pairs differ and which contain an equal pair cancels all imbalances. The admissible subgraph is strongly connected by alternating bridges, so an Euler tour gives the desired cyclic host, with only admissible cyclic factors. For *all* possible additional host factors, including forbidden ones, the potential phi(v)=-first equal-adjacency index (or -(k-1) if none) satisfies phi(head)-phi(tail)<=1. Added target arcs are tight, yielding a dual circulation lower bound of exactly |S_k| extra windows for any closed host walk. Compositions into runs of size1 or2 give |W_k|=2 F_{k+1}, |S_k|=2 F_{k-1}-2, hence optimum 2(F_{k+1}+F_{k-1})-2. Independently enumerated full de Bruijn edges at k=3..12 to check potential bound and target balance plus the exact counts. These finite tests corroborate the general Eulerian/primal-dual proof rather than replacing it.

## originality

PASS

Best-of-knowledge PASS for the specific shortest circular constrained-word covering theorem, not the Lucas sequence itself. Chee et al optimize distinct run-limited de Bruijn walks, Moreno/Matamala address exact-once cycles over periodically admissible languages, Chen et al universal cycles of removed words; none inspected directly solves cover-all finite admissible words allowing repeated factors and forbidden host windows. Known OEIS values are numerical, not the new combinatorial interpretation. Relevant Bryant/Fredricksen 1991 full text is missing, recorded as residual priority risk.

## value

PASS

Shortest indexed circular universal covering is a natural exact combinatorial invariant distinct from constrained de Bruijn sequences requiring no repetitions. The theorem gives a sharp all-length formula, constructive optimal multiplicities, and a global lower bound valid even when hosts include forbidden factors; the connection to a known Lucas sequence alone is not the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
