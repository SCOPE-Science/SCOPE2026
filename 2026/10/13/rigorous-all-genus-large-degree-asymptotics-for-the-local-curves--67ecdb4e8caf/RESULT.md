# Rigorous all-genus large-degree asymptotics for the local curves \(X_p\)
## Finding
For an integer \(p\ge2\), let
\[
X_p=\operatorname{Tot}\!\left(\mathcal O_{\mathbf P^1}(p-1)\oplus\mathcal O_{\mathbf P^1}(-p-1)\right),
\]
and for \(g\ge2\) write its closed genus-\(g\) potential as
\[
\mathcal F_g(Q)=\sum_{d\ge0}N_{g,d}^{(p)}Q^d.
\]
Set
\[
Q_c=\frac{(p^2-1)^{p^2-1}}{p^{2p^2}}.
\]
Then, for every fixed \(p\ge2\) and \(g\ge2\),
\[
\boxed{
N_{g,d}^{(p)}\sim
(-1)^{g-1}
\frac{p^{g-1}(p^2-1)^{(g-1)/2}}
{2^{(5g-5)/2}\,\Gamma((5g-5)/2)}
\frac{\langle\tau_2^{3g-3}\rangle_g}{(3g-3)!}
Q_c^{-d}d^{(5g-7)/2}
}
\]
as \(d\to\infty\).

Equivalently,
\[
\lim_{d\to\infty}
(-1)^{g-1}N_{g,d}^{(p)}Q_c^d d^{-(5g-7)/2}
=
\frac{p^{g-1}(p^2-1)^{(g-1)/2}}
{2^{(5g-5)/2}\,\Gamma((5g-5)/2)}
\frac{\langle\tau_2^{3g-3}\rangle_g}{(3g-3)!}.
\]
The constant on the right is positive. Consequently the radius of convergence of the positive-degree part of \(\mathcal F_g\) is exactly \(Q_c\), and the degree coefficients have eventual sign \((-1)^{g-1}\).

This turns the long-standing fixed-genus large-degree prediction for these local curves into an all-genus theorem with an exact tautological leading constant.

## Assumptions and scope
The Gromov--Witten potential and normalization are those of Guo--Xu--Zhang. Their A-model variable \(Q\) and B-model variable \(q\) satisfy
\[
Q=q(1-q)^{p^2-1}.
\]
For \(g\ge2\), their polynomiality theorem has the form
\[
\mathcal F_g(Q)
=(-1)^{g-1}\frac{P_g(\Delta,p^2)}{\Delta^{5g-5}},
\qquad
\Delta=\frac{1-p^2q}{1-q},
\]
where \(P_g\) is polynomial in \(\Delta\). Their double-scaling theorem gives the exact critical value
\[
P_g(0,p^2)
=
\frac{p^{6g-6}}{(p^2-1)^{2g-2}}
\frac{\langle\tau_2^{3g-3}\rangle_g}{(3g-3)!}.
\]

The result concerns fixed \(p\) and fixed \(g\) with degree tending to infinity. It does not assert a simultaneous large-genus and large-degree expansion.

## Proof
Put \(r=p^2\). Solving the definition of \(\Delta\) for \(q\) gives
\[
q=\frac{1-\Delta}{r-\Delta},
\qquad
1-q=\frac{r-1}{r-\Delta}.
\]
Hence the mirror map becomes
\[
Q
=\frac{1-\Delta}{r-\Delta}
\left(\frac{r-1}{r-\Delta}\right)^{r-1}.
\]
At the critical point \(\Delta=0\), equivalently \(q=r^{-1}\), this gives
\[
Q_c=\frac{(r-1)^{r-1}}{r^r}
=
\frac{(p^2-1)^{p^2-1}}{p^{2p^2}}.
\]
Moreover
\[
\frac{Q}{Q_c}
=(1-\Delta)\left(1-\frac{\Delta}{r}\right)^{-r}.
\]
Taking logarithms and expanding at \(\Delta=0\), the linear terms cancel and
\[
1-\frac{Q}{Q_c}
=
\frac{r-1}{2r}\Delta^2+O(\Delta^3).
\]
Thus on the branch analytically continued from \(q=0\),
\[
\Delta
=
\left(\frac{2r}{r-1}\right)^{1/2}
\left(1-\frac{Q}{Q_c}\right)^{1/2}
+O\!\left(1-\frac{Q}{Q_c}\right).
\]

Let
\[
\alpha_g=\frac{5g-5}{2}.
\]
Because \(P_g(0,p^2)\ne0\), the polynomiality theorem and the preceding local change of coordinate yield
\[
\mathcal F_g(Q)
=
C_{g,p}
\left(1-\frac{Q}{Q_c}\right)^{-\alpha_g}
\left(1+O\!\left((1-Q/Q_c)^{1/2}\right)\right),
\]
where
\[
C_{g,p}
=(-1)^{g-1}P_g(0,p^2)
\left(\frac{p^2-1}{2p^2}\right)^{(5g-5)/2}.
\]
Substituting the exact critical value of \(P_g\) simplifies this to
\[
C_{g,p}
=
(-1)^{g-1}
\frac{p^{g-1}(p^2-1)^{(g-1)/2}}{2^{(5g-5)/2}}
\frac{\langle\tau_2^{3g-3}\rangle_g}{(3g-3)!}.
\]

