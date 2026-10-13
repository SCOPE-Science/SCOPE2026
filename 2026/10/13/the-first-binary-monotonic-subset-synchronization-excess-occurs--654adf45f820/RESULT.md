# The first binary monotonic subset-synchronization excess occurs at nine states
## Finding
Let \(T_2(n)\) be the maximum, over all \(n\)-state binary monotonic deterministic automata and all synchronizable subsets of their states, of the length of a shortest word synchronizing the chosen subset.

Then
\[
T_2(n)=n-1\qquad\text{for }1\le n\le8,
\]
but
\[
T_2(9)=9.
\]
Thus nine states are the first size at which binary monotonic subset synchronization requires more than \(n-1\) letters.

After relabeling a preserved order as
\[
0<1<\cdots<8,
\]
there are exactly four ordered pairs of nondecreasing letter maps attaining \(T_2(9)=9\). They form one orbit under interchange of the two letters and reversal of the state chain.

One representative is
\[
a=(0,0,1,2,4,4,5,5,8),\qquad
b=(0,2,3,4,4,6,7,8,8).
\]
For the state pair \(\{1,6\}\), a shortest synchronizing word is
\[
\mathtt{babbaabbb},
\]
of length \(9\).

The second unordered normalized representative is
\[
a=(0,0,1,2,4,4,5,6,8),\qquad
b=(0,3,3,4,4,6,7,8,8),
\]
with hard pair \(\{2,7\}\). It is obtained from the first by reversing the chain and interchanging the letters.

## Assumptions and scope
An automaton is monotonic when there exists a linear order of the states preserved by every input letter. After relabeling one preserved order as \(0<1<\cdots<n-1\), each letter is exactly a nondecreasing map from this chain to itself.

A subset is synchronizable when some word maps all of its states to one state. The threshold \(T_2(n)\) maximizes the shortest such word over every binary monotonic automaton and every synchronizable nonempty subset.

The enumeration is normalized by a chosen preserved order. The statement that exactly four ordered extremal transition pairs occur is therefore a count in this normalized chain model, not a count of abstract automata with all possible preserved orders.

## Proof
For any monotonic word map \(f\) and any subset \(S\),
\[
f(\min S)\le f(s)\le f(\max S)\qquad(s\in S).
\]
Hence a word synchronizes \(S\) if and only if it synchronizes the pair \(\{\min S,\max S\}\), and the shortest lengths are equal. Therefore it is enough to consider state pairs.

For a fixed \(n\), a nondecreasing self-map of an \(n\)-element chain is determined by a weakly increasing length-\(n\) sequence with entries in \(\{0,\ldots,n-1\}\), so there are
\[
\binom{2n-1}{n}
\]
possible letter maps. In particular, for \(n=9\) there are \(24310\) maps and
\[
24310^2=590976100
\]
ordered binary transition pairs.

The verifier quotients only by exchanging the two input letters during exhaustive search, so every ordered automaton is represented. For each unordered pair of letter maps it constructs the pair automaton on states
\[
(i,j),\qquad 0\le i\le j<n.
\]
The diagonal pairs are synchronized. Reverse breadth-first search from all diagonal pairs gives, for every state pair, its exact shortest synchronization length or detects that it is not synchronizable.

Exhaustion gives
\[
T_2(1),\ldots,T_2(9)=0,1,2,3,4,5,6,7,9.
\]
At \(n=9\), exactly two unordered normalized letter pairs contain a state pair at distance \(9\); neither uses equal letters, hence they yield exactly four ordered transition pairs.

For the displayed first representative, the hard pair follows the trajectory
\[
(1,6)\to(2,7)\to(1,5)\to(2,6)\to(3,7)\to(2,5)\to(1,4)\to(2,4)\to(3,4)\to(4,4)
\]
under \(\mathtt{babbaabbb}\). Reverse breadth-first distance \(9\) proves that no shorter word synchronizes \(\{1,6\}\).

Finally, conjugating both maps by the reversal \(i\mapsto8-i\) sends the first unordered pair to the second with the two letters exchanged. Thus the four ordered normalized extremals form one orbit under chain reversal and letter interchange.

## Verification
Run `python3 verify.py` beside `census.cpp` and `certificate.json`.

The compiled census generates all nondecreasing letter maps for every \(1\le n\le9\), checks the binomial map counts, and exhausts every binary transition pair up to harmless letter interchange. It computes exact pair-synchronization distances by reverse breadth-first search and reproduces the threshold sequence
\[
0,1,2,3,4,5,6,7,9.
\]

At \(n=9\) the same census isolates exactly the two unordered normalized extremals stated above. The Python verifier independently performs a forward breadth-first search for the displayed witness pair, obtaining the unique stored shortest witness \(\mathtt{babbaabbb}\) and the stated trajectory. It also checks the chain-reversal relation between the two normalized extremals.

## Relationship to prior work
Ryzhikov and Shemyakov study exactly subset synchronization in monotonic automata. They prove, for \(n\ge8\), a general upper bound of
\[
\frac{(n-2)^2}{4}
\]
on the length of a shortest word synchronizing a subset, and give a three-letter family nearly attaining that bound. For binary monotonic automata they give a quadratic lower-bound family on \(4m+3\) states whose selected subset requires at least \(m^2\) letters.

Those results establish asymptotic quadratic behavior but do not determine the exact binary small-state thresholds or the first state size at which the linear value \(n-1\) fails. The present finite classification fills that boundary: equality with \(n-1\) survives through eight states and first fails at nine.

A later study of weakly acyclic automata cites the monotonic result only at the asymptotic level and likewise does not give a binary monotonic small-state table. Searches using the exact nine-state value, the first-excess formulation, fixed-binary-alphabet terminology, and the explicit witness located no published exact boundary or extremal census.

## Limitations
The result is exact only through nine states. It does not determine \(T_2(n)\) for \(n\ge10\), nor a closed formula for binary monotonic automata.

The extremal count is made after choosing and normalizing one preserved state order. Abstract automata that admit multiple preserved orders can have multiple normalized presentations.

An unindexed computational note could contain the same small-state census even though the inspected primary and follow-up literature do not report it.

## References
1. A. Ryzhikov and A. Shemyakov, “Subset Synchronization in Monotonic Automata,” arXiv:1703.06356v1, first public version 2017-03-18; Fundamenta Informaticae 162(2–3) (2018), 205–221, DOI 10.3233/FI-2018-1721.
2. A. Ryzhikov, “Synchronization Problems in Automata without Non-trivial Cycles,” Theoretical Computer Science 787 (2019), 77–88, DOI 10.1016/j.tcs.2018.12.026.
