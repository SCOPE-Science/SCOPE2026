# Dyck-factor lengths in the regular paperfolding word
## Finding
Let \(\mathbf p=p_1p_2\cdots\) be the regular paperfolding word in the convention
\[
p_n=
\begin{cases}
0,&\text{if the odd part of }n\text{ is }1\pmod 4,\\
1,&\text{if the odd part of }n\text{ is }3\pmod 4.
\end{cases}
\]
Treat \(0\) as a left parenthesis and \(1\) as a right parenthesis.

Then \(\mathbf p\) has a nonempty Dyck factor of length \(L\) if and only if
\[
L=2^k-2^i
\]
for integers
\[
1\le i<k.
\]

For every such pair, a canonical witness is
\[
p_{2^i}p_{2^i+1}\cdots p_{2^k-1}.
\]

Thus the natural parity-corrected form of the published paperfolding conjecture is true. The printed statement allows \(i=0\), but those values give odd lengths, whereas every nonempty Dyck word has even length.

## Assumptions and scope
A binary word is Dyck when it has equally many \(0\)'s and \(1\)'s and every prefix has at least as many \(0\)'s as \(1\)'s.

The theorem uses the displayed standard regular-paperfolding convention. Complementing the entire infinite word changes the Dyck-factor problem because it swaps left and right parentheses, so the convention is part of the statement.

The result classifies possible lengths, not the number of Dyck factors at a given allowed length and not their nesting levels.

## Proof
Put
\[
a_n=1-2p_n\in\{+1,-1\},
\qquad
S(N)=\sum_{n=1}^N a_n,
\]
with \(S(0)=0\). From the odd-part definition,
\[
a_{2m}=a_m,
\qquad
a_{4m+1}=1,
\qquad
a_{4m+3}=-1.
\]
Consequently
\[
S(2m)=S(m)+\mathbf 1_{m\text{ odd}},
\]
and
\[
S(2m+1)=S(m)+\mathbf 1_{m\text{ even}}.
\]

For \(N\ge1\), let \(R(N)\) be the number of runs of equal bits in the standard binary expansion of \(N\), and set \(R(0)=0\). Appending a binary \(0\) creates a new run exactly when the preceding integer is odd, while appending a binary \(1\) creates a new run exactly when it is even. Hence \(R\) satisfies the same two recurrences and the same initial values as \(S\). Therefore
\[
S(N)=R(N)
\qquad(N\ge0).
\]

A factor
\[
p_{x+1}p_{x+2}\cdots p_y
\]
is Dyck exactly when
\[
R(n)\ge R(x)\quad(x\le n\le y),
\qquad
R(y)=R(x).
\]
Its length is \(L=y-x\).

We first prove existence. If \(1\le i<k\), take
\[
x=2^i-1,
\qquad
y=2^k-1.
\]
Both binary expansions consist entirely of \(1\)'s, so
\[
R(x)=R(y)=1.
\]
Every positive integer has at least one binary run, hence \(R(n)\ge1\) throughout the interval. Thus the factor from position \(2^i\) through \(2^k-1\) is Dyck and has length \(2^k-2^i\).

For the converse, suppose \(x<y\) satisfy the displayed Dyck conditions and put \(h=R(x)=R(y)\).

First assume \(x\) and \(y\) have the same binary length. Let \(P\) be their longest common binary prefix. Then for some equal-length suffixes \(X,Y\),
\[
x=P0X,
\qquad
y=P1Y.
\]
The suffixes after the first differing bit have a common length \(r\). If \(r=0\), changing the final bit changes the run count by one, contradicting \(R(x)=R(y)\). Thus \(r\ge1\).

The two boundary integers
\[
u=P0\underbrace{11\cdots1}_{r},
\qquad
v=P1\underbrace{00\cdots0}_{r}
\]
lie between \(x\) and \(y\). Since their run counts cannot fall below \(h\), the suffix \(0X\) can have at most one internal bit transition, and the suffix \(1Y\) can have at most one. Comparing the equal endpoint run counts gives exactly two possibilities, according to the last bit of \(P\).

If \(P\) ends in \(0\), then
\[
0X=0^a1^{d-a},
\qquad
1Y=1^d
\]
for some \(1\le a<d\). If \(P\) ends in \(1\), then
\[
0X=0^d,
\qquad
1Y=1^a0^{d-a}
\]
for some \(1\le a<d\). In either case the common high-order prefix cancels in the difference and
\[
y-x=(2^a-1)2^{d-a}=2^d-2^{d-a}.
\]
This is of the required form with \(1\le d-a<d\).

It remains to consider endpoints of different binary lengths. Then the interval crosses some number \(2^m-1\), whose binary expansion is all \(1\)'s and hence has run count \(1\). The Dyck condition forces \(h=1\). The positive integers with exactly one binary run are precisely
\[
2^j-1.
\]
Therefore
\[
x=2^i-1,
\qquad y=2^k-1
\]
for integers \(1\le i<k\), and once again
\[
L=y-x=2^k-2^i.
\]
This proves the classification.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier independently constructs the regular paperfolding prefix in two ways: from the odd-part definition and from the recursion
\[
W_{r+1}=W_r\,0\,\overline{W_r^R},
\]
and checks agreement through length \(32767\).

It verifies
\[
S(N)=R(N)
\]
for every \(1\le N\le10^6\). It then exhausts all endpoint pairs with \(0\le x<y\le4096\) until the binary-run path drops below its starting level, confirming that the complete observed Dyck-length set is exactly the set of integers \(2^k-2^i\) with \(1\le i<k\). Finally, it directly checks the canonical factors for all \(2\le k\le17\).

These computations stress-test the argument; the infinite theorem follows from the binary-run proof above.

## Relationship to prior work
Mol, Rampersad, and Shallit explicitly conjecture that the paperfolding sequence has a Dyck factor of length \(n\) exactly at differences of two powers of two. Their printed range is \(0\le i<k\). Since nonempty Dyck words necessarily have even length, the \(i=0\) branch cannot be literal; the mathematically natural corrected range is \(1\le i<k\).

The theorem above proves that corrected statement completely. Its mechanism is not an automaton computation: the cumulative parenthesis balance of the regular paperfolding word is exactly the number of runs in the binary expansion of the endpoint, reducing the Dyck-factor question to a short binary-interval classification.

The same authors' standard Walnut convention for the paperfolding sequence is
\[
001001100011011\cdots,
\]
matching the odd-part definition in this result.

Targeted searches for the conjecture number, paperfolding Dyck factors, the power-difference length set, and the binary-run formulation did not locate a published proof or equivalent classification.

## Limitations
The theorem fixes the regular paperfolding convention explicitly. It does not classify Dyck factors for arbitrary members of the uncountable family of paperfolding sequences.

It determines exactly which lengths occur, but not the number of factors or their nesting-level distribution at each allowed length.

An unindexed note or unpublished proof could contain the same binary-run argument.

## References
1. L. Mol, N. Rampersad, and J. Shallit, “Dyck Words, Pattern Avoidance, and Automatic Sequences,” arXiv:2301.06145v1, first public version 2023-01-15; WORDS 2023; Communications in Mathematics 33 (2025), no. 2, DOI 10.46298/cm.12695.
2. J. Shallit, *The Logical Approach to Automatic Sequences: Exploring Combinatorics on Words with Walnut*, Cambridge University Press, 2023, Chapter 12, “Paperfolding sequences,” DOI 10.1017/9781108775267.014.
