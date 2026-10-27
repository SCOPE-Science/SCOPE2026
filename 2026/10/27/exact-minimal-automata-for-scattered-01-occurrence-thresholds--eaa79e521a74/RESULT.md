# Exact minimal automata for scattered-\(01\) occurrence thresholds

## Finding
For every integer \(k\ge1\), let \(N_{01}(w)\) denote the number of pairs of indices \(i<j\) with \(w_i=0\) and \(w_j=1\) in a finite binary word \(w\). Let
\[
\mathcal L_k=\{w\in\{0,1\}^{*}:N_{01}(w)\ge k\}.
\]
The minimal **complete deterministic finite automaton** (DFA) recognizing \(\mathcal L_k\) has exactly
\[
\boxed{\operatorname{sc}(\mathcal L_k)=\left\lfloor\frac{k^2}{4}\right\rfloor+3}
\]
states. This includes all boundary cases, including \(k=1\) and the empty input.

More precisely, the complete Myhill–Nerode classification consists of one initial residual, one residual accepting exactly the continuations that contain at least one \(1\), one accepting sink, and \(\min(d,k-d)\) nonaccepting residuals for each \(d\in\{1,\ldots,k-1\}\). The residual at level \(d\) is indexed by \(z\in\{1,\ldots,k-d\}\), where all \(z\ge d\) merge and every \(z<d\) remains distinguishable.

## Assumptions and scope
Inputs are finite (possibly empty) words over the *ordered, named* binary alphabet \(\{0,1\}\). The count \(N_{01}\) is by **scattered**, not necessarily adjacent, occurrences and counts distinct index pairs, not distinct subsequence strings. \(k\) is an arbitrary positive integer. DFA means deterministic, complete on both letters, with its number of reachable states minimized under language equivalence. Complementing the accepted language leaves the same state count, but this statement itself concerns the inclusive threshold \(\ge k\).

For a prefix \(u\), write \(z(u)=|u|_0\) and \(p(u)=N_{01}(u)\). For a suffix \(v\), write \(t(v)=|v|_1\) and \(h(v)=N_{01}(v)\). Define the residual \(R_u=\{v:uv\in\mathcal L_k\}\).

## Proof
**1. Concatenation formula.** Partition a scattered \(01\) pair in \(uv\) according as both indices lie in \(u\), both in \(v\), or the zero lies in \(u\) and the one in \(v\). This gives, for *all* finite \(u,v\),
\[
N_{01}(uv)=p(u)+z(u)t(v)+h(v).\tag{1}
\]
Therefore the right residual is determined by the two prefix statistics \((z,p)\).

**2. Three exceptional classes.** If \(p\ge k\), (1) shows that every suffix is accepted: this is the accepting sink. If \(z=0\), then \(p=0\), and \(R_u\) is the initial residual \(\{v:h(v)\ge k\}\). If \(p<k\), \(z\ge1\), and \(p+z\ge k\), no suffix consisting only of zeros is accepted, while *any* suffix with at least one one contributes at least \(z\) cross-pairs and is accepted. Thus these prefixes share the residual \(R_u=\{v:t(v)\ge1\}\). Call it the one-one residual.

**3. All remaining classes.** Suppose \(p<k\), \(z\ge1\), and \(p+z<k\). Put \(d=k-p-z\). Then \(d\ge1\), and by (1),
\[
 v\in R_u\quad\Longleftrightarrow\quad h(v)+z(t(v)-1)\ge d.\tag{2}
\]
Because \(p\ge0\), we have \(z+d\le k\). Since \(z\ge1\), this places \(d\in\{1,\ldots,k-1\}\) and \(1\le z\le k-d\). Conversely, every such \((d,z)\) is realized by the explicit prefix \(u=0\,1^{k-d-z}0^{z-1}\): its statistics are \(z\) and \(p=k-d-z\).

If \(z\ge d\), then (2) fails on suffixes with no ones, holds on all suffixes with at least two ones, and for a suffix with exactly one one holds precisely when at least \(d\) zeros precede that one. Hence in this region the residual is **independent of \(z\)** and depends only on \(d\). For \(z<d\), retain the label \((d,z)\).

