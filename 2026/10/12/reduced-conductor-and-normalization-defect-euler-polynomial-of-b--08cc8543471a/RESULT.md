# Reduced conductor and normalization-defect Euler polynomial of binary resultant hypersurfaces

## Finding
For integers \(m,n\ge2\), let \(R_{m,n}\) be the hypersurface of ordered pairs of nonzero degree-\(m\) and degree-\(n\) binary forms with a common linear factor, viewed in \(\mathbb P^m_{\mathbb C}\times\mathbb P^n_{\mathbb C}\). Define
\[
N=\mathbb P^1\times\mathbb P^{m-1}\times\mathbb P^{n-1},\qquad
\nu([\ell],[F],[G])=([\ell F],[\ell G]),\qquad
D=V(\operatorname{Res}(F,G))\subset N.
\]
The finite map \(\nu\) is the normalization. Its **scheme-theoretic conductor on the normalization** is exactly the reduced irreducible divisor of residual pairs with a common root:
\[
\mathfrak c\,\mathcal O_N=\mathcal I_{D/N}
=\mathcal O_N(-D)=\mathcal O_N(0,1-n,1-m).
\]
Moreover \(\mathfrak c=\nu_*\mathcal I_{D/N}\subset\mathcal O_{R_{m,n}}\) is the **radical ideal** of the reduced locus \(S_2\) of pairs with a common quadratic factor (multiplicities included). This statement concerns the conductor scheme, not the generally different Jacobian scheme.

Define \(\mathcal Q=\nu_*\mathcal O_N/\mathcal O_{R_{m,n}}\). Its two-variable Euler-characteristic polynomial is exactly, for all integer \(u,v\),
\[
\begin{aligned}
\chi\bigl(\mathcal Q(u,v)\bigr)
={}&(u+v+1)\binom{u+m-1}{m-1}\binom{v+n-1}{n-1}\
&-\binom{u+m}{m}\binom{v+n}{n}
+\binom{u-n+m}{m}\binom{v-m+n}{n}.
\end{aligned}
\]
Every binomial coefficient here is evaluated as a polynomial in its upper argument, including for negative twists.

## Assumptions and scope
All schemes are over \(\mathbb C\), and \(m,n\) are arbitrary integers at least two. Binary forms are considered up to independent nonzero scalar multiples. A common quadratic factor means a factor of total degree two, possibly a repeated linear form. The conductor is \(\mathfrak c=\operatorname{Ann}_{\mathcal O_R}(\nu_*\mathcal O_N/\mathcal O_R)\), viewed also as the largest ideal of \(\nu_*\mathcal O_N\) contained in \(\mathcal O_R\). The symbols \(\mathcal O_N(a,b,c)\) and \(\mathcal O_R(u,v)\) use the product polarization of the respective projective factors.

## Proof
**Normalization and conductor support.** The universal binary resultant is irreducible and has bidegree \((n,m)\); hence \(R_{m,n}\) is an integral Cartier divisor in \(\mathbb P^m\times\mathbb P^n\). The map \(\nu\) is proper, and its geometric fiber is a finite set indexed by distinct common roots. It is therefore finite; for generic pairs the gcd has degree one, so it is birational. Because \(N\) is smooth, \(\nu\) is the normalization. This projective argument is the homogeneous version of the affine normalization described by Choudary (1990).

The preimage of \(S_2\) is exactly \(D\): after one common factor has been marked and divided out, a second common factor exists precisely when \(F\) and \(G\) have a common root. The universal residual resultant is irreducible, and \(D\) is a reduced Cartier divisor of class \(\mathcal O_N(0,n-1,m-1)\). Outside \(S_2\), the resultant hypersurface is smooth. Generic points of \(S_2\) have exactly two distinct simple common roots and are ordinary two-branch crossings, as in Choudary's normal-crossing criterion. The nonnormal locus is closed; it includes these generic crossing points and hence their whole irreducible closure \(S_2\). Consequently the support of the conductor on \(N\) is exactly \(D\).

**Scheme-theoretic multiplicity via finite duality.** Since \(R_{m,n}\) is a hypersurface in a smooth variety, its canonical sheaf is invertible. Finite duality and the identification of the conductor as a Hom module give, as invertible sheaves on \(N\),
\[
\mathcal I_{\mathrm{cond}/N}\simeq\omega_N\otimes\nu^*\omega_{R_{m,n}}^{-1}.
\]
Here \(\omega_{R_{m,n}}\simeq\mathcal O_{R_{m,n}}(n-m-1,m-n-1)\) by adjunction, and
\[
\nu^*\mathcal O_R(1,0)=\mathcal O_N(1,1,0),\qquad
\nu^*\mathcal O_R(0,1)=\mathcal O_N(1,0,1).
\]
It follows that
\[
\nu^*\omega_R=\mathcal O_N(-2,n-m-1,m-n-1),\qquad
\omega_N=\mathcal O_N(-2,-m,-n),
\]
and hence
\[
\mathcal I_{\mathrm{cond}/N}\simeq\mathcal O_N(0,1-n,1-m)=\mathcal O_N(-D).
\]
The conductor is an **invertible ideal inside** \(\mathcal O_N\), not merely an abstract line bundle. Its nontrivial effective divisor is supported on the single reduced irreducible divisor \(D\), so is some positive multiple of \(D\). Comparing its computed class with \(\mathcal O_N(-D)\) in the free group \(\operatorname{Pic}(N)\cong\mathbb Z^3\) forces multiplicity one. Therefore the conductor ideal is \(\mathcal I_{D/N}\) scheme-theoretically, at every point, including loci with higher common-factor degree.

