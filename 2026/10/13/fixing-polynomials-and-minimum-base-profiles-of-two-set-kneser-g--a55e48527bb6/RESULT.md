# Fixing polynomials and minimum-base profiles of two-set Kneser graphs

## Finding

For every integer \(n\ge5\), let \(K(n,2)\) denote the Kneser graph whose vertices are the two-element subsets of \([n]=\{1,\ldots,n\}\), adjacent precisely when disjoint. A *fixing set* (or *determining set*) is a subset of its vertices having trivial **pointwise** stabilizer in its graph automorphism group. Define the fixing polynomial
\[
\Phi_n(z)=\sum_{\substack{S\subseteq V(K(n,2))\\S\text{ fixing}}}z^{|S|}.
\]
This polynomial counts every fixing set, without identifying sets under automorphisms.

**Complete polynomial.** Set
\[
\mathcal G(t,z)=\sum_{m\ge0}(1+z)^{\binom m2}\frac{t^m}{m!}.
\]
For every \(n\ge5\), the exact fixing polynomial is
\[
\boxed{\Phi_n(z)=n![t^n](1+t)\exp\!\left(-t-\frac{zt^2}{2}\right)\mathcal G(t,z).}
\]
The coefficient operator extracts only the stated \(n\)-th coefficient. The expression's auxiliary coefficients at orders below five are *not* claimed to be fixing polynomials of Kneser graphs.

**Structural characterization.** Identify each selected vertex \(\{i,j\}\in S\) of \(K(n,2)\) with the edge \(ij\) of a simple graph \(H_S\) on the *labeled* ground set \([n]\). Then \(S\) is fixing if and only if \(H_S\) has **no two-vertex component** and **at most one isolated vertex**. Equivalently, its components have orders at least three, apart from at most one isolated vertex.

**Minimum fixing sets.** The already-known minimum cardinality is \(d_n=\lfloor2n/3\rfloor\). All fixing sets of size \(d_n\) are forests. Their component sizes are exactly:

* If \(n=3q+1\), one isolated vertex and \(q\) three-vertex paths.
* If \(n=3q+2\), one isolated vertex, one four-vertex tree, and \(q-1\) three-vertex paths.
* If \(n=3q\), either \(q\) three-vertex paths; or one isolated vertex, one five-vertex tree, and \(q-2\) three-vertex paths; or, for \(q\ge3\), one isolated vertex, two four-vertex trees, and \(q-3\) three-vertex paths.

Writing \(D_n=[z^{d_n}]\Phi_n(z)\), the exact number of labeled minimum fixing sets is
\[
\boxed{D_{3q+1}=\frac{(3q+1)!}{2^q q!},\qquad
D_{3q+2}=\frac{2(3q+2)!}{3\cdot2^{q-1}(q-1)!},}
\]
and, for \(q\ge2\),
\[
\boxed{
D_{3q}=\frac{(3q)!}{2^q q!}
+\frac{125(3q)!}{120\cdot2^{q-2}(q-2)!}+E_q,}
\]
where the third summand is defined without a singular factorial at the boundary:
\[
E_q=\begin{cases}
0,&q=2,\\[2pt]
\dfrac{256(3q)!}{2(4!)^2\,2^{q-3}(q-3)!},&q\ge3.
\end{cases}
\]
The first two formulas apply only when their indices also satisfy the global assumption \(n\ge5\).

## Assumptions and scope

All graphs are finite and simple, all ground vertices are individually labeled, and \(n\ge5\). The graph automorphism group of \(K(n,2)\) is the natural symmetric-group action on \([n]\), a standard fact used by the cited Kneser-graph literature. Fixing means *pointwise*, not merely setwise, stabilization. A polynomial coefficient counts a subset of distinct unordered two-element vertices once, irrespective of any symmetry of its selected-edge graph. The exponential series is formal in \(t\), with coefficients in \(\mathbb Q[z]\); no analytic convergence is required.

## Proof

**Step 1: an exact pointwise-stabilizer test.** Every permutation \(\sigma\in S_n\) fixes every selected two-subset \(\{i,j\}\in S\) setwise as a two-subset if and only if it preserves the incident-edge membership signature of each ground vertex. Two ground vertices \(a,b\) can be transposed while all selected two-subsets remain fixed exactly when their membership signatures coincide. Indeed, if signatures are all distinct, any such permutation must preserve each signature and hence fixes each ground vertex. Conversely, a signature repetition yields the nonidentity transposition \((a\ b)\) that fixes each selected edge.

The vertices of a selected-edge graph with no incident edge all share the empty signature; hence there can be at most one. A connected component on two ground vertices is exactly an isolated selected edge, and its two endpoints both have the same singleton-edge signature. In a component with at least three vertices, signatures are pairwise different: different nonincident vertices have disjoint nonempty sets of incident edges; if two adjacent vertices have the same signature, their common selected edge is their sole incident edge and is an isolated two-vertex component. Therefore all signatures are distinct if and only if there is no two-vertex component and at most one isolated vertex. This is also a direct specialization of the known Kneser determining-set separation criterion [2, 3].

**Step 2: full enumerator.** A simple graph on \(m\) labeled ground vertices has \(\binom m2\) possible edges, so the weight enumerator over all such graphs is \((1+z)^{\binom m2}\). The labeled exponential formula decomposes graphs uniquely into connected components. Singleton components contribute exponential factor \(e^t\), and isolated two-vertex edge components contribute \(e^{zt^2/2}\). Removing both component types therefore multiplies \(\mathcal G(t,z)\) by \(e^{-t-zt^2/2}\). Allowing either zero or exactly one singleton component multiplies by \(1+t\). By Step 1 these are precisely the labeled selected-edge graphs of fixing sets, proving the coefficient identity for every \(n\ge5\).

