# Exact dyadic-shift state complexity of all-one-pattern parity sequences

## Finding
For each integer \(m\ge3\), define \(s_m(n)\) to be the parity of the number of overlapping occurrences of \(1^m\) in the binary expansion of the nonnegative integer \(n\). For each integer \(r\ge0\), let \(N_m(r)\) be the number of states in the *smallest complete binary deterministic finite automaton with output* computing \(s_m(n+2^r)\) on every finite least-significant-digit-first binary representation of \(n\), including the empty word and arbitrarily many high-order zeroes.

Define the piecewise integer function
\[
A_m(k)=\begin{cases}
k+1,&0\le k<m,\\
m+1+\min\{m-1,k-m\},&k\ge m.
\end{cases}
\]
Then the exact minimum is
\[
\boxed{N_m(r)=2m+\sum_{k=0}^r A_m(k)+\mathbf1_{\{r=m\}}.}
\]
In particular, after the finite transition range,
\[
\boxed{N_m(r)=2mr+m(5-2m)\quad(r\ge2m-1).}
\]
The isolated correction at \(r=m\) comes from a carry state whose parity one has appeared, but whose zero trailing-run state has not yet appeared.

A stronger structural fact underlying the count is that **no two distinct reachable arithmetic states merge under minimization**: for any fixed nonnegative additive shift \(c\), the natural carry/trailing-ones/parity construction for \(s_m(n+c)\) is already a minimal complete least-significant-digit-first DFAO after unreachable states are removed. This also yields an exact finite reachability algorithm for every shift \(c\), although the displayed explicit formula concerns powers of two.

## Assumptions and scope
All integers and quantifiers are as stated above. A finite binary input \(w=b_0b_1\cdots b_{h-1}\), read left to right, represents \(\sum_{i=0}^{h-1}b_i2^i\). Its empty input represents zero. The symbol \(1^m\) is a run of \(m\) consecutive ones and overlapping occurrences are counted. Adding extra high-order zeroes changes neither the integer nor the required output.

Write \(\nu_2(d)\) for the exponent of two dividing the positive integer \(d\). Set \(t(y)=\nu_2(y+1)\), the number of trailing ones in the usual binary expansion of \(y\), for all \(y\ge0\). All parity sums below are in \(\mathbb F_2\).

