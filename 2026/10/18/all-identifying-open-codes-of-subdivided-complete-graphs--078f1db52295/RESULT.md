# All identifying open codes of subdivided complete graphs

## Finding

Let \(n\ge3\) be an integer. Let \(B_n=S(K_n)\) be the graph obtained by subdividing *every* edge of a labelled complete graph once. Its bipartition is \(V=[n]\) (original vertices) and \(E=\binom{[n]}2\) (the vertices replacing the original edges). An **identifying open code** is a set \(C\subseteq V(B_n)\) for which every intersection \(N_{B_n}(w)\cap C\) is nonempty and these intersections are pairwise distinct.

Write \(C=X\sqcup F\), with \(X\subseteq V\) and \(F\subseteq E\). Regard \(F\) also as the edges of a spanning simple graph \(H_F=([n],F)\). Then the following is an *if and only if* classification:

\[
C\text{ is an identifying open code}\quad\Longleftrightarrow\quad
|X|\ge n-1\ \text{and every component of }H_F\text{ has at least three vertices}.
\]

The component condition is equivalently the absence of isolated vertices and isolated-edge components \(K_2\); other components may contain cycles. Consequently, if \(P_n(z)=\sum_C z^{|C|}\) ranges over **all** identifying open codes of \(B_n\), then

\[
P_n(z)=(nz^{n-1}+z^n)A_n(z),\qquad
A_n(z)=\sum_{\substack{F\subseteq\binom{[n]}2\\ H_F\text{ has no component of order }1\text{ or }2}}z^{|F|}.
\]

The complete edge factor has the labelled exponential generating function

\[
\sum_{n\ge0} A_n(z)\frac{x^n}{n!}
=\exp\!\left(-x-\frac{zx^2}{2}\right)
\sum_{j\ge0}(1+z)^{\binom j2}\frac{x^j}{j!}.
\]

Here the formal auxiliary values \(A_0(z)=1\), \(A_1(z)=A_2(z)=0\) are used in the generating function; the code theorem concerns \(n\ge3\). An explicit finite form, requiring no generating-function coefficient extraction, is

\[
A_n(z)=\sum_{\substack{a,b\ge0\\a+2b\le n}}
\frac{(-1)^{a+b}n!\,z^b}{a!\,b!\,2^b\,(n-a-2b)!}
(1+z)^{\binom{n-a-2b}{2}}.
\]

In particular, the minimum identifying open code size is

\[
\boxed{\gamma_{\mathrm{IOC}}(B_n)=n-1+\left\lceil\frac{2n}{3}\right\rceil.}
\]

Every minimum code consists of exactly \(n-1\) original vertices, together with the subdivision vertices corresponding to a spanning forest with \(\lfloor n/3\rfloor\) tree components, each of order at least three. The forest characterization is exhaustive.

For completeness, put \(q=\lfloor n/3\rfloor\) and let \(T_n\) denote the number of labelled minimizing edge subsets. With \(\mu_3,\mu_4,\mu_5\) ranging over nonnegative integers, one has the exact finite expression

\[
T_n=n!\!\sum_{\substack{3\mu_3+4\mu_4+5\mu_5=n\\
\mu_3+\mu_4+\mu_5=q}}
\prod_{s=3}^{5}\frac{(s^{s-2})^{\mu_s}}{(s!)^{\mu_s}\mu_s!},
\qquad
\#\{\text{minimum codes}\}=nT_n.
\]

Only component sizes three, four and five occur at the minimum. Equivalently, for \(n=3q\), \(T_n=n!/(2^q q!)\); for \(n=3q+1\), \(T_n=n!\, (2/3)\,2^{-(q-1)}/(q-1)!\); and for \(n=3q+2\),

\[
T_n=n!\left(
\frac{25}{24}\frac{2^{-(q-1)}}{(q-1)!}
+\mathbf 1_{\{q\ge2\}}\frac{2}{9}\frac{2^{-(q-2)}}{(q-2)!}
\right).
\]

All counts refer to labelled vertices and labelled code subsets, not automorphism orbits.

## Assumptions and scope

All graphs are finite, simple and undirected. In \(S(K_n)\), **every** original edge is replaced by a length-two path. Each original vertex is adjacent exactly to the subdivision vertices indexing its incident edges; each subdivision vertex indexed by \(\{i,j\}\) is adjacent exactly to \(i\) and \(j\). The term *identifying open code* is synonymous with an open-locating-dominating set and an open-separating total-dominating code, not a closed-neighborhood identifying code or an ordinary locating-total-dominating set. The theorem is asserted for all integers \(n\ge3\), with no asymptotic or hidden degree assumptions.

## Proof

