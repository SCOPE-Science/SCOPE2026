# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The argument was checked from the exact trace-defect identity and from the
geometry of the constructed one-dimensional set.

For each \(0<\alpha<1\), the balanced branching rule gives
\(M_\ell\asymp q^{(1-\alpha)\ell}\). The retained \(q\)-adic children are
separated and include both endpoint children, so the limiting Cantor set has
two-sided neighborhood size
\[
|(C_\alpha)_r|\asymp r^\alpha.
\]
The alternating-gap set \(E_\alpha\) has boundary exactly \(C_\alpha\).

At every odd level \(\ell\), each new gap has length at least
\(h=q^{-\ell}\). Its adjacent retained child also has length \(h\). Since the
next level is even, all portions of \(E_\alpha\) inside that child lie in the
next retained children, whose total length is at most \(h/3\). Therefore each
odd-level gap contributes at least \(2h/3\) to the translation discrepancy at
shift \(h\). Since the number of such gaps is
\(\asymp q^{(1-\alpha)\ell}\), this gives
\[
|E_\alpha\triangle(E_\alpha+h)|\gtrsim h^\alpha.
\]
The opposite inequality follows from
\(E_\alpha\triangle(E_\alpha+h)\subset(C_\alpha)_{|h|}\).

For the spatial lower bound, scaling an odd level by
\(R=q^{\ell+1}\) makes every gap endpoint integral and every such gap at least
\(q\) lattice units long. Its left endpoint lies outside \(RE_\alpha\), while
the next integer lies inside. Hence the unit-shift symmetric difference has at
least one distinct lattice point per gap, giving \(R^{1-\alpha}\).

When \(\gamma<\eta\), the product set
\(F=E_\gamma\times[0,1)^{d-1}\) supplies
\(R^{d-\gamma}\) lattice discrepancies at the single shift \(e_1\).
The spectral box has a nonzero Fourier coefficient at \(e_1\), so one term of
the exact trace identity yields the required trace lower bound.

When \(\gamma>\eta\), the spatial cube reduces the problem to the spectral
translation modulus. For the one-dimensional interval lattice,
\[
D_N=\sum_m|K(m)|^2\min(N,|m|).
\]
Parseval and
\[
|e^{2\pi im/N}-1|^2
 \le4\pi^2\min(1,|m|/N)
\]
give
\[
D_N\ge \frac{N}{4\pi^2}|E_\eta\triangle(E_\eta-1/N)|.
\]
The odd-level shifts therefore give \(D_N\gtrsim N^{1-\eta}\). Restricting the
\(d\)-dimensional trace identity to axial frequencies multiplies this by
\(N^{d-1}\), yielding \(N^{d-\eta}\).

Product boundary estimates were checked in both regimes. A Lipschitz boundary
satisfies any weaker exponent in \((0,1]\), so the smooth side is admissible
for the prescribed larger exponent. The lower bounds are only asserted along
explicit lacunary subsequences, which is sufficient to rule out a smaller
uniform power.

No numerical computation is needed for the proof.

## Originality

**PASS, to the best of our knowledge.**

The primary source was inspected in full at arXiv:2609.12226v1. Its Theorem
2.2 gives the powers \(d-\eta\) for \(\gamma>\eta\) and \(d-\gamma\) for
\(\gamma<\eta\). Proposition 9.3 proves logarithmic sharpness only at
\(\gamma=\eta=1\). Remark 9.4 explicitly says that sharpness of both
off-critical powers remains open. Section 10 tests alternating-gap Cantor
examples numerically and explicitly says that the experiment is not a proof of
sharpness.

The present argument proves both off-critical lower powers and extends the
self-similar numerical examples to every fractional exponent by balanced
variable branching. It does not claim originality for Moran constructions,
Cantor neighborhood estimates, Parseval, or the trace-defect identity.

Searches included exact and synonymous formulations involving discrete Fourier
concentration, trace defects, off-critical sharpness, fractional translation
regularity, Minkowski boundaries, Cantor/Moran sets, and the specific source
identifier. No later paper or earlier theorem giving these lower bounds was
located. The current SCOPE archive was also checked by source identifier,
trace-defect terminology, concentration-operator terminology, and equivalent
claim wording, with no accepted overlap found.

The closest older works located were Hughes--Israel--Mayeli
(arXiv:2607.02996), on continuous rough-domain trace bounds, and
Marceca--Romero--Speckbacher (arXiv:2301.11685), on concentration eigenvalue
estimates under different Ahlfors-regular hypotheses. Neither supplied the
claimed discrete off-critical lower bounds.

Residual originality risk remains because the motivating preprint is recent
and the lower-bound mechanism is elementary once the alternating-gap geometry
is isolated. An unindexed contemporaneous observation is therefore possible.
No inaccessible paper was identified whose available metadata or theorem
description gave concrete evidence of coverage.

## Value

**PASS.**

The theorem settles the complete off-critical sharpness question posed in
Remark 9.4 of arXiv:2609.12226v1, for every dimension and every unequal pair of
fractional exponents. The construction also identifies a simple mechanism:
the smaller of the spatial and spectral regularity exponents alone forces the
upper power, while the other side may be smooth.

The critical fractional line remains open, and the result does not claim
all-scale asymptotics or sharp plunge-count lower bounds. These limitations
are explicit in RESULT.md.
