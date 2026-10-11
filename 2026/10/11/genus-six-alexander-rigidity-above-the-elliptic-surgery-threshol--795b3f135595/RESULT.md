# Genus-six Alexander rigidity above the elliptic-surgery threshold
## Finding
Let \(K\subset S^3\) be a hyperbolic knot of Seifert genus \(6\). If \(r\)-surgery on \(K\) is an elliptic manifold for some positive slope \(r>21\), then \(r\in\{22,23\}\) and, under the symmetric normalization \(\Delta_K(1)=1\),
\[
\Delta_K(t)=t^6-t^5+t^3-t^2+t-1+t^{-1}-t^{-2}+t^{-3}-t^{-5}+t^{-6}.
\]
This is exactly the Alexander polynomial of the pretzel knot \(P(-2,3,9)\). The conclusion concerns the Alexander polynomial; it does not assert that \(K\) is isotopic to \(P(-2,3,9)\).

## Assumptions and scope
The knot is assumed hyperbolic, contained in \(S^3\), and of Seifert genus exactly \(6\). The surgery slope is positive and satisfies \(r>4\cdot6-3=21\), and the filled manifold is assumed elliptic. The Alexander polynomial is symmetrically normalized by \(\Delta_K(t)=\Delta_K(t^{-1})\) and \(\Delta_K(1)=1\).

## Proof
An elliptic three-manifold is an L-space, so \(K\) is an L-space knot. Schmalian--Sivek, Theorem 2.2 and Lemma 3.9, imply that the nonzero coefficients of \(\Delta_K\) alternate between \(+1\) and \(-1\), that the two highest terms are \(t^6-t^5\), and that the remaining positive exponents are chosen from \(\{4,3,2,1\}\). Thus there are at most \(2^4=16\) support patterns before applying the additional restriction of Proposition 2.4.

Proposition 2.4 excludes precisely a support whose first missing exponent below \(6\) occurs at odd offset after the fixed initial pair. In genus \(6\), this removes the four patterns with exponent \(4\) present but exponent \(3\) absent, and the one pattern with exponents \(4,3,2\) present but exponent \(1\) absent. Eleven candidates remain.

Schmalian--Sivek, Corollary 3.7, applies because \(r>21\): if \(\lambda>1\) is the pseudo-Anosov dilatation, then \(\Delta_K(-\lambda)=0\). Hence the polynomial \(Q(t)=t^6\Delta_K(t)\) must have a real root in \(( -\infty,-1)\).

The accompanying exact verifier enumerates all eleven candidates and uses Sturm sequences over \(\mathbb Q\) to count their roots in \(( -\infty,-1)\). Exactly one candidate has such a root, and it has positive support \(\{6,5,3,2,1\}\). Its polynomial is
\[
\Delta_K(t)=t^6-t^5+t^3-t^2+t-1+t^{-1}-t^{-2}+t^{-3}-t^{-5}+t^{-6}.
\]
Schmalian--Sivek, Example 3.8, gives this same polynomial for \(P(-2,3,9)\).

It remains to locate the slope. Schmalian--Sivek, Proposition 3.5, gives \(r\le23\). An elliptic filling is a finite surgery, and Ni--Zhang record that a finite surgery slope on a hyperbolic knot is integral or half-integral. Thus \(r>21\) leaves only \(43/2,22,45/2,23\). Their Table 4 identifies both half-integral possibilities \(43/2\) and \(45/2\) with knot Floer homology of a genus-seven sample, so neither can occur on a genus-six knot. Therefore \(r\in\{22,23\}\).

## Verification
Run `python3 verify_genus6_alexander.py`. The verifier constructs the sixteen L-space support candidates, applies the Proposition 2.4 support exclusion, checks that eleven remain, and performs exact Sturm root counts on \(Q(t)=t^6\Delta(t)\). It returns

`VERIFY_OK total=16 admissible=11 unique_negative_root_support=6,5,3,2,1 root_count=1`

No floating-point root computation is used in the proof certificate.

## Relationship to prior work
Schmalian--Sivek prove the negative-dilatation-root condition for high elliptic surgeries and state in Remark 1.7 that a genus-six knot with finite surgery of slope \(22\) or \(23\) has the same dilatation as \(P(-2,3,9)\). They do not state the exact genus-six Alexander-polynomial rigidity above. Ni--Zhang's finite-surgery tables already force the \(P(-2,3,9)\) knot Floer homology in the O-type \(22\)-surgery and I-type \(23\)-surgery cases, but their statement does not cover the claimed surgery-type-independent implication from a high elliptic surgery. Futer--Ishikawa--Kabaya--Mattman--Shimokawa classify finite surgeries within the three-tangle pretzel family; that family-specific classification does not imply the assertion for an arbitrary hyperbolic genus-six knot.

## Limitations
The result determines only the normalized Alexander polynomial and the two possible slopes. It does not prove that every candidate surgery exists, does not identify the knot up to isotopy, and does not extend the finite enumeration beyond genus \(6\). The originality comparison has residual risk from classifications of cyclic lens-space surgeries via Berge knots: no source located in the checked literature stated the genus-six polynomial rigidity in this form, but a sufficiently explicit unpublished or differently indexed finite Berge-table computation could conceivably imply the cyclic subcase.

## References
1. M. Schmalian and S. Sivek, *Lens space surgeries on knots of small genus*, arXiv:2609.39260v1, 2026. Relevant items: Theorem 2.2, Proposition 2.4, Proposition 3.5, Corollary 3.7, Example 3.8, Lemma 3.9, Remark 1.7.
2. Y. Ni and X. Zhang, *Finite Dehn surgeries on knots in \(S^3\)*, Algebraic & Geometric Topology 18 (2018), 441--492, doi:10.2140/agt.2018.18.441. Relevant items: Known Facts 1.1--1.2, Tables 2--5, Corollary 1.7.
3. D. Futer, M. Ishikawa, Y. Kabaya, T. W. Mattman, and K. Shimokawa, *Finite surgeries on three-tangle pretzel knots*, Algebraic & Geometric Topology 9 (2009), 743--771, arXiv:0809.4278.
