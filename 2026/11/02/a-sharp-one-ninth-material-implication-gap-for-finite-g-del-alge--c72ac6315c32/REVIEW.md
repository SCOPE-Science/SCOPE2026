# Scientific review: sharp material-implication gap on finite Gödel algebras

## Correctness — PASS

The proof works with the standard finite-forest representation \(H=J(P)\). It derives the exact implication-fixpoint count recurrences \(\sigma(H_1\times H_2)=\sigma(H_1)\sigma(H_2)\) and \(\sigma(\mathbf 0\oplus B)=|B|+1+\sigma(B)\). The corresponding material-implication failure identity for a new least element is \(\Delta(\mathbf 0\oplus B)=|B|^2-\sigma(B)\). Induction proves \(\sigma(B)\le |B|(|B|+1)/2\), with equality exactly for chain duals, yielding the sharp connected bound. The coordinatewise product calculation then yields the one-ninth gap and its full equality classification. The decoded accompanying checker directly enumerates the material implication and verifies the structural recurrences for 5,913 finite forest presentations through seven vertices, plus selected larger families. The proof, not this enumeration, handles all finite sizes.

## Originality — PASS, subject to stated search limits

Bumpus and Kocsis (arXiv:2110.11515, §3.15 and §6.6) establish absence of a material-implication gap for all finite Heyting algebras and explicitly propose restricted Gödel algebras as a further research setting. They do not derive the present restricted **positive** gap, its sharp equality cases, or the exact connected-tree extremum. Flaminio et al. (arXiv:2110.02528, §2) provide the prelinear algebra/forest duality used as a known premise; their inspected material concerns representations, not valuation-frequency inequalities. Related research records on materializers address lattice closure and intrinsic distributivity, not probabilities. Searches also considered equivalent 'strict versus material implication', implication-fixed-point counts, and forest duality formulations. No stronger covering statement was found, although absence from searches does not prove absolute novelty; a disguised equivalent counting theorem remains the main priority risk.

## Mathematical value — PASS

This gives an exact optimal answer in a natural restricted class to a direction explicitly raised in the satisfiability-degree literature. In contrast with the failure of finite gap over arbitrary Heyting algebras, finite Gödel algebras have the sharp gap \(1/9\). The connected bound is attained at **every** eligible algebra size, and the equality classification identifies exactly the products \(C_3\times C_2^k\). The auxiliary implication-fixpoint extremum exposes the structural reason for sharpness rather than merely providing an isolated example. The theorem concerns finite algebras and uniform ordered pairs; its generalization to other sampling distributions or infinite algebra measures is unproved.

## Sources and remaining risk

Primary mathematical motivation: B. M. Bumpus and Z. A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, arXiv:2110.11515 (2021), especially §3.15 and §6.6. Representation background: T. Flaminio, L. Godo, P. Menchón and R. O. Rodríguez, *Algebras and relational frames for Gödel modal logic and some of its extensions*, arXiv:2110.02528 (2021), especially §2. Historical priority in equivalent tree-count or implication terminology requires further independent comparison; no independent scientific audit is claimed.

Self-review: passed. Independent audit: not yet performed.
