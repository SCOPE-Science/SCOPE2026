# Marked one-point type spectra and sharp symmetry-breaking dichotomies for random-poset reducts
## Finding
Let \(\mathbb P\) be the countable homogeneous random partial order and let \(A\subset\mathbb P\) be a nonempty, individually named finite parameter set of size \(n\). The five closed reduct groups are, in order, \(G_{\mathrm{aut}}\), \(G_{\mathrm{rev}}\), \(G_{\mathrm{turn}}\), \(G_{\mathrm{mix}}\), and \(G_{\mathrm{sym}}\): the automorphism group, its join with global order reversal, its join with finite poset rotations, the join of all three, and the full symmetric group. Let \(t_G(A)\) denote the number of orbits of the pointwise stabilizer \(G_{(A)}\) on points outside \(A\), equivalently complete nonalgebraic one-types over the individually named base in the corresponding reduct.

Define \(t(A)\) as the number of pairs \((L,U)\) such that \(L\) is a downset of \(A\), \(U\) is an upset, \(L\cap U=\varnothing\), and every point of \(L\) is strictly below every point of \(U\). Empty sets are allowed. Call a nonempty subset \(M\subseteq A\) *two-level complete* if its induced order is a linear sum of at most two antichains (either level may be empty), and put
\[
\rho(A)=\bigl|\{\varnothing\ne M\subseteq A:\ A|_M\text{ is two-level complete}\}\bigr|.
\]
Write \(W(A)\) for the assertion that \(A\) itself is two-level complete. Then the exact marked-base spectrum is
\[
\boxed{\begin{aligned}
t_{G_{\mathrm{aut}}}(A)&=t(A),\\
t_{G_{\mathrm{rev}}}(A)&=\begin{cases}2^n,& A\text{ antichain},\\t(A),&\text{otherwise},\end{cases}\\
t_{G_{\mathrm{turn}}}(A)&=\rho(A),\\
t_{G_{\mathrm{mix}}}(A)&=\begin{cases}2^{n-1},&W(A),\\\rho(A),&\text{otherwise},\end{cases}\\
t_{G_{\mathrm{sym}}}(A)&=1.
\end{aligned}}
\]
Moreover
\[
\boxed{\binom{n+1}{2}\le\rho(A)\le2^n-1.}
\]
Equality on the left holds exactly for posets that are disjoint unions of at most two chains. Equality on the right holds exactly when \(W(A)\) holds. Thus the mixed and turning groups have identical relative one-type counts *precisely outside* the rotation class of an antichain, while reversal does not reduce the automorphism count as soon as the base contains a comparable pair.

The five counts are pairwise distinct if and only if \(A\) is an antichain and \(n\ge2\). In that case the spectrum is
\[
\boxed{(2^{n+1}-1,\ 2^n,\ 2^n-1,\ 2^{n-1},\ 1)}.
\]
Consequently two individually named incomparable parameters, and no singleton parameter set, distinguish all five reduct groups numerically through their nonalgebraic one-types.

## Assumptions and scope
All groups act on the same underlying set of the random partial order. We use the finite-rotation characterization and extension-to-global-rotation theorem of Pach, Pinsker, Pongrácz, and Szabó, and the five-group classification of Pach, Pinsker, Pluhár, Pongrácz, and Szabó. All parameter points are named *individually*; setwise stabilizers have different spectra. The theorem concerns nonalgebraic one-point orbits only, not general tuple types. For the empty parameter base all five counts are \(1\); the displayed mixed formula is explicitly restricted to \(n\ge1\).

A finite poset is two-level complete precisely when every induced three-element suborder belongs to the orientation-invariant rotation class \(O_1\), comprising a three-point antichain and the two orientations of a fork. The two other labeled rotation classes \(O_2,O_3\) are interchanged by duality. These are *labeled* three-point classes, not merely isomorphism types.

## Proof
**Step 1 (the automorphism and reversal terms).** Homogeneity of \(\mathbb P\) identifies an unmarked new point over \(A\) with its strict lower set \(L\) and strict upper set \(U\) in \(A\). Transitivity of the extended partial order is equivalent to the downset/upset, disjointness, and strict separation conditions in the definition of \(t(A)\). Every admissible pair is realized by the Fraïssé extension property. A global antiautomorphism can fix the named base pointwise only if all named points are mutually incomparable. If a comparable pair exists, the reversing coset contributes nothing to the pointwise stabilizer. For an antichain, the extension types consist of \(B_S\) (new point below precisely the nonempty set \(S\)), \(H_S\) (above precisely \(S\)), and \(I\) (incomparable with every base point). There are \(2^{n+1}-1\) types; reversal exchanges \(B_S\) and \(H_S\) and fixes \(I\), yielding \(2^n\) types.

**Step 2 (canonical maximum and turning types).** Given any finite one-point extension \(Q=A\cup\{x\}\), finite-rotation theory supplies a rotation of \(Q\) whose unique maximal point is \(x\). In a finite poset, this makes \(x\) the greatest element. The rotated restriction to \(A\) is a labeled finite rotation \(A'\) of \(A\). The canonical rotation with unique maximum \(x\) is unique inside the labeled rotation-equivalence class of \(Q\): finite rotations preserving the maximal set preserve the entire labeled order. Therefore the map \([Q]\mapsto A'\) is well-defined and injective on turning orbits of one-point extensions over the fixed base.

