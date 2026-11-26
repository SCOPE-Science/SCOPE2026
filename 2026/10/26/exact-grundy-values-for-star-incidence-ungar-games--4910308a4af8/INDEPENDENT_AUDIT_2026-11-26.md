# Independent mathematical audit

## correctness

PASS

The moves in F remove i chain tops and j original singletons, leaving (a−i,b+i−j) with decreased weight 2a+b. At a≤T_b, no successor can have the current weight as nimber. Deleting a fixed singleton alone or with any move from (a,b−1) supplies the initial interval through F(a,b−1). If T_{b−1}<a≤T_b, that last value is a−1; the all-chain-top moves supply a through a+b, and extra-singleton-free moves on i chain tops stay in the high branch and give 2a+b−i. The cases a=0 and b=0 are consistent (for b=0 no positive a is in the high branch). In the low branch, write the proposed nimber T_b+r. High-branch options have weight ≥a>T_b+r. For low-branch options, larger b' gives a higher triangular band, smaller b' a lower band, and equal b'=b forces 1≤i=j≤b so the residue changes. For every b'<b, the moves j=i+b−b' for 0≤i≤b' have a−i>T_{b'} and sweep the entire lower band; the moves i=j=1,…,r reach the missing part of the current band and stay low. Thus the claimed mex is exact. For H, omitting the centre leaves H(a−i,b+i); removing it leaves F(a−i,b+i), with no newly exposed edge deleted in that same move. For b≥1 these classes fill 0,…,a−1 and exclude a, including the base a=0. For a=n,b=0 the F high branch condition is n−i≤T_i, equivalently n<T_{i+1}, so precisely i≥κ(n) fill n through 2n−κ(n). This also verifies the triangular breakpoints where n=T_k. The original labelled star is H(n,0) in the edges-below-vertices convention. The finite replay path is the standard-library verify.py (compressed recurrence plus separately represented labelled posets); it was inspected, not executed, and the infinite claim follows from the induction.

## originality

PASS

The checked outcome and small-heap theorems cover meaningful parts, but do not determine the arbitrary-size exact star and two-parameter residual nimbers. The strongest same-object Resultary match computes classical rowmotion periods for the dual order, not game nimbers. Pass is limited to the full exact nimbers in the stated orientation and unrestricted residual parameters, not the already-known win/loss or small-heap slices.

## value

PASS

A star is a natural first test of this incidence-poset game: the centre couples otherwise separable edge–leaf pairs, and deciding the winner loses almost all the information in the initial positions. The triangular breakpoint gives the exact invariant uniformly in the number of leaves without expanding the game tree. The auxiliary result also gives a reusable high-branch/periodic classification for a natural infinite restricted slow-Nim family. These values are not a recomputation of the known outcome theorem or an unmotivated finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
