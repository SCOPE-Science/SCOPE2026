# Sharp one-comparability sensitivity and local counting hardness for random-poset one-types

## Finding
Let \(\mathbb P\) be the countable universal homogeneous partial order. For a finite bipartite graph \(G=(A\sqcup B,E)\), with nonempty specified sides, form the height-at-most-two poset \(P_G\) by setting \(u<v\) exactly when \(uv\in E\), \(u\in A,v\in B\). Let \(t(G)\) be the number of complete nonalgebraic one-types in \(\mathbb P\) over the individually named elements of \(P_G\). Choose a nonedge \(ab\) with \(a\in A,b\in B\), and write \(G^+=G+ab\). Denote the bipartite complement by \(\bar G\), and the number of vertex-independent subsets of a finite graph \(H\) (including the empty subset) by \(i(H)\). Put
\[
 R=V(G)\setminus(\{a,b\}\cup N_G(a)\cup N_G(b)),\qquad S=N_G(a)\cup N_G(b).
\]
Here \(G[R]\) and \(\bar G[S]\) are induced bipartite graphs. Then the exact signed change caused by the single new comparability is
\[
 \Delta_e t:=t(G^+)-t(G)=i(\bar G[S])-2i(G[R]). \tag{1}
\]
For \(n=|A|+|B|\ge2\), this has the **sharp two-sided range**
\[
 1-2^{n-1}\ \leq\ \Delta_e t\ \leq\ 2^{n-2}-2. \tag{2}
\]
Equality on the left holds exactly when \(G\) has no edges. Equality on the right holds exactly when \(G=K_{|A|,|B|}-ab\), i.e. every possible cross-edge other than \(ab\) is already present. In particular, for every \(n\ge4\), imposing one new order relation can INCREASE the complete nonalgebraic one-type count by exactly \(2^{n-2}-2\), despite restricting the parameter order.

