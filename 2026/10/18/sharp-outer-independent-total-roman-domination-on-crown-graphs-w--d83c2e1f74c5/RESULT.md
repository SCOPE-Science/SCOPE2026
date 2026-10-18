# Sharp outer-independent total Roman domination on crown graphs, with all optimal labelings

## Finding

Let \(\operatorname{Cr}_n\) have two labeled parts \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where \(a_i\) is adjacent to \(b_j\) precisely when \(i\ne j\). For every integer \(n\ge3\), an outer-independent total Roman dominating function is a labeling \(f:V\to\{0,1,2\}\) for which the zero set is independent, each zero-labeled vertex has a label-two neighbor, and every positively labeled vertex has a positive neighbor. Its weight is the sum of its labels.

The exact minimum weight and number of optimum labelings are
\[
\boxed{\gamma_{oitR}(\operatorname{Cr}_n)=\begin{cases}6,&n=3,\\ n+3,&n\ge4,\end{cases}}
\qquad
\boxed{\#\mathrm{Opt}(\operatorname{Cr}_n)=\begin{cases}25,&n=3,\\2n(n-1),&n\ge4.\end{cases}}
\]

For every \(n\ge4\), these optima have just one shape: on one chosen side, label exactly two vertices by one and the other \(n-2\) by zero; on the opposite side, label exactly one vertex by two and all others by one. The unique label-two vertex must be the deleted-matching partner of one of the selected label-one vertices. Hence there are \(2\binom n2\cdot2=2n(n-1)\) optima.

For \(n=3\), the \(25\) optimum labelings consist of the all-one labeling, twelve with one zero and one label-two vertex on opposite sides (all other vertices labeled one), and twelve with two zeros on the ends of one deleted-matching pair and one label-two vertex in each part (all others labeled one).

The known complete bipartite value \(\gamma_{oitR}(K_{n,n})=n+2\) for \(n\ge3\) is increased by one under deletion of a perfect matching for every \(n\ge4\).

## Assumptions and scope

All graphs are finite, simple and undirected; vertex and deleted-pair labels are fixed. Roman labels zero, one and two are distinct. The zero-set independence requirement is essential: ordinary total Roman domination is a different invariant. The theorem does not claim a full generating polynomial for nonoptimal labelings or any result for \(n=2\).

## Proof

Let \(Z\) be the set of zero vertices. Since every cross pair except \(\{a_i,b_i\}\) is adjacent, independence forces one of three disjoint cases: \(Z=\varnothing\), \(Z\) lies entirely on one side, or \(Z=\{a_i,b_i\}\) for one index \(i\). There are no other possibilities.

**No zeros.** Every vertex has a positive label, so the weight is at least \(2n\). The all-one labeling meets every condition for \(n\ge3\).

**Zeros on both sides.** The zeros must be exactly \(a_i,b_i\). Each needs a label-two neighbor, and their neighborhoods lie on opposite sides, so at least one of the \(n-1\) remaining positive vertices on each side must be labeled two. All \(2n-2\) other vertices are positive, so the weight is at least \((2n-2)+2=2n\). Equality holds when there is exactly one label-two vertex among the remaining vertices on each side and all others are labeled one; every positive vertex then has a positive neighbor for \(n\ge3\). At \(n=3\), there are \(n(n-1)^2=12\) such labelings.

**Zeros on just one side.** By symmetry, suppose they lie on \(A\). All \(B\) vertices are positive. Let \(p\) be the number of positive vertices on \(A\). Every positive vertex in \(B\) must have a positive neighbor in \(A\). If \(p=1\), the vertex of \(B\) paired by the missing edge with that sole positive \(A\)-vertex has no positive neighbor, which is impossible. Thus \(p\ge2\). As some \(A\)-vertex is zero, its defense needs a label-two vertex in \(B\). Hence the weight is at least \(n+p+1\ge n+3\). Equality requires exactly two label-one vertices in \(A\), precisely one label-two vertex in \(B\), and all other \(B\)-vertices labeled one. Conversely, for such a configuration the only requirement on the label-two vertex \(b_j\) is that its index \(j\) not belong to the zero set of \(A\), because \(b_j\) has no edge to \(a_j\). For \(n\ge4\), two chosen positive \(A\)-vertices and two choices for \(j\) give \(2\binom n2\) configurations when the zero side is \(A\), and the same number for zero side \(B\). All positive vertices do have positive neighbors because the other side is fully positive and the chosen zero side has two positive vertices.

For \(n\ge4\), \(2n\ge n+4>n+3\), hence neither the zero-free nor two-side-zero cases can be optimal. The displayed constructions attain the lower bound and comprise every optimum. For \(n=3\), \(2n=n+3=6\); the three cases contribute, respectively, one all-one, twelve two-side-zero, and \(2\cdot3\cdot2=12\) one-side-zero functions, for total \(25\). This proves every formula and classification.

## Verification

The independent checker `verification/check_crown_oitrd.py` iterates all \(3^{2n}\) labeled maps for \(3\le n\le6\), implements the three conditions directly from graph adjacency, calculates minimum weight and its multiplicity, and categorizes all optima by their zero-patterns. Its stdout is retained in `verification/check_output.txt`. It exhaustively tests \(3^6+3^8+3^{10}+3^{12}=597780\) labelings, a finite check independent of the proof.

## Relationship to prior work

Cabrera Martínez, Kuziak and Yero introduced this precise domination parameter and later established its basic comparison bounds. Their open paper on relationships records \(\gamma_{oitR}(K_{r,s})=r+2\) for \(3\le r\le s\), but does not list a crown-graph minimum and exact optimum multiplicity in its examined special-family sections. A previously available exact total Roman polynomial on crown graphs concerns labelings **without the independent-zero constraint**, hence does not imply the current optimum weight or multiplicity. Other nearby published results involve perfect Roman domination of crowns, or outer-independent Roman functions on complete multipartite graphs, neither of which combines these same restrictions on this matching-deleted family. The asserted original contribution is the sharp change under matching deletion and complete classification of all optimum functions, not the underlying domination definition or the complete-bipartite value.

## Limitations

Novelty remains a best-knowledge comparison rather than absolute priority proof. The full original 2019 introduction paper was accessible in repository abstract/metadata but was not inspected in full, so coverage in its special families remains a bibliographic risk. The exact formula for nonoptimum configurations was not pursued. The exhaustive computer check covers only \(3\le n\le6\); the infinite proof is combinatorial. No independent validation has been performed.

## References

- A. Cabrera Martínez, D. Kuziak, I. G. Yero, *Outer-independent total Roman domination in graphs*, Discrete Applied Mathematics 269 (2019), 107–119, DOI 10.1016/j.dam.2018.12.018, public repository https://rodin.uca.es/handle/10498/30892 .
- A. Cabrera Martínez, D. Kuziak, I. G. Yero, *Relating the outer-independent total Roman domination number with some classical parameters of graphs*, arXiv:2112.05476 (first posted 10 December 2021), https://arxiv.org/abs/2112.05476 .
- A. Cabrera Martínez, D. Kuziak, I. G. Yero, same title, Mediterranean Journal of Mathematics 19 (2022), article 144, DOI 10.1007/s00009-022-02061-y .
