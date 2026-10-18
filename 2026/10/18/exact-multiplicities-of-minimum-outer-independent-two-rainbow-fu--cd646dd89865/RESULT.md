# Exact multiplicities of minimum outer-independent two-rainbow functions on rook graphs

## Finding

Let \(2\le m\le n\) be integers and let \(R_{m,n}=K_m\square K_n\), with labeled vertex set \([m]\times[n]\). Let an **outer-independent two-rainbow dominating function** be a map \(f:V(R_{m,n})\to\{\varnothing,\{1\},\{2\},\{1,2\}\}\) such that (i) the vertices carrying \(\varnothing\) form an independent set and (ii) every vertex carrying \(\varnothing\) has both colors among the labels of its open neighbors. Its weight is \(w(f)=\sum_v |f(v)|\). Colors 1 and 2 are named and distinct.

The minimum weight is \(mn-m\). Write \(N_{m,n}\) for the **number of distinct functions of that minimum weight**, with the rows, columns, and two colors all labeled. Then

\[
\boxed{N_{m,n}=\frac{n!}{(n-m)!}\left[2^{mn-m}+\sum_{k=1}^{m}(-1)^k\binom{m}{k}\,2^{mn-m-k(m+n-k-1)+1}\right].}
\]

More precisely, every minimum function has exactly \(m\) empty labels, forming the graph of an injection from the \(m\) rows to the \(n\) columns, and every other label is exactly one of \(\{1\},\{2\}\). For each fixed injection, the expression in square brackets counts exactly the feasible singleton-color assignments. The scalar minimum is included to identify the solutions being counted; the new claim concerns the complete classification and exact labeled multiplicity of its minimizers.

For example, \(N_{2,2}=4\), \(N_{2,3}=60\), \(N_{3,3}=264\), and \(N_{4,4}=87024\). For a fixed positive integer \(m\ge2\), the proportion of singleton-color assignments for a fixed maximum empty-label placement that are feasible is

\[
1-m2^{-(n+m-3)}+O_m(2^{-2n})\qquad(n\to\infty).
\]

## Assumptions and scope

Graphs are finite, undirected, and simple. Cartesian adjacency means two distinct cells are adjacent exactly when they share a row or a column. A label \(\{1,2\}\) contributes weight two; an empty label contributes zero. The enumerator counts functions, not color-swap or graph-automorphism orbits. The domain is every pair of integers \(2\le m\le n\); the case \(m>n\) follows by swapping coordinates. No claim is made for higher-dimensional Hamming graphs, arbitrary Cartesian factors, or outer-independent total variants.

## Proof

**Step 1 (sharp minimum and its rigid equality case).** Every independent set in the rook graph is a set of cells with pairwise distinct rows and columns, hence has at most \(m\) cells. Writing \(Z=\{v:f(v)=\varnothing\}\) and \(D=\{v:f(v)=\{1,2\}\}\) gives the exact weight identity

\[
w(f)=mn-|Z|+|D|\ge mn-m.
\]

For sharpness, make \((i,i)\) empty for \(i\in[m]\), label \((i,j)\) by \(\{1\}\) for \(j>i\), and by \(\{2\}\) for \(j<i\). Each empty cell \((i,i)\) sees \((i,j)\) and \((j,i)\), for any \(j\in[m]\setminus\{i\}\); these have opposite singleton colors. This is feasible for every \(m\ge2\). Thus the minimum is \(mn-m\). Equality in the displayed weight identity forces \(|Z|=m\) and \(|D|=0\), and conversely these conditions together with the rainbow rule characterize the minimizers.

**Step 2 (normalize and count empty-cell placements).** A maximum independent set has exactly one vertex in each row and lies in \(m\) different columns. There are

\[n(n-1)\cdots(n-m+1)=\frac{n!}{(n-m)!}\]

such placements. Independent permutations of the row and column indices act transitively on them, so it suffices to count singleton-color assignments for the canonical holes \(Z_0=\{(i,i):i\in[m]\}\). There are \(B=mn-m\) nonhole cells and \(2^B\) unconstrained assignments.

