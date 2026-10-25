# Independent mathematical audit

## correctness

PASS

The Lyapunov identity W(t)=P-e^{At}Pe^{A^Tt} yields the exact kernel K=RUPU*R-UPU*. Stability makes p(z) and p(-z) coprime, so the forward and reversed observability ranges are disjoint; minimality gives P>0, U injective, and exactly d positive/d negative eigenvalues. Reflection parity yields orthogonal block ± singular values with the stated Gram matrices. Rechecked scalar limit at a->0 from the closed formula; the saved numerical checker independently tests Jordan and oscillatory cases but finite sections do not prove generality.

## originality

PASS

The rank is for the self-commutator of the causal triangular convolution, not rank of a general truncated Toeplitz/Hankel convolution itself. Andersson–Carlsson companion arXiv:1506.05566 §2.1 treats finite-rank symbol characterization of Θ_f, whereas T here is generally infinite rank. Potts thesis concerns cyclicity and commutants. Neither inspected comparison directly states inertia (d,d), the signed spectrum, or recovery of McMillan degree by commutator rank.

## value

PASS

A sharp system-order invariant for causal rational convolution plus signed spectral recovery is a natural bridge between realization theory, Gramian geometry and finite-rank operator theory; beyond a renamed standard trace identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
