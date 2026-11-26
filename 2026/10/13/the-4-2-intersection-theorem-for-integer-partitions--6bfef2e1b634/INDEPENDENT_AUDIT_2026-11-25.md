# Independent mathematical audit

## correctness

PASS

Two fixed parts of sum s leave floor((n-s)/2) unordered completions when n-s>=2. For n>=30 the largest size exceeds 13, and sums 2 and (only at odd n) 3 are the sole maximal centers. The canonical occurrence labels encode multiset intersections, and a triple of labels can occur in at most one partition because it forces the remaining part. Thus distinct compatible partitions meet in exactly two labels. For a nontrivial family choose such a pair with common labels I and disjoint remainders A,B of size two, and a third member not containing I. Members containing I must pick at least one external label from this third member (at most four triple completions); members containing one label of I must pick one each from A and B (at most eight); those avoiding I must equal A union B (at most one). This proves the uniform cap and forces full stars at n>=30. I inspected both supplied graph searches and outputs, without running the uploaded code. The independent interval-cut/submultiset implementation /workspace/branches/partition_fixed_check.py was actually run: target clique exists and target+1 does not for each n=4..29, using only induced minimum-degree pruning and exhaustive include/exclude branching. It reproduced all 26 exact maxima, including 4 on the six vertices at n=9. The bounded run does not certify other k,t or classify small-order extremizers.

## originality

PASS

Credit the prior n=9 lower-bound example, small-order theorem, eventual optimality, tied odd-order star, and general nontrivial-family bound. The supported increment is the exact all-order fixed-(4,2) solution and explicit large-order classification, in particular the finite gap not decided by those results. No distinct indexed or published source inspected closes that gap.

## value

PASS

This resolves a natural fixed-parameter case of a concrete prior conjecture, separating the actual exceptional maximum from merely a counterexample and connecting exhaustive small orders to an explicit finite structural cutoff. It is not a sampled list of arbitrary partition numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
