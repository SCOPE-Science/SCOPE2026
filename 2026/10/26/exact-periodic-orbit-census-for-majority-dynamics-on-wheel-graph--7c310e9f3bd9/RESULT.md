# Exact periodic-orbit census for majority dynamics on wheel graphs

## Finding

Let \(W_n\) be the labelled wheel with rim vertices \(0,\ldots,n-1\) (indices modulo \(n\)) and a distinguished hub, where \(n\ge3\). Every vertex synchronously takes the strict majority of its neighbours' binary states; if a tie occurs, it retains its own state. Let \(F\) denote the resulting map on \(\{0,1\}^{n+1}\).

There are exactly two fixed points (the unanimous states). Every other periodic point has least period two. Put
\[
Q_L(u,v)=1+u^Lv^L+\sum_{\substack{b\ge1,\ s\ge2b,\ L-s\ge b}}
 \frac{L}{b}\binom{s-b-1}{b-1}\binom{L-s-1}{b-1}u^s v^{s-b},\qquad L\ge2,
\]
where the sum ranges over integers \(b,s\). Define \(R_n(u,v)=Q_n(u,v)\) if \(n\) is odd and \(R_n(u,v)=Q_{n/2}(u,v)^2\) if \(n\) is even. Let
\[
H_n=\sum_{\substack{0\le s,e\le n\\2s>n,\ 2e<n}}[u^sv^e]R_n(u,v).
\]
Then \(H_n\) is **exactly** the number of primitive period-two orbits on which the hub switches state; the number of all primitive period-two orbits is
\[
\boxed{\ H_n+2\,\mathbf1_{2\mid n}\ }.
\]
There is one period-two orbit with the hub identically zero and one with it identically one precisely when \(n\) is even. Hub-switching two-cycles exist for every \(n\ge3\) except \(n=4\). Thus the four-rim wheel is the **unique** member of this family for which no periodic orbit changes the hub's opinion.

The first exact values of \(H_n\), for \(n=3,\ldots,14\), are
\[
3,\ 0,\ 5,\ 9,\ 21,\ 32,\ 66,\ 75,\ 220,\ 225,\ 715,\ 833.
\]
All periodic points are thereby classified, including their least periods, hub behaviour and exact number for every rim size.

## Assumptions and scope

The rim vertices are labelled; orbits are counted as distinct cycles in the full Boolean state space, **without** quotienting by rotational or reflection symmetry. The hub is distinguished even for \(W_3\cong K_4\). Rim vertices have three distinct neighbours: two rim neighbours and the hub. The hub has \(n\) neighbours; the only ties arise there when \(n\) is even. No restriction is made on initial states or on \(n\) beyond \(n\ge3\). The result is about *periodic states*, not the transient basin sizes or transient stabilization time.

