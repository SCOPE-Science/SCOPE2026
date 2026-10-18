# Top-class normal form and exact census for two-level S4I frames

## Finding

Let \(p,q\geq 2\). Fix labelled, disjoint antichains \(A\) and \(B\) with \(|A|=p\) and \(|B|=q\), and equip \(W=A\sqcup B\) with the complete height-two intuitionistic order \(\leq\): every element of \(A\) lies below every element of \(B\), and points within each level are incomparable unless equal. A **two-level S4I frame** is an infallible frame \((W,\leq,R)\) in which \(R\) is a reflexive, transitive relation satisfying both forth–up and forth–down confluence (defined below).

For a finite preorder \(Q\) on a set \(X\), write
\[
\operatorname{Top}(Q)=\{t\in X:(\forall x\in X)\ xQt\}.
\]
This is either empty or one entire greatest equivalence class of \(Q\). A \(Q\)-downset is a subset \(D\subseteq X\) satisfying \(xQy\land y\in D\Rightarrow x\in D\).

**Classification.** The S4I relations on the fixed two-level poset are exactly the relations
\[
\boxed{R=Q_A\ \cup\ Q_B\ \cup\bigl(U\times\operatorname{Top}(Q_B)\bigr)\ \cup\bigl(V\times\operatorname{Top}(Q_A)\bigr)}
\]
where \(Q_A\) and \(Q_B\) are arbitrary preorders on \(A\) and \(B\), respectively; \(U\) is a \(Q_A\)-downset, and \(V\) is a \(Q_B\)-downset. Here the products are subsets of \(A\times B\) and \(B\times A\), respectively. When \(\operatorname{Top}(Q_B)=\varnothing\) we canonically take \(U=\varnothing\), and when \(\operatorname{Top}(Q_A)=\varnothing\) we canonically take \(V=\varnothing\); with these conventions, the description is unique.

Let \(\mathcal P_n\) be the collection of preorders on a fixed labelled \(n\)-point set. For \(Q\in\mathcal P_n\), put \(d(Q)=|\{D\subseteq X:D\text{ is a }Q\text{-downset}\}|\) and \(g(Q)=1\) if \(\operatorname{Top}(Q)\ne\varnothing\), with \(g(Q)=0\) otherwise. Define four numerical invariants
\[
P_n=\sum_{Q\in\mathcal P_n}1,\quad
G_n=\sum_{Q\in\mathcal P_n}g(Q),\quad
T_n=\sum_{Q\in\mathcal P_n}d(Q),\quad
E_n=\sum_{Q\in\mathcal P_n}g(Q)d(Q).
\]
For fixed \(Q_A,Q_B\), the number of compatible relations is exactly
\[
\bigl[1+g(Q_B)(d(Q_A)-1)\bigr]\,
\bigl[1+g(Q_A)(d(Q_B)-1)\bigr].
\]
Consequently, the exact number of labelled two-level S4I relations is
\[
\boxed{
N_{p,q}=(P_p-G_p)(P_q-G_q)
 +(T_p-E_p)G_q+G_p(T_q-E_q)+E_pE_q.
}
\]
The first genuinely two-sided cases are
\[
\boxed{N_{2,2}=89,\quad N_{2,3}=762,\quad N_{3,3}=5922,\quad N_{2,4}=11534,\quad N_{4,4}=1062296.}
\]
The formula is symmetric in \(p,q\), even though the underlying two-level orders need not be isomorphic after exchanging the levels. The structural proof works for all \(p,q\geq1\); the stated theorem highlights \(p,q\geq2\), where both levels branch.

## Assumptions and scope

All world sets are finite and labelled. There are **no fallible worlds**. The intuitionistic order \(\leq\) is fixed, and only the modal accessibility preorder \(R\) varies. We use the S4I confluence conventions of Balbiani, Diéguez and Fernández-Duque [1]:
\[
\begin{aligned}
\mathrm{FU}:\quad &x\leq y\ \land\ xRz\ \Longrightarrow\
 \exists w\ (z\leq w\ \land\ yRw),\\
\mathrm{FD}:\quad &x\leq y\ \land\ yRz\ \Longrightarrow\
 \exists w\ (xRw\ \land\ w\leq z).
\end{aligned}
\]
Since \(R\) is a preorder, it has a partition of each level into strongly connected (mutual-accessibility) equivalence classes; \(\operatorname{Top}(Q)\) is the unique greatest one when it exists. The theorem counts labelled expansions of this one fixed intuitionistic poset, not arbitrary finite S4I frames, models, valuations or formulas. No claim about isomorphism-class counts or logical inequivalence of these frames is made.

