# Differential Galois group of a resonant symmetric doubly-confluent Heun boundary system is SL(2,C)

## Context

The admitted target fixes a traceless rank-2 meromorphic connection on P^1 with two unramified irregular singularities: Poincare rank 1 at x=0 and rank 2 at x=infinity. It is the symmetric point of the doubly-confluent Heun class with Am1=diag(1,-1), A2=diag(2,-2), A1=[[0,1],[1,0]], A0=diag(1/2,-1/2). The topic asked for a two-sided dichotomy: either an explicit Liouvillian solution with invariant line (reducible Borel case) or a Kovacic no-Liouvillian certificate plus a Stokes witness forcing irreducibility and hence SL(2,C). The second horn matters because the formal monodromy at 0 is the central scalar -I, so generic Ramis density arguments do not mechanically imply full monodromy and the point must be settled by hand.

## Definitions

System: dY/dx = M(x)Y with M(x) = A2 x + A1 + A0/x + Am1/x^2, i.e. with a(x) = 2x + 1/(2x) + 1/x^2, M(x) = [[a,1],[1,-a]], tr M = 0. The differential Galois group G over C(x) is an algebraic subgroup of SL(2,C). Write Y=(u,v); then u' = a u + v, v' = u - a v, so v = u' - a u and u'' = Q u with Q(x) = a^2 + a' + 1. Reducibility of the system over C(x) is equivalent to existence of a rational solution w of the Riccati equation w' + w^2 = Q (Kovacic Case 1). Kovacic Cases 2 and 3 correspond to dihedral/imprimitive and finite primitive projective Galois groups respectively; exclusion of all three gives Case 4 (no Liouvillian solution, connected Galois group SL(2,C)). At a rank-1 point with formal monodromy -I and Stokes matrices S1=[[1,s1],[0,1]], S2=[[1,0],[s2,1]], the loop monodromy satisfies tr(M_0) = -(2+s1*s2).

## Result

Theorem. For the system above, the differential Galois group over C(x) is the full group SL(2,C), not a proper reducible Borel subgroup. The scalar reduction u'' = Q u with Q = 4x^2 + 5 + 4/x - 1/(4x^2) - 1/x^3 + 1/x^4 admits no Liouvillian solution: Kovacic Cases 1, 2 and 3 are each impossible by exact tables (Case 1 degree values in {1/4,-9/4,-3/4,-13/4}; Case 2 single E-set row d=-3; Case 3 rows d=-2,-3,-6 for n=4,6,12). Independently, the loop monodromy at x=0 satisfies tr(M_0)+2 approx -262, so the Stokes product s1*s2 is nonzero; with the infinite exponential torus this independently forces irreducibility and hence G = SL(2,C).

## Proof / evidence

