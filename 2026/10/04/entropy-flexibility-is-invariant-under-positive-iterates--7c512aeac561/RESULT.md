# Entropy flexibility is invariant under positive iterates
## Finding
Let \(X\) be a compact metric space, let \(f:X\to X\) be a homeomorphism, and let \(q\ge 1\) be an integer. Using the entropy-flexibility definition in which every \(0\le c<h_{\mathrm{top}}(f)\) is realized simultaneously as topological entropy on a compact invariant subsystem and as metric entropy of an ergodic invariant measure, \(f\) is entropy flexible if and only if \(f^q\) is entropy flexible.

More precisely, a witness at entropy \(c\) for \(f\) transports to a witness at entropy \(qc\) for \(f^q\). Conversely, a witness at entropy \(qc\) for \(f^q\) can be symmetrized over the \(q\) phases to produce a witness at entropy \(c\) for \(f\).

## Assumptions and scope
The phase space is compact and \(f\) is invertible. Topological entropy is the usual entropy of a continuous self-map on a compact metric space, and metric entropy is Kolmogorov--Sinai entropy. The entropy-flexibility notion is Definition 1.2 of Arbieto--Oprocha--Rego. No finiteness assumption on \(h_{\mathrm{top}}(f)\) is needed: for an infinite-entropy system the argument applies to every finite target level.

The proof also preserves the stronger support-coupled formulation in which the ergodic witness measure is required to be supported on the realizing compact subsystem.

## Proof
We use four standard entropy facts. For a compact \(f\)-invariant set \(K\),
\[
h_{\mathrm{top}}(f^q|_K)=q\,h_{\mathrm{top}}(f|_K).
\]
For an \(f\)-invariant probability measure \(\mu\),
\[
h_\mu(f^q)=q\,h_\mu(f).
\]
Metric entropy is affine on the invariant-measure simplex, and topological entropy of a finite union of compact invariant sets is the maximum of their entropies.

We also use the following standard ergodic-component fact. If \(\mu\) is ergodic for \(f\), then the ergodic decomposition of \(\mu\) for \(f^q\) is a finite cycle \(\nu_0,\ldots,\nu_{r-1}\), where \(r\mid q\) and \(f_*\nu_j=\nu_{j+1}\) cyclically. Hence all \(\nu_j\) have the same \(f^q\)-entropy. Since their uniform average is \(\mu\),
\[
h_{\nu_j}(f^q)=h_\mu(f^q)=q\,h_\mu(f).
\]
For completeness, the finiteness follows by letting \(f\) act on the \(f^q\)-ergodic-component space: the induced action has order dividing \(q\), and ergodicity of \(\mu\) for \(f\) makes this finite-order factor ergodic, so it is supported on one finite orbit.

Assume first that \(f\) is entropy flexible. Fix
\[
0\le C<h_{\mathrm{top}}(f^q)=q\,h_{\mathrm{top}}(f)
\]
and put \(c=C/q\). Choose a compact \(f\)-invariant set \(\Lambda\) and an ergodic \(f\)-invariant measure \(\mu\) with
\[
h_{\mathrm{top}}(f|_\Lambda)=h_\mu(f)=c.
\]
The set \(\Lambda\) is also \(f^q\)-invariant and has
\[
h_{\mathrm{top}}(f^q|_\Lambda)=C.
\]
Choose any \(f^q\)-ergodic component \(\nu\) of \(\mu\). By the component fact,
\[
h_\nu(f^q)=q\,h_\mu(f)=C.
\]
Thus \((\Lambda,\nu)\) is an entropy-flexibility witness for \(f^q\).

