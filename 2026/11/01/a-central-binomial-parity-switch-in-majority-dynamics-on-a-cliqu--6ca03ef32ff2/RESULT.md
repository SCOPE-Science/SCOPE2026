# A central-binomial parity switch in majority dynamics on a clique with one leaf

## Finding
For every integer \(r\ge2\), let \(H_r\) have a clique of size \(r+1\), with a distinguished hub and an additional pendant leaf attached only to the hub. Under synchronous binary *open-neighborhood majority*, with a vertex retaining its current bit on a tie, define \(F_r\) as the update map. Define the **first periodic-entry time** \(T(x)=\min\{t\ge0:F_r^{t+p}(x)=F_r^t(x)\text{ for some }p\in\{1,2\}\}\) and let \(P(x)\in\{1,2\}\) be the eventual least period.

Put \(c_r=\binom{r}{\lfloor r/2\rfloor}\). The complete first-entry census of labelled initial bit configurations is as follows; omitted entries vanish:

| Parity of \(r\) | \(P\) | \(T\) | Number of configurations |
| --- | --- | ---: | ---: |
| Either | 1 | 0 | \(2\) |
| Either | 1 | 1 | \(2^{r+1}-2\) |
| Either | 1 | 2 | \(2^{r+1}-2c_r\) |
| Even | 1 | 3 | \(2c_r\) |
| Odd | 2 | 0 | \(2c_r\) |

**Parity switch.** When \(r\) is even, every state reaches one of the two consensus fixed points, and \(F_r^4=F_r^3\); the maximum \(T\) is sharply \(3\). When \(r\) is odd, the only recurrent states are the two consensus fixed points and exactly \(c_r\) primitive two-cycle orbits. They are already periodic at time zero; all remaining states reach consensus in at most \(2\) updates, with the sharp identity \(F_r^4=F_r^2\). In particular no transient state enters a two-cycle. In the odd case each consensus fixed point attracts \(2^{r+1}-c_r\) configurations; in the even case each attracts \(2^{r+1}\).

For uniformly independent initial bits, the probability of a three-step transient (even \(r\)), or of initial primitive period two (odd \(r\)), is exactly \(c_r/2^{r+1}\), which is asymptotic to \(1/\sqrt{2\pi r}\). The exceptional population of size \(2c_r\) moves from the terminal transient layer to the recurrent two-cycle layer as clique size changes parity.

## Assumptions and scope
All graphs are finite, simple, undirected and labelled. The hub has degree \(r+1\), every other clique vertex has degree \(r\), and the leaf has degree one. A vertex adopts bit one when more than half its current neighbors have bit one, bit zero when fewer than half do, and retains its own current bit at equality. No self-loop is included. The result covers all initial \(2^{r+2}\) labelled configurations for every integer \(r\ge2\); it does not concern random asynchronous voting or a different tie convention.

## Proof
**Symmetry reduction.** Let \(k\in\{0,\ldots,r\}\) be the number of bit-one nonhub clique vertices, and let \(h,\ell\in\{0,1\}\) denote the hub and leaf bits. Set \(s=k+h\). Since all nonhub clique vertices have the same neighbors except for themselves, the number of ones after one step is
\[
 k'= k\,\mathbf 1_{\{2(s-1)\ge r\}}+(r-k)\,\mathbf 1_{\{2s>r\}}.
\]
A nonhub one sees \(s-1\) one-neighbors; it remains one at majority or tie. A nonhub zero sees \(s\) one-neighbors; it switches only under a strict majority. The other two updates are
\[
 h'=\begin{cases}1,&2(k+\ell)>r+1,\\0,&2(k+\ell)<r+1,\\h,&2(k+\ell)=r+1,\end{cases}\qquad \ell'=h.
\]
These three exact formulas depend only on \((k,h,\ell)\), independent of which \(k\) nonhub vertices have bit one. Bit complementation sends \((k,h,\ell)\) to \((r-k,1-h,1-\ell)\), commutes with the update, and preserves \((T,P)\). Hence it is enough to analyze \(h=0\).

**Even parity.** Write \(r=2j\), where \(j\ge1\). For \(h=0\), direct substitution in the above update shows:

- If \(k\le j-1\), both leaf choices go to \((0,0,0)\) in one update.
- If \(k=j\) and \(\ell=0\), the state goes to \((0,0,0)\) in one update.
- If \(k=j\) and \(\ell=1\), the exact trajectory is \((j,0,1)\to(0,1,0)\to(0,0,1)\to(0,0,0)\), and no earlier state is periodic.
- If \(k\ge j+1\), regardless of \(\ell\), the trajectory is \((k,0,\ell)\to(r,1,0)\to(r,1,1)\), reaching the bit-one consensus fixed point after two updates.

