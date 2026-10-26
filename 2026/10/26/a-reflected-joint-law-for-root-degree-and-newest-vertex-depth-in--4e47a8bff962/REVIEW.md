# Scientific review

## Correctness — PASS

The increasing-tree decomposition gives the formal leaf enumerator differential equation \(T'=v-1+e^T\), its reciprocal substitution \(T(vz;v^{-1})=T(z;v)+(1-v)z\), and two independently derived bivariate generating functions: root-degree marking through the unordered root-forest decomposition and newest-vertex-depth marking through the unique branch containing the maximum label. Exact coefficient extraction establishes the full law for every integer \(n\ge2\), with \(n=1\) excluded explicitly. The covariance is derived from a conditional recursion rather than inferred only from experiments. Exhaustive integer counts, polynomial recurrences, and exact fractional moments were checked with the enclosed `verify.py` and `checks.txt`.

## Originality — PASS, with historical-priority risk

The accessible full primary manuscript by Leckey–Neininger (arXiv:1202.2439, 2012) treats depth and leaves separately; its Theorems 2.1 and 2.5 do not state the reflected bivariate law. The older Carlitz–Scoville generalized Eulerian polynomial framework is broader on permutation-record/descent enumerators, but no inspected statement directly links newest insertion depth and the reflected leaf count. A published root-degree/leaf covariance identity gives a covered corollary, not the reflected joint law. The older Carlitz–Scoville full article could not be retrieved for material comparison, so equivalent formulations via classical permutation bijections remain a substantive historical-priority risk. Failure to locate a matching statement is not treated as uniqueness proof.

## Mathematical value — PASS

The result identifies an exact finite-distribution symmetry between a local branching statistic and the depth of the newest arrival, **conditional on every attainable leaf count**, a much stronger assertion than equal marginals or a covariance. Its coefficient identity transfers all mixed moments and conditional laws across the two views. The weighted-root boundary shows the symmetry depends on uniform attachment, rather than extending mechanically to a larger class. The result is a structural classification of two natural growth-tree observables, not an isolated low-order calculation.

## Limitations

The result is restricted to unordered uniform recursive trees. It does not give a coupling of both pairs within the same tree, a samplewise equality, or a weighted-root generalization. Priority uncertainty persists for early Eulerian–Stirling bijections and inaccessible older surveys.

Self-review: passed. Independent audit: not yet performed.
