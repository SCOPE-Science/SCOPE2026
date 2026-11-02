# Exact finite-length capacity of the linear binary three-gram spectrum

## Finding

For a binary word \(w=w_1\ldots w_n\) of length \(n\ge3\), let \(N_{abc}(w)\) be the number of positions \(1\le i\le n-2\) at which the contiguous ordered factor is \(w_iw_{i+1}w_{i+2}=abc\). Define its complete (multiplicity-preserving) linear three-gram profile by
\[
P(w)=(N_{000},N_{001},N_{010},N_{011},N_{100},N_{101},N_{110},N_{111}).
\]
Let \(A_n=|\{P(w):w\in\{0,1\}^n\}|\). For \(m=n-2\) the exact generating function is
\[
\boxed{\sum_{m\ge0}A_{m+2}z^m=\frac{1+6z-z^2-z^3+4z^4+5z^5+9z^6+4z^7-3z^9+2z^{11}}{(1-z)^2(1-z^2)(1-z^3)(1-z^4)}.}
\]
At the formal boundary \(m=0\), set \(A_2=1\), since no three-gram is observed. For \(n\ge3\), \(A_n\) is exactly the maximum number of codewords admitting unique decoding from their complete linear three-gram multiset: any two words with the same profile are observationally indistinguishable, and taking one representative of each profile achieves the bound. The first values for lengths \(3\) through \(12\) are \(8,15,28,52,92,151,240,363,532,757\).

The reduced rational function has uncancelled poles at primitive third and fourth roots of unity and a fifth-order pole at one. Thus \(A_n\) is a degree-four quasipolynomial of **least period twelve**, with
\[
A_n=\frac{13}{288}n^4+O(n^3).
\]

## Assumptions and scope

The alphabet is labeled \(\{0,1\}\); a factor retains **its order**, not merely its weight. All length-three factors are contiguous and overlapping; the first and last positions are **not** identified cyclically, and the word endpoints are not supplied separately to the observer. Repeated reads are counted with multiplicity. The theorem counts realizable profile vectors, not the number of words in each profile fiber. It assumes no noise or missing reads.

## Proof

**1. Flow representation and connectivity.** Use the order-two binary de Bruijn digraph with vertex set \(\{00,01,10,11\}\). Its eight labeled edges are
\[
\begin{array}{c|cccccccc}
\text{label}&000&001&010&011&100&101&110&111\\
\text{edge}&00\to00&00\to01&01\to10&01\to11&10\to00&10\to01&11\to10&11\to11.
\end{array}
\]
Denote the corresponding nonnegative counts by \((a,b,c,d,e,f,g,h)\), and let \(\delta_v\) be the number of departures from vertex \(v\) minus arrivals. A linear word gives an Euler walk from its first two symbols to its last two. Hence either every \(\delta_v=0\), or exactly one equals \(+1\), another equals \(-1\), and the others vanish. Conversely, the directed Euler-trail criterion gives a realizing word whenever these degree conditions hold and the nonzero-edge support is weakly connected.

There are only four nonloop vertices; every directed nonloop cycle contains both vertices `01` and `10`. Every nonempty nonloop directed path touches at least one of these two vertices. Under the stated degree pattern, every weak component of the nonloop support other than a possible endpoint-trail component must be Eulerian, hence contains a cycle. Therefore any two nontrivial weak components would meet at `01` or `10`, a contradiction. Thus the nonloop support, whenever nonempty, is weakly connected. The **only** extraneous balanced objects are self-loops at `00` or `11` detached from that support. In an empty nonloop support, only one of these two kinds of loops can occur in a realizable word. These are precisely the connectivity exclusions below.

