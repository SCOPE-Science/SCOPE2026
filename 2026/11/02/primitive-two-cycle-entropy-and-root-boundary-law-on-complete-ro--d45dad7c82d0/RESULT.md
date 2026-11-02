# Primitive two-cycle entropy and root boundary law on complete rooted trees

## Finding

Let \(T_{d,h}\) be the finite undirected complete rooted \(d\)-ary tree of height \(h\), with \(d\ge2\), \(h\ge1\): the root has \(d\) children, every vertex at levels \(0,\ldots,h-1\) has \(d\) children, and the \(d^h\) level-\(h\) vertices are leaves. All vertices are distinguished; only temporal rotation identifies periodic chip configurations. In the usual synchronous, sink-free parallel chip-firing map, define \(N_{d,h}\) as the number of distinct primitive period-two orbits.

Set \(A_0=0\), \(B_0=1\), and, for \(j\ge0\), recursively set
\[
A_{j+1}=d B_j(A_j+B_j)^{d-1},\qquad
B_{j+1}=(A_j+B_j)^{d-1}(A_j+(d+1)B_j).
\]
Then **the exact orbit number for all integers \(d\ge2,h\ge1\) is**
\[
N_{d,h}=A_h.
\]
In particular, at height \(h=2\) the formula simplifies to \(N_{d,2}=d(d+1)(2d+1)^{d-1}\). For \(d=2\) and heights \(h=1,2,3,4,5\), the orbit counts are respectively
\[
2,\quad30,\quad9350,\quad859413750,\quad7323520810533593750.
\]

Uniformly choose one of these orbits and let \(K_{d,h}\) be the number of edges incident with the root whose endpoints fire in opposite phases. Put \(r_0=0\) and \(r_{j+1}=d/(d+1+r_j)\). The **exact root law** is
\[
K_{d,h}\ \overset{\mathrm d}=\ 1+\operatorname{Binomial}\!\left(d-1,\frac1{1+r_{h-1}}\right).
\]
Let
\[
r_d^*=\frac{\sqrt{(d+1)^2+4d}-(d+1)}2,\quad
C_d(r)=(1+r)^{d-1}(d+1+r),\quad
L_d=\sum_{j=0}^{\infty}\frac{\log C_d(r_j)}{d^{j+1}}.
\]
Then \(r_j\to r_d^*\), the root law converges to
\[
1+\operatorname{Binomial}\!\left(d-1,\frac1{1+r_d^*}\right),
\]
and the exact per-vertex orbit-growth constant satisfies
\[
\rho_d=\lim_{h\to\infty}N_{d,h}^{1/|V(T_{d,h})|}
=\exp\!\left(\frac{d-1}{d}L_d\right).
\]
More precisely, with
\[
\kappa_d=r_d^*\exp\!\left(\frac{L_d}{d}-\frac{\log C_d(r_d^*)}{d-1}\right),
\qquad q_d=\frac{d}{(d+1)^2},
\]
one has \(N_{d,h}=\kappa_d\rho_d^{|V(T_{d,h})|}(1+O_d(q_d^h))\). For binary trees, \(\rho_2\approx2.04324350511116\), and the limiting probability of two opposite-phase edges at the root is \((1+\sqrt{17})/8\). As branching increases,
\[
\rho_d=1+\frac{\log(2d)}d+O\!\left(\frac{(\log d)^2}{d^2}\right).
\]

## Assumptions and scope

A configuration is an integer nonnegative chip height \(x(v)\) at each vertex \(v\). At one synchronous step every vertex with at least \(\deg(v)\) chips sends one chip to each neighbor; the receiving chips are added after all firing decisions. No sink, source, loop, random update, or quotient by spatial symmetry is used. A primitive two-cycle is a pair of distinct configurations exchanged by the update, counted once as a temporal orbit. Heights are a priori unbounded; the proof shows that every primitive two-cycle is confined to a finite box.

## Proof

**1. A two-phase cut formula.** For any finite connected loopless graph with at least one edge, let \(f_t(v)\in\{0,1\}\) indicate firing at time \(t\). A two-step periodic state obeys \(\sum_{w\sim v}(f_0(w)+f_1(w))=\deg(v)(f_0(v)+f_1(v))\). By connectedness, this discrete harmonic integer-valued function is constant. If the common value is zero or two, all vertices wait or all fire at both steps, so the state is fixed. Thus in any primitive two-cycle every vertex fires exactly once in its two steps and switches phase at each step.

Color each vertex by whether it fires at the chosen first step. For a vertex \(v\), let \(c(v)\) count neighbors of the opposite color and write \(k(v)=\deg(v)\). If \(v\) fires first, its starting height must lie in
\[
\{k(v),k(v)+1,\ldots,k(v)+c(v)-1\};
\]
if \(v\) waits first, it must lie in
\[
\{k(v)-c(v),k(v)-c(v)+1,\ldots,k(v)-1\}.
\]
Indeed, the first update shifts a firing vertex by \(-c(v)\) and a waiting vertex by \(+c(v)\). Therefore these intervals are both necessary and sufficient for the required alternating firing pattern and return after two updates. Each contains exactly \(c(v)\) nonnegative heights; the pattern is possible only if every \(c(v)>0\).

On a tree, the set \(H\) of opposite-color edges determines the two-coloring up to simultaneous color reversal. Every edge subset \(H\subseteq E(T)\) is a color-cut on a tree, and \(c(v)=\deg_H(v)\). A subset contributes only when it covers all vertices. For any fixed \(H\), the two phase colorings admit \(\prod_v\deg_H(v)\) heights each, giving exactly \(\prod_v\deg_H(v)\) distinct temporal two-cycles. Consequently,
\[
N_2(T)=\sum_{\substack{H\subseteq E(T)\\\deg_H(v)\ge1\ \forall v}}\prod_{v\in V(T)}\deg_H(v).
\]
No external periodicity theorem is required for this identity, and the calculation includes every nonnegative primitive two-cycle state.

