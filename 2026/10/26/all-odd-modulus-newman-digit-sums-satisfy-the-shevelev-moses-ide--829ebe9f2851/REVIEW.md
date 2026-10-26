# Scientific review

## Correctness — PASS

For each odd \(n\ge3\) and integer \(x\ge0\), digit concatenation gives the exact transfer \(\mathbf S_n((n-1)x)=B_n\mathbf S_n(x)\). The Fourier basis diagonalizes \(B_n^2\); the explicitly computed nonconstant eigenvalues are \(-((\zeta^r-1)/(\zeta^r+1))^2\), which the binomial polynomial \(P_n\) annihilates by \(\zeta^{rn}=1\). On constants it acts as multiplication by \(n\), proving \(P_n(B_n^2)=J_n\). Pairing consecutive integers evaluates the residual digit-parity sum. Exact integer tests from the included verifier agree. The proof covers all odd, including composite, moduli and all integer cutoffs. No finite test is used as the infinite proof.

## Originality — PASS, with residual risk

Shevelev–Moses (arXiv:1209.5705, equations (15) and (74), first submitted 24 September 2012) state both the unrestricted odd-modulus identity and its all-residue generalization as hypothetical and prove only \(n=3,5\). Their separate arXiv:1207.0404 establishes the relevant tangent polynomial and a special identity for complete base-power intervals, not all cutoffs or all residue classes. OEIS A091042 concerns the spectral polynomial; Allouche's separately solved Shevelev conjecture concerns Thue–Morse translation. The present all-cutoff matrix identity is a substantive implication not supplied by those inspected statements. The residual risk is a later or otherwise unlocated equivalent proof.

## Mathematical value — PASS

The theorem supplies a uniform proof for every odd modulus of two explicitly posed Newman-type digital-sum conjectures, removing the prior restriction to two small moduli. The exact all-ones matrix polynomial explains why all residue classes obey the same relation at arbitrary endpoints. This structural result is useful for exact recurrences and analyses of signed digital sums; it does not claim bounds or signs beyond its scope.

## Limitations

No independent audit has been performed. The argument does not apply directly to even moduli, other bases, or alternative digital weights. Any literature gap reported here is conditional on the sources actually inspected, not a proof of novelty against all publications.

Self-review: passed. Independent audit: not yet performed.