For direct coefficient extraction, let \(H_n(z)=n![t^n]e^{-t-zt^2/2}\mathcal G(t,z)\). Then
\[
H_n(z)=\sum_{j=0}^n\ \sum_{k=0}^{\lfloor(n-j)/2\rfloor}
(-1)^{j+k}\frac{n!\,z^k(1+z)^{\binom{n-j-2k}{2}}}
{j!\,2^k k!\,(n-j-2k)!},
\qquad \Phi_n(z)=H_n(z)+nH_{n-1}(z).
\]
The convention \(H_0(z)=1\) makes all displayed finite sums unambiguous.

**Step 3: minimum structures.** Suppose the selected-edge graph has \(a\in\{0,1\}\) isolated ground vertices and \(c\) nontrivial components of orders at least three. Then \(c\le\lfloor(n-a)/3\rfloor\) and
\[
|S|\ge(n-a)-c\ge(n-a)-\left\lfloor\frac{n-a}{3}\right\rfloor.
\]
Minimizing this lower bound over \(a\) yields \(d_n=\lfloor2n/3\rfloor\). Explicit forests consisting of the stated three-, four-, or five-vertex trees attain it. In any graph attaining equality, every nontrivial component must be a tree; otherwise it contains an extra edge. The exact number of nontrivial components then determines the excess of their orders over three, which is zero, one, or two, giving precisely the component-size alternatives listed in the finding. No other components or cycle-containing graphs can attain the minimum.

**Step 4: exact labeled enumeration.** Cayley's theorem gives \(s^{s-2}\) labeled trees on \(s\) specified ground vertices; in particular three-, four-, and five-vertex trees have counts \(3,16,125\). For a forest with \(b_s\) indistinguishable tree components of size \(s\) and \(a\) isolated vertices, its number of labeled realizations is
\[
\frac{n!}{a!\,\prod_{s\ge3}(s!)^{b_s}b_s!}\prod_{s\ge3}\big(s^{s-2}\big)^{b_s}.
\]
Inserting the enumerated component profiles gives exactly the three displayed residue-class formulas for \(D_n\). This counts each selected-edge set once and completes the proof.

## Verification

The standalone standard-library script `artifacts/verify_fixing.py` independently constructs incidence signatures, connected-component tests, and the coefficient identity. It exhaustively checks every selected-edge subset for \(n=5,6,7\), independently checks all size-minimum candidate subsets for \(n=8,9\), compares coefficient formulas through \(n=21\), and checks the two highest coefficients against the binomial edge count. The exact outcomes are in `artifacts/checks.txt`. A finite calculation corroborates, but is not a substitute for, the preceding proof.

For example, the leading nonzero coefficients are \(D_5=80\), \(D_6=840\), \(D_7=630\), \(D_8=13440\), and \(D_9=277200\).

## Relationship to prior work

The fixing polynomial as an all-cardinality enumerator was introduced by Javaid–Fazil–Ali–Salman [1], whose Section 3 studies examples including cycles and complete multipartite graphs. Boutin's separation lemma, used by Cáceres–Garijo–González–Márquez–Puertas [2] and Das–Dey [3], already characterizes when a family of Kneser vertices is determining. In particular, the known determining number \(d_n=\lfloor2n/3\rfloor\) is **not new**. Albertson–Boutin [4] study distinguishing colorings obtained using Kneser determining sets, not their full cardinality distribution. Del Valle–Roney-Dougal [5] supply general **minimum base-size** formulas for symmetric-group actions, rather than the polynomial of every base or the labeled number of optimal bases. The present result specializes known feasibility characterizations to two-subsets and adds the full labeled fixing polynomial and complete count/classification of its minimum layer. Those new enumerative statements were not found in the inspected results; this is a literature-comparison judgment, not a proof of global uniqueness.

## Limitations

The theorem is restricted to \(K(n,2)\) with \(n\ge5\); it does not characterize fixing polynomials for higher subset sizes. The known scalar determining number and the general Kneser point-separation criterion are explicitly prior results. Although the enumerator follows from a specialized structural reduction and the standard labeled exponential formula, an unindexed presentation under the terminology of permutation-group bases, separating systems, or incidence-distinct graphs could overlap. Independent verification by another researcher has not been performed.

## References

1. I. Javaid, M. Fazil, U. Ali, M. Salman, *On Some Parameters Related to Fixing Sets in Graphs*, public author copy uploaded 2017-05-22: https://www.researchgate.net/publication/317041311_ON_SOME_PARAMETERS_RELATED_TO_FIXING_SETS_IN_GRAPHS.
2. J. Cáceres, D. Garijo, A. González, A. Márquez, M. L. Puertas, *The determining number of Kneser graphs*, Discrete Mathematics & Theoretical Computer Science 15 (2013), 1–14: https://dmtcs.episciences.org/en/articles/634/download.
3. A. Das, H. K. Dey, *Determining Number of Kneser Graphs: Exact Values and Improved Bounds*, first arXiv version 2020-09-17: https://arxiv.org/abs/2009.08787.
4. M. O. Albertson, D. L. Boutin, *Using Determining Sets to Distinguish Kneser Graphs*, Electronic Journal of Combinatorics 14 (2007), R20: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v14i1r20/pdf.
5. C. del Valle, C. M. Roney-Dougal, *The base size of the symmetric group acting on subsets*, arXiv first posted 2023-08-08; Algebraic Combinatorics 7 (2024), 959–967: https://arxiv.org/abs/2308.04360.
