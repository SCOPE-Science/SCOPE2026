# Fully flipping majority two-cycles on open ladders

## Finding

Let \(G_n=P_n\square K_2\) be the labelled, **open** two-row ladder with \(n\ge2\) rungs. Synchronously update each binary vertex to the strict majority of its *open neighbors*, retaining its old bit when the neighbor votes tie. Denote this map by \(M_n\), and write \(\bar x\) for bitwise complementation. With \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\), the number of configurations in which **every** vertex flips is

\[
\boxed{Q_n:=\#\{x\in\{0,1\}^{2n}:M_n(x)=\bar x\}=2F_{n-1}.}
\]

These configurations form exactly \(F_{n-1}\) distinct primitive temporal two-cycle orbits, counted as pairs \(\{x,\bar x\}\). More precisely, every rung is mixed, with top-rail bit \(w_i\) and bottom-rail bit \(1-w_i\). Let \(d_i=w_i\oplus w_{i+1}\) for \(1\le i<n\). The **complete** characterization is

\[
d_1=d_{n-1}=1,\qquad d_i+d_{i+1}\ge1\quad(1\le i\le n-2),
\]

where for \(n=2\) the two endpoint conditions refer to the same single indicator. Every word satisfying these conditions, together with either choice of \(w_1\), gives one and only one fully flipping configuration. In particular \(Q_2,Q_3,Q_4,Q_5,Q_6,Q_7=(2,2,4,6,10,16)\).

For comparison—not as a newly claimed total census—the previously published all-periodic formula on exactly this graph and update is
\[
P_n:=\#\operatorname{Fix}(M_n^2)=L_{2n}+1+3\mathbf1_{3\mid n},\qquad
H_n:=\#\operatorname{Fix}(M_n)=2(F_{n+1}+1),
\]
where \(L_0=2,L_1=1\) are Lucas numbers. It follows from that credited formula and the new sector count that the proportion of **primitive two-periodic states** which flip everywhere is
\[
\frac{Q_n}{P_n-H_n}=\frac{2F_{n-1}}{L_{2n}-2F_{n+1}-1+3\mathbf1_{3\mid n}}
\sim\frac{2}{\sqrt5\,\varphi^{n+1}},\qquad \varphi=\frac{1+\sqrt5}{2}.
\]
The denominator is positive for every \(n\ge2\). These are initially two-periodic states, not their transient basins.

## Proof

Write a rung's two bits as \((a_i,b_i)\) and suppose \(M_n(x)=\bar x\). If an **end** rung is homogeneous \(a_i=b_i\), its vertical neighbor agrees with it, so the single horizontal neighbor cannot give the strict opposite majority among two votes; a tie retains the old bit. Thus an end rung in a fully flipping configuration cannot be homogeneous. If an **interior** rung is homogeneous with value \(c\), its vertical vote agrees with the old bit. For each vertex to flip under degree-three strict majority, both horizontal neighbors must vote \(1-c\). On *both* rails this forces each adjacent rung to be homogeneous with value \(1-c\). Repetition propagates homogeneity along the finite connected rung path until an end, which is impossible. Hence every rung is mixed: \(b_i=1-a_i\).

Set \(w_i=a_i\). At an end, the vertical neighbor already votes opposite, but degree two demands that the sole horizontal neighbor also vote opposite, or else the old bit survives a tie. This is exactly \(d_1=d_{n-1}=1\). At an interior vertex the vertical neighbor again votes opposite, so to flip under degree-three strict majority at least one of the two horizontal neighbors must vote opposite. The bottom rail imposes the same condition because it is the complement of the top rail. This is \(d_{i-1}+d_i\ge1\) for each interior rung \(2\le i\le n-1\), equivalently no adjacent zero entries in the indicator word. All stated conditions are also sufficient by these same local vote checks.

For \(n=2\), the indicator word is the one-bit word \(1\), giving \(2=2F_1\) choices including \(w_1\). For \(n\ge3\), after the prescribed first and last ones, there are \(m=n-3\) free binary indicators with no adjacent zeros. Let \(c_m\) denote their count, including the empty word \(c_0=1\). A word ends in 1 (\(c_{m-1}\) options) or in 0 preceded by 1 (\(c_{m-2}\) options), giving \(c_m=c_{m-1}+c_{m-2}\), with \(c_0=1,c_1=2\); hence \(c_m=F_{m+2}=F_{n-1}\). Each indicator word and \(w_1\) uniquely reconstructs the entire top word and its complementary bottom. This proves \(Q_n=2F_{n-1}\) for all \(n\ge2\).

The majority rule, including tie retention, commutes with global bit-complementation. Hence \(M_n(x)=\bar x\) implies \(M_n(\bar x)=\overline{M_n(x)}=x\). Since no nonempty binary configuration equals its complement, each such pair is a primitive two-cycle and contributes exactly two states. The orbit count follows.

Finally, the credited full periodic-point formulas imply \(P_n-H_n\sim\varphi^{2n}\) while Binet's formula gives \(2F_{n-1}\sim 2\varphi^{n-1}/\sqrt5\); division proves the displayed asymptotic. No finite computation is used to infer this all-length conclusion.

## Why the focused invariant matters

The exact total two-cycle census does not determine *which* coordinates oscillate. The all-vertex-flipping sector is a natural dynamical subpopulation, separating global flips from mixed fixed/oscillating behavior. The open ladder's degree-two ends enforce two boundary changes and yield a Fibonacci rather than the Lucas-plus-residue count of the cyclic cubic prism. The complete indicator-word characterization gives a reusable boundary-sensitive sector classification. The proof is elementary once the rung constraint is identified; no broader theorem or unproved generalization is claimed.

## Verification and limits

Direct enumeration of every one of the \(4^n\) binary configurations for \(2\le n\le9\), independently constructing the graph and local strict-majority rule, returned \(Q_n=(2,2,4,6,10,16,26,42)\). The source package's `verification/bruteforce_verify.py` checks the original fixed, periodic and pure-flip counts through \(n=10\); `verification/transfer_verify.py` checks the original transfer certificate and restricted pure-flip counts through \(n=80\). These finite tests corroborate, but do not establish, the unrestricted pure-flip classification above. The original all-periodic transfer proof is preserved in the frozen source history and remains credited to the earlier published result; it is **not** claimed novel here. We do not count basins or first-entry times.

## Prior-work boundary

- *Lucas–Fibonacci orbit census for synchronous majority dynamics on open ladders* (November 1, 2026), https://github.com/Resultary/2026/tree/main/2026/11/1/SCOPE-lucas-fibonacci-orbit-census-for-synchronous-majority-dynamics-o--589e6314b7c7 : **already proves** the fixed, all-two-periodic and primitive-orbit formulas, including the mod-three resonance. These results are used only as credited comparison, not an independent contribution.
- *Fully flipping majority two-cycles on cyclic prisms and Möbius ladders* (November 8, 2026), https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-a-modulo-six-twist-resonance-in-synchronous-majority-dynamics-on--0a383da6731a : establishes exact all-flip sectors for degree-three **cyclic** graphs, with a wraparound/twisted seam instead of open ends. Its cyclic word constraints do not directly supply the present degree-two endpoint conditions.
- Z. Agur, A. S. Fraenkel, S. T. Klein, *The number of fixed points of the majority rule*, Discrete Mathematics 70 (1988), 295–302, DOI 10.1016/0012-365X(88)90005-2, https://www.imbm.org/wp-content/uploads/2020/01/AFK88.pdf : enumerates ordinary cyclic one-row no-triple words and identifies Fibonacci restrictions, but does not study the two-row open-ladder pure-flip sector. The generic Fibonacci word count itself is classical and is not claimed new.
- V. Turau, *Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees*, arXiv:2202.01580v1 (2022), https://arxiv.org/html/2202.01580v1 : general pure-flip constructions for **trees**; open ladders contain squares.
- D. Kaaser, F. Mallmann-Trenn, E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519 (2015), https://arxiv.org/abs/1508.03519 : general majority convergence time and period-two background, not a pure-flip ladder census.

An unindexed open-ladder pure-flip enumeration, or an implicit specialization of a more general graph-word transfer theorem, remains a genuine priority risk. The focused result is a best-of-knowledge mathematical refinement, not a claim of independent external certification.
