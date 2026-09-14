# Inside-Voigt-Reuss Certified Enclosure of a_hom for i.i.d. Uniform-[1/2,2] Conductances on Z^2

## Context
Consider the 2D nearest-neighbour random conductance model on Z^2 with independent edge conductances uniform on [1/2,2]. Qualitative stochastic homogenization (Kozlov; Papanicolaou-Varadhan) yields an infinite-volume homogenized matrix A_hom. By rotation/reflection invariance of the law, A_hom = a_hom I for a scalar a_hom. The classical Voigt-Reuss bounds are E[a]=5/4=1.25 (Voigt) and 1/E[1/a]=3/(4 ln 2)≈1.082 (Reuss). The admitted target asked for a rigorous proof that a_hom lies in [1.10,1.20] strictly inside Voigt-Reuss, or a rigorous exclusion.

## Definitions
- Omega=[1/2,2]^{E(Z^2)} with product uniform measure; tau_x lattice shifts; a_i(x,omega) stationary edge conductances.
- m=E[a]=5/4, m2=E[a^2]=7/4, v=3/16.
- s=1/a reciprocal conductance with E[s]=(4/3)ln2=:mu, E[s^2]=1, E[s^3]=5/4.
- D_i F = F o tau_{e_i} - F stationary gradient.

## Result
A_hom = a_hom I with

  1000/889 <= a_hom <= 119/100,

i.e. approximately 1.12486 <= a_hom <= 1.19. In particular 1.10 <= a_hom <= 1.20, and [1000/889,119/100] lies strictly inside the Voigt-Reuss interval [1/E[1/a],E[a]].

## Proof / Evidence
Upper bound: stationary variational principle e1.A_hom e1 <= E[a1(0)(1+D1 F)^2+a2(0)(D2 F)^2] for mean-zero local F. With psi=c0 a1(0)+c1 a1(-e1), c0=4/25, c1=-4/25, independence and vanishing third central moment of the symmetric uniform law give linear part -3/25, D1 quadratic 9/250, D2 quadratic 3/125, hence J=5/4-3/25+9/250+3/125=119/100, so a_hom<=119/100.

Lower bound: 2D Keller-Dykhne duality a_hom(a).a_hom(1/a)=1 for bounded rotation-invariant laws. Single-site dual test psi_s=p s1(0), p=1/4, gives a_hom(s)<=P(mu) with P(mu)=-mu^3/8+mu^2/2+17mu/16-27/64. Certified ln2 in [0.6931,0.6932] via 4-term atanh(1/3) series S3=53056/76545 with remainder<=1/78732 yields mu in [6931/7500,1733/1875] subset [0.92,0.93]. Since P'>1.65 there, P(mu)<=P(1733/1875)=374876538179/421875000000<889/1000, so a_hom(s)<=889/1000 and a_hom(a)>=1000/889>1.10.

Strict inclusion: 1000/889>11/10>Reuss and 119/100<5/4=Voigt by integer cross-products. All numerics are exact rational arithmetic rechecked by output/artifacts/verify.py (Fraction class, ALL EXACT CHECKS PASSED). No Monte Carlo used.

## Limitations
Certifies the interval [1000/889,119/100], not the sharp value; test functions are non-optimal by design. Isotropy and 2D duality are used in standard qualitative-homogenization form for bounded ergodic media with textbook proofs cited. Computation confined to exact rational checks.

## Reproducibility
Run `python3 output/artifacts/verify.py`; it rechecks primal J, S3 and ln2 inequalities, P(mu_hi), monotonicity bound 132653/80000, and all strict-inclusion cross-products.

## References
Kozlov 1979; Papanicolaou-Varadhan; Bensoussan-Lions-Papanicolaou; Armstrong-Kuusi-Mourrat quantitative stochastic homogenization; Keller-Dykhne 2D duality; Luck 1991 weak-disorder expansion (prior, non-covering); Alessandrini-Nesi 2D bounds (periodic, non-covering); Colecchio et al. 2025 RRN simulations (lognormal, non-covering).
