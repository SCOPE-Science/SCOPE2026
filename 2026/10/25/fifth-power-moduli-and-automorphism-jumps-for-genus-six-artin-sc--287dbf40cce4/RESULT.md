# Fifth-power moduli and automorphism jumps for genus-six Artin–Schreier fibre products

## Finding
Let \(k\) be an algebraically closed field of characteristic two, fix \(\alpha\in\mathbb F_4\setminus\mathbb F_2\) with \(\alpha^2+\alpha+1=0\), and for each \(\lambda\in k\) let \(\pi_\lambda:C_\lambda\to\mathbb P^1_x\) be the connected \((\mathbb Z/2)^2\)-Galois cover defined by the smooth projective normalization of
\[
 y^2+y=x^5,\qquad z^2+z=\alpha x^5+\lambda x^3.
\]
Here isomorphisms of covers may act nontrivially on the base projective line and may permute the three nontrivial deck involutions; a marking of either is NOT imposed. Then, for every \(\lambda,\mu\in k\),
\[
 (C_\lambda,\pi_\lambda)\simeq (C_\mu,\pi_\mu)
 \quad\Longleftrightarrow\quad \lambda^5=\mu^5.
\]
Thus \(t=\lambda^5\) completely indexes these geometric cover-isomorphism classes. If \(N_\lambda\) denotes the group of all automorphisms of the curve \(C_\lambda\) that normalize the specified deck group (equivalently, all automorphisms of the cover allowing an automorphism of \(\mathbb P^1\)), then
\[
 |N_\lambda|=\begin{cases}
 960&\lambda=0,\\
 16&\lambda^5=1,\\
 4&\lambda\ne0\text{ and }\lambda^5\ne1.
 \end{cases}
\]
The value \(t=1\) is the unique nonzero isomorphism class in this family whose cover-automorphism group exceeds the deck group. Every fibre has genus six. In the previously computed Ekedahl–Oort classification, all nonzero parameters have identical type; hence the symmetry jump at \(t=1\) lies inside one Ekedahl–Oort stratum.

## Assumptions and scope
All geometric isomorphisms and group orders are over \(k\). These statements classify the *equipped Galois covers*, not their underlying unmarked abstract curves; in particular no equality with the full automorphism group of an unmarked curve is claimed. For \(\lambda=0\), an alternative model is \(w^4+w=x^5\), the Hermitian curve of degree five, but the order \(960\) here concerns only the normalizer of the particular degree-four deck group. The case \(\lambda=0\) is included in both the parameter classification and the group calculation. The characteristic-two Artin–Schreier operator is \(\wp(h)=h^2+h\).

## Proof
**The cover and branch point.** The two defining Artin–Schreier classes, and their nonzero sum, all have nonzero leading coefficient and degree five. Such odd-degree polynomials are nontrivial in \(k(x)/\wp(k(x))\); their classes are independent. Hence the compositum is a connected degree-four Galois extension with deck group \(G\cong(\mathbb Z/2)^2\). Its only branch point on the base is infinity, with different contribution \(3(5+1)=18\). Riemann–Hurwitz gives \(2g-2=-8+18=10\), so \(g=6\). Any isomorphism of these equipped covers must fix the unique branch point on the base, and thus induces \(x\mapsto ax+b\), \(a\in k^\times\), \(b\in k\).

**Reduced Artin–Schreier subspaces.** Over algebraically closed \(k\), polynomial Artin–Schreier classes admit unique representatives with only positive odd powers (constants are killed by \(\wp\)). With \(\operatorname{Tr}:\mathbb F_4\to\mathbb F_2\), \(\operatorname{Tr}(c)=c+c^2\), the rank-two \(\mathbb F_2\)-space defining \(\pi_\lambda\) is
\[
 V_\lambda=\{c x^5+\lambda\operatorname{Tr}(c)x^3:c\in\mathbb F_4\}\ \bmod\wp(k(x)).
\]
For any \(c\in\mathbb F_4\), reduce \(f_c(ax+b)\), with \(f_c=cx^5+\lambda\operatorname{Tr}(c)x^3\). Expanding in characteristic two and cancelling its even-degree monomials by the Artin–Schreier operator gives the unique odd part
\[
 c a^5x^5+\lambda\operatorname{Tr}(c)a^3x^3
 +a\bigl[c(b^4+b^{1/4})+\operatorname{Tr}(c)(\lambda b^2+\lambda^{1/2}b^{1/2})\bigr]x.
 \tag{1}
\]
For example, the \(x^4\) term \(ca^4bx^4\) reduces to \(ca b^{1/4}x\), since \(c^4=c\), and the \(x^2\) term \(\lambda\operatorname{Tr}(c)a^2bx^2\) reduces to \(\lambda^{1/2}\operatorname{Tr}(c)a b^{1/2}x\). This proves (1) with no hidden terms.

