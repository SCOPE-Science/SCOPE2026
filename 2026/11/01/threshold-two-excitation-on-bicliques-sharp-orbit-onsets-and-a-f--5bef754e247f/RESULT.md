# Threshold-two excitation on bicliques: sharp orbit onsets and a five-step clock

## Finding

Let \(K_{a,b}\) be a labelled complete bipartite graph with \(a,b\geq1\). In the synchronous, three-state Greenberg–Hastings model with excitation threshold two, vertices occupy states \(0\) (resting), \(1\) (excited), and \(2\) (refractory). Excited vertices advance to refractory, refractory vertices return to resting, and a resting vertex becomes excited exactly when at least two neighbors are excited. For every initial labelled configuration, let \(T\) denote the first iteration on a periodic orbit and \(p\) the eventual least period.

**Theorem.** The only possible least periods are \(1,3,4\), and \(0\le T\le5\) in every size. Period three exists precisely when \(a,b\ge6\); period four exists precisely when \(a,b\ge4\). Define
\[
H(m)=\sum_{\substack{i,j,k\ge2\\i+j+k=m}}\frac{m!}{i!j!k!},\qquad
F(m)=\sum_{j=2}^{m-2}\binom mj
\]
with empty sums equal to zero. The exact primitive-orbit counts are
\[
C_1=1,\qquad C_3=\frac{H(a)H(b)}3,\qquad C_4=\frac{F(a)F(b)}2.
\]
The unique fixed point is the all-resting configuration. The sharp maximum first-periodic-entry time is
\[
T_{\max}(a,b)=\begin{cases}
2& a=b=1,\\
3& \min(a,b)=1<\max(a,b)\ \text{or}\ a=b=2,\\
4& \min(a,b)=2<\max(a,b)\ \text{or}\ a=b=3,\\
5& \min(a,b)\ge3\ \text{and}\ \max(a,b)\ge4.
\end{cases}
\]
Thus the two nontrivial primitive periods have distinct, sharp minimum shore sizes, while the maximum transient never depends on the magnitude of either shore above four.

A complete exact first-entry/period census for every \(a,b\) is the coefficient formula below. Put \(W_0(z)=1\), \(W_1(z)=z\), and \(W_2(z)=e^z-1-z\). For each six-tuple \(s\in\{0,1,2\}^6\) with at least one nonzero coordinate among the first three and among the last three, define \(\tau(s),\pi(s)\) by the finite recurrence in the proof. Then
\[
N_{a,b}(t,p)=a!b!\,[u^av^b]
\sum_{\substack{s\in\{0,1,2\}^6\\\sum_{i=0}^2s_i>0,\ \sum_{i=3}^5s_i>0\\\tau(s)=t,\ \pi(s)=p}}
\left(\prod_{i=0}^2W_{s_i}(u)\right)
\left(\prod_{i=3}^5W_{s_i}(v)\right).
\]
The empty sum has value zero. This has only \(676\) fixed summands before filtering and is an explicit finite expression for all labelled-state counts, including all transient shells. Under independent uniform initial colors, the probability of already being in a three-cycle is \(H(a)H(b)/3^{a+b}\), which tends to one as \(\min(a,b)\to\infty\); the immediate four-cycle probability is \(2F(a)F(b)/3^{a+b}\sim2(2/3)^{a+b}\).

## Assumptions and scope

The graph is simple, loopless, finite, labelled, and genuinely complete bipartite. Each vertex updates simultaneously according to the specified deterministic three-state rule; the excitation threshold is exactly two, not one and not a fraction of the neighbor count. No assumption of balanced shores or random initial coloring is used for the deterministic conclusions. The probabilistic limit assumes each vertex initially chooses each of the three states independently with probability \(1/3\). The definition of \(T\) uses labelled configurations, rather than only the counts of state colors in each shore.

## Proof

