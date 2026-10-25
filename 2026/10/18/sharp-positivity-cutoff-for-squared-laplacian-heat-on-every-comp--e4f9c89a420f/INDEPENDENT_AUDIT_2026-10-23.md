# Independent mathematical audit

## correctness

PASS

For G=K_{m_1,...,m_r} with r>=2 and n=sum m_i, Laplacian spectral projectors onto constants, part-constant mean-zero vectors, and within-part zero sums have eigenvalues 0,n,n-m_i. Applying e^{-tL^2} gives exact cross-part off-diagonal (1-e^{-n²t})/n>0 for t>0; the positive diagonal and within-part off-diagonal w_s(t)=[s/n+(1-s/n)e^{-n²t}-e^{-(n-s)²t}]/s show only within-part signs matter. T(t)1=1, hence the sharp ℓ∞ norm equals 1+2 max_i(m_i-1)[-w_{m_i}(t)]_+, proving interval-preservation equivalence. Let x=(n-s)/n and u=n²t; the sign of -w_s is F(x,u)=e^{-x²u}-(1-x+xe^{-u}). F(x,0)=0, its t derivative has precisely one turning point, and its long-time value is -(1-x), so there is a unique strictly positive recovery root u(x). For fixed u the derivative in x is initially and finally positive (above u0), with at most two zeros by F_xx=2u(2ux²-1)e^{-ux²}; this yields a unique spatial sign-changing point and strict decrease of u(x). Hence the largest part s determines the final root. As x↑1 the root tends to u0>0 with e^{u0}=1+2u0; as x↓0, xu(x)->1. This gives n²τ for one deleted edge ->u0 and nτ for a star ->1, although their first-order norms both grow 1+2(n-2)t+O_n(t²). Independently computed four small graph matrices from adjacency, squared them, exponentiated and matched source closed-form row norms within 1e-10; finite tests are not a proof for all part sizes. The result does not cover weighted/normalized Laplacians or ordinary e^{-tL}.

## originality

PASS

Daners–Glück–Kennedy primary semigroup papers establish eventual positivity criteria and examples including squared Laplacians, but the materially read full-text sections do not furnish these exact complete-multipartite matrix entries, strict part-size ordering and recovery root. A SCOPE-published three-spectral-value no-gap principle does not calculate the root and fails to dominate arbitrary part profiles with >3 distinct spectral levels; where it applies it covers only the no-gap shape, not the quantitative theorem. The distinct ordinary heat derivative result cannot directly give positivity of e^{-tL²}. Search non-exhaustivity and an unpublished equivalent matrix-exponential computation remain risks.

## value

PASS

Positivity of a mass-preserving smoothing kernel is the precise order-preservation and bounded-input range-stability criterion. The theorem finds the sharp recovery time for a large natural graph family, a nontrivial largest-part sufficiency law, and contrasting star versus almost-clique timescales even when their first-order amplification is identical. This is a motivated structural classification requiring a real root-ordering lemma, not just reporting diagonalization of a graph matrix.

The dated certificate retains the supplied scientific assessment, sources and limitations.
