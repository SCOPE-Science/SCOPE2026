# Independent mathematical audit

## correctness

PASS

The single prescribed pair consists of distinct labelled arcs except for the excluded constant word. Contraction to one labelled arc is reversible up to rotation, including loops and parallel arcs, and lowers just the middle outdegree from q to q−1. Thus BEST gives the tree-count ratio divided by q−1. The rank-one row-Laplacian update is (e_a−e_b)(e_b−e_c)^T; for the grounded minor one subtracts a constant from the full solution to set the root component to zero, and the difference functional is unchanged. The powers of adjacency count overlaps before m=n−1 and A^m is all-ones, so the finite geometric inverse gives (1). The zero-index coefficient is 0 exactly when one of the n-letter end blocks is constant (then one update vector is zero), −2 exactly for alternation, and −1 otherwise. For −1, the absolute residual tail is strictly less than 2/[q(q−1)], which gives a strict gap from both bounds even at q=3. For alternation the coefficients are −2,+2,…, and summation gives (q−1+2(−1/q)^m)/(q²−1); the lower endpoint occurs only at m=1 and alternation cannot attain the upper endpoint. The equality counts and union bound follow. I inspected verify.py and the frozen verification_output.txt, including the 24 ternary order-two cycles and both extremal counts; these are recorded finite corroboration, not an all-orders proof or a fresh run.

## originality

PASS

Pass is limited to the order-uniform sharp two-sided nonbinary bounds and full equality classification. The support theorem, labelled cyclic counting framework, general conditional expected counts, and the contraction/BEST count are not new. The most relevant general count machinery permits individual computations, but the inspected results do not implement or mechanically supply the order-uniform optimization over overlap patterns.

## value

PASS

The improvement from qualitative support to explicit probability bounds independent of order changes what can be guaranteed when sampling cycles to cover local windows. The equality classification distinguishes two concrete overlap mechanisms (boundary runs and the shortest alternating return) and establishes sharp constants without exhaustive enumeration. The application is marginal/union-bound only, not independence of motifs within a cycle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
