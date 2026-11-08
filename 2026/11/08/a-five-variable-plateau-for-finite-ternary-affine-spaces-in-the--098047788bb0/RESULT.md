# A five-variable plateau for finite ternary affine spaces in the parallelogram language

## Finding
Let \(d\ge0\), and let \(\mathcal T_d\) have universe \(\mathbb F_3^d\), equality, and exactly one four-place relation
\[
P(a,b,c,e)\quad\Longleftrightarrow\quad a-b+c-e=0.
\]
For \(k\in\{1,2,3,4,5\}\), set \((\tau_1,\tau_2,\tau_3,\tau_4,\tau_5)=(0,1,2,3,3)\). Then, for all \(d,e\ge0\),
\[
\mathcal T_d\equiv_{\mathrm{FO}^k}\mathcal T_e
\quad\Longleftrightarrow\quad
\min(d,\tau_k)=\min(e,\tau_k).
\]
Here \(\mathrm{FO}^k\) means counting-free first-order logic with at most \(k\) reusable variable names and arbitrary quantifier depth. In particular, the numbers of theories at widths one through five are respectively \(1,2,3,4,4\), and the \(27\)-point and \(81\)-point ternary affine spaces have the same five-variable theory. The five-variable and four-variable equivalence partitions coincide **within this family**, not necessarily on all finite structures.

## Assumptions and scope
All dimensions are finite nonnegative integers; the dimension-zero space has one point. The field is precisely \(\mathbb F_3\). There is no named origin, vector addition operation, counting quantifier, or extra predicate. Equality is logical equality. All formulas below are in the pure \(\{P\}\) signature. The result makes no claim about widths at least six.

## Proof
**Affine circuits and atomic visibility.** For an ordered tuple \(\mathbf a=(a_1,\ldots,a_t)\), an affine dependence is a coefficient vector \((\lambda_1,\ldots,\lambda_t)\in\mathbb F_3^t\) with \(\sum_i\lambda_i=0\) and \(\sum_i\lambda_i a_i=0\). All nonzero coefficients lie in \(\{1,-1\}\). A minimal dependence on two positions means equality. A minimal dependence on three pairwise distinct positions means collinearity and, in characteristic three, is expressible as \(P(x,y,z,y)\), equivalent to \(x+y+z=0\) after choosing any affine origin. A minimal dependence on four pairwise distinct positions, none of whose triples is collinear, necessarily has two coefficients \(+1\) and two coefficients \(-1\); the relation is therefore one of the three pairings
\[
P(x,y,z,w),\qquad P(x,z,y,w),\qquad P(x,y,w,z).
\]
Thus an atomic \(P\)-and-equality diagram on at most four pebbled positions determines every affine dependence of those positions, and conversely each atomic instance is an affine dependence involving no more than four positions.

**Distinguishing sentences.** One variable sees only valid instances \(x=x\) and \(P(x,x,x,x)\), so every nonempty \(\mathcal T_d\) has the same one-variable theory. Two variables distinguish dimension zero from positive dimension with \(\exists x\exists y\,(x\ne y)\). Three variables distinguish dimension at most one from dimension at least two with
\[
\exists x\exists y\exists z\,(x\ne y\land y\ne z\land x\ne z\land\neg P(x,y,z,y)).
\]
Four variables distinguish dimension at most two from dimension at least three with the sentence asserting existence of four pairwise distinct elements \(x,y,z,w\), no three of which satisfy \(P(u,v,t,v)\), and the negations of the three displayed four-place pairings. By the complete circuit classification above, these four elements are affinely independent exactly when the formula holds. These distinguishing formulas prove every required inequality below the threshold \(\tau_k\), also for larger variable budgets.

**Permanent pebble strategies for widths two through four.** Suppose both dimensions are at least \(k-1\) for \(k\in\{2,3,4\}\). Duplicator maintains a partial affine isomorphism between the affine spans of the currently pebbled points, preserving each pebbled position. After one pebble is lifted, at most \(k-1\) points survive and their affine rank is at most \(k-2\). If the newly chosen point lies in their affine span, reply by its affine image. Otherwise, choose any point outside the image span and extend the affine isomorphism. Such a point always exists because the target dimension is at least \(k-1\). The maintained affine map preserves every atomic predicate and equality; the strategy is valid for arbitrarily many rounds.

