# Finite-order Markov dichotomy for dyadic sensors of the doubling map

## Finding
Let \(T:[0,1)\to[0,1)\) be \(T(x)=2x\pmod 1\), with its stationary Lebesgue probability, and let
\[
 Z_j=\mathbf 1_{\{T^j(X_0)<c\}},\qquad j\ge 0,
\]
where \(c=k/2^r\) is dyadic, \(r\ge1\), and \(0<k<2^r\). Then the stationary binary process \((Z_j)\) is a Markov process of some finite order **if and only if** \(c=1/2\). At \(c=1/2\) it is a fair independent Bernoulli sequence. At every other dyadic threshold it has a presentation as a finite-state hidden Markov process, but is not Markov of order \(m\) for **any** integer \(m\ge0\).

The all-constant-word probabilities also have uniform exponential bounds. For any \(r\ge2\) and \(k\ne 2^{r-1}\), set \(a=0\) when \(k<2^{r-1}\), and \(a=1\) when \(k>2^{r-1}\). Write \(L=n+r-1=qr+t\), with \(0\le t<r\), and define \(s=2^r-k\) in the first case and \(s=k\) in the second. Then for every \(n\ge1\),
\[
 \frac{2^q}{2^L}\ \le\ \Pr(Z_0=\cdots=Z_{n-1}=a)\ \le\ \frac{s^q2^t}{2^L},\qquad 1<s<2^r.
\]
Both bounds are exact combinatorial inequalities, not assertions of the exact persistence exponent. Thresholds \(c=0,1\), if allowed, yield constant processes and are excluded from the nontrivial classification.

## Assumptions and scope
The source is deterministic doubling, initialized with normalized Lebesgue measure. Binary expansions are chosen uniquely off the countable dyadic ambiguity set; those null exceptions do not affect finite-dimensional laws. The observation compares \(T^j(X_0)\) to the half-open interval \([0,c)\). The dyadic denominator exponent \(r\) need not be reduced, and the claim is uniform over all its numerators. No assertion is made for nondyadic thresholds or for non-Lebesgue invariant initializations. An order-\(m\) Markov process means that its one-step conditional law given any positive-probability finite history of length at least \(m\) depends only on the last \(m\) observations; order zero means independent observations.

## Proof
**Binary coding and hidden states.** Under Lebesgue probability, the binary digits \(B_0,B_1,\ldots\) of \(X_0\) are independent fair bits, and \(T\) shifts these digits. For dyadic \(c=k/2^r\), the event \(Z_j=1\) is equivalent, outside the null ambiguity set, to
\[
  \sum_{i=0}^{r-1}2^{r-1-i}B_{j+i}<k.
\]
Thus \(Z_j\) reads a sliding word of \(r\) fair bits. The successive \(r\)-bit windows form a stationary Markov chain on \(2^r\) states, shifting and appending an independent fair bit. The output is a deterministic state label; this gives the finite hidden Markov presentation. For \(c=1/2\), the comparison reads only \(B_j\), so the output is an independent fair bit.

**Persistent-word counting.** Suppose henceforth \(r\ge2\) and \(k\ne2^{r-1}\). Let \(a=0\) when the cutoff is below one half and \(a=1\) when it is above. The all-\(a\) event of output length \(n\) requires that every consecutive \(r\)-bit window in its initial input string of length \(L=n+r-1\) have output label \(a\). Denote the number of such input strings by \(N_L\). Their equally likely binary inputs give
\[
  \Pr(Z_0=\cdots=Z_{n-1}=a)=\frac{N_L}{2^L}.
\]
Every \(N_L\) is a strictly positive integer.

To bound \(N_L\) above, partition the first \(qr\) input digits into \(q\) disjoint complete \(r\)-blocks, leaving a tail of length \(t\). Each complete block must itself receive label \(a\); the number \(s\) of such blocks is \(2^r-k\) when \(a=0\), or \(k\) when \(a=1\). Dropping all overlapping-window restrictions can only increase the count. Therefore \(N_L\le s^q2^t\), with \(s<2^r\).

