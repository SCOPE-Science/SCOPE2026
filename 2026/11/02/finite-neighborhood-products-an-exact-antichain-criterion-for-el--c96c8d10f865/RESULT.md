# Finite neighborhood products: an exact antichain criterion for eliminating the rectangle modality

## Finding
Let \(X,Y\) be nonempty finite sets of sizes \(m,n\). At each \(x\in X\) and \(y\in Y\), assign a nonempty upward-closed family \(\mathcal A_x\subseteq\mathcal P(X)\setminus\{\varnothing\}\) and \(\mathcal B_y\subseteq\mathcal P(Y)\setminus\{\varnothing\}\). No closure under intersections is assumed. The full neighborhood product has the horizontal, vertical, and rectangular box modalities \(\Box_1,\Box_2,\Box\), respectively.

Write \(\min(\mathcal A_x)\) and \(\min(\mathcal B_y)\) for the antichains of inclusion-minimal neighborhoods. **The sharp local criterion** is: for every Boolean valuation \(p\subseteq X\times Y\), the equivalence
\[
 (x,y)\models\Box p\leftrightarrow\Box_1\Box_2p
\]
holds exactly when either *every* minimal member of \(\mathcal A_x\) is a singleton, or \(\mathcal B_y\) has a unique minimal member. Symmetrically, equivalence with \(\Box_2\Box_1\) holds exactly when every minimal member of \(\mathcal B_y\) is a singleton or \(\mathcal A_x\) has a unique minimal member. Since the product-to-iterated implications always hold, these characterize precisely when their converses are valid. The criterion also applies to all modal subformulas by substituting their truth sets.

Let \(D_t\) denote the Dedekind number (the number of antichains of subsets of a labelled \(t\)-set), and put \(T_t=D_t-2\), \(S_t=2^t-1\). At a specified pair \((x,y)\), among the \(T_mT_n\) ordered pairs of permitted local families, the numbers that eliminate \(\Box\) in the horizontal-then-vertical orientation and in *both* orientations are exactly
\[
 E_{m,n}=S_mT_n+(T_m-S_m)S_n,
\]
\[
 J_{m,n}=mD_n+nD_m+2S_mS_n-2m2^n-2n2^m+mn.
\]
For \(m=n=2\), these counts are \(15\) and \(14\) out of \(16\); for \(m=n=3\), they are \(203\) and \(131\) out of \(324\).

For complete labelled factor frames (each world independently receives one permitted local family), the number of ordered pairs of frames for which \(\Box=\Box_1\Box_2\) holds **at every product world** on every valuation is
\[
 G_{m,n}=S_m^mT_n^n+T_m^mS_n^n-S_m^mS_n^n.
\]
Thus \(G_{2,2}=207\) among \(256\) possible frame pairs; the fraction \(G_{m,n}/(T_m^mT_n^n)\) tends to zero as both \(m,n\to\infty\). This distinguishes the typical finite *monotone non-normal* product from the finite normal case, where each neighborhood family is a principal filter and the three boxes collapse as in relational products.

## Assumptions and scope
All sets are finite, nonempty and labelled. Local neighborhood families are nonempty and upward closed, do not contain the empty set, and need not be filters or contain the evaluating world. Consequently they form a legitimate monotone (but possibly non-normal) neighborhood semantics; the theorem does **not** assert that arbitrary choices validate the normal modal axiom \(\mathsf K\) or the reflexivity axiom \(\mathsf T\). For an arbitrary \(P\subseteq X\times Y\), at \((x,y)\), the three operators mean:
\[
\begin{aligned}
\Box P&\iff (\exists U\in\mathcal A_x)(\exists V\in\mathcal B_y)\ U\times V\subseteq P,\\
\Box_1\Box_2P&\iff (\exists U\in\mathcal A_x)(\forall u\in U)(\exists V_u\in\mathcal B_y)\ \{u\}\times V_u\subseteq P,\\
\Box_2\Box_1P&\iff (\exists V\in\mathcal B_y)(\forall v\in V)(\exists U_v\in\mathcal A_x)\ U_v\times\{v\}\subseteq P.
\end{aligned}
\]
The quantified equivalence is at a fixed point for *all* subsets \(P\); global equality quantifies over all points in the product. Local families at other points play no part in the local criterion but are included independently in the global census.

