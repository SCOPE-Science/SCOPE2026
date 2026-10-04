# Non-Hausdorff suspension commutes with Stong cores away from the contractible case
## Finding
Let \(X\) be a nonempty finite \(T_0\)-space, viewed as a finite poset, and let \(\mathbb S X=X\oplus S^0\) denote its non-Hausdorff suspension: two new incomparable maximal points \(+\) and \(-\) are placed above every point of \(X\).

Then \(\mathbb S X\) is a minimal finite space if and only if \(X\) is minimal and \(|X|\ge 2\).

More generally, let \(C\) be a Stong core of \(X\). If \(|C|\ge2\), then \(\mathbb S C\) is a Stong core of \(\mathbb S X\). If \(|C|=1\), then \(\mathbb S X\) is contractible and its core is a point. Therefore, for every integer \(k\ge1\),
\[
|\operatorname{core}(\mathbb S^k X)|=
\begin{cases}
1,&\text{if \(X\) is contractible},\\
|C|+2k,&\text{otherwise}.
\end{cases}
\]
Thus every noncontractible strong-homotopy core gains exactly two points per non-Hausdorff suspension, while the contractible case remains contractible.

## Assumptions and scope
All spaces are finite, nonempty, and \(T_0\). The order convention is the specialization order in which continuity is equivalent to order preservation. A point \(x\) is an up beat point when its strict upper set has a least element, and a down beat point when its strict lower set has a greatest element. A minimal finite space has no beat points. A Stong core is a minimal strong deformation retract obtained by deleting beat points.

The statement concerns the non-Hausdorff suspension \(\mathbb S X=X\oplus S^0\), not the ordinary topological suspension as a point-set construction on arbitrary spaces. The core conclusion is a statement about finite-space homotopy type, which is stronger than the weak homotopy equivalence between \(\mathbb S X\) and the ordinary suspension of an associated polyhedron.

## Proof
Write the two new maximal points of \(\mathbb S X\) as \(+\) and \(-\).

First, every beat point of \(X\) remains a beat point of \(\mathbb S X\) with the same witness. If \(x\) is down beat in \(X\), its strict lower set is unchanged by suspension, so the same greatest lower neighbor witnesses that \(x\) is down beat in \(\mathbb S X\). If \(x\) is up beat in \(X\) with least strict upper element \(y\), then \(y<+\) and \(y<-\); hence \(y\) is still below every strict upper element of \(x\) after the two new maxima are added. Thus \(y\) remains the least strict upper element.

Consequently, any beat-point deletion sequence reducing \(X\) to a core \(C\) lifts verbatim inside the suspension and gives a chain of strong deformation retracts
\[
\mathbb S X\searrow\mathbb S C.
\]

Assume now that \(C\) is minimal and \(|C|\ge2\). No old point of \(C\) becomes a beat point in \(\mathbb S C\). Its strict lower set is unchanged, so down-beat status is unchanged. For up-beat status, if an old point has old strict upper elements, then a least strict upper element in \(\mathbb S C\) would have to be an old point and would already be least among the old strict upper elements, contradicting minimality of \(C\). If the old point is maximal in \(C\), then its strict upper set in \(\mathbb S C\) is exactly \(\{+,-\}\), which has no least element because \(+\) and \(-\) are incomparable.

The new point \(+\) has strict lower set \(C\), and similarly for \(-\). Such a new point is down beat exactly when \(C\) has a greatest element. A minimal finite poset with at least two points cannot have a greatest element: if \(g\) were greatest, choose a maximal element \(m\) of \(C\setminus\{g\}\); then \(m\) would be up beat with unique least strict upper element \(g\). Therefore neither \(+\) nor \(-\) is a beat point. They are maximal, so they cannot be up beat. Hence \(\mathbb S C\) is minimal. Since it is also a strong deformation retract of \(\mathbb S X\), it is a core.

