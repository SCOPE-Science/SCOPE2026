# Independent mathematical audit

## correctness

PASS

Dilworth partitions a finite width-w poset into w nonempty chains. On a chain of length l, prefix hypotheses have dimension floor(log2(l+1)) by leaf counting and recursive bisection. In a product on disjoint domains, a query affects one factor only; a branch of a shattered query must reduce that factor's dimension by at least one, giving the upper bound by summing factor dimensions. Concatenating independent trees gives equality for the product. Every ideal is a prefix tuple, so k_i=floor(log2(l_i+1)) must sum to at least K. Minimizing the sum of 2^k_i-1 first forces sum K, then balancing by discrete strict convexity, giving the stated N_w(K). At equality all l_i=2^k_i-1 and a K-tree needs all 2^K available tuples. A cross-chain comparison would forbid one, so the disjoint union is forced. For w>=2 this excludes connected equality; adjoining a global bottom preserves the antichain and all projected old ideals. Padding above with a chain preserves width and the old tree for the fixed-size formula. An antichain is statically shattered by taking down-closures, and no comparable pair can be shattered. The frozen code and output were read, not executed; the finite enumeration and arithmetic checks are not the unrestricted proof.

## originality

PASS

The closest same-day finding treats the same query model on two-row grids, and the known chain decomposition and threshold facts cover ingredients. The supported distinct claim is the exact minimum over all width-w posets and the equality structure, which also yield the connected and fixed-size statements. No inspected source gives an equivalent or stronger extremal theorem.

## value

PASS

For the natural ideal-membership class, the theorem gives a uniform, sharp element budget for adaptive shattering at prescribed static dimension, rather than a bound or a family example. It forces all extremizers at the onset and determines exactly the extra cost of comparability connectivity. These facts also answer the fixed-size adaptive-minus-static extremum without running an instance algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
