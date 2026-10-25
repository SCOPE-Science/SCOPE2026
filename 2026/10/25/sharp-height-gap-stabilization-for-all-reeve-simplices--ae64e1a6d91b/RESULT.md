# Sharp height-gap stabilization for all Reeve simplices

## Finding
For each integer dimension \(d\ge3\) and height parameter \(m\ge2\), the arithmetic range of the height coordinate on every integer dilation of the Reeve simplex has an explicit residue-by-residue formula. Its missing heights become an exactly translated, dilation-independent finite set at a sharp threshold, and their number has a closed expression involving a greatest common divisor.

Write \(k=d-2\), and let \(f_s=\lfloor ks/m\rfloor\) for \(1\le s<m\). The exact arithmetic range at dilation \(n\ge0\) is
\[
H_n=\{mq:0\le q\le n\}\,\cup\!\bigcup_{s=1}^{m-1}\{mq+s:0\le q\le n-d+1+f_s\}.
\]
A set with upper bound less than zero is empty. Define
\[
n_0=d-1-\left\lfloor\frac{d-2}{m}\right\rfloor,\qquad
E_{d,m}=\bigcup_{s=1}^{m-1}\{mj-s:1\le j\le d-2-f_s\}.
\]
For every integer \(n\ge n_0\), the missing heights are exactly
\[
([0,mn]\cap\mathbb Z)\setminus H_n=\{mn-\ell:\ell\in E_{d,m}\}.
\]
Their number is the positive integer
\[
G_{d,m}=|E_{d,m}|=\frac{(d-1)(m-1)-\gcd(d-2,m)+1}{2},
\]
so the *height-direction* arithmetic width (cardinality of the range) is \(mn+1-G_{d,m}\). All residue classes modulo \(m\) appear in \(H_n\) precisely from dilation \(n_0\) onward: height \(1\) is missing at \(n=n_0-1\), present at \(n=n_0\), and the other residues have no larger first-appearance threshold. The gap window is entirely at the upper end; the maximal deficit is \(m(n_0-1)-1\), so all heights from \(0\) through \(mn-m(n_0-1)\) occur when \(n\ge n_0\).

## Assumptions and scope
Let \(e_1,\ldots,e_d\) be the standard integer basis. Set
\[
R_{d,m}=\operatorname{conv}\left\{0,e_1,\ldots,e_{d-1},\sum_{i=1}^{d-1}e_i+me_d\right\}\subset\mathbb R^d,
\]
with integer \(d\ge3\), \(m\ge2\), and integer dilations \(n\ge0\). Define \(H_n=\{x_d:x\in nR_{d,m}\cap\mathbb Z^d\}\). The arithmetic width of this range means \(|H_n|\); no minimization over lattice directions is claimed. Both endpoints \(0\) and \(mn\) occur at every positive dilation. The convention \(n=0\) gives \(H_0=\{0\}\).

## Proof
Write a point of \(nR_{d,m}\) as \((x_1,\ldots,x_{d-1},z)\). Its barycentric coefficient at the apex is \(z/m\), and the coefficients at the other nonzero vertices are \(x_i-z/m\). Nonnegativity of these and of the coefficient at the origin is equivalent to
\[
0\le z\le mn,\qquad x_i\ge z/m\ (1\le i\le d-1),\qquad \sum_{i=1}^{d-1}x_i\le n+(d-2)z/m.
\]
For integer \(z\), an integral horizontal section is nonempty if and only if
\[
(d-1)\left\lceil z/m\right\rceil\le n+(d-2)z/m. \tag{1}
\]
Necessity follows from the individual lower bounds. For sufficiency choose every \(x_i=\lceil z/m\rceil\); this also proves that no other arithmetic restriction is hidden in (1).

For \(z=mq\), inequality (1) says \(q\le n\). For \(z=mq+s\) with \(1\le s<m\), it says
\[
(d-1)(q+1)\le n+(d-2)(q+s/m),\quad\text{or}\quad q\le n-d+1+\left\lfloor (d-2)s/m\right\rfloor.
\]
All \(q\) here are nonnegative. This establishes the full formula for every \(n\ge0\), including empty residue blocks.

