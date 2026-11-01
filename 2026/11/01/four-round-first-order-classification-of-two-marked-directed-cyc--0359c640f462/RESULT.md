# Four-round first-order classification of two-marked directed cycles

## Finding
For positive integers \(a,b\), let \(D_{a,b}\) be the directed cycle of length \(a+b\) with domain \(\mathbb Z/(a+b)\mathbb Z\), successor relation \(S(u,v)\) iff \(v=u+1\pmod{a+b}\), and two **distinct named constants** \(c_0=0\), \(c_1=a\). The signature contains equality, \(S\), and only those two constants; it has no linear order or addition.

The family \(\{D_{a,b}:a,b\ge1\}\) has **exactly 340 first-order quantifier-rank-four equivalence classes**. Each class contains a member on at most **35 vertices**, and 35 is sharp among family members: the class of \(D_{17,18}\) has no representative on fewer than 35 vertices. This is the unique class attaining the bound.

An exhaustive, reproducible exact-type table specifies the complete classification: for each \(1\le a,b\le32\), `class_table.csv` records the equivalence-class index. For arbitrary \(a,b\ge1\), replace them by \(\min(a,32)\) and \(\min(b,32)\), then look up this row. Two structures are four-round equivalent **if and only if** the resulting indices agree. The file `class_representatives.csv` gives an optimal shortest representative for each of the 340 classes.

For comparison, the same method yields exactly 4, 14, 40, and 108 equivalence classes at ranks zero, one, two, and three, with respective sharp family-representative bounds 4, 7, 11, and 19.

## Assumptions and scope
All cycles are finite, coherently oriented, with two distinct individually named vertices. The integers \(a\) and \(b\) are the forward successor distances from \(c_0\) to \(c_1\) and from \(c_1\) back to \(c_0\), respectively. The two constants cannot be interchanged when evaluating a formula. Quantifier rank is maximal nesting depth of first-order quantifiers, with unrestricted numbers of variables and Boolean connectives.

## Proof
**Step 1: complete types.** For an ordered tuple consisting initially of \((c_0,c_1)\) and then the newly selected vertices, record its equality pattern and all successor atoms \(S(x_i,x_j)\). Call this quantifier-free diagram \(\delta(\bar x)\). Recursively define a finite rooted type
\[
T_0(\bar x)=\delta(\bar x),\qquad
T_{r+1}(\bar x)=\left(\delta(\bar x),\{T_r(\bar x,y):y\in D_{a,b}\}\right).
\]
The usual induction on formulas, or equivalently on the Ehrenfeucht–Fraïssé game, shows that two tuples have identical \(T_r\) precisely when every rank-at-most-\(r\) formula with those free coordinates has the same truth value. The type sets—not multiplicities—are essential because one first-order quantifier asks whether a witness of a specified previous type exists.

**Step 2: gap encoding.** List the distinct selected vertices in forward cyclic order, starting at the block containing \(c_0\). Record for each block the indices of tuple coordinates equal to that vertex. Consecutive blocks are separated by positive integer successor gaps summing to the cycle length. This description exactly reconstructs the quantifier-free diagram. Choosing a new vertex either reuses an existing block or splits one gap of length \(g\ge2\) into ordered positive parts \(h,g-h\) for some \(1\le h<g\). These are *all* possible one-point extensions.

**Step 3: finite reduction for arbitrary cycles.** Set \(B_r=2^{r+1}\). If two tuples have the same coordinate-block pattern and corresponding gaps satisfy
\[
\min(g,B_r)=\min(g',B_r),
\]
then they have the same \(T_r\). Induct on \(r\). At \(r=0\), the atomic successor diagram only tests whether each gap is one. For the induction step, matched gaps below \(B_{r+1}=2B_r\) are split at identical positions. If both gaps are at least \(2B_r\), then any split has either a side shorter than \(B_r\) (copy this side exactly and keep the other side at least \(B_r\)) or both sides at least \(B_r\) (respond with a split into two sides at least \(B_r\)). The argument is symmetric between the structures. Repeated-element choices are matched by the identical coordinate-block patterns. Thus all possible successor \(T_r\) sets agree, proving the induction.

For rank four, \(B_4=32\), so every member is equivalent to one of exactly 1024 canonical gap pairs \((a,b)\in\{1,\ldots,32\}^2\). This infinite-to-finite reduction is a proof, not a computational extrapolation.

**Step 4: exhaustive exact finite classification.** `verify_symbolic.py` evaluates exactly the recurrence in Step 1 using the complete extension list from Step 2. It interns full atomic diagrams and the **sets** of recursively computed types, with gap clipping justified independently in Step 3. It calculates all 1024 canonical rank-four types, partitions them into 340 distinct classes, and selects the minimum \(a+b\), breaking ties lexicographically, within each class. Exactly one minimum representative has size 35, namely \((17,18)\); every other minimum has size at most 34. The emitted CSV files carry every comparison and every optimal representative. The same program checks the lower ranks against its recorded expected totals.

Combining the mathematical completeness of the finite reduction with the exhaustive type partition proves the claim.

## Verification
From the directory containing the accompanying artifacts, run `python verify_symbolic.py --write-tables` and `python verify_direct.py`. The first regenerates `class_table.csv` and `class_representatives.csv`, checks the five exact class counts and minimal representative bounds, and prints `EXACT_FINITE_CLASSIFICATION_OK`. The second independently constructs direct vertex-based atomic diagrams and full first-order extension types, without cyclic-gap abstractions, then checks equality of the partitions against the symbolic method at ranks 0–3 through cycles of size 20 and at rank 4 through size 12. It prints `INDEPENDENT_DIRECT_CHECKS_OK`.

The symbolic run checks every canonical pair and therefore the entire infinite family by Step 3. The direct run is a separate finite cross-check, **not** the reason the infinite result holds. Python's standard library suffices; no external theorem prover, random sampling, or inaccessible certificate is needed.

## Relationship to prior work
Brown and Hoshino (2007) give an exact Ehrenfeucht–Fraïssé classification of **unmarked undirected** paths and cycles, and develop gap strategies for their games. Their theorem does not state a two-constant, directed-successor classification or the 340-type partition. Their treatment of cycles and path cuts motivates the present distinguished-gap question. Mwesigye and Truss (2010) give an algorithmic classification framework for **coloured linear orders**, a stronger order signature on a different class of structures. The published directed-path successor-only classification likewise concerns paths **without distinguished constants**. None of these inspected results implies this specific two-marked cyclic type census merely by forgetting symbols or taking a special case: the two named landmarks remain observable, whereas ordinary successor does not define a global linear order at bounded quantifier rank.

## Limitations
No statement is made for higher ranks, any other number of named markers, reversals of the successor orientation, arbitrary directed functional graphs, or languages admitting a global linear order. The count and sharp bound rely on the supplied exact finite calculation, which remains open to independent replication. A related older formula or software census in unindexed literature cannot be excluded; this is a historical-priority limitation, not a claim of established uniqueness. Independent scientific review has not been performed.

## References
1. Jason Brown and Richard Hoshino, “The Ehrenfeucht–Fraïssé Game for Paths and Cycles,” *Ars Combinatoria* **83** (2007), 193–212. Publicly published 2007-04-30. https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf
2. Feresiano Mwesigye and John K. Truss, “Classification of Finite Coloured Linear Orderings,” *Order* **28** (2011), 387–397; first online 2010-09-07. DOI: 10.1007/s11083-010-9178-9.
3. “Exact quantifier-rank threshold for finite directed paths,” public research result (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-quantifier-rank-threshold-for-finite-directed-paths--75a6b05e7112.
