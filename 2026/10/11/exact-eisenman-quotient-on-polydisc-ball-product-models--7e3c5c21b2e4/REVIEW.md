# Review of Exact Eisenman quotient on polydisc–ball product models

## Correctness

PASS. For every admissible map
\[
F:\Delta^k\times\mathbb B^m\to\mathbb B^{k+m},
\qquad
F(0)=0,
\]
the derivative is a contraction from the product Minkowski norm to the Euclidean norm. Averaging its action on independent phases gives the exact budget
\[
\sum_{j=1}^k\|u_j\|^2+\|Bv\|^2\le1
\]
for every unit ball direction \(v\). Hadamard's inequality and AM-GM then reduce the determinant problem to
\[
\max_{0\le s\le1}
\left(\frac{s}{k}\right)^k(1-s)^m,
\]
whose unique optimizer is \(s=k/(k+m)\). The explicit linear map in the result attains the resulting value.

The Kobayashi–Eisenman identity follows from the exact sandwich
\[
\mathbb B^{k+m}
\subset
\Delta^k\times\mathbb B^m
\subset
\Delta^{k+m}
\]
and the endpoint value \(1\) on both the ball and polydisc.

## Originality

PASS. The full 2026 source was inspected at the definitions, the polydisc computation, Corollary 2.7, and the product-model scaling argument. It proves
\[
k_{\Delta\times\mathbb B^n}(0)=1
\]
but does not compute the corresponding Carathéodory–Eisenman value or quotient invariant. Exact-formula searches and semantic searches did not locate the mixed-product formula
\[
m^m/(k+m)^{k+m}.
\]

The closest broader source gives dimension-dependent estimates and comparability results on convex and \(\mathbb C\)-convex domains rather than this exact product determinant. A residual risk remains that classical invariant-volume literature contains the same product computation in different notation.

## Value

PASS. The product
\[
\Delta\times\mathbb B^n
\]
is not an arbitrary test domain: it is the explicit scaling model in the recent boundary-asymptotic paper, and the quotient invariant is one of that paper's central intrinsic quantities. The source computes the Kobayashi–Eisenman factor of this model but leaves the Carathéodory factor unevaluated.

The exact value completes the intrinsic model at the origin and reveals a clean dimension law,
\[
q_{\Delta\times\mathbb B^n}(0)\sim1/(en).
\]
The full
\[
\Delta^k\times\mathbb B^m
\]
formula shows that this is part of a natural product-family determinant principle rather than an isolated one-dimensional accident.

Same-model review: passed. Independent audit: not yet performed.