Conversely, assume that \(f^q\) is entropy flexible. Fix \(0\le c<h_{\mathrm{top}}(f)\) and set \(C=qc\). Choose a compact \(f^q\)-invariant set \(K\) and an ergodic \(f^q\)-invariant probability measure \(\nu\) satisfying
\[
h_{\mathrm{top}}(f^q|_K)=h_\nu(f^q)=C.
\]
Define
\[
\Lambda=\bigcup_{j=0}^{q-1} f^j(K),
\qquad
\mu=\frac1q\sum_{j=0}^{q-1} f_*^j\nu.
\]
Then \(\Lambda\) is compact and \(f\)-invariant, while \(\mu\) is \(f\)-invariant. Each map \(f^j:K\to f^j(K)\) conjugates the restrictions of \(f^q\), so every \(f^j(K)\) has \(f^q\)-entropy \(C\). Therefore
\[
h_{\mathrm{top}}(f^q|_\Lambda)=C,
\qquad
h_{\mathrm{top}}(f|_\Lambda)=c.
\]
To prove that \(\mu\) is ergodic for \(f\), let \(A\) be \(f\)-invariant. Then \(A\) is \(f^q\)-invariant, so \(\nu(A)\in\{0,1\}\); moreover \(f^{-j}A=A\), hence
\[
\mu(A)=\frac1q\sum_{j=0}^{q-1}\nu(f^{-j}A)=\nu(A)\in\{0,1\}.
\]
Thus \(\mu\) is \(f\)-ergodic. Finally, each \(f_*^j\nu\) is \(f^q\)-invariant and measure-theoretically conjugate to \(\nu\), so by affinity
\[
h_\mu(f^q)=\frac1q\sum_{j=0}^{q-1}h_{f_*^j\nu}(f^q)=C.
\]
Hence
\[
h_\mu(f)=C/q=c,
\]
which completes the converse.

If the original witness measure is supported on the original realizing set, the forward ergodic components remain supported there, and in the converse the averaged measure \(\mu\) is supported on \(\Lambda\). Thus the same equivalence holds for the support-coupled variant.

## Verification
The proof was checked separately in both directions. The potentially delicate points are the loss of ergodicity under positive powers and the loss of invariance when passing backward from an \(f^q\)-invariant subsystem. The first is handled by the finite cyclic decomposition of an \(f\)-ergodic measure under \(f^q\); the second is handled by the finite phase union \(\bigcup_{j=0}^{q-1}f^j(K)\) and the averaged measure \(q^{-1}\sum_j f_*^j\nu\).

The edge cases \(q=1\) and \(c=0\) reduce directly to the same formulas. No finite experiment or numerical approximation enters the argument.

## Relationship to prior work
Arbieto, Oprocha, and Rego introduced entropy flexibility for discrete- and continuous-time systems and proved it for broad classes, including shifts of finite type and several hyperbolic or hyperbolic-like systems. Their Definition 1.2 is the notion used here. Inspection of the full preprint found no proposition about invariance under powers or iterates; searches for the terms “power”, “iterate”, and “time map” did not reveal such a statement.

The older lowerability literature proves realization of intermediate topological entropy on compact subsets, generally without requiring invariance or a simultaneously matching ergodic measure. Those results therefore do not imply the present iterate-invariance statement for entropy flexibility.

The proof here uses only classical entropy identities and ergodic decomposition, so it applies to every homeomorphism of a compact metric space, independently of shadowing, expansiveness, hyperbolicity, or symbolic structure.

## Limitations
The theorem is stated for homeomorphisms. The converse argument uses invertibility to conjugate \(f^q|_K\) with \(f^q|_{f^j(K)}\); a non-invertible analogue would require separate hypotheses or a different argument.

The theorem does not assert that a strictly ergodic realizing subsystem remains strictly ergodic under every power. That stronger statement is false in general: a minimal uniquely ergodic system can have a positive power that splits into several cyclic minimal components. The result concerns entropy flexibility itself, for which ergodic components and phase symmetrization recover the required witnesses.

## References
1. A. Arbieto, P. Oprocha, and E. Rego, *Entropy Flexibility of Dynamical Systems*, arXiv:2507.11048v1, 15 July 2025.
2. P. Walters, *An Introduction to Ergodic Theory*, Graduate Texts in Mathematics 79, Springer, 1982.
3. W. Huang, X. Ye, and G. Zhang, *Lowering topological entropy over subsets*, Ergodic Theory and Dynamical Systems 30 (2010), 181--209.
