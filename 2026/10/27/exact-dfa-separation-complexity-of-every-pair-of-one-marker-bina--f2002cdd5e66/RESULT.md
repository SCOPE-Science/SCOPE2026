# Exact DFA separation complexity of every pair of one-marker binary words

## Finding

For every integer \(n\ge2\) and \(0\le i<j<n\), write
\[
x=0^i1\,0^{n-i-1},\qquad y=0^j1\,0^{n-j-1},\qquad d=j-i.
\]
A complete binary deterministic finite automaton (DFA) *separates* the words if it accepts one and rejects the other. Let \(s(x,y)\) be the minimum possible state count, and put \(p(d)=\min\{m\in\mathbb Z:m\ge2,\ m\nmid d\}\). Then
\[
\boxed{s(x,y)=\min\{p(d),\ i+3,\ n+1-j\}.}
\]
This is an exact classification with no asymptotic or sufficient-padding hypothesis.

In particular, for \(S_1(n)=\max_{0\le i<j<n}s(x,y)\),
\[
S_1(n)=\max_{1\le d<n}\min\left\{p(d),\left\lfloor\frac{n-d+4}{2}\right\rfloor\right\}.
\]
Writing \(L_m=\operatorname{lcm}(1,\ldots,m)\), for every integer \(k\ge3\),
\[
\boxed{S_1(n)\ge k\ \Longleftrightarrow\ n\ge L_{k-1}+2k-4.}
\]
For \(n\ge2\), \(S_1(n)\ge2\); the first lengths requiring respectively three, four, five and six states are \(4,10,18,68\). The standard fact \(\log L_m\sim m\) gives \(S_1(n)\sim\log n\), with natural logarithm.

## Assumptions and scope

Indices are zero-based. Exactly one occurrence of symbol \(1\) appears in each word; both inputs have equal length \(n\). The alphabet is \(\{0,1\}\); transition maps are total, no promise on input words or acceptance beyond the two tested words is imposed. Automata have one initial state and an arbitrary subset of final states. Distinct terminal states are necessary and sufficient for separation because we can choose the final set accordingly. The state budget includes the initial and all auxiliary states, and unreachable states are unnecessary. We make no claim about two-marker words or the general maximum over arbitrary binary pairs.

## Proof

Let \(d=j-i\) and \(r=n-1-j\), so the trailing zero suffixes have lengths \(r+d\) for \(x\) and \(r\) for \(y\). Denote by \(f\) the zero-transition, by \(g\) the one-transition and by \(q\) the start state. Their terminal states are
\[
f^{r+d}g(f^i(q))\quad\text{and}\quad f^r g(f^{i+d}(q)).
\]

**Three constructions.** (1) On a directed zero-cycle of length \(p(d)\), let the one-transition reset every state to a fixed point on the cycle. The terminal states differ by a cyclic displacement of \(d\), hence differ because \(p(d)\nmid d\). (2) On \(i+3\) states \(q_0,\ldots,q_i,A,B\), let the zero-transition trace \(q_0\to\cdots\to q_i\to A\), fixing \(A,B\), and define \(g(q_i)=B\), \(g(A)=A\). Starting at \(q_0\), the marker in \(x\) is read at \(q_i\), while the later marker in \(y\) is read at \(A\); the terminal states remain \(B,A\). Unspecified one-transitions can be arbitrary. (3) On \(r+2\) states \(0,\ldots,r+1\), let \(f(t)=\min(t+1,r+1)\) and let \(g\) send every state to \(0\). The terminal states are respectively \(r+1\) and \(r\), since \(d\ge1\). All three constructions separate the pair, proving the claimed upper bound.

**Lower bound.** Fix a \(k\)-state DFA with \(k<\min\{p(d),i+3,r+2\}\). Every integer \(\ell\) with \(1\le\ell\le k\) divides \(d\): this follows from \(k<p(d)\), the definition of the least nondivisor, and the trivial case \(\ell=1\). For any map \(f\) on \(k\) points, every trajectory eventually enters a directed cycle of length at most \(k\), with transient length at most \(k-1\). Since every such cycle length divides \(d\),
\[
f^{r+d}=f^r\quad\text{on all states},\qquad r\ge k-1.
\]
Consider the zero-trajectory of \(q\). If its transient length is at most \(k-2\), then \(i\ge k-2\), so \(f^i(q)\) is already periodic with period dividing \(d\). Thus \(f^i(q)=f^{i+d}(q)\); after the same one-transition and equal final zero maps the two terminal states coincide.

