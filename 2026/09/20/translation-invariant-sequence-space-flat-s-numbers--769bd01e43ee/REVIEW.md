# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof uses only the translation symmetry and the elementary geometry
of l_p and c_0. A finitely supported near-norming vector u is translated to
pairwise disjoint input supports. Finite truncations of Tu are simultaneously
translated to pairwise disjoint output supports. The discarded output tails are
made summable in exactly the dual form needed for p>1, uniformly small for p=1,
and l_1-summable for c_0. This yields a lower bound arbitrarily close to ||T||
on a classical sequence subspace.

Complementability is verified directly. A norm-one functional on the finite
coordinate block supporting u is translated to each disjoint block; the resulting
blockwise rank-one map is a norm-one projection onto the span of the translates.
No inference from unconditionality or a block-basis principle is used.

The distance to the strictly singular ideal follows because a strictly singular
operator cannot be bounded below on the infinite-dimensional witness. The compact
and finitely strictly singular distances then follow from ideal inclusion. The
approximation and Bernstein identities are immediate consequences of those bounds
and the witness. For Gelfand numbers, every finite-codimensional subspace meets the
witness in an infinite-dimensional subspace. For Kolmogorov numbers, a separate
finite-dimensional-tail argument shows that a translate of Tu can escape any
prescribed finite-dimensional quotient target almost at full norm. These arguments
also cover uncountable discrete groups because only finitely many group elements
are excluded at each translate-selection step.

Boundary checks include p=1, where the perturbation estimate uses sup delta_k;
1<p<infinity, where Holder duality is used; and c_0, where summable tail errors
and the vanishing-at-infinity property guarantee convergence of the explicit
projection. The finite-group case is correctly excluded.

## Originality

**PASS, to the best of our knowledge.** Crombez--Govaerts (1978) is classical
prior art for compact convolution operators on L_p-spaces. Their 1980 paper treats
compactness, weak compactness and strict singularity for convolution-type maps from
l_1 to l_infinity, so strict-singularity phenomena for convolution-type operators
are not new in general. Finol (1986) studies strict singularity and existence of
translation-invariant operators in Orlicz sequence-space settings, especially
between distinct spaces.

The closest result located is Karlovych--Shargorodsky (2024), which proves maximal
noncompactness for translation-invariant operators between broad translation-invariant
sequence spaces on Z^d under mild conditions on the target. Its abstract explicitly
identifies equality of the operator norm with the Hausdorff measure of noncompactness,
and the bibliographic record lists essential norm among the keywords. Accordingly,
this record does not claim novelty for essential-norm equality or maximal
noncompactness itself; those phenomena are treated as prior art.

Searches under translation-invariant operators, convolution operators, multipliers,
strict singularity, Bernstein numbers, Gelfand numbers, Kolmogorov numbers and
s-number terminology did not locate the all-n equality
`a_n=b_n=c_n=d_n=||T||`, the exact distance to the FSS/SS ideals, or the explicit
1-complemented almost-norming witness for this class. Edmunds--Lang (2025) further
emphasize that Bernstein numbers and strict singularity encode structure not
captured by ordinary noncompactness quantities, supporting the substantive
distinction from maximal noncompactness alone.

The principal residual risk is the 2024 Karlovych--Shargorodsky paper itself: its
full text could not be exhaustively inspected in the available source trail, so a
stronger theorem or corollary there could overlap part of the present claim even
though the accessible abstract states only maximal noncompactness. Older multiplier
monographs and Fredholm/local-spectral literature are a second residual risk because
the disjoint-translate mechanism may appear there under different terminology.
These risks limit originality to the best of our knowledge rather than an absolute
priority claim.

## Value

**PASS.** The result upgrades a qualitative noncompactness phenomenon to a complete
finite-index profile for four classical s-number scales and to exact distances from
three nested operator ideals. The 1-complemented almost-norming subspace gives a
reusable structural obstruction: every nonzero translation-invariant operator in
this class fixes a complemented classical sequence subspace at arbitrarily close
to its full norm. The theorem applies uniformly to every infinite discrete group,
including nonabelian and uncountable groups.

## Scientific limitations

The theorem is for same-space operators on l_p(G), 1<=p<infinity, and c_0(G). It
does not cover l_infinity(G), where finite-support density fails, and it does not
classify cross-space translation-invariant maps. It also does not identify the
operator with a convolution kernel in any particular multiplier algebra.

The 2024 closest source was verified at the bibliographic/abstract level but not
exhaustively at full-text theorem level; this is the most scientifically relevant
remaining literature uncertainty.
