# Weight rigidity for binary Keith numbers
## Finding
Let \(N\ge2\) have binary expansion
\[
N=(b_1b_2\cdots b_n)_2,\qquad b_1=1,
\]
and let
\[
w=b_1+\cdots+b_n
\]
be its Hamming weight. Form the \(n\)-step Keith recurrence
\[
K_1=b_1,\ldots,K_n=b_n,\qquad
K_m=K_{m-1}+\cdots+K_{m-n}\quad(m>n).
\]

If \(w=1\), then \(N=2^{n-1}\), and every such power of two is a binary Keith number.

Assume \(w\ge2\). Put
\[
c=\lceil\log_2 w\rceil,\qquad L=2^c,
\]
and perform the Euclidean division
\[
2^{n-c}w=(L+1)P+S,\qquad 0\le S\le L.
\]
Then there is a binary Keith number with bit length \(n\) and Hamming weight \(w\) if and only if
\[
S<L
\]
and
\[
s_2(P)+s_2(S)=w,
\]
where \(s_2\) denotes binary Hamming weight. In that case the number is unique and is
\[
N=PL+S.
\]

Consequently, for every \(n\ge2\), there is at most one non-power-of-two binary Keith number of each Hamming weight \(w\in\{2,\ldots,n\}\), and together with the power \(2^{n-1}\) there are at most \(n\) binary Keith numbers with \(n\) bits.

If \(B_2(x)\) counts binary Keith numbers \(N\le x\), and
\[
h=\lfloor\log_2x\rfloor+1,
\]
then
\[
B_2(x)\le\sum_{n=1}^{h}n=\frac{h(h+1)}2.
\]
In particular,
\[
B_2(x)=O((\log x)^2).
\]

## Assumptions and scope
The binary Keith definition is the standard base-\(2\) specialization: the full binary digit string initializes a recurrence in which every later term is the sum of the preceding \(n\) terms. The convention \(n\ge2\) is used for nontrivial Keith numbers; including the one-bit value \(1\) changes no estimate.

The characterization is for all bit lengths and all Hamming weights. It is not a finite enumeration and does not assume any unproved distributional statement.

## Proof
For \(1\le k\le n\), subtract the two consecutive recurrence sums. This gives
\[
K_{n+k+1}=2K_{n+k}-b_k.
\]
Since
\[
K_{n+1}=w,
\]
an induction yields
\[
K_{n+j}=2^{j-1}w-P_{j-1}\qquad(1\le j\le n+1),
\]
where
\[
P_{j-1}=(b_1b_2\cdots b_{j-1})_2
\]
and \(P_0=0\).

Suppose first that \(w\ge2\). After \(K_{n+1}=w\), the recurrence is strictly increasing, because
\[
K_{m+1}=2K_m-b_k>K_m
\]
whenever \(K_m\ge2\). Moreover,
\[
K_{2n+1}=2^nw-N>N,
\]
since \(w\ge2\) and \(N<2^n\). Therefore, if \(N\) is Keith, then
\[
N=K_{n+j}
\]
for a unique \(j\in\{1,\ldots,n\}\).

At such an occurrence,
\[
N=2^{j-1}w-P_{j-1}.
\]
Because
\[
0\le P_{j-1}<2^{j-1},
\]
we get
\[
2^{j-1}(w-1)<N\le2^{j-1}w.
\]
Together with
\[
2^{n-1}\le N<2^n,
\]
this pins down the recurrence offset uniquely. If
\[
c=\lceil\log_2w\rceil,
\]
then necessarily
\[
j=n-c+1.
\]

