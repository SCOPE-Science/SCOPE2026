# Exact ternary \((2,3)\)-overlap-free code size for lengths at least six

## Finding

Let \(\Sigma=\{0,1,2\}\). A block code \(C\subseteq\Sigma^n\) is **\((2,3)\)-overlap-free** when, for each \(k\in\{2,3\}\) and all \(u,v\in C\), including \(u=v\), the first \(k\) symbols of \(u\) do not equal the last \(k\) symbols of \(v\). Denote the largest possible size by \(S_2^3(3,n)\). For every integer \(n\ge6\),

\[
\boxed{S_2^3(3,n)=132\cdot3^{n-6}.}
\]

An explicit optimal code is \(P\Sigma^{n-6}T\), where

\[
P=\{(a,b,c)\in\Sigma^3: 0\in\{a,b\}\text{ and }0\in\{b,c\}\},
\qquad
T=\{(a,b,c)\in\Sigma^3:b\ne0,\ c\ne0\}.
\]

These sets have cardinalities \(11\) and \(12\), respectively. The formula concerns **only** overlaps of lengths two and three; it makes no restriction on overlaps of other lengths.

## Assumptions and scope

All words are ordered strings over the three-symbol alphabet, not vectors subject to a linearity condition. Prefixes and suffixes of a given length are ordinary consecutive end-blocks. The parameter \(n\) is an arbitrary integer at least six, so the first three and last three positions do not overlap. Self-overlaps are forbidden. The independent \(n-6\) middle symbols contribute the factor \(3^{n-6}\).

## Proof

For any admissible code \(C\), let \(P_C\) and \(T_C\) be its sets of length-three prefixes and suffixes. Let \(A_C\) and \(B_C\) be its sets of length-two prefixes and suffixes. The forbidden overlaps imply

\[
P_C\cap T_C=\varnothing,\qquad A_C\cap B_C=\varnothing.
\]

Every codeword is determined by a length-three prefix, a length-\(n-6\) middle block, and a length-three suffix. Consequently,

\[
|C|\le |P_C|\,|T_C|\,3^{n-6}.
\]

Fix arbitrary disjoint sets \(A,B\subseteq\Sigma^2\), with \(a=|A|\) and \(b=|B|\). Define the candidate triple sets

\[
U_A=\{(i,j,k)\in\Sigma^3:(i,j)\in A\},\qquad
V_B=\{(i,j,k)\in\Sigma^3:(j,k)\in B\}.
\]

Then \(|U_A|=3a\), \(|V_B|=3b\), and their intersection has cardinality

\[
h(A,B)=\sum_{i,j,k\in\Sigma}\mathbf1_{(i,j)\in A}\mathbf1_{(j,k)\in B}.
\]

Since \(P_C\subseteq U_{A_C}\), \(T_C\subseteq V_{B_C}\) and \(P_C\cap T_C=\varnothing\), the largest possible product of the two sizes for this fixed \((A,B)\) is at most

\[
F(A,B)=\max_{0\le t\le h(A,B)}
\bigl(3a-h(A,B)+t\bigr)\bigl(3b-t\bigr).
\]

Indeed, the parts of \(U_A\) and \(V_B\) outside their intersection can all be retained, whereas their \(h(A,B)\) common triples can be allocated disjointly to either side. Because both factors are nonnegative and the product is monotone in each, allowing all common triples to be allocated cannot decrease the attainable upper envelope. If \(t\) common triples go to the prefix side, the displayed factors follow.

It remains to bound \(F(A,B)\). There are exactly \(3^9=19683\) ordered pairs of disjoint subsets \((A,B)\) of \(\Sigma^2\): each of the nine ordered pairs receives one label, *unused*, *in* \(A\), or *in* \(B\). The accompanying finite certificate explicitly enumerates all these assignments, evaluates \(h(A,B)\) from all 27 triples, maximizes the above quadratic for every integer \(t\) in its complete range, and checks

\[
\max_{A\cap B=\varnothing}F(A,B)=132.
\]

