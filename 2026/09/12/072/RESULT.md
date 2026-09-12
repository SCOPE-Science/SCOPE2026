# Parameterized Picard-Vessiot group of the Kummer operator xY''+(1/2-x)Y'-tY

## Context

Let C be algebraically closed of characteristic 0 and F = C(t,x) with commuting
derivations dx(x)=1, dx(t)=0, dt(x)=0, dt(t)=1, where t is transcendental over C.
Consider the Kummer confluent-hypergeometric operator

  L = x*dx^2 + (1/2-x)*dx - t,

i.e. the companion system dx Z = A Z with A = J + K/x,
J = [[0,1],[0,1]], K = [[0,0],[t,-1/2]].
The target (TARGET route, no preset fallback) is the PPV trichotomy for generic
t: (A) reducible Borel, (B) infinite imprimitive dihedral, or (C) Zariski-dense
differential-algebraic subgroup of GL2/SL2 with explicit dt-equations and the
isomonodromic versus non-isomonodromic verdict across x=0 (regular singular)
and x=infinity (rank-one irregular).

## Definitions

- Normalized (SL2) form: gauge Y = u*exp(-int b/2) with b=(1/2-x)/x sends
  L = x(D^2+bD+c), c=-t/x, to u'' = r u with
  r = b^2/4 + b'/2 - c = 1/4 + (t-1/4)/x - 3/(16x^2).
- Kovacic case 1 data: at x=0 (order-2 pole, coeff b0=-3/16),
  discriminant 1+4b0=1/4, alpha_0 in {3/4,1/4}; at infinity (order 0,
  [sqrt(r)] = +-1/2), alpha_inf in {t-1/4,-(t-1/4)};
  d-values d = alpha_inf - alpha_0 in {t-1, t-1/2, -t-1/2, -t}.
