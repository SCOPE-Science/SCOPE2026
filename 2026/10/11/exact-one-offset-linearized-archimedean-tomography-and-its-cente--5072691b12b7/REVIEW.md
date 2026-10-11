# Same-model review

## Correctness

PASS. An explicit radial-graph differentiation yields the first-order area density \(2\varphi\) and the two signed boundary terms \(s\delta(t-s)\) and \(-(s+h)\delta(t-s-h)\). The Funk--Hecke formula converts the operator into exact multipliers
\[
J_\ell(s,h)=\int_s^{s+h}\bigl(P_\ell(t)-tP_\ell'(t)\bigr)dt.
\]
For every \(\ell\ge2\), the coefficient of \(s^\ell\) is \(h(1-\ell)c_\ell\ne0\), yielding the complete zero-set and kernel claims. At centered offset, parity annihilates all odd degrees. The symbolic replay checked the coefficient and parity formulas through degree \(12\); the independent numerical replay integrated the perturbed graph area directly. Infinite-dimensional assertions rest on the analytical proof, not these tests.

## Originality

PASS, subject to the specific accessible-source risk below. Lai's eligible preprint announces nonlinear rigidity for **all offsets** of a fixed-width slab; its abstract contains no claimed one-offset linearization. The later, stronger Ghomi--Howard--Lai full manuscript gives periodic density and potential-theoretic arguments but no Legendre first-variation multipliers, single-offset kernel or centered blindness. Source/alias, spherical-harmonic, Radon and inverse-data searches produced no covering statement. Nonlinear injectivity does not logically imply injectivity of its derivative from a single offset.

**Residual risk:** The complete earliest preprint was inaccessible despite bounded lawful alternatives. Its accessible abstract cannot rule out an unindexed earlier derivation, and analogous formulas might be known under generic spherical-convolution terminology. The later primary full text is the stronger materially inspected source.

## Value

PASS. The recent rigidity problem uses the full family of fixed-width slabs. Identifying the exact kernel of an angular scan at only one absolute displacement is a distinct, motivated inverse-geometric question. The theorem shows a sharp measurement-design dichotomy: all but countably many displacements detect every shape mode modulo translations, while the natural centered displacement misses infinitely many modes. No unsupported nonlinear or stable reconstruction claim is attached.

Same-model review: passed. Independent audit: not yet performed.

## Closest sources and limitations

M. Lai, arXiv:2610.01550v1 (full abstract only); M. Ghomi, R. Howard and M. Lai, *A Converse to the Archimedes Sphere Theorem* (full author-hosted manuscript, Sections 1--6). The work is linearized at the unit sphere, with an implicitly described countable exceptional set. It asserts neither nonlinear uniqueness for one offset nor a conditioning bound.
