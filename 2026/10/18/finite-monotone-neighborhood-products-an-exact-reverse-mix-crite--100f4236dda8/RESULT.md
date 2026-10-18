# Finite monotone neighborhood products: an exact reverse-mix criterion and sharp six- and nine-point obstructions

## Finding

Let \(X,Y\) be finite nonempty sets equipped with monotone reflexive (\(\mathsf T\)) neighborhood frames. At a point \((x,y)\), put \(\mathcal F=N_X(x)\) and \(\mathcal G=N_Y(y)\). Each neighborhood family is nonempty, upward closed and consists of sets containing its point; closure under intersections is **not** assumed. Give the full product its horizontal and vertical modalities \(\Box_1,\Box_2\), together with the rectangle-generated product modality \(\Box\).

Then the reverse interaction principles have the following **exact local criteria**, with validity understood for every valuation of the variable \(p\):

\[
(x,y)\models\Box_1\Box_2p\to\Box p\text{ for every valuation}
\quad\Longleftrightarrow\quad
\{x\}\in\mathcal F\ \text{or}\ \mathcal G\text{ is closed under binary intersections},
\]
\[
(x,y)\models\Box_2\Box_1p\to\Box p\text{ for every valuation}
\quad\Longleftrightarrow\quad
\{y\}\in\mathcal G\ \text{or}\ \mathcal F\text{ is closed under binary intersections}.
\]

The forward implications from \(\Box p\) to both iterated boxes always hold. A finite counterexample to either converse first exists on a product of **six** worlds, with factor sizes \(2\) and \(3\); the least full product on which **both** converses fail at one point under the **same** valuation has **nine** worlds, with factor sizes \(3\) and \(3\). Both bounds are attained by explicit reflexive monotone neighborhood products.

## Assumptions and scope

A monotone reflexive neighborhood frame on a nonempty set \(Z\) assigns to each \(z\in Z\) a nonempty family \(N_Z(z)\subseteq\mathcal P(Z)\), satisfying (i) \(A\in N_Z(z),\ A\subseteq B\subseteq Z\Rightarrow B\in N_Z(z)\), and (ii) \(A\in N_Z(z)\Rightarrow z\in A\). A *filter* additionally satisfies binary-intersection closure; that extra normality assumption is not made here.

For a set \(P\subseteq X\times Y\), put \(P_u=\{v:(u,v)\in P\}\) and \(P^v=\{u:(u,v)\in P\}\). At \((x,y)\), the three modal truth conditions are

\[
\begin{aligned}
\Box p &\iff \exists U\in\mathcal F\ \exists V\in\mathcal G:\ U\times V\subseteq P,\\
\Box_1\Box_2p &\iff \{u:P_u\in\mathcal G\}\in\mathcal F,\\
\Box_2\Box_1p &\iff \{v:P^v\in\mathcal F\}\in\mathcal G.
\end{aligned}
\]

The claimed local equivalences quantify over **all** \(P\subseteq X\times Y\). No assumption on valuations of additional variables is needed: a single variable tests all subsets. Factor neighborhood families at points other than \(x,y\) can be any monotone reflexive families. Product size always means \(|X|\,|Y|\), not the cardinality of either factor alone.

## Proof

**Forward interaction.** Suppose \(U\in\mathcal F\), \(V\in\mathcal G\) and \(U\times V\subseteq P\). For each \(u\in U\), \(P_u\supseteq V\), hence \(P_u\in\mathcal G\) by upward closure. Thus \(\{u:P_u\in\mathcal G\}\supseteq U\) belongs to \(\mathcal F\). The transpose argument proves the other direction.

