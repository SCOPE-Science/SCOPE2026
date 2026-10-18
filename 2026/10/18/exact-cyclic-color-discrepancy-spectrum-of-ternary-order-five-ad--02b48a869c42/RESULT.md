# Exact cyclic color-discrepancy spectrum of ternary order-five adjacency-hopping de Bruijn cycles

## Finding

Among the cyclic ternary adjacency-hopping de Bruijn words of order five, modulo cyclic rotation but **not** alphabet permutation or reversal, exactly \(23{,}700\) have cyclic color discrepancy \(3\), exactly \(420{,}924\) have discrepancy \(4\), and exactly \(341{,}808\) have discrepancy \(5\). There are no other values. Thus the total is \(786{,}432\), the sharp minimum is \(3\), the sharp maximum is \(5\), and the fraction of optimal cycles is \(1975/65536\).

Here cyclic color discrepancy is the maximum, over a circular contiguous interval and over two alphabet symbols, of the absolute difference of their numbers of occurrences. In the same model at orders two, three, and four, the respective complete distributions are \(\{2:3\}\), \(\{2:12\}\), and \(\{3:384\}\). Hence order five is the first order in this ternary family for which the discrepancy depends on the choice of cycle.

## Assumptions and scope

The alphabet is \(\Sigma=\{0,1,2\}\). A length-\(48\) circular word \(w\) qualifies precisely when adjacent cyclic symbols differ and the \(48\) distinct words of length five with unequal consecutive symbols occur exactly once each as cyclic factors. Two qualifying words are identified only when they differ by cyclic rotation. In particular, reversal and color relabeling are **not** quotiented out.

