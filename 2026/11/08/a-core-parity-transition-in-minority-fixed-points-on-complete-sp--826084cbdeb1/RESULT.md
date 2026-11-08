# A core-parity transition in minority fixed points on complete split graphs

## Finding
For every pair of integers \(a\ge1\), \(b\ge a\), let \(G_{a,b}=K_a\vee\overline{K_b}\) be the complete split graph with \(a\) labeled, mutually adjacent core vertices and \(b\) labeled independent peripheral vertices. Under synchronous **tie-retaining minority** dynamics, every vertex replaces its bit by the strict minority bit in its open neighborhood, retaining its bit when its neighbors are tied. Let \(U_{a,b}\) count one-step fixed configurations (not eventual fixed points). Then
\[
U_{a,b}=\begin{cases}
2,&a\text{ odd},\\
2+\binom{a}{a/2}\binom{b}{b/2},&a\text{ even},\ b\text{ even},\\
2+2\binom{a}{a/2}\binom{b}{(b-1)/2},&a\text{ even},\ b\text{ odd}.
\end{cases}
\]
For odd \(a\), the only fixed states are the two polarized configurations (the core unanimous and the periphery unanimously opposite). For even \(a\), these are joined by exactly the configurations with half of the core carrying each bit and the peripheral one-count differing by at most \(1/2\) from half of \(b\). In particular, for every fixed \(a\ge1\),
\[
\lim_{b\to\infty}\frac{\log U_{a,b}}{b}=\begin{cases}0,&a\text{ odd},\\\log2,&a\text{ even}.\end{cases}
\]
Thus changing the core size by one can change the fixed-state entropy density from zero to maximal \(\log2\) in the peripheral population.

## Assumptions and scope
The graph is finite, simple, undirected and loopless, with the stated labeled vertex partition. For a bit configuration \(x:V\to\{0,1\}\), a vertex with \(d\) neighbors of which \(s\) hold bit one updates to bit one when \(2s<d\), to bit zero when \(2s>d\), and retains its existing bit when \(2s=d\). The core size and peripheral size are integers with \(1\le a\le b\). All counts refer exclusively to configurations fixed **at time zero** by one synchronous update.

## Proof
Let \(k\) of the \(a\) core vertices and \(\ell\) of the \(b\) peripheral vertices carry bit one. Every core vertex has degree \(a+b-1\); every peripheral vertex has degree \(a\). Because all vertices within each opinion/part class have identical neighborhoods apart from themselves, the fixed-state conditions are precisely
\[
\begin{aligned}
 k>0&\implies 2(k-1+\ell)\le a+b-1,\\
 k<a&\implies 2(a-k-1+b-\ell)\le a+b-1,\\
 \ell>0&\implies 2k\le a,\\
 \ell<b&\implies 2k\ge a.
\end{aligned}
\tag{1}
\]
For a mixed core \(0<k<a\), the first two inequalities in (1) combine to
\[
a+b-1\le2(k+\ell)\le a+b+1.\tag{2}
\]
If \(k<a/2\), the peripheral zero condition in (1) forces \(\ell=b\). The upper bound in (2) gives \(2k+b\le a+1\), impossible because \(b\ge a\) and \(k\ge1\). If \(k>a/2\), the peripheral one condition forces \(\ell=0\). The lower bound in (2) gives \(2k\ge a+b-1\), impossible because \(k\le a-1\) implies \(2k\le2a-2<a+b-1\). Thus every mixed fixed core has \(k=a/2\), which requires even \(a\). Then (2) is equivalent to \(b-1\le2\ell\le b+1\). The peripheral inequalities in (1) are both equalities and impose nothing further. For even \(b\), this gives \(\ell=b/2\). For odd \(b\), this gives either \(\ell=(b-1)/2\) or \(\ell=(b+1)/2\). Each choice of \(k\) core ones and \(\ell\) peripheral ones yields \(\binom ak\binom b\ell\) labeled configurations, and these all satisfy (1).

If \(k=0\), each peripheral vertex strictly prefers one, so \(\ell=b\), and the zero core vertices remain zero since \(b\ge a-1\). If \(k=a\), each peripheral vertex strictly prefers zero, so \(\ell=0\), and the one core vertices remain one by the same inequality. These are the only two uniform-core fixed states. Summing the distinct cases proves the formula and the exhaustive classification.

For fixed even \(a\), Stirling's formula gives \(\binom b{\lfloor b/2\rfloor}=2^b\sqrt{2/(\pi b)}(1+O(b^{-1}))\). The central-layer term is positive and has that growth, multiplied by one when \(b\) is even and by two when \(b\) is odd. For fixed odd \(a\), the count is identically two. Taking logarithms proves the asserted entropy dichotomy.

## Verification
The independent exhaustive bit-level checker `verification/verify_split_direct.py` evaluated the actual synchronous update on 1,206,956 labeled initial configurations over its stated finite graph range. The separate occupancy checker `verification/verify_split_occupancy.py` summed the four necessary-and-sufficient inequalities in (1), weighted by binomial multiplicity, for 500 additional parameter pairs. Both agree with the closed formula. Run them with Python 3: `python3 verification/verify_split_direct.py` and `python3 verification/verify_split_occupancy.py`. Their captured outputs appear in `verification/split_direct_output.txt` and `verification/split_occupancy_output.txt`. The proof, not the finite tests, establishes the formula for all \(b\ge a\ge1\).

## Relationship to prior work
The uniform symmetric threshold-period framework of Goles and Olivos supplies general restrictions on possible periods but does not, in the accessible material, give this exact fixed-state census for split graphs. Wacław and Burda's 2008 metastability study treats disorder-averaged Ising spin-glass couplings; its calculation does not specialize to the deterministic, uniformly repulsive, tie-retaining complete split graph with this exact finite count. Complete split graphs also support an independent majority-dynamics census, but minority dynamics with tie retention is not a complement conjugacy of majority at the even-degree peripheral vertices responsible for the entropy transition.

## Limitations
Only time-zero fixed configurations are counted; this is not a classification of transient basins or primitive period-two states. The theorem assumes \(b\ge a\); outside that regime additional mixed-core cases can arise. The entropy limit keeps \(a\) fixed and sends \(b\) to infinity. Exhaustive checks are finite and do not prove the theorem beyond the stated tested ranges. The possibility of a prior unindexed equivalent formulation remains, particularly given limited full-text access to the original 1980 threshold-period paper. No independent external scientific audit has been performed.

## References
- J. Goles and J. Olivos, “Periodic behaviour of generalized threshold functions,” *Discrete Mathematics* **30** (1980), 187–189. General threshold-cycle framework; full text not relied on here.
- B. Wacław and Z. Burda, “Counting metastable states of Ising spin glasses on arbitrary graphs,” arXiv:0801.1224 (first public version January 8, 2008). Disorder-averaged metastability comparison.
