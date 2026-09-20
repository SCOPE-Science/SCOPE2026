# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The proof uses two exact identities stated in the source: the reverser
\(S(x,y,z)=(x,-y,-z)\) and the divergence
\(-a\cos y\sin z\). The divergence changes sign under \(S\). On a setwise
\(S\)-invariant periodic orbit, time reversal therefore forces its period-average
to vanish. Liouville's formula then gives monodromy determinant one; after the
trivial flow multiplier is removed, the two transverse multipliers have product
one. The same conclusion follows directly from conjugacy of the monodromy to its
inverse under reversibility.

For the explicit family \(\varphi_{k,s}\), setwise \(S\)-invariance is immediate on
the torus, and the divergence integral can also be evaluated directly. The
\(a=0\) parity classification follows from the exact constant-coefficient normal
system. The Hill reduction for \(\varphi_{0,0}\) was algebra-checked directly
from the source's normal variational equation.

Adversarial checks included the resonant cases where a unit-circle multiplier is
\(\pm1\); these are classified as parabolic rather than elliptic. The theorem does
not promote spectral ellipticity to nonlinear Lyapunov stability.

## Originality

PASS, to the best of our knowledge.

The primary source, arXiv:2609.19958v1 (submitted 17 September 2026), was inspected
in full-text HTML. It states the reversing symmetry, divergence, explicit periodic
family, Liouville formula, and the normal variational equation along
\(\varphi_{0,0}\). Full-text searches found no occurrence of "reciprocal" or
"Floquet"; the paper discusses characteristic multipliers only for its
averaging-based non-integrability argument and does not derive the symmetric-orbit
no-attraction consequence.

Searches using the exact title, arXiv identifier, "Floquet", "reversible periodic
orbit", "attractor repeller", and equivalent Nosé–Hoover formulations did not
locate a source-specific prior statement or correction. Classical reversible
dynamics literature does contain the general reciprocal-multiplier theorem for
symmetric periodic orbits; that theorem is explicitly excluded from the novelty
claim.

The main residual risk is the very recent date of the source: author revisions,
comments, or discussions may not yet be indexed. No inaccessible paper was found
that specifically appears likely to contain this model-specific consequence.

## Value

PASS.

The result gives an exact all-parameter obstruction for the source paper's
distinguished periodic family and clarifies a potentially ambiguous use of
"stable": the central orbit may be elliptic but cannot be an asymptotic attractor.
It also imposes a concrete hidden-structure requirement on the paper's numerically
reported attracting windows: every attracting periodic orbit must be
symmetry-broken and accompanied by a distinct repelling time-reversed orbit.
The \(a=0\) parity classification and the Hill discriminant formulation provide
reusable analytic structure for further stability work.

## Sources checked

- W. Szumiński and J. Llibre, *Trigonometric Nosé–Hoover oscillator: chaos,
  periodic orbits and integrability*, arXiv:2609.19958v1:
  https://arxiv.org/abs/2609.19958
- J. S. W. Lamb and J. A. G. Roberts, *Time-reversal symmetry in dynamical
  systems: a survey*, Physica D 112 (1998), 1–39:
  https://doi.org/10.1016/S0167-2789(97)00199-1
- Standard reversible-dynamics literature was checked for the classical
  reciprocal-multiplier fact; no originality is claimed for that general fact.

## Limitations retained

No closed-form stability boundary for the Hill discriminant is claimed. No
nonlinear stability theorem is claimed for elliptic periodic orbits. The
numerically reported attracting orbit is not reconstructed or independently
validated here. The result applies to the exact reversible system and \(b\ne0\)
for the explicit periodic family.
