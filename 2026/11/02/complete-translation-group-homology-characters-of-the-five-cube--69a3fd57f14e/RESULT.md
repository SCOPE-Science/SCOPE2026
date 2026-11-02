# Complete translation-group homology characters of the five-cube at Čech scale three

## Finding
Let \(Q_5\) denote the graph on \(\{0,1\}^5\), with edges between Hamming-distance-one vertices, and let \(X=\mathcal N(Q_5,3)\) be the nerve of closed balls of radius \(3/2\) centered at its vertices, in the geometric realization of \(Q_5\). The translation group \(T=(\mathbb Z/2\mathbb Z)^5\) acts by addition on binary strings.

For \(S\subseteq[5]=\{1,2,3,4,5\}\), let the one-dimensional rational character \(\chi_S:T\to\{\pm1\}\) be \(\chi_S(t)=(-1)^{\sum_{i\in S}t_i}\). Then the **complete rational translation representation** is
\[
\widetilde H_3(X;\mathbb Q)\cong\bigoplus_{|S|=4}\chi_S\ \oplus\ \chi_{[5]}^{\oplus4},
\qquad
\widetilde H_4(X;\mathbb Q)\cong
\bigoplus_{|S|=1}\chi_S^{\oplus6}\ \oplus
\bigoplus_{|S|=2}\chi_S^{\oplus6}\ \oplus
\bigoplus_{|S|=3}\chi_S^{\oplus3}.
\]
All other reduced rational homology groups vanish; the dimensions of these two groups are \(9\) and \(120\). For a translation of Hamming weight \(w\), the character values are:

| \(w\) | 0 | 1 | 2 | 3 | 4 | 5 |
|:---:|---:|---:|---:|---:|---:|---:|
| \(\operatorname{tr}(t\mid\widetilde H_3)\) | 9 | -7 | 5 | -3 | 1 | 1 |
| \(\operatorname{tr}(t\mid\widetilde H_4)\) | 120 | 24 | -12 | -12 | 0 | 0 |

No nonzero translation-invariant positive-degree rational homology survives. Consequently \(\widetilde H_*(X/T;\mathbb Q)=0\).

## Assumptions and scope
This is the ordinary simplicial Čech nerve whose vertices are precisely the \(32\) graph vertices and whose closed balls live in the geometric graph, not the distinct Vietoris–Rips or discrete-vertex Čech construction. There are exactly \(80\) facets indexed by unordered graph edges \(uv\), each the ten-element set \(N_1[u]\cup N_1[v]\). The group \(T\) acts on the **five binary coordinates**, not on labels of cells or homology generators. Homology is reduced except where indicated; all representations are over \(\mathbb Q\). The conclusion applies only to this fixed graph and filtration scale; there is no asserted general formula for other cube dimensions or Čech scales.

## Proof
**Facet presentation.** For each cube edge \(uv\), define \(F_{uv}=N_1[u]\cup N_1[v]\). The odd-integer-scale Čech description in Adams–Shukla–Singh, Lemma 2.2, identifies \(X\) with the down-closure of these facets. With vertices encoded by integers \(0,\ldots,31\), the \(80\) edges \(u,u\mathbin{\mathrm{xor}}2^i\) enumerate every facet once. All face sets are tested exactly by the attached checker.

**Integral homology ranks (independent verification).** The down-closure has \(54{,}416\) nonempty simplices, with dimension-by-dimension face vector \((32,400,2560,8320,14592,14752,9280,3600,800,80)\). Process binary vertices \(0,\ldots,31\): at vertex \(v\), match every remaining face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), if both are still present, and delete both. This defines \(27{,}134\) valid, pairwise-disjoint incidences; the fully reversed-matched Hasse diagram on all \(54{,}416\) faces is acyclic. The unmatched cells comprise one zero-cell, eighteen three-cells and 129 four-cells. Exact recursive elimination along all matched three/four incidences gives the signed degree-four Morse boundary matrix of size \(18\times129\). It has 54 entries, all \(\pm1\), and Smith normal form with exactly nine unit nonzero factors; hence the integral reduced ranks are \(\beta_3=9\), \(\beta_4=120\), with no torsion or other reduced homology. This agrees with the published nonequivariant calculation but is established afresh for the representation argument.

**Signed fixed-face enumeration.** Every translation \(t\) acts simplicially. For \(t\ne0\), the 32 vertices form sixteen transposition orbits \(\{x,x+t\}\). A nonempty simplex fixed setwise by \(t\) is a union of \(m\) such orbits and therefore has \(2m\) vertices. Its orientation sign under \(t\) is \((-1)^m\). As its simplicial dimension is \(2m-1\), its contribution to the ordinary Lefschetz number is \((-1)^{m-1}\). The reduced Lefschetz number further subtracts one for the augmentation chain. Exhaustive orbit-pair enumeration from the 80 facets, repeated for each of the 32 group elements, yields, in Hamming-weight order \(w=0,\ldots,5\),
\[
\widetilde L_w=(111,31,-17,-9,-1,-1).
\]
At the identity, this is independently the alternating sum of the face vector with the empty-face correction, \(120-9=111\).

