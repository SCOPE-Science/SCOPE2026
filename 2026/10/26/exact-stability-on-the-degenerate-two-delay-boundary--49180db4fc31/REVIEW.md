# Scientific review: exact stability on the degenerate two-delay boundary

## Correctness — PASS

The characteristic frequency polynomial has a unique positive double root on the stated locus. The phase equations give exactly the delays in (3). At every such delay the characteristic root is simple because \(f_\lambda=1+2c\tau_n>0\). Implicit differentiation gives the exact second derivative (4), whose sign is strictly negative. Thus the root pair remains in the left half-plane on both sides of each contact. The bound \(|\lambda+a|\le |b|+|c|\) for roots with nonnegative real part rules out entry from infinity; small-delay stability and the complete imaginary-root list then establish the global root-count claim. The symbolic checker is supplementary to this proof.

## Originality — PASS, best-knowledge assessment

Hata–Matsunaga (2022) explicitly identify this exact discriminant-zero/positive-double-frequency case as excluded from their explicit stability criteria. Their Lemma 2.3 identifies the repeated frequency and their imaginary-root lemmas identify the critical-delay sequence, but the stated theorems do not classify stability on the excluded locus. The new comparison is the second-order root-contact calculation and the resulting necessary-and-sufficient asymptotic-stability criterion. Bortz's inspected full text develops root-series approximations for general two-lag equations; it does not state this exact stability classification. Li–Ruan–Wei's inspected paper treats a different linearization without the same instantaneous coefficient and does not imply this result. published-finding corpus searches returned related delay-crossing work for different characteristic equations, not this boundary theorem. Search failure is not proof of uniqueness.

## Mathematical value — PASS

This resolves an explicit boundary case left outside a published necessary-and-sufficient criterion. The practical distinction is structural: coalescing frequency roots need not create a stability-switch interval; here the critical conjugate pair is tangent to the imaginary axis from the stable side, and only the isolated critical delays fail asymptotic stability. This prevents a false instability interval being inferred from nearby parameter scans.

## Closest literature and residual limitations

- Hata and Matsunaga (2022), DOI 10.7494/OpMath.2022.42.5.673: same equation; explicitly excludes the exceptional case from its main stability theorems.
- Mahaffy and Busken (2015), DOI 10.3934/dcds.2015.35.4955: the same normalized delay ratio \(R=1/2\) is included in a broad D-partitioning analysis, and the paper discusses geometric tangencies. The inspected conclusions do not state the exact necessary-and-sufficient criterion along this coefficient ray; this is the strongest residual implication risk.
- Bortz (2012 preprint; 2016 journal version), arXiv:1206.6364: general two-lag root-series method; inspected full HTML text, not a closed-form exceptional-locus stability theorem.
- Li, Ruan, and Wei (1999), DOI 10.1006/jmaa.1999.6418: broad two-delay stability and bifurcation analysis, but the inspected main linearized family differs from (5).
- published-finding corpus near-matches concern other delay systems or double-Hopf points. No exact same-equation match was returned; an unindexed equivalent analysis remains a priority risk.

Self-review: passed. Independent audit: not yet performed.
