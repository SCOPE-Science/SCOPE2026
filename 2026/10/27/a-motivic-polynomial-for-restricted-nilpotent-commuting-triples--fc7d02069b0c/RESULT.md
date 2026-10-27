# A motivic polynomial for restricted-nilpotent commuting triples in the modular Witt algebra

## Finding
Let \(p\ge5\) be prime, let \(k\) be any field of characteristic \(p\), and write \(W=\operatorname{Der}_k(k[t]/(t^p))\). With its standard restricted structure, let \(\mathcal N=\{D\in W:D^{[p]}=0\}\) be the **reduced** restricted nilpotent variety and let \(\mathcal C_3\) be the **reduced** variety of ordered triples \((D_1,D_2,D_3)\in\mathcal N^3\) with all three brackets zero. In the Grothendieck ring of reduced finite-type \(k\)-varieties, putting \(\mathbb L=[\mathbb A^1_k]\), one has

\[
\boxed{[\mathcal C_3]=\mathbb L^{(3p-5)/2}(\mathbb L+1)^2-\mathbb L^{p-2}(\mathbb L^2+\mathbb L+1).}
\]

Consequently, if \(k=\mathbb F_q\), with \(q\) any power of \(p\), then the exact number of ordered restricted-nilpotent commuting triples is

\[
\boxed{T_p(q)=q^{(3p-5)/2}(q+1)^2-q^{p-2}(q^2+q+1).}
\]

The formula holds as well over every finite extension \(\mathbb F_{q^s}\) after replacing \(q\) by \(q^s\). Thus its Hasse–Weil zeta function is

\[
Z(\mathcal C_3/\mathbb F_q,z)=
\frac{(1-q^p z)(1-q^{p-1}z)(1-q^{p-2}z)}
{(1-q^{(3p-1)/2}z)(1-q^{(3p-3)/2}z)^2(1-q^{(3p-5)/2}z)}.
\]

These formulas give an exact arithmetic/motivic refinement of earlier geometric analyses of commuting nilpotent pairs and higher tuples in \(W\); no new claim is made about their previously studied irreducible components.

## Assumptions and scope
The characteristic is an odd prime \(p\ge5\). No algebraic-closedness or perfection hypothesis is needed. The full Witt algebra has basis \(t^i\partial_t\) for \(0\le i<p\), and \(\partial_t=d/dt\) on the truncated polynomial algebra. For \(0\ne f\in k[t]/(t^p)\), \(v(f)\) is its lowest nonzero exponent, in \(\{0,1,\ldots,p-1\}\); put \(v(0)=p\). Let \(I_m=t^m k[t]/(t^p)\) for \(2\le m\le p\), interpreted as coefficient spaces of derivations. All varieties in the identity are reduced underlying varieties, not claims about potentially nonreduced defining schemes. Equality in the Grothendieck ring is not a proposed isomorphism of whole varieties.

