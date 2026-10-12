# Exact reset thresholds for bounded positive-translation automata

## Finding
For integers \(n\ge2\) and \(m\ge1\), let \(\mathcal A_{n,m}\) have states \(Q=\{0,1,\ldots,n-1\}\), letters \(a\in\{1,2,\ldots,m\}\), and transitions
\[
\delta(x,a)=\begin{cases}x+a,&x+a<n,\\x,&x+a\ge n.\end{cases}
\]
A reset word sends every state to a single state. Its minimum length is exactly
\[
\boxed{r(n,m)=\min\left\{k\ge1:\sum_{j=0}^{k-1}\min(m,2^j)\ge n-1\right\}.}
\]
In particular, \(r(n,1)=n-1\); \(r(n,2)=\lceil n/2\rceil\); and \(r(n,m)=\lceil\log_2 n\rceil\) whenever \(m\ge n-1\). The formula gives the optimal synchronization time for *every* pair of positive integer parameters, not only asymptotic bounds or a parameter census.

## Assumptions and scope
All state and letter values are integers. A letter instructs every state to advance by its value, but a state that would exit the finite interval remains fixed; there is no wraparound or truncation to the last state. The alphabet consists only of *positive* instructions; this is a directed (not bidirectional) difference DFA in the geometric-translation sense. Letters larger than \(n-1\) act identically. No claim is made for general geometric point configurations, noninterval state sets, negative commands, or arbitrary transition rules.

## Proof
**1. Every reset target is the endpoint.** State \(n-1\) is fixed by every letter. Thus any reset word sends all states to \(n-1\).

**2. Reduction to covering a consecutive interval by subset sums.** Suppose a reset word has letters \(a_1,\ldots,a_k\), with \(1\le a_i\le m\). Each initial state \(x\) either advances by \(a_i\) or remains fixed at its \(i\)-th instruction. Therefore its total displacement \(n-1-x\) is the sum of some subcollection of these \(k\) values. As \(x\) ranges through the entire state interval, the subset sums of \(a_1,\ldots,a_k\) must contain **every integer** in \(\{0,1,\ldots,n-1\}\).

**3. Sharp upper limit on consecutive subset sums.** Order the same positive integers nondecreasingly, writing \(b_1\le\cdots\le b_k\), all at most \(m\). If at some index \(i\) one has \(b_i>1+\sum_{j<i}b_j\), then the positive integer \(1+\sum_{j<i}b_j\) is absent from *all* subset sums: it exceeds the sum of the smaller entries, while every remaining entry is at least \(b_i\). Therefore a collection whose subset sums contain \(0,\ldots,R\) either already covers this interval using a proper initial segment, or all entries up to the point needed for \(R\) satisfy \(b_i\le1+\sum_{j<i}b_j\). Let \(S_0=0\) and \(S_i=S_{i-1}+\min(m,S_{i-1}+1)\). Induction on these admissible entries bounds the length of any consecutive subset-sum interval beginning at zero by \(S_k\). Equivalently, the largest possible such interval endpoint over all \(k\)-entry choices at most \(m\) is \(S_k\).

The recurrence has the explicit solution \(S_k=\sum_{j=0}^{k-1}\min(m,2^j)\). Indeed, until the first capped increment, \(S_j=2^j-1\); afterwards the increment remains equal to \(m\). Consequently every reset word of length \(k\) must satisfy \(n-1\le S_k\).

**4. An optimal word and the matching upper bound.** Define \(d_1=1\), and recursively
\[
d_{i+1}=\min\left(m,1+\sum_{h=1}^{i}d_h\right).
\]
For the least \(k\) with \(S_k\ge n-1\), use the reset word \(d_k d_{k-1}\cdots d_1\), interpreting each displayed integer as a distinct alphabet letter (repetitions allowed). Minimality of \(k\) gives \(S_{k-1}<n-1\), so \(d_k\le S_{k-1}+1\le n-1\); every chosen letter is effective somewhere.

To verify the reset property, write the remaining distance of a state from \(n-1\) as \(t\). Initially \(0\le t\le n-1\le\sum_{j=1}^{k}d_j\). Suppose a suffix of the word consists of denominations \(d_i,\ldots,d_1\), where \(0\le t\le\sum_{j=1}^i d_j\). Under \(d_i\), the distance becomes \(t-d_i\) if \(t\ge d_i\), and stays \(t\) if \(t<d_i\). In the first case the new distance is at most \(\sum_{j<i}d_j\); in the second case it is at most \(d_i-1\le\sum_{j<i}d_j\). Induction over the remaining letters yields distance zero. Thus every initial state reaches \(n-1\) after \(k\) letters.

The lower and upper bounds agree, proving the formula with all quantifiers and boundary cases. For \(m=1\) the sum equals \(k\). For \(m=2\) it equals \(2k-1\) for every \(k\ge1\). If \(m\ge n-1\), the minimizing \(k\) satisfies \(2^{k-1}\le n-1\le m\), so the sum is \(2^k-1\), giving the stated logarithmic case.

## Verification
Run `python3 verify.py` using only the Python standard library. The checker independently computes minimum reset-word length by breadth-first search on the *power automaton* for all \(105\) parameter pairs \(2\le n\le16\), \(1\le m\le7\). For each pair it compares the BFS optimum with the formula and replays the constructed word directly on all states. This finite calculation is a reproducibility cross-check, not the basis of the theorem for arbitrary parameters.

## Relationship to prior work
Bradshaw, Clow and Stacho introduced difference DFAs as geometric movement models, studied universal reachability and synchronization, and bounded reset-word length under bidirectional connectivity and diameter hypotheses. The present *positive-only interval* automata are directed, with an absorbing endpoint, so their bidirectional upper-bound theorem does not give this exact parameter-dependent reset threshold. The proof here uses the classical complete-sequence/subset-sum principle; that combinatorial ingredient is not claimed as new. The new assertion is the precise reset-length formula, its optimal control word, and the exact transition between linear and logarithmic synchronization regimes for this natural directed translation model.

## Limitations
The proof assumes all positive integer shift letters through \(m\) are available and every unsuccessful move is a self-loop. The formula need not survive deleting a letter, changing the boundary rule, or allowing negative shifts. The comparison cannot exclude all unindexed equivalent results. No independent validation has been performed.

## References
- P. Bradshaw, A. Clow and L. Stacho, *A cornering strategy for synchronizing a DFA*, arXiv:2405.00826 (first public version 1 May 2024), especially Sections 3 and 4.
- M. V. Volkov, *Synchronization of finite automata*, Russian Mathematical Surveys **77** (2022), 819–891 (general background on reset thresholds).