**1. Exact finite reduction.** Partition each shore into the three cohorts of vertices initially in colors zero, one, and two. Let their six sizes be \(c_i\), with \(i=0,1,2\) in the first shore and \(i=3,4,5\) in the second. All vertices in any nonempty cohort remain in the same color at every iteration, by induction: every member has the same current color and sees the same excited population on the opposite shore. Define \(s_i=\min(2,c_i)\). Since the excitation threshold is two, for every subset of the three cohorts on a shore,
\[
\sum_{i\in S}c_i\ge2\quad\Longleftrightarrow\quad\sum_{i\in S}s_i\ge2.
\]
The six capped sizes therefore determine the entire future of the initially occupied cohorts. An absent cohort is assigned the symbol \(-1\) and is not updated. A nonempty initial cohort has color \(i\bmod3\). Write \(y_i(t)\in\{-1,0,1,2\}\) for the color of cohort \(i\) at time \(t\); define
\[
E_A(t)=\sum_{i=0}^2s_i\mathbf1_{\{y_i(t)=1\}},\qquad E_B(t)=\sum_{i=3}^5s_i\mathbf1_{\{y_i(t)=1\}}.
\]
The exact recurrence is: \(-1\mapsto-1\); \(1\mapsto2\); \(2\mapsto0\); and \(0\mapsto1\) if the corresponding opposite-shore \(E\) is at least two, otherwise \(0\mapsto0\). Both \(T\) and \(p\) for the actual labelled trajectory equal their values for the six occupied-cohort colors: the labelled state is uniquely determined by those colors, and each nonempty cohort has a vertex witness.

There are \((3^3-1)^2=676\) admissible capped-size vectors, independent of \(a,b\). Iterate the above explicit recurrence until its first repeated six-color state, defining \(\tau(s)\) as its first index and \(\pi(s)\) as its least cycle length. The accompanying `certificate.tsv` lists every vector and its two results, and `verify.py` regenerates and compares every row. Its exhaustive counts over the \(676\) vectors are

| \((\tau,\pi)\) | Number of capped-size vectors |
|---|---:|
| \((0,1)\) | 4 |
| \((0,3)\) | 1 |
| \((0,4)\) | 2 |
| \((1,1)\) | 60 |
| \((1,4)\) | 10 |
| \((2,1)\) | 324 |
| \((2,4)\) | 30 |
| \((3,1)\) | 160 |
| \((3,4)\) | 8 |
| \((4,1)\) | 51 |
| \((4,4)\) | 2 |
| \((5,1)\) | 24 |

This is an exhaustive finite proof, not an extrapolation from bounded graph sizes: the cohort correspondence above covers every possible number of vertices.

**2. Exact periodic configurations.** Among the \(676\) vectors, the only genuinely periodic signatures are the four all-resting signatures, the single signature with all six capped sizes two (period three), and the two signatures where each shore has exactly two nonempty color cohorts of capped size two, arranged in complementary excitation phases (period four). The former four signatures represent only one labelled state: all vertices resting. The period-three signature represents exactly \(H(a)H(b)\) labelled states. Each period-four signature represents \(F(a)F(b)\) states: one shore has states zero and one, the other shore states zero and two, with each of their two occupied color classes of size at least two; the other signature interchanges the shores. Every period-three orbit contains three distinct labelled states, every period-four orbit four distinct states, proving the formulas for \(C_1,C_3,C_4\) and the onset thresholds.

**3. Maximum transient and its sharpness.** A capped three-tuple \(w\) is realizable on a shore of size \(m\) exactly when \(\sum_i w_i\le m\) and either at least one entry equals two, or \(\sum_iw_i=m\). Any extra vertices can be placed into a cohort already of size at least two. For \(m\ge6\), the realizable set is exactly that for \(m=6\), so the finite matrix for \(1\le a,b\le6\) settles all larger sizes. The exact maximum-\(T\) matrix, with rows \(a=1,\ldots,6\) and columns \(b=1,\ldots,6\), is
\[
\begin{pmatrix}
2&3&3&3&3&3\\
3&3&4&4&4&4\\
3&4&4&5&5&5\\
3&4&5&5&5&5\\
3&4&5&5&5&5\\
3&4&5&5&5&5
\end{pmatrix}.
\]
Each entry is attained because only realizable signatures are included. For example, shore color-count vectors \((2,0,1)\) and \((0,2,2)\) give \(T=5\) on \(K_{3,4}\); vectors \((0,2,2)\) and \((3,0,1)\) give \(T=5\) on \(K_{4,4}\). Extra vertices can be added to any originally size-at-least-two cohort without changing the reduced orbit, proving sharpness throughout the large-size region. Reflection handles interchanged shore sizes.