The first case includes the bit-zero consensus state \((0,0,0)\), whose actual first-entry time is zero. Complementation gives the other half of the state space and proves that no non-consensus recurrent states exist. The explicit exceptional trajectories prove sharpness \(T_{\max}=3\) and \(F_r^4=F_r^3\).

**Odd parity.** Write \(r=2j+1\), where \(j\ge1\). For \(h=0\), the formulas give:

- If \(k\le j\), both leaf choices go to \((0,0,0)\) in one update, except the bit-zero consensus already has time zero.
- If \(k=j+1\) and \(\ell=0\), then \((j+1,0,0)\to(j,0,0)\to(0,0,0)\).
- If \(k=j+1\) and \(\ell=1\), then \((j+1,0,1)\leftrightarrow(j,1,0)\) is a primitive two-cycle. Its second state has \(h=1\), and its complement corresponds to a potentially different choice of the nonhub ones. In each arrow every nonhub bit is complemented, not merely the count, since the strict-majority tests send every nonhub one to zero and every nonhub zero to one. Consequently all labelled bits, not just the reduced triple, return after two steps; the orbit has least period two.
- If \(k\ge j+2\), both leaf choices give \((k,0,\ell)\to(r,1,0)\to(r,1,1)\).

Complementation completes the classification. In particular, every non-periodic state reaches consensus within two steps, and every periodic two-cycle state has \(T=0\). This proves \(F_r^4=F_r^2\), which is sharp for reaching the periodic part at \(T=2\).

**Exact labelled counting.** A triple with count \(k\) represents exactly \(\binom rk\) labelled states. The complement involution exchanges disjoint halves \(h=0\) and \(h=1\). For each parity, the two consensus fixed states contribute \(2\) states at time zero. Summing the two one-step cases gives \(2^{r+1}-2\) states at time one. The two-step cases give \(2^{r+1}-2c_r\) states. For even \(r\), the unique \(h=0\) three-step condition \((k,\ell)=(r/2,1)\) has \(\binom r{r/2}=c_r\) choices, doubled by complementation. For odd \(r\), the unique \(h=0\) primitive two-cycle condition \((k,\ell)=((r+1)/2,1)\) has \(\binom r{(r+1)/2}=c_r\) choices, doubled by complementation; each orbit contains precisely one configuration with \(h=0\), hence there are \(c_r\) orbits. All displayed populations sum to \(2^{r+2}\). Complement symmetry also gives the consensus basin sizes. Finally, the central binomial coefficient asymptotic \(c_r\sim2^r\sqrt{2/(\pi r)}\) proves the probability statement.

## Verification
The standalone Python script `verify_reduced.py` reconstructs the exact reduced update and checks the parity-specific case classification and every labelled first-entry count for each integer \(2\le r\le256\); it checks \(132600\) reduced triples. The independent C++ source `verify_full.cpp` builds the full adjacency matrix implicitly and evolves every one of the \(524272\) labelled configurations for all \(2\le r\le16\), using no reduced transition in its update. Its first-entry counts equal the stated formulas. The transcripts `verify_reduced.log` and `verify_full.log` record successful execution. These finite checks corroborate; the preceding algebraic case split is the proof for unbounded \(r\).

## Relationship to prior work
Goles and Olivos established eventual period at most two for synchronous binary threshold dynamics on finite undirected networks. Benjamini, Chan, O'Donnell, Tamuz and Tan (2014) address convergence and disagreement on unimodular and random graphs. Kaaser, Mallmann-Trenn and Natale (2015) derive general voting-time results and describe fast-stabilizing clique modules. Those facts motivate, but do not supply, the *sharp parity-resolved first-entry distribution* for the graph with exactly one leaf and a single perturbed clique vertex. The present proof is self-contained, and makes no claim to rediscover the general period-two principle.

## Limitations
The claim is limited to one leaf on a clique with at least three clique vertices, synchronous deterministic open-neighbor majority, and retention on ties. It does not supply a classification for multiple leaves, longer attached paths, arbitrary threshold graphs or asynchronous rules. Earlier unindexed or inaccessible sources could contain an equivalent special case; a negative literature search alone does not prove historical uniqueness. The independent formal audit remains outstanding.

## References
1. Itai Benjamini, Siu-On Chan, Ryan O'Donnell, Omer Tamuz and Li-Yang Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1 (publicly posted 2014-05-11), https://arxiv.org/abs/1405.2486.
2. Dominik Kaaser, Frederik Mallmann-Trenn and Emanuele Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519v1 (publicly posted 2015-08-14), https://arxiv.org/abs/1508.03519.
3. Eric Goles and Jorge Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1.