**The exceptional five-variable strategy.** Suppose both dimensions are at least three. Duplicator maintains, on the currently placed at most five pebbles, precisely the same affine dependencies whose supports contain at most four pebbled positions. Equivalently, every equality and every \(P\)-atomic instance agrees. After one pebble moves, at most four survivor positions remain. Their complete affine dependence relations agree, because each uses at most four positions; hence the two survivor tuples induce a well-defined affine isomorphism between their spans.

If the survivors have affine rank at most two, Duplicator maps any new point within the survivor span to its affine image and responds to an outsider by any target point outside the target span; both dimensions are at least three. Every dependence involving the new point and at most three survivor positions is preserved.

If the survivors have affine rank three, they are four affinely independent points \(a_1,a_2,a_3,a_4\). A new point belonging to the affine span of some at-most-three of these points is mapped under the survivor-span isomorphism. Otherwise, no dependence involving the new point and at most three survivors exists. The target response may then be the affine sum \(a'_1+a'_2+a'_3+a'_4\). Its barycentric coefficients are all nonzero and sum to \(4=1\) in \(\mathbb F_3\), so it lies in none of the affine spans of at most three survivor points. Consequently every affine dependence involving at most four current pebbles is preserved. This includes the case in which Spoiler's selected point lies outside the full survivor span: a possible five-point dependence is invisible in this signature and variable budget. The invariant is restored after every round; therefore any two dimensions at least three are \(\mathrm{FO}^5\)-equivalent, even with unlimited quantifier depth.

Combining the lower distinguishing sentences and the upper permanent strategies yields the stated classification and counts. The plateau at widths four and five follows immediately.

## Verification
Run the accompanying Python programs `verify_direct.py` and `verify_orbit.py` with Python 3, using only the standard library. `verify_direct.py` exhaustively evaluates the three-variable and four-variable distinguishing witnesses for dimensions zero through three. `verify_orbit.py` enumerates affine-dependence kernels of tuples and performs bisimulation refinement for widths two through five and dimensions zero through five. The latter explicitly checks the predicted dimension partitions. Their recorded stdout appears in `direct_output.txt` and `orbit_output.txt`. These finite tests corroborate but do **not** establish the theorem's unrestricted quantifier-depth conclusion; the permanent strategies above do that.

## Relationship to prior work
Grohe and Otto, *Pebble Games and Linear Equations* (first public arXiv posting April 9, 2012), develop the finite-variable pebble-game method and its linear-equation connections but do not give this four-place ternary affine-space classification. Dawar and Holm, *Pebble Games with Algebraic Rules* (2012), develop more powerful algebraic games but do not assert the present specific dimension plateau. Kuusisto, Meyers and Virtema, *Undecidable First-Order Theories of Affine Geometries* (first public August 24, 2012), treat logics of geometric betweenness over subsets of real affine space, not the present finite-field parallelogram signature. The new theorem should not be conflated with results about unpointed Boolean affine spaces: characteristic three gives a different circuit pattern and different four-to-five-variable behavior. A stronger unlocated general theorem on bounded-variable logic of finite affine torsors remains a legitimate priority risk.

## Limitations
No assertion is made for \(k\ge6\), positive-characteristic fields other than three, arbitrary affine matroids, enriched languages, counting logic, or the full first-order theories. A published priority exhaustive search and independent proof audit have not been completed. Programs check finite orbit cases; no finite enumeration alone certifies infinite-round equivalence.

## References
1. Martin Grohe and Martin Otto, *Pebble Games and Linear Equations*, arXiv:1204.1990, first submitted April 9, 2012. https://arxiv.org/abs/1204.1990
2. Anuj Dawar and Bjarki Holm, *Pebble Games with Algebraic Rules*, ICALP 2012, DOI:10.1007/978-3-642-31585-5_25. https://doi.org/10.1007/978-3-642-31585-5_25
3. Antti Kuusisto, Jeremy Meyers and Jonni Virtema, *Undecidable First-Order Theories of Affine Geometries*, arXiv:1208.4930, first submitted August 24, 2012. https://arxiv.org/abs/1208.4930
