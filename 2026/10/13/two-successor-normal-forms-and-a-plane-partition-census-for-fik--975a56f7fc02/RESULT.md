# Two-successor normal forms and a plane-partition census for FIK chain semantics

## Finding

Fix the ordered world set \(C_n=\{0<1<\cdots<n-1\}\), with \(n\ge1\). Consider all binary relations \(R\subseteq C_n\times C_n\) satisfying **forward confluence**
\[
 z\le x\ \land\ zRy\quad\Longrightarrow\quad
 \exists t\,(xRt\ \land\ y\le t).
\]
Interpret intuitionistic propositions as upsets, with the FIK clauses
\[
 \Diamond_R U=\{i:\exists y\in U,\ iRy\},\qquad
 \Box_R U=\{i:\forall j\ge i\ \forall y\,(jRy\Rightarrow y\in U)\}.
\]
Call two such relations *pointwise modally equivalent* when these two operations agree on every upset \(U\) at every world. Equivalently, every FIK formula has the same truth value at each world under every fixed upward-closed atomic valuation.

**Classification.** Every equivalence class has a representative with **at most two outgoing successors per world**. If exactly \(r\) rows are nonempty, they are necessarily the final \(r\) rows. The classes with this value of \(r\) correspond bijectively to pairs of weakly increasing sequences
\[
0\le u_1\le\cdots\le u_r\le n-1,\qquad
0\le m_1\le\cdots\le m_r\le n-1,
\qquad u_i\le m_i\quad(1\le i\le r).
\]
A canonical representative has empty earlier rows and row \(i\) equal to \(\{u_i,m_i\}\) on the nonempty suffix (the set is a singleton when \(u_i=m_i\)).

**Exact census.** The number of pointwise modal-equivalence classes is
\[
\boxed{E_n=1+\sum_{r=1}^{n}
\frac{(n+r-1)!(n+r)!}{(n-1)!\,n!\,r!\,(r+1)!}.}
\]
The summand is the number of plane partitions in a \(2\times r\times(n-1)\) box. The first ten values, beginning at \(n=1\), are
\[
2,\ 10,\ 77,\ 726,\ 7667,\ 87074,\ 1040405,\ 12906910,\ 164817875,\ 2153616444.
\]
Precisely \(\binom{2n}{n}\) classes admit a representative of maximum outdegree at most \(1\); the remaining \(E_n-\binom{2n}{n}\) classes necessarily require outdegree \(2\), so the universal branching bound is sharp for every \(n\ge2\). This is an exact classification of finite-chain *modal operator pairs*, not merely a count of their underlying accessibility relations.

## Assumptions and scope

The intuitionistic preorder is the **fixed, labeled, nonempty total order** \(C_n\). World labels are not factored out, and equivalence is pointwise across corresponding worlds under the same valuations. A relation may be empty, and no reflexivity, seriality, transitivity, or backward confluence requirement is imposed. The two operations are exactly those in Balbiani, Gao, Gencer and Olivetti's FIK semantics [1], not the pair of locally interpreted modalities used for their later LIK system [2]. Every upset is one of \(U_k=\{k,k+1,\ldots,n-1\}\), with \(0\le k\le n\) and \(U_n=\varnothing\).

The result does **not** equate pointwise modal equivalence with agreement merely on the set of globally valid formulas; the latter is a coarser question. The sharp branching claim concerns representatives on the same labeled world set, not arbitrary bisimilar frames of different cardinality.

## Proof

Write \(R_i=\{y:iRy\}\). Forward confluence implies that if \(R_z\ne\varnothing\) and \(z\le i\), then \(R_i\ne\varnothing\), and that the maxima \(m_i=\max R_i\) of consecutive nonempty rows are weakly increasing. Conversely, these two conditions imply forward confluence: for any \(zRy\) and \(z\le i\), use \(t=m_i\ge m_z\ge y\). Thus the nonempty rows are exactly a final interval \(\{n-r,\ldots,n-1\}\), with \(0\le r\le n\).

Assume \(r>0\) and renumber the nonempty suffix rows \(1,\ldots,r\). Define
\[
m_i=\max R_i,\qquad u_i=\min\Bigl(\bigcup_{j=i}^{r}R_j\Bigr).
\]
The maxima \(m_i\) are nondecreasing by confluence, while the suffix minima \(u_i\) are nondecreasing because the unions shrink. Every row is included in its suffix union, so \(u_i\le m_i\). For the upset \(U_k\), the modal clauses reduce to
\[
i\in\Diamond_R U_k\quad\Longleftrightarrow\quad m_i\ge k
\quad\text{on the nonempty suffix},
\]
\[
i\in\Box_R U_k\quad\Longleftrightarrow\quad
 \min\Bigl(\bigcup_{j\ge i}R_j\Bigr)\ge k.
\]
For earlier empty rows \(\Diamond_R U_k\) is false; their box truth depends on the same suffix minimum \(u_1\). If \(R=\varnothing\), \(\Diamond_R U_k\) is everywhere false and \(\Box_R U_k\) everywhere true. Hence the two operators are determined by \(r\), the maxima \(m_i\), and the suffix minima \(u_i\).

Conversely, fix any pair of sequences meeting the displayed inequalities and define rows \(R_i^*=\{u_i,m_i\}\) on the last \(r\) worlds, leaving the others empty. Their maxima are the prescribed \(m_i\), so \(R^*\) is forward confluent. Since \(u_i\) is nondecreasing, the minimum of the union of all rows from \(i\) onward is exactly \(u_i\). Thus \(R^*\) induces the prescribed box and diamond, proving existence and the two-successor upper bound.

