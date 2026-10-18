# Isomorphism classes and automorphism groups of finite two-level S4bI frames

## Finding
For integers \(p,q\ge 2\), let \(W=A\sqcup B\), with \(|A|=p\), \(|B|=q\), and let the intuitionistic order be \(a\le b\) for every \(a\in A\), \(b\in B\), in addition to equality. Consider **reflexive and transitive** relations \(R\subseteq W\times W\) satisfying both forth-up and forth-down confluence in the sense of Fernández-Duque, McLean and Zenger. Isomorphisms preserve \(\le\) and \(R\).

Every isomorphism class of such frames is described uniquely by a pair of finite-preorder isomorphism classes with permissible **automorphism-orbits of order ideals** as marks. More precisely, choose representatives \(Q_A\) and \(Q_B\) of preorders on \(p\) and \(q\) points. A preorder has a *greatest class* when the quotient by mutual reachability has a greatest element. If \(Q_B\) has a greatest class, choose an order ideal \(U\) of \(Q_A\) up to \(\operatorname{Aut}(Q_A)\); otherwise \(U=\varnothing\). Independently, if \(Q_A\) has a greatest class, choose an order ideal \(V\) of \(Q_B\) up to \(\operatorname{Aut}(Q_B)\); otherwise \(V=\varnothing\). These choices classify all frames without duplication.

Their automorphism groups are exactly
\[
\operatorname{Aut}(W,\le,R)\cong
\operatorname{Stab}_{\operatorname{Aut}(Q_A)}(U)\times
\operatorname{Stab}_{\operatorname{Aut}(Q_B)}(V).
\]
Here the order-ideal marks are understood to be empty when disallowed.

Write \(a_n\) for the number of unlabelled \(n\)-point preorders, \(b_n\) for those with a greatest class, \(c_n\) for isomorphism classes of an \(n\)-point preorder equipped with one marked order ideal, and \(d_n\) for such marked classes whose preorder has a greatest class. Then the number \(I_{p,q}\) of isomorphism classes of these frames is exactly
\[
\boxed{I_{p,q}=a_pa_q+(c_p-a_p)b_q+(c_q-a_q)b_p+(d_p-b_p)(d_q-b_q).}
\]
The auxiliary sequences satisfy, for \(n\ge1\),
\[
 b_n=\sum_{j=0}^{n-1}a_j,\qquad
 d_n=\sum_{j=0}^{n-1}(a_j+c_j),\qquad a_0=c_0=1.
\]
Furthermore, the remaining marked-preorder counts are given without enumerating modal relations by the exact Burnside formula
\[
 c_n=\frac1{n!}\sum_{\sigma\in\mathfrak S_n}
 \sum_{Q\colon\sigma Q=Q}
 \bigl|\{U\in\operatorname{Id}(Q):\sigma U=U\}\bigr|.
\]
For \(n=2,3,4\), respectively, the tuples \((a_n,b_n,c_n,d_n)\) are \((3,2,8,5)\), \((9,5,34,16)\), and \((33,14,173,59)\). Thus
\[
\begin{array}{c|ccc}
 I_{p,q}&q=2&q=3&q=4\\\hline
 p=2&38&135&584\\
 p=3&135&452&1842\\
 p=4&584&1842&7034
\end{array}
\]
These are **unlabelled** frame counts, not the previously known counts of labelled relations on a fixed poset.

## Assumptions and scope
A preorder \(Q\) is reflexive and transitive. A set \(U\) is an *order ideal* (predecessor-closed) when \(xQy\) and \(y\in U\) imply \(x\in U\). The equivalence relation \(x\sim y\) means \(xQy\) and \(yQx\). Define \(\operatorname{Top}(Q)\) as the entire greatest equivalence class if present, and the empty set otherwise.