- Sym^2 equation for u''=r u: w'''-4r w'-2r' w=0; dihedral case (B) holds iff
  it admits a nonzero rational solution w in C(t,x).
- Isomonodromy in the Schlesinger sense: existence of rational
  B in M2(C(t,x)) with dt A - dx B = [B,A].

## Result

For transcendental t, exactly case (C) holds for generic t. The normalized
equation has classical (Zariski) Galois group SL2, and its parameterized
Picard-Vessiot group is the full differential-algebraic group SL2, defined by
the single equation det(g)=1 with NO further dt-polynomial equations
(differential dimension 3, Zariski-dense); the family is non-isomonodromic in t
across x=0 and x=infinity. For the original companion system this is GL2 with
the same projective/derived SL2 picture up to the known scalar determinant
character (tr A = 1-1/(2x)). Supporting fiber data: d in N forces a rational
Riccati solution only when t makes one of t-1, t-1/2, -t-1/2, -t a nonnegative
integer; verified Liouvillian witnesses: t=0: Y=1; t=-1/2: Y=sqrt(x);
t=1/2: Y=e^x; t=1: Y=e^x*sqrt(x)-type; t=-1: Y=x-1/2. Generic t admits no
rational Riccati solution, no nonzero rational Sym^2 solution, and no rational
Lax matrix.

## Proof / evidence

1. Normal form: direct gauge computation gives r above (machine-checked).
2. Irreducibility (excludes A): a rational Riccati solution requires some
   d-value in N; for transcendental t none of t-1, t-1/2, -t-1/2, -t lies in N.
   Hence no rational Riccati solution over C(t,x) for generic t.
3. Non-dihedral (excludes B): for the Sym^2 equation, a pole at a != 0 needs
   m<0 with m(m-1)(m-2)=0, impossible; at x=0 the indicial equation is
   m(m-1)(m-2)+(3/4)m-3/4 = (m-1)(2m-1)(2m-3)/4 with roots {1,1/2,3/2}, so no
   pole; at infinity w=c*x^d, d>=1 gives leading term -d*c*x^{d-1} != 0 from
   -4r w', so d<=0 and w is constant c, whence -2r' c=0 with r' != 0 forces
   c=0. No nonzero rational Sym^2 solution for generic t.
4. Infinitude: x=infinity is irregular of rank one with leading part J of
   distinct eigenvalues {0,1}, so formal solutions involve distinct exponentials
   e^{0}, e^{x}; the exponential torus is nontrivial and Stokes data is
   nontrivial, forcing an infinite group and excluding finite primitive
   (Kovacic case 3, whose exponent data is incompatible with moving
   alpha_inf= +-(t-1/4) at transcendental t). Irreducible + non-dihedral +
   infinite gives classical group SL2 (Kovacic trichotomy).
5. Full PPV group (non-isomonodromy): there is no rational Lax matrix.
   Indeed dt A = E/x, E=[[0,0],[1,0]]. Write B rational in x. Pole at 0:
   top polar coefficient satisfies a nonzero combination of k*Id and ad_K whose
   eigenvalues are k, k, k+-1/2 (ad_K eigenvalues {0,0,+-1/2}), never 0 for
   integer k>=1, so B has no pole at 0. Top degree d>=1: with
   Bd=beta*(J-I/2) in the centralizer of J, the residual
   S = +-(d*Bd-[Bd,K]) must lie in image(ad_J)={M:M11=M21}, but
   S11-S21 = -+beta*d/2, forcing beta=0; hence deg B <= 0. Constant term
   B0=aI+bJ gives [B0,K]-E with (1,2)-entry -b/2 and (2,1)-entry b*t-1,
   with no common zero for transcendental t. Hence no rational B exists, so the
   family is not isomonodromic; with Zariski-dense classical group the PPV
   correspondence (Cassidy-Singer / Arreche-Dreyfus-Roques / Dreyfus-Schumann-
   Sauloy-Zhang theory for irregular confluent equations) forces the PPV group
   to be full SL2 with no extra dt-equations. The Stokes jump (moving formal
   exponent 1/4-t at infinity) corroborates non-isomonodromy. Corrected sign
   note: intermediate write-ups may state k*Id+ad_K vs -k*Id-ad_K or
   S:=d*Bd-[Bd,K] vs its negative; both conventions give nonzero data and gap
   +-beta*d/2, so the vanishing conclusion is unchanged as machine-checked.

## Limitations

- GL2-companion versus SL2-normalized determinant bookkeeping is standard gauge
  theory, stated without re-deriving the full PPV correspondence.
- Classical infinitude uses the standard exponential-torus/Stokes consequence
  of the rank-one irregular point rather than a line-by-line Kovacic case-3
  polynomial search.
- Stokes matrices at infinity are cited as corroboration, not re-proved.
- Special-fiber census beyond the verified instances t in {0,-1/2,1/2,1,-1} is
  d-necessity plus degree 0-3 rank evidence; only the verified instances and
  the necessity pattern are claimed, which suffices for the generic-t verdict.

## Reproducibility

Run python3 verify_kummer.py (copied to output/artifacts/): checks normal form
r, Kovacic d-values, the five special solutions L(Y)=0, Sym^2 indicial
factorization, K eigenvalues {0,-1/2} with ad_K char poly l^2(l^2-1/4),
centralizer(J), image(ad_J) condition M11=M21, residual gap -beta*d/2, and the
[B0,K]-E entries -b/2, b*t-1. Expected: ALL CHECKS PASSED.

## References

- Cassidy-Singer, parameterized Picard-Vessiot theory; isomonodromic iff PPV
  group is conjugate to constants (regular-singular case).
- Arreche (arXiv:1208.2226; ISSAC 2014; JSC 2016) and Dreyfus (Proc. AMS 2014;
  HAL hal-01897284): algorithms for PPV groups of second-order parameterized
  equations extending Kovacic; integrability criterion when no Liouvillian
  solutions exist.
- Mitschi (Pacific J. Math. 1996): classical Galois groups of confluent
  generalized hypergeometric equations via Stokes multipliers.
- Mitschi-Singer (arXiv:1002.2005v5): projective isomonodromy; derived-group
  condition; regular-singular hypotheses stated therein.
- Minchenko-Ovchinnikov-Singer (IMRN 2015): reductive linear differential
  algebraic groups and PPV computation.
- Standard: Kummer/Whittaker connection formulas; Ramis and van der Put-Singer
  formal/inverse theory at irregular singularities; Kovacic algorithm.
