# Review

## Scientific assessment

The record proves an unweighted necessity theorem for commutators of Hilbert
transforms along monomial curves:
\[
[b,H_\gamma]:L^p\to L^{q,\infty}
\quad\Longrightarrow\quad
b\in\operatorname{BMO}^{\gamma,\alpha},
\qquad
\frac{\alpha}{|\beta|}=\frac1p-\frac1q,
\]
for every \(1<p\le q<\infty\) and every ambient dimension \(n\ge2\).

### Correctness

**PASS.**

The key input is the companion-cube pointwise decomposition in Li--Zeng. Its
normalization scales like \(|Q|\): the product of the \(n\) curve parameters
contributes \(\ell(Q)^n\), while the Jacobian determinant contributes
\(\ell(Q)^{|\beta|-n}\). The remaining logarithmic parameter integrals have
scale-independent mass.

The only analytic change from the published diagonal argument is to replace the
final \(L^p\) norm by
\[
\|F\|_{q,\infty}^{\#}
=
\sup_A |A|^{-1/q'}\int_A |F|.
\]
For \(q>1\) this is an equivalent Banach norm for weak \(L^q\), so Minkowski's
integral inequality is valid. On a major subset of the companion cube the
constant mean oscillation therefore satisfies
\[
m_Q|Q|^{1/q}
\lesssim
\|[b,H_\gamma]\|_{L^p\to L^{q,\infty}}|Q|^{1/p}.
\]
The complementary-major-subset case uses the bounded mean-zero test function
from Li--Zeng, whose \(L^p\) norm is at most \(2|Q|^{1/p}\), and gives the same
estimate. Dividing by
\(|Q|^{\alpha/|\beta|}=|Q|^{1/p-1/q}\) yields the claimed seminorm bound.

Stress checks at \(q=p\), in dimension two, under anisotropic scaling, and for
constant symbols are consistent.

### Originality

**PASS, to the best of our knowledge.**

Li--Zeng (arXiv:2609.18613, 16 September 2026) prove the all-dimensional
necessity theorem only for the diagonal \(L^p\to L^p\) problem. Oikari
(arXiv:2304.00621v2) proves off-diagonal sufficiency in arbitrary dimensions but
states that the necessity results are restricted to the plane; Question 1.22
asks for the higher-dimensional necessity theory.

The primary statements and the relevant proof sections of both sources were
inspected. Searches using combinations of monomial curve, commutator,
off-diagonal, weak type, higher dimensions, and
\(\operatorname{BMO}^{\gamma,\alpha}\) did not locate the theorem recorded here.
The Li--Zeng preprint is extremely recent, so a contemporaneous or
not-yet-indexed observation remains the main originality risk. No inaccessible
paper was identified as a specific likely source of prior coverage.

The companion-cube construction, determinant estimates, and the known
off-diagonal sufficiency theorem are not claimed as new. The claimed
contribution is the all-dimensional off-diagonal necessity, including its
weak-\(L^q\) strengthening, obtained from the new companion-cube proof.

### Value

**PASS.**

The result closes the boundedness-necessity portion of a specifically stated
higher-dimensional problem in the currently known strong-boundedness range and
does so under the weaker weak-\(L^q\) hypothesis. It also provides a necessary
condition for all finite \(q\ge p\), including exponents outside the presently
known sufficiency region.

## Limitations

The result is unweighted and does not establish higher-dimensional Bloom
necessity, compactness, \(q<p\), endpoint \(q=\infty\), or general finite-type
curve analogues. It does not enlarge the known sufficiency region. The
higher-dimensional companion geometry is taken from the all-dimensional
Li--Zeng theorem and its stated extension of the detailed three-dimensional
construction.

Same-model review: passed. Independent audit: not yet performed.
