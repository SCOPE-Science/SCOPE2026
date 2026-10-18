# Sharp one-comparability gap for finite-parameter types of the random poset

## Finding
Let \(\mathcal R\) denote the countable universal homogeneous strict partial order. For a finite induced subposet \(P\subset\mathcal R\), denote by \(t(P)\) the number of complete nonalgebraic \(1\)-types over \(P\) realized in \(\mathcal R\).

**Theorem.** For every integer \(n\ge2\):

1. If \(P\) is the \(n\)-element antichain then \(t(P)=2^{n+1}-1\).
2. If an \(n\)-element poset \(P\) has at least one strict comparable pair, then \(t(P)\le3\cdot2^{n-1}\).
3. The second bound is attained by the disjoint union of one two-element chain with \(n-2\) isolated points; also by a height-two star with one minimum below \(n-1\) mutually incomparable maxima and by its dual.

In particular a single comparability reduces the maximum possible finite-parameter type count by at least \(2^{n-1}-1\) compared with an antichain of the same size. A stronger **doubling lemma** drives the bound: if \(P\) contains a comparable pair and \(P\) is an induced subposet of \(Q=P\cup\{v\}\), then \(t(Q)\le2t(P)\).

## Assumptions and scope
Work in the single strict partial-order language. A one-point extension of \(P\) determines disjoint sets \(D=\{p\in P:p<x\}\) and \(U=\{p\in P:x<p\}\). Such an extension is legal exactly when \(D\) is a lower ideal, \(U\) is an upper filter, and every element of \(D\) is strictly below every element of \(U\). The sets fix all incidences involving the new point. Homogeneity and the one-point extension property of \(\mathcal R\) identify these legal profiles with nonalgebraic complete \(1\)-types over \(P\). Here \(D\) and \(U\) may be empty, and empty-to-empty contributes one type. No restriction to connected posets or to realized types of bounded quantifier depth is made.

## Proof
**Restriction fibers.** Fix an induced extension \(Q=P\cup\{v\}\), and write \(L=\{p\in P:p<v\}\), \(H=\{p\in P:v<p\}\). Restricting a legal profile for an extra point \(x\) over \(Q\) to \(P\) gives a legal profile \((D,U)\) over \(P\). For each such profile, there are at most three possible statuses: \(x<v\), \(v<x\), or \(x\parallel v\). The first status forces \(D\subseteq L\) and \(H\subseteq U\), whereas the second forces \(L\subseteq D\) and \(U\subseteq H\). Therefore both are simultaneously possible only when \((D,U)=(L,H)\). Conversely, at that one profile all three statuses are legal: one may put a second element immediately below \(v\), immediately above \(v\), or incomparable with \(v\) while retaining the same incidences to \(P\). Thus exactly one restriction fiber has cardinality three, and every other fiber has size at most two.

Assume \(P\) has a comparable pair. There exists at least one legal profile whose restriction fiber has cardinality one. If \(v<a\) for some \(a\in P\), take \(x\) above all points of \(P\). Then \(v<x\) is forced. If instead \(a<v\) for some \(a\in P\), take \(x\) below all of \(P\), forcing \(x<v\). In the remaining case \(v\parallel p\) for every \(p\in P\). Choose \(a<b\) in \(P\), and choose the legal profile \(D=\downarrow a\), \(U=\uparrow b\), with downward and upward closures taken inside \(P\). Its realizations satisfy \(a<x<b\); neither strict order between \(v\) and \(x\) is possible, or else \(v\) would be comparable with \(a\) or \(b\). In each case the claimed profile is legal over \(P\), and the remaining prescribed status is consistent with \(Q\). (The unique three-element fiber is a different profile.) Consequently \(t(Q)\le2t(P)+1-1=2t(P)\).

