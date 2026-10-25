# Exact Burrows–Wheeler run spectrum of cyclic binary words with three markers

## Finding
For every integer \(n\ge4\), consider necklaces (binary words modulo rotation, but **not** reflection) of length \(n\) with exactly three symbols equal to \(1\). The sentinel-free circular Burrows–Wheeler transform (BWT) is obtained by lexicographically sorting **all \(n\)** cyclic rotations, retaining repeated rows with multiplicity, and reading the last column. Define \(r(w)\) as its number of maximal constant-letter *linear* runs. Writing \(C_j(n)\) for the number of necklaces with \(r(w)=j\), and \(\delta_n=1\) when \(3\mid n\) (otherwise \(0\)), the complete spectrum is

\[
C_2(n)=1,\qquad C_4(n)=n-4+\delta_n,
\]
\[
C_6(n)=\frac{\binom{n-1}{2}+2\delta_n}{3}-1-(n-4+\delta_n),
\]
with \(C_j(n)=0\) for every other \(j\). In particular \(C_6(n)/\sum_j C_j(n)\to1\) as \(n\to\infty\), whereas exactly one necklace is maximally clustered (two runs) at every length.

Equivalently the ordinary generating functions, indexed by total word length, are
\[
G_2(z)=\frac{z^4}{1-z},\qquad G_4(z)=\frac{z^5}{(1-z)^2}+\frac{z^6}{1-z^3},
\]
\[
G_6(z)=\frac{z^3}{3(1-z)^3}+\frac{2z^3}{3(1-z^3)}-z^3-G_2(z)-G_4(z).
\]
The familiar two-run/balanced-word characterization is background, not claimed as original; the contributions here are the complete weight-three classification and all-length distribution.

## Assumptions and scope
The binary alphabet is ordered \(0<1\). A necklace is an equivalence class under cyclic rotations only. Equal cyclic rotations appear with their natural multiplicity in the BWT matrix, so periodic necklaces are included. Runs are counted in the linear last column, not cyclically and without an added endmarker. The formulas hold for every integer \(n\ge4\), including nonprimitive necklaces.

Represent a necklace by a cyclic orbit of its three nonnegative zero-gaps \((g_0,g_1,g_2)\), with \(g_0+g_1+g_2=M=n-3\), via the circular word \(1 0^{g_0}1 0^{g_1}1 0^{g_2}\). Only cyclic permutations of gap triples are identified.

## Proof
**Rotation-order lemma.** For each index \(i\) (modulo \(3\)), and each integer \(0\le t\le g_i\), the rotation starting with the final \(t\) zeros of gap \(g_i\) is
\[
R_{i,t}=0^t1 0^{g_{i+1}}1 0^{g_{i+2}}1 0^{g_i-t}.
\]
Its preceding symbol, hence its last-column BWT entry, is \(1\) if and only if \(t=g_i\); otherwise it is \(0\). Sorted rotations are ordered first by decreasing \(t\), and at each equal \(t\) by decreasing lexicographic order of the cyclic gap continuation \((g_{i+1},g_{i+2},g_i-t)\). The statement follows by comparing the first differing zero-run before a \(1\): a longer zero-run gives the smaller binary row. Equal periodic rotations have equal predecessors, so tie-breaking cannot affect the BWT. Thus there are three marked \(1\)-entries, one for each gap, amid \(n-3\) unmarked \(0\)-entries.

Because \(M\ge1\), the first sorted row starts after a longest positive zero-gap, so the first BWT entry is \(1\). The lexicographically last row starts at the beginning of a longest cyclic run of ones, which is preceded by a zero, so the last BWT entry is \(0\). Therefore the number of linear runs equals twice the number of consecutive blocks of marked rows. It belongs to \(\{2,4,6\}\).

**Adjacency lemma.** Inspection of the equal-\(t\) groups in the rotation-order lemma gives these exhaustive possibilities for adjacent *marked* rows. Equal gap lengths yield adjacent marked rows. Distinct lengths differing by at least two cannot be adjacent because an unmarked rotation has a strictly intermediate value of \(t\). For three pairwise distinct gaps \(x<y<z\), adjacency of the small and middle marks occurs exactly when \(y=x+1\) and the cyclic triple is \((y,x,z)\); adjacency of the middle and large marks occurs exactly when \(z=y+1\) and the cyclic triple is \((y,z,x)\). Indeed, for lengths \(t,t+1\), the only possible unmarked competitors are rotations with the same leading zero length \(t\), and their next gap sorts immediately before or after the marked row according to these two displayed cyclic orders. The third marked row has a different \(t\), so no other adjacency is possible. If two gap lengths agree, their marked rows are adjacent and there are exactly two marked blocks except when the remaining gap differs from them by at most one, in which case all three marks are in a single block. If the gaps are all distinct, the displayed adjacency conditions are the only way to obtain two marked blocks; otherwise there are three.