**Step 3 (exact overlapping failure events).** For each \(i\in[m]\), let \(E_i\) be the event that all nonhole cells in row \(i\) or column \(i\) share one singleton color. Since all those cells are neighbors of the empty cell \((i,i)\), \(E_i\) is exactly failure of the two-rainbow requirement there. The neighborhood is nonempty and has \(m+n-2\) cells.

Fix a nonempty index set \(J\subseteq[m]\) with \(|J|=k\). The union of the neighborhoods indexed by \(J\) comprises \(k(n-1)\) cells in its selected rows and \(k(m-k)\) additional cells in the other rows and selected columns. Thus its size is

\[u_k=k(m+n-k-1).\]

For distinct \(i,j\in J\), the two neighborhoods overlap at both \((i,j)\) and \((j,i)\). Consequently, imposing all events \(E_i\) for \(i\in J\) forces the **same** monochromatic color on their whole union (also valid trivially when \(k=1\)). There are exactly two choices for that color, and the \(B-u_k\) other cells are free. Therefore

\[\left|\bigcap_{i\in J}E_i\right|=2^{B-u_k+1}.\]

Inclusion-exclusion over \(E_1,\ldots,E_m\), grouped by \(k=|J|\), gives precisely the bracketed expression in the theorem. Multiplying by the number of empty-cell injections finishes the finite exact enumeration for all \(m,n\).

**Step 4 (asymptotic statement).** Divide the bracket by \(2^B\). The \(k=1\) correction is \(-m2^{1-(m+n-2)}=-m2^{-(n+m-3)}\). For fixed \(m\), every term with \(k\ge2\) has exponent at most \(1-2(n+m-3)\) for sufficiently large \(n\). Their finite sum is \(O_m(2^{-2n})\), proving the stated asymptotic. The cases \(m=2,n=2\) and all other boundaries are already covered by the exact formula, without asymptotic assumptions.

## Verification

The standalone file `verify.py` computes the formula using exact integers and independently enumerates all singleton-color assignments for each maximum nonattacking empty-cell placement for nine parameter pairs: \((2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(4,4)\). It separately enumerates every four-label function for \((2,2),(2,3),(3,3)\) to verify not just the counting but also the attained minimum. Run `python3 verify.py`. The recorded output appears in `verification_output.txt`.

These checks test finite instances only; the proof of the theorem for unbounded parameters is the four-step argument above.

## Relationship to prior work

Mansouri and Mojdeh (2020) established foundational bounds for outer-independent two-rainbow domination. Samadi and Soltankhah's 2022 preprint (published in 2023) treated product graphs and established scalar bounds; in particular their Cartesian-product analysis supplies a previously known minimum of \(m(n-1)\) for \(P_m\square K_n\) in a stated range. The scalar value for \(K_m\square K_n\) is accordingly **not** claimed as the original contribution. The present finding instead counts **all** optimal labeled functions for every rectangular rook graph, including the correlations between the color requirements at different empty cells. The known product bounds and related rainbow-enumerator work on complete multipartite graphs do not provide this matching-neighborhood multiplicity formula.

## Limitations

The novelty comparison covers searched mathematical research records and accessible primary papers, not all unpublished or unindexed literature. No independent scientific audit has been conducted. The theorem does not enumerate nonminimum functions or arbitrary graph products. The computational checks are finite, while the proof covers all stated parameters.

## References

1. Z. Mansouri and D. A. Mojdeh, *Outer independent rainbow dominating functions in graphs*, Opuscula Mathematica **40** (2020), 599–615, DOI: 10.7494/OpMath.2020.40.5.599.
2. B. Samadi and N. Soltankhah, *Further results on outer independent 2-rainbow dominating functions of graphs*, arXiv:2208.02340 (first posted 2022-08-03); RAIRO - Operations Research (2023), DOI: 10.1051/ro/2023097.
3. A. Cabrera-Martínez, *A Note on Outer-Independent 2-Rainbow Domination in Graphs*, Mathematics **10** (2022), 2287, DOI: 10.3390/math10132287.
