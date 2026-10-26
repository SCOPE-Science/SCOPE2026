# Support-refined enumeration of ternary cyclic dinucleotide profiles

## Finding
For each integer \(n\ge1\) and word \(w=(w_0,\ldots,w_{n-1})\in\{0,1,2\}^n\), read indices modulo \(n\) and set
\[
m_{ij}(w)=\#\{t:0\le t<n,\ (w_t,w_{t+1})=(i,j)\}\quad(0\le i,j\le2).
\]
A **profile** is the full ordered matrix \(m(w)=(m_{ij}(w))\), with equal matrices identified regardless of how many words realize them. Its **off-diagonal support size** is \(s(m)=\#\{(i,j):i\ne j,\ m_{ij}>0\}\). Let \(p_{n,s}\) count distinct realizable profiles with this support size. With
\[
L=\frac{z}{1-z},\qquad H=\frac{u^2z^2}{1-z^2},
\]
the complete bivariate generating function is
\[
\boxed{\sum_{n\ge1}\sum_{s=0}^6p_{n,s}z^nu^s
=3L+\frac{3H}{(1-z)^2}+\frac{1}{(1-z)^3}
\left[\frac{2u^3z^3}{1-z^3}\left(1+\frac{uz^2}{1-z^2}\right)^3+3H^2+H^3\right].}
\]
Consequently the only possible off-diagonal support sizes, as \(n\) ranges over positive integers, are \(0,2,3,4,5,6\). Their first possible lengths are respectively \(1,2,3,4,7,6\). Setting \(u=1\) counts all realizable profiles; the first fifteen totals, at lengths \(1\) through \(15\), are
\[
3,6,11,24,48,95,174,306,510,819,1266,1901,2775,3960,5531.
\]
These are also the maximum cardinalities of codes transmitting through the channel that reveals only the complete cyclic adjacent-pair multiplicity profile.

## Assumptions and scope
The alphabet has three **labeled** symbols. A word is cyclically closed for profiling, but rotations are not separately counted as different profiles. Repeated ordered pairs contribute their multiplicity, and loops \((i,i)\) do **not** contribute to the support statistic \(s\). Formulae hold formally over \(\mathbb Z[u][[z]]\), including \(n=1\) and words using fewer than three letters. A codebook contains at most one word for each profile under zero-error reconstruction and one representative can be chosen for each realizable profile.

## Proof
**1. Characterize realizability.** To any nonnegative integer matrix \(m\) associate a directed multigraph on \(\{0,1,2\}\), with \(m_{ij}\) parallel arcs \(i\to j\). A word produces a closed Euler walk of length \(n\), and therefore its matrix has equal row and column sums and connected underlying undirected graph after vertices of degree zero are discarded. Conversely, these two conditions are sufficient: every balanced weakly connected finite directed multigraph with at least one arc has an Euler circuit, whose sequence of tails realizes the matrix. A positive loop alone on one vertex is allowed.

**2. Parametrize all balanced off-diagonal matrices uniquely.** Write the three oriented pairs as \((0,1),(1,2),(2,0)\), and let their reverse pairs be \((1,0),(2,1),(0,2)\). Flow conservation is exactly
\[
m_{01}-m_{10}=m_{12}-m_{21}=m_{20}-m_{02}=t
\]
for some integer \(t\). For unique nonnegative integers \(x,y,v\), the forward multiplicities are \(x+t_+,y+t_+,v+t_+\) and reverse multiplicities are \(x+t_-,y+t_-,v+t_-\), with \(t_+=\max(t,0)\), \(t_-=\max(-t,0)\). The three diagonal multiplicities are independent nonnegative integers. The signs and the number of positive \(x,y,v\) determine \(s\).

**3. Exactly one active symbol.** All off-diagonal counts vanish, and precisely one diagonal entry is positive. The contribution is \(3L\), with \(s=0\).

**4. Exactly two active symbols.** There are three choices of the unordered pair. On that pair, conservation forces equal **positive** multiplicities in opposite directions, contributing \(H=u^2z^2/(1-z^2)\); both diagonal entries may be arbitrary, contributing \((1-z)^{-2}\). Hence \(3H/(1-z)^2\). A third isolated vertex with a positive loop would not be realizable by a single word and is not included.

**5. All three active symbols, nonzero circulation.** For \(t\ne0\), the oriented triangle has \(3|t|\) arcs, exactly three distinct nonloop arc types, and guarantees connectivity. Each pair of opposing directions may additionally acquire \(x\ge0\) matched arc pairs, which introduces the reverse arc type if \(x>0\). Therefore the contribution before loops is
\[
2\sum_{t\ge1}u^3z^{3t}\left(1+\frac{uz^2}{1-z^2}\right)^3
=\frac{2u^3z^3}{1-z^3}\left(1+\frac{uz^2}{1-z^2}\right)^3.
\]
There are two orientations, not six, because the alphabet vertices remain labeled.

**6. All three active symbols, zero circulation.** When \(t=0\), each pair \((i,j)\) is represented by a bidirectional link with equal multiplicity. It contributes \(H\) when positive. On three vertices the underlying graph is connected precisely when at least two of the three links are present. The corresponding polynomial is \(3H^2+H^3\). In the three-active-symbol cases all three loop multiplicities are unrestricted, multiplying by \((1-z)^{-3}\). This proves the displayed identity with no double counting.

**7. Support spectrum and ordinary totals.** The contributions show supports \(0,2,3,4,5,6\) occur, and \(1\) cannot occur. Their minimal lengths follow by choosing no loops and minimum positive arc multiplicities: respectively \(1,2,3,4,7,6\). Setting \(u=1\), formal power-series simplification yields the previously known three-symbol balanced-matrix series minus disconnected matrices:
\[
\sum_{n\ge1}\left(\sum_sp_{n,s}\right)z^n
=\frac{1-z+z^2}{(1-z)^7(1+z)^2(1+z+z^2)}-1-3L^2-L^3-\frac{3Lz^2}{(1-z)^2(1-z^2)}.
\]
The first rational term counts every balanced matrix (including disconnected matrices). Its disconnected correction consists of two loop-only components, three loop-only components, or one loop-only component plus a connected two-symbol component. This specialization is included to connect the refinement to earlier enumeration; it is not claimed as a new unrefined balanced-matrix formula. The code-size conclusion follows because the channel identifies exactly the words with identical profiles.

## Verification
The companion standalone file `verify.py` expands the theorem by integer sums and independently enumerates (a) all ternary words at lengths \(1\) through \(11\) and (b) all flow-conserving matrix entries, with a separate graph-connectivity test, at lengths \(1\) through \(14\). It checks the full \(s\)-refined distribution, not only total coefficients. The observed success token is `TERNARY_SUPPORT_REFINEMENT_PASS`. An explicit example: at length \(7\), the support counts \((s:p_{7,s})\) are \((0:3),(2:36),(3:36),(4:90),(5:6),(6:3)\); their sum is \(174\). Finite replay checks the implementation, while steps 1–7 prove the identity for all lengths.

## Relationship to prior work
Jacquet, Knessl, and Szpankowski (2010; expanded 2012), *Counting Markov Types*, derive the exact generating function of all balanced frequency matrices for alphabet size three and show that feasible cyclic Markov types correspond to Eulerian directed graphs; their main enumeration addresses unrefined totals and asymptotics. Their all-balanced series is explicitly reused above. The **new claim** is the joint all-length length/off-diagonal-support generating function, with explicit support sizes and thresholds, including corrections for disconnected support. Beeri and Schwartz (arXiv:2101.06033, first public 2021-01-15) investigate rank-based DNA sequence profiles and Eulerian feasibility, not this support-refined numerical profile census. Kiah, Puleo, and Milenkovic discuss DNA sequence profile codes and asymptotic enumerations, without this ternary bivariate law.

## Limitations
Only three labeled symbols and cyclic reads of length two are treated. The result counts distinct profiles, not the number of original words or Euler circuits per profile. It does not estimate noise robustness, and it does not provide an algorithmic construction beyond selecting an Euler tour per profile. The unrefined balanced-matrix generating function and general Eulerian graph criterion are prior results, not independent contributions.

## References
1. P. Jacquet, C. Knessl, W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM (2010), https://www.cs.purdue.edu/homes/spa/papers/aofa10.pdf , doi:10.46298/dmtcs.2768.
2. P. Jacquet, C. Knessl, W. Szpankowski, *Counting Markov Types, Balanced Matrices, and Eulerian Graphs*, IEEE Transactions on Information Theory 58 (2012), https://www.cs.purdue.edu/homes/spa/papers/it12-types.pdf , doi:10.1109/TIT.2012.2191476.
3. N. Beeri, M. Schwartz, *Improved Rank-Modulation Codes for DNA Storage with Shotgun Sequencing*, arXiv:2101.06033 (2021), https://arxiv.org/pdf/2101.06033.
4. H. M. Kiah, G. J. Puleo, O. Milenkovic, *Codes for DNA Sequence Profiles*, https://personal.ntu.edu.sg/hmkiah/docs/papers/DNA_seq_profile_ISIT.pdf.
