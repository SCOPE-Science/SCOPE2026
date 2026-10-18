# A sharp three-marker transition for circular binary string attractors

## Finding
Let \(1\le a<b<c\) be integers and let the circular binary word be
\[
 w=0\,1^a\,0\,1^b\,0\,1^c.
\]
Write \(Z_0,Z_1,Z_2\) for the consecutive zeros, so \(Z_1\) lies between the runs of lengths \(a\) and \(b\), while \(Z_2\) precedes the run of length \(c\). Let \(X_j\) denote position \(j\) within the \(c\)-run, counted from \(Z_2\), for \(1\le j\le c\).

**Theorem.** The circular string attractors containing exactly two positions are precisely
\[
 \left\{\{Z_1,X_j\}:c-a\le j\le a+1\right\}.
\]
The number of such position sets is therefore \(\max\{0,2a+2-c\}\). The minimum circular attractor size is
\[
 \gamma_c^*(w)=\begin{cases}2,&c\le 2a+1,\\3,&c\ge 2a+2.\end{cases}
\]
In the second case the three-point set \(\{Z_1,X_{a+1},X_{c-a}\}\) is a circular attractor. The exact threshold is independent of the intermediate gap length \(b\). Every permutation of the three distinct gap lengths is a rotation or reflection of the displayed ordering; the result thus covers all circles with exactly three zeros separated by pairwise-distinct positive one-run lengths.

## Assumptions and scope
A circular factor of a word of length \(n\) means a nonempty contiguous factor of length at most \(n\) of one of its cyclic rotations. A circular occurrence covers the positions that its letters occupy, interpreted modulo \(n\). A circular string attractor is a set of positions meeting at least one circular occurrence of **every** circular factor. Positions are physical positions modulo \(n\), not distinct letters or positions in an arbitrary rotated representative. We use three nonempty, pairwise distinct gaps, so the normalized parameters obey \(1\le a<b<c\). No assertion is made for repeated gap lengths.

For reproducibility using zero-based indexing, \(Z_0=0\), \(Z_1=a+1\), \(Z_2=a+b+2\), and \(X_j=a+b+2+j\). The length is \(n=a+b+c+3\). The stated counts refer to distinct unordered subsets of this labeled cycle's positions, not to symmetry orbits.

## Proof
**Step 1: a lower bound and forced positions.** Every attractor must meet an occurrence of the one-letter factor \(0\) and one of \(1\), so its size is at least two, and every size-two attractor has one zero and one one. Since \(c>b\), the factor \(1^c\) occurs only in the longest run, so the one position must be \(X_j\) for some \(1\le j\le c\). The factors \(0\,1^a\,0\) and \(0\,1^b\,0\) each occur in exactly one place on the circle, because the three gap lengths are distinct. Neither factor touches the \(c\)-run. Their occurrences share exactly the zero \(Z_1\). Thus the chosen zero is forced to be \(Z_1\).

**Step 2: two necessary inequalities.** The factor \(1^{a+1}0\) can end only at \(Z_2\) or \(Z_0\): the preceding gap lengths are respectively \(b\) and \(c\), while the preceding gap at \(Z_1\) is only \(a\). These occurrences do not contain \(Z_1\). The only one containing a position of the \(c\)-run is its suffix of length \(a+1\) ending at \(Z_0\). It meets \(X_j\) only if \(j\ge c-a\).

The factor \(1^{a+1}0\,1^{a+1}\) occurs uniquely with its center at \(Z_2\): there are at least \(a+1\) ones on either side of \(Z_2\), but each other zero has the \(a\)-run on one side. That occurrence contains \(X_j\) only if \(j\le a+1\). Consequently every two-point attractor must have \(c-a\le j\le a+1\).

**Step 3: sufficiency for every position in that interval.** Fix \(c-a\le j\le a+1\), and mark \(Z_1\) and \(X_j\). The two circular arcs of unmarked positions, read clockwise, are exactly
\[
 A=1^b0\,1^{j-1},\qquad B=1^{c-j}0\,1^a.
\]
Any occurrence not crossing a marked site lies entirely in one of these arcs. A factor of pure ones occurring in either arc has length at most \(c\); it has another occurrence crossing \(X_j\) inside the longest run. Both arcs have only one zero, so every occurrence containing two or more zeros already crosses a marked site. It therefore remains only to examine factors \(1^u0\,1^v\), with \(u,v\ge0\), that lie in either unmarked arc.