The confluence requirements are: for every \(x\le x'\), (forth-up) \(xRy\) implies that some \(y'\ge y\) satisfies \(x'Ry'\); (forth-down) \(x'Ry\) implies that some \(y'\le y\) satisfies \(xRy'\). No antisymmetry of \(R\) is assumed. The two levels are separately named by the fixed order; even when \(p=q\), swapping the levels is *not* an order automorphism. Claims cover all integers \(p,q\ge2\); the numerical table only illustrates small sizes.

## Proof
**1. Reconstruct the normal form.** Restricting \(R\) to its two levels gives preorders \(Q_A\) and \(Q_B\). If \(aRb\) with \(a\in A\), \(b\in B\), then for any \(b'\in B\), forth-up applied to \(a\le b'\) forces \(b'Rb\), as \(b\) is maximal in the intuitionistic order. Thus \(b\) lies in \(\operatorname{Top}(Q_B)\); transitivity forces \(a\) to reach the whole class. The set \(U\) of lower sources of these arrows is an ideal of \(Q_A\) by transitivity. Dually, if \(bRa\), forth-down for each \(a'\le b\) forces \(a'Ra\); hence the target belongs to \(\operatorname{Top}(Q_A)\), and the set \(V\) of upper sources is an ideal of \(Q_B\). Therefore necessarily
\[
R=Q_A\cup Q_B\cup\bigl(U\times\operatorname{Top}(Q_B)\bigr)
 \cup\bigl(V\times\operatorname{Top}(Q_A)\bigr).
\]
Conversely every such relation is reflexive and forth-up/down confluent: the only nontrivial confluence witnesses for cross-level edges are supplied by the greatest classes; all other cases use reflexivity. It is also transitive. Within-level compositions use preorder transitivity and ideal closure. For a two-cross-edge path, reaching the opposite top class and crossing back is possible only if the second source ideal contains that top class, which (by being an ideal) forces it to contain the entire opposite level. The resulting endpoint already lies in the greatest class reachable from every point on its level. This proves the converse and uniqueness of the marks. This labelled normal form is a **previously established ingredient**, not the present novelty.

**2. Pass to isomorphism classes.** The minimal and maximal elements of \((W,\le)\) are exactly \(A\) and \(B\). Every order automorphism is therefore a pair of permutations from \(\mathfrak S_p\times\mathfrak S_q\), and each isomorphism carries the normal-form restrictions \(Q_A,Q_B\) and the *two source ideals* \(U,V\) to their corresponding images. Conversely any pair of preorder isomorphisms preserving the permissible source ideals preserves all four terms of the displayed normal form. At fixed \(Q_A,Q_B\), the allowed source-ideal choices are independent modulo \(\operatorname{Aut}(Q_A)\times\operatorname{Aut}(Q_B)\). It follows at once that the marked preorder classes classify the frames and that the automorphism group is the product of the two stabilizers.

**3. Count the orbits.** Let \(o(Q)\) denote the number of automorphism-orbits of the ideals of \(Q\), and let \(t(Q)\in\{0,1\}\) indicate the existence of a greatest class. For a fixed pair of *unlabelled* preorders \(Q_A,Q_B\), the number of compatible frame classes is exactly
\[
\bigl(1+t(Q_B)(o(Q_A)-1)\bigr)
\bigl(1+t(Q_A)(o(Q_B)-1)\bigr).
\]
Expanding and summing over all unlabelled preorder pairs gives the boxed formula, by the definitions of \(a,b,c,d\).

**4. Reduce top-class statistics.** A preorder with a greatest class uniquely decomposes as an arbitrary preorder on \(j\) points, followed by a new greatest equivalence class of size \(n-j\ge1\). Thus \(b_n=\sum_{j<n}a_j\). For each such extension, its order ideals are precisely the ideals of the lower preorder, together with the full carrier, and automorphisms preserve this distinction. Hence its ideal-orbit count is \(o(Q)+1\). Summing gives \(d_n=\sum_{j<n}(c_j+a_j)\). Finally, Burnside's lemma applied to preorder-and-ideal pairs on \(n\) labelled points gives the formula for \(c_n\), counting ideals fixed simultaneously with their preorder.

## Verification
The accompanying `verify.py` enumerates labelled preorders and their ideals; it computes fixed-point statistics for every level permutation, Burnside averages, and canonical orbit representatives. It compares canonical relabelling against Burnside counting through \((3,2)\), tests each constructed relation against the *literal* reflexivity, transitivity, forth-up and forth-down clauses through \((3,3)\), and computes the \((3,3)\) orbit total by Burnside. The supplied `calcstats.py` also computes the unlabelled auxiliary statistics through four points and reproduces every entry of the displayed two-parameter table. The independent `exhaust_orbits.c` instead enumerates **all** reflexive candidate binary relations, without using the normal form, and confirms both labelled and unlabelled counts for \((2,2)\), \((2,3)\), and \((3,2)\). These finite tests check implementations and small instances; the proof above supplies the quantification over arbitrary sizes.

Run `python3 verify.py` using Python 3 standard library. Optionally run `cc -O3 -o exhaust_orbits exhaust_orbits.c && ./exhaust_orbits` for the direct-axiom check. Both report `VERIFY_OK` on success.

## Relationship to prior work
Fernández-Duque, McLean and Zenger introduce the bi-intuitionistic frame conditions and the reflexive/transitive modal subclasses; Balbiani, Diéguez and Fernández-Duque study the corresponding pseudo-classical S4I setting. The earlier labelled top-class normal form and its labelled counts for the same two-level poset are *stronger than, and completely cover,* the normal-form premise in Step 1. In contrast, **they do not count or classify isomorphism classes**, nor determine their automorphism groups, nor give the marked-ideal orbit formula and the recurrences for unlabelled statistics. Those are the precise claims here. Plain enumeration of unlabelled preorders is a classical separate ingredient, not claimed new.

## Limitations
The formula counts only finite two-level complete bipartite intuitionistic orders with \(p,q\ge2\), and only reflexive-transitive modal relations with both specified confluences. It does not classify all finite pseudo-classical frames, nor compute formula-equivalence classes or bisimulation quotients, and it says nothing about logics over infinite frames. The originality assessment is necessarily limited by incomplete indexing of possible equivalent counting formulations; no independent external audit is asserted.

## References
1. D. Fernández-Duque, B. McLean and L. Zenger, *A Family of Decidable Bi-intuitionistic Modal Logics*, KR 2023, pp. 262–271, DOI:10.24963/kr.2023/26, especially Definitions 4–5, full open proceedings PDF: https://proceedings.kr.org/2023/26/kr2023-0026-fernandez-duque-et-al.pdf.
2. P. Balbiani, M. Diéguez and D. Fernández-Duque, *Some constructive variants of S4 with the finite model property*, arXiv:2104.15053v1 (30 April 2021), especially its S4I semantics: https://arxiv.org/abs/2104.15053.
3. *Top-class normal form and exact census for two-level S4I frames*, earlier labelled-count result, opaque record identifier `e7e391a5-d9c0-4936-b7c0-2c4a3793fea7` (unpublished research record); used only as a prior mathematical claim, not as external certification.
