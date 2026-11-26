# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT.md lines 50–83. Odd exponentiation by d/2 permutes each finite odd-unit 2-group. Odd squares have image 1 mod 8, and every such residue occurs: given an odd root modulo 2^n, n>=3, shifting it by 2^(n−1) toggles the 2^n bit of its square modulo 2^(n+1). Equal-size fibres of the homomorphism give uniformity. Exactly one odd input has probability 1/2 and gives a uniform additive coset 1 mod 8; two odd inputs have mass 1/4 on 2 mod 8. Both-even has mass 1/4 and rescales an independent copy by 2^d, in a disjoint coset. At iteration j the two masses are 4^(−j)/2 and 4^(−j)/4 on cylinders of measure 2^(−dj−3), and no atom remains at zero. At n=1 the fibre densities are (1,1), at n=2 they are (1,2,1,0), and at 3<=n<=d the both-even mass contributes only 2^(n−2) at zero. For n>d the scaled branch contributes multiplier 2^(d−2) in the density and a fraction 2^(−d) of the residue average. Iterating that recurrence at s=2 gives the stated collision constant and geometric factor, since the four-tuple count groups ordered pairs by common target. The cylinder moment sum is geometric and diverges at equality in the stated threshold. The finite densities are conditional expectations of the integrable density; martingale convergence and an L^u bound for max(1,s)<u<d/(d−2) give the stated convergence. Independent bounded replay counts the residues pow(x,d,2^n), cyclically convolves their integer histogram and checks every normalized fibre for d=6,n=1..7 and d=10,n=8..11. For example, at (6,6),(6,7), support counts are 17,34 and collisions are both 13/2. These checks include the change at n=d+1 but do not replace the proof. Frozen verify.py and VERIFICATION.md inspected, not executed.

## originality

PASS

Pass the weighted two-variable representation law, sharp integrability threshold and exact finite collision law for the stated even-exponent class. The shell support and its Haar size are already covered. The prior support theorem shares the power-image lemma and branch decomposition, but uses them for existence and does not count preimages or push input measure through each branch. The later even-exponent result provides exact weighted overlap; the close same-day results have different exponent or modulus hypotheses.

## value

PASS

For the natural two-term diagonal power-sum map, existence of a local representation does not quantify how uneven its counts are. The weighted law resolves the singular scaling quantitatively: it identifies the exact threshold for finite moments, explains the infinite limiting second moment, and predicts every normalized finite collision count including its dependence on precision modulo d. The earlier support law alone cannot supply these invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
