# Independent mathematical audit

## correctness

PASS

Starting from g=P_w U, six forbidden Hessenberg entries (4,1),(5,1),(6,1),(5,2),(6,2),(6,3) define codimension 6 in the 15-dimensional chart. On six-dimensional Schubert cell, J has eight possibly nonzero columns. The source RESULT.md displays complete 6x8 restricted Jacobian. Independent symbolic 28 maximal-column-subset calculation from that displayed matrix found exactly seven nonzero determinants, all divisible by Δ=z12-z23-z45+z56, including ±Δ; separate five-by-five minor is identically 1. Thus rank 6 iff Δ != 0 and rank 5 on Δ=0. Compared source Abe–Insko actual Example 4.10 chart and displayed open smooth subset; confirms conventions. The independent check was on displayed J; original bundled verify.py reconstructs the defining equations but was inspected, not executed.

## originality

PASS

Abe–Insko Example 4.10 presents the same Δ and proves that Δ!=0 is a dense open smooth subset. Although its lead-in prose says all remaining points are smooth, the displayed calculation concludes only generic smoothness. The exact vanishing of every maximal minor on Δ=0 and constant five-minor proves a strictly stronger exact singular intersection, resolving the ambiguity instead of merely copying the open set. Horiguchi–Shirato has special h_m, not this h or w.

## value

PASS

Determining the entire singular hyperplane inside a named natural Hessenberg–Schubert cell is a geometric classification: it refines generic smoothness to an exact codimension-one singular subset and identifies a non-permutation singular family. The precise locus is useful for further local singularity questions without claiming a global classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
