# Exact three-one Cusick bias spectrum and sharp minimizers

## Finding

Let \(s_2(m)\) be the number of ones in the binary expansion of a nonnegative integer \(m\). For every positive integer \(t\), define the natural density
\[
 c_t=\lim_{X\to\infty}\frac{1}{X}\#\{0\le n<X:s_2(n+t)\ge s_2(n)\}.
\]
If \(s_2(t)=3\), write uniquely
\[
 t=2^r(1+2^a+2^{a+b}),\qquad r\ge0,\quad a,b\ge1.
\]
Then \(c_t\) is unchanged when either gap \(a\) or \(b\) is replaced by \(\min(a,4)\) or \(\min(b,4)\), respectively. Its full set of values, as \(t\) ranges over *all* three-one shifts, is
\[
 \left\{\frac{19}{32},\frac58,\frac{41}{64},\frac{21}{32},\frac{43}{64}\right\}.
\]
The complete table has rows \(\min(a,4)=1,2,3,4\), and columns \(\min(b,4)=1,2,3,4\):

| \(\min(a,4)\) | \(1\) | \(2\) | \(3\) | \(4\) |
|---|---|---|---|---|
| \(1\) | \(43/64\) | \(19/32\) | \(41/64\) | \(21/32\) |
| \(2\) | \(19/32\) | \(5/8\) | \(5/8\) | \(41/64\) |
| \(3\) | \(41/64\) | \(5/8\) | \(5/8\) | \(41/64\) |
| \(4\) | \(21/32\) | \(41/64\) | \(41/64\) | \(21/32\) |

In particular,
\[
\min_{s_2(t)=3}c_t=\frac{19}{32},
\qquad
F(3):=\inf_{s_2(t)=3}\left(c_t-\frac12\right)=\frac3{32}.
\]
The minimum is attained **if and only if** \(t=11\cdot2^r\) or \(t=13\cdot2^r\) for some integer \(r\ge0\).

## Assumptions and scope

All integers \(n\) used in the density are nonnegative and \(t\) is fixed and positive. The theorem covers every shift with exactly three binary ones, without imposing any upper bound on the gaps or on \(t\). Density is natural density of nonnegative integers. The uniform binary-digit probability measure agrees with natural density on every finite union of residue classes modulo a power of two. The result does not concern other Hamming weights.

## Proof

**Carry interpretation.** In ordinary base-two addition of \(n\) and \(t\), let \(e_i\in\{0,1\}\) be the binary digit of \(t\) at column \(i\), \(x_i\in\{0,1\}\) the digit of \(n\), and \(h_i\in\{0,1\}\) the incoming carry, with \(h_0=0\). The outgoing carry is
\[
 h_{i+1}=\left\lfloor\frac{x_i+e_i+h_i}{2}\right\rfloor.
\]
The identity obtained by summing digit equations over all columns (or by Kummer's theorem and Legendre's formula) is
\[
 s_2(n+t)-s_2(n)=s_2(t)-\sum_{i\ge0}h_{i+1}.
\]
For a three-one shift, the defining event for \(c_t\) is therefore *exactly* the event that at most three outgoing carries occur.

**Finite exact recurrence.** Suppose the highest nonzero digit of \(t\) is at column \(B\). Any history with an outgoing carry at column \(B+3\) (that is, \(h_{B+4}=1\)) must have outgoing carries at columns \(B,B+1,B+2,B+3\), since every column above \(B\) contains a zero in \(t\). Such a history already has at least four carries, so it is excluded. Thus, for histories with at most three carries, no carry survives past column \(B+3\), and the event is determined completely by the lower \(B+4\) digits of \(n\).

