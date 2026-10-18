# The \(\mathcal O(-1)\) normal bundle of level-three modular curves in Picard modular compactifications

## Finding
For every integer \(n\ge 2\) and every prime \(p\equiv 1\pmod {12}\), consider the Hermitian matrix
\[
J_p=\begin{pmatrix}0&i\sqrt p\\-i\sqrt p&0\end{pmatrix},\qquad H_{p,n}=J_p\oplus(-I_{n-1}),
\]
and the principal level-three special-unitary lattice
\[
\Gamma_{p,n}=\{g\in \operatorname{SL}_{n+1}(\mathbf Z[i\sqrt p]):g^*H_{p,n}g=H_{p,n},\quad g\equiv I_{n+1}\pmod 3\}.
\]
Let \(\overline X_{p,n}\) be the smooth toroidal compactification of the quotient of the positive-line complex ball by \(\Gamma_{p,n}\). Let \(C_{p,n}\subset\overline X_{p,n}\) be the closed, smooth modular curve obtained by taking positive lines in the first two coordinates. This is the embedded compact modular curve \(X(3)\simeq\mathbf P^1\) with four boundary cusps of Memarinasorkhabi--Yeung (2026).

**The normal bundle has the exact splitting**
\[
N_{C_{p,n}/\overline X_{p,n}}\simeq\mathcal O_{\mathbf P^1}(-1)^{\oplus(n-1)}.
\]
In particular,
\[
H^0(C_{p,n},N_{C_{p,n}/\overline X_{p,n}})
=H^1(C_{p,n},N_{C_{p,n}/\overline X_{p,n}})=0.
\]
Consequently the point representing \(C_{p,n}\) in the Hilbert scheme of \(\overline X_{p,n}\) is reduced and isolated. For \(n=2\), the curve is a \((-1)\)-curve on a smooth surface; for \(n=3\), it is a \((-1,-1)\)-curve on a smooth threefold. No global contraction type is asserted.

## Assumptions and scope
All spaces and bundles are over \(\mathbf C\). The full family of primes \(p\equiv1\pmod{12}\) and integers \(n\ge2\) is covered. By the originating paper's Lemmas 2.1, 3.1 and Proposition 3.3, the curve is embedded, its open part is \(Y(3)=\Gamma(3)\backslash\mathfrak H\), its completion is \(\mathbf P^1\), and the four cusps meet four distinct toroidal boundary components transversely. By Proposition 4.1 of that paper,
\[
K_{\overline X_{p,n}}\cdot C_{p,n}=n-3.
\]
These geometric input results are used as stated; the normal-bundle computation below is additional.

## Proof
Write \(r=n-1\). Over the open modular curve, choose the positive-line chart \([\tau:1:\boldsymbol\xi]\), where \(\tau\in\mathfrak H\) and \(\boldsymbol\xi\in\mathbf C^r\). The curve itself is given by \(\boldsymbol\xi=0\). The stabilizer of this disk inside the arithmetic lattice is exactly the image of \(\Gamma(3)\) under
\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix}\longmapsto
\operatorname{diag}(A,I_r)
\]
(originating paper, Lemma 2.1). Direct projective normalization therefore gives
\[
\tau'={a\tau+b\over c\tau+d},\qquad
\boldsymbol\xi'={\boldsymbol\xi\over c\tau+d}.
\]
Differentiating in the transverse directions along the disk yields the *scalar* matrix \((c\tau+d)^{-1}I_r\). Thus the open normal bundle is a direct sum of \(r\) copies of a single automorphy line bundle \(L^\circ\), with no nontrivial mixing of summands.

It remains to identify the extension across the four cusps: ignoring this step could change the normal degree. In the originating paper's toroidal chart at infinity, the ambient local coordinates are \((\boldsymbol\zeta,q)\), the boundary is \(q=0\), and the compact curve is \((\boldsymbol\zeta,q)=(0,q)\), with \(\boldsymbol\zeta=\boldsymbol\xi\) (Section 3, especially Lemma 3.1). The cusp generator \(\tau\mapsto\tau+3\) has \(c=0,d=1\), hence acts trivially on every transverse coordinate. These coordinates extend as a nonsingular frame across \(q=0\). For each of the other three cusps, a matrix in \(\operatorname{SL}_2(\mathbf Z)\), acting block-diagonally as \(\operatorname{diag}(A,I_r)\), transports exactly the same chart and scalar transformation law (originating paper, proof of Lemma 3.1). Since the embedded curve meets four *distinct* boundary components, these are the only new points. Hence the \(r\) identical normal lines extend compatibly and independently across every cusp. There is an algebraic line bundle \(L\) on \(X(3)\simeq\mathbf P^1\) for which
\[
N_{C_{p,n}/\overline X_{p,n}}\simeq L^{\oplus r}.
\]

