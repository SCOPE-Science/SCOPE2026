# Exact ordinal spectrum for an atom-free two-agent belief update

## Finding

Fix two agents \(a,b\), and use the **same** announcement at every stage:
\[
\chi:=\Diamond_a\top\wedge\Diamond_b\top.
\]
Let \(M^0=M\), let \(M^{\xi+1}\) be the believed-public-announcement update that keeps an existing arrow \(xR_i^\xi y\) precisely when \(M^\xi,y\models\chi\), and at each nonzero limit ordinal take intersections of the preceding arrow relations. Define \(h(M)\) as the least ordinal \(\alpha\) for which \(M^\alpha=M^{\alpha+1}\).

**Theorem (exact closure spectrum).** In ZFC, for every infinite cardinal \(\kappa\),
\[
\{h(M):M\text{ is a two-agent }K45\text{ model with }1\le |W|\le\kappa\}
=\{\alpha:\alpha<\kappa^+\}.
\]
The valuation can be empty, and \(\chi\) contains **no propositional letters** and has modal depth one. In particular, one fixed formula attains every countable ordinal as its exact first stabilization stage on a countable two-agent \(K45\) model, and attains no uncountable ordinal there. For an atom-free formula, modal depth zero or a single \(K45\) agent cannot realize any first stabilization stage greater than one.

## Assumptions and scope

A \(K45\) relation is transitive and Euclidean, with neither seriality nor reflexivity of every world required. A model is \((W,R_a,R_b,V)\), where \(W\ne\varnothing\). The update is *believed* announcement, which preserves worlds and valuations but restricts arrow **targets**:
\[
R_i^{\xi+1}=\{(x,y)\in R_i^\xi:M^\xi,y\models\chi\},\qquad
R_i^\lambda=\bigcap_{\xi<\lambda}R_i^\xi\quad(\lambda\text{ limit}).
\]
All ordinal and cardinal arguments assume ZFC. The claim concerns the first equality of successive whole models, not the first change in truth of \(\chi\) at a distinguished world. In this construction, no atomic valuation affects the update.

## Proof

**1. Universal cardinal bound.** An update never adds arrows. Once \(M^\xi=M^{\xi+1}\), deterministic iteration leaves it unchanged at every later successor and limit. Thus if \(h(M)=\alpha\), every stage \(\xi<\alpha\) removes at least one arrow from the disjoint union of the two current relations. Distinct strict stages remove disjoint nonempty sets of original labelled arrows. Well-order the original arrow set and choose its least newly removed arrow at each \(\xi\); this gives an injection from \(\alpha\) into that set. For infinite \(|W|\le\kappa\), it has size at most \(2|W|^2\le\kappa\). Hence \(\alpha<\kappa^+\). This also proves the existence of a first fixed stage. Transitivity and Euclideanness are preserved by this target-filtering update and by intersections.

**2. Construct any prescribed rank.** Fix any ordinal \(\alpha\). Let \(T_\alpha\) be the set of finite strictly decreasing sequences of ordinals below \(\alpha\), including the empty sequence \(\varepsilon\). Give \(\varepsilon\) rank \(\rho(\varepsilon)=\alpha\); give each nonempty sequence rank equal to its last entry. For \(\sigma\in T_\alpha\), let
\[
C_\sigma=\{\sigma^\frown\beta:\beta<\rho(\sigma)\},\qquad
B_\sigma=(\{\sigma\}\cup C_\sigma)\times C_\sigma.
\]
Put \(B_\sigma\) into \(R_a\) if \(\sigma\) has even sequence length, and into \(R_b\) if its length is odd. Do not introduce any other arrows. For each fixed agent, the source sets \(\{\sigma\}\cup C_\sigma\) used by these blocks are pairwise disjoint: every nonroot node has a unique parent, and adjacent levels use opposite agents. A block \(X\times Y\), where \(Y\subseteq X\), is transitive and Euclidean. Consequently both relations are \(K45\), and each block consists of one complete successor set shared by its sources.