**Sufficiency for the first converse.** Set \(Q=\{u:P_u\in\mathcal G\}\) and assume \(Q\in\mathcal F\). If \(\{x\}\in\mathcal F\), then the reflexivity assumption gives \(x\in Q\), so \(P_x\in\mathcal G\); the rectangle \(\{x\}\times P_x\subseteq P\) witnesses \(\Box p\). Otherwise, suppose \(\mathcal G\) is intersection-closed. Since \(X\) is finite, \(Q\) is finite and nonempty; its sections \(P_u\), for \(u\in Q\), have a common intersection \(V=\bigcap_{u\in Q}P_u\in\mathcal G\). The rectangle \(Q\times V\subseteq P\) witnesses \(\Box p\). This uses finite factor size, not finiteness of formulas.

**Necessity for the first converse.** Suppose \(\{x\}\notin\mathcal F\), and \(\mathcal G\) fails binary-intersection closure. Choose \(B_0,B_1\in\mathcal G\) with \(B_0\cap B_1\notin\mathcal G\). Choose an inclusion-minimal \(U\in\mathcal F\), possible since \(X\) is finite. Reflexivity forces \(x\in U\), and if \(|U|=1\) then \(U=\{x\}\), contradicting the supposition; hence choose distinct \(u_0,u_1\in U\). Set the sections of \(P\) as follows:

\[
P_{u_0}=B_0,\qquad P_{u_1}=B_1,\qquad
P_u=B_0\ (u\in U\setminus\{u_0,u_1\}),\qquad
P_u=\varnothing\ (u\notin U).
\]

Every section on \(U\) belongs to \(\mathcal G\), and since \(U\in\mathcal F\), the first iterated modality holds. Were \(U'\in\mathcal F,V\in\mathcal G\) to satisfy \(U'\times V\subseteq P\), then \(V\ne\varnothing\) (because every member of \(\mathcal G\) contains \(y\)). Therefore \(U'\subseteq U\). Minimality of \(U\) forces \(U'=U\), and then \(V\subseteq B_0\cap B_1\). Upward closure of \(\mathcal G\) would imply \(B_0\cap B_1\in\mathcal G\), a contradiction. Thus the reverse implication fails whenever neither disjunct of its criterion holds. Interchanging factors proves the second exact criterion.

**Six-world sharpness.** If \(|X|=1\), every nonempty reflexive upward-closed family at \(x\) contains \(\{x\}\). If \(|Y|\le2\), all subsets containing \(y\) form a chain, so any upward-closed family of such subsets is closed under intersection. Hence the first converse cannot fail unless \(|X|\ge2\) and \(|Y|\ge3\), giving a product-size lower bound \(6\). The reversed implication has the symmetric bound.

The bound is realized by \(X=\{0,1\},\ Y=\{0,1,2\}\), distinguished point \((0,0)\), and local families

\[
\mathcal F=\bigl\{\{0,1\}\bigr\},\qquad
\mathcal G=\bigl\{\{0,1\},\{0,2\},\{0,1,2\}\bigr\}.
\]

For
\[
P=\{(0,0),(0,1),(1,0),(1,2)\},
\]
\(P_0=\{0,1\}\) and \(P_1=\{0,2\}\) both lie in \(\mathcal G\), so \(\Box_1\Box_2p\) holds. Any rectangle with horizontal member \(\{0,1\}\) would require a vertical neighborhood contained in \(P_0\cap P_1=\{0\}\), which does not exist. Thus \(\Box p\) fails. Choose principal neighborhood families at the remaining points to obtain entire frames satisfying the hypotheses.

**Nine-world simultaneous sharpness.** If both converse principles fail at a point, the first criterion implies \(\mathcal G\) is non-intersection-closed and \(\{x\}\notin\mathcal F\), and the second implies \(\mathcal F\) is non-intersection-closed and \(\{y\}\notin\mathcal G\). A reflexive monotone family over a carrier of size at most two is automatically intersection-closed, so \(|X|,|Y|\ge3\). Thus at least nine product worlds are needed, even if the two failures are witnessed by different valuations.

