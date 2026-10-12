# Unique optimal ternary length-three single limited-magnitude asymmetric-error code
## Finding
Let
\[
Q=\{0,1,2\},
\]
and for \(x\in Q^3\) let the one-error output set be
\[
B(x)=\{x\}\cup\{x+e_i:x_i<2,\ 1\le i\le3\},
\]
where \(e_i\) is the \(i\)-th unit vector. Thus at most one coordinate may increase by exactly \(1\), and no wraparound is allowed.

If \(C\subseteq Q^3\) has pairwise disjoint output sets \(B(x)\), then
\[
|C|\le9.
\]
Equality is attained by exactly one labeled code:
\[
C_*=\{000,002,020,022,111,200,202,220,222\}
     =\{0,2\}^3\cup\{111\}.
\]

The optimizer is exactly the \(q=3\), \(\ell=1\), \(n=3\) specialization of the Cassuto--Schwartz--Bohossian--Bruck construction with binary repetition base code
\[
\Sigma=\{000,111\}.
\]
Indeed,
\[
C_*=\{x\in Q^3:x\bmod2\in\Sigma\}.
\]

## Assumptions and scope
The channel is the non-wraparound asymmetric limited-magnitude channel: an error vector has at most one nonzero coordinate, every nonzero error is \(+1\), and outputs must remain in \(Q^3\). A code corrects the channel exactly when distinct codewords have disjoint output sets.

The symbols \(0,1,2\) have their ordered level meaning; arbitrary alphabet permutations are not channel symmetries. Coordinates are labeled. No linearity assumption is imposed.

## Proof
A direct nine-part conflict partition gives the upper bound. Partition \(Q^3\) into the following nine triples:
\[
\begin{aligned}
&\{000,001,010\},\quad \{002,011,012\},\quad \{020,021,120\},\\
&\{022,112,121\},\quad \{100,101,200\},\quad \{102,201,202\},\\
&\{110,111,210\},\quad \{122,212,222\},\quad \{211,220,221\}.
\end{aligned}
\]
Within each displayed triple, every two words have intersecting one-error output sets. Hence a correcting code contains at most one word from each triple, proving \(|C|\le9\).

For the lower bound, direct inspection of
\[
C_*=\{0,2\}^3\cup\{111\}
\]
shows that its nine output sets are pairwise disjoint, so \(|C_*|=9\) is achievable.

For uniqueness, the verifier constructs the complete compatibility graph on all \(27\) words, where two vertices are adjacent exactly when their output sets are disjoint. An exact Bron--Kerbosch traversal enumerates every maximal clique and finds one clique of maximum size \(9\). A separate fixed-size recursive search independently counts compatible nine-subsets and also returns exactly one. The unique set is \(C_*\).

Finally, reducing the symbols of \(C_*\) modulo \(2\) gives either \(000\) or \(111\), and every ternary word with one of those two residue patterns belongs to \(C_*\). Thus the optimizer is precisely the length-three lift of the binary repetition code under the published modulo-\(2\) construction.

## Verification
Run `python3 verify.py`. The verifier uses only the Python standard library. It rebuilds all \(27\) words and their one-error output sets in two independent ways, verifies every conflict in the nine-triple upper-bound certificate, checks the nine-word construction, exhaustively enumerates all maximal compatibility cliques, independently counts all compatible nine-subsets, and checks the modulo-\(2\) construction identity.

The terminal line is:

`VERIFY_OK maximum=9 labeled_maxima=1 unique_code=corners_plus_center`

## Relationship to prior work
Cassuto, Schwartz, Bohossian, and Bruck introduced the asymmetric limited-magnitude flash-memory model and the modulo-\(\ell+1\) lifting construction. For \(\ell=1\), their Construction 1 lifts a binary code \(\Sigma\) to all \(q\)-ary words whose coordinatewise residues modulo \(2\) lie in \(\Sigma\). Taking the binary length-three repetition code therefore already constructs the nine-word set \(C_*\).

The inspected paper proves general correction properties, size formulas for the construction, broader bounds, asymptotic optimality statements, and a ternary perfect-code example at length \(2\). It does not state the finite non-wraparound \(q=3,n=3,t=1,\ell=1\) optimum, prove that no tenth word is possible, or classify the equality case. The result here adds exactly those finite extremal facts; it does not claim the nine-word construction itself as new.

The earliest public technical-report file located in the Caltech Paradise index is the April 2007 report, whose public file index records the file date \(2007\)-\(04\)-\(23\). The later ISIT 2007 and IEEE Transactions on Information Theory versions describe the same model and construction.

## Limitations
This is an exact finite classification only for three ternary cells, one upward magnitude-one error, and the non-wraparound channel. It does not classify wraparound codes, downward-error variants with independently relabeled levels, more than one error, larger alphabets, or larger blocklengths.

The exhaustive search is used only for uniqueness. The maximum-size upper bound has the independent explicit nine-triple certificate above. A residual bibliographic risk remains that an obscure or unindexed finite enumeration could contain the same equality statement; no such statement was found in the inspected primary text, exact-parameter searches, or published-result search.

## References
1. Y. Cassuto, M. Schwartz, V. Bohossian, and J. Bruck, “Codes for Multi-Level Flash Memories: Correcting Asymmetric Limited-Magnitude Errors,” Caltech Paradise technical report, public file index dated 2007-04-23; later ISIT 2007, DOI 10.1109/ISIT.2007.4557123.
2. Y. Cassuto, M. Schwartz, V. Bohossian, and J. Bruck, “Codes for Asymmetric Limited-Magnitude Errors With Application to Multilevel Flash Memories,” IEEE Transactions on Information Theory 56(4), 2010, DOI 10.1109/TIT.2010.2040971.
3. T. Kløve and M. Schwartz, “Linear covering codes and error-correcting codes for limited-magnitude errors,” Designs, Codes and Cryptography, DOI 10.1007/s10623-013-9917-1.