For a compact reproducibility checksum, the maxima when the number \(|A|+|B|\) of labeled (nonunused) ordered pairs is, respectively, \(0,1,2,3,4,5,6,7,8,9\) are

\[
(0,0,9,18,36,54,81,108,121,132).
\]

The source file `verify.py` contains all loops, set definitions, and assertions necessary to rederive these values using only Python's standard library. The finite certificate establishes an exhaustive inequality, not an inference from a sample of codewords. Therefore \(|C|\le132\cdot3^{n-6}\).

For the opposite inequality, use the displayed sets \(P,T\). If the middle symbol of a triple in \(P\) is zero, its two other symbols are unrestricted, yielding nine possibilities; otherwise both end symbols must be zero, yielding two more. Thus \(|P|=11\). For \(T\), the first symbol is unrestricted and the last two have two options each, giving \(|T|=12\). Every length-two prefix of a member of \(P\) contains zero, whereas no length-two suffix of a member of \(T\) contains zero. Therefore \(P\Sigma^{n-6}T\) has no overlap of length two. Moreover, the last two symbols of every member of \(P\) contain zero, whereas the last two of every member of \(T\) do not; hence \(P\cap T=\varnothing\), excluding length-three overlaps. All \(11\cdot3^{n-6}\cdot12\) concatenations are different. They attain the upper bound for every \(n\ge6\).

## Verification

Run `python3 verify.py` using a Python interpreter supporting `int.bit_count()` (Python 3.8 users can substitute a population-count routine; the included script targets Python 3.10 or later). The verifier prints `VERIFY_OK` after checking the complete \(3^9\) pair-label assignment universe, the upper-bound checksum, an independent bitmask-based enumeration, and explicit all-word overlap checks for lengths six and seven. Those short-length checks are supporting consistency tests; the proof of the infinite length range comes from the arbitrary-middle-block decomposition.

## Relationship to prior work

Blackburn, Nasr Esfahani, Kreher, and Stinson develop general restricted-overlap bounds and prefix/suffix-block constructions. Stanovnik proves the general reduction from \(n\ge2t_2\) to the base length \(2t_2\), in particular the already-known scaling identity \(S_2^3(3,n)=3^{n-6}S_2^3(3,6)\). Yang and Ding provide \(q\)-ary constructions and enumerations for interval-restricted overlaps, but their inspected results do not give the exact unrestricted ternary optimum \(S_2^3(3,6)=132\). For these parameters, their bipartition construction with \(k\in\{1,2\}\) reaches at most \(108\cdot3^{n-6}\); this is a construction comparison, not a bound on their broader research program. The substantive new content here is the exact base-six optimum, together with an attaining construction and a complete small finite upper-bound certificate.

## Limitations

No optimum is asserted for other alphabets, lengths below six, or other forbidden-overlap intervals. The upper certificate requires finite exhaustive enumeration of 19683 assignments; it is fully reproducible and independently expressed as a bitmask check, but is not reduced to a classification-free inequality. Absence of an equivalent unpublished or unindexed result cannot be guaranteed by literature searches. No independent external audit is claimed.

## References

1. H. Yang and Y. Ding, *Q-Ary \((t_1,t_2)\)-Overlap-Free Codes*, IEICE Transactions on Fundamentals E109-A (2026), 757–762, DOI: 10.1587/transfun.2025EAL2050; advance online publication 2025-09-22.
2. L. Stanovnik, *Codes with restricted overlaps: expandability, constructions, and bounds*, arXiv:2411.02899 (2024), published in Journal of Applied Mathematics and Computing (2025), DOI: 10.1007/s12190-025-02441-z, Proposition 3.
3. S. R. Blackburn, N. Nasr Esfahani, D. L. Kreher, and D. R. Stinson, *Constructions and bounds for codes with restricted overlaps*, IEEE Transactions on Information Theory 70 (2024), 2479–2490, DOI: 10.1109/TIT.2023.3304712, arXiv:2211.10309.