**2. Rooted recursion.** Consider a subtree of height \(j\), and fix whether its external edge to its parent belongs to \(H\). Let \(A_j\) and \(B_j\) be the weighted sums (including the root's \(\deg_H\) factor) when the external edge is absent or present. For a leaf, \(A_0=0,B_0=1\). For a root with \(d\) children, summing over the \(d\) child-edge indicators \(e_i\in\{0,1\}\), its weight is \(p+\sum_i e_i\), where \(p=0\) or \(1\) is the external indicator. Independence of subtrees gives the displayed pair of recurrences. The full tree has no parent edge, hence \(N_{d,h}=A_h\).

**3. The root law.** Conditional on exactly \(k\) of the root's \(d\) child edges belonging to \(H\), the weighted number of orbits is \(k\binom dk B_{h-1}^k A_{h-1}^{d-k}\). The sum over \(k\) is \(dB_{h-1}(A_{h-1}+B_{h-1})^{d-1}\). Dividing yields the size-biased binomial law stated above, and \(A_j/B_j=r_j\) satisfies \(r_{j+1}=d/(d+1+r_j)\). Both \(A_j\) and \(B_j\) are positive for \(j\ge1\).

**4. Entropy and precise asymptotics.** The map \(r\mapsto d/(d+1+r)\) has Lipschitz constant at most \(q_d=d/(d+1)^2<1\) on the nonnegative reals, hence \(r_j=r_d^*+O_d(q_d^j)\). From \(B_{j+1}=B_j^d C_d(r_j)\) and \(B_0=1\) follows the exact identity
\[
\log B_h=d^h\sum_{j=0}^{h-1}d^{-j-1}\log C_d(r_j).
\]
Since \(|V(T_{d,h})|=(d^{h+1}-1)/(d-1)\) and \(\log A_h=\log B_h+\log r_h\), the convergent series gives \(\log\rho_d=(d-1)L_d/d\). Subtracting \(|V(T_{d,h})|\log\rho_d\), writing the missing series tail with index \(h+k\), and using \(r_{h+k}=r_d^*+O_d(q_d^{h+k})\) gives the constant \(\log\kappa_d\) and error \(O_d(q_d^h)\).

For the large-branching formula, \(0\le r_j\le1\), while \(r_j=1+O(1/d)\) uniformly for \(j\ge1\). Thus \(\log C_d(r_0)=\log(d+1)\) and \(\log C_d(r_j)=d\log2+\log d+O(1)\) uniformly for \(j\ge1\). Summing the geometric weights yields \(\log\rho_d=\log(2d)/d+O((\log d)/d^2)\), and exponentiation gives the stated expansion.

## Verification

Run `python3 verify.py` with standard Python. It computes the recursion exactly, independently enumerates edge-cover weights and root-degree histograms for complete trees including the binary tree of height three and the four-ary tree of height two, and directly simulates all nonnegative confined configurations for smaller trees. It also prints a numerically evaluated binary-tree entropy bracket obtained from the elementary tail bound
\[
0\le\log\rho_d-\frac{d-1}{d}\sum_{j=0}^{J-1}d^{-j-1}\log C_d(r_j)
\le\frac{\log(2^{d-1}(d+2))}{d^{J+1}}.
\]
The finite checks corroborate, but do not replace, the unrestricted proof.

## Relationship to prior work

Bitar and Goles established that eventual periods on trees are at most two; this is a period restriction, not the displayed orbit census. Jiang proved the equal-firing-count characterization for any periodic state on a connected graph (Proposition 2.5 in the 2010 manuscript); step 1 uses and independently derives its two-step specialization. Scully, Jiang and Zhang studied firing-word constraints and tree-like attachments but not the weighted complete-tree orbit recursion or the associated root law and entropy. Recent work on binary-tree chip-firing with an infinite tree, initial chips concentrated at its root, and terminating stable configurations concerns a distinct evolution and invariant. The new assertion is the explicit full-tree orbit statistic and its limits, not the known period restriction or the general harmonic-firing observation.

## Limitations

The theorem counts only primitive temporal period-two orbits, with individual vertices distinguished. It does not count fixed configurations, transient basins, or orbits modulo tree automorphisms. The asymptotic entropy is for fixed branching factor as tree height tends to infinity; the large-branching expansion concerns those already-defined limiting constants. The 1992 Bitar–Goles full text was not available for an exhaustive comparison; an unindexed historical equivalent or a result whose stated scope already includes the tree-specific count remains an originality risk. The numerical constant is an approximation, not an independently certified decimal.

## References

1. J. Bitar and E. Goles, *Parallel chip firing games on graphs*, Theoretical Computer Science 92 (1992), 291–300. DOI: 10.1016/0304-3975(92)90316-8.
2. T.-Y. Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943 (first arXiv posting 2010-03-04), especially Section 2, Proposition 2.5. https://arxiv.org/abs/1003.0943.
3. Z. Scully, T.-Y. Jiang and Y. X. Zhang, *Firing Patterns in the Parallel Chip-Firing Game*, DMTCS Proceedings (2014), 537–548, especially Sections 3–5. https://ziv.codes/pdf/dmtcs2014-scully.pdf.
4. R. Inagaki, T. Khovanova and A. Luo, *On Chip-Firing on Undirected Binary Trees*, arXiv:2410.00039 (2024), especially Sections 1 and 3. https://arxiv.org/abs/2410.00039.
