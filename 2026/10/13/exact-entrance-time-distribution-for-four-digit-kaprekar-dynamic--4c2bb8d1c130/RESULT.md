# Exact entrance-time distribution for four-digit Kaprekar dynamics in odd bases

## Finding

Let \(B=2m+1\ge5\) be odd. Consider the four-digit Kaprekar subtraction map with leading zeros allowed, omitting the \(B\) constant-digit strings. For a string with decreasingly sorted digits \(a_1\ge a_2\ge a_3\ge a_4\), set \(d=a_1-a_4\), \(e=a_2-a_3\). The induced state space and stable region are
\[
X_B=\{(d,e):1\le d<B,\ 0\le e\le d\},\qquad
T_B=\{(d,e)\in X_B:d>e>0,\ d\equiv e\equiv1\pmod2\}.
\]
Let \(h_B(d,e)\) be the least nonnegative number of Kaprekar steps needed for the difference state to enter \(T_B\). Put \(\delta_m=1\) for even \(m\), and \(\delta_m=0\) for odd \(m\). Then the complete entrance-time distribution among **difference states** is
\[
\begin{aligned}
N_0&=\frac{m(m-1)}2,\\
N_1&=\frac{3m^2-m-2}2+\delta_m,\\
N_2&=4m-\delta_m,\\
N_3&=1.
\end{aligned}
\]
Among **ordered four-digit strings**, with each of the \(B^4-B\) nonconstant strings counted once, the corresponding counts are
\[
\begin{aligned}
W_0&=4m(m-1)(m+1)(m+2),\\
W_2&=16m^3+32m^2+10m-(12m^2+8m)\delta_m,\\
W_3&=4m(3m+2),\\
W_1&=B^4-B-W_0-W_2-W_3.
\end{aligned}
\]
In both ensembles, the **only** state with entrance time \(3\) is \((d,e)=(m+1,0)\). Consequently, for a uniformly random nonconstant four-digit string,
\[
\mathbb P(h_B=0)\longrightarrow\frac14,\quad
\mathbb P(h_B=1)\longrightarrow\frac34,\quad
\mathbb P(h_B=2)\sim\frac2B,\quad
\mathbb P(h_B=3)\sim\frac3{B^2}
\]
as odd \(B\to\infty\). The sharp three-step tail is quadratic-order rare rather than linear-order rare.

## Assumptions and scope

The digits range independently over \(\{0,\ldots,B-1\}\); leading zeros are allowed. The starting difference state, before any subtraction, is counted at time zero. Constant-digit strings are omitted because their difference state is \((0,0)\notin X_B\). The stable region \(T_B\) is the forward-invariant odd unequal region of Chen--Ono--Schwartz--Thakur. Entrance into \(T_B\) is **not** the same as reaching a terminal digit cycle. The result concerns every odd base \(B\ge5\), including composite bases, with no primality assumption.

## Proof

**Step 1: Exact entrance times.** For \(d>e>0\), the first Kaprekar subtraction has the unsorted digit vector
\[
[d,\ e-1,\ B-e-1,\ B-d].
\]
Write \(A=d\), \(C=e-1\), \(D=B-e-1\), \(E=B-d\). Sorting these four digits gives the five possible order patterns in Table 1 of Chen--Ono--Schwartz--Thakur, Section 2.1. In four of the patterns, the new difference pair lies in \(T_B\). In the remaining pattern \(A\ge D\ge E\ge C\), the new pair is
\[
(d-e+1,\ d-e-1),
\]
which lies in \(T_B\) exactly when \(d,e\) have the same parity. The remaining pattern requires \(B-1\le d+e\le B+1\). Since \(B\) is odd, \(d+e\) is odd exactly when \(d,e\) have opposite parity, so a state with \(d>e>0\) requires two steps precisely when \(d+e=B\). All other interior states outside \(T_B\) enter in one step; states already in \(T_B\) require zero steps. The second-step assertion follows directly by substituting the even pair \((d-e+1,d-e-1)\) into the same digit subtraction (including the boundary \((2,0)\)).

For a diagonal state \((d,d)\), the first image is \((h+1,h-1)\), where \(h=|B-2d|\) is odd. It is an even pair and therefore cannot be in \(T_B\); its next image is in \(T_B\). Thus every diagonal state requires exactly two steps.

For \((d,0)\), put \(u=d-1\) and \(v=B-d\). Sorting \([d-1,B-1,B-1,B-d]\) gives
\[
K_B(d,0)=(B-1-\min(u,v),\ B-1-\max(u,v)).
\]
As \(u+v=B-1\) is even, \(u,v\) have equal parity. When \(d\ne m+1\), the two new coordinates are unequal. Even \(d\) gives odd positive coordinates and entrance at time one. Odd \(d\) gives an even pair and entrance at time two (including \(d=1\), for which the first image is \((B-1,0)\)). When \(d=m+1\), the successive states are
\[
(m+1,0)\mapsto(m,m)\mapsto(2,0)\mapsto(B-2,1)\in T_B,
\]
so the entrance time is exactly three. This is its only occurrence.