The invariants are also **recoverable from the modal operators**. The upset \(U_0=C_n\) makes \(\Diamond_R U_0\) exactly the set of nonempty rows, hence reveals \(r\). On each such row, \(m_i\) is the largest index \(k\) for which \(i\in\Diamond_R U_k\). Meanwhile \(u_i\) is the largest index \(k\) for which \(i\in\Box_R U_k\); the suffix from \(i\) is nonempty, so this threshold lies between \(0\) and \(n-1\). Therefore different invariant tuples induce different modal operator pairs. The induction on formulas now gives pointwise equivalence exactly when the operator pairs agree; any disagreeing operator is witnessed by \(\Box p\) or \(\Diamond p\), assigning \(V(p)=U_k\).

For fixed \(r\), our invariant pairs are two weakly increasing rows with weak column inequality, entries in \(\{0,\ldots,n-1\}\). Reversing both coordinate orders identifies them with plane partitions inside a \(2\times r\times(n-1)\) rectangular box. The classical MacMahon box product [3] becomes
\[
P_{n,r}=\prod_{a=1}^{2}\prod_{b=1}^{r}\frac{n+a+b-2}{a+b-1}
=\frac{(n+r-1)!(n+r)!}{(n-1)!\,n!\,r!\,(r+1)!}.
\]
Adding the unique all-empty relation gives \(E_n=1+\sum_{r=1}^nP_{n,r}\). Equivalently, the same product is the standard hook-content count for semistandard tableaux of shape \((r,r)\) over an alphabet of size \(n+1\), obtained by replacing \((u_i,m_i)\) with strict column entries \((u_i+1,m_i+2)\).

A representative with at most one successor per nonempty row must have \(u_i=m_i\), because its maxima are weakly increasing and therefore each suffix minimum equals that row's unique successor. Conversely, these equalities make the canonical representative partial-functional. For a suffix of length \(r\), there are \(\binom{n+r-1}{r}\) such nondecreasing sequences. Summing \(r=0,\ldots,n\) and applying the hockey-stick identity yields \(\binom{2n}{n}\). Already for \(n=2\), the remaining four classes have \(u_i<m_i\) somewhere and cannot have partial-functional representatives. Therefore two successors are genuinely required in general.

## Verification

Run the standalone standard-library checker `python3 verify.py`. It enumerates **all** \(2^{n^2}\) binary relations for each \(1\le n\le4\), directly tests forward confluence, explicitly evaluates both modal operators on every upset and at every world, recovers the invariants, constructs the two-successor representative, and tests equivalence of all operator tables. The raw forward-confluent relation counts are \(2,11,198,13377\), while the distinct operator-pair counts are exactly \(2,10,77,726\). The test also enumerates all legal sequence pairs for \(n\le6\), confirms MacMahon's product and the partial-functional classification, and checks the latter against \(\binom{2n}{n}\).

The recorded deterministic result is

`VERIFY_OK 378803 exact assertions; exhaustive all 66066 relations through n=4; independent ordered-pair counts through n=6`.

These finite computations independently check the critical reductions and the first cases; the proof establishes the unrestricted statement.

## Relationship to prior work

Balbiani–Gao–Gencer–Olivetti [1] define FIK's forward-confluent semantics and establish its logical proof theory, soundness, completeness, decidability, and finite model property. The forward-confluence condition itself was known earlier as Simpson's (F1). The inspected complete 30-page FIK manuscript does not supply modal-equivalence classes of accessibility relations on a chain, a two-successor canonical form, or an exact count of induced modal operators. Full-text searches find neither “enumerat” nor “normal form” nor “MacMahon”. The later LIK work [2] imposes **both** forward and downward confluence and takes both modalities locally; it concerns a different semantic setting and does not provide the one-sided quotient classified here. The plane-partition formula [3] is classical; novelty is not claimed for that enumerative identity alone, but for its precise interpretation as a complete semantics-preserving quotient of FIK's finite linear frames, together with the sharp two-successor normal form and branching spectrum.

An exact Gaussian-binomial count of **raw** forward-confluent relations follows from row-maxima monotonicity; it counts different objects from these pointwise modal-equivalence classes and does not imply the suffix-minimum invariant, canonical reduction, or plane-partition quotient. Unindexed related finite-frame calculations and general algebraic-duality folklore remain plausible prior-art risks.

## Limitations

This does not classify arbitrary finite preorders, varying underlying world sets, bisimulation equivalence across different frames, or validity-equivalence of entire frames. The result assumes the **global** FIK box forcing clause; substituting local box would change the relevant minima and the count. The search is not a proof of priority. No independent expert mathematical audit has been performed.

## References

[1] P. Balbiani, H. Gao, Ç. Gencer, N. Olivetti, *A Natural Intuitionistic Modal Logic: Axiomatization and Bi-nested Calculus*, arXiv:2309.06309 (first public 2023-09-12), CSL 2024, DOI:10.4230/LIPIcs.CSL.2024.13; https://arxiv.org/abs/2309.06309.

[2] P. Balbiani, H. Gao, Ç. Gencer, N. Olivetti, *Local Intuitionistic Modal Logics and Their Calculi*, arXiv:2403.06772 (first public 2024-03-11); DOI:10.1007/978-3-031-63501-4_5; https://arxiv.org/abs/2403.06772.

[3] C. Krattenthaler, *Plane Partitions in the Work of Richard Stanley and His School*, arXiv:1503.05934, Section on MacMahon's box formula; https://arxiv.org/abs/1503.05934.