For an ordinal \(\xi\), define \(C_\sigma^\xi=\{\sigma^\frown\beta:\xi\le\beta<\rho(\sigma)\}\). We prove by transfinite induction, simultaneously for every \(\sigma\), that the contribution of its block to the relations at stage \(\xi\le\alpha\) is **exactly**
\[
B_\sigma^\xi=(\{\sigma\}\cup C_\sigma)\times C_\sigma^\xi.\tag{1}
\]
At stage zero this is the definition. Assume (1) at stage \(\xi\), and let \(y=\sigma^\frown\beta\) be an arrow target of rank \(\beta\). The agent opposite to the one governing \(\sigma\)'s block is the agent governing \(y\)'s own child block. Its successor set at \(y\) is \(C_y^\xi\), which is nonempty **if and only if** \(\xi<\beta\). Meanwhile, if \(y\) remains a target of its parent block (so \(\beta\ge\xi\)), the parent-agent successor set at \(y\) contains \(y\) itself. Therefore, for every current arrow target \(y\),
\[
M^\xi,y\models\Diamond_a\top\wedge\Diamond_b\top
\quad\Longleftrightarrow\quad \xi<\rho(y).\tag{2}
\]
Equations (1) and (2) show that the successor update deletes precisely targets with \(\rho(y)=\xi\), obtaining \(C_\sigma^{\xi+1}\). At a limit \(\lambda\), intersection of the sets \(C_\sigma^\xi\) for \(\xi<\lambda\) gives \(C_\sigma^\lambda\) by ordinal order, proving (1) at all stages.

For each \(\xi<\alpha\), the root block still contains the arrow to its child \(\langle\xi\rangle\), which equation (2) deletes at the next stage; thus \(M^\xi\ne M^{\xi+1}\). At stage \(\alpha\), every \(C_\sigma^\alpha\) is empty because \(\rho(\sigma)\le\alpha\), so the relations are empty and the model is fixed. Hence \(h(M)=\alpha\) exactly. For \(\alpha=0\) this is the one-world edgeless model.

If \(\kappa\) is infinite and \(\alpha<\kappa^+\), the tree \(T_\alpha\) has at most \(\max(\aleph_0,|\alpha|)\le\kappa\) nodes. Combining this construction with part 1 proves the theorem.

**3. Minimality of the stated expressive resources.** With no modalities, an atom-free Boolean formula is globally either true or false. Its target-filtering update is therefore either the identity or complete arrow deletion, giving \(h\le1\). With one \(K45\) relation, any two arrow targets have pointed-generated successor structures bisimilar to a reflexive complete cluster when no atoms are named. Thus every atom-free modal formula has the same truth value at all arrow targets. Again the first update is either the identity or removes every arrow, so \(h\le1\). The two-agent depth-one witness is consequently minimal in agent count and modal depth among atom-free formulas capable of arbitrary finite or infinite closure stages.

## Verification

The standalone \(\texttt{verify.py}\) builds the blocks, evaluates \(\chi\) from both accessibility relations independently, checks transitivity and Euclideanness, and compares each finite update with (1). It passed all ranks \(\alpha=0,1,\dots,8\), ranging from one through 256 states, with each run stabilizing at the asserted exact rank. This is a finite sanity check only: the proof for limit and arbitrary ordinals is the transfinite induction above, not an extrapolation from the program.

## Relationship to prior work

Yamada (2026), Definitions 5 and 8, supplies the believed-public-announcement semantics; Proposition 3 gives the general cardinal termination argument. Lemma 6 proves finite convergence of a generated component for one-agent \(K45\) and a fixed finite propositional vocabulary. Lemma 7 exhibits an \(\omega\)-rank, two-agent peeling frame with a parity atom and a more deeply nested announcement designed for eventual self-refutation. The block geometry here is adapted from that example, not claimed as newly invented. The present result differs in its **one fixed atom-free depth-one formula**, full spectrum of first fixed stages, cardinal-sharp realization, and matching expressivity obstruction. The source does not state the resulting exact ordinal spectrum. The finite-state target-count refinement in prior research concerns finite models and does not supply this transfinite realization.

Generic results about iterated public announcements, deflationary fixed points, or iterated elimination do not alone imply a realization by this fixed syntactically restricted formula on \(K45\) models. Terminological equivalences elsewhere remain a residual literature risk.

## Limitations

This theorem uses nonserial \(K45\), not \(KD45\) or \(S5\); arbitrary cardinals are treated in ZFC. The updates preserve worlds but can destroy all belief arrows. The finite verifier is not a certificate of arbitrary ordinal behavior. The theorem concerns equality of model relations, not epistemic truth oscillations or decidability of general formulas. An independently conducted scientific audit has not been performed.

## References

1. E. Yamada, *Eventual and Strong Eventual Notions in Public Announcements*, arXiv:2609.24006v1, submitted September 21, 2026; especially Definitions 5 and 8, Proposition 3, and Lemmas 6–7. https://arxiv.org/abs/2609.24006
2. A. Klein and R. Rendsvig, *Convergence, Continuity and Recurrence in Dynamic Epistemic Logic*, arXiv:1709.00359 (2017). https://arxiv.org/abs/1709.00359
