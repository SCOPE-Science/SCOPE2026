# Scientific review: a divisibility boundary for bipartite fractional hedonic games

## Correctness — PASS

The final claim uses coalition-size normalization, strict unilateral entry, and the strict-core notion with a weakly improving group and at least one strict improver. Reconstructing all four directed one-player deviations gives exactly the determinant bounds, with no missed singleton case because stable coalitions are mixed. Cauchy–Schwarz proves the welfare optimum and equality case, and integer residuals \(\delta_i=y_i-qx_i\) establish rigidity in divisible populations. In nondivisible populations the \((1,q)\)/\((1,q+1)\) construction passes every determinant inequality, produces the stated strictly positive exact deficit, and has an explicit weak blocking coalition. The divisible exact count follows by labeled exponential enumeration. `verification/checker.py` performs direct independent exact-arithmetic checks on every labeled partition for 25 size pairs totaling 684404 partitions; finite checks support rather than prove the infinite theorem.

## Originality — PASS, with priority risk

The primary source arXiv:2311.11101 investigates approximate coalitional core stability, not the complete bipartite unilateral Nash spectrum. The closest same-graph literature is Aziz et al., arXiv:1705.10116, Theorem 5.3: it establishes type-proportional strict-core partitions and thus does **not** establish that all Nash equilibria are type-proportional exactly under divisibility, nor the exact labeled Nash enumeration. Bilò et al. (JAIR 2018), Lemma 12, already establishes the welfare-merging inequality but not the Nash determinant conditions or arithmetic coincidence classification. Krogmann et al., arXiv:2501.05334, imposes restricted placement rules and measures a different social objective. Checks across accessible previously recorded claims found related strict-core blocker-count calculations for the same \(K_{a,b}\) family, but no implication to the unilateral Nash theorem. Specialist literature beyond inspected material may contain an equivalent result; absence from searches is not proof of novelty.

## Mathematical value — PASS

The two-population complete bipartite game is a canonical tractable testbed for contrasting unilateral equilibrium, group stability, and optimal utility. A sharp integer-divisibility boundary gives an all-size structural classification, not an isolated example. The determinant description makes checking any proposed Nash partition immediate, and the exact divisible-case enumeration quantifies equilibrium multiplicity. The nondivisible construction produces genuinely inefficient yet individually stable outcomes, with a quantified gap and an explicit strict-core obstruction. These facts address a natural stability-versus-efficiency question that does not follow merely from existence of an optimal equilibrium.

## Sources and limitations

Material inspected: arXiv:2311.11101 (introduction, definitions, simple-fractional discussion); arXiv:1705.10116 (Section 5.3, strict-core characterization, related bipartite discussion); JAIR 62 (2018), pp. 323 and 338–340 (model and welfare lemma); arXiv:2501.05334 (model and restricted-placement setting). The 2014 AAMAS predecessor's initial pages were checked as supporting provenance. This review does not certify exhaustive global priority. The result does not classify nondivisible Nash counts or exact nondivisible price of anarchy.

Self-review: passed. Independent audit: not yet performed.
