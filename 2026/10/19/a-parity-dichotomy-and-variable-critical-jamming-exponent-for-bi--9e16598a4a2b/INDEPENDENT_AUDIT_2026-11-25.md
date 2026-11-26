# Independent mathematical audit

## correctness

PASS

Correct under the explicit Assumptions: uniform ordering of embedded paths, equivalently independent identically distributed continuous clocks. Independence and continuity alone, as in the abbreviated model sentence, would not suffice for the odd-path laws. An even path always takes r from each side until one side is below r. For odd paths all admissible vertex sets have the same number (r+1)!r!/2 of undirected embeddings. Under the uniform order, the remaining paths contained in the vacant set retain an exchangeable relative order, so the next orientation has probability (a−r)/(S−k+1). This yields drift (S−k)/(S−k+1) times D. The multiplicative correction h validates the stopped martingale; the S=k to S=0 transition is deterministic and contributes zero martingale increment under the convention. At S≥εN, the martingale fluctuations are O_P(√N), giving uniform macroscopic drift approximation. In the nonzero-imbalance case, below the positive root of s=|δ|s^{1/k} the approximated |D| would exceed S, whereas above the root the terminal estimate S−|D|≤2r rules out stopping. Boundedness gives the expectation limit. In the critical case there is no early stop at S≥εN with high probability. Summing predictable variance there gives k⁻¹ times the integral of s^(−2/k), and the normalized small-S contribution is at most O(ε^(1−2/k))+o(1). The normalized jumps are O(N^(1/k−1/2)), so the martingale CLT applies with variance 1/(k−2). A bounded terminal size would force normalized |M| to tend to zero there, excluded by the limiting Gaussian's lack of a zero atom. Substitution of h≈(S/N)^(1/k) and S≈|D| at stopping gives the stated exponent and power. The K_{11m,9m} perfect packing takes the specified 3m and m orientations, yet the random vacancy fraction is (1/10)^(5/4). A separate exact reconstruction passed all 11 small full-labeled state laws, 564 drift, 6300 even-remainder and six scaling checks (/workspace/branches/515a47f0-fc47-43bc-9dc2ead3e21f/full_checks.txt); it was not a proof of the asymptotic laws. The uploaded checker was inspected, not executed.

## originality

PASS

Credit is for the fixed odd lengths k≥5, particularly the noncentral terminal law and changing critical exponent. Even-path stoichiometry and the shorter indexed k=3 case are not separately credited. The exact reduction locates the result in diminishing two-color urns, but the relevant primary statements inspected do not provide this two-coordinate-deletion stopped asymptotic. The packing-paper access limitation does not establish noncoverage or block a decision.

## value

PASS

The result measures a natural finite-size jamming gap invisible to near-perfect packing bounds. The stochastic critical law and length-dependent scale distinguish odd adsorbates from exact deterministic even remainders and distinguish a kinetic macroscopic waste fraction from a packing obstruction. This goes beyond the one-length overlap and the routine even stoichiometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