**4. Pairwise inequivalence.** Different levels \(d<d'\) are distinguished by suffix \(v=0^d1\). Indeed, for every residual in step 3 its acceptance condition with exactly one one is \(h(v)=d\ge d_{\mathrm{level}}\), independently of \(z\). The same suffix distinguishes every level from the initial residual, which requires \(k\) such pairs. Within one level \(d\), take \(z_1<z_2\) with \(z_1<d\). If \(z_2<d\), suffix \(v=1\,0^{d-z_2}1\) contributes two ones and exactly \(d-z_2\) internal \(01\) pairs, so (2) holds for \(z_2\) but fails for \(z_1\). If \(z_2\ge d\), suffix \(v=11\) distinguishes them in the same way. A level-\(d\) residual rejects the suffix \(1\), whereas the one-one residual accepts it. The accepting sink alone accepts the empty suffix. Finally the initial residual differs from the one-one residual on suffix \(1\), and from all level residuals as above. Thus there are no further identifications.

**5. Reachability and count.** The initial residual is realized by \(\varepsilon\), the one-one residual by \(0^k\), and the accepting sink by \(0^k1\). Every level label is reached by the explicit prefix in step 3. For a fixed \(d\), there are \(\min(d-1,k-d)\) distinct labels with \(z<d\) and, if \(k-d\ge d\), one common label for all \(z\ge d\). Their total is \(\min(d,k-d)\). Thus Myhill–Nerode gives
\[
\operatorname{sc}(\mathcal L_k)=3+\sum_{d=1}^{k-1}\min(d,k-d)
=3+\left\lfloor\frac{k^2}{4}\right\rfloor.
\]
This is an exact infinite-family result; no experimental extrapolation is used in the proof.

## Verification
The accompanying standalone `verify.py` computes the ordinary capped-prefix-counter DFA with states \((z,p)\), independently minimizes it by transition-partition refinement, and checks the closed formula for all thresholds \(1\le k\le40\). It additionally checks every prefix up to length nine against every suffix up to length six for the first twelve thresholds, comparing direct index-pair counting with (1). The observed output is:

`VERIFY_OK minimized_thresholds=40 bounded_automaton_states=22220 direct_prefix_suffix_tests=1559052`

These are finite independent checks of implementation and boundary cases, not a replacement for the Myhill–Nerode proof. Run with a standard Python 3 interpreter as `python verify.py`.

## Relationship to prior work
Mansour, Rastegar and Roitershtein [2, Section 2.2, especially Lemma 2.1 and Definition 2.2] construct finite equivalence-class automata for prescribed bounded counts of scattered order patterns. Their notion distinguishes more detailed occurrence data and underlies general regularity and enumeration results. The present theorem isolates the much coarser **single inclusive threshold** for the fixed binary \(01\) pattern, identifies its *minimal* right-residual quotient, and obtains the explicit quadratic formula with all equivalence classes and separating suffixes. It does not claim to originate pattern-count automata or regularity.

The Parikh matrix entry that counts scattered \(01\) pairs appears in the general combinatorics framework of [1]. The generalized Parikh-matrix treatment [3] considers subsequence-count transforms and identities, not the minimal threshold DFA. These comparisons concern the respective mathematically inspected statements, not a proof of uniqueness of the result across all literature.

## Limitations
This theorem concerns a *single* scattered pattern of length two over the binary alphabet; it neither identifies state complexities for other patterns nor analyzes simultaneous or modular thresholds. It supplies no general lower bounds on time or memory of computational algorithms outside the minimal-DFA model. The exact formula might be implicit in a more general minimization construction or occur as an unindexed specialization elsewhere; that bibliographic risk has not been eliminated. Formal third-party proof review has not been conducted.

## References
1. A. Atanasiu, G. Poovanandran and W. C. Teh, *Parikh Matrices for Powers of Words*, arXiv:1808.04102 (first posted 2018-08-13). https://arxiv.org/abs/1808.04102
2. T. Mansour, R. Rastegar and A. Roitershtein, *Finite Automata, Probabilistic Method, and Occurrence Enumeration of a Pattern in Words and Permutations*, arXiv:1905.05646 (first posted 2019-05-14), Section 2.2. https://arxiv.org/abs/1905.05646
3. S. Z. Fazekas and X. Huang, *Generalized Parikh Matrices For Tracking Subsequence Occurrences*, arXiv:2407.04462 (first posted 2024-07-05). https://arxiv.org/abs/2407.04462
