# The unique twenty-individual double reversal among three Hill diversity orders at fixed richness

## Finding

For two positive-integer species-abundance profiles with equal census size \(N\) and equal richness, there is no pair for which Shannon-effective diversity at order one and Berger–Parker-effective diversity at order infinity rank community \(B\) above \(A\), while inverse Simpson diversity at order two ranks \(A\) above \(B\), until \(N=20\). At that first census, there is precisely **one** unordered pair of abundance profiles, modulo permutations of species:

\[
 A=(1,4,6,9),\qquad B=(2,2,8,8).
\]

Their strict order comparisons are

\[
 D_1(A)<D_1(B),\qquad D_2(A)>D_2(B),\qquad D_\infty(A)<D_\infty(B).
\]

This yields at least two distinct intersections of the two continuous Hill-diversity profiles at finite orders greater than one. It gives a richness-controlled example in which a single intermediate diversity measure reverses two agreeing larger-scale diversity rankings. The claimed minimum and uniqueness refer only to the displayed strict pattern at orders one, two, and infinity and to integer census profiles.

## Assumptions and scope

An abundance profile is a finite tuple \(a=(a_1,\ldots,a_s)\) with all \(a_i\in\mathbb Z_{>0}\), richness \(s\ge1\), and total \(N=\sum_i a_i\). Species labels do not affect any of the indices, so profiles are identified up to permutation. Put \(p_i=a_i/N\). For all real \(q>0\), set

\[
D_q(a)=\begin{cases}
\exp(-\sum_i p_i\log p_i),&q=1,\\
(\sum_i p_i^q)^{1/(1-q)},&q\ne1,
\end{cases}
\quad D_\infty(a)=1/\max_i p_i.
\]

The comparison is restricted to two profiles with exactly the same \(N\) and \(s\); no sampling uncertainty or phylogenetic structure is modeled. The finite completeness claim concerns all integer totals \(1\le N\le20\), all admissible richness values, and unordered pairs of distinct profiles.

## Proof

**Integer comparison reduction.** Define the squared-abundance sum \(S(a)=\sum_i a_i^2\), weighted abundance product \(P(a)=\prod_i a_i^{a_i}\), and maximum \(M(a)=\max_i a_i\). For equal totals \(N\),

\[
D_2(a)=N^2/S(a),\qquad D_\infty(a)=N/M(a),
\]

and logarithmic expansion gives

\[
\log D_1(a)=\log N-\frac1N\log P(a).
\]

Hence the specified strict ranking of \(A\) versus \(B\) is **equivalent**, with no approximation, to the three simultaneous integer inequalities

\[
S(A)<S(B),\qquad P(A)>P(B),\qquad M(A)>M(B).
\]

**Exact witness.** Direct integer evaluation for \(A=(1,4,6,9)\) and \(B=(2,2,8,8)\) gives

\[
\begin{aligned}
S(A)&=134,&S(B)&=136,\\
P(A)&=4627325525704704,&P(B)&=4503599627370496,\\
M(A)&=9,&M(B)&=8.
\end{aligned}
\]

In particular, \(D_2(A)=200/67>50/17=D_2(B)\), whereas \(D_\infty(A)=20/9<5/2=D_\infty(B)\). The weighted product inequality establishes \(D_1(A)<D_1(B)\) exactly.

**Exhaustive integer certificate for minimality and uniqueness.** The companion executable file `verify_hill20.py` enumerates every nonincreasing partition of each \(N\) from one through twenty. The recursive generator is complete: the first part may be any integer between one and \(N\), and the residual partition has parts no larger than that first part. This gives every positive integer multiset exactly once. A separate unlimited-coin dynamic program computes the classical partition counts at each census, independently checking the enumerator's counts; uniqueness of yielded tuples and conservation of totals are also asserted.

For each \(N\), the program groups the complete list by length \(s\), visits every unordered pair of *different* same-length profiles, tests **both orientations**, and evaluates \(S,P,M\) using only arbitrary-precision integers. The program visits exactly **49,958** unordered pairs across \(1\le N\le20\). It finds no qualifying pair when \(N<20\) and finds exactly one qualifying orientation when \(N=20\): the witness above. As the list is complete and every comparison is integer-exact, this establishes the stated finite no-go and boundary uniqueness. This is a finite exhaustive proof, not a claim that sampled numerical experiments prove a general unbounded statement.

**Two profile crossings.** Hill diversities are continuous in the order \(q>0\), including at \(q=1\), and converge to \(D_\infty\) as \(q\to\infty\). The strict negative, positive, negative signs of \(D_q(A)-D_q(B)\) at \(q=1,2,\infty\), respectively, force at least one zero in \(1<q<2\) and another at a finite \(q>2\). No uniqueness of those crossings is claimed.

## Verification

Run `python3 verify_hill20.py` with Python 3 and no third-party dependencies. The code verifies every recursion output against independent integer-partition counts, every relevant pair and orientation, and the exact witness products and inequalities. A complete reproduction prints the following core conclusions: **49,958** candidate pairs, zero reversals below twenty, and one unique qualifying ordered pair at twenty. A separate preliminary partition generator with parts in ascending order reproduced the same minimum and witness; the packaged checker is the standalone authoritative executable certificate.

## Relationship to prior work

Hill (1973) unified richness, Shannon entropy, and Simpson diversity into an order-indexed effective-species framework. Tóthmérész (1995) studied non-comparability of diversity-ordering methods and small artificial ecological profiles. Jost (2006) clarified conversion of entropies to effective diversity. Liu, Whittaker, Ma, and Malcolm (published online in 2006) analyzed equivalent and non-equivalent diversity-ordering methods and compared community profiles; their publicly available complete manuscript was examined, including definitions, examples, empirical tables and conclusions. None of the inspected materials states or implies the exact minimal census \(N=20\) under **simultaneously fixed** abundance total and richness, the precise three-order strict orientation, or the single boundary partition pair. This conclusion is limited to the materials actually inspected; absence of matching text is not a uniqueness proof for all scientific literature.

Other results on generic profile crossing do not directly establish the equal-richness fixed-census threshold or classification. Other literature may imply the result through unrecognized formulations.

## Limitations

The integer census bound refers to idealized complete observations, not estimates from sampling. The theorem does not optimize the magnitude of diversity differences, classify all possible Hill-order intersections, or determine minimal census sizes for other triples of orders. Its computational proof is exact and exhaustive over a **finite** domain; it does not assert completeness of bibliographic searches. The full 1995 paper of Tóthmérész was not obtained; publisher abstract and metadata were accessible, and institutional access was unavailable. An overlooked equivalent result, especially in ecological diversity-ranking or Rényi-entropy literature, remains a substantive bibliographic risk.

## References

1. Hill, M. O. (1973). *Diversity and evenness: a unifying notation and its consequences*. Ecology 54:427–432. DOI: 10.2307/1934352. First publicly published March 1, 1973.
2. Tóthmérész, B. (1995). *Comparison of different methods for diversity ordering*. Journal of Vegetation Science 6:283–290. DOI: 10.2307/3236223.
3. Jost, L. (2006). *Entropy and diversity*. Oikos 113:363–375. DOI: 10.1111/j.2006.0030-1299.14714.x.
4. Liu, C., Whittaker, R. J., Ma, K., and Malcolm, J. R. (2007). *Unifying and distinguishing diversity ordering methods for comparing communities*. Population Ecology 49:89–100. DOI: 10.1007/s10144-006-0026-0. First online December 15, 2006.