The determinant of the tangent-normal exact sequence, or adjunction, gives
\[
\deg N_{C_{p,n}/\overline X_{p,n}}
=\deg K_{C_{p,n}}-K_{\overline X_{p,n}}\cdot C_{p,n}
=-2-(n-3)=-(n-1)=-r.
\]
It follows that \(r\deg L=-r\), so \(\deg L=-1\). Every line bundle of degree \(-1\) on \(\mathbf P^1\) is \(\mathcal O_{\mathbf P^1}(-1)\); this proves the displayed splitting.

Finally \(H^0(\mathbf P^1,\mathcal O(-1))=H^1(\mathbf P^1,\mathcal O(-1))=0\). The embedded Hilbert-scheme tangent space is \(H^0(N)\), which vanishes, so the Hilbert local ring at the curve has zero maximal-ideal cotangent space and is a field by Nakayama's lemma. Thus the point is reduced and isolated; the vanishing of \(H^1(N)\) additionally shows no first obstruction space remains. The surface and threefold specializations follow immediately from the splitting. \(\square\)

## Verification
The projective transformation can be recomputed directly from \(\operatorname{diag}(A,I_r)\): divide all coordinates of \([a\tau+b:c\tau+d:\boldsymbol\xi]\) by \(c\tau+d\). Its transverse derivative is a scalar matrix; at the infinity cusp, the width-three translation has scalar factor one. The source's local expression \((\boldsymbol\zeta,q)=(0,q)\) and block-diagonal transport to the other cusps supply the precise extension. Independently, the total degree computed from adjunction is \(-(n-1)\), agreeing with \(n-1\) copies of degree \(-1\); the cohomology of \(\mathcal O(-1)\) vanishes in degrees zero and one. These exact identities, together with the cited primary geometric input, are the verification; no finite sampling is used to infer the universal statement.

## Relationship to prior work
Memarinasorkhabi and Yeung (arXiv:2610.12071v1, Theorem C; Lemma 2.1; Lemma 3.1; Propositions 3.3 and 4.1) construct the curves, give their cusp behavior, and compute \(K\cdot C=n-3\), but do not state their full normal-bundle splitting or the Hilbert-scheme reduced-isolated consequence. The present argument extracts the transverse automorphy factor and checks its extension at the cusps, which is not determined by the canonical degree alone.

Bakker and Tsimerman (arXiv:1503.05654, Lemma 4.8) show a general statement on numerical decomposition into rigid curves for \(K\)-trivial rational curves in dimension three; they do not identify the normal bundle of this newly constructed level-three modular curve. Di Cerbo and Di Cerbo (arXiv:1502.06258) prove nefness properties and discuss the *boundary-divisor* normal bundles, not this curve's normal bundle. The general automorphic-line viewpoint is classical; it is applied here to give the exact extension and splitting for the specified family.

## Limitations
The assertion concerns these particular level-three Picard modular curves, not all rational curves in the compactifications or arbitrary totally geodesic curves. It does not count all isolated Hilbert-scheme points, establish uniqueness of a rational curve in its ambient variety, classify global contractions, or calculate higher-dimensional deformation invariants. The proof uses the originating paper's embedding and canonical-degree theorems as external geometric inputs. General automorphic-bundle technology may subsume the scalar-bundle reasoning in more abstract form; the exact specialization to these examples is the claimed contribution.

## References
1. S. Memarinasorkhabi and S.-K. Yeung, *Rational curves on toroidal compactifications of Picard modular varieties*, arXiv:2610.12071v1 (first posted 2026-10-08), especially §§2–5. https://arxiv.org/abs/2610.12071
2. B. Bakker and J. Tsimerman, *The Kodaira dimension of complex hyperbolic manifolds with cusps*, arXiv:1503.05654, especially Lemma 4.8. https://arxiv.org/abs/1503.05654
3. G. Di Cerbo and L. F. Di Cerbo, *On the canonical divisor of smooth toroidal compactifications*, arXiv:1502.06258, especially Theorem 1.1 and §2.1. https://arxiv.org/abs/1502.06258
