# Four-modal observational fibers on finite intuitionistic chains

## Finding

Fix the linearly ordered intuitionistic frame carrier \(C_n=\{0<\cdots<n-1\}\), with \(n\geq1\), and allow an **arbitrary** binary modal relation \(R\subseteq C_n^2\). Interpret the four unary operators \(\lozenge\), \(\blacklozenge\), \(\square\), and \(\blacksquare\) exactly as in Balbiani and Gencer [1], on the lattice of upward-closed sets. Two relations are *observationally equivalent* when, for every persistent valuation, every formula of this four-modal intuitionistic propositional language has the same truth set at the same worlds on the two relations.

For each row \(R(i)\), set
\[
 m_i=\begin{cases}\min R(i)&R(i)\ne\varnothing,\\ n&R(i)=\varnothing,\end{cases}
 \quad
 M_i=\begin{cases}\max R(i)&R(i)\ne\varnothing,\\ -1&R(i)=\varnothing.\end{cases}
\]
Define four records, for \(0\leq i<n\):
\[
 A_i=\max_{t\leq i}M_t,\qquad B_i=\min_{t\geq i}M_t,
 \qquad H_i=\max_{t\leq i}m_t,\qquad K_i=\min_{t\geq i}m_t.
\]

**Complete observable invariant.** Two modal relations are observationally equivalent **if and only if** their four record sequences \((A,B,H,K)\) agree. This criterion applies without confluence, seriality, transitivity, or any other restriction on \(R\).

**Exact fiber formula.** Given four proposed integer sequences \(S=(A,B,H,K)\) of length \(n\), use boundary values \(A_{-1}=H_{-1}=-1\) and \(B_n=K_n=n\). For each \(i\), let \(E_i(S)\) consist of row endpoint pairs \((m,M)\) drawn from
\[
 \{(n,-1)\}\cup\{(m,M):0\leq m\leq M<n\}
\]
that satisfy all four equations
\[
 \max(A_{i-1},M)=A_i,\quad\min(M,B_{i+1})=B_i,
\]
\[
 \max(H_{i-1},m)=H_i,\quad\min(m,K_{i+1})=K_i.
\]
Assign weight \(w(n,-1)=1\), and \(w(m,M)=2^{\max(M-m-1,0)}\) for a nonempty row. The **exact number of binary relations realizing \(S\)** is
\[
 \boxed{F_n(S)=\prod_{i=0}^{n-1}\left(\sum_{(m,M)\in E_i(S)}w(m,M)\right).}
\]
In particular, the formula is an exact realizability criterion: \(S\) occurs if and only if \(F_n(S)>0\). It counts raw labelled relations rather than isomorphism types.

**Sharp identifiability boundary and large fibers.** The complete four-modal observational map is injective on binary relations for \(n=1,2\) and not injective for every \(n\geq3\). For every \(n\geq3\), one observable four-modal structure has at least
\[
 \boxed{2^{n(n-2)}}
\]
pairwise distinct realizing relations. Exhaustively, the numbers of observational equivalence classes on carriers of sizes \(1,2,3,4\) are respectively \(2,16,279,7171\); the largest fiber sizes are respectively \(1,1,8,324\).

## Assumptions and scope

The underlying order is the **fixed labelled chain** \(C_n\), and propositional valuations are arbitrary upsets. The relation \(R\) is not required to preserve the order: the four given semantic clauses automatically yield upsets for all formulas. Equality is on the same ordered carrier and under identical atomic valuations; it is stronger than agreement merely on global validities. All four connectives are taken together, not identified with four different accessibility relations. The enumeration is complete only for the stated finite carrier sizes, while the invariant and fiber formula are proved for every \(n\geq1\).

## Proof

Every upward-closed subset is a unique suffix \(U_j=\{j,j+1,\ldots,n-1\}\), with \(0\leq j\leq n\); in particular \(U_n=\varnothing\). A row meets \(U_j\) precisely if \(M_t\geq j\). A row is contained in \(U_j\) precisely if \(m_t\geq j\). These assertions include empty rows because of the sentinel values \(M_t=-1\) and \(m_t=n\).

The four semantic clauses of [1, Section 3.4] therefore give, for any \(i,j\),
\[
 i\in\lozenge U_j\iff \exists t\leq i\ (M_t\geq j)
 \iff A_i\geq j,
\]
\[
 i\in\blacklozenge U_j\iff \forall t\geq i\ (M_t\geq j)
 \iff B_i\geq j,
\]
\[
 i\in\blacksquare U_j\iff \exists t\leq i\ (m_t\geq j)
 \iff H_i\geq j,
\]
\[
 i\in\square U_j\iff \forall t\geq i\ (m_t\geq j)
 \iff K_i\geq j.
\]
Each record entry is recoverable from the threshold at which the corresponding truth table changes, including the two sentinel cases. Thus equality of all four unary operations on upsets is equivalent to equality of \(S\). The intuitionistic and co-intuitionistic operations on upsets are determined by the fixed order; induction on formulas proves that equal four-modal operations yield equal truth sets for every common valuation. Conversely, equality for all formulas includes each one-variable modal formula with the atom assigned each \(U_j\), recovering the four operations and \(S\). This proves the invariant theorem.

