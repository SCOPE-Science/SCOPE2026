# Two-leak forcing polynomials and fort spectra of the five Platonic graphs

## Finding
Let \(\mathcal P=\{K_4,Q_3,O,D,I\}\) be the graph skeletons of the regular tetrahedron, cube, octahedron, dodecahedron, and icosahedron, respectively. A set \(S\) is **two-leak forcing** when the usual color-change process succeeds even if any two vertices are prohibited from performing forces. Write
\[
L_2(G;z)=\sum_{S\subseteq V(G):\; S\text{ is two-leak forcing}}z^{|S|}.
\]
The complete exact evaluations are
\[
\begin{aligned}
L_2(K_4;z)&=4z^3+z^4,\\
L_2(Q_3;z)&=16z^6+8z^7+z^8,\\
L_2(O;z)&=6z^5+z^6,\\
L_2(D;z)&=2360z^9+21952z^{10}+56240z^{11}+73540z^{12}\\
&\quad+60600z^{13}+35100z^{14}+15024z^{15}+4815z^{16}\\
&\quad+1140z^{17}+190z^{18}+20z^{19}+z^{20},\\
L_2(I;z)&=240z^8+220z^9+66z^{10}+12z^{11}+z^{12}.
\end{aligned}
\]
In particular the two-leak forcing numbers, in the displayed graph order, are \((3,6,5,9,8)\), with respectively \((4,16,6,2360,240)\) minimum-size choices.

Define the **two-leak fort polynomial** \(H_2(G;z)\) by counting inclusion-minimal nonempty sets \(W\subseteq V(G)\) with at most two vertices outside \(W\) having exactly one neighbor in \(W\). The exact values are
\[
\begin{aligned}
H_2(K_4;z)&=6z^2,\\
H_2(Q_3;z)&=12z^2,\\
H_2(O;z)&=15z^2,\\
H_2(D;z)&=30z^4+120z^6+695z^8+120z^9+240z^{10},\\
H_2(I;z)&=255z^4.
\end{aligned}
\]
The dodecahedral graph therefore has \(1205\) inclusion-minimal two-leak forts of five different sizes, whereas every inclusion-minimal two-leak fort of the icosahedral graph has size four.

For comparison, the triplets of minimum forcing numbers for zero, one, and two leaks are respectively
\[
(3,3,3),\quad(4,4,6),\quad(4,4,5),\quad(6,6,9),\quad(6,6,8).
\]
The dodecahedral and icosahedral one-leak minima are previously known. Moreover, the numbers of minimum one-leak forcing sets on these two graphs are \(600\) and \(80\), as against \(2040\) and \(200\) minimum zero-leak forcing sets; equal minimum *sizes* need not imply equal minimum *set families*.

## Assumptions and scope
All graphs are undirected and simple. A blue vertex may color its unique white neighbor blue; a **leak** is a vertex that cannot perform such a force but may itself become blue. Leaks are chosen adversarially before the process, independently of the initial blue set. Success means all graph vertices become blue for every leak set of size at most two. Distinct labeled vertex subsets are counted separately, while vertex relabelings preserve all displayed coefficients.

The five graph inputs are fully specified by the five edge-list files in `graphs/`, with zero-based vertex labels. They have respectively \((|V|,|E|)=(4,6),(8,12),(6,12),(20,30),(12,30)\), the usual Platonic degrees \(3,3,4,3,5\), and are isomorphic to the standard graph skeletons. In particular \(D\cong GP(10,2)\), the generalized Petersen graph whose outer and inner cycles have step lengths one and two, joined by spokes.

These are **exact finite classifications**, not assertions about an infinite graph family. The general fort characterization and the general enumeration algorithm are known; the specific evaluated five-graph forcing and minimal-fort spectra are the subject of this result.

## Proof
For any nonempty \(W\subseteq V(G)\), let
\[
\partial_1(W)=\{v\in V(G)\setminus W:|N_G(v)\cap W|=1\}.
\]
The known fort characterization says that an initial set \(S\) is two-leak forcing exactly when it intersects every nonempty \(W\) with \(|\partial_1(W)|\le2\). Briefly, if \(S\cap W=\varnothing\), declaring all vertices of \(\partial_1(W)\) leaks prevents the first force into \(W\). Conversely, if a forcing process stalls with uncolored set \(W\ne\varnothing\), every vertex of \(\partial_1(W)\) must be one of the at-most-two leaks. Thus such a \(W\) witnesses failure. This is a pre-existing general lemma, not a new assertion.

