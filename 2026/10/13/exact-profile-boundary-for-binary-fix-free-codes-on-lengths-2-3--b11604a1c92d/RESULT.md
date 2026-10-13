# Exact profile boundary for binary fix-free codes on lengths \(2,3,4\)

## Finding
A binary fix-free code is a finite set of binary words in which no codeword is a prefix or a suffix of any distinct codeword. Restrict the allowed codeword lengths to \(2,3,4\), and write \(a_j\) for the number of codewords of length \(j\). For each feasible pair \((a_2,a_3)\), let \(M(a_2,a_3)\) be the largest attainable value of \(a_4\).

The exact table is
\[
\begin{aligned}
M(0,0),\ldots,M(0,8)&=(16,13,10,8,6,4,2,1,0),\\
M(1,0),\ldots,M(1,5)&=(9,7,6,5,4,1),\\
M(2,0),M(2,1),M(2,2)&=(4,3,2),\\
M(3,0),M(3,1)&=(1,0),\\
M(4,0)&=0.
\end{aligned}
\]
All unlisted pairs \((a_2,a_3)\) are infeasible. Consequently a profile \((a_2,a_3,a_4)\) is realizable exactly when its pair is listed and \(0\le a_4\le M(a_2,a_3)\).

Equivalently, among profiles supported on these three consecutive lengths, every profile whose Kraft sum
\[
K=\frac{a_2}{4}+\frac{a_3}{8}+\frac{a_4}{16}
\]
is at most \(3/4\) is realizable, whereas the first impossible discrete Kraft level above that universal guarantee is \(13/16\). At that level the unique impossible profile is \((2,0,5)\).

## Assumptions and scope
The alphabet is exactly binary. Codewords are distinct finite words, and prefix/suffix exclusion is only between distinct codewords. Only lengths \(2\), \(3\), and \(4\) are permitted. The claim is a complete finite profile classification for this length window; it is not a characterization for arbitrary length multisets and does not strengthen the general \(3/4\)-conjecture theorem.

## Proof
There are four binary words of length \(2\) and eight of length \(3\). Enumerate every subset \(C_2\) of the four length-two words and every subset \(C_3\) of the eight length-three words. Retain exactly those pairs for which no member of \(C_2\) is a prefix or suffix of a member of \(C_3\).

For a retained pair define \(A(C_2,C_3)\) to be the set of all sixteen length-four words having neither a prefix nor a suffix in \(C_2\cup C_3\). Every subset of \(A(C_2,C_3)\) can be added without creating a new fix-free violation: distinct length-four words cannot be proper prefixes or proper suffixes of one another, and membership in \(A(C_2,C_3)\) has already removed every conflict with a shorter selected word. Therefore, for fixed \((a_2,a_3)\),
\[
M(a_2,a_3)=\max\{|A(C_2,C_3)|:|C_2|=a_2,\ |C_3|=a_3,\ C_2\cup C_3\text{ is fix-free}\}.
\]
This reduction is exact in both directions: every fix-free code determines one enumerated shorter-layer pair and uses at most its available length-four words, while every enumerated pair together with any chosen subset of its available words is a fix-free code.

The bundled verifier exhausts all \(2^4\cdot2^8=4096\) shorter-layer choices and computes \(A(C_2,C_3)\) directly. It returns exactly the table above. It then tests every integer profile satisfying \(4a_2+2a_3+a_4\le16\), which is the Kraft condition \(K\le1\) after scaling by sixteen. The least scaled Kraft value among infeasible profiles is \(13\), and the sole infeasible profile at that level is \((2,0,5)\); every profile with scaled Kraft at most \(12\) is feasible. This proves both the table and the stated boundary.

## Verification
Run `python3 artifacts/verify.py`. The script uses only the Python standard library. It reconstructs all binary words at the three lengths, enumerates every pair of shorter-layer subsets, checks the prefix/suffix condition, computes the available longest layer, compares the resulting table with the claimed table, and independently scans the full finite profile grid through Kraft sum \(1\). The captured package replay in `artifacts/verification_output.txt` begins with `VERIFY_OK` and records the first impossible scaled Kraft value as \(13\), corresponding to \(13/16\).

The computation is exhaustive rather than statistical. No timeout, floating-point optimization, or unproved extrapolation is used.

## Relationship to prior work
Harada and Kobayashi studied sufficient length conditions for binary fix-free codes and proved the \(3/4\) guarantee for multisets with at most two distinct lengths. Congero and Zeger later proved the \(3/4\) conjecture for every binary multiset with at most three distinct codeword lengths. Their Theorem III.1 restates the two-length \(3/4\) guarantee, while their main theorem handles three distinct lengths at Kraft sum at most \(3/4\).

Those theorems imply the feasible part of the present table below or on the \(3/4\) boundary, but they do not determine which profiles above \(3/4\) remain feasible, nor the exact longest-layer function \(M(a_2,a_3)\) for the consecutive window \(2,3,4\). Focused searches under the aliases fix-free, biprefix, bifix, and reversible variable-length code did not locate a published exact table or a statement implying the complete profile classification above. The closest indexed computational record concerns implementing the general three-length \(3/4\) construction efficiently; it does not address the region above \(3/4\).

## Limitations
The result is intentionally local: it classifies one shortest nontrivial three-consecutive-length window and does not give a formula for shifted windows \(m,m+1,m+2\) or arbitrary length sets. The originality conclusion is bibliographic rather than a proof of historical priority; an obscure or unindexed small-profile enumeration may exist. The first-impossible-level statement is relative to profiles supported on lengths \(2,3,4\), not to all binary fix-free length multisets.

## References
1. K. Harada and K. Kobayashi, “A Note on the Fix-Free Code Property,” *IEICE Transactions on Fundamentals*, E82-A(10), 2121–2128, 1999. Publication date: 1999-10-25.
2. Z. Kukorelly and K. Zeger, “Sufficient conditions for existence of binary fix-free codes,” *IEEE Transactions on Information Theory* 51(10), 3433–3444, 2005. DOI: 10.1109/TIT.2005.855581.
3. S. Congero and K. Zeger, “The 3/4 Conjecture for Fix-Free Codes With at Most Three Distinct Codeword Lengths,” *IEEE Transactions on Information Theory* 69(3), 1452–1485, 2023. DOI: 10.1109/TIT.2022.3218212.