For a prescribed signature, the recurrences \(A_i=\max(A_{i-1},M_i)\) and \(B_i=\min(M_i,B_{i+1})\) are necessary and sufficient for its two records of row maxima, given the two boundary values. The analogous recurrences for \(H,K\) characterize the two records of row minima. Hence any independent choice of one admissible endpoint pair from each \(E_i(S)\) realizes precisely those four record sequences; conversely every realization makes such choices. When \(m=M\), its row is the singleton \(\{m\}\); when \(m<M\), it must contain its endpoints and may choose each of its \(M-m-1\) internal positions independently. The empty pair gives the unique empty row. Therefore the number of rows for the pair is \(w(m,M)\), and multiplying the independent row counts proves the fiber product formula and realizability test.

If \(n\leq2\), a nonempty subset of \(C_n\) is uniquely determined by its minimum and maximum. Moreover, the first row's maximum is \(A_0\), the last row's maximum is \(B_{n-1}\), the first row's minimum is \(H_0\), and the last row's minimum is \(K_{n-1}\). When \(n\leq2\), these observations determine all rows, so the map is injective.

For \(n\geq3\), insist that every row contain both extreme worlds \(0\) and \(n-1\). Then every row has \(m_i=0\) and \(M_i=n-1\), hence the same four record profiles and operators. The \(n-2\) interior membership bits of each of the \(n\) rows can nevertheless be chosen independently, giving \(2^{n(n-2)}\) distinct relations in one fiber. This proves both sharp noninjectivity and the quantitative lower bound.

The finite counts and maximal fiber sizes for \(n\leq4\) follow from the separate exhaustive enumerations described next; they are finite exact results, not evidence for an unstated all-size maximal-fiber formula.

## Verification

Run `python checker.py` with Python 3. The program enumerates **every** binary relation on each fixed chain of sizes \(1\leq n\leq4\), totaling \(2,16,512,65536\) relations in the four respective tests. It independently (i) evaluates all four published modal clauses literally at every world and every upward-closed one-variable valuation, (ii) constructs the four endpoint record sequences, and (iii) checks that the two induced partitions are identical. Separately, for every recorded signature it recomputes the claimed fiber cardinality by enumerating the row choices satisfying the four recurrence equations. It confirms the class counts \(2,16,279,7171\) and the maximal fiber sizes \(1,1,8,324\), with `ALL_CHECKS_OK` as final output.

For general \(n\), exhaustive enumeration is not claimed. The infinite-family statements are proved algebraically above; the code is a finite independent check of those steps.

## Relationship to prior work

Balbiani and Gencer [1] establish the precise semantics of these four modalities, investigate elimination and frame correspondence, and prove decidability over arbitrary frames. Their sections on confluence concern when different connectives coincide, not whether different raw relations induce identical **full four-modal** operations. The present theorem addresses this latter representational inverse problem.

Přenosil [2] develops compatibility and canonical relational representation for distributive modal algebras, including the distinction between raw and minimally generated accessibility relations. That general theory motivates taking representation nonuniqueness seriously, but does not give the four-record invariant or the exact labeled fibers of the specific four operators studied here.

The previously published finite-chain KI endpoint census [3] restricts to relations satisfying simultaneous forward and downward confluence and counts those *relations*. It neither characterizes observational equivalence for **arbitrary** relations nor computes fiber sizes or the number of distinct induced four-modal operator structures. The separate condensation theorem [4] is a compatibility theorem for two right-sided relation-closure maps, not an identifiability or enumeration theorem for the four truth operations in [1].

## Limitations

The result uses finite **total** order and cannot be transferred to branching preorders by assigning a single minimum and maximum to each row. Equality under all formulas is assessed under a common valuation; no claim is made about frame bisimulation or any alternative notion of structural equivalence. The class census and largest-fiber values beyond four worlds remain uncomputed; the displayed exponential lower bound is not asserted to be the all-size optimum. Formula-by-formula observational equivalence need not mean the two relations are identical or isomorphic. Priority under older relation-reconstruction or distributive-modal terminology remains an open historical risk.

## References

[1] Philippe Balbiani and Çiğdem Gencer, *Four intuitionistic modal connectives*, arXiv:2606.07348, first posted June 5, 2026, especially Sections 3.4, 4, and 5. https://arxiv.org/html/2606.07348

[2] Adam Přenosil, *Compatibility between modal operators in distributive modal logic*, arXiv:2311.10017, first posted November 16, 2023, especially Sections 1–3. https://arxiv.org/abs/2311.10017

[3] *Endpoint normal form and exact census for finite-chain KI frames*, public research record `2026/10/4/SCOPE-endpoint-normal-form-and-exact-census-for-finite-chain-ki-frames--df6301f11b97`, published in the published-finding corpus mathematical research repository. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-endpoint-normal-form-and-exact-census-for-finite-chain-ki-frames--df6301f11b97

[4] *Finite criterion for commuting box and diamond condensations*, public research record `2026/10/4/SCOPE-finite-criterion-for-commuting-box-and-diamond-condensations--c53088b3c02d`, published in the published-finding corpus mathematical research repository. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-finite-criterion-for-commuting-box-and-diamond-condensations--c53088b3c02d
