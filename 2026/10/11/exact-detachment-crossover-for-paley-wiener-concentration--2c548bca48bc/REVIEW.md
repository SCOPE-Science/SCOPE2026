# Mathematical review: Exact detachment crossover for Paley–Wiener concentration

## Correctness

The claimed law holds for a fixed interval length s>0 and a joint limit epsilon->0, epsilon<=b->0. With r=s/2 and u_s the squared normalized first prolate function, the centered weighted discrepancy is exactly

D_0(E_{epsilon,b}) = integral from r-epsilon to r, integral from 0 to b, of -u_s'(x+t) dt dx.

The strict endpoint slope gives D_0=-u_s'(r)epsilon*b(1+o(1)). The interval mass profile has unique maximizing center zero with curvature 2u_s'(r)<0. A first-derivative perturbation of order epsilon*b shifts its maximizing center by O(epsilon*b), changing the optimized mass by only O(epsilon^2*b^2). The published comparison 0<=D(E)-eta(E)<=A_s D(E)^2 then transfers the sharp leading term to the spectral deficit. The proof is analytic and does not rely on finite sampling.

## Originality

The 2026 Paley–Wiener stability theorem of Denis Zelent already introduces this exact family, supplies the weighted discrepancy and quadratic spectral comparison, and gives two order examples. The exact joint vanishing-displacement coefficient is not stated there. The mathematical addition is narrowly the recentering-sensitive two-scale asymptotic, not a new global concentration or stability theorem. This short deduction depends heavily on existing work; an unindexed equivalent corollary remains a priority risk.

## Mathematical value

The canonical detached-piece example demonstrates that ordinary symmetric difference does not measure displacement. The sharp coefficient identifies how local loss depends on moved length times distance and supplies a precise benchmark across the adjacent and mesoscopic regimes. No fixed-displacement coefficient, second-order expansion, or new general set-stability theory is claimed.

## References

- Denis Zelent, *Stability of concentration in the Paley–Wiener space*, arXiv:2610.01299v1 (2026), especially the detached example, Proposition 1 and equation (21).
- Luís D. Abreu and Michael Speckbacher, *Optimal concentration in the Paley–Wiener space*, arXiv:2607.19192v1 (2026), Theorem 1.1.
- Classical prolate spheroidal analysis of Slepian, Landau, and Pollak, as used in the cited stability theorem.