**4. Complete first-entry counts.** The exponential generating function for a color cohort of capped size \(0\), \(1\), or \(2\) is respectively \(1\), \(z\), or \(e^z-1-z\). Multiplying for all three color cohorts on each shore and extracting coefficients counts each labelled initial configuration exactly once. Restricting to the signatures having \((\tau,\pi)=(t,p)\) gives the claimed coefficient formula. The sum over \(t,p\) equals \(3^{a+b}\). Finally, a binomial union bound proves \(H(m)/3^m\to1\), and \(F(m)\sim2^m\), giving the stated typical-state asymptotics.

## Verification

Execute `python verify.py` alongside the included `certificate.tsv`, using Python's standard library. The verifier recomputes every one of the \(676\) exact finite signatures, its first repetition time and least period, checks the twelve-class histogram, checks the sharp size table and primitive-period onsets, and uses exact multinomial sums to verify the periodic-state formulas and total census for all \(1\le a,b\le6\). A second implementation iterates actual labelled vertex configurations for every \(1\le a,b\le4\) and for \(a=b=5\), comparing \((T,p)\) against the independently constructed six-cohort model on all \(73,449\) configurations. The included `verification_output.txt` records the successful execution. The all-size conclusion relies on the exact capped-cohort proof plus the exhaustive finite certificate, not on the bounded labelled-state experiments.

## Relationship to prior work

The three-state Greenberg–Hastings model and its contact threshold parameter are established; see Fisch–Gravner–Griffeath [1]. Gravner–Lyu–Sivakoff [2] classify qualitative behavior for threshold-one GHM on arbitrary finite graphs, not the threshold-two full finite-time orbit census. Bello–Sivakoff [3] investigate threshold at least two on infinite regular trees, rather than finite bicliques. An existing exact threshold-one biclique classification finds the same possible primitive period values but different size conditions and different counts; changing the activation threshold does not preserve that statement. A prior threshold-two census on crown graphs concerns the distinct graph \(K_{n,n}\) with a perfect matching removed, which can have primitive periods six, ten, twelve, and thirty, so it neither implies nor is implied by the present biclique classification. The contribution here is the all-size threshold-two sharp onset, orbit census, and five-step first-entry law, not the GHM definition.

## Limitations

Only three states, the synchronous update, excitation threshold exactly two, and complete bipartite graphs are covered. The coefficient formula is finite and exact but not simplified to a short closed form separately for every one of the twelve nonempty \((T,p)\) classes. The certificate is computationally finite and replayable; it is not an independent human audit or a formal proof-assistant artifact. Literature searching cannot exclude an unindexed historical equivalent. The 1991 journal paper cited in [1] predates its exactly dated 1993 arXiv submission; no specific 1991 public day is asserted.

## References

1. R. Fisch, J. Gravner and D. Griffeath, *Threshold-range scaling of excitable cellular automata*, Statistics and Computing **1** (1991), 23–39, DOI: 10.1007/BF01890834; arXiv:patt-sol/9304001v1, publicly posted 1993-04-02, https://arxiv.org/abs/patt-sol/9304001. Accessible author copy: https://www.math.ucdavis.edu/~gravner/papers/fgg.pdf.
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, posted 2016-10-24, https://arxiv.org/html/1610.07320v1.
3. J. Bello and D. Sivakoff, *Cyclic Cellular Automata and Greenberg-Hastings Models on Regular Trees*, arXiv:2108.06404, posted 2021-08-13, https://arxiv.org/abs/2108.06404.
