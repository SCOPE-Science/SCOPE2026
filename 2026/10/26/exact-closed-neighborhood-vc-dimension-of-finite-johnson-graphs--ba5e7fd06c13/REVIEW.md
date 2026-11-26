# Independent mathematical audit

## correctness

PASS

A full trace puts the sample in N[C]. Encode its other vertices as unique swaps (removed row, added column). Relative to C, a center at distance 0 gives the full trace; one swap gives the union of its row and column and includes C; two swaps give the product of the selected row and column pairs and omit C; greater distance gives an empty trace by the triangle inequality. Verified the bound with an independent exhaustive enumeration over all samples of five cells in a 5x5 grid and four cells in a 4x4 grid with C included. Every pattern can be relabeled into these grids; the code permits arbitrary unoccupied coordinates in determining traces and thus can only enlarge the real trace family. It yielded maxima 24 over 53,130 samples and 25 over 1,820 samples, both below 32. Independently enumerating traces by symmetric difference in the seven base graphs returned 1,2,3,3,4,3,4 for J(4,2), J(5,2), J(6,2), J(7,2), J(8,2), J(6,3), J(7,3), and exact open dimension 4 in both J(7,2) and J(6,3). A parameter increase can preserve all witnesses by adjoining common elements to every vertex and leaving other new elements unused, so both equality and Johnson distance are preserved. This transfers the two size-four lower witnesses to all larger required parameters, up to complementation. Rank one is complete, and the optional k=0,n cases have one vertex; identical closed neighborhoods give dimension zero.

## originality

PASS

The supported distinct content is the sharp closed-neighborhood upper bound uniformly in both Johnson parameters and its use in the complete dimension table. An exact open-neighborhood theorem and boundedness of the closed variant are prior. The k=2 branch is expressly not claimed new, and later catalogue records give exact, in parts stronger, coverage of the k=2 and k=3 branches. No inspected source gives an all-rank closed upper bound of four or a result implying it; the fixed slices do not control larger min(k,n-k).

## value

PASS

The uniform sharp dimension bound and complete finite classification are natural invariants of a standard graph family. They quantify exactly when taking closed instead of open neighborhoods changes shattering, and the finite trace kernel removes any dependence of the proof on the ambient Johnson parameters. Neither a low-rank regression nor a mildly improved algorithm on a few graphs would establish this structural result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
