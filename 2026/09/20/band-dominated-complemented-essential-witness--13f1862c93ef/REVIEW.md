# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The central estimate is deliberately one-sided and remains valid at the
p=1 endpoint: for finite F, the operator BP_F has finite rank because the input
fibers are finite-dimensional, hence ||BQ_F|| is at least the classical essential
norm of B. No false tail-limit assertion for arbitrary compact maps on l_1 is used.

For finite propagation R, recursively excluding the finite 2R-neighborhood of all
previous input supports produces finitely supported norming vectors whose input
supports are more than 2R apart. Their B-images lie in pairwise disjoint
R-neighborhoods, so the outer l_p norm (or c_0 sup norm) gives a uniform lower
bound on their entire closed span, not merely on the basis vectors. Passing from B
to a band-dominated A loses only the operator-norm approximation error, while the
essential norm changes by at most the same error.

Complementability is checked explicitly. On each finite input block a norm-one
functional attaining the chosen unit vector is used, and the blockwise rank-one
sum is a contractive projection. In the c_0 case its coefficient sequence tends to
zero because the disjoint finite supports escape every finite set. Thus no
complementability conclusion is inferred from unconditionality alone.

The reverse bound for the complemented modulus uses only that compact operators are
strictly singular. The exact SS/FSS/compact distances then follow from the witness
and the ideal inclusions K subset FSS subset SS. For Bernstein numbers, every
finite-dimensional slice of the infinite witness has the same lower bound. For
approximation numbers, finite coordinate projections on the target give the metric
approximation property needed to approximate compact maps by finite-rank maps.

Adversarial boundary checks show why the hypotheses matter. If an input fiber is
infinite-dimensional, a noncompact propagation-zero map can live entirely on one
coordinate and defeat the escaping-block argument. Local finiteness is exactly what
keeps the recursively excluded neighborhoods finite. The argument does not extend
unchanged to l_infinity because finitely supported vectors are not dense there, or
to different outer exponents because disjoint sums no longer have matching norms.

## Originality

**PASS, to the best of our knowledge.** Rabinovich--Roch--Silbermann (2001, 2004)
are prior art for operator-valued band-dominated operators and their Fredholm/finite
section theory. Seidel (2014) surveys that framework. Hagger--Lindner--Seidel
(2016) is especially close: it identifies essential norms through limit operators
in the standard band-dominated setting and develops operator-norm localization.
Spakula--Willett (2016/2017) extends limit-operator theory to metric spaces, and
Roch (2022) studies closed ideals inside a uniform Roe/band-dominated algebra.
None of those antecedent themes is claimed as new here.

The proposed contribution is the exact complemented disjoint-block formula for the
classical essential norm and its consequences for strict singularity and Bernstein
numbers. Searches using band-dominated, finite-propagation, uniform Roe, strictly
singular, finitely strictly singular, complemented copy, essential norm and
Bernstein-number formulations did not locate this statement or a stronger theorem
that plainly implies it. Searches of the current SCOPE archive under the same
objects and synonymous terminology also found no overlapping accepted record.

The main residual originality risks are the 2004 Rabinovich--Roch--Silbermann
monograph and Roch's 2022 *Ideals of band-dominated operators*, neither of which was
exhaustively inspected theorem by theorem. The accessible primary text of
Hagger--Lindner--Seidel was checked at the theorem/proof level around its essential
norm localization results; its stated focus is Calkin/P-compact norms, limit
operators and pseudospectra rather than strict singularity or Bernstein numbers.
Accordingly, priority is asserted only to the best of our knowledge.

## Value

**PASS.** The theorem gives a geometric realization of the classical essential
norm, not only a compactness criterion: every noncompact band-dominated map fixes a
1-complemented classical sequence subspace at every level below its essential
norm. This immediately collapses compactness, finite strict singularity and strict
singularity inside the class and identifies their three distances exactly. It also
forces every Bernstein number to be at least the essential norm and determines the
common asymptotic value of Bernstein and approximation numbers.

The mechanism is reusable and notably requires neither a group action nor Property
A, richness, bounded geometry, a uniform bound on fiber dimensions, or Hilbert
space structure. It therefore isolates a coarse finite-propagation phenomenon from
the stronger hypotheses usually needed for limit-operator Fredholm theorems.

## Scientific limitations

The result is restricted to finite-dimensional fibers and to l_p-sums for
1<=p<infinity or c_0-sums, with the same outer norm on domain and codomain. It does
not address l_infinity-sums, cross-exponent maps, or infinite-dimensional fibers.
The complemented lower modulus is identified as a supremum; an exact maximizing
subspace need not exist.

The most relevant unresolved literature uncertainty is possible equivalent wording
inside the 2004 monograph or the full 2022 ideal-structure paper. No claim is made
that those sources lack such a result merely because they were not exhaustively
checked.
