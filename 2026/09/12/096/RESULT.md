# Length-decision for the Z/3 cover of the Q5 theta (2,1,3)

## Context

Let K = Q_5 with |x| = 5^{-v_5(x)}. Let X_0/K be a genus-2 Mumford curve, i.e. X_0^{an} = (P^1 \ Lambda)/Gamma_0 for a rank-2 Schottky group Gamma_0 subset PGL_2(K). Its minimal Berkovich skeleton Gamma is a theta graph (two vertices, three parallel edges). Let phi_0: Gamma' -> Gamma be the connected cyclic Z/3 unramified topological triple cover, so V' = 6, E' = 9, b_1(Gamma') = 1-(6-9) = 4, matching genus 4 via Schreier 1+3(2-1) = 4. Equip Gamma' with the incompatible metric assigning length 1 to every edge (total length 9). The admitted target question: does phi_0 arise as the skeleton of a finite etale cover X' -> X_0 of degree 3 by a Mumford curve X' of genus 4 uniformized by an index-3 subgroup of Gamma_0? A complete answer either constructs such a cover or proves none exists, including under skeleton refinement.

## Definitions

- Schottky group: free discrete subgroup of PGL_2(K) pairing 2g disjoint closed discs; quotient is a Mumford curve of genus g.
- Berkovich skeleton: minimal metric-graph retract of X^{an}; edge lengths measured in the additive tree metric normalized so d(zeta_{0,1}, zeta_{0,5^{-1}}) = 1.
- Finite etale cover of skeleta: harmonic morphism of metric graphs with all local dilation factors d_{e'} = 1 (no ramification); lifted edge length equals pullback length l(e') = l(phi(e)).
- Admissible refinement: subdivision of edges; total metric length is preserved.

## Result

Put q_A = 125, q_B = 625 (v_5 = 3, 4) and

A = [[125,0],[124,1]], B = [[-1245,6240],[-624,3123]] in PGL_2(Q_5).

Then Gamma_0 = <A,B> is Schottky of rank 2 with pairing discs D_1 = Bbar(1,5^{-1}), D_2 = Bbar(2,5^{-1}), D_3 = Bbar(0,5^{-2}), D_4 = Bbar(5,5^{-3}); X_0 = quotient is a genus-2 Mumford curve with minimal skeleton the theta graph of unordered edge lengths {1,2,3}. The connected cyclic Z/3 topological triple cover with all nine edges of length 1 (total 9) does NOT arise as the skeleton of any degree-3 finite etale Mumford cover: the etale pullback metric forces total length 3*(1+2+3) = 18, and 18 != 9 persists under every admissible subdivision. Hence no index-3 subgroup of Gamma_0 induces phi_0.

## Proof / evidence

Schottky certification (exact rational arithmetic, machine-checked in output/artifacts/verify.py). Centers {1,2,0,5} satisfy |c_i-c_j| = 1 except |0-5| = 5^{-1}, while radii are 5^{-1},5^{-1},5^{-2},5^{-3}; ultrametric inequality gives six pairwise disjoint discs (D_3 vs D_4: separation 5^{-1} strictly exceeds max radius 5^{-2}). Poles: A pole -1/124 lies strictly inside D_1 (distance valuation 3 > 1); A^{-1} pole 125/124 strictly inside D_3 (v = 3 > 2); B pole 1041/208 strictly inside D_2 (v = 4 > 1); B^{-1} pole 415/208 strictly inside D_4 (v = 4 > 3). Fixed points A(0)=0, A(1)=1 with multiplier A'(0) = 125; B(2)=2, B(5)=5 with multiplier B'(5) = 625. Radius-multiplier identities |q_A| = 5^{-3} = 5^{-1}*5^{-2} and |q_B| = 5^{-4} = 5^{-1}*5^{-3} with |c_+-c_-| = 1 satisfy the Gerritzen-van der Put disc criterion. Spot valuations confirm ping-pong: A(6) = 150/149 boundary-to-boundary, A(2) interior, A^{-1}(25) boundary, B(7) = 165/83 boundary of D_4, B(0), B(1) interior, B^{-1}(130) boundary. Hence generators are free, Gamma_0 is Schottky rank 2, X_0 is Mumford genus 2.

Skeleton lengths: with u = zeta_{0,1}, v = zeta_{0,5^{-1}}, bridge l(u,v) = 1; arms l to disc boundaries 1,1,1,2 respectively; quotient gives loop edges e_A = 1+1 = 2 (A-pair), e_B = 1+2 = 3 (B-pair), plus bridge e_0 = 1: unordered {1,2,3}. Cross-check: translation lengths v_5(q_A) = 3 = e_A+e_0, v_5(q_B) = 4 = e_B+e_0.

Obstruction: for etale (d = 1) covers each lifted edge inherits l(e') = l(phi(e)); above each base edge of length l in {1,2,3} the three lifts each have length l. Total pullback length = 3*(1+2+3) = 18 versus target 9*1 = 9. Subdivision preserves totals, and metric-graph isometry preserves total length, so no isometry exists under any refinement; per-edge, above the length-3 edge lifts have length 3 != 1. This rules out every index-3 subgroup without enumeration.

## Limitations

Impossibility applies only to finite etale (unramified, dilation 1) covers as specified; ramified covers with nontrivial dilation are not addressed. The ping-pong uses the standard disc criterion plus exact spot valuations, not a formalized proof-assistant Berkovich certificate.

## Reproducibility

Run python3 output/artifacts/verify.py (exact Fraction arithmetic, no floating point): checks determinants, fixed points, multipliers, six disjointness valuations, four pole containments, multiplier/radius identities, ping-pong spot checks, theta edges, cover combinatorics, 18 != 9, Schreier rank. All checks pass.

## References

- L. Gerritzen, M. van der Put, Schottky Groups and Mumford Curves, LNM 817, 1980.
- M. van der Put, Etale coverings of a Mumford curve, Ann. Inst. Fourier 33(1), 1983.
- O. Amini, M. Baker, E. Brugalle, J. Rabinoff, Lifting harmonic morphisms I: metrized complexes and Berkovich skeleta, 2015; and part II: Tropical curves and metrized complexes, 2015.
- M. Chan, Tropical hyperelliptic curves, 2012.
- M. A. Cueto, H. Markwig, Tropical geometry of genus two curves, 2018.