Conversely let \(A'\) be any labeled rotation of \(A\). Adjoin a greatest point \(x\) to \(A'\). Choose a finite rotation carrying \(A'\) back to \(A\), described by a lower part \(D\) and upper part \(C\). Extend the same rotation to \(A'\cup\{x\}\) by placing \(x\) into the upper part (since \(D<x\)); its restriction to the base is the selected rotation. Thus the rotated extension restricts to the original order on \(A\). Every finite rotation extends, on the embedded configuration, to an element of the global turning group, so the correspondence is surjective. Consequently the number of turning types is *exactly the number of labeled rotations of the parameter order*.

**Step 3 (maximal-set census).** Finite rotation theory proves that a labeled rotated order is uniquely determined by its set \(M\) of maximal elements. It also proves that such maximal sets are exactly the nonempty unions \(S\cup T\) of two antichains with \(S<T\), where a single empty level is allowed. Equivalently, \(A|_M\) is two-level complete. Therefore the rotation count is \(\rho(A)\), establishing the turning formula for every finite base.

**Step 4 (mixed-group stabilizer dichotomy).** The mixed group is the union of the turning group and its coset represented by order reversal. A coset element can fix \(A\) pointwise exactly when the labeled dual \(A^{\mathrm{op}}\) is rotation-equivalent to \(A\). Rotation equivalence is tested by the labeled triple classes \(O_1,O_2,O_3\); duality preserves \(O_1\) but exchanges \(O_2\) and \(O_3\). Thus the reversing coset occurs in the stabilizer exactly when all triples of \(A\) are in \(O_1\), equivalently \(W(A)\). When \(W(A)\) fails, the mixed and turning pointwise stabilizers have identical orbits.

When \(W(A)\) holds, a finite rotation sends the labeled base to an antichain; conjugation preserves its pointed orbit counts. Over an antichain, a turning rotation identifies \(B_S\) with \(H_{A\setminus S}\) for every nonempty proper \(S\), and merges \(B_A,H_A,I\) in one central class. These are all identifications: the labeled cyclic three-point signatures distinguish the proper \(S\)'s. Order reversal further identifies the class indexed by \(S\) with the class indexed by \(A\setminus S\); the central class stays fixed. There are therefore \(1+(2^n-2)/2=2^{n-1}\) mixed types. This also proves the antichain five-term formula.

**Step 5 (sharp extrema and separation).** Every singleton and every two-point subset of \(A\) is two-level complete, giving \(\rho(A)\ge n+\binom n2=\binom{n+1}{2}\). Equality holds exactly when no three-point subset lies in \(O_1\). Absence of a three-point antichain gives width at most two; absence of forks makes undirected comparability transitive, hence its connected components are chains. There are at most two such components. Conversely, a disjoint union of at most two chains has no three-point \(O_1\) configuration, and attains equality. The trivial bound \(\rho(A)\le2^n-1\) is attained precisely when every nonempty subset qualifies, equivalently when \(A\) itself is two-level complete. Finally, equality of automorphism and reversal counts for every non-antichain base prevents five-way separation. For antichains of size at least two, the displayed five powers are strictly descending, while for a singleton the last three counts coincide. This proves the if-and-only-if criterion.

## Verification
The accompanying standard-library checker independently enumerates all labeled posets on one through five elements, all admissible one-point extensions, and their labeled three-point rotation signatures. It compares those signature counts against the nonempty two-level-complete-subset formula, recomputes reversal and mixed symmetry quotients, and checks both sharp equality classifications. It separately checks the antichain fibers for parameter sizes one through ten. The recorded output is `ALL_CHECKS_PASS`; the general theorem relies on the preceding unrestricted proof, not finite enumeration.

## Relationship to prior work
Pach, Pinsker, Pluhár, Pongrácz, and Szabó establish the five reduct groups and their relational descriptions (arXiv:1111.7109). Pach, Pinsker, Pongrácz, and Szabó establish finite rotations, maximal-set uniqueness, the triple-class criterion, extension to the generic poset, and homogeneity of the ternary rotating reduct (arXiv:1208.3504). These are essential structural inputs, not newly claimed results. The previously published published-finding corpus finding “Exact ordered-tuple orbit profiles of the five random-poset reduct groups” proves the *unbased* injective-arity formulas involving labeled-poset counts; it already uses the canonical-maximum method. Here the different object is the *pointwise named-base orbit fiber*: it varies with the full parameter order and has the new weak-order-versus-generic dichotomy for the mixed stabilizer, an exact maximal-subset count for the turning stabilizer, and a sharp classification of when five scalar one-type counts separate all groups. The unrestricted unbased formulas do not specify these conditional fibers.

## Limitations
The result does not establish a faster algorithm for arbitrary-base automorphism type counting. The calculation uses the published classification and rotation theorems; a very concise implicit derivation from those sources is a residual originality risk, particularly for the turning-group formula. All claims are subject to independent scientific validation, which has not been carried out. The finite checker is not an exhaustive proof over all finite parameter sizes.

## References
1. P. P. Pach, M. Pinsker, G. Pluhár, A. Pongrácz, and C. Szabó, “Reducts of the random partial order,” first arXiv version 2011-11-30, arXiv:1111.7109; DOI:10.1016/j.aim.2014.08.008.
2. P. P. Pach, M. Pinsker, A. Pongrácz, and C. Szabó, “A new operation on partially ordered sets,” first arXiv version 2012-08-16, arXiv:1208.3504; DOI:10.1016/j.jcta.2013.04.003.
3. “Exact ordered-tuple orbit profiles of the five random-poset reduct groups,” published published-finding corpus mathematical record dated 2026-09-30, identifier `2026/9/30/SCOPE-exact-ordered-tuple-orbit-profiles-of-the-five-random-poset-redu--635ca0d5aff9`.
