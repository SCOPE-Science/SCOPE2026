# Sharp five-run capacity and exceptional optimizers for the binary subsequence \(0101\)

## Finding

Fix the binary scattered-subsequence pattern \(p=0101\). For an integer \(n\ge4\), let \(c_p(w)\) be the number of strictly increasing four-tuples of positions of a length-\(n\) binary word \(w\) whose selected letters spell \(0101\). Let \(R(w)\) count its maximal constant runs and put
\[
M_n=\max_{w\in\{0,1\}^n}c_p(w),\qquad
Q_n=\max_{\substack{w\in\{0,1\}^n\\R(w)\le5}}c_p(w).
\]
Write \(n=4t+r\), where \(t\ge1\) and \(0\le r\le3\). Then
\[
\boxed{Q_n=t^{4-r}(t+1)^r.}
\]
The complete equality set between this low-run capacity and the unrestricted optimum is
\[
\boxed{M_n=Q_n\ \Longleftrightarrow\ n\in\{4,5,8\}.}
\]
For every other \(n\ge4\), an explicit length-\(n\) six-run word has strictly more \(0101\)-subsequences than *every* word with at most five runs. Consequently, every unrestricted maximizer at such lengths has at least six runs. No assertion that six runs suffice for global optimality at every large length is made.

## Assumptions and scope

Words are finite, indexed from left to right, and may have either initial symbol. A subsequence is an order-preserving selection of positions; it is not required to be contiguous. Two distinct position sets count as different occurrences even if their selected symbols are equal. A run is a maximal nonempty contiguous block of one symbol. Every claim holds for all integers \(n\ge4\); no claim is made for hosts shorter than the pattern.

## Proof

**Step 1: the exact five-run capacity.** A word containing \(0101\) requires at least four runs. A word with exactly four runs has a positive count only if it is
\[
w=0^a1^b0^c1^d,\quad a,b,c,d\in\mathbb Z_{\ge1},\quad a+b+c+d=n.
\]
All four selected positions must come from the four respective runs, so \(c_p(w)=abcd\). A word with exactly five runs either begins with a nonparticipating initial run of ones, or ends with a nonparticipating final run of zeros. Deleting that run leaves a four-run host of shorter length, without changing the count. Appending any symbol to a run of a four-run host increases its product, so no five-run host outperforms the best four-run host at length \(n\). Hosts with fewer than four runs have count zero. Finally, if \(a\ge b+2\), replacing \((a,b)\) by \((a-1,b+1)\) strictly increases \(ab\) while preserving the length. Iterating shows the positive integer parts of the optimal product differ by at most one. Thus, for \(n=4t+r\), \(Q_n=t^{4-r}(t+1)^r\).

**Step 2: an exact six-run improvement.** Select the balanced product maximizer
\[
(a,b,c,d)=(\underbrace{t+1,\ldots,t+1}_{r\text{ entries}},\underbrace{t,\ldots,t}_{4-r\text{ entries}}).
\]
For \(a,b\ge2\), define the length-\(n\) word
\[
W_{a,b,c,d}=0^{a-1}10\,1^{b-1}0^c1^d.
\]
It has exactly six nonempty runs. Partitioning \(0101\) occurrences according to the run chosen for the second selected symbol gives
\[
\begin{aligned}
c_p(W_{a,b,c,d})
&=(a-1)\bigl((b-1+d)+cd\bigr)+a(b-1)cd,\\
&=abcd+(a-1)(b-1+d)-cd.
\end{aligned}
\]
For the four possible residues, the strict improvement \(\Delta=c_p(W_{a,b,c,d})-Q_n\) is
\[
\Delta=\begin{cases}
t^2-3t+1,&r=0,\\
t^2-t,&r=1,\\
t^2,&r=2,\\
t^2-t,&r=3.
\end{cases}
\]
When \(n\ge9\), the residue cases are respectively \(t\ge3\), \(t\ge2\), \(t\ge2\), and \(t\ge2\), so each displayed integer is strictly positive. Hence \(M_n>Q_n\) for every \(n\ge9\), with a single explicit six-run witness for each \(n\).

**Step 3: the two remaining failures.** At length six, \(Q_6=4\) but the six-run word \(010101\) has five \(0101\)-subsequences. At length seven, \(Q_7=8\) but \(0010101\) has nine. These are directly evaluated by the same position-counting definition. (The length-six failure is also anticipated by the prior literature cited below.) Thus \(M_n>Q_n\) at \(n=6,7\).

**Step 4: the three exceptions.** For length four, five, and eight, the four-run words \(0101\), \(00101\), and \(00110011\) have respectively \(1\), \(2\), and \(16\) occurrences, matching \(Q_4,Q_5,Q_8\). To show these are globally maximal, not just maximal under the run restriction, the standalone exhaustive computation in `verify.py` enumerates every binary word of each length \(4\le n\le8\), counts subsequences by two independent routines, and verifies the global maximum sequence \((1,2,5,9,16)\). In particular the global maxima at the three exceptional lengths are \(1,2,16\). This is a finite complete case check, with full source code, not extrapolation. Combining all steps proves the theorem.

## Verification

Running `python3 verify.py` produces three positive assertions. The checker exhaustively enumerates all \(2^n\) words for each \(4\le n\le8\), counting via a dynamic program and independently by all four-index combinations. It independently computes the maximum over at-most-five-run hosts for \(4\le n\le12\), then tests the six-run count identity through \(n=512\) and the residue positivity through \(n=4096\). The latter finite ranges are stress tests only; the proof for all larger lengths is the four-case exact polynomial argument above.

## Relationship to prior work

Menon and Singh, *Subsequence Frequency in Binary Words* (first arXiv version June 13, 2023), Section 4, show that for targets with at most three runs a target-matching run count can realize every optimum. They explicitly note failure beyond three runs: for an alternating target of length \(\ell\ge4\), the unique optimal host at length \(\ell+2\) is the longer alternating word. Therefore the length-six negative example for the target \(0101\) is previously known, not new. Their accessible Section 4 and concluding questions do not give this theorem's exact exceptional set \(\{4,5,8\}\) or an all-length six-run obstruction from length nine onward.

Burstein, Hästö, and Mansour study packing densities and special classes of patterns in words. Barton proves structural maximizer theorems for clumpy and layered patterns. The target \(0101\), equivalently \(1212\) under alphabet relabeling, is not clumpy and falls outside those hypotheses; general asymptotic packing-density results alone do not determine the exact finite run-budget equality set. The statement has also been checked against relevant scientific research records by comparing claims rather than only matching titles; no corresponding global finite-length threshold was identified.

## Limitations

The theorem does not determine \(M_n\) for arbitrary \(n\ge9\), classify all unrestricted maximizers, or determine their exact minimum run count beyond the lower bound of six. Checks of the available literature cannot exclude an equivalent result hidden in unindexed or inaccessible research. The finite exceptions were verified by a complete executable finite search; the infinite strict inequality is proved algebraically.

## References

1. Krishna Menon and Anurag Singh, *Subsequence Frequency in Binary Words*, arXiv:2306.07870v1, 2023-06-13, Section 4 and concluding remarks. https://arxiv.org/pdf/2306.07870
2. Alexander Burstein, Peter Hästö, and Toufik Mansour, *Packing Patterns into Words*, *Electronic Journal of Combinatorics* **9**(2), R20, 2003. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v9i2r20/pdf/
3. Reid W. Barton, *Packing Densities of Patterns*, *Electronic Journal of Combinatorics* **11**, R80, 2004. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v11i1r80/pdf/
