# The ordinary-or-zero \(p\)-rank dichotomy for wild boundary cyclic curves

## Finding
Let \(K\) be an algebraically closed field of characteristic \(p\ge3\), and let \(X/K\) be a smooth, projective, geometrically connected curve of genus \(g\ge2\). Suppose that \(\operatorname{Aut}(X)\) contains a cyclic subgroup of order \(N\in\{2g,2g-1\}\) divisible by \(p\). Write \(\gamma(X)\) for the geometric \(p\)-rank of its Jacobian, characterized by \(\#\operatorname{Jac}(X)[p](K)=p^{\gamma(X)}\).

**Theorem.** Every such curve is ordinary or has \(p\)-rank zero: \(\gamma(X)\in\{0,g\}\). For the eight exhaustive normal forms in [1, Theorem 4.8], in their displayed order, the complete list of \((p,N,g,\gamma(X))\) is
\[
(3,3,2,2),\quad(3,6,3,0),\quad(3,12,6,6),\quad(3,12,6,0),
\]
\[
(5,30,15,0),\quad(3,30,15,0),\quad(3,15,8,8),\quad(5,15,8,8).
\]
Consequently the characteristic-three, genus-six order-twelve families have two different \(p\)-ranks, \(6\) and \(0\), so their underlying curves cannot be isomorphic to one another across the two displayed families.

The precise families, with every parameter condition, are the following. Each affine equation means its smooth projective normalization:

| Characteristic, group order, genus | Equation(s) | Exact \(p\)-rank |
|---|---|---|
| \((3,3,2)\) | \(y^3-y=ax+b/x\), \(ab\ne0\) | \(2\) |
| \((3,6,3)\) | \(y^3-y=ax^4+bx^2\), \(a\ne0\) | \(0\) |
| \((3,12,6)\) | \(y^3-y=\kappa/(x^4-1)\), \(\kappa\ne0\) | \(6\) |
| \((3,12,6)\) | \(w^4=z(z-1)^2\), \(y^3-y=az\), \(a\ne0\) | \(0\) |
| \((5,30,15)\) | \(w^6=z^2(z-1)^3\), \(y^5-y=az\), \(a\ne0\) | \(0\) |
| \((3,30,15)\) | \(w^{10}=z^2(z-1)^5\), \(y^3-y=az\), \(a\ne0\) | \(0\) |
| \((3,15,8)\) | \(y^3-y=\kappa/(x^5-1)\), \(\kappa\ne0\) | \(8\) |
| \((5,15,8)\) | \(y^5-y=\kappa/(x^3-1)\), \(\kappa\ne0\) | \(8\) |

## Assumptions and scope
The algebraically closed base field, odd characteristic, positive genus constraint, cyclic subgroup order, divisibility condition, and nonzero coefficients are essential to the classification [1]. This theorem concerns the wild portion \(p\mid N\) of the two exact boundary orders only. We use the completeness of [1, Theorem 4.8] as a cited input, not as a result reproved here. The \(p\)-rank is the stable Cartier rank on holomorphic differentials, equivalently the exponent of the number of geometric \(p\)-torsion points.

## Proof
**1. General cover formula.** Let \(\pi:X\to Z\) be a connected Artin--Schreier cover of degree \(p\), branched at \(r\) geometric points of \(Z\), with each point totally ramified. Denote the \(p\)-rank of \(Z\) by \(\gamma(Z)\). The Deuring--Shafarevich formula, as recalled in [2, Lemma 2.6] for rational bases and [3, (1-2)] for arbitrary bases, gives
\[
\gamma(X)-1=p(\gamma(Z)-1)+r(p-1),\qquad
\gamma(X)=p\gamma(Z)+(p-1)(r-1).\tag{1}
\]
The pole orders do not enter this rank formula, although they determine genus by Riemann--Hurwitz. All covers below have reduced pole orders prime to \(p\).

**2. Five rational-base cases.** In rows 1, 2, 3, 7, and 8 the quotient by the order-\(p\) translations is \(\mathbf P^1\), of \(p\)-rank zero. The rational functions have respectively \(r=2,1,4,5,3\) distinct simple or reduced poles: \(\{0,\infty\}\), \(\{\infty\}\), the four roots of \(x^4=1\), the five roots of \(x^5=1\), and the three roots of \(x^3=1\). The relevant roots are simple in the stated characteristics; the unique polynomial pole has order four, prime to three. Equation (1) gives ranks \(2,0,6,8,8\) respectively.

**3. Three positive-genus bases.** For rows 4--6, put \(Z=X/C_p\) and retain the tame Kummer equation for \(Z\). The following changes exhibit the three quotient curves birationally as nonsingular hyperelliptic models:
\[
\begin{array}{lll}
 w^4=z(z-1)^2 &: z=u^2,\ w=v, &v^2=u^3-u\quad(p=3),\\
 w^6=z^2(z-1)^3 &: z=u^3,\ w=uv, &v^2=u^3-1\quad(p=5),\\
 w^{10}=z^2(z-1)^5 &: z=u^5,\ w=uv, &v^2=u^5-1\quad(p=3).
\end{array}\tag{2}
\]
They are birational, not just degree-greater-than-one parametrizations: in the first case \(u=w^2/(z-1)\); in the second \(u=z(z-1)/w^2\); in the third \(u=z(z-1)^2/w^4\), and then \(v=w\) or \(v=w/u\) as appropriate. These formulae hold on dense open subsets, and consequently identify smooth projective function fields. The resulting bases have genera \(1,1,2\).

In characteristic three the elliptic model \(v^2=u^3-u\) has Hasse invariant the coefficient of \(u^2\) in \(u^3-u\), which vanishes. In characteristic five the elliptic model \(v^2=u^3-1\) has Hasse invariant the coefficient of \(u^4\) in \((u^3-1)^2\), also zero. Thus both elliptic bases have \(p\)-rank zero.

For \(v^2=u^5-1\) in characteristic three the genus-two Hasse--Witt matrix, with entries \(c_{3i-j}\) for \(i,j\in\{1,2\}\), where \(c_k\) denotes the coefficient of \(u^k\) in \(u^5-1\), is
\[
H=\begin{pmatrix}0&0\\1&0\end{pmatrix},\qquad H^2=0.\tag{3}
\]
The coefficients lie in the prime field so Frobenius twists do not change this nilpotence. The stable Frobenius rank, and hence the geometric \(3\)-rank of the genus-two quotient, is zero.

For each of these three hyperelliptic models, the rational function \(z=u^d\) has exactly one pole (at infinity) of order \(2d\), respectively \(4,6,10\), all prime to \(p\). Thus the Artin--Schreier equation \(y^p-y=az\) is branched at exactly \(r=1\) point of \(Z\). Equation (1) gives \(\gamma(X)=p\cdot0+(p-1)(1-1)=0\) in all three cases.

**4. Completeness.** The eight rows are exhaustive by [1, Theorem 4.8], so the previous calculations prove the dichotomy for every curve in the stated domain. The two order-twelve, genus-six rows have distinct ranks, and an isomorphism of curves preserves the \(p\)-rank. This completes the proof.

## Verification
The standalone standard-library program `verify_prank.py` checks all three polynomial identities underlying (2), the elliptic Hasse coefficients and nilpotent genus-two matrix (3), and the Deuring--Shafarevich ranks together with Riemann--Hurwitz genera for all eight rows. Run `python3 verify_prank.py` from the containing directory; the expected final output begins `VERIFY_OK`. These exact checks support, but do not replace, the universal cover formula or the cited completeness theorem.

## Relationship to prior work
Kazemifard--Tafazolian [1, Theorem 4.8] classify the wild odd-characteristic curves at the two cyclic boundary orders and supply the eight normal forms and genera. They do not state an exact \(p\)-rank table, an ordinary-versus-zero dichotomy, or the characteristic-three genus-six rank separation. Pries--Zhu [2] treat the \(p\)-rank stratification for Artin--Schreier covers of the projective line, so their general formula already covers the five rational-base computations given the models. Booher--Cais [3] recall the arbitrary-base Deuring--Shafarevich formula and analyze Cartier operators; they do not classify the eight cyclic-boundary models. The added specialization computes the positive-genus quotient ranks and assembles a complete invariant classification. These inputs make the deduction accessible, and possible earlier explicit tabulations remain a bibliographic risk.

## Limitations
The result does not determine the full Newton polygon, \(a\)-number or Ekedahl--Oort type for the higher-genus Jacobians. Rank zero alone does not establish supersingularity in genus greater than one. Nothing is asserted about tame boundary actions, characteristic two, other subgroup orders, or uniqueness of the parameters in the listed models. The argument depends on the completeness of the published eight-model list [1]; an independent reclassification is not provided.

## References
[1] A. Kazemifard and S. Tafazolian, *Cyclic automorphisms beyond the canonical bound*, arXiv:2610.04702v1 (first submitted 2026-10-03), Theorem 4.8 and its proof, https://arxiv.org/html/2610.04702v1 .

[2] R. Pries and H. J. Zhu, *The p-rank stratification of Artin-Schreier curves*, Ann. Inst. Fourier 62 (2012), 707--726, especially Lemma 2.6, https://doi.org/10.5802/aif.2692 .

[3] J. Booher and B. Cais, *a-Numbers of Curves in Artin-Schreier Covers*, Algebra & Number Theory 14 (2020), 593--641, especially equation (1-2) and §7B, https://arxiv.org/html/1807.10313v3 .
