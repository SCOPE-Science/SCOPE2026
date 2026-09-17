# A width gap and exact near-minimum classification for finite Gilbreath sequences

## Statement

Let \(S=(s_1,\ldots,s_n)\in\mathcal G_n\), \(n\ge 3\), be a strictly increasing Gilbreath sequence with \((s_1,s_2)=(2,3)\). Let
\[
(e_1,\ldots,e_{n-1}),\qquad e_i=s^{\,i}_{n-i},
\]
be its right anti-diagonal, let
\[
A(S)=\sum_{i=1}^{n-1}e_i,
\]
and let \(K_S\) be its two-sided valid-extension set. Then

\[
\boxed{\ |K_S|\ge \min\{A(S)+2,\,10\}\ }.
\]

More sharply, every defective sequence, i.e. every \(S\) for which the valid-extension set has a hole in its candidate interval, satisfies
\[
\boxed{\ K_S\ne C_S\quad\Longrightarrow\quad |K_S|\ge 10\ }.
\]
The constant \(10\) is best possible: the first-hole sequence
\[
(2,3,5,9,15)
\]
has right anti-diagonal \((6,2,0,1)\), \(A(S)=9\), and \(|K_S|=10\).

Consequently,
\[
\boxed{\ |K_S|\le 9\iff A(S)\le 7\ },
\]
and in this range \(K_S=C_S\) and
\[
|K_S|=A(S)+2\in\{5,7,9\}.
\]

This gives the following exact structural classification.

- \(|K_S|=5\) iff the right anti-diagonal is
  \[
  (2,0,\ldots,0,1).
  \]
- \(|K_S|=7\) iff \(e_1=2\), exactly one of \(e_2,\ldots,e_{n-2}\) equals \(2\), and all the others are \(0\).
- \(|K_S|=9\) iff either
  1. \(e_1=4\), exactly one of \(e_2,\ldots,e_{n-2}\) equals \(2\), and all the others are \(0\); or
  2. \(e_1=2\), exactly two of \(e_2,\ldots,e_{n-2}\) equal \(2\), and all the others are \(0\).

Thus no extension width \(6\) or \(8\) occurs in \(\mathcal G_n\), and the first possible width above \(9\) is \(10\).

## Context

Muney introduced the finite valid-extension problem for Gilbreath sequences, proved the reverse-tree characterization of valid distances, and established the exact interval-completeness criterion
\[
K_S=C_S
\iff
e_i\le 1+\sum_{j>i}e_j
\quad(1\le i\le n-2).
\]
The same paper proved that the minimum extension width is \(5\), uniquely attained by the minimal sequence, and explicitly posed the open problem:

> Stability classification near the minimum: characterize \(S\in\mathcal G_n\) with \(|K_S|\le 9\).

The theorem above resolves that question in terms of the anti-diagonal sum and gives an explicit anti-diagonal classification.

## Proof

We use two elementary facts from the valid-extension framework.

First, for \(S\in\mathcal G_n\),
\[
e_1,\ldots,e_{n-2}\ \text{are even},\qquad e_{n-1}=1,
\]
and \(e_1>0\).

Second, if
\[
D_S=\{|k-s_n|:k\in K_S\},
\]
then reverse preimages under \(x\mapsto |x-e|\) are given by
\[
P_e(T)=\{e+t:t\in T\}\cup\{e-t:t\in T,\ t\le e\}.
\]
Starting from \(\{1\}\) and applying \(P_{e_{n-1}},\ldots,P_{e_1}\) gives \(D_S\). Hence
\[
|K_S|=2|D_S|-\mathbf 1_{\{0\in D_S\}}.
\]

### Lemma: a zero suffix forces the preceding entry to be \(0\) or \(2\)

Suppose that for some \(i\le n-2\),
\[
e_{i+1}=\cdots=e_{n-2}=0.
\]
Then
\[
e_i\in\{0,2\}.
\]

Indeed, look at row \(i\) of the difference triangle and write its entries as
\[
x_1,x_2,\ldots,x_m.
\]
Because \(S\) is Gilbreath, \(x_1=1\), while \(x_m=e_i\). The equality \(e_{i+1}=0\) forces \(x_m=x_{m-1}\). Then \(e_{i+2}=0\) forces \(x_{m-1}=x_{m-2}\), and continuing gives
\[
x_2=x_3=\cdots=x_m=e_i.
\]
The leftmost entry of the next row is therefore
\[
|x_2-x_1|=|e_i-1|.
\]
It must equal \(1\), so \(e_i=0\) or \(2\).

### Width gap for defective sequences

Assume \(K_S\ne C_S\). By the interval-completeness criterion, choose the largest index \(i\) such that
\[
e_i>1+\sum_{j=i+1}^{n-1}e_j.
\]
Set
\[
B=\sum_{j=i+1}^{n-1}e_j.
\]
The integer \(B\) is odd because the last anti-diagonal entry is \(1\) and all preceding ones are even.