Let \(\mathcal I(w)\) be the set of all circular consecutive intervals of lengths zero through \(48\), including wrapping intervals. Write \(\#_a(I)\) for the count of symbol \(a\) in interval \(I\). Define

\[
D(w)=\max_{I\in\mathcal I(w)}\max_{a,b\in\Sigma}\big|\#_a(I)-\#_b(I)\big|.
\]

This is the ternary maximum-minus-minimum color-count discrepancy, as in the general-alphabet discrepancy definition of Álvarez et al. The result is an exact, finite, computer-assisted census at fixed alphabet size three and order five, not an asymptotic theorem for other parameters.

## Proof

**1. Exact model and canonical rooting.** Construct a directed graph whose vertices are the \(24=3\cdot2^3\) proper ternary words of length four and whose edges are the \(48=3\cdot2^4\) proper ternary words of length five. The edge \(a_1a_2a_3a_4a_5\) goes from \(a_1a_2a_3a_4\) to \(a_2a_3a_4a_5\). Every vertex has two incoming and two outgoing edges. A qualifying circular word is equivalent to a directed Eulerian circuit of this graph. The five-letter word `01010` occurs exactly once in every qualifying cycle, so rotating to begin with this factor gives a unique canonical edge-rooted circuit. Conversely, every Eulerian circuit beginning with the edge `01010` yields exactly one qualifying rotation class by taking the leading symbol of each successive edge. Thus counting rooted edge-simple closed Eulerian walks from that fixed edge counts every required cycle exactly once.

**2. Exact reduction of cyclic discrepancy.** Every qualifying word contains exactly sixteen occurrences of each symbol: there are precisely \(2^4=16\) permitted length-five words with each prescribed first symbol. For two different colors \(a,b\), define the integer prefix balance

\[
P_{ab}(t)=\#_a(w_0\cdots w_{t-1})-\#_b(w_0\cdots w_{t-1}),\quad 0\le t\le48.
\]

Because \(P_{ab}(48)=P_{ab}(0)=0\), the imbalance of a possibly wrapping interval is the difference of two prefix balances. Conversely, for two indices attaining the maximum and minimum balances, one of the two cyclic directions realizes their absolute difference. Therefore

\[
D(w)=\max_{(a,b)\in\{(0,1),(0,2),(1,2)\}}
\left(\max_{0\le t\le48}P_{ab}(t)-\min_{0\le t\le48}P_{ab}(t)\right).
\]

This identity evaluates every cyclic interval exactly, with no approximation and no dependence on the canonical cut.

**3. Exhaustive enumeration certificate.** The standalone program `verify_dfs.cpp` enumerates all edge-simple walks starting with `01010` by recursively extending only unused outgoing edges. It accepts a walk only after all \(48\) edges have appeared and the walk has returned to the starting vertex. This exhausts exactly all canonical Eulerian circuits by step 1. Each accepted walk is classified using the integer prefix-extrema formula in step 2. The resulting exact histogram is

\[
\begin{array}{c|rrr|r}
D&3&4&5&\text{total}\\\hline
\#\text{ cycles}&23{,}700&420{,}924&341{,}808&786{,}432.
\end{array}
\]

The sum also agrees with the published total enumeration for adjacency-hopping cycles at these parameters. The program repeats the same exhaustive method for orders two through four.

**4. Independent exhaustive mechanism.** The standalone `verify_pairings.cpp` uses a different finite search space. For each of the \(24\) graph vertices, it chooses one of the two bijections between the two incoming and two outgoing edges. Therefore there are exactly \(2^{24}=16{,}777{,}216\) local choices. Each choice defines a permutation of all \(48\) directed edges; it is a single Eulerian circuit exactly when the orbit of `01010` has length \(48\). Each rooted Eulerian circuit induces one and only one such local pairing. The program checks all choices and independently reproduces precisely the same three histogram entries, with no call to the edge-walk enumerator.

**5. Attainability and the lower boundary.** The mandatory cyclic factor `01010` has three zeros and no twos, immediately giving \(D(w)\ge3\) for every qualifying word. An explicit achieving word is

`010101201202012101212010202021212102101021202102`.

Two further words of discrepancy four and five appear in `witnesses.json`. The independent `verify_witnesses.py` directly tests all forty-eight length-five cyclic factors and every interval of length one through forty-eight of each word, confirming all three exact discrepancies. The census in step 3 excludes values above five and shows every listed value is attained.

## Verification

Compile and run the two standalone C++ checkers with a C++17 compiler and execute the Python checker from the same directory as `witnesses.json`:

```sh
c++ -O2 -std=c++17 verify_dfs.cpp -o verify_dfs
./verify_dfs
c++ -O2 -std=c++17 verify_pairings.cpp -o verify_pairings
./verify_pairings
python3 verify_witnesses.py
```

The edge-walk program must print `ORDER 5 EDGES 48 CYCLES 786432 D3=23700 D4=420924 D5=341808` followed by `VERIFY_DFS_OK`. The independent local-bijection program prints `3:23700 4:420924 5:341808` and `VERIFY_PAIRINGS_OK`. The direct witness checker prints `VERIFY_WITNESSES_OK`. The source code gives the exact finite enumeration algorithms; these are exhaustive proofs of the finite census by the bijections and invariants above, rather than numerical samples or unspecified logs.

## Relationship to prior work

Chen, Liang, and Wu [1] introduced adjacency-hopping de Bruijn sequences, described their Eulerian correspondence and application to non-repetitive colored fringe coding, and derived the **total** number of circular sequences, including the value \(786{,}432\) here. That total is previously known and is not claimed as new. The present finding splits this known total into three exact discrepancy classes; the total formula alone does not determine any of these three frequencies.

Álvarez, Becher, Mereb, Pajor, and Soto [2] defined the same multicolor maximum-minus-minimum discrepancy and developed minimum-discrepancy constructions for **unrestricted** de Bruijn sequences, whose factors may contain repeated adjacent symbols. Their sequences include every ternary five-factor, have length \(243\), and therefore cannot be adjacency-hopping cycles of length \(48\). Their existence and minimum bounds do not imply this restricted full histogram. Gabrić and Sawada [3] consider **unrestricted binary** de Bruijn discrepancy; Alhakim [4] considers preference-generated **unrestricted** nonbinary cycles. Neither gives the constrained ternary five-factor census. Chen, Sima, and Milenkovic [5] use the equivalent name *Kautz sequences* and establish bounds for orthogonal **collections** of such cycles, not the within-cycle color-discrepancy frequencies of all cycles at a fixed order. The present exact statements have been compared against those primary results, including the coverage implications, rather than merely their titles.

## Limitations

The scope is only three labeled colors and order five, with rotation as the sole equivalence. The result does not establish a closed formula for every alphabet size or order, or a robustness guarantee for a physical optical instrument. Its proof is a reproducible exhaustive certificate and the correctness of the explicitly stated finite correspondences; its scientific priority remains subject to literature not indexed or inspected. It has not received independent human or external validation.

## References

[1] B. Chen, Z. Liang, S. Wu, *Adjacency-hopping de Bruijn Sequences for Non-repetitive Coding*, arXiv:2309.02841v1 (first public 2023-09-06), https://arxiv.org/html/2309.02841v1 , Definition 2 and Theorem 3.

[2] N. Álvarez, V. Becher, M. Mereb, I. Pajor, C. M. Soto, *De Bruijn Sequences with Minimum Discrepancy*, arXiv:2407.17367v1 (2024-07-24), https://arxiv.org/html/2407.17367v1 , Section 1 and Theorem 1.

[3] D. Gabrić, J. Sawada, *Investigating the discrepancy property of de Bruijn sequences*, arXiv:2005.01638v2, https://arxiv.org/html/2005.01638v2 .

[4] A. Alhakim, *Nonbinary Counterparts of the Prefer-Same and Prefer-Opposite de Bruijn Sequences*, arXiv:2206.04408v1, https://arxiv.org/html/2206.04408v1 .

[5] Y.-P. Chen, J. Sima, O. Milenkovic, *Generalized Orthogonal de Bruijn and Kautz Sequences*, arXiv:2501.12921v2 (2025), https://arxiv.org/html/2501.12921v2 , Section VI.