Write \(x=(x_i)\) for the rim bits, \(h\) for the hub bit, \(s(x)=\sum_i x_i\), and \((x,h)\mapsto(y,h')=F(x,h)\). The exact local equations are
\[
y_i=\begin{cases}x_{i-1}x_{i+1},&h=0,\\x_{i-1}\lor x_{i+1},&h=1,\end{cases}\qquad
h'=\begin{cases}1,&2s(x)>n,\\0,&2s(x)<n,\\h,&2s(x)=n.\end{cases}
\]
Products and disjunctions act on Boolean values.

## Proof

**(1) Hub fixed along an orbit.** If the hub remains zero, the rim evolves by \(A(x)_i=x_{i-1}x_{i+1}\). Direct substitution yields \(A^2(x)_i=x_{i-2}x_ix_{i+2}\). Thus \(A^2(x)=x\) precisely when every occupied vertex has both distance-two neighbours occupied. The step-two permutation \(i\mapsto i+2\) is transitive for odd \(n\), and has exactly two vertex-orbits for even \(n\). Consequently, each of these classes must be either completely occupied or empty. For odd \(n\), the all-occupied rim contradicts a fixed-zero hub; only the all-zero fixed point remains. For even \(n\), the two checkerboard patterns are exchanged by \(A\) and have exactly \(n/2\) occupied rim sites, so the hub retains zero at both phases. They give one primitive period-two orbit. The other two class-unions are either the zero fixed point or incompatible with the hub remaining zero. For a fixed-one hub, use the complemented dual \(B(x)_i=x_{i-1}\lor x_{i+1}\); it gives the unanimous-one fixed point and one additional checkerboard orbit for even \(n\).

**(2) Hub switching.** A two-cycle with switching hub has a uniquely determined zero-hub phase \((x,0)\). The first step gives \(y_i=x_{i-1}x_{i+1}\), and the second gives
\[
B(y)_i=(x_{i-2}x_i)\lor(x_ix_{i+2})=x_i(x_{i-2}\lor x_{i+2}).
\]
Therefore the rim returns to \(x\) if and only if every occupied site \(i\) has at least one occupied distance-two neighbour. This forbids **isolated ones** on each cyclic orbit of the step-two permutation. The hub switches zero-to-one at the first step if and only if \(2s(x)>n\). Set \(e(x)=\sum_i x_{i-1}x_{i+1}\); this is the number of cyclic adjacent \(11\) pairs in step-two ordering, counted with multiplicity on a two-vertex cycle. The hub switches one-to-zero at the second step if and only if \(2e(x)<n\). Thus the no-isolated-ones condition together with these two strict inequalities is **necessary and sufficient**. Exactly one zero-hub phase occurs per switching cycle, so no division by two is needed in \(H_n\).

**(3) Circular-word enumeration.** On a step-two cycle of length \(L\ge2\), the admissible binary words comprise the empty word of ones, the full word of ones, and cyclic words having \(b\ge1\) nonempty runs of ones, each of length at least two, separated by \(b\) runs of zeros of length at least one. If such a word has \(s\) ones, its number of adjacent occupied pairs is \(e=s-b\). The positive run lengths for the ones can be distributed in \(\binom{s-b-1}{b-1}\) ways and those of zeros in \(\binom{L-s-1}{b-1}\) ways. Counting a marked cyclic run boundary and removing the \(b\)-fold marking gives \(L/b\) times their product. The two constant words contribute \(1\) and \(u^Lv^L\). This proves exactly the formula for \(Q_L\), including \(L=2\) (the two directed adjacent pairs are counted separately). For odd \(n\), step-two ordering consists of a single length-\(n\) cycle. For even \(n\), it consists of two independent length-\(n/2\) cycles. Their weighted enumerators therefore multiply, yielding \(R_n\). Extracting precisely those coefficients with \(2s>n\) and \(2e<n\) proves the formula for \(H_n\).

**(4) Fixed points, exhaustiveness and exceptional size.** A fixed hub zero forces a rim one to have two rim-one neighbours, hence either the entire rim is one or it is entirely zero. Hub consistency excludes the former. Complementation handles fixed hub one. Thus only the two unanimous states are fixed. The Goles–Olivos finite symmetric-threshold theorem (references below) excludes eventual periods greater than two; hence the classifications in (1)–(3) cover *all* periodic points. The proof of (1)–(3) does not rely on that external theorem for the classification of points with period dividing two.

If \(n=2m+1\), choose a single consecutive run of \(m+1\) ones on the step-two cycle and zeros elsewhere. Then \(s=m+1\), \(e=m\), and no one is isolated; a switching cycle exists for every odd \(n\ge3\). If \(n=2L\ge6\), take a single run of two ones on one step-two cycle and a single run of \(L-1\) ones on the other, with the remaining vertices zero. Then \(s=L+1\), \(e=L-1\), yielding a switching cycle. When \(n=4\), both step-two cycles have length two; admissibility forces each to be all zeros or all ones. In either case \(s=e\), making \(2s>4\) and \(2e<4\) impossible simultaneously. The exception is therefore sharp.

## Verification

The standalone standard-library script `verify.py` computes the coefficients of \(Q_L\) from the circular-run formula and independently enumerates all \(2^{n+1}\) Boolean wheel states for each \(3\le n\le14\), verifying both fixed points, fixed-hub and switching-hub period-two state counts. Run `python verify.py`; the expected final output is `VERIFY_OK: independent exhaustive checks through n=14`. The exact output of this run is included as `check_output.txt`. All statements for arbitrary \(n\) follow from the proof above, not the finite tests.

## Relationship to prior work

Goles and Olivos proved that synchronous symmetric threshold maps on finite undirected graphs eventually have period at most two. Benjamini, Chan, O'Donnell, Tamuz and Tan (arXiv:1405.2486v1, 11 May 2014) present this theorem and study almost-sure stabilization and random graphs. Their full HTML text addresses the period-two property, random regular graphs and random dense graphs, but not the labelled wheel's **exact number and combinatorial types of cycles**. Epperlein, Siegmund and Stehlík (arXiv:1411.4145v1, 15 November 2014) explicitly study **wheel graphs** in their Section 8, but for a different *imitation-of-the-fittest* update rule and payoff-dependent attractivity of unanimous states (Theorems 30 and 32); their formula does not apply to local neighbour-majority updating. A later study by Benjamini, Zakharov and Zhukovskii (2026) mentions wheels in connection with sharp stabilization-time bounds, not this periodic-state enumeration. The exact hub-switching criterion and run-weighted generating polynomial are additional assertions, rather than consequences of the mere period-two bound. These comparisons are based on the material identified in the references; they do not establish global uniqueness of the result.

## Limitations

Only recurrent dynamics is enumerated. The number of transient states in each basin, expected stabilization times, and asymptotic growth rates of \(H_n\) are not addressed. The formula counts labelled states and cycles rather than dihedral equivalence classes. Novelty is assessed relative to retrieved, inspected literature and indexed results; unindexed or inaccessible equivalent descriptions remain a residual risk.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, first posted 11 May 2014, https://arxiv.org/html/1405.2486v1.
3. J. Epperlein, S. Siegmund and P. Stehlík, *Evolutionary Games on Graphs and Discrete Dynamical Systems*, arXiv:1411.4145v1, first posted 15 November 2014, https://arxiv.org/html/1411.4145v1; in particular Section 8.
4. I. Benjamini, G. Zakharov and M. Zhukovskii, *Majority Dynamics on Finite Trees*, Random Structures & Algorithms (2026), https://doi.org/10.1002/rsa.70092; wheel graphs discussed in Section 6.1.