**Step 2: Count difference states.** There are \(m(m-1)/2\) pairs of distinct positive odd integers \(e<d<B\), giving \(N_0\). The two-step states consist of \(2m\) diagonal pairs, \(m\) positive pairs satisfying \(d>e\) and \(d+e=B\), and the \(m-\delta_m\) odd boundary values \(d\) with \(e=0\) other than \(m+1\). Thus \(N_2=4m-\delta_m\); there is one three-step state, and the remaining states have time one. Because \(|X_B|=m(2m+3)\), this yields the displayed \(N_1\).

**Step 3: Weight each difference state by its number of digit strings.** Fix \((d,e)\in X_B\). The minimum digit has \(B-d\) choices. The middle two digits then yield the following exact multiplicities, by permuting the sorted digit multiset:
\[
w_B(d,e)=(B-d)\begin{cases}
12d-4,&e=0,\\
24(d-e),&0<e<d,\\
6,&e=d.
\end{cases}
\]
For \(e=0\), the two endpoint choices each give \(4\) permutations and the remaining \(d-1\) choices give \(12\). For \(0<e<d\), the two endpoints give \(12\) permutations each and the \(d-e-1\) interior choices give \(24\). For \(e=d\), there are two pairs of equal digits and \(6\) permutations. These cases exhaust all nonconstant four-digit strings.

On time-zero states, write \(d=2i-1\), \(e=2j-1\), \(1\le j<i\le m\). Summing gives
\[
W_0=48\sum_{i=1}^m(m-i+1)i(i-1)=4m(m-1)(m+1)(m+2).
\]
The diagonal time-two states contribute \(6m(2m+1)\). The interior time-two line \(d+e=B\) contributes
\[
24\sum_{e=1}^m e(B-2e)=4m(m+1)(2m+1).
\]
The odd boundary values contribute
\[
\sum_{i=1}^m 16(m-i+1)(3i-2)-\delta_m\,4m(3m+2)
=8m^2(m+1)-\delta_m\,4m(3m+2).
\]
Adding these three expressions gives \(W_2\). The sole three-step state's weight is
\[
W_3=w_B(m+1,0)=m(12m+8)=4m(3m+2).
\]
Subtracting from the \(B^4-B\) nonconstant strings gives \(W_1\). Dividing by \(B^4-B\) and taking \(B=2m+1\to\infty\) proves the four stated probability estimates.

## Verification

Run `python3 verify.py` with Python 3 and the standard library. It independently constructs Kaprekar images by integer digit sorting and subtraction, exhaustively checks every difference state for odd bases \(5\le B\le101\), and checks every nonconstant ordered word in bases \(5,7,9,11\). It compares direct entrance-time counts with the displayed expressions and checks the uniqueness of the three-step state. `verify_output.txt` contains the actual run output. These finite checks are reproducibility tests; the all-base theorem follows from the proof above.

## Relationship to prior work

Chen, Ono, Schwartz and Thakur (2026), Theorem 1.1 and Section 2, prove \(K_B^3(X_B)\subseteq T_B\) and give the casewise difference-pair map. They enumerate terminal-cycle lengths, **not** exact entrance-time frequencies for the starting-state or starting-word ensembles. The present calculation uses their explicit transition formulas to obtain a closed-form, parity-sensitive transient distribution, identifying the sharp exceptional state and the rarity scale of each layer. It should be regarded as a quantitative refinement of the known transition map, not as a new conjugacy theorem. Devlin and Zeng (2021) study distance to nonzero fixed points and their attraction proportions; Kay and Downes-Ward (2022) analyze cycles in odd bases. Those statistics concern terminal cycles or specific attracting fixed points, rather than first entrance into this particular stable region for every odd base.

## Limitations

The frequency law is about entering the forward-invariant region, not distances to the eventual cycle or basin proportions for individual terminal cycles. Its derivation relies on the established explicit four-digit transition map; it does not classify new cycles or extend the result to even bases or different digit lengths. The probability asymptotics use uniform four-digit strings with leading zeros, not uniformly sampled distinct difference states. Literature comparisons may miss unindexed equivalent transient enumerations.

## References

1. E. Chen, K. Ono, R. E. Schwartz, D. S. Thakur, *Four-digit Kaprekar dynamics in odd bases*, arXiv:2606.20439v3 (first posted 2026-06-18), Section 2 and Theorem 1.1, https://arxiv.org/html/2606.20439v3 .
2. P. Devlin, T. Zeng, *Maximum distances in the four-digit Kaprekar process*, Integers 21 (2021), A97, https://math.colgate.edu/~integers/v97/v97.pdf .
3. A. Kay, K. Downes-Ward, *Fixed Points and Cycles of the Kaprekar Transformation: 1. Odd Bases*, Journal of Integer Sequences 25 (2022), Article 22.6.7, https://cs.uwaterloo.ca/journals/JIS/VOL25/Kay/kay5.pdf .