**Fourier inversion and positivity.** The reduced equivariant Euler character is the virtual character \(\chi_{H_4}-\chi_{H_3}\), because reduced homology is concentrated in the two adjacent degrees. For each \(S\subseteq[5]\), character orthogonality gives the integer virtual multiplicity
\[
v(S)=\frac1{32}\sum_{t\in T}\chi_S(t)\widetilde L_{|t|}.
\]
The exact values depend only on \(|S|=0,\ldots,5\) and are \((0,6,6,3,-1,-4)\), respectively. Denote nonnegative actual multiplicities by \(m_3(S),m_4(S)\), so \(m_4(S)-m_3(S)=v(S)\). The negative virtual coefficients force at least one degree-three copy for each of five characters of weight four, and four degree-three copies for the unique character of weight five. These **already account for all nine** degree-three homology dimensions. Thus there are no other degree-three summands, and degree-four multiplicities are precisely the positive virtual coefficients. This proves both claimed decompositions and all trace values without presupposing equivariance of the vertex-ordered Morse matching.

**Quotient.** Both decompositions omit \(\chi_\varnothing\), so every positive-degree rational invariant space under \(T\) is zero. For a finite simplicial group action, rational homology of the orbit space agrees with invariant rational homology (for example by passing to equivariant simplicial chains after barycentric subdivision). Connectivity supplies degree zero.

## Verification
Run `python3 checker.py` with Python 3 and SymPy. It independently generates all faces from the 80 facet sets, checks every matching incidence and every one of the \(54{,}416\) oriented Hasse vertices for global acyclicity, computes the full integer Morse boundary and its Smith form, enumerates **all 32 translations** and their signed fixed-simplex Lefschetz numbers, Fourier-transforms the resulting virtual character, and checks that the negative Fourier coefficients saturate the entire nine-dimensional degree-three homology. The expected terminal line is `HYPERCUBE5_CECH3_TRANSLATION_CHARACTER_EXACT_OK`. Finite exhaustive enumeration proves the stated **single finite complex** and full 32-element action, not a conjectured infinite family. No outsourced or independent audit is claimed.

## Relationship to prior work
Adams, Shukla and Singh (first public arXiv posting December 12, 2022), *Čech complexes of hypercube graphs*, prove the odd-radius facet description (Lemma 2.2), two-connectedness and dimension/homology bounds at scale three (Section 5), and tabulate this five-cube's **nonequivariant** Betti numbers (Section 3). They ask a general homotopy-type question (Question 7.1). None of those results fixes the translation character: equal Betti numbers permit many inequivalent \(T\)-modules. The contribution here is only the precise two-degree **equivariant translation representation** and its quotient consequence, not the previously documented Betti ranks or a universal homotopy theorem. The closest indexed four-cube scale-three result has a different graph dimension; the six-cube scale-three result is nonequivariant; scale-two hypercube equivariance concerns a different nerve. No implication from those checked statements determines the five-cube scale-three character.

## Limitations
This theorem concerns rational representations: it does not determine integral \(\mathbb Z[T]\)-module extensions or the action of coordinate permutations, nor does it generalize to all cube dimensions. The original nonequivariant homology ranks are not claimed as original. The available index entries for some related deposited results expose titles/abstract summaries rather than inspectable full documents; an unindexed or unavailable coincident computation is a residual bibliographic risk. Reproducing the finite result requires the attached exact program and SymPy; the mathematical reconstruction and Fourier positivity argument do not depend on an external database or numerical approximation.

## References
1. H. Adams, S. Shukla, A. Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871 (first public posting 2022-12-12), https://arxiv.org/abs/2212.05871. In particular Lemma 2.2, Section 3, Section 5 and Question 7.1.
2. Relevant indexed results: *The hyperoctahedral homology character of the four-cube Čech nerve at scale three* (published-finding corpus ID `2026/10/11/SCOPE-the-hyperoctahedral-homology-character-of-the-four-cube-ech-nerv--89c403fdb3a1`); *The integral homotopy type of the six-cube graph Čech complex at scale three* (ID `2026/10/11/SCOPE-the-integral-homotopy-type-of-the-six-cube-graph-ech-complex-at--6a192e252576`); *Translation characters of scale-two hypercube Čech complexes* (ID `2026/10/11/SCOPE-translation-characters-of-scale-two-hypercube-ech-complexes--8c586ad49940`). Only indexed claims could be compared for these related deposits.
