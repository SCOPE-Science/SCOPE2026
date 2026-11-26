# Independent mathematical audit

## correctness

PASS

Eliminating the inner ring from the two modulo-n quiet equations and multiplying by T^(k+1) gives F_k as in RESULT.md. Expansion over F_2 gives (t+1)^(2^(k−1)) Φ_5(t), with Φ_5 irreducible since 2 has order four modulo 5. In F_2[t]/(t^n+1) the kernel dimension is the gcd degree; the Φ_5 factor occurs precisely when 5 divides n and the (t+1) multiplicity in t^n+1 is 2^v_2(n). The h- and 5-periodic subspaces are killed by F_k and intersect in the constants; when δ=1 their sum has the full gcd dimension, with unique representatives x_i=a_i+b_i after a_0=0. This proves periodicity and exhausts the quiet strategies, including the smallest admissible graphs. I reconstructed all six base tables by counting rather than executing verify.py. With S=1+T+T^−1, write A=wt(a), C=wt(Sa), B=wt(b), D=wt(Sb). For δ=1 the Chinese remainder bijection gives weight 5(A+C)+h(B+D)−2(AB+CD). On five bits the joint (B,D) pairs (0,0),(5,5) occur once and (1,3),(4,2),(2,2),(2,4),(3,3),(3,1) occur five times each (singletons, adjacent or distance-two pairs, and complements). For h=1 only (A,C)=(0,0) occurs with a_0=0; for h=2 the pairs are (0,0),(1,1); for h=4 they are (0,0),(1,3),(2,2),(3,1) with counts 1,3,3,1 because Sa is the opposite-coordinate word plus the constant parity. These give exactly the three δ=1 rows, including counts 1,55,144,55,1 for h=4. For δ=0 use all h-bit words, with S the identity for h=1,2 and the same parity rule for h=4, giving the other three rows. Each base weight scales by n/m. The minimum weights, affine fiber cardinalities and solvability fractions follow. The shift in the proof rotates the rings simultaneously; no length-2n single-coordinate cyclic shift is needed.

## originality

PASS

Pass for the uniform six-polynomial homogeneous weight distribution. The nullity formula is already obtainable for arbitrary n from the October 25 conflict-free census, not just from the finite Torrence–Torrence table. Solvability fractions and multiplicities are standard consequences of nullity. No verified source supplies the full two-ring homogeneous weight census.

## value

PASS

The entire quiet-code weight distribution determines the distances from any particular solution to all other solutions in its affine fiber, which nullity alone cannot do. The period reduction and exact census give those distances across two infinite graph families and expose the five-divisibility change in the smallest possible quiet perturbation. This is a natural refinement of the prior Lights Out counts and not a claim about minimum presses needed for arbitrary configurations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
