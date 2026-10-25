# A sharp half-world cutoff for iterated \(\Box\Diamond\top\) on finite Kripke frames

## Finding

For every finite, nonempty Kripke frame \((W,R)\) with \(|W|=n\geq1\), define the variable-free formulas \(\alpha_0=\top\) and \(\alpha_{r+1}=\Box\Diamond\alpha_r\) for integers \(r\geq0\). Put \(h=\lfloor n/2\rfloor\). Then, at every world of the frame, \(\alpha_h\leftrightarrow\alpha_{h+1}\) holds, and all subsequent formulas \(\alpha_j\), \(j\ge h\), have identical truth sets.

The cutoff is optimal in the strongest possible finite-model sense: for every integer \(r\geq0\), the least number of worlds in a Kripke frame where \(\alpha_r\leftrightarrow\alpha_{r+1}\) fails is exactly \(2r+2\). In particular, a directed path realizes the maximal possible first stabilization index \(\lfloor n/2\rfloor\) for each \(n\).

## Assumptions and scope

A frame is an arbitrary finite directed relation \(R\subseteq W\times W\), permitting empty successor sets, self-loops, and branching; no valuation restrictions are necessary because the formulas contain no propositional atoms. Modal operators use standard classical Kripke semantics: \(w\models\Box\varphi\) iff every \(R\)-successor satisfies \(\varphi\), and \(w\models\Diamond\varphi\) iff some successor satisfies \(\varphi\). Vacuous necessity holds at terminal worlds.

For a set \(X\subseteq W\) write \(\operatorname{Pre}(X)=\{w:\exists u\in X\ (wRu)\}\) and \(R(w)=\{u:wRu\}\). Let \(S_r=\{w:w\models\alpha_r\}\), \(T_r=W\setminus S_r\), and \(U_r=\{u:R(u)\subseteq T_r\}\). Thus \(T_0=\varnothing\), and the modal truth conditions give
\[
T_{r+1}=\operatorname{Pre}(U_r),\qquad U_r=\{u:R(u)\subseteq T_r\}.
\]
Both \(T_r\) and \(U_r\) increase monotonically with \(r\). The formula \(\Box\Diamond\) is monotone in its argument, so the truth sets \(S_r\) decrease.

## Proof

**Two-sided separation lemma.** For all nonnegative integers \(i,j\), one has \(T_i\cap U_j=\varnothing\). Prove this by induction on \(i+j\). If \(i=0\), then \(T_i\) is empty. Otherwise, suppose \(x\in T_i\cap U_j\). From \(x\in T_i=\operatorname{Pre}(U_{i-1})\) there is a successor \(y\) of \(x\) with \(y\in U_{i-1}\). From \(x\in U_j\), every successor of \(x\) belongs to \(T_j\), so \(y\in T_j\cap U_{i-1}\). The indices of this last intersection sum to \(i+j-1\), contradicting the induction hypothesis. This argument requires no finiteness assumption.

**Sharp lower bound.** Suppose \(\alpha_r\) and \(\alpha_{r+1}\) differ somewhere. Monotonicity implies that \(T_{r+1}\setminus T_r\) is nonempty. Moreover, \(T_1\setminus T_0,\ldots,T_{r+1}\setminus T_r\) are all nonempty: equality of two consecutive \(T\)-sets would be a fixed point of the same deterministic modal operator, preventing any later change. Consequently \(|T_{r+1}|\ge r+1\).

Since \(T_1=\operatorname{Pre}(U_0)\ne\varnothing\), also \(U_0\ne\varnothing\). For each \(j=1,\ldots,r\), equality \(U_j=U_{j-1}\) would imply \(T_{j+1}=\operatorname{Pre}(U_j)=\operatorname{Pre}(U_{j-1})=T_j\), which is impossible. Thus each \(U_j\setminus U_{j-1}\) is nonempty, and \(|U_r|\ge r+1\). The separation lemma makes the sets \(T_{r+1}\) and \(U_r\) disjoint. Therefore
\[
|W|\ge |T_{r+1}|+|U_r|\ge 2r+2.
\]
Taking \(r=\lfloor n/2\rfloor\) rules out any disagreement at that index for an \(n\)-world frame. Once consecutive truth sets agree, all later ones agree.