If \(|C|=1\), then \(\mathbb S C\) is the three-point poset consisting of one lower point beneath \(+\) and \(-\). Each new maximum is down beat, so this space dismantles to one point. Since \(\mathbb S X\searrow\mathbb S C\), the suspension is contractible. This proves the core dichotomy.

For the minimality criterion, if \(X\) is not minimal then a beat point of \(X\) survives in \(\mathbb S X\), so the suspension is not minimal. If \(X\) is minimal with at least two points, the preceding argument shows \(\mathbb S X\) is minimal. The one-point case is excluded because its suspension has two down beat points.

Finally, iterate the core statement. In the noncontractible case the core has at least two points, so every successive suspension of that core remains minimal and adds exactly two points. In the contractible case the first suspension is contractible, and the same argument repeats. This yields the displayed formula for every \(k\ge1\).

## Verification
The proof above is symbolic and establishes the theorem for every finite nonempty \(T_0\)-space.

The accompanying standard-library program `verify.py` independently enumerates every labeled poset on at most five points. For each of the \(4473\) posets, it checks that every beat-point deletion used by a deterministic core reduction remains a valid deletion after one suspension. It also checks the exact minimality criterion and compares the predicted core cardinality with direct beat reduction after the first three iterated suspensions. The resulting run checks \(14864\) lifted beat deletions and \(17892\) theorem instances and ends with `VERIFY_OK`.

These finite computations are regression checks only; they are not used to infer the all-size statement.

## Relationship to prior work
Barmak and Minian explicitly place Stong's beat-point/core theory and McCord's non-Hausdorff suspension in the same finite-space framework. Their paper defines minimal finite spaces and cores, records that every finite space is homotopy equivalent to its core, and then defines \(\mathbb S X\) by adjoining two points above \(X\). It uses iterated suspensions to construct and characterize minimal finite models of spheres. The inspected full text does not state the general core formula above or the exact criterion that \(\mathbb S X\) is minimal precisely when \(X\) is minimal with at least two points.

Kukieła's work extends Stong-type core theory to broader classes of Alexandroff spaces, but the inspected core section does not treat non-Hausdorff suspension. Stong's original paper is the foundational source for beat points and cores; accessible metadata and later faithful restatements were checked, while the original article was not available in directly inspectable full text from the sources used for this review. That access limitation is retained as a residual originality risk rather than treated as evidence of novelty.

The nearest prior result in the current finite-space record on the same suspension construction counts fixed-point-free endomorphisms of \(X\oplus S^0\). That map-count theorem neither implies nor is implied by the beat-point/core statement here. A separate prior result on Cartesian products gives multiplicativity of core size under products, but ordinal sums with two new maxima are a different construction and require the beat-point analysis above.

## Limitations
The theorem is specific to adjoining a two-point antichain of universal maxima. For a general ordinal sum \(X\oplus Y\), new comparabilities inside \(Y\) can create or destroy beat witnesses in ways not covered by this argument.

The result classifies Stong cores and finite-space homotopy compression, not simple-homotopy reductions by weak points and not weak homotopy minimality among all finite models of a given CW complex. The computational verification is exhaustive only through five points and three suspension iterates; the unrestricted result rests on the symbolic proof.

The literature search was targeted at core, beat-point, minimality, suspension, and Alexandroff-space aliases. The original Stong full text was not available in directly inspectable full text from the sources used for this review, so an older equivalent formulation cannot be ruled out absolutely.

## References
1. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156v1, 6 November 2006; Journal of Homotopy and Related Structures 2(1) (2007), 127–140.
2. R. E. Stong, *Finite topological spaces*, Transactions of the American Mathematical Society 123 (1966), 325–340, DOI:10.1090/S0002-9947-1966-0195042-2.
3. M. C. McCord, *Singular homology groups and homotopy groups of finite topological spaces*, Duke Mathematical Journal 33 (1966), 465–474, DOI:10.1215/S0012-7094-66-03352-7.
4. M. Kukieła, *On homotopy types of Alexandroff spaces*, arXiv:0901.2621.