Moreover, restrict input pairs \((G,ab)\) by the promise that \(a\) is adjacent to every vertex of \(B\setminus\{b\}\) and \(b\) to every vertex of \(A\setminus\{a\}\). On this family the nonnegative integer-valued function
\[
 D(G,ab):=\Delta_e t+2
\]
is \(\#\mathrm P\)-complete under polynomial-time Turing reductions. Indeed, \(D(G,ab)=i(\bar G[(A\setminus\{a\})\cup(B\setminus\{b\})])\), and the bipartite graph on the right can be arbitrary. This is an exact local counting-complexity statement, not a claim of hardness of approximating independent sets.

## Assumptions and scope
The old order has no relations within \(A\) or within \(B\), and all strict relations run from \(A\) to \(B\). Every element is named as a separate parameter. The pair \(a,b\) is a nonedge of the **specified bipartite graph**. Isolated vertices are permitted, so the parameter order may have height one; after adding \(ab\) it has height two. All formulas count nonalgebraic one-types, not algebraic equality types. The complexity claim uses binary-encoded exact integer outputs and standard polynomial-time Turing reductions; it makes no assertion about parsimonious completeness of the unshifted, possibly negative, difference \(\Delta_e t\). The bounds concern one new cross-level comparability; they are not asserted for arbitrary new relations in unrestricted posets.

## Proof
**1. Extension profiles.** The extension property and ultrahomogeneity of \(\mathbb P\) identify every nonalgebraic one-type over a finite poset \(P\) with a pair \((L,U)\) of disjoint subsets: \(L=\{v:v<x\}\) is a downset, \(U=\{v:x<v\}\) an upset, and every \(l\in L\) is strictly below every \(u\in U\). Conversely, this condition constructs a finite poset on \(P\cup\{x\}\), realized in \(\mathbb P\), and two different profiles give different complete types. In a bipartite height-two poset, the number of downsets equals \(i(G)\): choose the upper-layer vertices of a downset, then any lower-layer set containing their neighbors; this is in bijection with choosing an independent set of \(G\) by complementing the lower-layer choice. The same number counts upsets. The profiles with one of \(L,U\) empty therefore contribute \(2i(G)-1\). If both are nonempty, necessarily \(L\subseteq A\), \(U\subseteq B\), and all cross pairs between them are edges of \(G\). These correspond to independent sets in the bipartite complement having at least one vertex in each side. Their number is \(i(\bar G)-2^{|A|}-2^{|B|}+1\). Consequently
\[
 t(G)=2i(G)+i(\bar G)-2^{|A|}-2^{|B|}. \tag{3}
\]
This identity is previously available and is used as the starting point, not claimed as new here.

**2. Local difference.** Independent sets destroyed on inserting the edge \(ab\) into \(G\) are exactly those containing both endpoints. They biject with independent subsets of \(G[R]\), giving \(i(G^+)-i(G)=-i(G[R])\). Simultaneously \(\overline{G^+}=\bar G-ab\), and independent sets newly gained upon removing \(ab\) from \(\bar G\) are exactly those containing both endpoints. Their remaining vertices lie in \(S=N_G(a)\cup N_G(b)\) and must form an independent set of \(\bar G[S]\). Hence \(i(\overline{G^+})-i(\bar G)=i(\bar G[S])\). Substitution into (3) yields (1).

**3. Sharp bounds and equality.** Because \(R\) and \(S\) partition the \(n-2\) vertices other than \(a,b\), \(1\le i(G[R])\le 2^{|R|}\) and \(1\le i(\bar G[S])\le2^{|S|}\). Thus (2) follows. For the lower bound to be an equality one must have \(|R|=n-2\), \(i(G[R])=2^{n-2}\), and \(i(\bar G[S])=1\). The first equality makes \(a,b\) isolated and the second forces no other edges, so \(G\) is empty; conversely an empty \(G\) attains the bound. For the upper bound, equality forces \(|S|=n-2\), \(i(\bar G[S])=2^{n-2}\), and \(i(G[R])=1\). Thus \(a\) meets every \(B\setminus\{b\}\), \(b\) meets every \(A\setminus\{a\}\), and \(\bar G[S]\) has no edges, so every remaining cross-edge also lies in \(G\). Precisely \(G=K_{|A|,|B|}-ab\); its converse is immediate. At \(n=2\), both bounds and both extremal descriptions coincide.

**4. Local hardness.** Under the stated near-universal-neighbor promise, \(S=V\setminus\{a,b\}\) and \(R=\varnothing\), whence (1) becomes \(D(G,ab)=i(\bar G[S])\). Given any bipartite input \(H=(X\sqcup Y,F)\), construct \(A=X\cup\{a\}\), \(B=Y\cup\{b\}\) and let \(G\) contain all \(aY\) edges, all \(Xb\) edges, and exactly the \(XY\) edges absent from \(H\), but not \(ab\). Then \(\bar G[S]=H\) and \(D(G,ab)=i(H)\) without a scaling factor or a second oracle call. This construction is polynomial in \(|X|+|Y|\). Exact bipartite independent-set counting is \(\#\mathrm P\)-complete, equivalently counting bipartite vertex covers. On the promised family, \(D\) itself counts independent subsets of an explicitly computable bipartite graph, so is in \(\#\mathrm P\). Together these establish the promised \(\#\mathrm P\)-completeness.

## Verification
The bundled standard-library Python program `verify.py` forms every bipartite graph with fixed nonempty parts and total size at most six, and for each missing cross-edge compares (1), (2), and both equality characterizations against an independently computed extension count. The latter enumerates all three-way positions of the new point and computes the transitive closure on \(n+1\) vertices, rejecting cycles or induced order changes. For the hardness gadget it also compares the type-count difference with a direct independent-set census on small exhaustive and sampled inputs. Its recorded output is in `verification_output.txt`. Finite tests corroborate, but do not replace, the proof for all \(n\) and the complexity reduction.

## Relationship to prior work
The general height-two count (3), previously derived in research on random-poset type counting, covers absolute values \(t(G)\) but does not by itself provide the signed local-change classification, sharp equality cases, or the promised one-change \(\#\mathrm P\) realization. Pretzel (1980) studies the poset of insertion positions and its dimension, a related but differently quantified invariant. Provan and Ball (1983) establish the relevant exact bipartite counting hardness; Ge and Štefankovič (2009/2010) develop an independent-set-encoding bipartite graph polynomial, not one-type sensitivity. The independent-set edge recurrences used here are elementary; their combination into a sharp local type-sensitivity and counting-completeness result is the contribution. No claim of newness is made for (3) or for bipartite independent-set hardness itself.

## Limitations
The extremal inequalities rely on the specified two-level bipartition. The hardness theorem is about exact computation with a near-universal-edge promise, not approximate counting or unrestricted signed-output membership in \(\#\mathrm P\). The relevant 1980 Pretzel article was only accessible at abstract level during comparison; an unexamined specialized antecedent is a residual originality risk. No independent scientific review or external certification is claimed.

## References
- O. Pretzel, “A construction for partially ordered sets,” *Discrete Mathematics* 32 (1980), 59–68, DOI 10.1016/0012-365X(80)90100-4.
- J. S. Provan and M. O. Ball, “The complexity of counting cuts and of computing the probability that a graph is connected,” *SIAM Journal on Computing* 12 (1983), 777–788, DOI 10.1137/0212053.
- Q. Ge and D. Štefankovič, “A graph polynomial for independent sets of bipartite graphs,” arXiv:0911.4732, initially public 2009-11-24, https://arxiv.org/html/0911.4732v4.
