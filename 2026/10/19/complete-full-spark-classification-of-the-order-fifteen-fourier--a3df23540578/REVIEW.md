# Scientific review

## Correctness: PASS

The theorem is finite with explicit quantifiers for all \(2^{15}-2\) nonempty proper row sets. The cited general balance necessity is confirmed from Alexeev–Cahill–Mixon, Section 2. Complementarity follows from Jacobi's identity for invertible Fourier matrices, and affine transformations act by invertible diagonals and permutations. The exact standard-library verifier exhaustively enumerates balanced affine classes through seven rows. Every exceptional class has a completely vanishing integer determinant polynomial modulo \(X^{15}-1\); every other class has all maximal minors nonzero in at least one of two valid prime-field specializations. The original complex determinant cannot vanish if its polynomial has a nonzero specialization. Check results: \(54{,}928\) certified nonzero minors, five explicit singular minors, counts \(15,60,60,180,60,180,600\) for row sizes one through seven. Finite enumeration is exhaustive here because the domain has exactly fifteen indices.

## Originality: PASS, residual risk documented

Alexeev–Cahill–Mixon [1] prove a necessary balance condition for all orders and its sufficiency for prime powers, but neither a sufficient criterion nor full census at order \(15\). Closest published classifications at orders \(10\), \(12\), and \(14\) concern different Fourier matrices. The known all-modulus three-row criterion and four-row special-pattern results cannot determine arbitrary five-, six-, or seven-row classes. Caragea–Lee [2] concern only principal minors, not full spark. Targeted literature and published-record searches found no statement implying the five-orbit classification and exact count, but absence of a match is not a proof of global novelty; equivalent material under another formulation is a residual risk.

## Mathematical value: PASS

This is a complete classification for the first odd semiprime Fourier matrix and pinpoints exactly when the natural divisor-balance necessary condition ceases to be sufficient. The sharp anomaly is structurally nonmonotone across five, six, and seven rows; the result gives a complete, reproducible count of deterministic harmonic frames maximally robust to observation erasures. It is not a parameter substitution in a prime-power theorem: order \(15\) falls outside that theorem's sufficient regime, and the five exceptional affine orbits are genuine additional obstructions.

## Scope and limitations

Only Fourier order \(15\) is classified, with no quantitative conditioning or extension to arbitrary composite moduli. All scientific verification is from a fully inspectable finite proof and self-review. Independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
