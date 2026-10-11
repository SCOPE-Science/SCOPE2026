# Finite-dimensional generalized-hyperbolic perturbations are mutual factors
## Finding
Let \(n\ge 1\). Let \(f\in\mathfrak D(\mathbb R^n)\) satisfy generalized hyperbolicity in the sense of Tikhomirov, and let
\[
g=f+\Delta
\]
satisfy the hypotheses of Theorem 2.3 of arXiv:2610.04179v1. Thus the theorem supplies bounded continuous maps \(h,k:\mathbb R^n\to\mathbb R^n\) for which
\[
H=\operatorname{Id}+h,\qquad K=\operatorname{Id}+k,
\]
\[
g\circ H=H\circ f,\qquad f\circ K=K\circ g.
\]
Then \(H\) and \(K\) are automatically proper and surjective. Thus \(H\) is a factor map from \((\mathbb R^n,f)\) onto \((\mathbb R^n,g)\), and \(K\) is a factor map in the reverse direction.

Define
\[
h_{\mathrm{cpt}}(q)=
\sup\left\{
h_{\mathrm{top}}(q|_C):
C\subset\mathbb R^n\text{ is nonempty, compact, and forward invariant}
\right\}.
\]
Then
\[
h_{\mathrm{cpt}}(f)=h_{\mathrm{cpt}}(g)
\]
in \([0,+\infty]\).

## Assumptions and scope
The conclusion uses exactly the semiconjugacies and bounded-displacement estimates of Theorem 2.3 of arXiv:2610.04179v1, specialized to the finite-dimensional phase space \(\mathbb R^n\). No additional regularity of the generalized-hyperbolic splitting is assumed.

The entropy statement concerns only the supremum of ordinary topological entropy over compact forward-invariant subsystems. It makes no assertion about Bowen entropy, co-compact entropy, or any other entropy definition on the whole noncompact phase space.

## Proof
Write
\[
M_H=\|h\|_\infty,\qquad M_K=\|k\|_\infty.
\]

First, \(H\) is proper. If \(C\subset\mathbb R^n\) is compact and \(H(x)\in C\), then
\[
\|x\|\le \|H(x)\|+\|h(x)\|
\le \max_{y\in C}\|y\|+M_H.
\]
Thus \(H^{-1}(C)\) is bounded. It is closed because \(H\) is continuous, hence compact in finite dimension.

Next, \(H\) is surjective. Fix \(y\in\mathbb R^n\), and choose
\[
R>\|y\|+M_H.
\]
On \(\|x\|=R\), define
\[
F_t(x)=x+t h(x)-y,\qquad 0\le t\le 1.
\]
Then
\[
\|F_t(x)\|\ge \|x\|-t\|h(x)\|-\|y\|>0.
\]
Therefore the Brouwer degree of \(F_t\) on the radius-\(R\) ball at \(0\) is constant in \(t\). At \(t=0\), the map is \(x\mapsto x-y\), with degree \(1\). Hence \(F_1=H-y\) has a zero, so \(H(x)=y\) for some \(x\). The same argument proves that \(K\) is proper and onto.

Now let \(C\subset\mathbb R^n\) be nonempty, compact, and forward invariant under \(g\). Put
\[
D=H^{-1}(C).
\]
Properness makes \(D\) compact, surjectivity makes \(D\) nonempty and gives \(H(D)=C\), and
\[
H(f(x))=g(H(x))\in C
\]
shows that \(D\) is forward invariant under \(f\). Hence
\[
H|_D:(D,f|_D)\longrightarrow(C,g|_C)
\]
is an onto semiconjugacy between compact dynamical systems. Monotonicity of ordinary topological entropy under factors yields
\[
h_{\mathrm{top}}(g|_C)\le h_{\mathrm{top}}(f|_D).
\]
Taking suprema gives \(h_{\mathrm{cpt}}(g)\le h_{\mathrm{cpt}}(f)\). Applying the same argument to \(K\) gives the reverse inequality.

## Verification
Theorem 2.3 of arXiv:2610.04179v1 was checked in the full arXiv text. It states the two semiconjugacy identities and the uniform bounds
\[
\|h\|_\infty,\|k\|_\infty\le Md.
\]
Definition 2.2 explicitly says that surjectivity is not required, and the introduction says that surjectivity is not asserted in general. The future-research section identifies mutual invertibility, rather than merely surjectivity, as the remaining obstacle to structural stability.

The new finite-dimensional step is self-contained: any continuous bounded perturbation of the identity on \(\mathbb R^n\) is proper and onto by the degree argument above. The entropy step uses only properness, surjectivity, semiconjugacy, and the compact-space factor inequality. No finite numerical experiment is used.

## Relationship to prior work
Tikhomirov proves bi-sided bounded continuous semiconjugacy for generalized-hyperbolic diffeomorphisms on arbitrary Banach spaces while explicitly declining to assert surjectivity in that generality. The finite-dimensional degree argument upgrades those particular semiconjugacies to onto factor maps but not to conjugacies.

Kwietniak and Ubik use the natural noncompact-space quantity obtained by taking the supremum of ordinary topological entropies over compact invariant subsystems for maps of the real line. Their work motivates \(h_{\mathrm{cpt}}\), but does not address the generalized-hyperbolic perturbation setting or the mutual-factor conclusion here.

Targeted searches under the aliases “bounded displacement”, “proper semiconjugacy”, “finite-dimensional generalized hyperbolicity”, “mutual factors”, and “compact-subsystem entropy” found no statement implying this finite-dimensional upgrade.

## Limitations
Surjectivity does not imply injectivity. Nothing here proves
\[
K\circ H=\operatorname{Id}
\qquad\text{or}\qquad
H\circ K=\operatorname{Id}.
\]
Accordingly, the structural-stability question left open in arXiv:2610.04179v1 remains open.

The proof uses finite-dimensional compactness and Brouwer degree and does not extend the surjectivity conclusion to arbitrary infinite-dimensional Banach spaces. The entropy conclusion is deliberately restricted to \(h_{\mathrm{cpt}}\).

## References
1. Sergey Tikhomirov, “Discontinuous Generalized Hyperbolicity and Structural Stability,” arXiv:2610.04179v1, 2026.
2. Dominik Kwietniak and Martha Ubik, “Topological entropy of compact subsystems of transitive real line maps,” arXiv:1208.3975; Dynamical Systems 28 (2013), 62–75.
3. Standard Brouwer-degree fact used above: a continuous map \(x\mapsto x+b(x)\) on \(\mathbb R^n\) with bounded continuous \(b\) has degree \(1\) relative to sufficiently large balls and is therefore surjective.
