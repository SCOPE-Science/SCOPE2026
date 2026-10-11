# Same-model review

## Correctness

PASS. The primary source gives both required geometric inputs: for initially flat normal bundle,
\[
\partial_t
\left\langle
R^\perp(e_1,e_2)\nu,\xi
\right\rangle
=
-2
\left\langle
\mathcal C(\nu,\xi)e_1,e_2
\right\rangle,
\]
and for the compact profile,
\[
\mathcal C(\nu,\xi)
=
\frac{2\kappa'\sin\theta}{(2+\cos\theta)^4}
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
\]
Their combination gives the claimed scalar derivative. Exact one-variable calculus gives the unique admissible critical cosine, and the energy coefficient follows from the initial area form and an exact trigonometric integral. The bundled checker replays every new algebraic constant.

## Originality

PASS. The inspected v1 source proves non-preservation by evaluating the source term at \(\theta=\pi/2\). It does not state the complete first-order scalar profile, its maximizing latitude, or the global \(L^2\) onset coefficient. Exact-formula, exact-constant, source-specific, and broader normal-curvature searches found no covering result. The earlier Baker--Nguyen work supplies a general evolution framework but not this later torus-specific quantitative law.

## Value

PASS. The result quantifies the central compact counterexample rather than adding an unrelated computation. It replaces one nonzero witness with a complete pointwise production profile and an exact global instability energy. The coefficient
\[
\frac{118\sqrt3\pi}{243}
\int(\kappa')^2
\]
links the strength of normal-flatness failure directly to the variation of the generating curve's geodesic curvature, providing a natural quantitative invariant of the construction.

Same-model review: passed. Independent audit: not yet performed.

## Closest literature and limitations

The closest source is Kunikawa, arXiv:2609.34291v1. Baker--Nguyen's 2017 paper is the closest earlier normal-curvature evolution reference.

The result is restricted to the compact profile
\[
(2+\cos\theta,\sin\theta)
\]
and to the initial-time expansion. It does not determine the later nonlinear location or magnitude of maximal normal curvature, nor does it treat all profiles in the source's general ansatz.