**Conductor downstairs.** The conductor is the same ideal considered in the two finite-related rings, so \(\mathfrak c=\nu_*\mathcal I_{D/N}\) as an ideal subsheaf of \(\mathcal O_R\). Since \(D\) is reduced, the ideal is radical in \(\mathcal O_N\), and an element of \(\mathcal O_R\) whose positive power lies in it also lies in it. Thus \(\mathfrak c\) is radical in \(\mathcal O_R\). Its support is \(S_2\), hence it equals the defining ideal of \(S_2\) with its reduced induced scheme structure.

**Euler polynomial.** By the exact sequence \(0\to\mathcal O_R\to\nu_*\mathcal O_N\to\mathcal Q\to0\) and finiteness of \(\nu\), the Euler characteristic of \(\mathcal Q(u,v)\) is the difference between the Euler characteristic on \(N\) of \(\mathcal O_N(u+v,u,v)\) and that on \(R\) of \(\mathcal O_R(u,v)\). The exact hypersurface sequence for bidegree \((n,m)\) computes the latter as \(\chi(\mathcal O_{\mathbb P^m\times\mathbb P^n}(u,v))-\chi(\mathcal O_{\mathbb P^m\times\mathbb P^n}(u-n,v-m))\). Substituting \(\chi(\mathbb P^k,\mathcal O(t))=\binom{t+k}{k}\) proves the formula for every integer twist.

## Verification
The standalone exact script `check_conductor.py` requires Python 3 with SymPy. Run `python check_conductor.py` in a directory containing only that script; the recorded output is in `checker_output.txt`. It checks explicit normalization and conductor identities in the bidegree-two affine chart, the canonical/adjunction classes for 25 degree pairs, 48 exact residual-resultant homogeneity identities, and 64 exact Euler-polynomial evaluations. No finite check certifies arbitrary degree: the all-degree argument is the symbolic duality and divisor-class proof above.

For a direct smallest-case check, write the monic quadratic pair in normalized parameters as \(f=(x-t)(x+u)\), \(g=(x-t)(x+v)\). The residual resultant is \(v-u\). If their coefficients are \(a=u-t\), \(b=-tu\), \(c=v-t\), \(d=-tv\), then \(u-v=a-c\) and \(t(u-v)=d-b\). Thus the conductor on the affine source is \((u-v)\), and its image ideal is generated by the two coefficient differences \(a-c\) and \(d-b\).

## Relationship to prior work
Choudary (1990), pp. 261–262, explicitly constructs the affine normalization of the resultant hypersurface, characterizes the singular points by gcd degree, and proves that squarefree higher gcd gives normal crossings. Those results are used, not presented as new. Eisenbud–Schreyer (2001) studies Chow-complex formulas for resultants; Imbach–Moroz–Pouget (2014) studies certified topology of resultant/discriminant curves. The statement isolated here is the global **scheme-theoretic conductor with multiplicity exactly one at every stratum**, its reduced downstairs ideal, and the explicit two-variable Euler polynomial for the normalization defect. A classical but unindexed conductor formula may still exist; literature searching does not establish historical uniqueness.

## Limitations
This result assumes characteristic zero, concerns the conductor rather than the Jacobian scheme, and does not provide minimal generators for the reduced common-quadratic-factor ideal. It neither classifies every formal singularity at higher gcd degree nor establishes anything about arbitrary multivariate resultant loci. Finite computational checks supplement an algebraic argument; no independent external audit has been performed.

## References
A. D. R. Choudary, "On the resultant hypersurface," *Pacific Journal of Mathematics* 142 (1990), 259–263, https://doi.org/10.2140/pjm.1990.142.259 (original full text examined, pp. 259–263; day of first publication not stated).

D. Eisenbud and F.-O. Schreyer, "Resultants and Chow forms via exterior syzygies," arXiv:math/0111040v1 (first public version 2001-11-05), https://arxiv.org/abs/math/0111040.

R. Imbach, G. Moroz and M. Pouget, "Numeric certified algorithm for the topology of resultant and discriminant curves," arXiv:1412.3290v1 (first public version 2014-12-10), https://arxiv.org/abs/1412.3290.