The principal inverse of \(Q=q(1-q)^{r-1}\) has its first nonzero branch point at \(q=r^{-1}\): indeed
\[
\frac{dQ}{dq}=(1-q)^{r-2}(1-rq),
\]
so the only nonzero critical value reached from the germ at \(q=0\) is \(Q_c\). Standard transfer for this algebraic square-root singularity gives
\[
[Q^d]\left(1-\frac{Q}{Q_c}\right)^{-\alpha_g}
\sim
\frac{Q_c^{-d}d^{\alpha_g-1}}{\Gamma(\alpha_g)}.
\]
Since \(\alpha_g-1=(5g-7)/2\), multiplication by \(C_{g,p}\) gives the claimed formula.

The intersection number \(\langle\tau_2^{3g-3}\rangle_g\) is a positive Witten--Kontsevich intersection number, so the leading constant is nonzero and has sign \((-1)^{g-1}\). This also makes \(Q_c\) the exact convergence radius.

## Verification
The proof uses three inputs that were checked directly in the full initiating source: the closed mirror map
\[
Q=q(1-q)^{p^2-1},
\]
the genus-\(g\) rational form with denominator \(\Delta^{5g-5}\), and the all-genus double-scaling evaluation of \(P_g(0,p^2)\) in terms of \(\langle\tau_2^{3g-3}\rangle_g\).

The singularity calculation was then reconstructed independently. Differentiating the mirror map gives the critical point \(q=p^{-2}\); substituting it gives \(Q_c\). Rewriting the mirror map in the variable \(\Delta\) shows that the first derivative vanishes and the quadratic coefficient is exactly \((p^2-1)/(2p^2)\). Combining this square-root conversion with the exact pole order \(5g-5\) gives the exponent \((5g-7)/2\) after coefficient transfer.

No finite-degree fit is used. The argument is an exact local singularity calculation followed by the standard coefficient-transfer theorem for algebraic singularities.

## Relationship to prior work
Caporaso--Griguolo--Mariño--Pasquetti--Seminara predicted the critical behavior and pure-gravity double-scaling law for this local-curve family. Their analysis explicitly treated the all-genus critical coefficient as a conjecture, with checks at low genus and in a limiting regime. Guo--Xu--Zhang prove that conjectural critical coefficient for every genus.

Couso-Santamaría--Schiappa--Vaz later wrote the corresponding fixed-genus large-degree asymptotic shape for local curves and tested it numerically. Their local-curve analysis relied on the earlier higher-genus ansatz, used finite-genus data to determine coefficients, and described part of the large-degree step as numerical. Thus the exponent and qualitative asymptotic shape are not new here. The new content is that Guo--Xu--Zhang's 2026 all-genus polynomiality and double-scaling theorem, combined with exact singularity transfer, supplies a proof for every finite \(p\ge2\) and every \(g\ge2\), with the leading coefficient expressed exactly by a tautological intersection number.

Targeted searches for an all-genus rigorous theorem with this exact coefficient located no covering statement. The closest indexed results concerned other enumerative geometries or finite-degree descendant computations and do not imply the local-curve asymptotic.

## Limitations
The theorem is a leading fixed-genus large-degree asymptotic. It does not provide the complete asymptotic expansion in descending half-integer powers, although the same local algebraic structure suggests how further terms could be extracted.

The statement uses the normalization of the local-curve Gromov--Witten potential in Guo--Xu--Zhang. Older physics papers use a shifted parameter convention for the local-curve family, so parameters must be translated before comparing constants.

No claim is made for \(g=0\) or \(g=1\), whose potentials have different singular forms, or for a coupled limit in which \(g\) also grows.

## References
S. Guo, J. Xu, Q. Zhang, “Structure of higher-genus open-closed Gromov--Witten theory of \(\mathcal O_{\mathbf P^1}(p-1)\oplus\mathcal O_{\mathbf P^1}(-p-1)\),” arXiv:2609.40257v1, first public 2026-09-30. See the closed mirror map, Theorem 3.3, Theorem 4.5, and Corollaries 4.6 and 4.8.

N. Caporaso, M. Cirafici, L. Griguolo, S. Pasquetti, D. Seminara, R. J. Szabo, “Topological strings and large \(N\) phase transitions I: Nonchiral expansion of q-deformed Yang--Mills theory,” and the associated local-curve double-scaling analysis; see also the local-curve phase-transition paper cited by Guo--Xu--Zhang as the source of the higher-genus ansatz and double-scaling conjecture.

R. Couso-Santamaría, R. Schiappa, R. Vaz, “On asymptotics and resurgent structures of enumerative Gromov--Witten invariants,” arXiv:1605.07473, especially the local-curve large-degree discussion and its asymptotic formula.
