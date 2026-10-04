# Review

## Correctness

PASS. The distributed EF21 recursion closes exactly on the exchangeable second moments \(\mathbb E[x^2]\), \(\mathbb E[xm]\), \(\mathbb E[m^2]\), and \(\mathbb E[q]\). The derived \(4\times4\) matrix has
\[
\det(I-M_n(s))
=
\frac{s[6n-(n+8)s]}{16n}.
\]
Because the underlying covariance map is positive, its spectral radius is a real nonnegative eigenvalue; a loss of mean-square stability therefore occurs through a \(+1\) eigenvalue. General EF21 theory supplies stability for sufficiently small positive steps, while the moment operator becomes unbounded for large steps, so the unique positive determinant root is the exact boundary. The infinite-worker limit independently reduces to a \(2\times2\) deterministic system with Jury ceiling \(6\).

Risk: the exact closure relies on identical scalar client curvatures and independent compressor coins.

## Originality

PASS. The defining EF21 paper gives the distributed memory update, contractive-compressor theory, and broad linear convergence guarantees, but the inspected full text does not state an exact half-dropout scalar mean-square boundary or a worker-count law. The 3PC follow-up embeds EF21 into a wider compressor framework and connects it to lazy aggregation, but likewise does not state the moment matrix or the threshold \(6n/(n+8)\).

Focused semantic searches covered EF21, Markov compressors, lazy gradients, Bernoulli and half-dropout compression, scalar quadratics, worker count, and exact mean-square stability. No covering published statement was identified. The one-worker value \(2/3\) coincides with a previously derived classical Bernoulli error-feedback threshold, but the distributed growth to \(6\) is a distinct EF21 result.

## Value

PASS. EF21 was designed to stabilize biased compression and empirically tolerates large steps. The exact worker-count frontier explains a concrete mechanism: independent memories average into a lagged gradient, and this lag can stabilize normalized steps beyond the ordinary gradient-descent ceiling. The transition \(2/3\to6\) provides a sharp benchmark for distributed compression theory and a useful implementation test.

Same-model review: passed. Independent audit: not yet performed.