## Proof
**1. Arithmetic-state construction.** Fix \(m\ge3\) and a shift \(c\ge0\). After reading \(h\) input digits of value \(v<2^h\), write
\[
c+v=q2^h+B,\qquad 0\le B<2^h.
\]
Let \(p\) be the parity of the occurrences of \(1^m\) in the length-\(h\) binary block \(B\), padded to exactly \(h\) digits, and let \(a\in\{0,\ldots,m-1\}\) be the number of consecutive ones at its high-order end, capped at \(m-1\). The state is the triple \((q,a,p)\). Initially it is \((c,0,0)\). Reading an additional digit \(b\in\{0,1\}\), write \(q+b=2q'+d\), \(d\in\{0,1\}\), and update
\[
(q,a,p)\xrightarrow{b}\begin{cases}
(q',0,p),&d=0,\\
(q',\min\{m-1,a+1\},p+\mathbf1_{\{a=m-1\}}),&d=1.
\end{cases}
\]
This follows from ordinary binary addition and from counting each occurrence at the moment its final one is read. In a terminal state \((q,a,p)\), finish with the remaining binary digits of \(q\), least-significant first, to produce the output. The set of states reachable from \((c,0,0)\) is finite: \(q\) never increases above \(c+1\), drops under repeated zeros, and the other coordinates have only \(2m\) possibilities.

**2. Exact residual functions.** Let \(z\ge0\) represent an arbitrary continuation of the input. The unprocessed high-order part is \(y=z+q\). Only runs of ones crossing the boundary between the completed low block and the binary expansion of \(y\) require correction. The parity of those crossing occurrences is
\[
\chi_m(a,t)=\min\{a,\max\{0,a+t-m+1\}\}\pmod2,
\quad t=t(y).
\]
Indeed, for a terminal run of length \(a\le m-1\) followed by an initial run of \(t\) ones, there are \(\max(0,a+t-m+1)-\max(0,t-m+1)\) crossing copies of \(1^m\), which equals the displayed bounded expression. Thus the residual function from state \((q,a,p)\), evaluated at a continuation of numeric value \(z\), is exactly
\[
F_{q,a,p}(z)=p+s_m(z+q)+\chi_m(a,t(z+q))\pmod2.
\]
The same formula applies to the empty continuation. In particular it shows the constructed automaton computes the required function on *every* finite representation and respects extra terminal zeroes.

**3. Minimality for arbitrary shifts.** We prove that two distinct triples produce different residual functions. Suppose first their first coordinates coincide, say \(q\). There exist arbitrarily large \(z\) with \(z+q\) even, so \(t(z+q)=0\) and all correction terms vanish. Different parity coordinates \(p\) therefore separate the states. If parity coordinates are equal but \(0\le a<b\le m-1\), choose arbitrarily large \(z\) for which \(t(z+q)=m-b\). At this value of \(t\), the crossing count for \(b\) is one and that for \(a\) is zero. Hence those states also differ.

Now assume \(q<q'\), and put \(\Delta=q'-q\ge1\). For every sufficiently large \(K\), the continuation \(z_K=2^K-q'\) is nonnegative. From \((q',a',p')\) the high part is \(2^K\), which contains no copy of \(1^m\) and has zero trailing ones; its residual is the fixed bit \(p'\). From \((q,a,p)\) the high part is \(2^K-\Delta\). Choose \(h\ge0\) with \(2^h\ge\Delta\). The binary expansion of \(2^K-\Delta\) consists of a run of \(K-h\) leading ones followed by a fixed \(h\)-bit tail (for all \(K>h\)). Consequently, once \(K-h\ge m\), the parity \(s_m(2^K-\Delta)\) alternates whenever \(K\) increases by one: its length-dependent contribution is the \(K-h-m+1\) occurrences entirely inside the long initial run; occurrences inside or crossing into the fixed tail contribute a constant. Meanwhile \(t(2^K-\Delta)=K\) if \(\Delta=1\), and equals the fixed number \(\nu_2(\Delta-1)\) if \(\Delta>1\) and \(K\) is sufficiently large. Therefore \(\chi_m(a,t(2^K-\Delta))\) is eventually independent of \(K\). The residual from \(q\) alternates, while the residual from \(q'\) remains fixed. Distinct carry coordinates cannot be equivalent.

Every pair of distinct reachable triples is distinguishable by a finite continuation. Thus the reachability automaton is minimal, rather than merely an upper-bound construction.

**4. Reachable states for a dyadic shift.** Now set \(c=2^r\). After any \(k\) input digits with \(0\le k\le r\), there is no carry from the processed input block into the added power of two. Therefore \(q=2^{r-k}\), and the other two coordinates are exactly those obtained by reading an arbitrary length-\(k\) binary word into the pattern-parity machine. Let \(A_m(k)\) count those distinct pairs \((a,p)\).

For \(k<m\), no occurrence of \(1^m\) fits and every run length from zero to \(k\) occurs, giving \(A_m(k)=k+1\). For \(k\ge m\), parity zero occurs with all \(m\) possible \(a\). Parity one occurs with \(a=m-1\) via \(0^{k-m}1^m\), and occurs with any \(0\le a\le m-2\) precisely when \(k\ge m+1+a\). Necessity follows because a run of \(m\) ones has to be completed and, when \(a<m-1\), must be separated from the final run by a zero. Sufficiency follows from the word \(0^{k-(m+1+a)}1^m01^a\). This proves the stated \(A_m(k)\) formula.

The positive-carry levels with \(q=2^{r-k}\) for \(0\le k<r\) contribute \(\sum_{k=0}^{r-1}A_m(k)\) states. At \(q=1\), the states reachable after \(r\) digits contribute \(A_m(r)\). A further input digit \(1\) emits a zero and leaves \(q=1\), so this level additionally permits \((a,p)=(0,p)\) for every parity appearing among the length-\(r\) words. Such a state is new exactly at \(r=m\): before that parity one is absent; at \(r=m\), it exists only at \(a=m-1\); from \(r=m+1\) onward, \(1^m0\) already supplies the parity-one zero-run state. Therefore the \(q=1\) level has \(A_m(r)+\mathbf1_{\{r=m\}}\) states.

Once \(q\) drops to zero, all \(2m\) pairs \((a,p)\) are reachable: a zero resets the current run, a separated block \(1^m0\) toggles the parity, and a final shorter run chooses \(a\). No other values of \(q\) occur. Since step 3 proves all reachable triples inequivalent, summing their numbers gives the first boxed formula.

For \(k\ge2m-1\), \(A_m(k)=2m\). Evaluating the finite initial sum yields \(\sum_{k=0}^{r}A_m(k)=2mr+m(3-2m)\) for \(r\ge2m-1\); the exceptional indicator is then zero. This proves the second boxed formula.

## Verification
The accompanying file `check_pattern_shift.py` constructs the arithmetic-state automata and independently minimizes their complete Moore transition tables by partition refinement. It checks the formula and full reachability/no-merging for 190 pairs of parameters \((m,r)\) with \(2\le m\le11\) and \(0\le r\le18\), and it checks 194,560 direct outputs against binary pattern counts. It also checks absence of merging for 405 further pairs \((m,c)\) of arbitrary shifts. The complete output is embedded in `check_output.txt`. Run using `python check_pattern_shift.py` from the directory containing this file. Finite tests are corroboration only; the infinite proof is above.

For example, for \(m=3\), the values at \(r=0,1,\ldots,10\) are \(7,9,12,17,21,27,33,39,45,51,57\). For \(m=4\) they are \(9,11,14,18,24,29,36,44,52,60,68\).

## Relationship to prior work
Hendel introduced and analyzed the all-one-pattern parity family, proving the \(2m\)-state unshifted automata and studying word-combinatorial properties. The paper does not state the present dyadic-shift complexity formula or its non-merging criterion. Zantema and Bosma proved general bounds for shifting automatic sequences, while Moradi, Rampersad, and Shallit analyzed the complexity of linear subsequences and gave general most-significant-digit-first shift bounds. Their results imply automaticity and rough constructions, not this exact two-parameter least-significant-digit-first count. Earlier exact special-case calculations for other automatic sequences or the \(m=2\) Rudin–Shapiro pattern do not imply the \(m\ge3\) parity-transition law.

## Limitations
The explicit summation and linear stabilization formula apply to the specified dyadic additive shifts and to least-significant-digit-first *complete* DFAOs that must accept all finite representations. The structural distinctness theorem holds for arbitrary shifts, but no similarly simple closed expression for the count at arbitrary \(c\) is asserted here. The proof does not concern most-significant-digit-first state complexity, other digit patterns, or nonbinary bases. Historic priority cannot be established by negative searches alone; an equivalent result outside inspected primary sources remains possible. The finite tests provide no replacement for the mathematical proof, and no independent external validation has been performed.

## References
- R. J. Hendel, *A Family of Sequences Generalizing the Thue Morse and Rudin Shapiro Sequences*, arXiv:2505.20547, first submitted 26 May 2025; revised under the title *Runs, Squares, Palindromes, and Unbordered Factors of a Family of Binary Pattern Sequences with the All-One Pattern*. https://arxiv.org/abs/2505.20547
- H. Zantema and W. Bosma, *Complexity of automatic sequences*, Information and Computation 288 (2022), 104710. https://www.math.ru.nl/~bosma/pubs/Zantema_Bosma_Complexity_of_Automatic_Sequences.pdf
- D. Moradi, N. Rampersad, and J. Shallit, *Complexity of Linear Subsequences of \(k\)-Automatic Sequences*, arXiv:2512.10017, first submitted 10 December 2025. https://arxiv.org/abs/2512.10017
