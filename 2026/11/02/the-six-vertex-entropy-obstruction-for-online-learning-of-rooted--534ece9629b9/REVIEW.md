# Independent mathematical audit

## correctness

PASS

A complete shattered depth-d binary tree requires 2^d different ideals, and the exact dimension of a nonsingleton version space is the maximum, over nonconstant queries, of one plus the smaller branch dimension. An independent census recursively formed all multisets of child shapes totaling n−1 vertices, enumerated ancestor-closed masks, and applied this recurrence. It matched the rooted shape counts 1,1,2,4,9,20; precisely ((()())(())) and ((())(())()) have entropy floor 4 but dimension 3, with 16 and 19 ideals. Replay: python /workspace/branches/594d4e60-96db-41a6-b1d4-9f4615c8acf3/independent_census.py; captured output independent_census_output.txt in the same directory. A fork has dimension 2 (include its root and freely label two leaves), and a two-vertex chain dimension 1. Root-present subfamilies of both exceptions have dimension 3 by product additivity. At size 16 no legal first query splits 8:8; at size 19 the only query with at least 8 concepts on both sides is the standalone leaf, whose positive branch is a dimension-2 product of two chains. Additivity follows by concatenating optimal trees for the lower bound and using the branch with smaller factor dimension in a first query for the upper bound. For R_s the root-present product has dimension 3s and 16^s elements; only the empty ideal omits the root, giving count 1+16^s and entropy exactly 4s for s≥1. Adding one concept raises dimension by at most one, since at the first query one branch does not contain it. Thus the connected family has the stated interval and diverging deficit, not an asserted exact dimension.

## originality

PASS

The accepted distinct content is the sharp census (including completeness at orders up to five and no other exceptions at six), the 16-ideal obstruction, and its specific connected product family. One of the two examples is already a specialization of a distinct same-day indexed theorem and is not credited as distinct on its own. Neither the inspected general directed-cut bounds nor the related exact families give the entire classification.

## value

PASS

The sharp first failure of the cardinality-based mistake bound on a natural closure family identifies two different obstructions, one purely at the first-query count level and one requiring actual branch dimension. Exhaustive exclusion of smaller or additional same-order shapes turns isolated witnesses into a useful boundary classification. The explicit connected family quantifies repeated deficit without purporting to give an exact dimension or claiming qualitative unboundedness independently of already covered examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
