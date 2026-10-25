# A sixty-four-sphere wedge and a 600-symmetry character for the Paley-25 flag complex

## Finding
For the ordinary clique complex \(K=\operatorname{Cl}(P_{25})\) of the Paley graph of order \(25\),
\[
K\simeq\bigvee^{64}S^2.
\]
This is an integral homotopy equivalence, not merely a calculation of Betti numbers. In particular, \(\pi_1(K)=1\) and \(H_2(K;\mathbb Z)\cong\mathbb Z^{64}\), with no other positive-dimensional integral homology.

Let \(G\) consist of all semiaffine maps \(x\mapsto u x^{5^e}+b\), where \(u\) is a nonzero square of \(\mathbb F_{25}\), \(b\in\mathbb F_{25}\), and \(e\in\{0,1\}\). The \(600\) distinct maps act simplicially on \(K\). The complete distribution of traces on \(H_2(K;\mathbb Q)\) is
\[
\begin{array}{c|rrrrr}
\text{trace}&-16&-1&0&4&64\\\hline
\text{number of elements}&15&72&450&62&1
\end{array}.
\]
In particular, \(H_2(K;\mathbb Q)^G=0\). The following known translation-subgroup specialization is recorded only as a consistency check, not as an original statement: for a translation by \(b\), the trace is \(64\) if \(b=0\), \(4\) if \(b\) is a nonzero square, and \(-1\) otherwise. Writing \(N=(\mathbb F_{25},+)\), this determines every complex irreducible multiplicity of \(H_2(K;\mathbb C)|_N\): the trivial additive character occurs four times; a nontrivial character whose kernel is one of the three square-direction lines occurs three times; every other nontrivial character occurs twice.

## Assumptions and scope
Use the concrete finite field \(\mathbb F_{25}=\mathbb F_5[\omega]/(\omega^2-2)\). The elements are pairs \(a+b\omega\), encoded by the integer \(5a+b\) with \(0\le a,b<5\). Distinct elements \(x,y\) are adjacent precisely when \(x-y\) is a nonzero square. Square multiplication gives the twelve-element connection set
\[
S=\{5,10,15,20,6,12,18,24,9,13,17,21\}
\]
in this encoding. This is the union of the nonzero points of three one-dimensional \(\mathbb F_5\)-subspaces of \(\mathbb F_{25}\).

The bijective linear coordinates \(r=b-a\), \(c=b+a\) turn adjacency into equality of \(r\), equality of \(c\), or equality of \(r+c\). Hence \(P_{25}\) is also the Latin-square graph of the addition table of \(\mathbb F_5\). All assertions concern this particular graph and the explicitly specified group \(G\); there is no extrapolation to other orders.

## Proof
**1. Complete simplicial enumeration and reduction of dimension.** Directly from the square-difference predicate, the clique complex has face numbers
\[
(f_0,f_1,f_2,f_3,f_4)=(25,150,250,75,15),
\]
with no larger cliques. The fifteen five-vertex cliques are the five affine lines in each of the three square directions. Each four-vertex clique belongs to exactly one of these maximal five-vertex cliques. The deterministic elementary-collapse procedure in `verify.py` first removes each of the fifteen four-simplices together with a free three-face. Afterward, the sixty remaining three-simplices can successively be removed with free two-faces. At every step the program tests that the proposed lower-dimensional face has no other surviving coface of any higher dimension, so every pair is a valid elementary simplicial collapse. The result is a connected two-dimensional complex with face counts \((25,150,190)\). Thus the original complex has the homotopy type of a finite two-complex.

**2. Integral fundamental-group trivialization.** The graph is connected. Choose the breadth-first spanning tree rooted at the encoded field element \(0\), visiting neighbors in ascending integer order. Contracting this tree yields \(150-24=126\) oriented edge generators. Each of the original \(250\) triangular faces supplies the usual oriented length-at-most-three relator, with tree edges interpreted as identity. The verifier executes \(126\) consecutive Tietze eliminations: at each step it picks a shortest remaining relator containing some generator exactly once, solves that relator for the generator with the correct orientation, substitutes the resulting word in every other relator, and deletes the pivot relator. Free and cyclic cancellations only conjugate or reduce relators and preserve their normal closure. All \(126\) different generators are eliminated, and all remaining relators reduce to the empty word. Therefore \(\pi_1(K)=1\). This argument uses the original two-skeleton, which has the same fundamental group as \(K\), and does not infer simple connectivity from vanishing first homology.

**3. Integral homotopy type.** By the elementary collapses, \(K\) is homotopy equivalent to a simply connected two-complex. Euler characteristic is
\[
\chi(K)=25-150+250-75+15=65.
\]
For a connected simply connected two-complex, reduced homology is concentrated in degree two, where it is free abelian of rank \(\chi-1=64\). Hurewicz identifies the second homotopy group with this free group. A map \(\bigvee^{64}S^2\to K\) representing an integral basis of \(\pi_2(K)\) is an isomorphism on all integral homology groups, hence a homotopy equivalence by the simply connected homological Whitehead theorem.