Here is a complete exhaustive finite certificate with an explicit recursion. Fix one of the input graphs with \(N\le20\) labeled vertices, let \(F=2^N-1\) represent the full vertex set, and encode each subset by its binary integer mask. Let \(b(W)\) mean that \(W\ne\varnothing\) and \(|\partial_1(W)|\le2\). Recursively define
\[
A(0)=0,\qquad
A(W)=b(W)\lor\bigvee_{v\in W} A(W\setminus\{v\}).
\]
By induction on \(|W|\), \(A(W)=1\) precisely when \(W\) contains a two-leak fort. The induction is executed in increasing numeric mask order: deletion of any set bit strictly decreases the integer mask, so every prerequisite is already computed. It follows *exactly* that
\[
L_2(G;z)=\sum_{S\subseteq V(G)}[A(V(G)\setminus S)=0]z^{|S|}.
\]
Similarly, a nonempty \(W\) is inclusion-minimal among two-leak forts exactly when \(b(W)=1\) and \(A(W\setminus\{v\})=0\) for every \(v\in W\). Hence
\[
H_2(G;z)=\sum_{W\ne\varnothing}[b(W)=1]\prod_{v\in W}[A(W\setminus\{v\})=0]z^{|W|}.
\]
These formulas are complete, because they evaluate **every one of the \(2^N\) masks**, rather than a sample. The source file `enumerate.cpp` implements these definitions using only unsigned-integer masks, popcounts, and the stated induction. The complete inputs and the exact expected cardinality vectors for leak allowances zero, one, and two are included. The C++ integer counts are safe in unsigned 32-bit accumulators for this census (the largest coefficient is below \(2^{20}\)); the computed polynomial coefficients are compared to explicit expected integers by `verify.py`.

## Verification
Run `python3 verify.py` in a directory containing the delivered standalone files, with Python 3 and any C++17 compiler providing `g++` available. The script compiles `enumerate.cpp` and `direct_check.cpp`, reads every graph input, checks all expected counts for leak allowances zero, one, and two, and independently decides every one of the \(2^N\) possible initial sets for graphs with \(N\le12\): it checks every adversarial leak placement for predicted winners and exhibits at least one failing leak placement for predicted losers. For the \(20\)-vertex dodecahedron, the direct simulator checks every one of the \(2360\) optimal two-leak forcing configurations and a deterministic sample of other configurations. The full dodecahedral polynomial itself is certified by the exhaustive \(2^{20}\)-mask fort recursion; the independent forcing simulation does not claim exhaustive direct testing of all \(2^{20}\) initial sets.

The direct check returns `DIRECT_CHECK_OK` for all five graph inputs, including \(594303\) adversarial-leak tests on the dodecahedral graph, and `verify.py` returns `ALL_EXACT_CHECKS_OK`. The finite nature of the statement makes this an exhaustive computational proof when the supplied code, inputs, and induction are checked; no claim of machine-independent formal verification is made.

## Relationship to prior work
Dillman and Kenter introduced leaky forcing in the 2019 arXiv version of their foundational paper. Alameda, Kritschgau, Warnberg, and Young developed its resilience framework in 2020. Bjorkman et al. (2025), Theorem 4.8, already prove that \(Z_1(GP(n,2))=6\) for \(n\ge9\); thus the dodecahedral **one-leak minimum of six is not new**. Their Table 1 gives two-leak values of \(GP(n,2)\) only for \(5\le n\le9\); their Theorem 4.16 assumes a different parameter regime \(k\ge7\) and does not cover \(GP(10,2)\). The 2026 preprint by Xinjun Wang defines the general leaky forcing polynomial and derives an exact fort-based algorithm on graphs of bounded neighborhood diversity. Its general counting framework is not claimed here; the present explicit Platonic coefficients and the five-size dodecahedral minimal-fort spectrum are concrete evaluated invariants not displayed in that paper.

These comparisons do not establish absolute publication priority. Exact finite counts may occur in other terminology or unpublished computational tables; that risk remains.

## Limitations
All coefficients refer to the standard vertex-leak model, not edge-leaky or positive-semidefinite forcing, nor faults that change graph adjacency. The classification covers only the five named graphs. Mathematical correctness uses the exhaustiveness of the supplied finite enumeration and the input graph identifications; independent formal auditing has not been performed. Although relevant prior papers were inspected, a differently formulated or unindexed prior tabulation could cover a part of the enumerated data.

## References
1. S. Dillman and F. Kenter, *Leaky Forcing: A New Variation of Zero Forcing*, arXiv:1910.00168, first submitted 2019-10-01, https://arxiv.org/abs/1910.00168.
2. J. S. Alameda, J. Kritschgau, N. Warnberg, and M. Young, *On leaky forcing and resilience*, arXiv:2008.06552, 2020, https://arxiv.org/abs/2008.06552.
3. B. Bjorkman, L. Cao, F. Kenter, R. Moruzzi Jr., C. Reinhart, and V. Vasilevska, *Leaky Forcing: Extending Zero Forcing Results to a Fault-Tolerant Setting*, arXiv:2508.02564, 2025, https://arxiv.org/abs/2508.02564.
4. X. Wang, *Modular Compression of Leaky Forts and Leaky Forcing Polynomials*, preprint, 2026-05-26, DOI:10.5281/zenodo.20388397, https://doi.org/10.5281/zenodo.20388397.
