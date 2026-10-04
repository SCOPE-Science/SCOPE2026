# Quasipolynomial spanning-tree type counts for fixed-side complete bipartite graphs
## Finding
For every fixed integer \(d\ge 2\), write \(I_d(m)=\tau_{\mathrm{iso}}(K_{d,m})\). For every \(m>d\), define \(\mathcal C_d\) to be the finite set of bipartition-preserving isomorphism types of bipartite trees \(F\) with a distinguished side \(A\) of size \(d\), an opposite side of size \(k_F\in\{1,\ldots,d-1\}\), and degree at least two at every vertex outside \(A\). Let \(H_F\) be the action of \(\operatorname{Aut}(F)\) on \(A\), and for \(g\in H_F\) let \(c_j(g)\) denote the number of \(j\)-cycles of \(g\) on \(A\). Then
\[
I_d(m)=\sum_{F\in\mathcal C_d}[z^{m-k_F}]\frac{1}{|H_F|}\sum_{g\in H_F}\prod_{j=1}^d(1-z^j)^{-c_j(g)}.
\]
Therefore \(I_d(m)\) is, for every integer \(m>d\), a quasipolynomial in \(m\) of degree \(d-1\) and period dividing \(\operatorname{lcm}(1,2,\ldots,d)\). Its leading coefficient is
\[
A_d=\frac{1}{d!(d-1)!}\sum_{k=1}^{d-1}d^{k-1}S(d-1,k),
\]
where \(S(d-1,k)\) is a Stirling number of the second kind.

## Assumptions and scope
Graphs are finite and simple. Tree isomorphism is abstract unrooted graph isomorphism. The theorem fixes \(d\ge2\) and assumes \(m>d\); this strict inequality makes the two bipartition classes of every spanning tree intrinsically distinguishable by their sizes. No assertion is made here about the minimal quasipolynomial period, only that it divides \(\operatorname{lcm}(1,\ldots,d)\).

## Proof
Let \(T\) be a spanning tree of \(K_{d,m}\), and let \(A\) be its side of size \(d\). Delete every leaf of \(T\) that lies in the side of size \(m\), keeping every vertex of \(A\). The remaining graph \(F\) is a connected bipartite tree. Every retained vertex on the large side has degree at least two. Moreover,
\[
\sum_{v\notin A}(\deg_T(v)-1)=d-1.
\]
Hence if \(k_F\) retained large-side vertices remain, then \(1\le k_F\le d-1\). Thus only finitely many core types \(F\) can occur for fixed \(d\).

Conversely, fix such a core \(F\). Every spanning tree having core \(F\) is obtained by adding \(m-k_F\) new leaves on the large side and attaching each new leaf to exactly one vertex of \(A\). Hence it is encoded by a vector
\[
x=(x_a)_{a\in A}\in\mathbb Z_{\ge0}^A,\qquad \sum_{a\in A}x_a=m-k_F.
\]
Because \(m>d\), any isomorphism between two resulting trees preserves the two bipartition classes. It also preserves the set of large-side leaves and therefore restricts to an isomorphism of the recovered cores. Consequently expansions of distinct core types cannot be isomorphic, while for a fixed core \(F\) two leaf vectors give isomorphic trees exactly when they lie in the same orbit of \(\operatorname{Aut}(F)\) on \(A\).

The action on \(A\) is faithful. Indeed, suppose a core automorphism fixes \(A\) pointwise. If it sent a large-side core vertex \(u\) to a distinct vertex \(v\), then \(u\) and \(v\) would have the same neighbourhood in \(A\). Since both have degree at least two, choosing two common neighbours would create a four-cycle, impossible in a tree. Thus every vertex is fixed.

For \(g\in H_F\), a leaf vector is fixed by \(g\) exactly when it is constant on every cycle of \(g\). If \(c_j(g)\) is the number of cycles of length \(j\), the ordinary generating function for fixed vectors by total weight is
\[
\prod_{j=1}^d(1-z^j)^{-c_j(g)}.
\]
Burnside's lemma gives the displayed coefficient formula after averaging over \(H_F\) and summing over core types.

