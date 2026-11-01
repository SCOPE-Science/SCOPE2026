# Scientific assessment: partition-growth monotone-gap subshift

## Correctness

**PASS.** The language count is a bijection from a word having at least two markers to its first/last marker distance, starting position, and weakly increasing integer partition of that distance. The Euler product then follows from the standard partition identity. The exact leading stretched-exponential constant follows from the Hardy--Ramanujan partition asymptotic and a dominated Riemann-sum argument, with exponentially negligible large-distance tails. A periodic sequence of nondecreasing positive gaps must be constant, which yields the exact prime-orbit census and zeta product. A strict gap increase produces a nonreturning cylinder; the remaining nonperiodic configurations have a nonreturning endpoint cylinder. Poincare recurrence proves the periodic-atomic invariant-measure decomposition. The companion finite checker was executed successfully. Main proof risks: correct treatment of finite/one-sided supports and the normalization in the partition asymptotic; both were explicitly verified in the argument. The finite checker is corroborative, not a proof of infinite assertions.

## Originality

**PASS under the material inspected, subject to historical priority risk.** Xie--Chen--Zhou (arXiv:2608.10460, Section 6) constructs subshifts by varying a sparse support, and estimates growth up to comparison constants; their construction does not enforce ordered neighboring gap distances or give a partition-exact language/zeta relation. Greenfeld--Moreira--Zelmanov (arXiv:2408.03403, Theorem 1.1) provides general asymptotic-equivalence realizability, not the exact invariant-measure and primitive-period classification. The 2019 *Increasing Gap Shifts* paper instead constrains each gap to a prescribed numerical set and proves mixing, which is an inequivalent problem. Indexed research on geometric or modular \(S\)-gap shifts also restricts individually allowed gap lengths rather than imposing successive monotonicity. No inspected stronger result implies the complete four-part conclusion: exact language count, sharp constant, periodic zeta, and invariant-measure rigidity. Search incompleteness and unindexed specialized combinatorics remain possible priority risks.

## Mathematical value

**PASS.** The system is the elementary local-pattern restriction that successive marked-return times cannot decrease. The exact Euler partition growth has entropy dimension \(1/2\) and a nontrivial sharp constant even though all invariant ergodic measures are periodic and every recurrent configuration is periodic. The identity \(c_{n+1}-c_n=[z^n]\zeta_\sigma(z)\) couples two usually separate dynamical diagnostics without a generic zeta/complexity equivalence; this is a meaningful structural example in intermediate-entropy dynamics, rather than a re-expression of an arbitrarily chosen finite enumeration. The elementary partition algebra by itself is classical; value is in the complete dynamical synthesis and rigorous transient-complexity phenomenon.

## Closest literature and limits

See RESULT.md for complete scientific definitions, proof, verification and references. Specifically inspected the accessible primary full-text Section 6 of Xie--Chen--Zhou; introductory theorems of Greenfeld--Moreira--Zelmanov and the full scientific description and Section 3 of Kamarudin--Baloush--Che Dzul-Kifli. The theorem does not cover unrestricted \(S\)-gap shifts, variants allowing gap decreases, or arbitrary intermediate-complexity subshifts. Historical priority is not an independently verified fact; independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