## Proof
**1. Finite generators.** Every nonempty upward-closed family of nonempty subsets of a finite carrier has a nonempty antichain of minimal members, uniquely determining the family. Conversely every nonempty antichain of nonempty subsets specifies such a family. There are \(T_t=D_t-2\) choices on \(t\) points: discard the empty antichain and the antichain consisting only of the empty subset.

**2. Product implies either iteration.** A rectangle \(U\times V\subseteq P\) witnesses both iterated boxes by using the same \(V\) for every \(u\in U\), or the same \(U\) for every \(v\in V\).

**3. The sufficient local conditions.** If every minimal \(U\in\mathcal A_x\) is a singleton, shrink any \(U\) witnessing \(\Box_1\Box_2P\) to such a minimal singleton \(\{u\}\), and use the vertical witness at \(u\). This supplies a rectangle. If \(\mathcal B_y\) has one minimal member \(V_0\), then \(V_0\) lies inside every \(V_u\in\mathcal B_y\); the iterated-box witness \(U\) yields the rectangle \(U\times V_0\). The reverse orientation is symmetric.

**4. Necessity and explicit separating valuation.** Suppose \(\mathcal A_x\) has a minimal neighborhood \(U_0\) containing two distinct points \(u_1,u_2\), and \(\mathcal B_y\) has two distinct minimal neighborhoods \(V_1,V_2\). Define \(P\) to have row \(V_2\) at \(u_2\), row \(V_1\) at all other points of \(U_0\), and empty rows outside \(U_0\). Then \(U_0\) witnesses \(\Box_1\Box_2P\). Any rectangle contained in \(P\) must have its horizontal neighborhood contained in \(U_0\), hence equal \(U_0\) by minimality. Its vertical neighborhood would have to be contained in \(V_1\cap V_2\); this is impossible because neither of the distinct inclusion-minimal neighborhoods \(V_1,V_2\) contains a neighborhood of \(\mathcal B_y\) below their intersection. Thus \(\Box P\) fails. The symmetric construction proves the other necessity.

**5. Exact local counts.** On a \(t\)-point set, there are \(S_t\) antichains consisting entirely of singletons (choose a nonempty set of singletons) and \(S_t\) antichains containing exactly one nonempty set. Their intersection consists of the \(t\) single-singleton antichains. Counting the union of the two alternatives in Step 3 gives \(E_{m,n}\). To satisfy both orientations, split left local families into four disjoint classes: both conditions (\(m\)); singleton-only (\(S_m-m\)); principal-only (\(S_m-m\)); and neither (\(T_m-2S_m+m\)). The allowed right families number, respectively, \(T_n,S_n,S_n,n\), giving
\[
 J_{m,n}=mT_n+2(S_m-m)S_n+(T_m-2S_m+m)n.
\]
Expanding \(S_t=2^t-1\) and \(T_t=D_t-2\) produces the displayed symmetric expression.

**6. Global census and rarity.** The local criterion at all \((x,y)\) says
\[
 (\forall x\in X\;\mathcal A_x\text{ has only singleton minima})\quad\text{or}\quad
 (\forall y\in Y\;\mathcal B_y\text{ has one minimum}).
\]
(The equivalence of \(\forall x\forall y(P_x\lor Q_y)\) with \((\forall xP_x)\lor(\forall yQ_y)\) uses nonempty carriers.) These events have sizes \(S_m^mT_n^n\) and \(T_m^mS_n^n\), with intersection \(S_m^mS_n^n\), establishing \(G_{m,n}\). Since \(D_t\ge2^{\binom{t}{\lfloor t/2\rfloor}}\) by choosing arbitrary subfamilies of the middle layer, \(S_t/T_t\to0\). The global probability equals \((S_m/T_m)^m+(S_n/T_n)^n-(S_m/T_m)^m(S_n/T_n)^n\), and tends to zero as both dimensions grow.