**Attainment.** For each \(r\ge0\), take the directed path on exactly \(2r+2\) worlds, with edges only from each world to its next world and no edge from the last. For a path world at distance \(d\) edges from the terminal vertex, induction on \(j\) gives
\[
w\not\models\alpha_j\quad\Longleftrightarrow\quad d\in\{1,3,\ldots,2j-1\}.
\]
Indeed a terminal world satisfies every \(\alpha_j\), the penultimate world fails all positive stages, and at every other world the truth of \(\alpha_{j+1}\) equals the truth of \(\alpha_j\) two edges nearer the terminal vertex. At the initial world \(d=2r+1\), so \(\alpha_r\) is true and \(\alpha_{r+1}\) false. For arbitrary \(n\ge2\), the path of length \(n-1\) also contains a world with terminal distance \(2\lfloor n/2\rfloor-1\), witnessing a change at the last possible index. For \(n=1\), the truth sets are stationary already at index zero. This proves all assertions.

## Verification

Run `python3 checker.py` with Python 3 (standard library). This script implements the modal operator directly using successor masks; separately evaluates the original recursive modal semantics on selected cases; checks the two-sided separation invariant; exhaustively tests all \(2^{n^2}\) labelled relations for each \(n=1,2,3,4\); performs 35,000 reproducible sampled tests for 5, 6, and 9 worlds; and verifies path sharpness for all sizes from 1 to 80. The exhaustive stabilization-index histograms are \(\{0:2\}\), \(\{0:12,1:4\}\), \(\{0:374,1:138\}\), and \(\{0:52056,1:12712,2:768\}\) at those four sizes. Its final output is `ALL_CHECKS_OK`.

These computations are independent consistency checks, not a substitute for the all-size set-theoretic proof above. No external solver, computation certificate, or infinite search is necessary for the theorem.

## Relationship to prior work

Alpay and Başaran [1, Section 7] exhibited the path family with \(2r+2\) worlds separating \(\alpha_r\) from \(\alpha_{r+1}\) for all \(r\ge1\), and proved its **minimality only for \(r=1,2,3\)** using exhaustive evaluation and SAT/DRAT certificates. Their stated path lemma explicitly does not give a general lower bound. The current result is the all-index lower bound and sharp global stabilization theorem. The path construction, the individual small-index minimality results, and the existence of a descending sequence of approximants are prior facts, not separately claimed as contributions here.

The ordinary finite fixpoint iteration principle provides an upper bound of \(n\) strict changes for a monotone operator on subsets of an \(n\)-element carrier [2,3]; it does not establish the factor-two improvement or a sharp general finite-model separation spectrum for this specific operator. The critical additional argument is the disjointness of all the finite-stage \(T_i\) and \(U_j\) approximants. Modal \(\mu\)-calculus game semantics is a related language for interpreting such iterations, but the present statement is a finite-frame, variable-free theorem without added fixpoint syntax.

## Limitations

This is a theorem about the exact sequence \(\alpha_r=(\Box\Diamond)^r\top\) on **finite** frames and standard Kripke semantics; no bound of this shape is claimed for arbitrary formulas, unrelated combinations of modalities, or infinite frames. The lower-bound witnesses use terminal worlds. On a serial frame \(\Diamond\top\) holds at every world and every \(\alpha_r\) is valid from the outset, so sharpness does not apply there. The older game-attractor and iteration literature may contain an equivalent formulation of the separation lemma that is not indexed under these modal formulas; priority beyond the inspected material requires independent review.

## References

[1] Faruk Alpay and Barış Başaran, *GPU-Accelerated Search and Certification of Bounded Indistinguishability in Finite Kripke Semantics*, arXiv:2606.15437v1, first public June 13, 2026. In particular Section 7, Proposition 5, Lemma 2, and the SAT/DRAT results for indices 1–3. https://arxiv.org/abs/2606.15437

[2] Florian Bruse, Marco Sälzer, and Martin Lange, *Finite Convergence of μ-Calculus Fixpoints on Genuinely Infinite Structures*, MFCS 2021, DOI:10.4230/LIPIcs.MFCS.2021.24. https://doi.org/10.4230/LIPIcs.MFCS.2021.24

[3] Lauri Hella, Antti Kuusisto, and Raine Rönnholm, *Bounded Game-Theoretic Semantics for Modal μ-Calculus*, arXiv:1706.00753, 2017. https://arxiv.org/abs/1706.00753