For the lower bound, put \(b=1\) when \(a=0\) and \(b=0\) when \(a=1\). Concatenate, independently in each of the \(q\) consecutive complete \(r\)-blocks, either \(b^r\) or \((1-b)b^{r-1}\); then append \(t\) digits equal to \(b\). These yield \(2^q\) distinct strings. Every \(r\)-window starting at \(b\) has the required label because its leading bit alone places it on the correct side of \(k/2^r\). The only windows starting at \(1-b\) begin at the start of one of the constructed special blocks, and equal \((1-b)b^{r-1}\). In the low-cutoff case this word has value \(2^{r-1}-1\ge k\); in the high-cutoff case it has value \(2^{r-1}<k\). Hence every constructed string is admissible. This proves \(2^q\le N_L\le s^q2^t\) simultaneously for every \(L\ge r\).

**Integer-growth obstruction to finite memory.** Suppose the observation process were Markov of some finite order \(m\ge0\). All-\(a\) cylinders have positive probability by the lower bound, so for all sufficiently large \(n\), the extension probability \(\Pr(Z_n=a\mid Z_0=\cdots=Z_{n-1}=a)\) would be a fixed positive number \(p\), depending only on the last \(m\) copies of \(a\). The exact cylinder formula would then imply
\[
   \frac{N_{L+1}}{N_L}=2p=R>0
\]
for every sufficiently large integer \(L\). Since the \(N_L\) are positive integers, \(R\) is rational. Write \(R=u/v\) in coprime positive integers. The equalities \(N_{L+j}=N_Lu^j/v^j\in\mathbb N\) for every \(j\ge0\) force \(v^j\mid N_L\) for all \(j\), hence \(v=1\). Consequently \(R\) is a positive integer.

If \(R=1\), the eventually constant \(N_L\) contradict the lower bound \(N_L\ge 2^{\lfloor L/r\rfloor}\), which diverges. If \(R\ge2\), eventual geometric growth contradicts \(N_L\le s^{\lfloor L/r\rfloor}2^{L\bmod r}\), because \(s^{1/r}<2\). These exhaust all positive integers and give a contradiction. No finite Markov order exists unless \(c=1/2\). Together with the first step, this completes the classification.

## Verification
A standalone exact-integer verifier, `verify.py`, independently implements direct brute-force window enumeration and a suffix-state dynamic program. It matches the two counts for 570 configurations across 114 non-half dyadic thresholds with denominators from four through sixty-four, and checks 3,876 exact lower/upper persistence inequalities at longer finite lengths. It also checks the exact one-symbol probability and the half-threshold Bernoulli normalization. Executing it as `python verify.py` prints `VERIFY_OK 114 thresholds, 570 exact brute/DP comparisons, 3876 finite persistence bounds`.

The proof does not infer the infinite classification from these finite tests. Its critical infinite step is the divisibility consequence of an eventually constant ratio of positive integers, combined with the uniform strict exponential lower and upper growth bounds; all three ingredients are proved above.

## Relationship to prior work
Binary coding of doubling maps, symbolic descriptions of open interval maps, and hidden Markov/sofic factor criteria are established theory. Alcaraz Barrera (2015) studies survivor sets, entropy, and intrinsic ergodicity for open doubling maps, using binary symbolic coding. Those topological survivor results do not state a classification of finite-order Markov *probability laws* induced by all dyadic thresholds under Lebesgue initialization. Boyle and Petersen (2010, Section 5) survey general matrix-rank and algorithmic characterizations of when hidden Markov processes are finite-order Markov. Applying such a criterion separately to each threshold would be a possible alternative method, but the cited general theory does not give the uniform all-cutoff classification or the elementary persistence-count obstruction proved here. The finite hidden Markov representation itself is standard and not claimed as new. The contribution is the exact family-wide dichotomy and simultaneous uniform word-count proof.

## Limitations
The novelty assessment is bounded by available indexed literature; a prior unindexed specialization of a general finite-state factor result could imply this theorem. No absolute historical priority, independent audit, or general classification for nondyadic thresholds is asserted. The explicit word-count bounds are not claimed to be sharp asymptotics for individual cutoffs. Stationarity and Lebesgue initialization are essential to the exact integer-count formula. Finite verification runs are not an infinite proof.

## References
1. R. Alcaraz Barrera, *Intrinsic Ergodicity of Open Dynamical Systems for the Doubling Map*, arXiv:1509.00255v1, submitted 2015-09-01, https://arxiv.org/html/1509.00255v1.
2. M. Boyle and K. Petersen, *Hidden Markov Processes in the Context of Symbolic Dynamics*, 2010, especially Section 5 on finite-order Markov images, https://math.umd.edu/~mboyle/papers/BoylePetersen06Jan2010.pdf.
