# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The proof reduces the DNP failure probability to three independently controlled quantities. The projector-intersection step uses the quantum union bound and the Friedrichs-angle estimate from Foxman--Lombardi--Ma--Nehoran--Wright. The NoPlus estimate is valid for arbitrary entangled \(t\)-register inputs because conjugating a projector acting on one query register leaves identity on the other registers; only the one-copy operator \(\mathbb E_U U^\dagger|+\rangle\langle+|U\) is needed. The ordinary-distinctness estimate follows from the operator union bound over pair collisions. For product local 2-designs, the equality-projector twirl factors across sites and has local norm \(2/(d+1)\). Tensor products of independent local 1-designs are global 1-designs. These points cover the main hidden-hypothesis risks in the argument.

The bound is deliberately restricted to \(t\le N/2\), safely inside the regime in which the cited Friedrichs-angle estimate is applied. The asymptotic corollary only uses polynomial \(t\) and fixed local dimension, so this restriction is immaterial there.

## Originality

**PASS, to the best of our knowledge.** Raza--Eisert--Fefferman explicitly ask whether the depth-one ensemble of independent single-qubit Clifford gates is non-plussed distinct. Their paper proves ordinary distinctness/entangled anticoncentration but does not answer that stronger question. Foxman--Lombardi--Ma--Nehoran--Wright prove DNP concentration for a global unitary 2-design; their stated theorem does not cover the product-local Clifford ensemble, which is not a global 2-design.

Targeted searches for the exact open-question terminology and synonymous combinations involving non-plussed distinctness, local/single-qubit Cliffords, NoPlus, 1-designs, and DNP found the open question and the two source papers, but no prior theorem giving this implication or the local-Clifford corollary. The current SCOPE archive was also checked by the motivating arXiv identifier, the phrase “non-plussed distinct”, and “single-qubit Clifford”, with no overlap found.

Priority uncertainty remains material because the motivating paper is recent and the deduction becomes short once the projector-angle proof from the earlier DNP paper is combined with the local ensemble's 1-design property. A near-simultaneous observation or an unindexed note could therefore cover the same corollary. No specific inaccessible paper was identified whose known statement appears likely to subsume the result.

## Value

**PASS.** The result resolves an explicit structural question about the shallowest distinct ensemble highlighted by Raza--Eisert--Fefferman. The lifting inequality is more general than the single example: it shows that DNP concentration follows from ordinary distinctness plus a one-copy flatness parameter, and it yields a uniform qudit product-2-design family with an explicit error bound. The conclusion is directly relevant to attempts to simplify PRU constructions, while the record carefully does not claim the additional PRU-security implication.

## Scientific limitations

The result proves DNP concentration only. It does not establish security of \(P\bigotimes_i C_i\), does not treat stronger oracle-access models, and does not optimize the Friedrichs-angle or union-bound constants. The originality claim is therefore confined to the lifting statement, its product-local 2-design specialization, and the affirmative resolution of the stated non-plussed-distinctness question.