**Step 1: Separate the two kinds of signatures.** For an original vertex \(i\in[n]\), the open code signature is

\[
N_{B_n}(i)\cap C=\{\{i,j\}\in F:j\ne i\},
\]

while for an edge-vertex \(e=\{i,j\}\in E\), it is

\[
N_{B_n}(e)\cap C=X\cap\{i,j\}.
\]

The former consists of subdivision vertices, the latter of original vertices. If both are nonempty, no original-vertex signature can equal an edge-vertex signature. Thus nonemptiness and pairwise distinctness can be assessed separately within the two bipartition classes.

**Step 2: The original-vertex selection.** For every edge-vertex \(\{i,j\}\), its signature must be nonempty. If two distinct original vertices were outside \(X\), the edge-vertex joining them would have empty signature, hence \(|X|\ge n-1\). Conversely, if \(|X|=n\), every edge-vertex has its own distinct two-element signature; if \(|X|=n-1\), the unique omitted vertex is \(u\), edges incident with \(u\) have distinct singleton signatures and all other edges have distinct two-element signatures. Thus all edge-vertex signatures are nonempty and distinct precisely when \(|X|\ge n-1\).

**Step 3: The selected-edge condition.** For an original vertex, nonempty signature means positive degree in \(H_F\). Suppose distinct original vertices \(i,j\) have the same nonempty signature. Every edge in that common set must be incident with both \(i\) and \(j\); in a simple graph the only such edge is \(\{i,j\}\). It follows that both have degree exactly one and form an isolated \(K_2\) component. Conversely, the two endpoints of an isolated \(K_2\) component have the same singleton signature, and an isolated vertex has empty signature. Therefore the original-vertex signatures are nonempty and pairwise distinct if and only if the graph has no isolated vertices and no isolated \(K_2\) components, exactly the condition that every component has at least three vertices. Steps 1–3 prove the full code classification and the polynomial factorization.

**Step 4: Enumerate every code.** All labelled simple graphs on \(j\) vertices have edge-count polynomial \((1+z)^{\binom j2}\). The exponential formula for labelled graph components expresses their full generating function as the exponential of the connected-component generating function. Removing components of order one (one structure, weight \(x\)) and order two (the isolated edge, weight \(zx^2/2\)) gives the displayed expression for \(A_n(z)\). Expanding the two negative exponentials yields the finite double sum. Finally, for any admissible \(F\) there are \(n\) choices of \(X\) with \(|X|=n-1\) and one choice with \(|X|=n\), proving the claimed polynomial for every coefficient.

**Step 5: Minimum size and equality.** Suppose \(H_F\) has \(c\) connected components of orders \(v_1,\ldots,v_c\), each at least three. Then \(c\le\lfloor n/3\rfloor\), while every connected component contains at least \(v_i-1\) edges. Consequently

\[
|F|\ge\sum_{i=1}^c(v_i-1)=n-c\ge n-\lfloor n/3\rfloor
=\lceil2n/3\rceil.
\]

The lower bound is attained by partitioning the vertices into \(q=\lfloor n/3\rfloor\) blocks of sizes at least three and taking any spanning tree on each block: distribute the remainder \(n-3q\in\{0,1,2\}\) among the blocks. Equality throughout the displayed inequalities holds *only* if \(c=q\) and each connected component is a tree. The smallest permitted original-vertex selection has \(n-1\) members, independently of \(F\). Thus the claimed minimum size and the exhaustive minimum-code characterization follow.

**Step 6: Count every minimum.** Since \(q\) blocks each have size at least three and their total excess is at most two, the only allowed component-size profiles are: \(q\) size-three trees when \(n=3q\); \(q-1\) size-three trees and one size-four tree when \(n=3q+1\); or one size-five tree and \(q-1\) size-three trees, plus the additional option of two size-four trees and \(q-2\) size-three trees when \(n=3q+2\). Cayley's tree formula gives \(s^{s-2}\) labelled trees on a specified \(s\)-element vertex set. Partitioning the \(n\) labels into \(\mu_s\) unordered blocks of each size \(s\) gives \(n!/\prod_s((s!)^{\mu_s}\mu_s!)\). Multiplying these quantities and summing the admissible profiles proves \(T_n\) and its residue-class expressions. Finally the one omitted original vertex can be chosen in \(n\) ways, giving exactly \(nT_n\) minimum codes. This counts all minimizers with no overlap.

## Verification

