# Self-review

## Correctness
**PASS.** Otsubo's Theorem 1.1 gives the parameter relation
\[
\mu'^{3}=\frac{(\mu+2)^{3}}{9(\mu^{2}+\mu+1)}
\]
for the cubic-AGM Hesse \(3\)-isogeny. On the diagonal \(\mu'=\mu\), exact expansion gives
\[
9\mu^{3}(\mu^{2}+\mu+1)-(\mu+2)^{3}
=
(\mu-1)(3\mu^{2}+2\mu+4)(3\mu^{2}+4\mu+2).
\]
The singular root \(\mu=1\) is excluded. The two irreducible quadratics give four allowed complex parameters. Substitution into Otsubo's exact formula
\[
j(H(\mu))=27\mu^{3}\left(\frac{\mu^{3}+8}{\mu^{3}-1}\right)^{3}
\]
reduces identically to \(-32768\) on \(3\mu^{2}+2\mu+4=0\) and to \(8000\) on \(3\mu^{2}+4\mu+2=0\). The packaged exact checker independently replays these polynomial identities. Sage's CM reference table identifies the two \(j\)-values with fundamental discriminants \(-11\) and \(-8\), respectively.

Risk: the checker certifies the algebraic identities, not the general theorem of Otsubo nor the external CM table; those are literature premises explicitly cited in the result.

## Originality
**PASS.** The inspected full text of arXiv:2610.03100v1 states the isogeny correspondence and the Hesse \(j\)-formula but does not state its diagonal fixed locus; searches in that full text found no occurrence of \(8000\), \(-32768\), or a self-isogeny classification. The closest older literature, *Adventures in Supersingularland*, already knows the four \(j\)-level self-\(3\)-isogeny values \(0\), \(54000\), \(8000\), and \(-32768\). That result does not identify which self-isogenies preserve Otsubo's newer Hesse parameter itself. The new claim is exactly that level-structured diagonal classification and shows that only the two double-loop values \(8000\) and \(-32768\) occur.

Residual risk: Hashimoto--Nuida's 2026 finite-field cubic-AGM paper is highly relevant, but only its abstract was inspectable. It may contain a finite-field fixed-point statement. Such a statement would have to match the literal complex Hesse-parameter diagonal and the same four parameters to cover the present claim.

## Value
**PASS.** Fixed points are a natural first invariant of a newly explicit dynamical/isogeny correspondence. The classification is structural rather than a parameter sample: it determines the complete diagonal, connects the two quadratic parameter fields to exactly two classical CM \(j\)-classes, and explains why the Hesse level parameter sees the double self-\(3\)-isogeny classes but not the simple-loop classes. This gives a compact bridge between the new cubic-AGM formula and the classical modular-\(3\) self-isogeny picture.

Risk: the calculation is short once the new correspondence is available. Its value lies in the complete fixed-locus interpretation and its precise comparison with the modular-polynomial self-loop classification, not in computational complexity.

Self-review: passed. Independent audit: not yet performed.