**The gap.** A two-element chain has six legal one-point profiles (the three gap positions and the three profiles with one or both endpoints incomparable as permitted), hence \(t(C_2)=6\). Every non-antichain \(n\)-element poset contains an induced two-element chain. Order its other vertices arbitrarily and adjoin them one at a time as induced extensions. The doubling lemma yields \(t(P)\le6\,2^{n-2}=3\cdot2^{n-1}\).

For the \(n\)-element antichain, the conditions on \(D,U\) forbid only their simultaneous nonemptiness. Thus there are \(2^n\) profiles with \(D=\varnothing\), another \(2^n\) with \(U=\varnothing\), with the empty/empty profile counted twice, giving \(2^{n+1}-1\).

**Sharpness.** For the disjoint union of a two-element chain and \(n-2\) isolated points there are \(J=3\cdot2^{n-2}\) lower ideals and equally many upper filters. Exactly one legal profile has both \(D\) and \(U\) nonempty, namely the bottom of the chain below \(x\) and its top above \(x\). The number of profiles is \(2J-1+1=3\cdot2^{n-1}\).

For a height-two star with bottom point \(c\) and top antichain of size \(n-1\), there are \(J=2^{n-1}+1\) ideals (empty, or \(c\) together with an arbitrary top subset). There are \(2^{n-1}-1\) legal profiles with both sides nonempty, namely \(D=\{c\}\), and \(U\) any nonempty subset of the tops. Hence \(t(P)=2J-1+(2^{n-1}-1)=3\cdot2^{n-1}\). Order duality preserves \(t(P)\). This proves all assertions. \(\square\)

## Verification
Run the bundled standalone `verify.py` using Python 3.10 or later. It independently enumerates all strict partial orders on labeled sets of sizes one through five, computes admissible one-point profiles, checks the bound and equality instances, and independently verifies the profile count via transitive closure through four points. It also checks the unique three-point fiber and existence of a one-point fiber across all 4,200 induced five-point extensions whose first four points have a comparable pair. Both sharpness constructions are checked directly through nine points. These finite tests corroborate the proof but are not used as a proof for arbitrary \(n\).

## Relationship to prior work
The universal homogeneous poset and its extension property are standard; Laflamme, Nguyen Van Thé, and Sauer (2008) study homogeneous structures, including the random poset, rather than the sharp finite-parameter type-count gap derived here. Oliver Pretzel's earlier insertion-poset construction is directly relevant to legal positions of a new point; its available abstract emphasizes dimension rather than the maximal number of positions. A separately published result on counting finite-parameter types in the random poset already establishes the ideal/filter encoding, the antichain value \(2^{n+1}-1\), and a \(\#P\)-completeness theorem; these facts are background here. The new statement is the sharp numerical stability gap and the restriction-fiber doubling inequality, not the representation by ideal/filter pairs or complexity of counting them.

## Limitations
The theorem does not classify every equality case, does not address multiple new points or a fixed quantifier-rank fragment, and does not prove any novelty priority. The full text of Pretzel (1980) was unavailable for inspection, leaving the possibility of an earlier related extremal inequality. General bounds do not assign individual type-count values to arbitrary finite posets; these can be computed using the ideal/filter profile condition.

## References
1. C. Laflamme, L. Nguyen Van Thé, and N. W. Sauer, *Distinguishing Number of Countable Homogeneous Relational Structures*, arXiv:0804.4019v1 (first public 24 April 2008); subsequently *Electronic Journal of Combinatorics* 17 (2010), R20. https://arxiv.org/abs/0804.4019.
2. O. Pretzel, *A construction for partially ordered sets*, *Discrete Mathematics* 32 (1980), 59–68, DOI: 10.1016/0012-365X(80)90100-4. The available abstract concerns the dimension of insertion-position posets; full text was not available for this comparison.
3. *Finite-parameter 1-type counting in the random poset is #P-complete* (2026), published mathematical record `3b955f4020e1`. Its ideal/filter formulation, antichain type count, and complexity result are treated as prior background, not as new contributions here. The full public RESULT.md was inspected.