All indices to the right of \(i\) satisfy the interval-completeness inequalities. Reversing only this suffix therefore gives the full even interval
\[
T=\{0,2,4,\ldots,B+1\}.
\]
This follows directly by induction from \(P_1(\{1\})=\{0,2\}\): whenever the next even fold parameter is at most one plus the remaining tail sum, the reverse preimage of a full even interval is again a full even interval.

The case \(B=1\) is impossible. It would mean
\[
e_{i+1}=\cdots=e_{n-2}=0,
\]
so the lemma gives \(e_i\le2=B+1\), contradicting the choice of \(i\). Hence
\[
B\ge3.
\]

Now \(e_i>B+1\). Therefore every \(t\in T\) satisfies \(t<e_i\), and
\[
P_{e_i}(T)
=
\{e_i-(B+1),e_i-(B-1),\ldots,e_i+(B+1)\}.
\]
This is a set of exactly
\[
B+2\ge5
\]
positive integers.

Every earlier reverse step \(P_e\) contains the injective translate \(e+T\), so cardinality can never decrease. If \(0\) never appears afterwards, then
\[
|D_S|\ge5,\qquad |K_S|=2|D_S|\ge10.
\]
If \(0\) first appears at some earlier step, then it arises from a value \(t=e\) already in the current set. At that step the translate \(e+T\) still contributes at least five positive values, and \(0\) is an additional distinct value. Hence the new set has at least six elements, and subsequently cardinality again cannot decrease. Thus
\[
|D_S|\ge6,\qquad |K_S|\ge 2|D_S|-1\ge11.
\]
In all cases,
\[
K_S\ne C_S\Longrightarrow |K_S|\ge10.
\]

### Near-minimum classification

The candidate interval has
\[
|C_S|=A(S)+2.
\]
If \(A(S)\le7\), then \(K_S\subseteq C_S\) gives \(|K_S|\le9\). The defective-width gap just proved rules out \(K_S\ne C_S\), so \(K_S=C_S\) and
\[
|K_S|=A(S)+2.
\]
Conversely, if \(|K_S|\le9\), the width gap forces \(K_S=C_S\), and therefore
\[
A(S)+2=|K_S|\le9.
\]
This proves
\[
|K_S|\le9\iff A(S)\le7.
\]

It remains only to list the possible anti-diagonals. Since \(e_1>0\) is even, all \(e_1,\ldots,e_{n-2}\) are nonnegative even integers, and \(e_{n-1}=1\):

- \(A=3\): the even entries sum to \(2\), so \(e_1=2\) and all others are zero.
- \(A=5\): the even entries sum to \(4\). The possibility \(e_1=4\) followed only by zeros is excluded by the zero-suffix lemma. Hence \(e_1=2\) and exactly one later entry is \(2\).
- \(A=7\): the even entries sum to \(6\). The possibility \(e_1=6\) followed only by zeros is excluded. If \(e_1=4\), exactly one later entry is \(2\). If \(e_1=2\), the remaining sum \(4\) cannot be a single later \(4\), again by the zero-suffix lemma applied at that later index; it must be two entries equal to \(2\).

This proves the explicit classification.

## Sharpness and computational check

The lower bound \(10\) for defective sequences is sharp at the known first-hole example
\[
S=(2,3,5,9,15),\qquad e=(6,2,0,1),
\]
whose valid distance set is
\[
D_S=\{2,4,6,8,10\},
\]
so \(|K_S|=10\).

The accompanying exact-integer program separately enumerates \(\mathcal G_n\) through \(n=10\) using the reverse-tree recurrence and checks, for every sequence in that range,
\[
|K_S|\ge\min\{A(S)+2,10\},
\qquad
(|K_S|\le9)\iff(A(S)\le7),
\]
together with the three stated anti-diagonal forms. The computation is supplementary; the theorem is proved for all \(n\).

## Limitations

This result concerns the finite valid-extension problem for strictly increasing Gilbreath sequences. It does not prove Gilbreath's conjecture for the primes, does not determine the maximum extension width, and does not classify widths \(10\) and above.

Originality is claimed only to the best of our knowledge. The closest source is very recent and itself lists the \(|K_S|\le9\) classification as an open problem, so incompletely indexed follow-up work remains the principal residual risk.

## References

1. L. Muney, *Holes in Valid-Extension Sets of Finite Gilbreath Sequences*, arXiv:2606.23721v2 (2026). https://arxiv.org/abs/2606.23721
2. R. Gatti, *Gilbreath equation, Gilbreath polynomials, and upper and lower bounds for Gilbreath conjecture*, Mathematics **11** (2023), 4006. https://doi.org/10.3390/math11184006
3. OEIS Foundation Inc., *A080839: Number of positive increasing integer sequences with Gilbreath transform \((1,1,1,\ldots)\)*. https://oeis.org/A080839
