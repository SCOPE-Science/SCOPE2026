# Endpoint-gap saturation for block reversals of equally spaced binary markers

## Finding

For every integer \(m\geq 0\), let \(w_m=1\,0^m1\,0^m1\). The block reversal of a finite word \(w\), denoted \(\operatorname{BR}(w)\), consists of all concatenations \(B_tB_{t-1}\cdots B_1\) for all decompositions \(w=B_1B_2\cdots B_t\) into nonempty consecutive blocks. Then

\[
\operatorname{BR}(w_m)=\bigl\{0^p1\,0^q1\,0^r1\,0^s:\ p,q,r,s\in\mathbb Z_{\geq0},\quad p+q+r+s=2m,\quad p\leq m,\quad s\leq m\bigr\}.
\]

In particular,
\[
\bigl|\operatorname{BR}(w_m)\bigr|=\binom{2m+3}{3}-2\binom{m+2}{3}=(m+1)^3,
\]
where \(\binom{u}{3}=0\) for \(u<3\). Thus the fraction of all binary length-\(2m+3\), weight-three words obtainable by block reversal of \(w_m\) tends to \(3/4\) as \(m\to\infty\). The defining endpoint inequalities are not merely necessary: they are sufficient.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), the word has exactly three occurrences of \(1\), the two internal zero runs have the same nonnegative length \(m\), and a block reversal reverses the *order of blocks without reversing the letters inside each block*. All decompositions use one or more nonempty contiguous blocks. Images are counted as distinct words, not with partition multiplicity. For \(m=0\), the word is \(111\) and the formula gives one image.

## Proof

**Necessity.** Any output of a block reversal begins with the final block \(B_t\), a suffix of \(w_m\). Every suffix of \(w_m\) ends in \(1\), and its initial run of zeros has length at most \(m\): the longest zero run anywhere in \(w_m\) has length \(m\). Therefore, an output's initial zero run has length at most \(m\). Similarly, the output ends with the initial block \(B_1\), a prefix of \(w_m\). Every such prefix begins in \(1\), and its terminal run of zeros has length at most \(m\). Thus the output's terminal zero run also has length at most \(m\). Block permutation preserves the number of each symbol, so every output contains three ones and \(2m\) zeros, and must have the displayed form with \(p,s\le m\).

**Sufficiency.** Fix nonnegative integers \(p,q,r,s\) with \(p+q+r+s=2m\) and \(p,s\le m\). Set \(A=m-s\) and \(B=m-p\). Then \(A,B\ge0\) and \(q+r=A+B\). Set
\[
i=\max(0,q-B),\qquad j=B+i-q.
\]
If \(q\le B\), then \(i=0\) and \(0\le j=B-q\le B\); otherwise, \(i=q-B\le A\) and \(j=0\). Hence \(0\le i\le A\), \(0\le j\le B\), and \(B-j+i=q\). Consider the consecutive pieces
\[
B_1=1\,0^s,\quad B_2=0^{A-i},\quad B_3=0^i1\,0^j,\quad B_4=0^{B-j},\quad B_5=0^p1.
\]
Their concatenation is exactly \(w_m\), since \(s+(A-i)+i=m\) and \(j+(B-j)+p=m\). The reversed block order spells
\[
B_5B_4B_3B_2B_1=0^p1\,0^{B-j+i}1\,0^{j+A-i}1\,0^s=0^p1\,0^q1\,0^r1\,0^s.
\]
If a zero-only piece is empty, omit it; the remaining pieces are nonempty and still form a valid partition. Therefore every word obeying the endpoint constraints occurs in the block-reversal set. This proves the set equality for all \(m\ge0\).

**Enumeration.** The four zero-gap lengths of a word with three ones and \(2m\) zeros sum to \(2m\); by stars and bars there are \(\binom{2m+3}{3}\) unrestricted choices. For \(m\ge1\), exactly \(\binom{m+2}{3}\) choices have \(p>m\), by replacing \(p\) with \(p-m-1\); the same number have \(s>m\). Both violations cannot occur at once because \(p+s\ge2m+2>2m\). The same formula applies when \(m=0\) using the usual zero binomial convention. Subtraction gives
\[
\binom{2m+3}{3}-2\binom{m+2}{3}
=\frac{m+1}{3}\bigl((2m+3)(2m+1)-m(m+2)\bigr)=(m+1)^3.
\]
Finally, dividing by \(\binom{2m+3}{3}\) and taking the leading coefficients yields \(3/4\). \(\square\)

## Verification

The supplied `check.py` independently enumerates every cut pattern of \(w_m\) for \(0\le m\le7\), constructs the proposed endpoint-constrained language using four gap variables, and checks equality of the two resulting sets and the cube-count identity. Execute `python3 check.py` with Python 3. No computation is required for the preceding all-\(m\) proof; the finite tests serve only as reproducibility checks.

## Relationship to prior work

Mahalingam, Maity, Pandoh, and Raghavan (2021) introduced and investigated block reversal, including global extremal sizes and equivalence of image sets. Mahalingam, Maity, and Pandoh (2023) studied which block-reversal sets consist entirely of palindromically rich words, and discussed further questions concerning the sizes of such sets. The present statement instead classifies every attainable output for the natural periodic family of three equally spaced markers and counts the resulting distinct words. An ordinary reversal or a conjugate orbit does not encode the same family of all block partitions. The output-count sequence consists of classical cubes; that numeric coincidence alone supplies neither the reachability characterization nor an implication from earlier word-combinatorics results.

## Limitations

The theorem covers only the binary family with three equally spaced ones; unequal internal zero runs, four or more ones, other block operations, and output multiplicities are not classified. The statement does not assert a global extremum over all source words of equal length or weight. The complete text of the 2021 foundational article was not available for comparison, leaving a residual risk of undiscovered or subsuming prior coverage.

## References

1. K. Mahalingam, A. Maity, P. Pandoh, and R. Raghavan, *Block reversal on finite words*, Theoretical Computer Science 894 (2021), 135–151. DOI: 10.1016/j.tcs.2021.06.046.
2. K. Mahalingam, A. Maity, and P. Pandoh, *Rich Words in the Block Reversal of a Word*, arXiv:2302.02109v1, first posted 4 February 2023; Discrete Applied Mathematics 334 (2023), 127–138. https://arxiv.org/pdf/2302.02109.
3. N. J. A. Sloane et al., *The On-Line Encyclopedia of Integer Sequences*, entry A000578 (cubic numbers). https://oeis.org/A000578. This is a numerical comparison, not a block-reversal result.