Let \(A_i(h,j)\) count length-\(i\) binary words of the lower digits of \(n\) for which the incoming carry at column \(i\) is \(h\) and exactly \(j\le3\) outgoing carries have already occurred. Set \(A_0(0,0)=1\), with all other entries zero. At each column \(i\), for both choices \(x\in\{0,1\}\), put
\[
 h'=\left\lfloor\frac{x+e_i+h}{2}\right\rfloor,
 \qquad j'=j+h'.
\]
If \(j'\le3\), add \(A_i(h,j)\) to \(A_{i+1}(h',j')\); otherwise discard it. This is an integer-only recurrence on eight states. After \(L=B+4\) columns,
\[
 c_t=2^{-L}\sum_{j=0}^3 A_L(0,j).
\]
This is an *exact density formula*, not an approximate finite-range count: the carry-budget argument proves the periodic cylinder reduction for every \(t\) in scope.

**Unbounded gaps reduce to four.** Consider two successive nonzero digits of \(t\), at positions \(u\) and \(u+d\). When \(d\ge4\), all three intervening digits at positions \(u+1,u+2,u+3\) are zeros. A surviving carry emerging from column \(u\) and persisting to the end of those three zero columns would have contributed at least four outgoing carries, so all histories counted by the recurrence have carry zero after column \(u+3\). Every further zero column before position \(u+d\) has zero incoming carry and leaves it zero for either input digit \(x\); summing over both input choices multiplies the integer count and total number of input words by the same factor of two. Therefore inserting or deleting any zeros beyond these three does not change the probability of at most three carries. This proves that \(c_t\) depends only on the clipped gaps \(\min(a,4)\), \(\min(b,4)\).

**Complete table and extremizers.** Set \(r=0\), \(1\le a,b\le4\), and \(t=1+2^a+2^{a+b}\). Run the displayed eight-state recurrence through column \(a+b+3\), normalizing by \(2^{a+b+4}\). Each of the sixteen rational outputs is displayed in the table in the Finding section; `verify.py` implements precisely these integer transitions and checks every entry. Because of the preceding proved clipping lemma and the elementary invariance \(c_{2t}=c_t\), these sixteen cases exhaust every positive three-one shift. The unique table cells with minimum \(19/32\) are \((a,b)=(1,2)\) and \((2,1)\), whose odd shifts are \(11\) and \(13\). All five reported values occur. Subtracting \(1/2\) gives \(F(3)=3/32\), with precisely the stated extremizers.

## Verification

The standalone Python 3 standard-library program `verify.py` calculates the sixteen table entries by three independent methods: the finite carry recurrence above, finite deconvolution of digit-sum correlation measures using exact rational arithmetic, and direct residue enumeration modulo the proven period. It then compares 256 further gap pairs \(1\le a,b\le16\) using the first two methods. It verifies each table entry and the set of five attained values; the saved output is `verification_output.txt`. These computations are exhaustive for the sixteen canonical cases *because the gap-clipping proof makes them exhaustive*; the 256 extra comparisons are diagnostic checks, not a substitute for that proof.

For the second method, let \(P_1=\delta_0\), \(P_{2u}=P_u\), and \(P_{2u+1}=\tfrac12\tau_{+1}P_u+\tfrac12\tau_{-1}P_{u+1}\), with \(\tau_j\) translation by \(j\). These finite measures deconvolve the digit-sum law as \(\mu_t=\mu_1*P_t\); hence
\[
 c_t=\sum_{v\ge-1}P_t(v)\bigl(1-2^{-v-2}\bigr).
\]
This independent recurrence reproduces the sixteen carry-derived rational outputs. The finite deconvolution is documented in Cheng's earlier first-exit paper.

## Relationship to prior work

Cheng's August 2026 paper [1] defines the exact fixed-weight extremal function \(F(k)\) and determines its asymptotic as \(k\to\infty\); its asymptotic result does not identify the exact minimum or extremizers at \(k=3\). Cheng's June 2026 paper [2] proves a universal positive lower bound for all shifts and gives a stopped-tree law, including an explicit finite distribution for the isolated shift \(11\); the present result does **not** claim that the single coefficient \(c_{11}\) or its computation is new. Spiegelhofer and Wallner [3] developed the binary correlation recurrences and many-block asymptotics. Drmota, Kauers and Spiegelhofer [4] provided a digit-sum correlation recurrence, a table for small shifts, numerical values for a large bounded set of shifts, and equivalent formulations via binomial valuations and congruence zeros. None of these inspected statements is an all-gap exact classification at binary weight three or a sharp proof of \(F(3)\). The present contribution is the finite carry-budget gap theorem plus complete all-shift exact classification with extremizers.

## Limitations

Only Hamming weight three is classified. The first-exit and digit-sum recurrences are known tools and the exact values for some small shifts are already tabulated or implicit in them; those isolated values are not claimed as new. Search and full-text comparisons may miss an equivalent previous global classification in unindexed work. The computations independently check the table but do not certify novelty or provide a result for arbitrary higher weight. Independent audit has not been performed.

## References

1. Kaimin Cheng, *Sharp extremal asymptotics for Cusick's sum-of-digits bias at fixed Hamming weight*, arXiv:2608.25899v1 (first publicly available 2026-08-26), https://arxiv.org/abs/2608.25899.
2. Kaimin Cheng, *A first-exit proof of Cusick's sum-of-digits conjecture*, arXiv:2606.23398v1 (first publicly available 2026-06-22), https://arxiv.org/abs/2606.23398.
3. Lukas Spiegelhofer and Michael Wallner, *The binary digits of n+t*, arXiv:2005.07167v3 (first version 2020-05-14), https://arxiv.org/abs/2005.07167.
4. Michael Drmota, Manuel Kauers and Lukas Spiegelhofer, *On a Conjecture of Cusick Concerning the Sum of Digits of n and n+t*, arXiv:1509.08623v2 (first version 2015-09-29), https://arxiv.org/abs/1509.08623.
