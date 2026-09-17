# Review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

**PASS.**

The argument was checked at the points where the special diagonal presentation
could conceal a degeneracy.

1. **Smoothness.** Fourier orthogonality identifies the squared-coordinate
   vectors of points of \(X\) with evaluations of cubics at the eighth roots of
   unity. A Jacobian dependence would force a projective point to have support
   at most three, while its corresponding cubic would then vanish at at least
   five distinct eighth roots. This forces the zero cubic and is impossible.

2. **Tangent-fibre reduction.** For the chosen
   \(f=-2-t+2t^3\) and \(g=2+t^2\), both are coprime to \(t^8-1\), so all
   coordinates of the constructed \(x\) and \(w\) are nonzero. Multiplication
   by the fixed diagonal vector \(w\) identifies the fibre with cubics
   \(h\in K\) satisfying \(h^2f\in g^2K\) in
   \(\mathbb Q[t]/(t^8-1)\). Thus the four displayed quadrics describe the
   fibre scheme, not merely its set of closed points.

3. **Reduced singleton certificate.** Exact Gröbner-basis computation gives
   \(b_1=b_3=0\) and \(b_2=1/2\) on \(b_0=1\), and the three standard charts
   covering \(b_0=0\) are empty. Hence the projective fibre is exactly the
   reduced point \([2:0:1:0]\).

4. **Passage to generic degree.** A proper generically finite morphism with a
   reduced singleton fibre has generic degree one: after restricting to a
   finite neighbourhood, the finite module has one-dimensional special fibre,
   hence is locally cyclic by Nakayama; torsion-freeness then bounds its generic
   rank by one.

The tangential Chern-gap identity for \(X_{2,2,2,2}\) gives the product
\(\tau_{\mathrm{tan}}\deg\operatorname{Tan}=64\), so the tangent-variety degree
is 64 once \(\tau_{\mathrm{tan}}=1\).

The exact symbolic certificate was executed with SymPy 1.14.0 and its recorded
output agrees with the displayed equations and Gröbner bases.

## Originality

**PASS, to the best of our knowledge.**

Kanazawa, arXiv:2609.17513 (submitted September 15, 2026), conjectures tangent
degree one for complete Calabi–Yau embeddings in ambient dimension at least
seven and proves it for a **general** intersection of four quadrics. The paper
does not identify this Fourier-diagonal member or provide the reduced-fibre
certificate above.

Targeted searches were made for tangent degree, tangent birationality, and
tangent varieties of diagonal, cyclic, symmetric, and Fourier-type intersections
of four quadrics. Searches also covered equivalent formulations through the
number of tangent spaces through a general point. No source matching this
explicit example or its certificate was found. The current SCOPE archive was
searched by the motivating arXiv identifier, tangent-birationality terminology,
and four-quadric terminology, with no overlapping record found.

Hernandez Gomez–Russo, arXiv:2605.09437, supplies general results on tangent
degree and tangent varieties, but the inspected text does not identify this
special four-quadric example.

Residual originality risk is non-negligible because the motivating preprint is
only days old and concurrent or not-yet-indexed work on special members may
exist.

## Value

**PASS.**

The result moves the newly stated conjecture from a generic-family assertion to
a completely explicit, highly symmetric special member. The proof also provides
a compact exact certificate: one reduced tangent-incidence fibre suffices to
establish birationality. This is useful both as a test example for the conjecture
and as a reproducible template for certifying other special members.

## Scope and limitations

The result treats one smooth \(X_{2,2,2,2}\) in \(\mathbb P^7\). It does not
show that every smooth intersection of four quadrics has tangent degree one and
does not address arbitrary stable-range Calabi–Yau threefolds.

## Sources inspected

- Atsushi Kanazawa, *Chern bounds and tangent geometry of polarized Calabi-Yau
  threefolds*, arXiv:2609.17513. The tangent-incidence definition, the
  tangential Chern-gap formula, the stable-range conjecture, and the theorem for
  a general intersection of four quadrics were inspected.
- Jordi Hernandez Gomez and Francesco Russo, *On the tangent degree and the
  degree of the tangent variety of a projective variety*, arXiv:2605.09437.
  General tangent-degree results and the small-dimensional framework were
  inspected.
- Public literature searches for exact and synonymous formulations described
  above.
- The current public SCOPE archive for internal overlap.

No specifically identified inaccessible paper was found whose available title
or metadata closely suggests that it contains this exact result.
