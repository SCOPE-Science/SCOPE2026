# A parity threshold in two-letter composition spectra

## Finding

Fix a labeled alphabet \(\Sigma\) of \(q\geq2\) symbols. For every word \(w=w_1\cdots w_n\), \(n\geq2\), its **adjacent-pair composition spectrum** \(M_2(w)\) is the multiset of unordered pairs \(\{w_i,w_{i+1}\}\), \(1\leq i<n\), with multiplicities. In particular \(\{a,b\}=\{b,a\}\); the spectrum records no single-letter observations. Let \(N_q(m)\) be the number of distinct spectra of words with exactly \(m=n-1\) adjacent pairs.

**Theorem (exact rational enumeration and sharp alphabet threshold).** For each fixed \(q\geq2\), the generating function \(F_q(t)=\sum_{m\geq1}N_q(m)t^m\) is the explicit rational function given by the finite parity-and-partition formula below. At the first alphabet size with a persistent parity obstruction, \(q=4\), the result simplifies to

\[
\begin{aligned}
F_4(t)={}&\frac{4t}{1-t}+\frac{6t}{(1-t)^3}+\frac{4t^2(3-2t)}{(1-t)^6}\\
&+\frac{t^3(12+27t-47t^3-2t^4+30t^5-6t^7)}{(1-t)^{10}(1+t)^4}.
\end{aligned}
\]

Its first eleven coefficients, for \(m=1,\dots,11\), are \(10,34,116,367,1060,2782,6704,14963,31276,61738,116020\). For all fixed \(q\geq2\), writing \(r=\binom{q+1}{2}\),

\[
\boxed{\displaystyle
\lim_{m\to\infty}\frac{N_q(m)}{\binom{m+r-1}{r-1}}
=\frac{1+\binom q2}{2^{q-1}}.}
\]

Thus all but a vanishing proportion of putative pair-composition spectra are realizable for alphabets of size two or three, whereas exactly \(1/8\) are asymptotically unrealizable for four symbols. For every \(q\), \(N_q(n-1)\) is also the exact maximum cardinality of a length-\(n\) code that admits error-free unique decoding from this **pair-composition-only** observation.

## Assumptions and scope

A spectrum is a vector \((m_{ab})_{a\leq b}\) of nonnegative integers with \(\sum_{a\leq b}m_{ab}=m\). Symbols are labeled; reversal does not change the spectrum. The observation comprises the compositions of **length-two contiguous factors only**, not ordered bigrams and not the joint multisets of length-one and length-two factors. All statements concern finite nonempty words and fixed \(q\) in the asymptotic limit. The case \(m=0\) is excluded because all one-letter words yield the same empty spectrum.

For a finite vertex set \(B\) with \(|B|=s\), let \(\mathcal E(B)=\binom B2\) denote its unordered pairs of *distinct* vertices. For a simple edge set \(E\subseteq\mathcal E(B)\), let \(o(E)\) be the number of vertices of odd degree in \((B,E)\). Introduce

\[
A_s(t,u)=\frac{\displaystyle\sum_{E\subseteq\mathcal E([s])}t^{|E|}u^{o(E)}}{(1-t)^s(1-t^2)^{\binom s2}}.
\]

Let \(\Pi_s\) be the set partitions of \([s]\). Define the linear functional \(\mathcal L(P)=[u^0]P+[u^2]P\) and

\[
C_s(t)=\mathcal L\!\left(\sum_{\pi\in\Pi_s}(-1)^{|\pi|-1}(|\pi|-1)!\prod_{B\in\pi} A_{|B|}(t,u)\right).
\]

Then the finite **all-alphabet exact expression** is

\[
\boxed{\displaystyle F_q(t)=\sum_{s=1}^{q}\binom qs C_s(t)-q.}
\]

Every sum is finite for fixed \(q\); no numerical interpolation is required. Here \(C_1\) includes the empty graph, which is removed by the final \(-q\).

## Proof

**1. Euler-trail equivalence.** Associate a spectrum to an undirected multigraph on the \(q\) labeled symbols: \(m_{ab}\) parallel edges join distinct symbols \(a,b\), and \(m_{aa}\) loops are based at \(a\). An adjacent word pair traverses exactly its corresponding edge. Therefore a word spelling the spectrum is an Euler trail through all edges. Conversely, a finite undirected multigraph with at least one edge admits an Euler trail precisely when the vertices incident to edges form one connected component and zero or two vertices have odd degree. The usual Euler-trail characterization extends unchanged to loops, whose degree contribution is two. Reading the successive vertices of such a trail gives a word with that spectrum. Distinct edge multiplicity vectors are distinct observations. Choosing one representative word per realizable vector yields the exact code-size statement.

**2. Parity decomposition.** For every nonloop edge type, write its multiplicity uniquely as \(2k+\epsilon\), \(k\geq0\) and \(\epsilon\in\{0,1\}\). Loops have arbitrary nonnegative multiplicity and contribute even degree. Hence each loop contributes \((1-t)^{-1}\), each nonloop edge contributes \((1-t^2)^{-1}\), and the odd nonloop types form a simple edge set \(E\), weighted by \(t^{|E|}u^{o(E)}\). This proves the formula for \(A_s\) coefficient by coefficient, without probabilistic assumptions.