Otherwise the trajectory has the largest possible transient length \(k-1\). Its \(k-1\) transient points are distinct and leave exactly one state for the periodic cycle; thus the cycle consists of a single fixed point \(a\). All \(k\) points lie on this same chain into \(a\), and hence \(f^{k-1}\) is the constant map with value \(a\). As \(r\ge k-1\), both \(f^r\) and \(f^{r+d}\) are constant with value \(a\), independently of the one-transition. The terminal states again coincide. No \(k\)-state DFA with \(k\) below the claimed minimum separates. The lower bound and exact equality follow, including \(k=1\).

**Sharp global thresholds.** Fix the gap \(d\) and write \(j=i+d\). The largest possible value, as \(i\) ranges over \(0,\ldots,n-d-1\), of the lesser boundary budget is
\[
\max_i\min\{i+3,n+1-i-d\}=\left\lfloor\frac{n-d+4}{2}\right\rfloor.
\]
Thus \(S_1(n)\ge k\) for \(k\ge3\) exactly if some \(d<n\) satisfies \(p(d)\ge k\) and \(n-d\ge2k-4\). The first condition is equivalent to divisibility of \(d\) by every integer \(1,\ldots,k-1\), hence to \(L_{k-1}\mid d\). The smallest positive such \(d\) is \(L_{k-1}\), yielding \(n\ge L_{k-1}+2k-4\). The case \(k=2\) follows from distinctness of the two words. The asymptotic follows from the classical estimate \(\log\operatorname{lcm}(1,\ldots,m)\sim m\).

## Verification

The standalone `one_marker_separation_checker.py` reconstructs the formula, exhausts all complete binary transition tables for state budgets up to three on small lengths (274 input/budget triples), separately enumerates all zero-transition functions and tests all possible one-transition endpoints for budgets up to five (9,231 triples), and checks sharp global thresholds through length 200. Running `python3 one_marker_separation_checker.py` yields:

```
CHECK_OK full_transition_tests 274 all_zero_transition_tests 9231 sharp_threshold_lengths 199
```

These finite checks corroborate but do not substitute for the preceding all-length proof. The attached checker is dependency-free and does not require external scientific data.

## Relationship to prior work

Robson (1989) proved asymptotic upper bounds for separating arbitrary strings. Demaine, Eisenstat, Shallit and Wilson (2011), *Remarks on Separating Words*, study minimum-state DFA separation and give elementary boundary constructions (their Propositions 4 and 5) matching two of the three upper-bound mechanisms; they also give logarithmic lower-bound examples involving widely separated markers, but not the present all-index exact identity. Ebrahimnejad (2016) analyzes reversal gaps and automaton-tail lower bounds; it does not state this parameterized classification. Nicol (2026), *Further Remarks on Separating Words*, supplies different bounds in terms of runs of mismatches, reversals and shifts; its general statements do not determine the exact value for each pair of one-marker words. Comparison here is by claimed implication and hypothesis, not by titles alone.

## Limitations

The result concerns only equal-length, weight-one binary pairs and unrestricted complete DFAs. It does not classify optimal automata up to isomorphism, nor establish a new upper bound for arbitrary words. Although relevant full texts were examined, unpublished, unindexed or older sources (including the 1986 work of Goralčík and Koubek) may contain an equivalent statement. This literature assessment is a self-review rather than independent historical-priority verification.

## References

1. J. M. Robson, “Separating Strings with Small Automata,” *Information Processing Letters* **30** (1989), 209–214; https://gwern.net/doc/cs/algorithm/1989-robson.pdf .
2. E. D. Demaine, S. Eisenstat, J. Shallit, and D. A. Wilson, “Remarks on Separating Words,” arXiv:1103.4513, first posted March 23, 2011; https://arxiv.org/abs/1103.4513 .
3. E. Ebrahimnejad, “On the Gap Between Separating Words and Their Reversals,” arXiv:1605.04835 (2016); https://arxiv.org/abs/1605.04835 .
4. J. Nicol, “Further Remarks on Separating Words,” arXiv:2608.30928 (2026); https://arxiv.org/abs/2608.30928 .