Scalar reduction: expanding a^2 + a' + 1 with a = 2x + 1/(2x) + 1/x^2 gives exactly Q = 4x^2 + 5 + 4/x - 1/(4x^2) - 1/x^3 + 1/x^4. Pole inventory: Q = s(x)/t(x) with s = 16x^6 + 20x^4 + 16x^3 - x^2 - 4x + 4 (degree 6), t = 4x^4 (degree 4); x^4 Q -> 1, x^5 Q -> 0, s(0) = 4 != 0, so the only finite pole is x=0 of order 4; o(inf) = deg(t)-deg(s) = -2 (ordinary point of Q). Gauge check: with P=[[1,0],[a,1]] and W=PY, W' = (P'P^{-1} + PMP^{-1})W equals exactly the companion [[0,1],[Q,0]], verified symbolically, so the reduction is exact.

Formal data at 0: leading matrix diag(1,-1) has distinct eigenvalues, hence unramified with two rank-1 blocks; system exponents +-1/2, scalar Frobenius indices {3/2,1/2}; formal monodromy is scalar -I on both sides. Correction retained from the draft: despite the topic phrase logarithmic formal type, there are no logarithm terms (leading part split, Riccati recurrence denominators 2*lambda*(k+3) never vanish); the genuine resonance is coincidence of both formal-monodromy eigenvalues at -1, which is central and cannot force irreducibility alone. Exponential torus: q = -/+1/x at 0 and -/+x^2 at infinity with distinct branches, a full 1-dimensional torus.

Case 1: seeking w = l/x^2 + m/x + ... at 0 and w = p x + q + t1/x + ... at infinity, R := w'+w^2-Q times x^4 gives coefficient conditions l^2-1=0 (x^0), 2lm-2l+1=0 (x^1), p^2-4=0 (x^6), 2pq=0 (x^5), yielding (l,m) in {(1,1/2),(-1,3/2)} and (p,q,t1) in {(2,0,3/4),(-2,0,-7/4)}. The degree d = t1-m takes values {1/4,-9/4,-3/4,-13/4}, none a nonnegative integer, so no rational Riccati solution exists; no invariant line over C(x); G is not Borel. All arithmetic is exact rational and was independently recomputed.

Cases 2 and 3 (Kovacic 1986): necessary-condition gates already fail for Cases 2 (needs a pole of order 2 or odd order >2; orders are {0:4, inf:0}) and 3 (needs all pole orders <=2 and o(inf)>=2; violated by order 4 and o(inf)=-2). E-sets: finite pole of order 4>2 gives E_0={4}; o(inf)=-2<2 gives E_inf={-2}. Case 2 (n=2): d=(e_inf-e_0)/2 gives single row (4,-2)->d=-3, inadmissible. Case 3: d=(n/12)(e_inf-e_0) gives d=-2 (n=4), -3 (n=6), -6 (n=12), all inadmissible. Permissive cross-check: over E_0 in {2,4} x E_inf in {-2,0,2} the only Case-2 d>=0 integer pair is (2,2),d=0 with theta=1/x, and the symmetric-square step-3 quantity S(1/x) = -32x-20/x-8/x^2-2/x^4+4/x^5 is exactly nonzero. Hence Case 4 holds: no Liouvillian solution, G^0 = SL(2,C), so G = SL(2,C).

Stokes corroboration: the relation tr(M_0) = -(2+s1*s2) is standard given F_hat=-I. Direct 50-digit fixed-step RK4 integration of the linear system around |x|=r gives tr(M_0) = -263.9932152548..., det = 1+8.6e-14, radius independence r=0.25,0.5,1.0 to 12+ digits, mesh convergence N=2000->4000 stable to 9 digits. Thus |tr(M_0)+2| approx 261.99, so s1*s2 != 0: both Stokes matrices are nontrivial opposite unipotents. By Ramis density the local group at 0 embeds into global G, so G contains opposite nontrivial unipotents plus an infinite torus; G is irreducible, not dihedral (which has no nontrivial unipotents), not finite (torus infinite), hence Zariski-dense in SL(2,C).

## Limitations

The exact core (reduction, pole inventory, formal data, Cases-1/2/3 tables, permissive step-3 check, Stokes relation, classification closing) is proved with exact rational arithmetic and machine-checked. The Stokes loop value is high-precision numerics with det/radius/mesh checks, not a formal interval-arithmetic enclosure; it is corroboration only since the Kovacic tables already prove G=SL(2,C) exactly.

## Reproducibility

Run python3 output/artifacts/kovacic_case2.py (exact Case-1 plus permissive step-3 certificate to kovacic_certificate.json and kovacic_stdout.txt); python3 output/artifacts/kovacic_cases23.py (Cases-2/3 tables and gates to kovacic_cases23.json); python3 output/artifacts/stokes_monodromy.py (loop monodromy to stokes_monodromy.json). Reference for the algorithm: J. J. Kovacic, An algorithm for solving second order linear homogeneous differential equations, J. Symbolic Computation 2 (1986) 3-43, DOI 10.1016/S0747-7171(86)80010-4.

## References

Kovacic 1986 (algorithm); DLMF 31.12 confluent Heun forms; Mitschi 1996 differential Galois groups of confluent generalized hypergeometric equations via Stokes multipliers; Duval-Loday-Richaud Kovacic applications to special functions; Buchstaber-Tertychny symmetries of a special doubly-confluent Heun equation; Levai potentials from BHE/DHE/THE.
