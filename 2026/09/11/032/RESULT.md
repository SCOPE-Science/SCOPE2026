# Explicit Fibonacci Cilleruelo-cluster scarred witnesses blocking Planck-scale mass equidistribution on the flat 2-torus

## Context

Let T^2 = R^2/Z^2 with Laplacian eigenfunctions e_nu(x) = e^{2 pi i nu.x},
nu in Z^2. The eigenspace E(N) = span{e_nu : |nu|^2 = N} has eigenvalue
4 pi^2 N. A central question in quantum ergodicity on the torus is whether
L^2 mass equidistributes at the Planck (wavelength) scale rho ~ 1/sqrt(eigenvalue).
Density-one and window-averaged results (Lester-Rudnick, Hezari-Riviere,
Granville-Wigman) tolerate sparse exceptional sequences; classifications of
possible Planck limits (Sartori) and universal unspecified-constant failures
(Han) name no explicit coherent witness with a certified constant.
Cilleruelo-Granville (Canad. J. Math. 61(6), 2009) classify 4 lattice points
on short arcs of circles and give an infinite Fibonacci family, but state no
eigenfunction, center, radius, or mass ratio.

## Definitions

Let F_m be the Fibonacci numbers (F_0 = 0, F_1 = 1). For integer n >= 2 define

  base_n = (1/2)(F_{3n+3}, F_{3n}),
  z_1(n) = (-2 F_{n-1}, 2 F_{n+2}),  z_2(n) = (-F_{n-2}, F_{n+1}),
  z_3(n) = (F_{n-1}, -F_{n+2}),     z_4(n) = (F_n, -F_{n+3}),
  nu_{j,n} = base_n + (-1)^n z_j(n).

Put N_n = (5/2) F_{2n-1} F_{2n+1} F_{2n+3} (an integer), R_n = sqrt(N_n),
psi_n = (1/2) sum_{j=1}^4 e_{nu_{j,n}} (L^2-normalized),
lambda_n = 2 pi R_n, rho_n = 1/lambda_n (Planck radius), x_n = 0,
and M(psi,x,rho) = (pi rho^2)^{-1} int_{B(x,rho)} |psi|^2.

## Result

For every n >= 2 the points nu_{j,n} are four distinct lattice points with
|nu_{j,n}|^2 = N_n, lying in an arc of length at most 15 R_n^{1/3}.
With x_n = 0,

  M(psi_n, 0, rho_n) >= 2.734 > 1.1 for all n >= 2,

and in fact M -> 4 as n -> infinity. Hence Planck-scale mass
equidistribution fails along this explicit sparse scarred sequence.
In particular the n = 2 instance nu = (15,10),(17,6),(18,1),(18,-1),
N = 325, R* = sqrt(325), psi* = (1/2) sum e_{nu_j}, x* = 0,
r* = 1/(2 pi sqrt(325)) satisfies M >= 2.734 >= 1.1 with arc <= 10 (R*)^{1/3}.

## Proof / evidence

Norm and distance identities: 4|nu_{j,n}|^2 - 10 F_{2n-1}F_{2n+1}F_{2n+3} = 0
and the six squared distances
|d_12|^2 = 10 F_{2n-1}, |d_13|^2 = 18 F_{2n+1}, |d_14|^2 = 10 F_{2n+3},
|d_23|^2 = 2 F_{2n+3}, |d_24|^2 = 10 F_{2n+1}, |d_34|^2 = 2 F_{2n-1}
are exact Laurent-polynomial identities in u = phi^n over Q(sqrt(5)) via
Binet's formula, proved by exact coefficient comparison for both parities
(output/artifacts/laurent_cert.py -> LAURENT_CERT_OK), cross-checked in exact
integer arithmetic for n = 2..27 (output/artifacts/verify_target.py -> VERIFY_OK).

Mass bound: at x = 0 all phases align,
|psi_n(y)|^2 = (1/4) sum_{j,k} cos(2 pi d_{jk}.y).
Disc averaging with cos t >= 1 - |t| and disc mean radius 2 rho/3 gives each
off-diagonal average >= 1 - (2/3)(|d|/R_n). Since
(cmax/R_n)^2 = 10 F_{2n+3}/N_n = 4/(F_{2n-1}F_{2n+1}) <= 2/5 < 0.633^2,
every off-diagonal term is >= 0.578, so
M >= (1/4)(4 + 12 x 0.578) = 2.734. As F grows exponentially, |d|/R_n -> 0
and M -> 4.

Short arc: largest chord squared is 10 F_{2n+3}. From F_{m+1} <= 2F_m and
F_{m+2} <= 3F_m one gets chord^6/R_n^2 <= 10800 <= 4.71^6 (exact integer
check), so chord <= 4.71 R_n^{1/3}; a set of diameter delta on a circle lies
in an arc <= (pi/2) delta < 15 R_n^{1/3}. The n = 2 datum is verified by hand
(norm 325, max chord sqrt(130), arc margin ~9.7x in sixth powers).

## Limitations

Uses the Fibonacci subfamily of Cilleruelo-Granville (not all 4-point
families); center fixed at x_n = 0; arc constant 15 is not sharp; mass bound
2.734 is not the limit 4. Finite integer audit covers n = 2..27 as a
cross-check; full generality rests on the exact Laurent-polynomial certificate.

## Reproducibility

- python3 output/artifacts/laurent_cert.py -> LAURENT_CERT_OK (stdlib only)
- python3 output/artifacts/verify_target.py -> VERIFY_OK (stdlib only)
- Lattice source: Cilleruelo-Granville, Close Lattice Points on Circles,
  Canad. J. Math. 61(6) (2009), 1214-1238, Sec. 1.

## References

- Cilleruelo, Granville, Close Lattice Points on Circles, doi:10.4153/cjm-2009-057-2
- Lester, Rudnick, Small scale equidistribution of eigenfunctions on the torus, arXiv:1508.01074
- Granville, Wigman, Planck-Scale Mass Equidistribution of Toral Laplace Eigenfunctions, doi:10.1007/s00220-017-2953-3
- Sartori, Mass distribution for toral eigenfunctions via Bourgain's de-randomization, doi:10.1093/qmathj/haz029
- Han, From nodal points to non-equidistribution at the Planck scale, doi:10.5802/crmath.311
- Wigman, Yesha, CLT for Planck scale mass distribution, arXiv:1712.03318
