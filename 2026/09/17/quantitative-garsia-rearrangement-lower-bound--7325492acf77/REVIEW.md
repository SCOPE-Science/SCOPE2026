# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The proof uses three published ingredients in compatible finite forms.

Karagulyan's Theorem 1.1 gives a permutation of the first \(m\) trigonometric
characters whose maximal partial-sum operator has \(L^2\)-norm
\(\gtrsim\log m\). Restricting a maximizing input to the first \(m\)
frequencies yields an \(\ell^2\)-normalized finite coefficient vector.

Lewko's deletion proof for the prescribed-pattern coloring lemma is kept
unchanged, but the qualitative estimate \(r_m(N)=o(N)\) is replaced by the
explicit condition \(r_m(N)\le\eta_mN\), with
\(\eta_m=(2m)^{-10m}\). Each intersection support then has size at most
\(\binom{m^2}{m}\eta_mN\). The resulting entropy contribution is
\(o(N/m)\), while the balanced-coloring comparison has a negative main
exponent
\[
2N\log(m-1)-2N\log m\sim-2N/m.
\]
Thus the same averaging argument produces the required second permutation
once \(N\) is sufficiently large.

Gowers' explicit quantitative Szemeredi estimate gives such an \(N\) below a
five-fold exponential \(E_5(Cm)\). The arithmetic-progression transfer is
exact: integer modulation has unit modulus and integer dilation preserves
Haar measure. The two-copy probability space contributes only the factor
\(2^{-1/2}\). Padding by fixed extra frequencies preserves the lower bound.
Inverting \(N\le E_5(Cm)\) and then taking the logarithmic Karagulyan lower
bound gives \(\log_{(6)}N\).

Checks were also made for coefficient normalization, the second-copy index
assignment, the balanced-coloring count, and the direction of the padding
argument. No empirical computation is used as a substitute for the proof.

## Originality — PASS

Originality is asserted only to the best of our knowledge. Lewko's
arXiv:2609.18491, submitted 16 September 2026, explicitly says that the proof
as written gives no useful dependence of \(N\) on \(H\) and that the true
rate of growth of the optimal finite constant is unknown. Searches combining
that paper and theorem with quantitative Garsia/Kolmogorov rearrangement
bounds, Karagulyan's logarithmic finite obstruction, and quantitative
Szemeredi estimates found no prior statement of the iterated-log lower bound
or of this quantitative synthesis.

The constituent results are not claimed as new. The main residual
originality risk is contemporaneous work or commentary on the very recent
Lewko preprint that is not yet indexed.

## Value — PASS

The result answers an explicit quantitative gap left by the new negative
solution of Garsia's conjecture: qualitative divergence is replaced by a
fully explicit, if extremely slow, universal lower rate. It also isolates
where the poor rate enters, so improved quantitative arithmetic-progression
bounds can be transferred directly to the analytic rearrangement problem.

The result does not approach Bourgain's \(O(\log\log N)\) upper bound and
does not claim sharpness.

## Source and access limitations

The relevant theorem statement and finite combinatorial argument in Lewko's
arXiv preprint were inspected. Karagulyan's theorem statement and operator
definition were inspected in the published-paper text. Gowers' quantitative
Szemeredi bound was checked against the 2001 theorem and its standard
explicit consequence. Bourgain's upper bound was cross-checked through the
statement quoted in Lewko's introduction.

No inaccessible paper was identified as specifically likely to overturn the
claim. The largest residual literature risk comes from very recent,
not-yet-indexed discussion of arXiv:2609.18491.

Not independent validation, peer review, formal verification, or a guarantee
of first discovery.
