# Same-model review

## Correctness

PASS. The disease-free Jacobian is reconstructed directly from the printed map. Its two multiplier-\(-1\) equations meet at
\[
h=\frac{2}{d},
\qquad
\lambda=\frac{dr}{A},
\]
with nonzero parameter-transversality determinant
\[
-\frac{2A}{d}.
\]
At that step size the invariant disease-free boundary is exactly
\[
x\longmapsto\frac{2A}{d}-x,
\]
so its square is the identity. The two-step transverse derivative at the pair
\[
\frac{A}{d}\pm u
\]
is exactly
\[
1-\left(\frac{2ru}{A}\right)^2.
\]
The explicit rational witness is replayed by the bundled checker.

## Originality

PASS. The location of the double nonhyperbolicity is not claimed as independently new: the earlier same-map stability theorem already lists the two curves whose intersection gives it, and a later broader discrete-SIR paper again contains the double-\(-1\) disease-free case in its topological table. The surviving original content is the source-specific correction plus the exact nonlinear disease-free two-cycle continuum and its transverse multiplier. Searches by exact source identity, disease-free resonance aliases, period-two language, and the earlier/later papers did not locate those nonlinear statements.

## Value

PASS. The primary paper is devoted to codimension-two resonances yet excludes the disease-free fixed point. The omitted point has a strong, interpretable nonlinear consequence: an entire positive disease-free interval becomes exact period two under the Euler map. The transverse multiplier additionally distinguishes normally contracting members of this neutral family, making the correction useful both for bifurcation interpretation and for recognizing a discretization-induced epidemic artifact.

## Closest literature and limitations

The closest prior result is Hu, Teng, and Zhang, DOI 10.1016/j.matcom.2013.08.008, which gives the same map's disease-free stability and both nonhyperbolicity curves. Suo and Ge, DOI 10.1080/10236198.2025.2525863, later give a broader uncertain-incidence disease-free topological classification, but their nonlinear resonance analysis is developed at the endemic fixed point.

The finding deliberately does not claim a generic isolated \(1{:}2\) normal form: the exact continuum of two-cycles is the degeneracy being identified. It also does not modify the primary source's endemic resonance calculations.

Same-model review: passed. Independent audit: not yet performed.