## Proof

**1. Necessary cross-level restrictions.** Let \(R\) be any S4I relation, and write \(Q_A=R\cap(A\times A)\) and \(Q_B=R\cap(B\times B)\). Both are preorders.

Suppose \(aRb\) with \(a\in A\), \(b\in B\). For every \(b'\in B\), we have \(a\leq b'\). Apply FU to \(a\leq b'\) and \(aRb\). Some \(w\geq b\) must satisfy \(b'Rw\). Since \(b\) is maximal for \(\leq\), necessarily \(w=b\). Thus every \(b'\in B\) satisfies \(b'Q_Bb\), so \(b\in\operatorname{Top}(Q_B)\). Transitivity also implies that if \(a'Q_Aa\) then \(a'Rb\), and if \(bQ_Bb'\), then \(aRb'\). Any \(b'\) reachable from a greatest point remains greatest. Hence the \(A\)-to-\(B\) cross block has the form \(U\times\operatorname{Top}(Q_B)\), where \(U=\{a\in A:\exists b\in B\ aRb\}\) is a \(Q_A\)-downset. If the top class is absent, this block is empty.

Dually, suppose \(bRa\) with \(b\in B\), \(a\in A\). For every \(a'\in A\) we have \(a'\leq b\). Apply FD to \(a'\leq b\) and \(bRa\). Some \(w\leq a\) must satisfy \(a'Rw\); since \(a\) is minimal for \(\leq\), necessarily \(w=a\). Hence every \(a'\in A\) satisfies \(a'Q_Aa\), so \(a\in\operatorname{Top}(Q_A)\). Transitivity forces the \(B\)-to-\(A\) cross block to be \(V\times\operatorname{Top}(Q_A)\) for a \(Q_B\)-downset \(V\). These restrictions determine the parameters uniquely whenever their associated top class is nonempty.

**2. Sufficiency and transitivity.** Conversely fix arbitrary \(Q_A,Q_B,U,V\) as in the statement and construct \(R\) from the displayed union. Reflexivity is immediate. For transitivity, the within-level products \(Q_A\circ Q_A\subseteq Q_A\) and \(Q_B\circ Q_B\subseteq Q_B\) follow from the preorder assumptions. The mixed products \(Q_A\circ(U\times\operatorname{Top}(Q_B))\) and \(Q_B\circ(V\times\operatorname{Top}(Q_A))\) are included in their respective cross blocks by downward closure of \(U\) and \(V\). The opposite within-level products preserve those blocks because every greatest equivalence class is upward closed under its preorder. Finally, the two alternating cross-level compositions land in \(Q_A\) or \(Q_B\), because **every** point reaches every point of its preorder’s greatest class. Thus all composable pairs are transitive.

To verify confluence it suffices to consider a nontrivial intuitionistic comparison \(a\leq b\) with \(a\in A,b\in B\). For FU, if \(aRz\) and \(z\in A\), choose \(w=b\): reflexivity gives \(bRb\) and \(z\leq b\). If instead \(z\in B\), then \(z\in\operatorname{Top}(Q_B)\), so \(bRz\) and we choose \(w=z\). For FD, if \(bRz\) and \(z\in B\), choose \(w=a\), using \(aRa\) and \(a\leq z\). If instead \(z\in A\), then \(z\in\operatorname{Top}(Q_A)\), so \(aRz\) and choose \(w=z\). When \(x=y\), both confluence clauses follow by taking the already given endpoint. Therefore the constructed relation is an S4I relation.

**3. Counting.** Fix \(Q_A,Q_B\). If \(\operatorname{Top}(Q_B)=\varnothing\), there is exactly one \(A\)-to-\(B\) cross block: the empty one. Otherwise it is indexed without collisions by the \(d(Q_A)\) downsets \(U\). Similarly the number of \(B\)-to-\(A\) blocks is \(1\) or \(d(Q_B)\), according to whether \(\operatorname{Top}(Q_A)\) is empty or not. These choices are independent by part 2. Multiplying gives the fixed-pair formula.

Partitioning the pairs \((Q_A,Q_B)\) by presence or absence of their greatest classes yields four contributions: \((P_p-G_p)(P_q-G_q)\), \((T_p-E_p)G_q\), \(G_p(T_q-E_q)\), and \(E_pE_q\), respectively. Summing proves the displayed formula for \(N_{p,q}\).

For an optional independent way to compute two ingredients, extend the conventions \(P_0=T_0=1\). Choosing the nonempty top equivalence class of size \(k\), and then an arbitrary preorder on the remaining \(n-k\) elements, gives
\[
G_n=\sum_{k=1}^{n}\binom{n}{k}P_{n-k},
\qquad
E_n=\sum_{k=1}^{n}\binom{n}{k}(T_{n-k}+P_{n-k}).
\]
For each such preorder the downsets are precisely the downsets of the non-top part together with the entire set. This confirms the top-class contributions in the counting formula.

## Verification

The standalone, standard-library-only script `verify.py` enumerates all labelled preorders on sets of sizes \(1\) through \(5\), independently identifies their greatest equivalence classes and downsets, and computes
\[
\begin{array}{c|rrrrr}
n&1&2&3&4&5\\\hline
P_n&1&4&29&355&6942\\
G_n&1&3&16&145&2111\\
T_n&2&12&130&2338&66304\\
E_n&2&8&59&746&15232
\end{array}
\]
It separately performs **literal exhaustive tests** of reflexivity, transitivity, FU and FD, comparing the complete sets of relations with those generated by the normal form on the eight pairs
\[
(p,q)\in\{(1,1),(1,2),(2,1),(2,2),(1,3),(3,1),(2,3),(3,2)\}.
\]
For all eight, the two sets coincide exactly (not merely in cardinality); counts are \(4,20,20,89,189,189,762,762\). The numerical formula is then checked also for \((3,3),(2,4),(3,4),(4,4),(5,5)\), yielding \(5922,11534,82511,1062296,470978369\). Run `python3 verify.py` to reproduce `VERIFY_OK`.

The finite computations corroborate the theorem and detect small-case errors. They are **not** substituted for the general proof of the classification or the formula.

## Relationship to prior work

Balbiani, Diéguez and Fernández-Duque [1, Definitions II.4 and II.7] introduced the relevant infallible S4I bi-preorders and identified the two confluence conditions; they established a finite-model property. Balbiani, Diéguez, Fernández-Duque and McLean [2, Definitions 6–7 in the first preprint] developed finite birelational frame results. Both sources treat S4I frames broadly, but the inspected full texts do not give a structural classification or the exact finite census for a fixed complete height-two intuitionistic order.

Balbiani, Gao, Gencer and Olivetti [3] studied locally interpreted intuitionistic modal logics under forward and downward confluence, including reflexive and transitive extensions, but their inspected text concerns proof theory and finite countermodel constructions rather than the present two-parameter classification.

Related published finite-chain normal forms count relations over a *totally ordered* intuitionistic reduct, and a different involutive Fischer–Servi-frame normal form forces modal targets to be minimal. Neither result implies this theorem: when \(p,q\geq2\), the present intuitionistic reduct has incomparable points at both levels, the modal relation is a preorder, and its allowed targets need not be intuitionistically minimal.

The new normal form isolates precisely how the two confluences constrain the cross-level arrows through globally greatest modal strongly connected classes, reducing enumeration to two within-level preorders and their downsets. This provides an exact finite test family for the bifurcating height-two case not addressed by chain formulas.

## Limitations

The result applies only to the fixed complete two-level intuitionistic order, not to arbitrary height-two incidence posets or arbitrary S4I frames. It counts *labelled* modal relations, without quotienting by permutations of each antichain, and does not classify nonisomorphic frames or formula theories. No new finite-model property, decidability bound or asymptotic for all S4I frames follows. All numerical values above follow from the finite formula and were computed exactly, but only the stated small pairs were checked via exhaustive relation-level search. Equivalence to an older combinatorial description using different terminology cannot be ruled out by search alone.

## References

[1] P. Balbiani, M. Diéguez, D. Fernández-Duque, “Some constructive variants of S4 with the finite model property,” arXiv:2104.15053v1, first public 30 April 2021, https://arxiv.org/html/2104.15053v1 .

[2] P. Balbiani, M. Diéguez, D. Fernández-Duque, B. McLean, “Constructive S4 modal logics with the finite birelational frame property,” arXiv:2403.00201v1, first public 1 March 2024, https://arxiv.org/html/2403.00201v1 .

[3] P. Balbiani, H. Gao, Ç. Gencer, N. Olivetti, “Local Intuitionistic Modal Logics and Their Calculi,” arXiv:2403.06772v1, 2024, https://arxiv.org/html/2403.06772v1 .
