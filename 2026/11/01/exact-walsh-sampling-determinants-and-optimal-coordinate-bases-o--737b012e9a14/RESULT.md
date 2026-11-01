# Exact Walsh sampling determinants and optimal coordinate bases on perfect matchings

## Finding
For an even integer \(N\ge6\), sample the uniform space of all perfect matchings of \(K_N\). For an edge \(e\), write \(X_e(M)=\mathbf1_{\{e\in M\}}\) and its Walsh character \(\chi_e(M)=1-2X_e(M)\). Select any edges \(S\), retain the constant function and \(\{\chi_e:e\in S\}\), and denote the probability-normalized Gram matrix by \(\Gamma_S\). Set \(F=E(K_N)\setminus S\), \(m=\binom N2\), \(c_N=(N-2)/((N-1)(N-3))\), and \(D_N=(N-2)^{N-1}(2N-2)\).

**Exact all-subsets determinant identity.** Let \(B_F\) denote the \(N\)-row unsigned vertex-edge incidence matrix of the graph with edges \(F\), with isolated vertices retained. Then
\[
\det\Gamma_S=(4c_N)^{|S|}\frac{\det(B_FB_F^{\mathsf T})}{D_N}
=\frac{(4c_N)^{|S|}}{D_N}\sum_{T\subseteq F\atop |T|=N,\;\text{spanning odd-unicyclic}}4^{b(T)}.
\]
Here an *odd-unicyclic spanning graph* has every component connected with exactly one cycle, that cycle odd; \(b(T)\) counts its connected components. The sum is zero when no qualifying subgraph exists. Consequently, the selected Walsh family including its constant is linearly independent **if and only if every component of the omitted-edge graph \(F\) is nonbipartite**.

**Optimal independent coordinate bases.** Exactly \(r=m-N\) distinct edge characters can be selected independently alongside the constant, and no more. At this cardinality, all positive determinants form precisely the levels
\[
\frac{(4c_N)^r4^j}{D_N},\qquad j=1,\dots,\left\lfloor\frac N3\right\rfloor.
\]
The omitted-edge graph has exactly \(N\) edges, and nonsingularity holds precisely when every component is odd-unicyclic. The determinant is largest precisely for \(b=\lfloor N/3\rfloor\) components; the collection of all such graphs is the complete family of D-optimal maximal-cardinality coordinate sets.

There are closed labeled optimizer counts. Put \(N=3b+s\) with \(s=0,1,2\). The number of maximal determinant edge sets \(S\), equivalently their complements \(F\), is
\[
\begin{cases}
\displaystyle\frac{N!}{6^b b!},&s=0,\\[4pt]
\displaystyle\frac{N!}{2\,6^{b-1}(b-1)!},&s=1,\\[4pt]
\displaystyle N!\left(\frac{162}{5!\,6^{b-1}(b-1)!}+
\frac{144}{2(4!)^2\,6^{b-2}(b-2)!}\right),&s=2.
\end{cases}
\]
These formulae count labeled edge-coordinate choices, not isomorphism classes. For \(N=6\), exactly ten coordinate sets optimize; for \(N=8\), exactly \(14{,}112\) optimize.

## Assumptions and scope
The integer \(N\) is even and at least six; the vertex set is fixed and labeled, all perfect matchings receive equal weight, Walsh characters are the real-valued functions \(1-2X_e\), all Gram inner products are uniform probability expectations, and every sampled function has unit norm. Subsets \(S\) may have any size, including empty and full. Positive Gram determinant is the *squared* sampling volume; D-optimality means maximizing that determinant among all independent families with the maximum possible number of coordinate characters.

## Proof
**1. Exact covariance projection.** Every edge lies in a uniform perfect matching with probability \(p=1/(N-1)\). Two adjacent distinct edges never co-occur; two disjoint edges co-occur with probability \(1/((N-1)(N-3))\). Therefore the centered indicator covariance \(C=(\operatorname{Cov}(X_e,X_f))\) has diagonal value \((N-2)/(N-1)^2\), adjacent-edge value \(-1/(N-1)^2\), and disjoint-edge value \(2/((N-1)^2(N-3))\).

Let \(B\) be the \(N\times m\) full unsigned incidence matrix of \(K_N\). Direct counting yields \(BB^{\mathsf T}=(N-2)I_N+J_N\), where \(J_N\) is the all-ones matrix. In particular \(B\) has full row rank and
\[
(BB^{\mathsf T})^{-1}=\frac1{N-2}\left(I_N-\frac{J_N}{2N-2}\right),\qquad
\det(BB^{\mathsf T})=D_N.
\]
For the orthogonal projection \(P=I_m-B^{\mathsf T}(BB^{\mathsf T})^{-1}B\), the diagonal/adjacent/disjoint entries above agree exactly with \(c_NP\). Thus \(C=c_NP\) for all \(N\ge6\). This equality is also consistent with the known matching-incidence spectrum [2–4], and is not asserted to be new independently.

**2. Every Gram principal minor.** Subtracting the constant part from every edge Walsh character (a determinant-preserving simultaneous row/column elimination) gives \(\det\Gamma_S=\det(4C[S,S])=(4c_N)^{|S|}\det P[S,S]\). Sylvester's determinant identity then gives
\[
\det P[S,S]=\det\left(I_N-(BB^{\mathsf T})^{-1}B_SB_S^{\mathsf T}\right)
=\frac{\det(B_FB_F^{\mathsf T})}{\det(BB^{\mathsf T})}.
\]
This argument also covers empty \(S\), with empty determinant convention one.