Now write the binary expansion of \(N\) at that cut as
\[
N=PL+S,\qquad L=2^c,
\]
where \(P\) is the prefix of length \(n-c\) and \(S\) is the numerical value of the final \(c\) bits. Thus \(0\le S<L\). Substituting \(j=n-c+1\) into the recurrence formula gives
\[
PL+S=2^{n-c}w-P,
\]
or equivalently
\[
2^{n-c}w=(L+1)P+S.
\]
Hence the Euclidean quotient and remainder of \(2^{n-c}w\) upon division by \(L+1\) must be precisely \(P\) and \(S\). The binary digit string has Hamming weight \(w\) exactly when
\[
s_2(P)+s_2(S)=w.
\]
This proves necessity.

Conversely, suppose the Euclidean division produces \(S<L\) and
\[
s_2(P)+s_2(S)=w.
\]
Put
\[
N=PL+S.
\]
Because \(w>2^{c-1}\), while \(P<2^{n-c}\), one has
\[
N=2^{n-c}w-P\ge2^{n-1}.
\]
Also \(N<2^n\); if \(w<2^c\) this is immediate, and if \(w=2^c\) then \(P\ge1\). Thus \(N\) has exactly \(n\) bits, with prefix \(P\), suffix \(S\), and weight \(w\). The recurrence identity then gives
\[
K_{2n-c+1}=2^{n-c}w-P=N.
\]
So \(N\) is Keith. Since Euclidean quotient and remainder are unique, there is at most one such \(N\) for each pair \((n,w)\).

Finally, the weight-\(1\) binary strings are exactly the powers \(2^{n-1}\), which are Keith. Hence at most \(n\) binary Keith numbers have \(n\) bits. Summing over bit lengths up to
\[
h=\lfloor\log_2x\rfloor+1
\]
gives the stated quadratic logarithmic bound.

## Verification
The accompanying checker compares the theorem with direct Keith-recurrence enumeration for every integer below \(2^{18}\). It independently constructs the predicted number for every pair
\[
2\le n\le18,\qquad 2\le w\le n,
\]
using only Euclidean division and binary Hamming weights, adds the corresponding power of two, and verifies exact equality of the predicted and directly enumerated sets at every bit length.

The finite computation is corroborative only. The infinite classification and counting bound follow from the proof above.

## Relationship to prior work
Klazar and Luca proved a density-zero upper bound for ordinary decimal Keith numbers and observed that their proof extends to every fixed base at least \(4\). They explicitly separated the binary case, citing an unpublished manuscript of Kenneth Fan that reportedly constructs all binary Keith numbers and shows infinitude; they also noted that every power of two is binary Keith.

The public exact sequence for binary Keith numbers records the efficient recurrence
\[
K_{n+k+1}=2K_{n+k}-b_k
\]
and notes that a non-power binary Keith occurrence is reached by position \(2n\). Those observations are used here as established context. The contribution is the Hamming-weight rigidity: once \((n,w)\) is fixed, the occurrence index is forced, the binary string is recovered by one Euclidean division, and at most one candidate can survive. This yields the explicit bound
\[
B_2(x)=O((\log x)^2).
\]

The companion base-\(3\) density problem requires a different antichain argument and does not imply the binary classification.

## Limitations
The result is special to base \(2\). Its proof uses both the binary recurrence identity and the fact that the digit sum equals Hamming weight. It does not by itself improve bounds in bases at least \(3\).

The strongest residual originality risk is the unpublished Kenneth Fan manuscript mentioned by Klazar and Luca. Bounded searches did not locate that manuscript or a public statement of its construction, so its exact contents could not be compared. The present claim is therefore supported by the accessible primary paper, the public binary sequence records, exact semantic searches, and a complete proof, but the unavailable manuscript remains a genuine prior-art risk.

## References
1. M. Klazar and F. Luca, “Counting Keith Numbers”, *Journal of Integer Sequences* 10 (2007), Article 07.2.2; first arXiv version 16 August 2006, arXiv:math/0608419v1. Primary MSC \(11B39\), secondary MSC \(11A63\).
2. OEIS Foundation, A162363, “Binary Keith numbers, excluding positive powers of \(2\) that are larger than \(1\).”
3. OEIS Foundation, A162724, “Binary Keith numbers.”
