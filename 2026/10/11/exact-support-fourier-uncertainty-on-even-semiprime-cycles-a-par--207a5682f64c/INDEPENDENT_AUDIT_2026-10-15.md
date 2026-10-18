# Independent mathematical audit

## correctness

PASS

The actual RESULT.md proof splits the cyclic 2p transform via CRT Z_2 x Z_p into h_+=f_0+f_1 and h_-=f_0-f_1. With both channels nonzero, each has time support <=k, so Tao's prime-order uncertainty lower bound gives >=2(p-k+1) Fourier coefficients. A vanishing channel forces equal/opposite slices and even exact support k=2r, giving >=p-r+1. For each s<=p, the polynomial product_{j=0}^{s-2}(X-zeta^j) has s-1 distinct prime-root Fourier zeros and, by the same prime uncertainty bound, all its s coefficients nonzero. It realizes the two possible channel mechanisms with EXACT k, proving the two candidate bounds are sharp. Algebra gives crossover 3r=p+1 and the claimed p-7 jump. The proof is for complex arbitrary signals and k<=p only; no monotonicity of the exact-k invariant is assumed. The finite checker is corroboration, not the infinite proof.

## originality

PASS

Bounded best-of-knowledge originality: the exact stated invariant and quantified result were compared by implication to the closest primary and published SCOPE sources; no decisive covering result found. Unread material and alternative nomenclature remain explicit, and source search is not proof of absolute novelty.

## value

PASS

The exact-support profile is a natural invariant genuinely different from the at-most-k Meshulam uncertainty function: its parity-driven optimal mechanisms and unbounded 4-to-5 jump identify nonmonotonic sparse Fourier behavior not visible in the ordinary envelope. It gives a complete infinite family rather than a small computed table. These are mathematically motivated exact sparsity boundaries useful in composite Fourier uncertainty problems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
