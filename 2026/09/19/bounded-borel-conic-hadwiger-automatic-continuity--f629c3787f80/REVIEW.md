# Review — Automatic continuity for bounded Borel rotation-invariant conic valuations

Same-model review: passed. Independent audit: not yet performed.

## Correctness

The proof has two independent inductive reductions before invoking the recent orthoscheme vanishing theorem.

First, after subtracting the intrinsic-volume combination with coefficients \(c_j=\nu(L_j)\), the residual \(\rho\) vanishes on every linear subspace. Restricting to any proper subspace \(V\) preserves boundedness and Borel measurability because the inclusion of polyhedral cones in \(V\) into the ambient cone space is continuous. Orthogonal invariance descends because an element of \(\mathrm O(V)\) extends by the identity on \(V^\perp\). The lower-dimensional induction therefore makes \(\rho\) vanish on every lower-dimensional polyhedral cone.

Second, for a fixed line \(\ell\), the stabilized functional
\[
\eta_\ell(D)=\rho(\ell\oplus D)
\]
on \(\ell^\perp\) is again a bounded Borel orthogonally invariant valuation. Its coefficients in the lower-dimensional classification are its values on subspaces, all of which vanish; the top coefficient also vanishes because \(\ell\oplus\ell^\perp=\mathbb R^n\) and \(\rho(\mathbb R^n)=0\). Hence \(\rho\) vanishes on every cone containing a line.

These two conclusions are exactly the algebraic vanishing condition required by Lotz's polyhedral orthoscheme theorem. The orthoscheme parametrization is continuous, so the pullback of the bounded Borel residual is bounded and measurable on a finite-measure chamber, hence lies in \(L^1\). Lotz's vanishing theorem then forces the residual to be zero.

The one-dimensional \(\mathrm O(1)\) base case was checked directly from the four cones \(\{0\},\mathbb R_+,\mathbb R_-,\mathbb R\). The final norm identity follows because the conic intrinsic volumes are nonnegative, sum to one, and satisfy \(v_i(L_j)=\delta_{ij}\). No numerical computation is used.

Potential hidden hypotheses were checked as follows. Intrinsic volumes are unchanged by isometric inclusion into a larger Euclidean space; the direct-sum map \(D\mapsto\ell\oplus D\) is continuous in the spherical Hausdorff topology; and a cone containing a line \(\ell\) decomposes as \(\ell\oplus(C\cap\ell^\perp)\). These facts cover the restriction, measurability, and lineality steps used in the proof.

## Originality

The primary source arXiv:2609.17437 was inspected at the statements establishing the continuous conic Hadwiger theorem, automatic reflection invariance for polyhedral-cone valuations, and the residual vanishing theorem under an \(L^1\) orthoscheme hypothesis. That paper emphasizes that its final vanishing step needs only integrability, but its advertised classification theorem is the continuous theorem. The present result uses an induction over subspaces and lineality to show that bounded Borel regularity is sufficient to manufacture the full residual hypothesis in every dimension.

The closest recent neighboring results found are distinct:

- arXiv:2608.19110 classifies measurable rigid-motion-invariant valuations on Euclidean polytopes, where translation invariance is essential to the setup;
- arXiv:2608.26015 states the spherical-polytope classification under continuity;
- arXiv:2609.09335 obtains automatic continuity for monotone invariant conic valuations without regularity assumptions, but monotonicity is substantially stronger and logically different from bounded Borel regularity.

Searches combining “bounded Borel”, “bounded measurable”, “polyhedral cones”, “spherical polytopes”, “rotation invariant valuation”, “conic intrinsic volumes”, and “automatic continuity” did not locate the theorem stated here or the isometric \(\ell_\infty^{n+1}\) corollary. Searches of the current SCOPE archive by conic valuation, spherical valuation, Hadwiger, and intrinsic-volume terminology found no overlapping record.

The full text of arXiv:2608.26015 was not used to establish a negative full-text claim; its public theorem statement explicitly assumes continuity. It remains a plausible source of an unadvertised remark or corollary close to the present statement. The same residual risk applies to the very recent valuation preprints cited above and to not-yet-indexed parallel work. Originality is therefore only to the best of our knowledge.

## Value

The result converts a local regularity relaxation inside the new orthoscheme proof into a complete global classification theorem. It shows that on polyhedral cones the usual continuity hypothesis can be replaced by the strictly weaker pair “bounded and Borel measurable”, and that this weaker hypothesis in fact forces a unique continuous extension to all closed cones.

The exact norm formula
\[
\|\nu\|_\infty=\max_j|\nu(L_j)|
\]
also identifies the entire bounded Borel invariant valuation space isometrically with \(\ell_\infty^{n+1}\). Thus arbitrary polyhedral-cone values are controlled by only \(n+1\) subspace evaluations.

## Limitations

Both boundedness and Borel measurability are assumed. The proof does not classify unbounded measurable invariant valuations and does not show that boundedness by itself implies measurability. It is scalar-valued and finite-dimensional. The proof depends on the recent \(L^1\) orthoscheme vanishing theorem rather than reproving it. Because several closely related classification results appeared in August–September 2026, unindexed or differently phrased parallel observations remain a meaningful originality risk.