A standalone Python file, `verify.py`, implements the open-neighborhood definition directly on the full subdivision graph and an independent test using selected-edge incidence signatures. For \(n=3,4,5\), it checks every possible code subset: respectively \(64\), \(1,024\), and \(32,768\) subsets. For \(n=3,4,5,6\) it exhaustively checks every selected-edge graph and compares every coefficient against the independently evaluated exponential-formula polynomial. In the same range it checks the predicted minimum and the Cayley-count formulas. The direct edge-graph enumeration finds, respectively, \(4,38,728,26{,}864\) admissible edge selections, and minimum-edge multiplicities \(3,16,125,90\). The corresponding minimum-code counts are \(9,64,625,540\). All tests pass. This finite testing supports the calculations but is not used as a proof for arbitrary \(n\); Steps 1–6 supply that proof.

To reproduce, use a standard installation of Python 3 and run `python verify.py`. The code uses only the Python standard library; neither remote data nor auxiliary files are required.

## Relationship to prior work

The open-neighborhood condition here is the identifying-open-code/OLD/OTD notion studied by Chakraborty and Wagler, *On lower bounds for cardinalities of several separating-dominating codes in graphs*, arXiv:2412.17469 (first public version December 23, 2024). That work establishes universal lower bounds and characterizes their extremal graph constructions; the present theorem instead obtains a complete code classification, polynomial, and optimal multiplicities for the all-edges-subdivided clique.

Chakraborty, Foucaud and Henning, *Identifying open codes in trees and 4-cycle-free graphs of given maximum degree*, arXiv:2407.09692, prove degree/order bounds and analyze subdivided stars. Their bound is general enough to apply to the current family but does not yield the exact enumerator, sharp value or equality classification here. Argiroffo, Bianchi, Lucarini and Wagler, *The Identifying Code, the Locating-dominating, the Open Locating-dominating and the Locating Total-dominating Problems Under Some Graph Operations* (2019), analyze universal vertices, generalized coronas, and squares of paths and cycles; these operations are distinct from full edge subdivision of a clique. Work on **closed** identifying-code numbers of graph subdivisions, including Mirasheh, Abbasi and Vatandoost, concerns a different, noncomparable identifying parameter and does not imply the open-code polynomial or its minimum multiplicities.

For a complete base graph, the central-graph construction coincides with full subdivision, \(C(K_n)=S(K_n)\). The published *Exact vertex-cover formula for total domination of central graphs* gives the ordinary total-domination value \(\gamma_t(S(K_n))=n-1+\lceil n/2\rceil\), which does not enforce the distinct-signature requirement. Thus the extra separation cost in the present theorem is exactly \(\lceil2n/3\rceil-\lceil n/2\rceil\); neither the all-code generating function nor the equality forests follow from ordinary total domination. The related published double-subdivision construction with pendant paths treats a different graph family and establishes a minimum number, rather than the one-subdivided clique code polynomial.

No published source examined establishes this precise full-subdivision-clique result. This is a best-knowledge comparison, not a proof of historical priority. Standard labelled exponential-formula and Cayley tree-counting tools are used as known combinatorial inputs.

## Limitations

The result is restricted to the one-subdivision of a *complete* graph; no claim is made for arbitrary base graphs or for closed-neighborhood codes. The polynomial counts labelled subsets, not equivalence classes under automorphisms. Exhaustive tests cover only the stated finite ranges; the infinite conclusion depends on the displayed proof. Bibliographic completeness and independent mathematical validation remain outstanding.

## References

1. D. Chakraborty and A. K. Wagler, *On lower bounds for cardinalities of several separating-dominating codes in graphs*, arXiv:2412.17469v1, December 23, 2024. https://arxiv.org/abs/2412.17469
2. D. Chakraborty, F. Foucaud and M. A. Henning, *Identifying open codes in trees and 4-cycle-free graphs of given maximum degree*, arXiv:2407.09692. https://arxiv.org/html/2407.09692v2
3. G. R. Argiroffo, S. M. Bianchi, Y. Lucarini and A. K. Wagler, *The Identifying Code, the Locating-dominating, the Open Locating-dominating and the Locating Total-dominating Problems Under Some Graph Operations*, Electronic Notes in Theoretical Computer Science **346** (2019), 135–145. DOI:10.1016/j.entcs.2019.08.013.
4. K. Mirasheh, A. Abbasi and E. Vatandoost, *Proof of a conjecture for the identifying code number of the subdivision of graphs*, Transactions on Combinatorics **15** (2026), 231–234. DOI:10.22108/toc.2025.143773.2228. This work concerns closed-neighborhood identifying codes.
5. *Exact vertex-cover formula for total domination of central graphs*, publicly available mathematical research result (September 2026); its complete-clique specialization gives the ordinary total-domination number rather than the identifying-open-code number.
6. Classical labelled exponential formula for graph connected components, and Cayley's tree enumeration \(s^{s-2}\).
