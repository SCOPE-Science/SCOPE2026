# Diagonal fixed points of the cubic-AGM Hesse 3-isogeny
## Finding
Let \(H(\mu):X^{3}+Y^{3}+Z^{3}-3\mu XYZ=0\) over \(\mathbb C\), with \(\mu^{3}\ne1\), and let Otsubo's cubic-AGM \(3\)-isogeny correspondence be defined by \(\mu'^{3}=(\mu+2)^{3}/(9(\mu^{2}+\mu+1))\). Its diagonal \(\mu'=\mu\) consists exactly of the four nonsingular parameters \(\mu=(-2\pm i\sqrt{2})/3\) and \(\mu=(-1\pm i\sqrt{11})/3\). At the first conjugate pair \(j(H(\mu))=8000\), and at the second \(j(H(\mu))=-32768\); hence the diagonal selects exactly the two complex-multiplication isomorphism classes with fundamental discriminants \(-8\) and \(-11\). For each of the four parameters, Otsubo's formula is a degree-\(3\) endomorphism of the same Hesse model with kernel \(X+Y+Z=0\).

Equivalently, the diagonal of the parameter correspondence has exactly two complex-conjugate pairs. The pair
\[
\mu=rac{-2\pm i\sqrt{2}}{3}
\]
has \(j\)-invariant \(8000\), while the pair
\[
\mu=rac{-1\pm i\sqrt{11}}{3}
\]
has \(j\)-invariant \(-32768\).

## Assumptions and scope
Work over \(\mathbb C\). The Hesse curve is
\[
H(\mu):X^{3}+Y^{3}+Z^{3}-3\mu XYZ=0,
\]
with the nonsingularity condition \(\mu^{3}
e1\). The parameter correspondence is the degree-\(3\) Hesse isogeny from Otsubo's Theorem 1.1, specialized to
\[
\mu'^{3}=rac{(\mu+2)^{3}}{9(\mu^{2}+\mu+1)}.
\]
Only literal diagonal fixed parameters \(\mu'=\mu\) are classified. This is stronger than merely asking whether source and target curves have the same \(j\)-invariant, and it does not classify longer cycles of the correspondence.

## Proof
Impose \(\mu'=\mu\). Since the original correspondence is defined only away from the cubic roots of unity, cross-multiplication gives
\[
9\mu^{3}(\mu^{2}+\mu+1)-(\mu+2)^{3}=0.
\]
The left side factors exactly as
\[
(\mu-1)(3\mu^{2}+2\mu+4)(3\mu^{2}+4\mu+2).
\]
The root \(\mu=1\) is excluded because \(H(1)\) is singular. The two quadratics have negative discriminants and give exactly
\[
\mu=rac{-1\pm i\sqrt{11}}{3},
\qquad
\mu=rac{-2\pm i\sqrt{2}}{3}.
\]
Their absolute values are respectively \(\sqrt{4/3}\) and \(\sqrt{2/3}\), so none is a cubic root of unity; hence all four are in the domain of the correspondence.

Otsubo's equation (4.8) gives
\[
j(H(\mu))
=
27\mu^{3}
\left(rac{\mu^{3}+8}{\mu^{3}-1}ight)^{3}.
\]
Reducing the numerator and denominator of this rational function modulo \(3\mu^{2}+2\mu+4\) yields the constant ratio \(-32768\). Reducing modulo \(3\mu^{2}+4\mu+2\) yields the constant ratio \(8000\). Thus the first conjugate pair maps to \(j=-32768\) and the second to \(j=8000\).

The standard CM table implemented in Sage identifies \(j=8000\) with fundamental discriminant \(-8\) and \(j=-32768\) with fundamental discriminant \(-11\). Finally, Otsubo's Theorem 1.1 applies with \(\mu'=\mu\) at each of the four allowed parameters, so its displayed degree-\(3\) isogeny has the same Hesse curve as source and target. Its kernel is exactly
\[
X+Y+Z=0.
\]

## Verification
The standalone checker `artifacts/verify_target.py` uses only Python's standard library. It verifies the degree-\(5\) factorization above by exact rational polynomial arithmetic, verifies the two exact reductions of the \(j\)-invariant numerator against its denominator, and verifies that the two quadratic factors have negative discriminant and therefore do not contribute roots with \(\mu^{3}=1\). Its expected terminal line is:
`VERIFY_OK fixed_parameters=4 j_values=8000,-32768`.

The CM-discriminant identification is literature-backed rather than recomputed by the checker.

## Relationship to prior work
Otsubo, arXiv:2610.03100v1, constructs the cubic-AGM Hesse \(3\)-isogeny, states the parameter relation in Theorem 1.1, and gives the Hesse \(j\)-invariant in equation (4.8). The paper does not state the diagonal fixed locus and contains no occurrence of \(8000\) or \(-32768\).

Arpin, Camacho-Navarro, Lauter, Lim, Nelson, Scholl and Sotáková, *Adventures in Supersingularland*, identify the \(j\)-level self-\(3\)-isogeny values by factoring the classical modular polynomial on the diagonal:
\[
\Phi_3(j,j)=-j(j-54000)(j-8000)^{2}(j+32768)^{2}.
\]
That result covers self-\(3\)-isogenies at the \(j\)-invariant level. It does not determine which values are fixed by Otsubo's newer Hesse parameter correspondence. The classification above shows that its literal parameter diagonal selects precisely the double-loop values \(8000\) and \(-32768\), not the simple-loop values \(0\) and \(54000\).

Hashimoto and Nuida's 2026 preprint studies cubic-AGM cycles and Hessian \(3\)-isogenies over finite fields with a congruence restriction. Its abstract confirms close thematic overlap, but only the abstract was available for inspection here; this is retained as a residual literature risk rather than treated as negative evidence.

## Limitations
The claim is over \(\mathbb C\) and concerns only literal equality \(\mu'=\mu\). It does not classify parameters for which \(H(\mu)\) and \(H(\mu')\) are merely isomorphic, does not classify cycles of length greater than one, and does not make a finite-field statement. The older modular-polynomial literature already knows the relevant \(j\)-level self-isogeny values; the new content is the exact diagonal lift to Otsubo's Hesse parameter correspondence and the resulting level-structured selection of the two CM types.

## References
1. N. Otsubo, *Cubic arithmetic-geometric mean and isogenies of Hesse elliptic curves*, arXiv:2610.03100v1, first public 2026-10-02. Theorem 1.1 and equation (4.8).
2. S. Arpin, C. Camacho-Navarro, K. Lauter, J. Lim, K. Nelson, T. Scholl, J. Sotáková, *Adventures in Supersingularland*, Experimental Mathematics 32 (2023), 241–268; published online 2021-10-21, DOI:10.1080/10586458.2021.1926009.
3. Y. Hashimoto and K. Nuida, *Cubic AGM graphs and Hessian 3-isogenies over finite fields*, arXiv:2609.14300v1, 2026.
4. SageMath Reference Manual, `cm_j_invariants_and_orders`, listing \((-8,1,8000)\) and \((-11,1,-32768)\).
