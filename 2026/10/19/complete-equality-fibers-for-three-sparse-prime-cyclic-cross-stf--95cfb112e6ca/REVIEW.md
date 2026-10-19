# Research review

## Correctness
**PASS.** Each time-delay STFT row is the Fourier transform of an intersection signal, so prime Fourier uncertainty and the exact intersection-count identity give \(|\operatorname{supp}V_gf|\ge |A-B|(p+1)-9\). Vosper's theorem forces common-step progressions when equality holds and \(p\ge7\). The five nonzero Fourier rows then supply one quadratic and two linear root constraints; exact factorization solves every nonzero complex coefficient, proves sufficiency, and gives a one-to-one parameterization. Independently coded finite checks reproduce the constructed supports and the sharp sumset geometry; universality is analytic, not inferred from tests.

## Originality
**PASS, qualified by historical-priority uncertainty.** Krahmer–Pfander–Rashkov already give the same sharp *numerical bound* in arXiv:math/0611493v1, Proposition 4.4. That bound and their Cauchy–Davenport argument are expressly credited. Their statement does not supply equality geometry, phase/amplitude parameters, or component counts. Nicola's 2022 full paper treats equality in the distinct global \(p\)-support bound. Bartusel's 2026 accessible introduction and theorem overview treat conditions for STFT phase retrieval rather than these equality fibers. Two closely relevant published specializations were read in their entirety: one is restricted to self-ambiguity \(g=f\), the other to two-sparse pairs. No inspected comparison covers the present independent three-sparse classification; unindexed equivalence remains a risk.

## Value
**PASS.** Equality cases for a standard sharp uncertainty inequality describe the maximally concentrated structured measurement pairs, not an arbitrary finite slice. This classification determines the support geometry, all admissible complex amplitudes and phases, and the topology of the normalized equality locus; previously knowing only the numerical threshold does not determine any of those. It also strictly extends a corresponding self-ambiguity classification to independent signals and windows without treating the numerical lower bound as new.

## Scientific limitations and literature risks
The result assumes prime \(p\ge7\) and exactly three nonzero entries in each signal; there is no near-extremizer stability theorem, composite-order classification, or exhaustive historical-priority guarantee. The continuous coefficient family is counted only with fixed normalized support labels. Numerical checks do not certify the infinite theorem.

Self-review: passed. Independent audit: not yet performed.