It follows that \(r(w)=2\) exactly when \(\max g_i-\min g_i\le1\). There is one such cyclic gap triple for each \(M\). For the four-run case, first count triples having two equal gaps, but not balanced. They have the form \((a,a,b)\) with \(b\ne a\), \(|b-a|\ge2\); for fixed \(M\) their number is \(\lfloor M/2\rfloor\). Next count all-distinct triples satisfying the small-gap adjacency criterion: they are determined by \((x,x+1,z)\), where \(z\ge x+2\), \(3x+1+z=M\), and exactly one cyclic order qualifies. Their number is \(\lfloor M/3\rfloor\). The big-gap criterion similarly yields \((x,y,y+1)\), where \(0\le x<y\), \(x+2y+1=M\), and exactly one cyclic order qualifies. Its count is \(F(M-3)\), where \(F(t)=[z^t]/((1-z^2)(1-z^3))\), taken as zero for \(t<0\). Triples with consecutive three gap values contribute two distinct cyclic orders, one per criterion, so there is no double counting. Consequently
\[
\sum_{M\ge0}C_4(M+3)z^M
=\frac{z^2}{(1-z)(1-z^2)}+\frac{z^3}{(1-z)(1-z^3)}+\frac{z^3}{(1-z^2)(1-z^3)}
=\frac{z^2}{(1-z)^2}+\frac{z^3}{1-z^3}.
\]
Reading coefficients for \(M\ge1\) yields \(C_4(M+3)=M-1+\mathbf1_{3\mid M}\), namely the stated \(C_4(n)\).

Finally, cyclic rotation acts on the three-gap compositions of \(M\). Burnside's lemma gives
\[
\#\operatorname{Necklaces}(n,3)=\frac{\binom{M+2}{2}+2\mathbf1_{3\mid M}}3
=\frac{\binom{n-1}{2}+2\delta_n}{3}.
\]
Subtract the two-run and four-run counts to obtain the six-run count and its generating function. The total count is quadratic in \(n\), whereas \(C_2(n)+C_4(n)\) is linear, proving the density limit.

## Verification
The accompanying self-contained `verify.py` independently constructs all necklaces from cyclic gap compositions, sorts every rotation to calculate the BWT run count directly, and checks the adjacency classification and closed count formulas for **each length from 4 through 53**. It needs only Python's standard library and can be run with `python3 verify.py`. These finite checks are corroboration; the preceding lemmas and Burnside count establish every length.

## Relationship to prior work
Crochemore, Désarménien and Perrin (2005, arXiv:cs/0502073) describe the sentinel-free cyclic-rotation BWT and its combinatorial foundations. Mantaci, Restivo and Sciortino (2003) connect two-run BWT images to standard/Sturmian words; Simpson and Puglisi (2008) revisit this simple two-run case and generalize to ternary alphabets. Neither is the all-length two/four/six-run distribution at exactly three ones. Mantaci et al. (2017) classify binary **fixed points** of BWT with at most four minority letters, which is a different condition from classifying run counts. A separate weight-four BWT spectrum, even when known, does not imply this weight-three distribution merely by relabeling parameters. A historical unindexed equivalent enumeration remains possible.

## Limitations
The classification is restricted to exactly three ones, sentinel-free circular BWT, and rotation-only necklace equivalence. It does not assert originality of the known two-run characterization or furnish an independent audit. An earlier unindexed gap-based run count or a stronger theorem subsuming this case remains a residual priority risk; the original 2003 two-run article was accessible through bibliographic/secondary descriptions rather than a confirmed complete primary full-text inspection.

## References
1. M. Crochemore, J. Désarménien and D. Perrin, *A note on the Burrows-Wheeler transformation*, arXiv:cs/0502073, originally public 17 February 2005; Theoretical Computer Science 332 (2005), 567–572. https://arxiv.org/abs/cs/0502073
2. S. Mantaci, A. Restivo and M. Sciortino, *Burrows-Wheeler transform and Sturmian words*, Information Processing Letters 86 (2003), 241–246. https://doi.org/10.1016/S0020-0190(02)00512-4
3. J. Simpson and S. J. Puglisi, *Words with Simple Burrows-Wheeler Transforms*, Electronic Journal of Combinatorics 15 (2008), R83. https://doi.org/10.37236/807
4. S. Mantaci, A. Restivo, G. Rosone, F. Russo and M. Sciortino, *On Fixed Points of the Burrows-Wheeler Transform*, Fundamenta Informaticae 154 (2017), 277–288. https://doi.org/10.3233/FI-2017-1566
