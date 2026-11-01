# Exact seven-layer synchronization census for three-color firefly stars

## Finding
For every integer \(r\ge1\), run the synchronous three-color inhibitory firefly cellular automaton on the labelled star \(K_{1,r}\). Write \(T\) for the first nonnegative time at which all \(r+1\) colors coincide, setting \(T=\infty\) if this never happens. The complete exact distribution over all \(3^{r+1}\) initial configurations is

\[
\begin{array}{c|rrrrrrrr}
T&0&1&2&3&4&5&6&\infty\\\hline
\#\{T\}&3&2^r&2^r&2^r&2^r-2&3^r-3&3^r-2^r-1&3^r-3\cdot2^r+3.
\end{array}
\]

In particular, synchronization occurs for every initial coloring if \(r\le2\), whereas for \(r\ge3\) exactly \(3^r-3\cdot2^r+3\) initial colorings never synchronize. Every synchronizing coloring synchronizes by time \(6\), with this uniform bound attained whenever \(r\ge2\) (and the sharp bound for \(r=1\) equal to \(3\)). Under independent uniform initial colors, the three outcomes \(T=5\), \(T=6\), and \(T=\infty\) each have limiting probability \(1/3\) as \(r\to\infty\).

## Assumptions and scope
The graph has a distinguished center and \(r\) individually labelled leaves; there are no loops or leaf-to-leaf edges. At each integer time, every site has a color in \(\{0,1,2\}\). The blinking color is \(1\). A site of color \(2\) remains at color \(2\) if at least one neighbor is blinking; every other site advances its color by \(1\) modulo \(3\). All updates use the colors before that update. All initial colorings are counted separately, with no identification under star automorphisms. Synchrony means every site has the same color; once achieved, it persists as a rotating three-cycle.

## Proof
Denote the center color by \(c\in\{0,1,2\}\) and the **set** of colors currently represented among the leaves by nonempty \(S\subseteq\{0,1,2\}\). The star rule depends only on \((c,S)\). Define
\[
 f_c(s)=\begin{cases}2,&c=1,\ s=2,\\s+1\pmod3,&\text{otherwise},\end{cases}
 \qquad
 g_S(c)=\begin{cases}2,&c=2,\ 1\in S,\\c+1\pmod3,&\text{otherwise}.\end{cases}
\]
Then the exact support-map is \(\Phi(c,S)=(g_S(c),\{f_c(s):s\in S\})\). Although leaf multiplicities are forgotten, no extra transitions become possible: leaves of a fixed color always make the same update. Thus each of the \(21=3(2^3-1)\) states represents all configurations with that center and exact leaf-color support, for every \(r\).

The following **complete** transition certificate lists all \(21\) possible support states. A time marked “never” is a state which remains outside synchrony indefinitely; all other listed times are verified recursively by applying the displayed update until a state \((c,\{c\})\) is reached. The three synchronized states update cyclically among themselves.

| State | Updated state | First synchrony time |
|---|---|---:|
| \( (0,\{0\}) \) | \( (1,\{1\}) \) | 0 |
| \( (0,\{1\}) \) | \( (1,\{2\}) \) | 2 |
| \( (0,\{0,1\}) \) | \( (1,\{1,2\}) \) | 2 |
| \( (0,\{2\}) \) | \( (1,\{0\}) \) | 3 |
| \( (0,\{0,2\}) \) | \( (1,\{0,1\}) \) | 6 |
| \( (0,\{1,2\}) \) | \( (1,\{0,2\}) \) | 6 |
| \( (0,\{0,1,2\}) \) | \( (1,\{0,1,2\}) \) | 6 |
| \( (1,\{0\}) \) | \( (2,\{1\}) \) | 2 |
| \( (1,\{1\}) \) | \( (2,\{2\}) \) | 0 |
| \( (1,\{0,1\}) \) | \( (2,\{1,2\}) \) | 5 |
| \( (1,\{2\}) \) | \( (2,\{2\}) \) | 1 |
| \( (1,\{0,2\}) \) | \( (2,\{1,2\}) \) | 5 |
| \( (1,\{1,2\}) \) | \( (2,\{2\}) \) | 1 |
| \( (1,\{0,1,2\}) \) | \( (2,\{1,2\}) \) | 5 |
| \( (2,\{0\}) \) | \( (0,\{1\}) \) | 3 |
| \( (2,\{1\}) \) | \( (2,\{2\}) \) | 1 |
| \( (2,\{0,1\}) \) | \( (2,\{1,2\}) \) | 5 |
| \( (2,\{2\}) \) | \( (0,\{0\}) \) | 0 |
| \( (2,\{0,2\}) \) | \( (0,\{0,1\}) \) | 3 |
| \( (2,\{1,2\}) \) | \( (2,\{0,2\}) \) | 4 |
| \( (2,\{0,1,2\}) \) | \( (2,\{0,1,2\}) \) | never |


