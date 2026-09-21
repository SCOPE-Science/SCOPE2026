# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The coding problem is reduced exactly to finite set packing. There is one binary variable for each of the 625 quinary length-four words, and one capacity-one constraint for each of the 125 possible length-three deletion outputs. Feasibility is equivalent to pairwise disjoint one-deletion shadows, so the integer optimum is exactly \(N(4,5,1)\).

The verification artifact reports matching primal and dual mixed-integer bounds 42 with zero MIP gap. Independently, it checks an explicit 42-word code by constructing every distinct deletion shadow and verifying disjointness. The same implementation returns 24 for \(q=4\), matching the published even-alphabet exact value.

The upper bound is therefore a computer-assisted finite verification, not an inference from failed heuristic search.

## Originality

PASS, to the best of our knowledge.

Kim–Lee–Oh (2010) is the most directly relevant length-four source. It proves the exact formula for even alphabet sizes and explicitly says that its odd-alphabet bound is not sharp and that a sharp odd-alphabet bound appears difficult. At \(q=5\), that published bound is 45, whereas the exact integer computation here gives 42.

Wang–Ji (2005) proves existence of perfect \(T^*(3,4,v)\) codes for odd \(v\), but perfect deletion codes need not have a fixed number of codewords because deletion shadows vary in size; that existence theorem does not establish the maximum cardinality. Kulkarni–Kiyavash (2013) gives the hypergraph/ILP framework and general nonasymptotic bounds, but does not supply this exact small parameter in the inspected theorem statements and numerical discussion.

Searches covered the direct notation \(N(4,5,1)\), quinary single-deletion codes, length-four deletion/insertion metric codes, perfect deletion-code terminology, and hypergraph matching formulations.

A concrete residual uncertainty remains for Li–Houghten (2012), DOI 10.1109/CIT.2012.137. Its bibliographic metadata and abstract were inspected, while the full paper was not inspected. The abstract describes computational experiments and extensions of nonbinary Tenengolts codes, so an unindexed small-parameter observation could conceivably overlap this result. No such exact \(q=5,n=4\) statement was found in accessible metadata or searches. Originality is therefore asserted only to the best of our knowledge.

## Value

PASS.

The result closes a concrete instance of the odd-alphabet sharp-bound problem singled out in the standard length-four paper. It improves the best directly applicable classical length-four upper bound from 45 to 42 and supplies a matching explicit code. The value is an exact small-parameter determination rather than a general asymptotic improvement, but it resolves the first nontrivial quinary instance with a complete upper-and-lower certificate.

## Scientific limitations

The upper bound is computer-assisted and does not yet yield a symbolic formula for all odd alphabet sizes. The computation uses a general-purpose mixed-integer solver rather than a formally checked proof certificate. The inaccessible full text of Li–Houghten (2012) leaves a specific residual originality uncertainty. The theorem is only for the standard ordered-word single-deletion channel.
