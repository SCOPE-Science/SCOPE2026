# Exact worst-case inverse degree for one noisy tandem duplication
## Finding
Let \(\Sigma_q\) be an alphabet with \(q\ge 2\), let \(n\ge k\ge 1\), and consider exactly one noisy tandem duplication of length \(k\): if a parent has the form \(x=uvw\) with \(|v|=k\), the channel outputs \(uvv'w\), where \(|v'|=k\) and \(d_H(v,v')=1\). For a received word \(y\in\Sigma_q^{n+k}\), let \(P_k(y)\) be the set of distinct length-\(n\) parents that can produce \(y\) by this operation. Put \(m=n-k+1\). Then
\[
\max_{y\in\Sigma_q^{n+k}} |P_k(y)|
=2\left\lfloor\frac{m}{k+1}\right\rfloor+
\min\{2,\,m\bmod(k+1)\}.
\]
This value is independent of \(q\) once \(q\ge2\).

## Assumptions and scope
The duplication length \(k\) is fixed and positive. The noisy copy differs from the original copied block in exactly one coordinate, as in the standard one-noisy-duplication model. Only one duplication is applied; no additional exact duplications or substitutions are included in \(P_k(y)\). Distinct operation locations that yield the same parent are counted once.

## Proof
Index \(y\) from \(0\). Define the binary mismatch profile
\[
z_t=\mathbf 1\{y_t\ne y_{t+k}\},\qquad 0\le t<n.
\]
There are \(m=n-k+1\) possible inverse starts \(i\in\{0,\ldots,m-1\}\). Start \(i\) is legal exactly when
\[
\sum_{t=i}^{i+k-1}z_t=1.
\]
For a legal start \(i\), let \(r(i)\in[i,i+k-1]\) be the unique index with \(z_{r(i)}=1\), and let \(p_i\) be the parent obtained by deleting \(y_{i+k},\ldots,y_{i+2k-1}\).

For legal \(i<j\), direct comparison of the two deleted strings gives
\[
p_i=p_j
\quad\Longleftrightarrow\quad
y_{i+k:j+k}=y_{i+2k:j+2k}
\quad\Longleftrightarrow\quad
z_t=0\text{ for every }t\in[i+k,j+k-1].
\]
If \(j-i\ge k\), the interval on the right contains \(r(j)\), so \(p_i\ne p_j\). If \(0<j-i<k\), that interval is the terminal part of the unique-one window of start \(j\), hence
\[
p_i\ne p_j\quad\Longleftrightarrow\quad r(j)\ge i+k.
\]

Now choose one start for each distinct parent. No three chosen starts can lie in \(k+1\) consecutive start positions. Indeed, if \(i<j<\ell\) and \(\ell-i\le k\) represented three distinct parents, then distinctness of \(p_i,p_j\) would force \(r(j)\ge i+k\ge\ell\), while distinctness of \(p_j,p_\ell\) would force \(r(\ell)\ge j+k>r(j)\). Both \(r(j)\) and \(r(\ell)\) would then lie in the length-\(k\) mismatch window of start \(\ell\), contradicting its having weight one. Partitioning the \(m\) possible starts into consecutive blocks of length \(k+1\) therefore gives
\[
|P_k(y)|\le 2\left\lfloor\frac{m}{k+1}\right\rfloor+
\min\{2,\,m\bmod(k+1)\}.
\]

For equality, prescribe \(z\) as the length-\(n\) truncation of the periodic binary word with block \(1 0^{k-1}1\), of period \(k+1\). In each complete block of \(k+1\) start positions, exactly the first two starts have a weight-one mismatch window; a final partial block contributes exactly \(\min\{2,\,m\bmod(k+1)\}\) legal starts. The two legal starts within one block yield distinct parents by the preceding criterion, and legal starts in different blocks are separated by at least \(k\), so all these parents are distinct.

Every such mismatch profile is realizable over any \(q\ge2\): choose two symbols \(a,b\), set the first \(k\) symbols of \(y\) to \(a\), and recursively set \(y_{t+k}=y_t\) when \(z_t=0\) and toggle \(a\leftrightarrow b\) when \(z_t=1\). This completes the proof.

## Verification
The accompanying `verify.py` independently reconstructs inverse parents by literal deletion from received words. It exhaustively checks the formula and the parent-collision criterion on \(27\) parameter cases over binary and ternary alphabets, totaling \(7{,}829\) received words. It also constructs the periodic witnesses for \(1\le k\le12\) and \(k\le n\le100\), checking \(1{,}134\) further parameter pairs. Its terminal output is `VERIFY_OK exhaustive_cases=27 received_words=7829 witness_cases=1134 k<=12_n<=100`.

## Relationship to prior work
Tang and Farnoud introduced and analyzed the fixed-length noisy tandem-duplication model in which the copied block is at Hamming distance one from the original, and developed codes correcting any number of exact duplications together with one noisy duplication. Their analysis is expressed through duplication roots and derived subsequences. The inspected full text defines the noisy operation and descendant cones and then characterizes root-level error patterns for code construction; targeted full-text searches for inverse-ball terminology did not locate a theorem counting distinct one-step parents of a fixed received word.

Lenz, Wachter-Zeh, and Yaakobi determined sphere information for exact tandem and palindromic duplication/deletion channels. That work is a necessary comparison because a one-step parent set is an inverse sphere, but its tandem-deletion condition requires equality of the adjacent length-\(k\) blocks. The present noisy condition requires Hamming distance exactly one, and the collision structure is governed by overlapping weight-one windows in the mismatch profile. Thus the exact-duplication sphere formulas do not imply the displayed noisy inverse-degree law.

## Limitations
The theorem concerns exactly one noisy duplication and counts distinct parents, not operation histories. It does not give code cardinalities, multiple-noisy-duplication inverse degrees, or inverse degrees when the copied block may contain more than one substitution. The literature comparison cannot exclude an unindexed or differently phrased prior derivation; no such statement was found in the inspected primary sources or published-result searches.

## References
1. Y. Tang and F. Farnoud, “Error-correcting Codes for Noisy Duplication Channels,” 57th Annual Allerton Conference on Communication, Control, and Computing, 2019, pp. 140–146, DOI 10.1109/ALLERTON.2019.8919847; expanded as arXiv:2008.08174 and IEEE Transactions on Information Theory 67(6), 2021.
2. Y. Tang, Y. Yehezkeally, M. Schwartz, and F. Farnoud, “Single-Error Detection and Correction for Duplication and Substitution Channels,” arXiv:1911.05413; IEEE Transactions on Information Theory 66(11), 2020.
3. A. Lenz, A. Wachter-Zeh, and E. Yaakobi, “Duplication-Correcting Codes,” arXiv:1712.09345; Designs, Codes and Cryptography 87, 2019.
4. Y. Tang and F. Farnoud, “Error-correcting Codes for Short Tandem Duplication and Substitution Errors,” arXiv:2011.05896.