## Proof
**1. Restricted nilpotent points.** Every derivation is uniquely \(f\partial_t\), with bracket
\[
[f\partial_t,g\partial_t]=(fg'-gf')\partial_t.
\]
If \(v(f)\ge2\), its action strictly raises the degree of every nonconstant monomial, so \((f\partial_t)^p=0\). If \(v(f)=1\), the action on the line \((t)/(t^2)\) has nonzero eigenvalue, hence is not \(p\)-nilpotent. Suppose \(v(f)=0\) and let \(c\) be the coefficient of \(t^{p-1}\) in \(f^{-1}\). Integrate the lower-degree terms of \(f^{-1}\) (all denominators from \(1\) through \(p-1\) are invertible) to obtain a coordinate \(u\) with \(u'=f^{-1}-ct^{p-1}\) and nonzero linear coefficient \(f(0)^{-1}\). Then
\[
(f\partial_t)(u)=1-cf(0)^p u^{p-1}.
\]
The restricted \(p\)-power of \((1+a u^{p-1})\partial_u\) is \(-a(1+a u^{p-1})\partial_u\), by differentiating \(u\) \(p\) times and using \((p-1)!=-1\) in characteristic \(p\). Thus \((f\partial_t)^p=0\) exactly when \(c=0\). The condition \(c=0\), for fixed \(f_0\ne0\), determines the last coefficient \(f_{p-1}\) uniquely and polynomially in \(f_0^{\pm1},f_1,\ldots,f_{p-2}\). Hence the unit-coefficient nilpotent stratum is \(\mathbb G_m\times\mathbb A^{p-2}\), while the other nilpotents form \(I_2\cong\mathbb A^{p-2}\). Therefore
\[
[\mathcal N]=\mathbb L^{p-1}.
\]

**2. Exact centralizers, including their field forms.** For nilpotent \(D=f\partial_t\), if \(v(f)=0\), then \(g\partial_t\) commutes with \(D\) exactly when \((g/f)'=0\); as the derivative kernel in the truncated algebra is \(k\), this centralizer is \(kD\). For \(r=v(f)\ge2\), compare the lowest coefficients of \(fg'-gf'\). The coefficient at degree \(r+j-1\) has pivot \(f_r(j-r)g_j\). This triangular elimination, together with the always-present commuting vector \(f\), yields
\[
C_W(D)=
\begin{cases}
kD\oplus I_{p-r+1},&2\le r\le(p-1)/2,\\
I_{p-r+1},&(p+1)/2\le r\le p-1.
\end{cases}
\]
Every member of these centralizers lies in \(I_2\) and is \(p\)-nilpotent. The displayed direct-sum parametrization is algebraic on each stratum. In the first range \(C_W(D)\) is abelian, since every bracket between elements of \(I_{p-r+1}\) vanishes by degree and \(D\) centralizes that ideal.

**3. A pair count inside the nilpotent coefficient ideals.** Put \(a=(p-1)/2\) and fix \(2\le m\le a+1\). Let
\[
\mathcal B_m=\{(E,F)\in I_m^2:[E,F]=0\}_{\mathrm{red}}.
\]
Classify the first entry by its valuation \(s\). At \(E=0\) the second entry is arbitrary in \(I_m\). For \(m\le s\le a\), its centralizer within \(I_m\) has dimension \(s\). For \(a+1\le s\le p-m\) that dimension is \(s-1\). For \(p-m+1\le s\le p-1\), all of \(I_m\) commutes with it, and the dimension is \(p-m\). Empty intervals contribute nothing. The base stratum of valuation \(s\) is \(\mathbb G_m\times\mathbb A^{p-s-1}\); the centralizer fibers are explicitly affine and trivial on this stratum. Summing the classes gives
\[
[\mathcal B_m]=\mathbb L^{p-2}\bigl(\mathbb L+(a+1-m)(\mathbb L^2-1)\bigr).
\]
In particular, partitioning the first entry of an arbitrary nilpotent commuting pair into the zero, unit-nilpotent, and valuation-at-least-two cases gives
\[
[\mathcal C_2(\mathcal N)]=\mathbb L^{p-2}\bigl(\mathbb L+a(\mathbb L^2-1)\bigr).
\]

**4. Count triples by the first derivation.** If \(D_1=0\), the other two form \(\mathcal C_2(\mathcal N)\). If \(v(D_1)=0\) and \(D_1\) is nilpotent, its centralizer is an abelian line, contributing \((\mathbb L-1)\mathbb L^p\). For each \(r\) from \(2\) through \(a\), the abelian \(r\)-dimensional centralizer gives \((\mathbb L-1)\mathbb L^{p+r-1}\). For \(a+1\le r\le p-1\), set \(m=p-r+1\). The centralizer is precisely \(I_m\); its commuting-pair variety is \(\mathcal B_m\), and the valuation-\(r\) base has class \((\mathbb L-1)\mathbb L^{m-2}\). Therefore, entirely in the Grothendieck ring,
\[
\begin{aligned}
[\mathcal C_3]={}&[\mathcal C_2(\mathcal N)]+(\mathbb L-1)\mathbb L^p
 +(\mathbb L-1)\sum_{r=2}^{a}\mathbb L^{p+r-1}\\
&+(\mathbb L-1)\sum_{m=2}^{a+1}\mathbb L^{m-2}[\mathcal B_m].
\end{aligned}
\]
Substitute the preceding pair formula, set \(z=\mathbb L\), and use the two polynomial identities \( (z-1)\sum_{j=0}^{a-1}z^j=z^a-1\) and \((z-1)\sum_{j=0}^{a-1}(a-1-j)z^j=\sum_{j=0}^{a-1}z^j-a\). The terms then telescope to
\[
[\mathcal C_3]=\mathbb L^{p+a-2}(\mathbb L+1)^2-\mathbb L^{p-2}(\mathbb L^2+\mathbb L+1),
\]
which is the claimed expression because \(p+a-2=(3p-5)/2\). Point counts and the zeta function follow by evaluating \(\mathbb L\) at the sizes of finite extensions and applying the definition of the Hasse–Weil zeta function.

## Verification
The standalone file `witt_triples_check.py` independently implements brackets, restricted powers, finite-field valuation checks, and the closed count. Run `OPENBLAS_NUM_THREADS=1 python witt_triples_check.py` with Python 3 and NumPy. For \(p=q=5\), it enumerates all \(5^5\) derivations, isolates the \(625\) restricted-nilpotent ones, builds their entire pairwise commutation matrix, and verifies exactly \(6625\) ordered commuting pairs and \(108625\) ordered commuting triples. It also exhaustively tests pairs in \(I_2,I_3\) at \(p=5\), and \(I_3,I_4\) at \(p=7\), plus random independent centralizer-rank checks at both characteristics. These are finite tests, not substitutes for the uniform symbolic argument.

## Relationship to prior work
Yao and Chang (2013 arXiv preprint, subsequently published in 2014) classify irreducible components of the **pair** variety in the restricted nilpotent Witt cone and present its centralizers (Lemma 2.3). Those centralizer patterns are acknowledged here as essential antecedents; they do not state the triple motivic class or its arithmetic polynomial. Yao (2015), *On nilpotent commuting varieties of r-tuples in the Witt algebra*, treats geometric irreducible components and dimensions of the same higher-tuple varieties, so its object and scope are directly relevant and cannot be dismissed by title. Its available abstract does not give a Grothendieck-class or zeta-function identity; the full text was not accessible for a decisive complete comparison, leaving a real literature-priority risk. The 2021 Yao–Zhang study concerns commuting tuples of the **whole** Witt algebra, not just restricted nilpotents; its available abstract likewise states component and dimension results, not an exact arithmetic class. The present assertion is only the explicit reduced motivic class, all-extension point counts, and zeta function; no earlier component classification is claimed as new.

## Limitations
The result assumes \(p\ge5\), and makes no statement for \(p=2,3\). It concerns three ordered, pairwise commuting restricted-nilpotent derivations, not arbitrary commuting tuples or nonrestricted nilpotents. It computes the class of the reduced variety, not the integral scheme structure or its singularities. The 2015 higher-tuple paper was compared from its accessible abstract only; exact novelty relative to its complete proofs is unresolved, and independent mathematical validation has not been performed. Absolute publication priority is not certified.

## References
1. Yu-Feng Yao and Hao Chang, *Nilpotent commuting varieties of the Witt algebra*, arXiv:1301.5667v1 (public 2013-01-23), subsequently *Journal of Pure and Applied Algebra* 218 (2014), 1783–1791. https://arxiv.org/abs/1301.5667
2. Yu-Feng Yao, *On nilpotent commuting varieties of r-tuples in the Witt algebra*, *Journal of Pure and Applied Algebra* 219 (2015), 4042–4054, DOI: 10.1016/j.jpaa.2015.02.005.
3. Yu-Feng Yao and Yajing Zhang, *Commuting variety of r-tuples over the Witt algebra*, *Journal of East China Normal University (Natural Science)*, 2021(3), 1–7, DOI: 10.3969/j.issn.1000-5641.2021.03.001.
4. A. Premet, *The theorem on restriction of invariants, and nilpotent elements in \(W_n\)*, *Mathematics of the USSR-Sbornik* 73 (1992), 135–159, DOI: 10.1070/SM1992v073n01ABEH002538.