**3. The graph expansion.** By Cauchy–Binet,
\[
\det(B_FB_F^{\mathsf T})=\sum_{T\subseteq F,\,|T|=N}(\det B_T)^2.
\]
Decompose the spanning graph \(T\) into connected components. The square \(N\times N\) incidence submatrix has nonzero determinant only when each component has as many edges as vertices and contains an odd cycle: tree-leaf elimination reduces each such connected block to the unsigned incidence of its single odd cycle, whose determinant has absolute value two. For an even cycle the determinant vanishes. Hence \((\det B_T)^2=4^{b(T)}\) precisely for spanning odd-unicyclic graphs and is zero otherwise. This is the classical signless-Laplacian TU-subgraph expansion [1,2], specialized here to the sampling complement graph.

For arbitrary \(F\), the left kernel of \(B_F\) consists of vertex labels \(y\) satisfying \(y_u+y_v=0\) along every edge; on a connected component this kernel has dimension one if the component is bipartite and zero if it has an odd cycle. Thus \(B_F\) has row rank \(N\) precisely when all components are nonbipartite. This proves the exact independence criterion.

**4. Basis size, determinant levels and extremizers.** Since the full centered Gram covariance \(C=c_NP\) has rank \(m-N\), there cannot be more than \(r=m-N\) independent edge characters together with the constant. Construct a spanning omitted-edge graph with exactly \(N\) edges and all components odd-unicyclic (for example, an odd triangle plus attached trees and any remaining odd triangles); its complement shows this bound is achieved. At equality \(|F|=N\), the nonsingular square incidence matrix has each connected block square, so each component is odd-unicyclic, and \(\det(B_FB_F^{\mathsf T})=4^b\). Each component needs at least three vertices, so \(b\le\lfloor N/3\rfloor\), while each \(b\) in the stated range is attained by \(b-1\) triangles and a remaining odd-unicyclic connected graph. Therefore all positive determinant levels and their maximizers follow.

**5. Count all labeled maximizers.** For \(N=3b+s\), each of the \(b\) odd-unicyclic components has at least three vertices and the total excess over triples is \(s\le2\). When \(s=0\), only \(b\) triangles occur. When \(s=1\), precisely one component has four vertices (a triangle with one pendant edge), admitting exactly \(12\) labeled structures on its specified vertex set. When \(s=2\), either one component has five vertices (\(162\) connected odd-unicyclic graphs on its given five vertices), or two components have four vertices (\(12^2\) structures). The five-vertex count is \(12\) distinct five-cycles, \(90\) triangle-plus-two-separate-pendants, and \(60\) triangle-plus-two-edge-path, totaling \(162\). Partitioning the labeled vertices into unordered components produces the three displayed factorial formulas, including the two-four-vertex exchange factor \(2!\). All cases are exhausted.

## Verification
Run `python checker.py` using Python's standard library only. Its independent exact finite evaluations enumerate actual uniform perfect matchings, form the raw integer Walsh evaluation Gram matrix, compute its determinant via Bareiss elimination, and compare it to the unsigned-incidence determinant identity. It also exhausts all \(\binom{15}{6}=5005\) omitted-edge sets on six vertices, verifies component classifications, and independently counts odd-unicyclic graphs on three, four and five vertices. The checker reports 158 direct determinant comparisons, 20 maximal-cardinality comparisons, and small-component counts \(1,12,162\). The analytic proof, not these bounded calculations, establishes the theorem for every allowed \(N\).

## Relationship to prior work
The rank \(m-N+1\) of the constant-plus-edge indicator space and matching incidence spectra are known in perfect-matching Erdős–Ko–Rado theory [3,4]. Unsigned incidence ranks and odd-unicyclic column-basis criteria are known [2], as is the signless-Laplacian TU-subgraph determinant expansion [1]. This theorem does not present those facts as original. Its focused contribution is the exact probability-normalized Gram determinant for *every edge-character selection*, coupled to the complete sharp determinant spectrum, optimal coordinate-basis topology, and labeled optimizer counts in the uniform-perfect-matching Fourier sampling problem. No equivalent combined sampling-design classification was located in the inspected primary literature, but absence from a bounded search does not establish absolute historical novelty.

## Limitations
This result concerns uniform perfect matchings of the complete graph, first-degree edge Walsh characters, equal sample weights, and coordinate selection among maximal independent families. It does not characterize higher-degree Walsh interactions, arbitrary matching distributions, non-coordinate linear combinations, or the condition number of each optimal family. The harmonic covariance projection and signless incidence-minor expansion are established prior ingredients, and equivalent D-optimal matroid-basis interpretations may exist. Independent mathematical validation has not been performed.

## References
[1] J. Zhang and X.-D. Zhang, *On signless Laplacian coefficients of unicyclic graphs with given matching number*, arXiv:1212.5008v1 (public 2012-12-20), https://arxiv.org/abs/1212.5008.

[2] R. E. Behrend, *Fractional Perfect b-Matching Polytopes I: General Theory*, arXiv:1301.7356v1 (public 2013-01-30), https://arxiv.org/abs/1301.7356.

[3] N. Lindzey, *Erdős–Ko–Rado for Perfect Matchings*, arXiv:1409.2057v1 (public 2014-09-06), https://arxiv.org/abs/1409.2057.

[4] C. Godsil and K. Meagher, *An algebraic proof of the Erdős–Ko–Rado theorem for intersecting families of perfect matchings*, arXiv:1506.08770v1 (public 2015-06-29), https://arxiv.org/abs/1506.08770.