For attainment let \(X=Y=\{0,1,2\}\), at both distinguished zeros use
\[
\mathcal F=\mathcal G=\bigl\{\{0,1\},\{0,2\},\{0,1,2\}\bigr\},
\]
and put
\[
P=\{(0,0),(0,1),(1,0),(1,2),(2,1)\}.
\]
Rows \(0\) and \(1\) are in \(\mathcal G\), while row \(2\) is not, so the set of qualifying rows is \(\{0,1\}\in\mathcal F\). Columns \(0\) and \(1\) similarly qualify, with qualifying-column set \(\{0,1\}\in\mathcal G\). Both iterated modalities hold. However the rows indexed by either allowable two-element horizontal neighborhood have intersection \(\{0\}\) or \(\{1\}\), neither in \(\mathcal G\); the three-element horizontal neighborhood is even more restrictive. Hence the rectangle modality fails. Other local families may again be taken principal. This is one valuation causing both converse failures.

## Verification

The accompanying standard-library program `CHECK.py` independently enumerates all nonempty upward-closed reflexive neighborhood families at a distinguished point on one-, two-, and three-element carriers, all valuations on their products, and the three modalities directly from their truth conditions. For each pair of carrier sizes through \(3\times3\), it confirms both exact criteria and the expected first possible failures. For \(2\times3\) it checks \(640\) family/valuation configurations, and for \(3\times3\) it checks \(12800\), including a common-valuation failure of both converses. It also checks the two displayed witnesses directly. Run with `python3 CHECK.py`; successful output terminates in `EXACT_FINITE_T_PRODUCT_OK; 2x3 and 3x3 witnesses confirmed`.

The finite enumeration corroborates only sizes at most three per factor. The unrestricted finite equivalence, all size lower bounds, and both examples are independently proved above. No claim is made about the same criterion for arbitrary infinite families, where nonprincipal set-theoretic obstructions may intervene.

## Relationship to prior work

Aghamov, Kudinov, Nguyen and Piribauer (2026) introduce the three modalities of full neighborhood products and prove the forward interaction \(\Box p\to\Box_1\Box_2p\wedge\Box_2\Box_1p\) for their **normal filter** neighborhood frames. For finite normal frames, the rectangle modality is already known to agree with both iterated modalities: every finite filter is principal. The present theorem keeps the three modal definitions but *drops finite-intersection closure*, while retaining monotonicity and reflexivity. It identifies the precise pointwise condition that replaces finite-normality, and proves the first finite failures have six or nine product worlds.

Sano's (2011) monotone neighborhood products address two coordinate modalities and hybrid interactions, rather than the additional rectangular modality compared with their iteration here. Kudinov's (2014) neighborhood product likewise concerns the two-coordinate setting. Neither gives the two finite reverse-mix equivalences or sharp simultaneous finite threshold stated here. The distinction from the existing rectangularization result is substantive: the latter characterizes the reverse implication for **filter pairs**, for which the present finite failures are excluded by hypothesis.

## Limitations

The biconditionals are pointwise and require **finite** factors. The claimed lower bounds concern Cartesian-product size and local validity over all propositional valuations; they do not say every product at those cardinalities fails. The described class is monotone reflexive and potentially nonnormal. The source paper's normal full-product completeness theorem is not being extended to a nonnormal logic axiomatization. Absolute historical priority over unindexed nonnormal neighborhood literature is not claimed.

## References

1. Rajab Aghamov, Andrey Kudinov, Maik Thanh Nguyen and Jakob Piribauer, *On Modal Logics of Full Products of Neighborhood Frames*, EPTCS 447 (2026), 1–15, DOI 10.4204/EPTCS.447.1, arXiv:2606.31852 (first posted 2026-06-30).
2. Katsuhiko Sano, *Axiomatizing Hybrid Products of Monotone Neighborhood Frames*, Electronic Notes in Theoretical Computer Science 273 (2011), 51–67, DOI 10.1016/j.entcs.2011.06.012.
3. Andrey Kudinov, *Neighbourhood Frame Product KxK*, Advances in Modal Logic 10 (2014).
4. *Rectangularization exactly controls modality elimination in neighborhood full products*, public research note, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-rectangularization-exactly-controls-modality-elimination-in-neig--d3f6516314ba.
