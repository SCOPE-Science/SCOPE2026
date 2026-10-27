# Sharp saturation of binary two-symbol deletion list codes

## Finding
For integers \(n\ge 3\) and \(L\ge 1\), let \(M(n,L)\) be the maximum size of a set of **distinct** binary words of length \(n\) such that every binary word of length two is a (not necessarily contiguous) subsequence of at most \(L\) selected words. Equivalently, exactly \(n-2\) symbols are deleted and the decoder's worst-case list has size at most \(L\). Define
\[
B(L)=\min\left\{2L,\left\lfloor\frac{4L+8}{3}\right\rfloor\right\}.
\]
Then \(M(n,L)\le B(L)\). Equality holds **if and only if** either \(L\le4\), or both \(L\ge5\) and
\[
n\ge n_{\mathrm{sat}}(L):=\max\left\{4,\left\lceil\frac L3\right\rceil+1\right\}.
\]
In particular, for every fixed list allowance \(L\ge5\), the optimum stabilizes at \(\lfloor(4L+8)/3\rfloor\) precisely from \(n_{\mathrm{sat}}(L)\) onward. Before that length, the optimum is strictly smaller. For \(1\le L\le4\), the optimum equals \(2L\) at every length \(n\ge3\).

## Assumptions and scope
Write \(\Sigma=\{0,1\}\), and for \(w=w_1\cdots w_n\in\Sigma^n\), define its **two-subsequence signature**
\[
S(w)=\{w_iw_j:1\le i<j\le n\}\subseteq\{00,01,10,11\}.
\]
A code \(\mathcal C\subseteq\Sigma^n\) is admissible precisely when \(\ell_y:=|\{w\in\mathcal C:y\in S(w)\}|\le L\) for each \(y\) in this four-element received alphabet. A subsequence need not consist of adjacent symbols; distinct output words, rather than the number of deletion patterns, are counted. This convention is essential.

## Proof
**1. Two universal upper bounds.** Every length-\(n\) binary word with \(n\ge3\) has a repeated symbol in two distinct positions, so it contains \(00\) or \(11\) as a subsequence. Hence
\[
|\mathcal C|\le\ell_{00}+\ell_{11}\le2L.
\]
Exactly two length-\(n\) words have a one-element signature, namely \(0^n\) and \(1^n\). Exactly four have a two-element signature, namely
\[
0^{n-1}1,\quad10^{n-1},\quad01^{n-1},\quad1^{n-1}0.
\]
To verify exhaustiveness, any word with at least two occurrences of both symbols has \(00\), \(11\), and at least one cross-symbol subsequence, and a word with a unique minority symbol at an interior position has the majority-symbol repeated pair and both cross-symbol subsequences. All other nonconstant words thus have at least three outputs. Summing the signature sizes therefore gives
\[
\sum_y\ell_y=\sum_{w\in\mathcal C}|S(w)|\ge3|\mathcal C|-8,
\]
because the two one-output words can each lower the baseline of three by two, and the four two-output words can each lower it by one. Since \(\sum_y\ell_y\le4L\), the second bound follows:
\[
|\mathcal C|\le\left\lfloor\frac{4L+8}{3}\right\rfloor.
\]

**2. All possible three-output signatures.** For \(n\ge4\), the words with exactly three distinct two-symbol subsequences split into the following four disjoint classes (the subscript names the *missing* output):
\[
\begin{aligned}
E_{00}&=\{1^a01^{n-a-1}:1\le a\le n-2\},&|E_{00}|&=n-2,\\
E_{11}&=\{0^a10^{n-a-1}:1\le a\le n-2\},&|E_{11}|&=n-2,\\
E_{01}&=\{1^a0^{n-a}:2\le a\le n-2\},&|E_{01}|&=n-3,\\
E_{10}&=\{0^a1^{n-a}:2\le a\le n-2\},&|E_{10}|&=n-3.
\end{aligned}
\]
Indeed, absence of \(00\) (or \(11\)) together with all other pairs forces exactly one interior zero (respectively one interior one). Absence of \(01\) (or \(10\)) forces a single descending (respectively ascending) run boundary with both runs of length at least two. Thus there are exactly \(4n-10\) three-output words. At \(n=3\), only the first two classes are nonempty, with one word each; the argument below treats this short case separately.

**3. Necessity of the saturation length.** Assume \(L\ge5\) and \(n\ge4\). Put \(B=\lfloor(4L+8)/3\rfloor\) and \(\delta=4L+8-3B\in\{0,1,2\}\). Suppose an admissible code has \(B\) words. Let \(a\le6\) be its number of words having at most two outputs, \(t\le4n-10\) its number with three outputs, and \(q\) its number with four outputs. Define \(e=\sum_{w\in\mathcal C,\,|S(w)|\le2}(3-|S(w)|)\le8\). By double counting,
\[
3B-e+q=\sum_y\ell_y\le4L,
\]
so \(q\le\delta\) and
\[
B=a+t+q\le6+(4n-10)+\delta=4n-4+\delta.
\]
Writing \(L=3h+s\) with \(s\in\{0,1,2\}\), the three cases respectively give
\[
(B,\delta)=(4h+2,2),\qquad(4h+4,0),\qquad(4h+5,1).
\]
The last bound forces \(n\ge h+1\) if \(s=0\), and \(n\ge h+2\) if \(s=1\) or \(s=2\), exactly \(n\ge\lceil L/3\rceil+1\). At \(n=3\) and \(L\ge5\), the bound \(B\ge9\) cannot be attained because only eight binary words exist. Hence \(n\ge n_{\mathrm{sat}}(L)\) is necessary.

