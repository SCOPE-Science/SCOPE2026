# Automatic continuity for bounded Borel rotation-invariant conic valuations

## Result

Let \(n\ge 2\), and let \(\mathcal P_n\) denote the space of polyhedral closed convex cones in \(\mathbb R^n\), equipped with the Borel structure inherited from the standard spherical Hausdorff topology on closed convex cones. Let
\[
\nu:\mathcal P_n\to\mathbb R
\]
be a valuation that is \(\mathrm{SO}(n)\)-invariant, Borel measurable, and bounded:
\[
\|\nu\|_\infty:=\sup_{C\in\mathcal P_n}|\nu(C)|<\infty.
\]

Then there are unique coefficients \(c_0,\ldots,c_n\in\mathbb R\) such that
\[
\boxed{\nu(C)=\sum_{j=0}^n c_j\,v_j(C)\qquad(C\in\mathcal P_n),}
\]
where \(v_0,\ldots,v_n\) are the conic intrinsic volumes. If \(L_j\subset\mathbb R^n\) is any \(j\)-dimensional linear subspace, then
\[
\boxed{c_j=\nu(L_j).}
\]

Consequently, every bounded Borel rotation-invariant valuation on polyhedral cones extends uniquely to a continuous \(\mathrm O(n)\)-invariant valuation on the space of all closed convex cones. In particular, bounded Borel regularity already forces continuity.

Moreover,
\[
\boxed{\|\nu\|_\infty=\max_{0\le j\le n}|\nu(L_j)|.}
\]
Thus the Banach space of bounded Borel \(\mathrm{SO}(n)\)-invariant real valuations on \(\mathcal P_n\), with the supremum norm, is isometrically isomorphic to \(\ell_\infty^{\,n+1}\) by evaluation on one subspace in each dimension.

## Context

Lotz recently gave a new proof of the spherical Hadwiger theorem: every continuous rotation-invariant valuation on all closed convex cones is a linear combination of the conic intrinsic volumes. Two ingredients of that proof are stronger than the final continuous statement:

1. on polyhedral cones, rotation invariance already implies reflection invariance without a continuity hypothesis; and
2. the final vanishing theorem for a residual valuation only requires an \(L^1\) orthoscheme restriction, provided the residual valuation vanishes on lower-dimensional cones and on cones containing a line.

The point here is that bounded Borel regularity can be propagated through dimensions so that these hypotheses hold automatically. This produces a global automatic-continuity theorem on the polyhedral domain.

The result is complementary to two other recent regularity theorems. Knoerr proved that measurable translation- and rotation-invariant valuations on Euclidean polytopes are intrinsic-volume combinations, while his spherical-polytope classification is stated under continuity. Lotz also classified monotone invariant conic valuations without assuming continuity or measurability; monotonicity is a substantially different hypothesis from bounded Borel regularity.

## Proof

We first prove the following \(\mathrm O(m)\)-invariant statement by induction on \(m\):

> Every bounded Borel \(\mathrm O(m)\)-invariant valuation on \(\mathcal P_m\) is a linear combination of \(v_0,\ldots,v_m\).

### Base dimension

For \(m=1\), the four polyhedral cones are
\[
\{0\},\qquad \mathbb R_+,\qquad \mathbb R_-,\qquad \mathbb R.
\]
Reflection invariance gives \(\nu(\mathbb R_+)=\nu(\mathbb R_-)\), and the valuation identity for
\[
\mathbb R_+\cup\mathbb R_-=\mathbb R,\qquad
\mathbb R_+\cap\mathbb R_-=\{0\}
\]
gives
\[
2\nu(\mathbb R_+)=\nu(\{0\})+\nu(\mathbb R).
\]
Since
\[
(v_0,v_1)(\{0\})=(1,0),\quad
(v_0,v_1)(\mathbb R_+)=(1/2,1/2),\quad
(v_0,v_1)(\mathbb R)=(0,1),
\]
the claim follows.

### Removing the subspace values

Assume the claim in all dimensions below \(m\), and let \(\nu\) be bounded, Borel, and \(\mathrm O(m)\)-invariant. For \(0\le j\le m\), choose a \(j\)-dimensional subspace \(L_j\) and put
\[
c_j=\nu(L_j),\qquad
\rho=\nu-\sum_{j=0}^m c_jv_j.
\]
Then
\[
\rho(L_j)=0\qquad(0\le j\le m).
\]

Let \(V\subsetneq\mathbb R^m\) be a \(k\)-dimensional subspace. Restriction gives a bounded Borel \(\mathrm O(k)\)-invariant valuation on \(\mathcal P(V)\): every orthogonal transformation of \(V\) extends to one of \(\mathbb R^m\), and the inclusion \(\mathcal P(V)\hookrightarrow\mathcal P_m\) is continuous. By induction,
\[
\nu|_{\mathcal P(V)}
=\sum_{j=0}^k \nu(L_j)\,v_j.
\]
Conic intrinsic volumes are intrinsic under isometric inclusion of a cone into a larger Euclidean space, so
\[
\boxed{\rho(C)=0\quad\text{for every lower-dimensional polyhedral cone }C.}
\]

### Cones containing a line

