# Independent mathematical audit

## correctness

PASS

Start with Gx_n of norms tending to one, for unit x_n. Weak sequential compactness applies even in a nonseparable Hilbert space, or one can work in the separable closed span of the sequence. A unit weak limit gives norm convergence and a one-dimensional initial space. Otherwise the normalized deviations are unit and weakly null. Enumerating the chosen vectors and the normalized weak limit if nonzero, their pairwise inner products can be made bounded by 2^(−i−j−3) for distinct indices i,j≥1, inductively by weak convergence. The off-diagonal Gram matrix then has row sums below 1/2 and a uniform lower coefficient bound. The closed span M of the weak limit and the even deviations contains the selected images; the same lower bound applied against finite combinations in M makes odd deviations independent modulo M. Thus M is separable and M⊥ has infinite dimension. In either case there is an isometry V from M into M⊥. The single S=VP_M has norm one, is a partial isometry, and S²=0; on the selected near-norming subsequence ||SGx_n|| tends to one, proving m_G(SG)=1. For relative admissible pairs, ||z−Gx||≤√(2δ), and |⟨Sa,a⟩|≤||P_Ma||||P_{M⊥}a||≤||a||²/2; hence v_G(SG)≤1/2. In scalar output a phase-aligned z gives exactly ||Tx||, proving equality, and for G=I on ℂ² one recovers the classical sharp w(T)≥||T||/2. Replay: RESULT.md lines 25–56. VERIFICATION.md and checker.py were inspected, not run; numerical matrices cannot establish the subsequence lemma, and the script's scalar nonnegativity test alone would not establish equality.

## originality

PASS

The ordinary-norm upper bound and square-zero postcomposition idea are already in Kadets et al.; the finite-dimensional classification and several infinite-dimensional special cases also have direct exact catalogue coverage. The supported distinct contribution is one fixed norm-one square-zero partial isometry witnessing the m_G obstruction for each arbitrary G, including nonattainment, nonseparable Hilbert spaces and distinct domain/codomain. Neither the prior approximate family nor the checked special cases establishes this quantified statement. Priority beyond the inspected sources is not resolved.

## value

PASS

The fixed-factor theorem addresses the actual near-norming seminorm, where a varying family can become invisible and where the usual operator-norm index cannot classify spears. It gives an explicit geometric obstruction even without norm attainment and settles the Hilbert codomain question under the claimed assumptions; the sharp constant is meaningful even though the individual index need not equal it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
