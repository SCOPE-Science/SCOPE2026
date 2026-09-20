# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The central identity follows from the nondegenerate finite-field trace pairing: a nonzero B-linear functional is Tr(beta ·), and the reused leakage functionals have coefficient vectors beta g_i, whose B-span has exactly the same dimension as the computation columns. The transcript-compression statement is then immediate from B-linear column relations. The criterion rho_B(G)=K iff a row-equivalent generator is defined over B follows by choosing a B-basis of the column span and observing that it must be F-independent because G has F-row rank K. Restricting a putative K-stream reconstruction to one freely varying selected base-code stream proves the LERS no-amplification equivalence. At rho_B(G)=Km, the local leakage map has full domain rank and is injective.

The random systematic corollary reduces exactly to the rank of L independent uniform vectors in the D=K(m-1) dimensional quotient F^K/B^K. The stated full-rank probability is the sequential count product_{i=0}^{D-1}(1-q^{i-L}); the lower bound follows from a union bound, and the no-amplification probability is the probability that all random columns lie inside B^K.

Adversarial checks considered dependence on the choice of generator basis, possible F-dependence of a B-basis when rho_B(G)=K, arbitrary non-coordinate trace functionals, and whether local rank alone was being overstated as a global LERS criterion. Generator-basis invariance holds under GL_K(F), the selected K basis columns are necessarily F-independent, every nonzero B-linear scalar functional is covered by trace duality, and the public statement explicitly does not infer a global LERS in the intermediate-rank regime.

The standalone verifier reports PASS. It checks 76,200 random trace-rank instances over GF(2^m), m=2,3,4; 65,216 exact transcript identities for a base-field computation; 308 injective rank-saturation share instances; and 11 small exhaustive random-matrix probability counts.

## Originality

**PASS, to the best of our knowledge.** The closest source is Aoutouf--Augot, arXiv:2609.19929 (v1, 17 Sep 2026). Its primary PDF, including the general rank criterion, numerical examples, and identical-leakage section, was inspected directly. It proves the identical-leakage no-improvement statement for simple addition, says that the argument "seems to extend directly" to its array-summation example, gives simulations for general linear relations, and gives the LFSR full-share-recovery example. It does not state an exact general invariant controlling the number of independent identical-leakage projections, a field-of-definition/no-amplification iff criterion, or the random systematic rank-saturation law.

The predecessor WCC 2026 primary PDF by the same authors was accessible; its contribution statement, LERS definitions, and subfield-subcode construction were inspected. Those sections develop the base repair construction rather than a linear-computation analysis.

Targeted searches covered identical leakage functions + linear computations; reused/same leakage + secret sharing; trace leakage + finite-field linear combinations; rank weight/rank support + leakage; computation code + subfield/defined-over-subfield; and the exact motivating arXiv identifier. These searches returned the motivating preprint and general rank-metric or leakage-resilience literature, but no equivalent theorem. The current SCOPE repository was searched by the motivating arXiv identifier, Massey/LERS terminology, identical leakage, subfield rank, and computation-code phrasing; no overlapping record was found.

No novelty is assigned to finite-field trace duality, rank weight/rank support, or the usual notion that a code descends to a subfield. The originality claim is only their synthesis into the exact reused-leakage rank law and its consequences for this computation-leakage model.

### Residual literature risk

The CRYPTO 2018 / Journal of Cryptology work of Benhamouda--Degwekar--Ishai--Rabin on local leakage resilience was inspected through its openly available ePrint; it studies local leakage and MPC more broadly but not the product-code identical-leakage computation invariant here. Nguyen's 2025 physical-bit leakage work was inspected at abstract/bibliographic level rather than in full; it is primarily about resilience bounds for code-based secret sharing, so it is a lower-probability but nonzero originality risk. Rank-metric literature uses closely related rank-support notions, so a mathematically equivalent linear-algebra lemma could be folklore even if the leakage application is not recorded. The motivating preprint is only days old, making a near-simultaneous observation or later revision the largest priority risk.

## Value

**PASS.** The result replaces example-by-example behavior by a single exact quantity with a sharp trichotomy. It proves the array-summation extension left informal in the motivating paper, shows that general coefficients outside {0,1} are not sufficient for amplification when they remain in the leakage subfield, identifies maximal subfield rank as complete local share disclosure, and gives an exact probability threshold for random systematic computation layers. These consequences clarify when repeated physical leakage of the same linear observable can actually exploit computational redundancy.

## Limitations

The result is confined to identical one-symbol B-linear leakage on linear computations. It does not address nonlinear leakage, fresh/independent leakage functions, refreshed shares, or multiplicative computations. In the intermediate regime K<rho_B(G)<Km it quantifies local information exactly but does not solve the global LERS existence problem.
