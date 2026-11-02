# Period-three predecessor law and constrained image entropy for cyclic Rule 22

## Finding

Consider one synchronous update of elementary cellular automaton Rule 22 on an indexed binary ring of arbitrary length \(n\ge1\). The local output is 1 exactly when precisely one of the three input sites (counted as neighbors with multiplicity on rings of size 1 or 2) is 1. Restrict attention to output rings with **no adjacent cyclic zeros**. The following gives a complete inverse-fiber characterization and an exact all-length count of the image within that constraint.

For any such output \(y\) with at least one zero, write \(a_1,\ldots,a_m\ge1\) for its successive cyclic lengths of runs of ones between its \(m\) zero sites. Define

\[
T_0=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
T_1=\begin{pmatrix}0&0\\0&1\end{pmatrix},\quad
T_2=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Its number of same-ring predecessors is exactly

\[
\nu_n(y)=\operatorname{tr}\bigl(T_{a_1\bmod3}\cdots T_{a_m\bmod3}\bigr).
\]

In particular, \(\nu_n(y)\in\{0,1,2\}\), and \(\nu_n(y)=2\) precisely when all the gaps are \(2\bmod3\) and \(m\) is even. The exceptional all-ones output has three predecessors if \(3\mid n\), and none otherwise. These statements also give a constructive existence test: follow each nonzero transition in the two-state matrix product around the ring.

Let \(B_n\) be the number of **distinct indexed** output configurations avoiding cyclic `00` and possessing at least one predecessor on the same \(n\)-site ring. Let \(t_0=3\), \(t_1=t_2=1\), and \(t_n=t_{n-1}+t_{n-3}\) for \(n\ge3\). Then for every \(n\ge1\),

\[
\boxed{B_n=t_n+(-1)^n+\mathbf1_{3\mid n}\left(1-3\cdot2^{n/3-1}\right).}
\]

Equivalently, the exact ordinary generating function is

\[
\boxed{\sum_{n\ge1}B_nz^n=
\frac{z(1+3z^2)}{1-z-z^3}-\frac{z}{1+z}
-\frac{2z^3}{1-z^3}-\frac{3z^6}{(1-z^3)(1-2z^3)}.}
\]

Among the zero-containing constrained outputs, exactly \(3(2^{k-1}-1)\) have two predecessors when \(n=3k\), and none have two predecessors if \(3\nmid n\). If \(\lambda\) is the real root of \(\lambda^3-\lambda^2-1=0\), approximately \(1.465571231876768\), then

\[
B_n=\lambda^n+O(2^{n/3}).
\]

Since the number of *all* cyclic `00`-avoiding words has growth \(\asymp\varphi^n\), where \(\varphi=(1+\sqrt5)/2\), the reachable proportion within this constrained output family decreases exponentially with rate \(\lambda/\varphi\).

## Assumptions and scope

A configuration is a function \(\mathbb Z/n\mathbb Z\to\{0,1\}\) with labelled sites. The update map is

\[
F_n(x)_i=\mathbf1\{x_{i-1}+x_i+x_{i+1}=1\}.
\]

For the shortest rings the three summands may refer to the same input site, but the formula still applies literally. Cyclic `00` avoidance means there is no \(i\in\mathbb Z/n\mathbb Z\) with \(y_i=y_{i+1}=0\); consequently for \(n=1\) the all-zero word is excluded. Words are not identified up to rotation or reversal. Every predecessor is required to have exactly the same ring length, with no enlargement of its spatial period.

## Proof

**1. Four-state labelled predecessor graph.** The standard two-bit states of the de Bruijn graph are `00`, `01`, `10`, `11`. A length-three input block labels an edge from its first two bits to its last two bits, with output equal to the Rule-22 value. The complete lists of labelled edges are:

- Output `1`: `00 -> 01`, `01 -> 10`, `10 -> 00`.
- Output `0`: `00 -> 00`, `01 -> 11`, `10 -> 01`, `11 -> 10`, `11 -> 11`.

A cyclic length-\(n\) labelled predecessor path is in bijection with an input configuration of length \(n\), including \(n=1,2\), because successive two-bit windows uniquely reconstruct all its bits. Therefore the number of predecessors of a specified output is the number of closed walks with its prescribed edge labels.

**2. Reduction between isolated zeros.** Suppose the cyclic output has a zero followed by \(a\ge1\) ones and then another zero. Immediately before the zero-labelled edge, any path continuing to a positive run of ones, as well as arriving after a positive run, must use one of the states `00` or `10`: the incoming one-edge lies on the three-cycle `00 -> 01 -> 10 -> 00`, and starting a zero-edge from `01` would enter `11`, from which an immediately following one-edge is impossible. The zero edge followed by \(a\) one-edges consequently acts on the surviving ordered states (`00`, `10`) by the matrices \(T_{a\bmod3}\) displayed above. Explicitly, for a zero-plus-ones block, a run of ones of length \(0\bmod3\) retains only `00`, of length \(1\bmod3\) retains only `10`, and of length \(2\bmod3\) swaps them. This follows directly by traversing the one-edge three-cycle.

Each cyclic output with zeros is a concatenation of such blocks; closed predecessor paths therefore correspond bijectively to diagonal entries in the resulting product, establishing the trace formula. Each \(T_r\) is a partial permutation on a two-element set. A product containing either of the rank-one matrices \(T_0,T_1\) has trace at most one; a product of only \(T_2\) has trace two if the number of factors is even and zero if it is odd. This proves the precise two-predecessor classification. For the all-ones output, only the three-edge cycle is available, yielding three closed paths when \(3\mid n\) and zero otherwise.

**3. Exact indexed count from gap cycles.** Attach an auxiliary weight \(z^{a+1}\) to a block consisting of one zero and \(a\ge1\) following ones. Summing these weights by residue gives

\[
g_0=\frac{z^4}{1-z^3},\qquad g_1=\frac{z^2}{1-z^3},\qquad g_2=\frac{z^3}{1-z^3}.
\]

Define the symmetric matrix

\[
U=\begin{pmatrix}g_0&g_2\\g_2&g_1\end{pmatrix}.
\]

For each \(m\ge1\), the trace \(\operatorname{tr}(U^m)\) sums the number of predecessors over ordered \(m\)-tuples of positive gaps. A monomial of degree \(n\), divided by \(m\) and then multiplied by \(n\), counts its contribution to labelled length-\(n\) ring outputs: every indexed output has \(m\) distinguished choices of zero site and \(n\) placements for that mark. This remains valid for periodic gap tuples because the counting is by labelled marks rather than free necklace orbits. Thus

\[
z\frac{d}{dz}\sum_{m\ge1}\frac{\operatorname{tr}(U^m)}m
= z\frac{d}{dz}\bigl[-\log\det(I-U)\bigr]
\]

is the generating function for the **total** number of predecessors, not yet the number of distinct reachable outputs. The only overcount within the zero-containing constrained family occurs when all \(m\) gaps have residue 2 and \(m\) is even. Such words have exactly two predecessors; subtract one copy of each. Their weighted correction, before applying \(z\,d/dz\), is

\[
-\sum_{j\ge1}\frac{g_2^{2j}}{2j}=\frac12\log(1-g_2^2).
\]

Finally the all-ones output is one distinct reachable word for every positive multiple of three. Therefore

\[
\sum_{n\ge1}B_nz^n
=z\frac{d}{dz}\left[-\log\det(I-U)+\frac12\log(1-g_2^2)\right]
+\frac{z^3}{1-z^3}.
\]

The formal power-series identity

\[
\det(I-U)=\frac{(1+z)(1-z-z^3)}{1-z^3}
\]

reduces this expression by differentiation to the stated rational generating function. All logarithms are formal power series with unit constant term, so no analytic convergence assumption is needed for the enumeration.

**4. Coefficients and asymptotics.** The first rational summand has coefficients \(t_n\), by the characteristic recurrence of \(1-z-z^3\) and initial values \(3,1,1\). The remaining terms contribute \((-1)^n\), and, at length \(n=3k\), \(1-3\cdot2^{k-1}\). This proves the closed formula for every positive \(n\). Double-predecessor outputs are exactly the all-residue-two even-gap tuples; their ordinary generating function is the negative correction calculated in step 3, giving \(3(2^{k-1}-1)\) when \(n=3k\). The denominator \(1-z-z^3\) has the unique dominant positive reciprocal root \(\lambda\), while the other terms contribute at most \(O(2^{n/3})\). This proves the exponential estimate and the constrained-image entropy comparison.

## Verification

The complete independent finite checker `verify.py` is embedded alongside this manuscript and runs with Python 3 standard library only. It independently enumerates every input and target output word on each indexed ring of length 1 through 17; compares direct predecessor counts to the two-state matrix formula; checks \(B_n\) and the exact doubled-fiber classification; and compares rational-series coefficients to the closed formula through degree 120. Replaying it prints `VERIFY_OK`. Direct enumeration is a finite consistency check only; the graph and formal-series arguments above establish the unrestricted-length statements.

The first indexed counts are \(B_1,\ldots,B_{17}=0,2,1,6,5,6,14,22,19,47,66,76,143,212,261,454,663\).

## Relationship to prior work

Jen (1989) gives classical Rule-22 preimage enumeration for linear blocks and the underlying recurrence machinery, but not the present period-matched isolated-zero fiber and all-length distinct indexed image count. Voorhees (1997) explicitly reports \(1.46557\) as a Rule-22 zero-label de Bruijn spectral radius. **That numerical constant and the general matrix approach are not claimed as new.** Gravner and Griffeath's work (online 2010) analyzes the exactly-one automaton from finite seeds and periodic dynamics, not the complete one-step inverse distribution under cyclic `00` avoidance. Martínez and collaborators (2019) give an extensive Rule-22 study, including de Bruijn and subset diagrams and regular expressions for Garden-of-Eden patterns. Those results provide broad algorithmic information, but the inspected reachability sections do not state the explicit cyclic fixed-period predecessor dichotomy or the closed count here. The 2019 paper remains an important potential route for deriving special-case implications; the historical-priority assessment is not independently certified.

## Limitations

The conclusion is restricted to **one** synchronous update and output words avoiding **cyclic** `00`. The total unrestricted image size, long-time dynamics and arbitrary-output predecessor multiplicities are not determined. The formula counts indexed rings, not rotation equivalence classes. As standard in finite-state symbolic dynamics, the general de Bruijn method is pre-existing; the contribution is the explicit constrained reduction, fiber dichotomy and distinct-image enumeration. Source comparisons are bounded and do not exclude inaccessible or unindexed historically equivalent results. No independent audit has been performed.

## References

1. E. Jen, *Enumeration of Preimages in Cellular Automata*, Complex Systems 3 (1989), 421–456. https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf
2. B. Voorhees, *Some Parameters Characterizing Cellular Automata Rules*, Complex Systems 11 (1997), 373–385. https://wpmedia.wolfram.com/sites/13/2018/02/11-5-3.pdf
3. J. Gravner and D. Griffeath, *The One-Dimensional Exactly 1 Cellular Automaton: Replication, Periodicity, and Chaos from Finite Seeds*, Journal of Statistical Physics (online December 10, 2010). https://doi.org/10.1007/s10955-010-0103-9
4. G. J. Martínez et al., *On Patterns and Dynamics of Rule 22 Cellular Automaton*, Complex Systems 28 (2019), 125–174. https://doi.org/10.25088/ComplexSystems.28.2.125