**4. Constructions achieving both upper bounds.** Let \(H\) be the set of the six words listed in Step 1. Their loads in the output order \((00,01,10,11)\) are \((3,2,2,3)\). For \(L=1\) select the two constant words. For \(L=2\) select \(0^n,1^n,0^{n-1}1,1^{n-1}0\). For \(L=3\) use \(H\). For \(L=4\) use \(H\) and one word each from \(E_{00}\) and \(E_{11}\); these exist even when \(n=3\). The resulting code sizes are \(2L\), with every receiver load at most \(L\).

For the remaining cases, choose any distinct words in each class according to the indicated multiplicities; the available class sizes in Step 2 guarantee the choices. In addition, the two distinct words \(0101\,0^{n-4}\) and \(1010\,1^{n-4}\) have all four outputs whenever \(n\ge4\).

* If \(L=3h\) with \(h\ge2\), take \(H\), \(h-1\) words from each of \(E_{00},E_{11}\), \(h-2\) from each of \(E_{01},E_{10}\), and both four-output words. This is possible for \(n\ge\max\{4,h+1\}\). Its size is \(4h+2=B(L)\), and every one of the four receiver loads is \(3h=L\).
* If \(L=3h+1\) with \(h\ge1\), take \(H\), \(h\) words from each of \(E_{00},E_{11}\), and \(h-1\) from each of \(E_{01},E_{10}\). For \(n\ge h+2\), the size is \(4h+4=B(L)\) and all loads equal \(3h+1=L\).
* If \(L=3h+2\) with \(h\ge1\), use the preceding \(L=3h+1\) selection and add one four-output word. For \(n\ge\max\{4,h+2\}\), the size is \(4h+5=B(L)\), and all loads equal \(3h+2=L\).

Each construction consists of distinct words because the signature classes are disjoint; within each class, the range of the run parameter gives distinct words. Together with Step 3 these constructions prove the asserted if-and-only-if saturation threshold. \(\square\)

## Verification
Run `python3 check.py` with Python 3.9 or later. The standalone standard-library checker independently enumerates all binary words of lengths three through eleven to verify the four signature-class counts, constructs codes at and above the stated thresholds for list allowances one through sixty, and uses an exact integer dynamic program to check the maxima for lengths three through six and list allowances one through ten. It reports `PASS enumerated_words 4088 construction_cases 240 exact_DP_cases 40`. These finite checks corroborate the argument; the proof above handles all permitted integers.

## Relationship to prior work
Lin, *Lower Bounds for all List-Decodable Deletion Codes* (2026), treats binary deletion list decoding primarily in the regime of a fixed deletion count and develops asymptotic lower bounds, plus common-subsequence inequalities. It does not give an exact extremal formula when precisely two symbols remain. Con, Doron, and Ribeiro (2026) study rate capacity with a fixed fraction of insertion or deletion errors, rather than the finite four-output capacity problem and its exact stabilization threshold. The new claim occupies the opposite, near-total-deletion regime, with both source length and list allowance variable. Unlike unordered multiset deletion, retaining \(01\) and \(10\) as separate outputs is essential here.

## Limitations
No exact value is asserted for \(M(n,L)\) at lengths below \(n_{\mathrm{sat}}(L)\) when \(L\ge5\); only strict nonattainment of the universal bound is proved. The analysis is for binary strings, exactly two *ordered* surviving symbols, distinct codewords, and worst-case list size. It does not cover longer surviving subsequences, larger alphabets, or multiplicity-weighted deletion transcripts. Independent validation and a complete literature-priority determination have not been performed.

## References
1. Andrew D. Lin, *Lower Bounds for all List-Decodable Deletion Codes*, arXiv:2609.26650v1, first posted 2026-09-22, https://arxiv.org/abs/2609.26650.
2. Roni Con, Dean Doron, João Ribeiro, *The Insertion List-Decoding Capacity and an Improved Bound on the Deletion List-Decoding Capacity*, arXiv:2607.03989v1, 2026-07-04, https://arxiv.org/abs/2607.03989.
3. Venkatesan Guruswami and Johan Håstad, *Explicit Two-Deletion Codes With Redundancy Matching the Existential Bound*, IEEE Transactions on Information Theory 67 (2021), 6384–6394, DOI:10.1109/TIT.2021.3069446.
