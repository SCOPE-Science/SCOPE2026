# Review of exact dyadic fibre and collision laws for odd powers

## Correctness — PASS
The crucial hypothesis is that the exponent is odd; exponentiation then permutes every finite 2-adic unit group. Partitioning by the parity of two independent inputs gives three absolutely continuous pushforward branches and a recursively scaled both-even branch with disappearing mass \(4^{-h}\). This directly proves the density recursion, its precise normalization, and the integer finite-level count formulas. Squaring and averaging gives the displayed \(7/8\) recurrence without a simulation assumption. Disjoint valuation shells give both upper and lower bounds for the precise \(L^s\) threshold. The attached exact verifier checks 4,600 targets across 36 cases. All finite experiments are corroboration, not proof of the unbounded quantifiers.

## Originality — PASS within inspected evidence
Brüdern and Vaughan, *A Montgomery–Hooley Theorem for sums of two cubes* (2021, DOI `10.1007/s40879-021-00495-4`), study global arithmetic-progression variance for cubical sums, with residue representation counts as auxiliary input. Their sections 1, 4, 5, and 6 do not state the general odd-exponent dyadic fibre distribution, its exact collision moment at every depth, or the sharp threshold. The closest known neighboring computations concern distinct primes or even exponents: neither covers odd exponents over \(\mathbb Z_2\). Searches under both local-density and diagonal-congruence terminology revealed no explicit stronger coverage. Unindexed local-zeta results or general published formulas remain a residual priority risk.

## Mathematical value — PASS
The count of collisions \(x^d+y^d\equiv u^d+v^d\pmod{2^n}\) is a natural local arithmetic variance invariant. Its full-depth exact recurrence detects a qualitative transition: the cubic density has finite variance, while every larger odd exponent has infinite limiting variance. The accompanying full fibre law and sharp \(L^s\) cutoff describe the singular mechanism, rather than merely recording an isolated finite residue computation.

## Limitations
This is a 2-adic theorem for odd exponents; it neither states independence from all possible published local-density formulas nor addresses global representations. The finite computational replay does not replace the symbolic proof.

Self-review: passed. Independent audit: not yet performed.
