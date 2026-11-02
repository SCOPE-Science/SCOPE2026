# Independent mathematical audit

## correctness

PASS

For q>=3 each q-clique fiber has at most one positive by independence. If empty, its q zero rows must receive 2-label neighbors from only the two adjacent fibers; at most two distinct rows can be defended, contradiction. Each fiber thus has exactly one positive (row c_j, type t_j), with c_j!=c_(j+1). A type-1 fiber has q-1 zero rows and no internal defender; the two adjacent fibers can cover only two other rows, forcing q=3 and type-2 neighbors in the two complementary colors. This is both necessary and sufficient. Thus for q>=4 all n positives are 2, weight 2n and optimum count is chromatic polynomial of C_n evaluated at q. For q=3, type-1 positions S form an independent subset of C_n; weight=2n-|S| and maximal |S|=floor(n/2) is realizable. For n=2k, S is one of the two alternate sets, and coloring the k type-2 positions cyclically with three colors gives 2*(2^k+2*(-1)^k), treating k=2 as two distinct colors. For n=2k+1, there are n maximum sets and the k+1 type-2 cyclic positions have 2^(k+1)+2*(-1)^(k+1) choices, treating k=1 as two differently colored vertices. The appropriate third color at each type-1 vertex is uniquely forced. n=3,4 boundaries explicitly checked. Independent full adjacency checks for ten (q,n) combinations matched all exact counts; computations corroborate, not replace, the unrestricted proof. The reviewed package has exactly seven source blobs; reconstructed source-tree SHA-1 agrees with assigned and current Git tree.

## originality

PASS

The exact infinite-family optimum-label classification and labeled minimizer counts for K_q Cartesian C_n were not deduced from the actual inspected published statements. The same-parameter 2023 paper advertises numerical values for some product graphs but complete text could not be accessed; this may preempt the scalar i_R result, not demonstrated coverage of the optimizer-count theorem. The closest Resultary public record is an enumerator on complete multipartite graphs, not the Cartesian cylindrical graph. This is a best-of-knowledge priority judgment with explicit uncertainty, not a uniqueness certificate.

## value

PASS

The Cartesian clique-by-cycle family is a canonical unbounded two-parameter product, and minimum independent Roman domination is a standard graph invariant. Exact counts of all labeled optimal defensive configurations, not merely the easily recoverable chromatic polynomial, answer a natural multiplicity/rigidity problem: a sharp q=3 threshold permits mixed labels and cyclic ternary compatibility, while q>=4 forces all 2-labels. The complete classification and parity-dependent counts are useful for comparing robust optimal designs and for testing future enumeration results. Although the counting step is elementary once the nontrivial fiber lemma is established, this is a motivated exact infinite-family classification, not an arbitrary table or parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
