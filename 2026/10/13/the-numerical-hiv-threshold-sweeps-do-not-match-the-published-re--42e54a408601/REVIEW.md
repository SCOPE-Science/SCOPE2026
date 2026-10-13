# Self-review

## Correctness

PASS. The Example 6.2 formula and Table 1 reduce, for equal delays, to
\[
\mathcal R_0(\tau,\xi)
=
\frac{508}{23}
\left(1-\frac{2\xi}{7}\right)e^{-\tau}.
\]
This exact reduction reproduces none of the four caption labels. It gives both Figure 1 cases and both Figure 2 cases above one. It also proves that decreasing \(\xi\) increases \(\mathcal R_0\), opposite to the Figure 2 labels. The bundled checker replays the calculation exactly.

## Originality

PASS. The exponential-delay threshold mechanism is established literature. The accepted contribution is source-specific: it reconciles the motivating article's own formula, table, and captions and shows that both advertised numerical threshold crossings disappear. Exact DOI/title, figure-number, numerical-label, correction, and prior-ledger searches found no equivalent published correction.

## Value

PASS. The figures are used to illustrate the biological conclusion that changing delay and the latent fraction can suppress infection by crossing \(\mathcal R_0=1\). The corrected arithmetic leaves every displayed case supercritical and reverses one comparative-static direction, so the published numerical validation is not reproducible from the stated inputs.

## Closest literature and limitations

The 2017 latent-HIV predecessor uses the same broad delay-survival threshold architecture and confirms that this modeling mechanism is prior art. It does not contain the source-specific numerical labels or their correction.

Undocumented simulation settings could explain the trajectories, so the finding is limited to the published formula, table, captions, and the interpretation attached to them.

Self-review: passed. Independent audit: not yet performed.