**3. Connected-support extraction.** For each graph on \(s\) labeled vertices, form the partition of its connected components, regarding an unused isolated vertex as a singleton component. In the partition sum defining \(C_s\), the graph contributes \(\sum_{\pi\geq\pi_0}(-1)^{|\pi|-1}(|\pi|-1)!\), where \(\pi_0\) is its actual component partition. Möbius inversion on the partition lattice makes this sum one if the graph is connected and zero otherwise. Parities are unchanged when a graph is represented as a disjoint product of block graphs; \(\mathcal L\) retains exactly zero or two odd vertices. Consequently \(C_s\) counts connected graphs on all \(s\) vertices with the Euler-trail parity property. A nonempty graph with connected active support on the \(q\)-symbol alphabet has a unique active-vertex set \(S\); choosing \(|S|=s\) proves the expression for \(F_q\), after removing the \(q\) all-empty one-vertex terms.

**4. Quaternary algebra.** Enumerating the simple graphs on at most four labeled vertices and applying the preceding exact partition identity gives

\[
C_1(t)=\frac1{1-t},\quad
C_2(t)=\frac{t}{(1-t)^3},\quad
C_3(t)=\frac{t^2(3-2t)}{(1-t)^6},
\]
\[
C_4(t)=\frac{t^3(12+27t-47t^3-2t^4+30t^5-6t^7)}{(1-t)^{10}(1+t)^4}.
\]

Thus \(F_4=4(C_1-1)+6C_2+4C_3+C_4\), exactly as displayed. The attached standard-library checker independently constructs all simple-graph parity polynomials, all set partitions and their Möbius coefficients, and **symbolically cross-multiplies the rational identities over integers**. This verifies the finite algebra exactly, rather than relying on a finite coefficient fit.

**5. Asymptotic constant for all alphabets.** Put \(e=\binom q2\) and \(r=e+q\). With any fixed parity pattern \(\epsilon\in\{0,1\}^e\) and \(h\) odd nonloop types, the generating function for all \(q\)-vertex profiles having this exact pattern is \(t^h(1-t)^{-q}(1-t^2)^{-e}\). Its \(m\)-th coefficient is \(2^{-e}\binom{m+r-1}{r-1}+O_q(m^{r-2})\), uniformly over the finitely many patterns, by the pole at \(t=1\) (the other pole \(t=-1\) has smaller order). Over the field with two elements, the incidence map from nonloop edge parities to vertex-degree parities has rank \(q-1\), because the support graph is complete. Its image consists of the \(2^{q-1}\) even-weight vertex parity vectors, each with exactly \(2^{e-q+1}\) preimages. Precisely \(1+\binom q2\) of those vertex parity vectors have weight zero or two.

Finally, graphs with disconnected active support occupy a negligible fraction of all profiles: each lies either in a proper active-vertex subset or has no edge across some nontrivial vertex partition. In either case at least one of the \(r\) independent nonnegative edge types is forced to zero. A finite union bound makes their number \(O_q(m^{r-2})\), compared with the unrestricted \(\binom{m+r-1}{r-1}=\Theta_q(m^{r-1})\). Combining the parity count and connectivity estimate proves the limit and its sharp four-letter value.

## Verification

Run `python3 verify.py` from the package. It uses only the Python standard library. It cross-checks the four connected generating-function identities and the combined quaternary numerator by exact integer polynomial multiplication; computes the first eleven quaternary coefficients from the rational recurrence; enumerates admissible Euler multigraph vectors independently for \(q=2,3,4\), \(1\leq m\leq8\); and compares against directly enumerated words whenever the resulting word space has at most \(65536\) elements. Every check completed successfully. The asymptotic statement follows from the proven parity-rank and pole arguments, not from numeric limits.

## Relationship to prior work

Ye and Elishco (first arXiv version 2022-08-31) introduce length-limited substring-composition reconstruction and give codes for a regime in which the read cutoff scales with word length; they do not present this fixed length-two-only spectrum enumerator or the alphabet-four parity transition in the inspected Section VIII. Acharya, Das, Milenkovic, Orlitsky and Pan study reconstruction from **all** substring compositions, a strictly finer observation. Previously indexed exact binary ordered adjacent-pair multispectrum and binary joint length-one/length-two composition counts concern other observation channels; neither determines the quaternary composition-only count or the all-alphabet asymptotic ratio. The classic Euler-trail criterion and graph-partition inversion are standard inputs, not claimed discoveries.

## Limitations

The result counts distinct observable spectra, not the number of words realizing each one and not the spectrum-class-size distribution. It does not account for missing/noisy observations, and it does not assert efficient decoding for a particular selected code. The exact rational expression is finite for each fixed alphabet size but may be expensive to expand when \(q\) is large. Novelty rests on the stated literature comparisons; unindexed equivalent enumerations may exist. All verification beyond the algebraic certificate is finite corroboration, not a substitute for the mathematical proof.

## References

- Z. Ye and O. Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, arXiv:2208.14963, initial version 31 August 2022, Section VIII, https://arxiv.org/abs/2208.14963.
- J. Acharya, H. Das, O. Milenkovic, A. Orlitsky and S. Pan, *String Reconstruction from Substring Compositions*, arXiv:1403.2439, 2014, https://arxiv.org/abs/1403.2439.
- Euler's trail criterion for connected undirected multigraphs and Möbius inversion on the lattice of set partitions are classical combinatorial facts.