Fix a line \(\ell\subset\mathbb R^m\). For a polyhedral cone \(D\subset\ell^\perp\), define
\[
\eta_\ell(D)=\rho(\ell\oplus D).
\]
The map \(D\mapsto\ell\oplus D\) is continuous in the spherical Hausdorff topology, hence \(\eta_\ell\) is bounded and Borel. It is also an \(\mathrm O(m-1)\)-invariant valuation.

By the induction hypothesis,
\[
\eta_\ell(D)=\sum_{j=0}^{m-1}d_jv_j(D).
\]
Evaluating on a \(j\)-dimensional subspace \(E_j\subset\ell^\perp\) gives
\[
d_j=\eta_\ell(E_j)=\rho(\ell\oplus E_j)=0.
\]
For \(j<m-1\), the last cone is a proper subspace and was already covered above; for \(j=m-1\), it is \(\mathbb R^m\), on which \(\rho\) is zero by construction. Hence \(\eta_\ell\equiv0\).

Every convex cone containing the line \(\ell\) splits as
\[
C=\ell\oplus(C\cap\ell^\perp),
\]
because the entire lineality direction can be subtracted from each point of \(C\). Therefore
\[
\boxed{\rho(C)=0\quad\text{for every polyhedral cone containing a line}.}
\]

Thus \(\rho\) satisfies the algebraic vanishing condition in Lotz's orthoscheme theorem: it vanishes on all lower-dimensional cones and on all cones containing a line.

### The orthoscheme restriction is automatically \(L^1\)

Let
\[
a\longmapsto C(a)
\]
be the standard orthoscheme parametrization on the positive chamber used in the signed orthoscheme decomposition. This map is continuous. Hence
\[
\psi(a):=\rho(C(a))
\]
is Borel measurable. Since \(\rho\) is globally bounded on polyhedral cones, \(\psi\) is bounded as well. The parameter chamber has finite spherical measure, so
\[
\psi\in L^1.
\]

Lotz's vanishing theorem for polyhedral cones now applies and gives
\[
\rho\equiv0.
\]
This completes the \(\mathrm O(m)\)-invariant induction.

### From rotations to all orthogonal transformations

For \(n\ge2\), Lotz's polyhedral rotation-invariance lemma shows that every \(\mathrm{SO}(n)\)-invariant valuation on polyhedral cones is already \(\mathrm O(n)\)-invariant, without a regularity hypothesis. In dimension two the same fact is also immediate directly, since a pointed cone is determined up to rotation by its opening angle.

Applying the induction above proves
\[
\nu=\sum_{j=0}^n \nu(L_j)v_j.
\]

### Continuous extension and exact norm

Each \(v_j\) extends continuously from polyhedral cones to all closed convex cones. Therefore
\[
\bar\nu(C):=\sum_{j=0}^n c_jv_j(C)
\]
is a continuous extension of \(\nu\). It is unique because polyhedral cones are dense in the closed-cone space.

Finally, conic intrinsic volumes satisfy
\[
v_j(C)\ge0,\qquad \sum_{j=0}^n v_j(C)=1.
\]
Thus
\[
|\nu(C)|\le\max_j|c_j|
\]
for every polyhedral cone \(C\), while equality of suprema follows because \(c_j=\nu(L_j)\). Hence
\[
\|\nu\|_\infty=\max_j|c_j|.
\]

## Why the boundedness and measurability assumptions enter

The proof uses the two assumptions only at the last regularity step: Borel measurability makes the orthoscheme pullback measurable, and boundedness makes it integrable on the finite-measure parameter chamber. The lower-dimensional and lineality reductions are purely valuation-theoretic once the inductive classification is available.

This leaves two natural questions open:

- whether Borel measurability alone forces enough integrability to obtain the same classification; and
- whether boundedness alone forces measurability of the orthoscheme restriction.

No claim on either point is made here.

## References

1. Martin Lotz, *Hadwiger's classification theorem on the sphere via signed orthoscheme decompositions*, arXiv:2609.17437 (2026). The continuous spherical/conic Hadwiger theorem, automatic \(\mathrm O(n)\)-invariance on polyhedral cones, and the \(L^1\) orthoscheme vanishing theorem are the principal inputs.
2. Jonas Knoerr, *Rigid motion invariant valuations on polytopes*, arXiv:2608.19110 (2026). Classifies measurable translation- and rotation-invariant valuations on Euclidean polytopes.
3. Jonas Knoerr, *Isometry invariant valuations on spherical polytopes*, arXiv:2608.26015 (2026). Gives the continuous isometry-invariant spherical-polytope classification.
4. Martin Lotz, *Monotone invariant valuations on convex cones*, arXiv:2609.09335 (2026). Classifies monotone invariant conic valuations and proves automatic continuity under monotonicity.

## Limitations

The theorem assumes both global boundedness and Borel measurability on the polyhedral-cone space. It does not prove that either hypothesis can be removed, does not address unbounded measurable valuations, and is restricted to real-valued scalar valuations. The main regularity input is Lotz's \(L^1\) orthoscheme vanishing theorem; no independent replacement for that theorem is supplied here. Originality is asserted only to the best of our knowledge, and the relevant 2026 valuation literature is sufficiently recent that differently phrased or not-yet-indexed parallel observations remain possible.
