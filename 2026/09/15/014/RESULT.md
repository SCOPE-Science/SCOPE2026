# Disproof of two-sided MBM wall-crossing for uniform J-stability on K3^[2]-type IHS varieties

## Context

The target proposed an explicit two-sided wall-crossing criterion for uniform J-stability on projective irreducible holomorphic symplectic (IHS) varieties of K3^[n]-type: slope uniform J-stability of a pair of Kaehler classes (alpha, beta), tested on all proper subvarieties, would be equivalent to an explicit Beauville-Bogomolov-Fujiki (BBF) inequality system indexed by MBM / prime-exceptional classes e, with walls at the hyperplanes e^perp; failure for some e would yield a destabilizing test configuration from the corresponding MMP contraction, and J-walls would coincide with MBM walls.

## Definitions

Let X = S^[2] where S is a smooth quartic K3 surface in P^3, so dim_C X = 4 and X is IHS of K3^[2]-type. Beauville decomposition: H^2(X,Z) = H^2(S,Z) + Z delta with q(delta) = -2, delta orthogonal to H^2(S). Let H in NS(X) be induced by H_S = c_1(O_S(1)) (Hilbert-Chow pullback), so q(H) = H_S^2 = 4, q(H,delta) = 0; write q(H) = 2d with d = 2. Let E be the Hilbert-Chow exceptional divisor; [E] = 2 delta. Consider the real plane P = span{H, delta} and the ray alpha(s) = H - s delta, beta = H - t0 delta with t0 = 1/k, k >> 1 integer. Slope uniform J-stability in the finite sense (*) is: for some epsilon > 0 uniform in Z, m (int_Z alpha^{m-1} beta)/(int_Z alpha^m) <= (2n - epsilon)(int_X alpha^{2n-1} beta)/(int_X alpha^{2n}) for every proper irreducible Z of dimension m. For a divisor Z = E this reduces to inequality (1) below.

## Result

The claimed two-sided equivalence and wall coincidence are false, already for n = 2 and divisorial destabilizers. The divisorial J-slope wall for E is an irrational quadric ray strictly inside the ample cone and coincides with no MBM wall e^perp (which meets P only in rational rays). J-stability changes along an ample segment meeting no MBM wall: (alpha(s),beta) is slope-destabilized by E for s below an interior wall s* in (0,t0), while (beta,beta) is slope uniformly J-stable. Hence no q_X-inequality system with walls at e^perp is equivalent to slope uniform J-stability, and J-walls do not coincide with MBM walls.

## Proof / evidence

Fujiki for K3^[2]-type: int_X gamma^4 = 3 q(gamma)^2. Polarizing gives int_X e alpha^3 = 3 q(alpha) q(e,alpha) and int_X e alpha^2 beta = q(alpha) q(e,beta) + 2 q(alpha,e) q(alpha,beta). Hence for Z = E with D = int_E alpha^3, N = int_E alpha^2 beta, 3N/D = 2 q(alpha,beta)/q(alpha) + q(e,beta)/q(e,alpha). With mu = q(alpha,beta)/q(alpha), slope semistability 3N/D <= 4 mu is q(e,beta)/q(e,alpha) <= 2 mu; the wall F = q(alpha)q(e,beta) - 2 q(alpha,beta)q(e,alpha) = 0 is a quadric cone, not a hyperplane. Scaling e = delta vs [E] = 2 delta cancels in ratios.

On P with e = delta: q(alpha) = 2(d-s^2), q(alpha,beta) = 2(d-s t0), q(alpha,e) = 2s, q(e,beta) = 2 t0. So F(s)/4 = t0 s^2 - 2 d s + t0 d =: G(s). For d = 2: G(0) = 2 t0 > 0 (violates even semistability near the MBM boundary s = 0), G(t0) = t0(t0^2-d) < 0 (passes). Roots satisfy s* s_big = d with s* = (d - sqrt(d(d-t0^2)))/t0 = 2k - sqrt(4k^2-2) in (0,t0) and s_big > t0 outside the cone; F' transverse at s*. s* is irrational: 4k^2-2 is never a square since (2k-1)^2 = 4k^2-4k+1 < 4k^2-2 < (2k)^2 for k >= 1.

Ampleness: H = HC^*A is nef (Hilbert-Chow pullback of ample); -E is HC-ample so H - eta E is ample for small eta > 0; beta = H - t0 delta with t0 = 1/k is ample for large k; each alpha(s) for 0 < s <= t0 is a positive convex combination of nef H and ample beta, hence ample (Kaehler). At alpha = beta, LHS = m <= 2n-1 = 3 and RHS = 4 - epsilon, so epsilon = 1 works uniformly: (beta,beta) is uniformly J-stable. Below s*, E violates even semistability, so (alpha(s),beta) is not uniformly J-stable. By continuity the zero s* is an interior J-slope wall.

No integral class matches it: for e' = D' + y delta in H^2(X,Z), q(e',alpha) = D'.H_S + 2 y s with D'.H_S in Z, so e'^perp cap P is all of P, empty, or the single rational ray s = -(D'.H_S)/(2y). Since s* is irrational, the J-wall meets P exactly at s* (and s_big outside) and coincides with no e'^perp. J-stability flips inside one ample chamber.

## Limitations

The disproof targets the slope (subvariety) formulation of uniform J-stability stated in the target, in particular its if-and-only-if and wall-coincidence clauses. It does not rule out a weaker one-sided divisorial instability criterion; indeed formula (1) is correct and useful. It does not compute analytic J-equation solvability beyond the slope picture. The counterexample uses K3^[2]-type with d = 2; a general-n computation shows the same quadric shape, but the written disproof needs only n = 2.

## Reproducibility

Run output/artifacts/fujiki_check.py (symbolic polarization check int a^2 b^2 = q(a)q(b) + 2q(a,b)^2, wall equation, discriminant, root location, transversality, numeric illustration) and output/artifacts/disproof_wall.py (locus-free algebra: F-sign table, s* s_big = d, interior J-wall vs endpoint MBM wall). Both reproduce s* = 4 - sqrt(14) ~= 0.258343 for d = 2, t0 = 1/2.

## References

- S. Boucksom, Divisorial Zariski decompositions on compact complex manifolds, Ann. Sci. ENS 2004.
- E. Markman, Prime exceptional divisors on holomorphic symplectic varieties and monodromy reflections, Duke Math. J. 2013 (arXiv:0912.4981).
- F. A. Denisi, Boucksom-Zariski and Weyl chambers on IHS manifolds, IMRN 2022; thesis Positivity on IHS manifolds 2023.
- Fujiki relation and Beauville lattice for S^[n]: standard; verified symbolically in artifacts.
