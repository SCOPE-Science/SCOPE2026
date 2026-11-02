# One chord completes all consecutive cycle sums through \(2^{10}\) vertices

## Finding
Let \(C_n\) be the cycle with consecutive integer vertex labels \(1,2,\ldots,n\), and let \(\operatorname{mEC}(n)\) be the least number of additional edges required to make every integer from \(1\) through \(T_n=n(n+1)/2\) the sum of labels of a nonempty connected vertex subset. Then
\[
\operatorname{mEC}(n)=1\qquad(8\le n\le1024).
\]
In fact, for each integer in this range one can choose the extra edge \(\{1,q_n\}\); every \(q_n\) is specified in `chords.txt` and satisfies \(3\le q_n\le n-2\). The assertion concerns the *entire* finite interval of 1017 orders, not extrapolation beyond it.

## Assumptions and scope
All graphs are finite simple undirected graphs. A vertex subset is connected when its induced subgraph is connected. The original cycle has edges between consecutive labels and between \(n\) and \(1\). A completion permits the addition of an edge not already in the cycle. The exact result covers \(8\le n\le1024\) and no greater orders.

## Proof
**Lower bound.** Marotti and Needleman [1, Theorem 1] prove that the consecutively labeled \(n\)-cycle fails to represent at least one target for every \(n\ge8\). Therefore \(\operatorname{mEC}(n)\ge1\) throughout the claimed interval.

**Sufficient connected sets after a chord.** Fix \(n\) and a candidate \(3\le q\le n-2\). Write \(I=[2,q-1]\) and \(J=[q+1,n]\) for the two interior paths between the endpoints of the chord \(\{1,q\}\). For each path choose a possibly empty prefix and a possibly empty suffix whose vertex sets do not overlap. Their union with \(\{1,q\}\) is connected using the chord, because every chosen vertex is linked to one of the endpoints by a selected interval. Every consecutive cyclic arc is connected even without the chord.

For an interval of successive labels \(u,u+1,\ldots,v\), let \(P_{u,v}\) be the exact finite set of prefix-plus-suffix sums, with disjoint selections. If the interval has length \(L=v-u+1\), then
\[
P_{u,v}=\left\{\frac{a(2u+a-1)}2+\frac{b(2v-b+1)}2:\ a,b\in\mathbb Z_{\ge0},\ a+b\le L\right\}.
\]
Let \(A_n\) be all nonempty cyclic-arc sums. Every target in
\[
A_n\;\cup\;\bigl(1+q+P_{2,q-1}+P_{q+1,n}\bigr)
\]
is therefore realized by a connected vertex subset of the cycle with this chord. Here the sum of sets denotes the Minkowski sum of integer sets.

**Finite exhaustive certificate.** The companion `chords.txt` gives one \(q_n\) for each \(n=8,9,\ldots,1024\). The standalone exact-integer checker `verify.py` constructs \(A_n\) from all \(n\) possible cyclic starts and each length \(1\le k\le n\), constructs the two prefix/suffix sum sets from the displayed formulas, and verifies for *every* one of the 1017 orders that the above union includes every target \(1\le s\le T_n\). Bit positions correspond exactly to target sums; there is no sampling, heuristic tolerance, or undetermined search bound. This proves \(\operatorname{mEC}(n)\le1\) in the complete stated range and hence equality.

## Verification
Execute `python3 verify.py` with `chords.txt` in the same directory. It checks each row in the finite domain, verifies the chord is absent from the original cycle, and asserts coverage of the entire inclusive target interval up to \(T_{1024}=524800\). It also performs independent direct vertex-subset connectivity enumerations at orders \(8,12,16\). Only standard Python 3 modules are required. The bound \(1024\) is part of the theorem; the calculation cannot imply the same result for arbitrary \(n\).

## Relationship to prior work
Marotti and Needleman [1] introduce the minimum-edge-completion problem for consecutive cycle sums, prove the original cycles incomplete for every \(n\ge8\), exhibit \(\operatorname{mEC}(8)=1\), and establish the general upper bound \(\operatorname{mEC}(n)\le n/2-1\). They identify improving its growth as a further question. The present result gives exact values across the initial dyadic interval through \(1024\), with a single edge in every case. It is a finite computational theorem rather than a proof of their hoped-for asymptotic bound. Relevant broader research-record and web searches did not reveal an equivalent initial-range census; this absence does not certify historical priority.

## Limitations
No claim is made for \(n>1024\), that any particular chord formula persists indefinitely, or that the finite evidence proves a universal one-edge conjecture. The proof of the lower bound relies on [1]; the upper bound is a fully repeatable finite exhaustive certificate. Previous unindexed computations could predate this classification.

## References
[1] Jessica Marotti and Jonathan Needleman, *Consecutive Cycle Sums*, arXiv:2610.08889v1, first posted 2026-10-06, especially Theorem 1 and Section 5, https://arxiv.org/abs/2610.08889 ; full text https://arxiv.org/html/2610.08889 .