**7. Sharp small reflexive boundary.** If the factor families are additionally point-containing, the orientation \(\Box_1\Box_2p\to\Box p\) can first fail on carriers of sizes \(2\) and \(3\). Choose \(X=\{x,u\}\), \(Y=\{y,v,w\}\); at \(x\) take the principal family generated by \(\{x,u\}\), and at \(y\) take the upward family generated by the incomparable sets \(\{y,v\}\) and \(\{y,w\}\). At all other points choose the principal family generated by the point singleton. Use \(P\) with rows \(P_x=\{y,v\}\), \(P_u=\{y,w\}\). Then \(\Box_1\Box_2p\) holds at \((x,y)\), but \(\Box p\) fails. No smaller pair can fail in this orientation with point-containing neighborhoods: a left carrier of size one forces singleton minima, while a right carrier of at most two forces a unique minimum because all subsets containing the distinguished point form a chain. These frames validate the atomic \(\mathsf T\)-axiom but **not** necessarily \(\mathsf K\), so the example does not contradict finite normal-frame collapse.

## Verification
The independent finite evaluator in `checker.py` enumerates all nonempty antichains of nonempty subsets on carriers of sizes one, two and three. For every local pair and every valuation on its Cartesian product, it compares the three modal conditions with the stated two Boolean criteria, and separately constructs a failing valuation whenever a criterion fails. It checks all local count formulas, all nine small point-containing cases and all four global frame counts for dimensions at most two. The output ends with `ALL_CHECKS_OK`. This exhaustive finite test does not replace the all-finite symbolic argument in Steps 1–7.

## Relationship to prior work
Aghamov et al. introduce precisely the three neighborhood product functions used here and establish one-way interactions, including \(\Box p\to\Box_1\Box_2p\land\Box_2\Box_1p\); they also note that normal relational full products obey stronger equivalences. Their cited paper investigates logical axiomatization of full products of **normal** neighborhood frames, not this exact structural and Dedekind-number census for finite non-normal monotone factors. Sano (2011) directly develops products of monotone neighborhood frames, but employs two coordinate modalities and hybrid naming axioms, rather than a third rectangle modality and its finite elimination census. Kudinov's earlier work studies two-modality products of normal neighborhood frames and uses intersection-closed neighborhood filters. A separately published rectangularization result already characterizes elimination by a general section-to-rectangle condition, and observes that finite normal factors satisfy it. The present statement specializes to finite monotone families but gives a new explicit local *minimal-antichain* dichotomy, two-orientation and global exact counts, and the sharp point-containing failure size. It is not a new claim of the abstract rectangle criterion or of finite-normal collapse.

## Limitations
The family nonemptiness and prohibition of empty neighborhoods are essential: allowing empty neighborhood families or the empty subset changes the conditional equivalences. The result is for monotone upward families, not arbitrary non-upward neighborhood assignments or infinite carriers. The enumerations count labelled neighborhood-function assignments, not isomorphism classes or frame-valid logics. Historical priority under different terms such as monotone neighbourhood bases or rectangularization remains uncertain. One related published record was available only through its indexed title and summary, not its full text, so possible overlap beyond that summary remains a risk. No independent mathematical audit has been performed.

## References
1. Aghamov, Kudinov, Nguyen and Piribauer, *On Modal Logics of Full Products of Neighborhood Frames*, EPTCS **447** (2026), 1–15, doi:10.4204/EPTCS.447.1; public 2026-06-29. Full openly available text: https://www.researchgate.net/publication/408180918_On_Modal_Logics_of_Full_Products_of_Neighborhood_Frames.
2. Sano, *Axiomatizing Hybrid Products of Monotone Neighborhood Frames*, Electronic Notes in Theoretical Computer Science **273** (2011), 51–67, doi:10.1016/j.entcs.2011.06.012; available full text: https://www.researchgate.net/publication/220368399_Axiomatizing_Hybrid_Products_of_Monotone_Neighborhood_Frames.
3. Kudinov, *Neighbourhood frame product KxK* (2014), author text: https://www.researchgate.net/publication/281691170_Neighbourhood_frame_product_KxK.
4. *Rectangularization exactly controls modality elimination in neighborhood full products* (2026), publicly indexed mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-rectangularization-exactly-controls-modality-elimination-in-neig--d3f6516314ba.
5. R. Dedekind, *Über Zerlegungen von Zahlen durch ihre grössten gemeinsamen Teiler* (1897), for the classical antichain-number sequence; only the elementary definition and middle-layer lower bound are used here.
