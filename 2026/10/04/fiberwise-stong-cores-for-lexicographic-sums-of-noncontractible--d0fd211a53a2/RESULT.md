# Fiberwise Stong cores for lexicographic sums of noncontractible finite spaces
## Finding
Let \(S\) be a finite poset. For every \(s\in S\), let \(X_s\) be a nonempty noncontractible finite \(T_0\)-space, viewed as a finite poset, and choose a Stong core \(C_s\subseteq X_s\) obtained by successive beat-point deletions. Form the lexicographic sum
\[
L=\bigoplus_{s\in S}X_s,
\]
whose points are pairs \((s,x)\), with \((s,x)\le (t,y)\) exactly when either \(s<t\) in \(S\), or \(s=t\) and \(x\le y\) in \(X_s\).

Then every beat-point deletion used inside a fiber \(X_s\) remains a valid beat-point deletion in the current lexicographic sum. Performing all of the chosen fiber reductions therefore gives a strong deformation retract
\[
L\searrow \bigoplus_{s\in S}C_s.
\]
The terminal lexicographic sum has no beat points. Consequently it is a Stong core of \(L\), and
\[
\left|\operatorname{core}(L)\right|=\sum_{s\in S}\left|\operatorname{core}(X_s)\right|.
\]

The noncontractibility hypothesis cannot simply be omitted. If \(S\) is a two-point chain, the lower fiber is a singleton, and the upper fiber is a two-point antichain, then the lexicographic sum is the three-point space with one minimum below two incomparable maxima; its core is a singleton, whereas the sum of the two fiber-core cardinalities is \(3\).
## Assumptions and scope
All spaces are finite \(T_0\)-spaces and are identified with their specialization posets. A point is an up beat point when its strict upper set has a minimum, and a down beat point when its strict lower set has a maximum. A Stong core is a beat-point-free strong deformation retract obtained by successive beat-point deletions.

The theorem assumes every fiber \(X_s\) is noncontractible. Equivalently, every core \(C_s\) has at least two points. No assumption is made that \(S\) is a chain, graded, connected, or bipartite, and the fibers may be disconnected.
## Proof
First observe that beat points internal to one fiber remain beat points after substitution into the lexicographic sum. Suppose \(x\in X_s\) is an up beat point in \(X_s\) with witness \(y\in X_s\). Thus \(y>x\) and every \(z>x\) in \(X_s\) satisfies \(y\le z\). In the lexicographic sum, an element strictly above \((s,x)\) is either \((s,z)\) with \(z>x\) in \(X_s\), or is contained in a fiber indexed by some \(t>s\). In the first case \((s,y)\le(s,z)\); in the second case \((s,y)<(t,z)\) by the definition of lexicographic sum. Hence \((s,y)\) is still the minimum of the strict upper set of \((s,x)\). The down-beat case is dual. The same argument remains valid after arbitrary deletions in other fibers, because every surviving fiber is nonempty.

It follows that the chosen beat-point deletion sequence reducing each \(X_s\) to \(C_s\) can be replayed fiber by fiber in \(L\). Since deletion of a beat point is a strong deformation retract, the resulting space
\[
C=\bigoplus_{s\in S}C_s
\]
is a strong deformation retract of \(L\).

It remains to prove that \(C\) is minimal. We use the elementary fact that a minimal finite \(T_0\)-space with at least two points has neither a global minimum nor a global maximum. Indeed, if such a space had a minimum \(m\), choose an element minimal among the remaining points. Its strict lower set would be exactly \(\{m\}\), making it a down beat point. The maximum case is dual.

Fix \((s,x)\in C\). Suppose first that \(x\) has an element strictly above it inside \(C_s\). If \((s,x)\) had an up-beat witness in \(C\), that witness could not lie in a higher fiber: every internal point above \(x\) lies below every point of every higher comparable fiber. Thus an up-beat witness would lie in \(C_s\) and would be the minimum of the strict upper set of \(x\) in \(C_s\), contradicting minimality of \(C_s\).

Suppose instead that \(x\) is maximal in \(C_s\). Then the strict upper set of \((s,x)\) consists only of points in fibers \(C_t\) with \(t>s\). If that set had a minimum \((t,z)\), then every point of the same fiber \(C_t\) would also lie above \((s,x)\), so \(z\) would have to be a global minimum of \(C_t\). This is impossible because \(C_t\) is minimal and has at least two points. Therefore \((s,x)\) is not an up beat point. The dual argument rules out down beat points.

Thus \(C\) has no beat points. Since it is already a strong deformation retract of \(L\), it is a Stong core. Its cardinality is the disjoint-fiber sum of the core cardinalities, proving the formula.
## Verification
The symbolic proof is the primary verification. The accompanying `verify.py` independently implements finite posets, beat-point detection, Stong reduction, and lexicographic sums. It tests four index-poset shapes and all assignments of four noncontractible fiber types, including a fiber with a genuine beat point. Across \(352\) lexicographic sums it replays \(320\) fiberwise beat deletions inside the global sum, checks that the terminal space equals the lexicographic sum of the independently computed fiber cores, and verifies that the terminal space has no beat points. It also verifies the three-point boundary example where a contractible fiber makes the additive formula fail.

Running

`python verify.py`

returns `VERIFY_OK` together with the case counts recorded in `verification_output.txt`.
## Relationship to prior work
Barmak and Minian recall Stong's beat-point criterion, the existence and uniqueness up to homeomorphism of cores, and the characterization of finite-space homotopy equivalence by cores. Their paper does not use lexicographic sums or state a fiberwise core theorem of the form above.

Ladkani gives the standard lexicographic-sum construction for finite posets and studies derived equivalences, including reversal of bipartite indexing posets and ordinal sums. The inspected lexicographic-sum section does not discuss beat points, Stong cores, strong deformation retracts, or an additive core-cardinality formula.

An earlier result on non-Hausdorff suspension treats one special binary ordinal-sum instance when the second fiber is a two-point antichain. That special case does not imply the theorem for an arbitrary index poset and arbitrary noncontractible fibers; the present statement supplies the general substitution mechanism and its exact boundary hypothesis.
## Limitations
The theorem does not classify what happens when one or more fibers are contractible. In that regime, a core fiber may be a singleton, which can create new cross-fiber beat points and cause further collapse after all internal reductions. The explicit three-point example shows that no unconditional additive formula survives.

The literature search did not identify an earlier statement of this exact Stong-core rule, but absence from the searched sources is not a proof of historical novelty. Terminology such as poset substitution, composition, or lexicographic sum may conceal equivalent statements outside the inspected literature.
## References
1. S. Ladkani, *On Derived Equivalences of Categories of Sheaves Over Finite Posets*, arXiv:math/0610685v1, first submitted 2006-10-23. See Section 4.4, especially Definition 4.10, for lexicographic sums.
2. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156v1, first submitted 2006-11-06. See the preliminaries recalling Stong beat points and cores.