**2. Integer parameterization.** Conservation gives
\[
 e=b-\delta_{00},\qquad g=d+\delta_{11},\qquad c=b+f-d+\delta_{01},
\]
with the fourth equation redundant, and the total number of edges is
\[
 m=a+h+3b+2f+d+\delta_{01}-\delta_{00}+\delta_{11}.
\]
One may choose nonnegative \(b,d,f,a,h\), subject to nonnegativity of \(e,g,c\) and to the indicated loop attachment. The vector \(\delta\) is recoverable from the profile itself. Thus profiles with distinct nonzero endpoint divergences never overlap, whereas all balanced profiles must be counted just **once**, regardless of how many starting vertices admit an Euler circuit.

Reversing every word and complementing all bits preserve both realizability and the number of edge counts. They partition the twelve nonzero ordered endpoint pairs into four orbit types, of sizes two, four, four and two, represented by `00→11`, `00→01`, `00→10` and `01→10` respectively.

**3. Two elementary constrained sums.** Put
\[
P(z)=(1-z^2)(1-z^3)(1-z^4),\qquad
U(z)=\sum_{\substack{b,d,f\ge0\\d\le b+f}}z^{3b+2f+d}=\frac{1+z^3}{P(z)},
\]
\[
V(z)=\sum_{\substack{b,d,f\ge0\\d\le b+f+1}}z^{3b+2f+d}=\frac{1+z}{P(z)}.
\]
Both identities follow by summing the finite geometric series in \(d\), then the independent geometric series in \(b,f\). Define the following auxiliary functions:
\[
K=\frac1{(1-z^2)(1-z^3)},\quad B=z^3K,\quad E=zK,\quad H=U-\frac1{1-z^2}-2B,\quad J=V-\frac1{1-z^2}-B-E.
\]
Here \(H\) enumerates balanced nonloop supports with both \(b>0\) and \(d>0\); \(J\) enumerates the analogous supports for the `01→10` divergence. A loop at `00` is permitted exactly when the nonloop support touches `00`; likewise at `11`. The two same-symbol loops cannot both be present without a connecting nonloop support.

**4. Exhaustive endpoint classes.** For balanced profiles, the generating series is
\[
 C=\frac{H}{(1-z)^2}+\frac{2B}{1-z}+\frac{z^2}{1-z^2}+1+\frac{2z}{1-z}.
\]
The four terms distinguish connected nonloop supports touching both loop vertices, touching just one, the pure `01↔10` alternating cycles, and pure constant loops (including the empty profile). For the four representative nonzero endpoint classes, the corresponding series are
\[
T_1=\frac{z^{-2}H}{(1-z)^2} \quad(00\to11),
\]
\[
T_2=z^{-2}\left(\frac{B}{1-z}+\frac{z^3U-B}{(1-z)^2}\right) \quad(00\to01),
\]
\[
T_3=z^{-1}\left(\frac{B}{1-z}+\frac{U-K-B}{(1-z)^2}\right) \quad(00\to10),
\]
\[
T_4=z\left(\frac{J}{(1-z)^2}+\frac{B+E}{1-z}+\frac1{1-z^2}\right) \quad(01\to10).
\]
Every displayed expression is a formal power series: the apparent negative powers cancel against zeros in the numerators. For \(T_1\), both \(b,d\) are positive; for \(T_2,T_3\), \(b>0\) with \(d=0\) or \(d>0\) separated; and for \(T_4\), the cases \(b,d>0\), exactly one positive, or both zero, are disjoint. The geometric factors \((1-z)^{-1}\) count attached-loop multiplicities, while \(z^{-2},z^{-1},z\) are exactly the divergence-dependent edge-count shifts from Step 2. These cases include every feasible profile once and no disconnected-loop object.

Consequently, multiplying by the four endpoint orbit sizes gives
\[
G(z)=C(z)+2T_1(z)+4T_2(z)+4T_3(z)+2T_4(z).
\]
Substitute the rational forms of \(U,V,K,B,E,H,J\), combine denominators and simplify to obtain the boxed generating function. Every candidate counted by these terms satisfies the Euler-trail criterion, so the counting is both necessary and sufficient, not a mere flow relaxation.

