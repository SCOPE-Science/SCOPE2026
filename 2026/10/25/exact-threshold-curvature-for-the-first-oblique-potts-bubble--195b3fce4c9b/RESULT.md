# Exact threshold curvature for the first oblique Potts bubble

## Finding

For the first oblique two-kink bubble threshold in the extreme-ferromagnetic three-state Potts chain, let \(v=h_2/g>0\), let \(a_1\) be the first threshold satisfying \(F(0,a_1)=0\), set \(\alpha_*=4/(3a_1)\) and \(G(\alpha)=J_{1-\alpha}(\alpha)+4J_{-\alpha}(\alpha)\), and define \(c_1\) by \(p_1(v)=ic_1(v-a_1)+O((v-a_1)^2)\). Then

\[
 c_1=-\frac{3\alpha_*^2}{4}\frac{G'(\alpha_*)}{J_{1-\alpha_*}(\alpha_*)}=8.696131059428713\ldots,
\]

and the leading two-kink energy satisfies

\[
 E_{\min}(g)-E_1(v,g)=K g(v-a_1)^2+O(g|v-a_1|^3),\qquad K=\frac23c_1^2=50.41513026850717\ldots.
\]

The derivative \(G'\) is the total derivative of the composite Bessel expression with respect to \(\alpha\). The displayed decimals are high-precision evaluations, not interval-certified enclosures.

## Assumptions and scope

The statement is for the first bubble branch in the positive oblique regime of the two-kink effective problem, with transverse field \(g>0\) in the extreme-ferromagnetic perturbative regime and \(v\) near \(a_1\). The Jost function and energy are those used for the leading-order two-kink spectrum in the cited analysis. This is not a nonperturbative theorem for the full infinite-chain Hamiltonian at arbitrary field strength.

## Proof

For \(v>0\), write \(\alpha=4/(3v)\). The Jost function used for the oblique two-kink sector is

\[
 F(p,v)=e^{ip}J_{1-\alpha\cos p}(\alpha)+4J_{-\alpha\cos p}(\alpha).
\]

At \(p=0\), this is \(F(0,v)=G(\alpha)\). Differentiating with respect to \(p\) at zero gives

\[
 F_p(0,a_1)=iJ_{1-\alpha_*}(\alpha_*),
\]

because the derivative of \(\cos p\) vanishes at \(p=0\). Differentiating with respect to \(v\), using \(d\alpha/dv=-3\alpha^2/4\), gives

\[
 F_v(0,a_1)=-\frac{3\alpha_*^2}{4}G'(\alpha_*).
\]

The denominator \(J_{1-\alpha_*}(\alpha_*)\) is nonzero. Otherwise \(G(\alpha_*)=0\) would also force \(J_{-\alpha_*}(\alpha_*)=0\); the Bessel identity \(J_\nu'(x)=\nu J_\nu(x)/x-J_{\nu+1}(x)\) would then give both value and derivative zero for the nonzero Bessel solution \(J_{-\alpha_*}(x)\) at \(x=\alpha_*>0\), contradicting uniqueness for its second-order differential equation.

The implicit-function theorem applied to \(F(p_1(v),v)=0\) therefore gives

\[
 p_1'(a_1)=-\frac{F_v(0,a_1)}{F_p(0,a_1)}=ic_1,
\]

which proves the stated expression for \(c_1\). The two-kink energy is \(E_1(v,g)=2-(4g/3)\cos p_1(v)\), while the continuum edge is \(E_{\min}(g)=2-4g/3\). Expanding \(\cos p_1(v)=1+c_1^2(v-a_1)^2/2+O(|v-a_1|^3)\) yields the quadratic gap and \(K=2c_1^2/3\).

## Verification

The accompanying `threshold_curvature.py` evaluates the defining root, the total derivative \(G'(\alpha_*)\), and the coefficient at 50 decimal digits. It reproduces \(a_1=1.4711214207943195\ldots\), \(\alpha_*=0.9063380591748921\ldots\), \(c_1=8.696131059428713\ldots\), and \(K=50.41513026850717\ldots\). This numerical replay is a consistency check; the proof of the formula is the implicit differentiation above, and the decimal output is not a rigorous interval certificate.

## Relationship to prior work

The primary source derives the same Jost function and threshold expansion, stating only that \(c_1>0\) and leaving its value unspecified. The present claim supplies an explicit derivative formula and evaluates the resulting curvature of the leading binding-energy gap. The earlier Potts-chain quench study uses semiclassical analysis and exact diagonalisation; its accessible abstract does not state this Jost-derivative coefficient. No claim is made that the general quadratic threshold exponent is new.

## Limitations

The coefficient belongs to the leading two-kink effective spectrum. Corrections beyond the perturbative model, rigorous error bounds for the displayed decimal, and implications for arbitrary field strength are not established here. Semantic database searches reduce but cannot eliminate the risk of an unindexed equivalent calculation.

## References

1. A. Krasznai, S. Rutkevich, and G. Takács, *Confinement in the three-state Potts quantum spin chain in extreme ferromagnetic limit*, arXiv:2508.20821v1 (first public date 2025-08-28), especially Eqs. (3.6), (3.11)–(3.13), and Appendix A.
2. O. Pomponio, A. Krasznai, and G. Takács, *Confinement and false vacuum decay on the Potts quantum spin chain*, arXiv:2410.03382 (2024). The abstract was inspected as related prior literature; only the abstract was consulted; the full text is not assessed here.