Every pole of every summand is a root of unity of order dividing \(\operatorname{lcm}(1,\ldots,d)\), so its coefficient sequence is a quasipolynomial with a period dividing that integer. The identity element of \(H_F\) has \(d\) cycles, while every nonidentity element has at most \(d-1\) cycles. Thus the contribution of \(F\) has degree \(d-1\) with leading coefficient \(1/(|H_F|(d-1)!)\).

It remains to sum these leading coefficients. For a fixed \(k\), Yan and Zhang count the labelled cores as \(d^{k-1}k!S(d-1,k)\). On the other hand, a core type \(F\) with \(k_F=k\) has exactly \(d!k!/|\operatorname{Aut}(F)|\) bipartition-respecting labellings. Since the action on \(A\) is faithful, \(|H_F|=|\operatorname{Aut}(F)|\). Therefore
\[
\sum_{F\in\mathcal C_d:\,k_F=k}\frac1{|H_F|}=\frac{d^{k-1}S(d-1,k)}{d!},
\]
and summing over \(k\) gives exactly the stated \(A_d\).

## Verification
The accompanying standard-library checker independently enumerates all core types for \(d=2,3,4\), computes their automorphism actions, compares direct orbit enumeration of weak compositions with Burnside counts for total leaf weights through eight, and verifies the labelled-core reciprocal-automorphism identity. It reproduces the classical exact formulas for \(K_{2,m}\) and \(K_{3,m}\), the published values \(28,45,73,105,152\) for \(K_{4,m}\) at \(m=5,6,7,8,9\), and independently enumerates all spanning-tree types of \(K_{3,4}\) and \(K_{3,5}\). The checker also confirms the leading coefficients \(1/2\), \(1/3\), and \(29/144\) for \(d=2,3,4\). These finite checks stress-test the construction; the all-\(d\), all-\(m>d\) theorem is proved above rather than inferred from computation.

## Relationship to prior work
Johnson and Nochumson (2026) ask for the number of isomorphism classes of spanning trees of \(K_{a,b}\) and prove partition-based lower bounds and a general upper bound, not an exact fixed-side formula. Yan and Zhang (2026) prove, for fixed \(d\), the asymptotic
\[
\tau_{\mathrm{iso}}(K_{d,n-d})=A_dn^{d-1}+O_d(n^{d-2}),
\]
and their proof introduces exactly the bounded core and leaf-vector decomposition used here. Their treatment controls the repeated-coordinate leaf vectors only as an error term. The present result replaces that error treatment with exact Burnside orbit counting, yielding an exact finite rational generating expression and quasipolynomiality for every \(m>d\).

Earlier work already covers small fixed sides: Mohr's 2008 thesis gives exact formulas for \(K_{2,t}\) and \(K_{3,t}\), as reported by van den Boomen, and van den Boomen's 2009 thesis derives a closed formula for \(K_{4,t}\). Those formulas are consistent with, and become special cases of, the general core-orbit framework above.

## Limitations
The theorem does not identify the minimal period for each \(d\), nor does it simplify the finite core sum to a single closed residue-class formula when \(d\) is large. It also does not cover the balanced case \(m=d\), where an abstract tree isomorphism may interchange the two bipartition classes. The 2008 Mohr thesis was not directly available in the material inspected; its reported \(K_{2,t}\) and \(K_{3,t}\) formulas were checked through van den Boomen's 2009 thesis, leaving a small archival risk that Mohr contained additional unpublished-looking general statements not reported there.

## References
1. P. Johnson and S. Nochumson, *Counting Isomorphism Classes of Spanning Trees of Complete Bipartite Graphs*, arXiv:2602.06867v1, 6 February 2026; revised v2, 2 March 2026.
2. Z. Yan and L.-M. Zhang, *An extremal theorem for non-isomorphic spanning trees*, arXiv:2609.30201v1, 24 September 2026.
3. J. van den Boomen, *Non-isomorphic spanning trees of graphs*, Master's thesis, Radboud University Nijmegen, July 2009.
4. A. Mohr, *Partitioning the labeled spanning trees of an arbitrary graph into isomorphism classes*, Master's thesis, 2008, cited by van den Boomen.