If such a factor lies in \(B\), then \(u\le c-j\le a\) and \(v\le a<b\). The factor also occurs around the marked zero \(Z_1\), and is attracted. If it lies in \(A\), then \(u\le b\) and \(v\le j-1\le a\). For \(u\le a\) it occurs around \(Z_1\). For \(u\ge a+1\), it occurs around \(Z_0\), which has \(c\) ones to its left and \(a\) ones to its right. In this occurrence its first \(u\) ones are the last \(u\) positions of the \(c\)-run, and these include \(X_j\) because \(j\ge c-a\ge c-u+1\). Thus every potentially missed factor has a marked occurrence, proving sufficiency and the exact enumeration.

**Step 4: the phase with no two-point attractor.** When \(c\ge2a+2\), the interval of Step 2 is empty, so \(\gamma_c^*(w)\ge3\). Mark
\[
 T=\{Z_1,X_{a+1},X_{c-a}\}.
\]
The three unmarked arcs are, respectively, \(1^b0\,1^a\), \(1^{c-2a-2}\), and \(1^a0\,1^a\). Factors of ones have a marked occurrence in the longest run. No arc contains two zeros. For one-zero factors in the third arc, occurrence at \(Z_1\) covers them all. In the first arc, those with at most \(a\) ones on the left again occur at \(Z_1\); those with at least \(a+1\) ones on the left have an occurrence at \(Z_0\) crossing \(X_{c-a}\). The middle arc has no zero. As in Step 3, all factors are attracted. Therefore \(T\) is an attractor of size three, and the lower bound is tight. \(\square\)

## Verification
The included standalone standard-library program `check_circular_gap_triplets.py` enumerates all \(\binom{12}{3}=220\) triples \(1\le a<b<c\le12\). Independently of the proof it builds, for every distinct circular factor up to full word length, the exact union of positions crossed by its circular occurrences, and exhaustively tests all pairs. The result matches the asserted sets and formula in all \(220\) cases: \(70\) have a two-point attractor and \(150\) have minimum size three. It checks the constructive three-point witness in every latter case. For \(c\le7\), a separate direct-occurrence implementation exhaustively rechecks the two-point sets without using the factor-mask method. Run `python check_circular_gap_triplets.py 12` from a folder containing the delivered program.

## Relationship to prior work
Mantaci, Restivo, Romana, Rosone, and Sciortino introduced circular string attractors and related *consecutive-position* minimal pairs to standard Sturmian conjugacy classes. Their Theorem 34 does not give the nonconsecutive pair classification or the threshold for these three-gap circles. Romana subsequently gave a general linear-time circular-attractor verification algorithm and NP-completeness results; these do not state the present parameter-uniform closed forms. The theorem is a direct special-family structural result, rather than a faster general decision procedure. Analogues for ordinary, noncircular attractors do not imply it because wraparound factors change the coverage relation. Searches of mathematical research records and the accessible relevant literature did not identify an equivalent three-gap formula; absence of a hit does not prove uniqueness.

## Limitations
The claim is restricted to three positive pairwise-distinct one-run lengths with exactly three zero markers. Tied gap lengths can create additional minimum pairs and are explicitly outside scope. The proof is elementary and complete within the stated assumptions, but originality has not been independently audited; a stronger or equivalent unindexed source is possible. No claim about approximation complexity or longer words with more zero markers is made. The finite checker supports reproducibility but is not the basis of the infinite proof.

## References
1. S. Mantaci, A. Restivo, G. Romana, G. Rosone, M. Sciortino, *A combinatorial view on string attractors*, Theoretical Computer Science 850 (2021), 236–248, DOI 10.1016/j.tcs.2020.11.006. Author-postprint: https://pages.di.unipi.it/rosone/Papers/MRRRS_TCS2021.pdf .
2. G. Romana, *Algorithmic View on Circular String Attractors*, ICTCS 2023, CEUR Workshop Proceedings, pp. 169–180. https://ceur-ws.org/Vol-3587/9885.pdf .