**5. Quasipolynomial and leading constant.** The displayed denominator factors into powers of \((1-z)\) and cyclotomic factors with root orders two, three, and four, so the coefficients for every \(m\ge1\) form a degree-at-most-four quasipolynomial of period dividing twelve. The numerator cancels exactly one factor \((1+z)\); it does not cancel the primitive third- or fourth-root factors. The pole at \(z=1\) has order five with leading coefficient
\[
\lim_{z\to1}(1-z)^5G(z)=\frac{13}{12}.
\]
Therefore the leading term is \(\frac{13}{12}\binom{m+4}{4}=\frac{13}{288}m^4+O(m^3)\), and hence the same leading term with \(m=n-2\). The nonvanishing primitive third- and fourth-root terms require periods divisible by three and four respectively, establishing least period twelve.

## Verification

The companion `VERIFY.py` uses only the Python standard library. It reconstructs rational-series coefficients by integer polynomial recurrence; independently enumerates all \(2^n\) linear binary words through length sixteen and counts their complete eight-coordinate read profiles; and independently enumerates all nonnegative eight-edge count vectors through sixteen edges and accepts precisely those meeting the Euler balance and weak-connectivity criteria. For all feasible profiles with up to nine edges it also constructs and rechecks an Euler-trail word witness. Results: exact agreement in every checked case, 1,481 short Euler witnesses, and 71 integer series coefficients reconstructed. Invocation: `python3 VERIFY.py` (success prints `VERIFY_OK`). These are finite corroborations. The general proof is the flow classification and series summation above.

## Relationship to prior work

Kiah, Puleo and Milenkovic, *Codes for DNA Sequence Profiles* (2015), formalize ordered length-\(\ell\) read-count profiles and use restricted de Bruijn graphs. Their Theorem 3.3 proves quasipolynomial degree and a period divisor for the balanced-flow bounding families on a strongly connected allowed-factor graph; the realizable profile count is bounded between these families. It does **not** give the present unrestricted binary length-three exact numerator or all finite coefficients. Its degree-four and period-at-most-twelve bounds are consistent with the present calculation.

Jacquet, Knessl and Szpankowski, *Counting Markov Types* (2010), count order-one Markov types by a balanced adjacency matrix and analyze their asymptotics. The four-vertex, order-two de Bruijn edge profile here has additional overlap restrictions and permits nonzero start/end divergence, so their binary order-one result does not imply the present formula. Yehezkeally, Marcovich and Yaakobi, *Multi-strand Reconstruction from Substrings* (2021), establish the full length-\(\ell\) read multiset model and asymptotic multi-strand codes, rather than an exact finite-length single-strand length-three profile count.

The corresponding exact cyclic binary length-three profile count is a strictly balanced-flow subproblem: appending two initial bits to a cyclic word realizes its balanced read vector linearly, but the unbalanced endpoint-divergence types create further linear profiles. Replacing ordered three-grams with their Hamming weights also loses information: a known linear three-window composition-histogram count is a coarser quotient and cannot determine the eight-coordinate count.

## Limitations

This establishes exact **profile capacity**, not the number of preimage words per profile or efficient recovery under substitution or erasure errors. The first-public date associated with the guiding reconstruction model belongs to that source, not to this theorem. No independent external scientific validation has been performed. An unindexed exact enumeration under higher-order Markov-type or DNA sequencing terminology is a residual originality risk; this work does not establish uniqueness by absence of search hits.

## References

1. Y. Yehezkeally, S. Marcovich, E. Yaakobi, *Multi-strand Reconstruction from Substrings*, arXiv:2108.11725, version 1 publicly posted August 26, 2021. https://arxiv.org/abs/2108.11725
2. H. M. Kiah, G. J. Puleo, O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1502.00517, publicly posted February 2, 2015. https://arxiv.org/abs/1502.00517
3. P. Jacquet, C. Knessl, W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings (2010), DOI 10.46298/dmtcs.2768. https://dmtcs.episciences.org/articles/2768
