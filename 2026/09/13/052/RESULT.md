# Disproof of the quantitative s-to-1 fractional-bubble rate claim

## Context

The target asks for explicit constants C>0, beta>0, s0 in [3/4,1) such that
every fractional two-chamber minimizer is L1-close to the classical
equal-volume standard double bubble D0 with polynomial energy rate
|(1-s)m_s - omega P0| <= C(1-s)^beta. A rigorous violation of every such
polynomial energy rate is an explicitly allowed complete resolution.

## Definitions

For 0<s<1 and measurable E subset R^3, P_s(E)=int_E int_{R^3\E}|x-y|^{-3-s}dxdy.
For disjoint chambers, F_s(E1,E2)=P_s(E1)+P_s(E2), m_s=inf{F_s:|E1|=|E2|=1}.
P is classical perimeter, omega>0 the Bourgain-Brezis-Mironescu constant with
(1-s)P_s->omega P on fixed smooth sets, D0 the equal-volume standard double
bubble, T=classical sum-perimeter of two disjoint unit balls,
S0=its sum energy, C0=its cluster energy.

## Result

The target claim is FALSE. With T=2(36pi)^{1/3},

  lim_{s->1-} (1-s) m_s = omega T,

while |T-P0|>=0.47 for either reading P0 in {S0,C0}: S0-T>=0.47, T-C0>=0.50.
Hence |(1-s)m_s-omega P0|->omega|T-P0|>=0.47 omega>0, so every polynomial
energy rate fails for every C, beta, s0. The joint conjunction is falsified.

## Proof / evidence

Upper bound: two fixed disjoint unit balls (B,B') are admissible, so
m_s<=2P_s(B) and BBM-Davila gives limsup (1-s)m_s<=2 omega P(B)=omega T.
Lower bound: sharp fractional isoperimetric inequality applied per chamber
gives P_s(G)>=c_{3,s}|G|^{(3-s)/3} with balls attaining c_{3,s}; for |Ei|=1,
(1-s)F_s>=2(1-s)c_{3,s}. Since c_{3,s}=P_s(B) for a unit ball,
(1-s)c_{3,s}=(1-s)P_s(B)->omega(36pi)^{1/3}, so liminf (1-s)m_s>=omega T.
No compactness, existence, or regularity of s-minimizers is used.
Classical gap: unit-ball radius r^3=3/(4pi) gives T^3=288pi. Equal-volume
double-bubble geometry (interface angle 120 deg, disc radius a sqrt3/2, cap
height 3a/2, a^3=8/(9pi)) gives S0=15pi a^2/2, C0=27pi a^2/4, hence
S0^3=1000pi/3, C0^3=243pi, (S0/T)^3=125/108, T^3-C0^3=45pi. Rational bounds
with 3.14<pi<22/7 yield S0-T>=0.47 and T-C0>=0.50, machine-checked.

## Limitations

Proves energy-rate falsification only; no L1 (non-)convergence of chambers or
fractional minimizer classification is claimed. The lower constant bound uses
ball optimality under BBM normalization as a standard quoted result. Concerns
exactly the sum functional F_s, not a fractional cluster functional.

## Reproducibility

Run output/artifacts/verify_gaps.py; expect ALL CHECKS PASSED with the exact
identities and rational gap bounds above.

## References

Bourgain-Brezis-Mironescu 2001; Davila 2002; Ambrosio-De Philippis-Martinazzi
2011 (Gamma-convergence of nonlocal perimeters); Frank-Lieb-Seiringer sharp
fractional isoperimetric inequality; Maggi Ch.14; Hutchings-Morgan double
bubble (cluster context only).