**4. Complete rational symmetry character.** The square multiplier, translation and fifth-power Frobenius maps preserve square differences. The verifier enumerates all \(25\cdot12\cdot2=600\) semiaffine permutations, checks they are pairwise distinct and preserve adjacency, then applies the signed simplicial Lefschetz formula. For each \(g\in G\),
\[
\operatorname{tr}(g\mid H_2(K;\mathbb Q))
=-1+\sum_{j=0}^{4}(-1)^j\sum_{\substack{\sigma\in K_j\\g\sigma=\sigma}}
\operatorname{sgn}(g|_{\sigma}).
\]
The initial \(-1\) subtracts the constant zero-dimensional homology. Since degree two is the sole positive-degree homology, the formula computes the actual character, not merely an alternating virtual character. Exhaustive evaluation yields the tabulated histogram. The sum of the \(600\) trace values is zero, so averaging characters proves \(\dim H_2(K;\mathbb Q)^G=0\).

**5. Previously known translation-isotypic restriction, recomputed for comparison.** All \(24\) nonzero translations have no fixed vertices. The fixed-simplex calculation gives traces \(4\) for the twelve nonzero square displacements and \(-1\) for the twelve other displacements. Under the dual Fourier transform on \(N\), an additive character \(\psi\) occurs with multiplicity
\[
m_{\psi}=\frac1{25}\sum_{b\in N}\operatorname{tr}(b\mid H_2)\overline{\psi(b)}.
\]
The trivial character gives multiplicity \(4\). For nontrivial \(\psi\), the sum of \(\psi\) on the square set is \(2\) if its kernel is one of the three square-direction lines, and \(-3\) otherwise. Hence the multiplicity is respectively \(3\) or \(2\). The dimension check is \(4+12\cdot3+12\cdot2=64\).

## Verification
Run `python3 verify.py` using Python's standard library only. The code reconstructs the field, graph, all cliques, and every legal elementary collapse; independently verifies the vanishing group presentation by a fully specified sequence of Tietze substitutions; checks the mod-two boundary ranks \((24,126,60,15)\); checks all \(600\) group actions and signed Lefschetz traces; and checks both the total character histogram and its restriction to translations. The file `verification_output.txt` records the actual successful execution. The code itself makes all assertions and is the replayable finite certificate; the output log alone is not a proof.

## Relationship to prior work
Chandler, Sin and Xiang (arXiv:1401.8260, first posted 31 January 2014) define Paley graphs and compute Smith and critical groups of their *graph adjacency and Laplacian matrices*, rather than clique-complex homotopy or homology representations. Cioabă, Guo, Ji and Mim (arXiv:2508.05871, Section 5) independently establish first *field* cohomology vanishing for \(P_{25}\); this does not prove its fundamental group trivial. Most importantly, Cioabă and Mim (arXiv:2606.27328, Section 3, especially Theorem 3.12 and Proposition 3.13) give the complete homology groups of *all Latin-square graphs*, which after the explicit identification above already imply the previously known degree-two rank \(64\) and the absence of integral torsion for this example. **That Betti-number calculation is prior work, not an original contribution claimed here.** An earlier complete translation-character theorem for odd-order cyclic Latin-square graphs (archived result e5a5d583-4b0e-4ec8-8e3a-68ffa1bf9c69) also already covers the translation restriction at order five. **The distinct contribution asserted here is exclusively the integral homotopy decomposition via fundamental-group elimination and the character on the full \(600\)-element semiaffine group, beyond its translation subgroup.**

## Limitations
The argument is an exhaustive finite proof for \(P_{25}\), not a uniform homotopy theorem for general Paley graphs or Latin-square graphs. Both the graph-theoretic ordinary-homology inputs and the translation-subgroup character overlap with prior mathematical results, as detailed above. No claim is made that an equivalent homotopy or symmetry description cannot exist in unindexed literature; the targeted record and primary-text comparisons reduce but cannot eliminate that risk. The self-review checks correctness, originality and value but is not an independent scientific audit.

## References
1. D. Chandler, P. Sin and Q. Xiang, *The Smith and critical groups of Paley graphs*, arXiv:1401.8260 (first submitted 2014-01-31), https://arxiv.org/abs/1401.8260.
2. S. M. Cioabă, K. Guo, C. Ji and M. Mim, *Clique complexes of strongly regular graphs, their eigenvalues, and cohomology groups*, arXiv:2508.05871 (2025), https://arxiv.org/pdf/2508.05871.
3. S. M. Cioabă and M. Mim, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328 (2026), https://arxiv.org/abs/2606.27328.
4. A. E. Brouwer, *Paulus–Rozenfeld graphs*, graph census, https://aeb.win.tue.nl/graphs/Paulus.html (the Paley-25 entry identifies the order-600 automorphism group and fifteen maximum cliques).