**Classification.** An affine base map carries \(V_\lambda\) to \(V_\mu\) exactly when the sets of reduced representatives match. Comparing the \(x^5\) coefficients forces \(a^5\mathbb F_4=\mathbb F_4\), or \(a^5\in\mathbb F_4^\times\). Comparing \(x^3\) coefficients then gives, for every \(c\in\mathbb F_4\),
\[
 \lambda a^3\operatorname{Tr}(c)=\mu\operatorname{Tr}(a^5c).\tag{2}
\]
Equation (2) implies \(\lambda=0\) if and only if \(\mu=0\), because the trace is nonzero. When both are nonzero, equality of the kernels of the trace functionals implies
\(a^{-5}\mathbb F_2=\mathbb F_2\), hence \(a^5=1\). Equation (2) reduces to \(\mu=\lambda a^3\). Therefore \(\mu^5=\lambda^5\). Conversely, if \(\mu^5=\lambda^5\ne0\), there is a unique \(a\in\mu_5(k)\) with \(a^3=\mu/\lambda\), and (1) with \(b=0\) proves equality of subspaces. When \(\lambda=\mu=0\), the identity suffices. The asserted if-and-only-if follows.

**Automorphism counts.** In (1), the \(x\) coefficient vanishes for all \(c\in\mathbb F_4\) exactly when
\[
 b^4+b^{1/4}=0,
 \qquad\lambda b^2+\lambda^{1/2}b^{1/2}=0.
 \tag{3}
\]
The first condition says \(b^{16}=b\), so \(b\in\mathbb F_{16}\). If \(\lambda=0\), the second condition is automatic and (2) allows every \(a\) with \(a^{15}=1\): there are \(16\cdot15=240\) affine base maps. For \(\lambda\ne0\), equations (2) and \(\mu=\lambda\) give \(a^5=a^3=1\), hence \(a=1\). The second condition in (3), upon squaring, becomes \(b(\lambda b^3+1)=0\). In \(\mathbb F_{16}^\times\), the nonzero solutions \(b^3=\lambda^{-1}\) exist exactly when \(\lambda\in\mu_5(k)\); then there are exactly three. Including \(b=0\), there are four admissible translations in this case, and only the identity translation otherwise. Each admissible affine base map has precisely \(|G|=4\) distinct lifts to an automorphism of the Galois cover, because its action identifies the defining Artin–Schreier subspaces. Multiplying the base counts by four proves \(960\), \(16\), and \(4\).

## Verification
The companion dependency-free Python script `verify_cover_moduli.py` builds \(\mathbb F_{256}\) explicitly, performs polynomial expansion and direct Artin–Schreier reduction independently of formula (1), enumerates all candidate affine maps for representative parameters, and verifies the predicted group sizes and parameter orbits. It prints `VERIFY_OK` on success. The finite-field check is corroborative: the preceding symbolic argument, not sampling, proves the claim over arbitrary algebraically closed characteristic-two fields.

## Relationship to prior work
Almeida Filho, Tafazolian, and Vieira (arXiv:2610.22755v1, Proposition 10.4) introduced precisely these genus-six covers and proved their supersingularity and their parameter-dependent \(a\)-numbers; Proposition 10.6 computed the Ekedahl–Oort types. These results do not themselves distinguish isomorphism classes at distinct nonzero parameters or determine deck-normalizer group orders. The present result is specifically the full *cover-isomorphism classification* and its stabilizer stratification. The paper *Artin–Schreier Curves of Prescribed \(p\)-Rank Without Extra Automorphisms* (arXiv:2610.13279v1) concerns cyclic degree-\(p\) covers in odd characteristic and a numerical existence problem, not these characteristic-two degree-four covers. Duque-Rosero et al. (arXiv:2401.08843) study genus-three and genus-four rank-one Artin–Schreier classification in odd characteristic. Standard Artin–Schreier correspondence and affine base-coordinate changes are background tools, not presented as new general principles.

## Limitations
The theorem does not decide whether two underlying abstract curves become isomorphic after forgetting the given \((\mathbb Z/2)^2\)-action; full abstract-curve automorphism groups are likewise not determined. Isomorphism is over an algebraic closure, not finite-field descent. Historical priority beyond the checked primary papers and mathematical literature remains a residual risk. The classification is restricted to this naturally published family and makes no claim for arbitrary rank-two Artin–Schreier fibre products.

## References
1. G. B. Almeida Filho, S. Tafazolian, S. C. Vieira, *\(a\)-numbers of covers in characteristic two: semigroups and Riemann–Roch spaces*, arXiv:2610.22755v1 (15 October 2026), especially Propositions 10.1, 10.4 and 10.6, https://arxiv.org/html/2610.22755v1.
2. S. Tafazolian, *Artin–Schreier Curves of Prescribed \(p\)-Rank Without Extra Automorphisms*, arXiv:2610.13279v1 (9 October 2026), https://arxiv.org/html/2610.13279v1.
3. J. Duque-Rosero, H. Goodson, E. Lorenzo García, B. Malmskog, R. Scheidler, *On invariants of Artin–Schreier curves*, arXiv:2401.08843 (2024), https://arxiv.org/abs/2401.08843.