For the sole nonsynchronizing state \((2,\{0,1,2\})\), the center remains frozen at \(2\) because there is always a blinking leaf, while all leaves rotate freely through their colors. Their occupied color set remains complete, so synchrony is impossible. Every other state in the certificate reaches a synchronized state by step \(6\). A witness for the sharp bound is initial center color \(0\) with leaves exhibiting precisely colors \(0\) and \(2\).

For a fixed set \(S\) of \(j\) colors, let \(U_j(r)\) be the number of assignments of \(r\) labelled leaves using **every** color in \(S\) and no others. Inclusion-exclusion gives
\[
U_1(r)=1,\qquad U_2(r)=2^r-2,\qquad
U_3(r)=3^r-3\cdot2^r+3.
\]
Reading the certificate, the numbers of states \((c,S)\) at each first synchronization time, grouped by \(|S|=1,2,3\), are
\[
\begin{array}{c|rrrrrrrr}
T&0&1&2&3&4&5&6&\infty\\\hline
|S|=1&3&2&2&2&0&0&0&0\\
|S|=2&0&1&1&1&1&3&2&0\\
|S|=3&0&0&0&0&0&1&1&1.
\end{array}
\]
Multiplying each column by the appropriate \(U_j(r)\) yields respectively \(3\), \(2+U_2(r)=2^r\) three times, \(U_2(r)=2^r-2\), \(3U_2(r)+U_3(r)=3^r-3\), \(2U_2(r)+U_3(r)=3^r-2^r-1\), and \(U_3(r)\). These sum to \(3^{r+1}\) identically. Since the support certificate exhausts all initial configurations for every \(r\), this is a complete proof for the infinite graph family, not an extrapolation from computational examples.

The sharpness statements follow from the witness above and vanishing of \(U_2(1)\), \(U_3(1)\). Division by \(3^{r+1}\) gives the asserted limiting probabilities because \((2/3)^r\to0\).

## Verification
The standalone `verify.py` implements the update directly on **labelled arrays**, independently of the support-map proof. It exhaustively iterates all \(3^{r+1}\) initial configurations for every \(1\le r\le9\), stops upon synchrony or repeated configurations, and compares the exact histograms to the theorem. The accompanying `verify_output.txt` records all nine counts and a final success line. This finite test is a reproducibility check; the general theorem follows from the exhaustive \(21\)-state support certificate and surjection formula.

## Relationship to prior work
Hanbaek Lyu, *Synchronization of finite-state pulse-coupled oscillators* (arXiv:1407.1103, public 2014-07-04), defines exactly the inhibitory firefly update and proves qualitative tree synchronization criteria, including its dependence on maximum degree and recurrent blinking. In particular, it establishes the graph-theoretic obstruction to universal synchronization on stars with at least three leaves. The same author's *Time complexity of Synchronization of discrete pulse-coupled oscillators on trees* (arXiv:1610.00837, public 2016-10-04) provides general tree recurrence criteria and worst-case time estimates and discusses other star-based obstructions. The present result does not claim either general criterion or the example of a permanently inhibited center as new. Its claimed contribution is the **entire seven-layer exact finite-size census**, including the sharp universal six-update time for synchronizing starts and the limiting three-way basin split, obtained through the stated explicit support quotient and exact counting.

## Limitations
Only the deterministic synchronous three-color firefly rule and labelled stars are treated. The result does not cover other periods, stochastic pulse transmission, asynchronous updates, or arbitrary trees. The classification is proved from the complete support-map certificate and independently sampled by exhaustive finite tests; it has not received an independent formal review. Literature comparisons reduce, but cannot eliminate, the possibility of an earlier unindexed equivalent enumeration.

## References
1. H. Lyu, *Synchronization of finite-state pulse-coupled oscillators*, arXiv:1407.1103 (first public 2014-07-04). https://arxiv.org/abs/1407.1103
2. H. Lyu, *Time complexity of Synchronization of discrete pulse-coupled oscillators on trees*, arXiv:1610.00837 (first public 2016-10-04). https://arxiv.org/abs/1610.00837
