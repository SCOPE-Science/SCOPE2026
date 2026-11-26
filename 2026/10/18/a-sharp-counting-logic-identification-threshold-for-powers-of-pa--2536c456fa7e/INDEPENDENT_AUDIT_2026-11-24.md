# Independent mathematical audit

## correctness

PASS

Use the standard colour-refinement/C² equivalence in the adjacency-only language, comparing against arbitrary finite simple graphs. For n≤k+1 the vertex count and full degree force the complete graph. For k≥2 and t=n−k−1∈{1,2,3}, the degree formula min(i,k)+min(n−1−i,k) gives the distinct pairs A_i={i,n−1−i} with degrees k+i, plus a universal class (which is empty at n=6,k=2). Reflection makes each pair equitable and the universal vertices have identical quotient counts. Between distinct pairs i<j, same-side distances are ≤2≤k and opposite-side distance is k+t−i−j, so the block is complete for i+j≥t and a perfect matching otherwise. The matching subgraph on classes is a forest; its arbitrary matching choices can be normalized by flips propagated along each tree, leaving internal edges and complete blocks unchanged. This reconstructs any refinement-equivalent graph. For k=1, refinement peels distance-from-nearest-end classes, a chain of pair matchings with a central singleton if odd and a central within-pair edge if even. For k≥2,n≥k+5, A_0 and A_1 are distinct exact degree pairs; A_2 is also an exact degree pair when k≥3 and otherwise consists of the degree-four neighbours of A_0, distinguished by the next round. Reflection prevents any of these pairs from splitting. Their three interclass blocks are matchings, because opposite-side distances between distinct classes are at least n−4>k. The stated switch changes just the A_0–A_2 matching while preserving every stable-class neighbour count (and hence all round colours by induction). It reduces the count of triangles meeting all three intrinsic classes from two to zero regardless of within-class edges. Thus the switched graph is nonisomorphic and witnesses the claimed first obstruction, including n=7,k=2. The two finite Python checkers were inspected, not run; the proof covers the full quantifiers and does not rely on testing a comparison corpus.

## originality

PASS

Credit the established equivalence, generic amenability characterizations, and switching mechanism. The earlier exact C²-depth result already covers ordinary paths (k=1). The supported distinct contribution is the explicit boundary n=k+5 for every k≥2 and its uniform switch witness. Extracting it from general characterizations requires a concrete stable-cell classification in the positive regime and a distinct stable matching triangle across the entire negative regime (including the extra refinement at k=2). Bounded checks did not identify this specialized threshold in another source; that does not settle publication priority.

## value

PASS

An exact boundary for identification against all graphs is useful even for this structured family: the first failure for each nontrivial power is explicit, and a two-edge switch gives a uniformly small concrete witness with an intrinsic certificate. The cutoff depends on when the end-layer quotient first supports conflicting matchings, not on an arbitrary finite scan. The already known logical equivalence and ordinary-path case do not provide this family-specific information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
