# Scientific review

## Correctness — PASS

The squarefree-discriminant criterion isolates precisely the omitted parameters. An explicit Cartier matrix computed from \((x^{10}+ax^5+1)^3\) gives determinant \(3a^2(a^2+1)^2\) and rank exactly two on its three roots; the two-step semilinear product vanishes there, so the \(7\)-rank is zero. Two explicit smooth genus-two quotients generate the genus-four Jacobian up to prime-to-seven isogeny. Their zero-rank Jacobians are supersingular abelian surfaces, proving that the exceptional genus-four Jacobians are supersingular rather than merely of rank zero. The standalone script replays the coefficient identities and a finite-field check, while the proof covers the entire algebraic closure.

## Originality — PASS, with historical risk

Van Geemen–Schütt (arXiv:1010.3897, §§3.4–3.5) already identified the same characteristic-zero hyperelliptic order-five family; they did not state these characteristic-seven Cartier determinants or exceptional Newton polygons. Harvey–Sutherland (arXiv:1410.5222) supplies the general matrix formula, not this family's full stratification. Kudo–Harashita (arXiv:1607.01114) excludes superspecial genus-four curves at \(7\), which neither implies nor excludes the exhibited supersingular non-superspecial specializations. Queries using alternative parametrizations and stronger invariants did not uncover equivalent coverage. Historical priority remains uncertain, especially for arithmetic work on cyclic-five covers or the Dwork pencil not accessible in full.

## Mathematical value — PASS

This is a full Newton-polygon classification of a natural one-parameter family appearing in genus-four Shimura-moduli studies, not a lone computational example. It locates the entire zero-rank and supersingular locus, gives its nonreduced Hasse divisor and constant exceptional \(a\)-number, and explains the dichotomy geometrically via two genus-two quotients. It supplies explicit supersingular-but-not-superspecial genus-four examples precisely in the characteristic where no superspecial genus-four curve exists.

## Boundaries and verification status

No claim of a general genus-four classification, exceptional-fiber isomorphism classification, or complete \(7\)-torsion group-scheme classification is made. Closest primary prior sources are listed in `RESULT.md`; uninspected historical arithmetic computations remain the chief originality risk.

Self-review: passed. Independent audit: not yet performed.
