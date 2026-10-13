# Singular-height fans admit narrow subsystems but no well-pruned subtree
## Finding
For every singular cardinal \(\kappa\), the fan \(F_\kappa\) of height \(\kappa\) admits a narrow subsystem of width exactly \(\operatorname{cf}(\kappa)\), yet \(F_\kappa\) has no well-pruned subtree of height \(\kappa\). Thus the regularity assumption in Adkisson's recent theorem cannot be removed if "narrow" continues to mean \(\operatorname{width}(S)^+<\kappa\).

## Assumptions and scope
Work in ZFC. Let \(\kappa\) be an arbitrary singular cardinal and put \(\mu=\operatorname{cf}(\kappa)\). Choose a strictly increasing cofinal sequence \(\langle\kappa_i:i<\mu\rangle\) of nonzero ordinals below \(\kappa\).

Use the concrete fan \(F_\kappa\) with a root \(r\) and, for every \(0<\gamma<\kappa\), a branch \(B_\gamma\) containing one node \(b_{\gamma,\alpha}\) at each positive level \(\alpha<\gamma\). Nodes on the same branch are ordered by level, and nodes on distinct branches are incomparable above the root. This is the fan of height \(\kappa\) from Adkisson's Definition 3.1, written with explicit coordinates.

A subsystem is understood in the one-relation sense of Adkisson's Definitions 2.2 and 2.4. Its width is \(\sup_\alpha |S_\alpha|\), and it is narrow when \(\operatorname{width}(S)^+<\kappa\).

## Proof
Let the index set be
\[
I=\{\kappa_j:j<\mu\}.
\]
For \(\alpha=\kappa_j\in I\), define
\[
S_\alpha=\{b_{\kappa_i,\alpha}:j<i<\mu\}.
\]
This is well-defined because \(j<i\) implies \(\kappa_j<\kappa_i\), so the branch \(B_{\kappa_i}\) contains a node at level \(\alpha=\kappa_j\).

The set \(I\) is cofinal in \(\kappa\). Every tail of the infinite regular cardinal \(\mu\) has cardinality \(\mu\), hence
\[
|S_{\kappa_j}|=\mu
\]
for every \(j<\mu\). Therefore \(\operatorname{width}(S)=\mu\).

The subsystem axioms hold. The inherited order respects levels. If \(\kappa_j<\kappa_k\) are in \(I\), choose any \(i>k\). Then
\[
b_{\kappa_i,\kappa_j}<b_{\kappa_i,\kappa_k},
\]
so the required comparable pair exists between the two subsystem levels. If two subsystem nodes lie below a common upper subsystem node, all three lie on the same fan branch, so the two lower nodes are comparable. Thus \(S\) is a subsystem of \(F_\kappa\).

Because \(\kappa\) is singular, \(\mu<\kappa\). Moreover \(\mu^+<\kappa\): equality \(\mu^+=\kappa\) would make \(\kappa\) a successor cardinal, hence regular, contrary to singularity. Consequently
\[
\operatorname{width}(S)^+=\mu^+<\kappa,
\]
so \(S\) is narrow.

Finally, every nonroot node \(b_{\gamma,\alpha}\) has all of its extensions inside the single branch \(B_\gamma\), hence its cone is bounded below level \(\gamma<\kappa\). A well-pruned subtree of height \(\kappa\) would require each of its nodes to extend to every higher level. No positive-level fan node can satisfy that requirement, while a subtree of height \(\kappa\) must contain positive-level nodes. Therefore \(F_\kappa\) has no well-pruned subtree of height \(\kappa\).

## Verification
The proof uses only three checks: tails of \(\operatorname{cf}(\kappa)\) have the same cardinality; a singular \(\kappa\) cannot equal \(\operatorname{cf}(\kappa)^+\); and every positive fan node has a bounded cone. The subsystem coherence condition is automatic from the fact that predecessors of a node in a tree form a chain.

The recent source proves the corresponding implication only for regular \(\kappa\), and its Proposition 3.2 rules out narrow subsystems in the fan only under regularity. The construction above shows that both regularity restrictions are substantive.

## Relationship to prior work
Adkisson proves that, for regular \(\kappa\), any height-\(\kappa\) tree admitting a narrow subsystem contains a well-pruned subtree, and separately proves that a regular-height fan has no narrow subsystem. The present singular-height construction shows that the fan itself is the sharp obstruction to extending those statements verbatim to singular heights.

Lambie-Hanson's work emphasizes the role of narrow systems in tree-property arguments around successors of singular cardinals and uses the standard width condition \(\operatorname{width}(S)^+<\kappa\) in the regular-cardinal setting. The finding here concerns a different issue: the height \(\kappa\) itself is singular, where ordinary narrowness no longer controls the cofinality-sized family of branches needed by the fan.

## Limitations
The result is only about one-cardinal trees at singular height. It does not address two-cardinal trees, does not weaken Adkisson's theorem at regular cardinals, and does not assert that every singular-height failure has width exactly \(\operatorname{cf}(\kappa)\). The construction is elementary enough that an equivalent observation may exist in older literature under different terminology; the checked recent source and closely related narrow-system literature do not state it.

## References
1. William Adkisson, *A Note on Narrow Systems*, arXiv:2610.00934v1, 2026. See Definition 3.1, Proposition 3.2, Definition 3.6, and Theorem 3.13.
2. Chris Lambie-Hanson, *Narrow systems revisited*, Bulletin of the London Mathematical Society 56 (2024), 1967--1987, DOI:10.1112/blms.13037.
