# Independent mathematical audit

## correctness

PASS

The high-digit split subtracts the shifted residual prefix, with shift +1 or -1 according to the bit index. On complete even blocks the two-step operator is 2I-P-P^(-1); even blocks are symmetric under residue negation. On representatives -h through h conjugating by (-1)^|r| gives a nonnegative recurrence on symmetric coefficients: the folded row at 0 has off-diagonal coefficient 2 and the row at h has diagonal 1, including h=1. For partial prefixes, adjacent opposite signs put both halves in the interval from zero to the full-block value. At the odd transition seam -h the full sum cancels but the prefixes stay between zero and the preceding even-block value. On the next step, at h the anomalous prefix has the same sign as the odd endpoint and no larger magnitude; at -h the next ordinary prefix contributes the correctly signed larger bound. This closes the interval induction. The zero entry of an even endpoint is always positive, and its odd analogue is A_0+A_1>0; subtracting any prefix at the neighboring residue cannot destroy strict positivity at zero. Sparse base-b digit words preserve binary order and digit parity and their value is congruent to the alternating digit sum because b=-1 modulo q. A new direct bit-mask enumeration checked 229383 prefixes across seven moduli (python3 /workspace/branches/recompute_frozen.py); it is only corroboration. The frozen checker uses int.bit_count, so the stated Python 3.8 compatibility in its notes is inaccurate (use Python 3.10+).

## originality

PASS

The distinct result is the uniform all-prefix sign pattern for every residue and every odd modulus, with strict zero-residue positivity. Somu already uses exactly the sparse digit set and the order-preserving change of base, and proves eventual signs at 0 and ±1. Neither the change of base nor the binary modulus-3 case is new. The same-day full-alphabet spectral projector is related but does not yield the sparse prefix sign law.

## value

PASS

The theorem resolves the initial-cutoff question in the sparse Newman setting, including cutoffs too small for asymptotic dominance, and extends the sign classification to every residue. The odd cyclic seam really can cancel a full block while partial sums remain nonzero, so neither eventual positivity nor a full-block recurrence answers the prefix problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