A nonzero residue \(s\) first occurs (with \(q=0\)) at \(n=d-1-f_s\). Since \(f_s\) is nondecreasing in \(s\), the largest of these thresholds is \(n_0=d-1-f_1\), and \(1\) witnesses sharpness. The same formula shows \(n_0\ge2\).

At any \(n\ge n_0\), the residue \(s\) appears for \(0\le q\le n-d+1+f_s\) and may lie in the total interval \([0,mn]\) only for \(q\le n-1\). Its missing values are therefore indexed by \(n-d+2+f_s\le q\le n-1\); putting \(j=n-q\) gives precisely \(mj-s\) for \(1\le j\le d-2-f_s\). Different residues give disjoint deficit sets. The largest deficit is attained for \(s=1\), \(j=d-2-f_1=n_0-1\), proving the contiguous initial block assertion.

Finally, put \(k=d-2\), \(g=\gcd(k,m)\), and write \(ks=m f_s+r_s\), \(0\le r_s<m\). As \(s\) runs from \(1\) to \(m-1\), the nonzero residues among the \(r_s\) are the nonzero multiples of \(g\), each repeated \(g\) times, and the zero residue occurs \(g-1\) times. Hence
\[
\sum_{s=1}^{m-1}r_s=\frac{m(m-g)}2,
\qquad \sum_{s=1}^{m-1} f_s=\frac{(k-1)(m-1)+g-1}2.
\]
The deficit cardinality is \(\sum_{s=1}^{m-1}(k-f_s)\), which simplifies to the asserted formula for \(G_{d,m}\). Subtracting from the total \(mn+1\) possible heights gives the width identity. Every argument is exact for the full stated parameter range.

## Verification
The accompanying standalone `check.py` enumerates integer points directly from the facet inequalities for \(75\) small parameter triples, and independently compares the predicted gap translates and cardinalities for \(276\) parameter pairs at four post-threshold dilations apiece. It checks the sharp missing-to-present transition of height \(1\). The checker returns `REEVE_RANGE_OK`. Such finite tests corroborate the proof; the proof itself covers all integer parameters.

## Relationship to prior work
Haase, Nill, and Paffenholz give this precise simplex family in equation (1.1) of their lattice-polytope lecture notes and prove its classical empty-simplex property; their discussion does not derive the projected-height range across all dilations. De Loera, Marsters, and O'Neill define arithmetic width and prove eventual near-arithmetic-progression structure, endpoint-gap stabilization, and eventual quasilinearity for broad convex-body and rational-polytope classes. Those qualitative general theorems neither specify the sharp threshold nor compute the individual missing heights and their gcd-dependent count for the Reeve family. The present result supplies an explicit benchmark for that fixed-direction theory. The direction-minimized arithmetic width and directions other than the apex-height functional are not analyzed.

## Limitations
This is an exact result for one canonical integer family and one specified coordinate projection. The finite checker does not independently certify the infinite quantification. The word 'first' concerns the threshold at which all residue classes are represented, not an assertion about the earliest possible translation identity under an alternative definition of stabilization. Older sources devoted to height semigroups or Reeve dilations might contain equivalent formulas; historical priority remains a limitation pending a broader comparison.

## References
1. J. A. De Loera, B. Marsters, and C. O'Neill, *An arithmetic measure of width for convex bodies*, arXiv:2509.04726v1 (first public version September 5, 2025), especially Main Theorems 1–2, Theorem 3.3, and Section 4.1. https://arxiv.org/abs/2509.04726
2. C. Haase, B. Nill, and A. Paffenholz, *Lecture Notes on Lattice Polytopes*, draft October 7, 2020, Section 1.2, equation (1.1), and Section 4.6. https://www2.mathematik.tu-darmstadt.de/~paffenholz/daten/preprints/20201007_Lattice_Polytopes.pdf
