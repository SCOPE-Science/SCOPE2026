# Six rational branches and an additive Picard group in the characteristic-five Bring model

## Finding

Let \(R=\mathbb Z_{(5)}\), and let \(\mathcal B\subset\mathbb P^4_R\) be the projective complete intersection
\[
\sum_{i=1}^5 X_i=\sum_{i=1}^5 X_i^2=\sum_{i=1}^5 X_i^3=0.
\]
Its characteristic-zero generic fiber is the standard genus-four Bring curve. Let \(B\) denote its coefficientwise special fiber over \(k=\mathbb F_5\). Then \(\mathcal B\) is flat over \(R\), and \(B\) is the reduced union of **six distinct \(k\)-rational projective lines**, all meeting at the unique point \(P=[1:1:1:1:1]\). These components are naturally indexed by the six cosets of the affine subgroup \(\operatorname{AGL}_1(\mathbb F_5)\) in \(S_5\).

The sole singularity has six branches and local delta invariant \(9\). Its local completed ring has Hilbert function \((1,3,5,6,6,\ldots)\), and its seminormalization defect is \(4\). More strongly, there is an isomorphism **over \(\mathbb F_5\)** of smooth connected algebraic groups
\[
\operatorname{Pic}^0_{B/k}\ \cong\ \mathbb G_a^4.
\]
Consequently for every integer \(n\ge1\),
\[
\#B(\mathbb F_{5^n})=6\cdot5^n+1,\qquad
Z(B/\mathbb F_5,T)=\frac1{(1-T)(1-5T)^6},
\]
and \(\operatorname{Pic}^0_B(\mathbb F_{5^n})\cong(\mathbb F_{5^n},+)^4\). The arithmetic genus remains \(4\). This is a statement about the specified **flat power-sum model**, not a claim to describe the stable reduction of the smooth generic curve or its Néron model.

## Assumptions and scope

All equations are coefficientwise in \(R\). The special fiber, its normalization, its connected Picard scheme and its zeta function are taken over \(k=\mathbb F_5\); group-scheme isomorphisms remain valid after every field extension of \(k\). The notation \(\operatorname{Pic}^0\) means the identity component, not the full Picard scheme of all multidegrees. For a permutation \(\alpha=(\alpha_1,\ldots,\alpha_5)\) of the five elements of \(k\), define a line
\[
L_\alpha=\{[a+b\alpha_1:\cdots:a+b\alpha_5]:[a:b]\in\mathbb P^1\}.
\]
Two such permutations determine the same line exactly when one is obtained from the other by an affine transformation of the values, \(\alpha_i\mapsto c+d\alpha_i\), with \(d\ne0\). Thus there are \(5!/(5\cdot4)=6\) lines.

## Proof

**1. Six lines, set-theoretically and scheme-theoretically.** In characteristic \(5\), the power sums of the five elements of \(k\), in degrees \(0,1,2,3\), all vanish. Hence every \(L_\alpha\) lies on \(B\). Conversely, Newton identities (valid here since \(2\) and \(3\) are invertible) turn the three equations into \(e_1=e_2=e_3=0\). At any geometric point the polynomial with its five homogeneous coordinates as roots therefore has the form
\[
\prod_{i=1}^5(U-X_i)=U^5+e_4U-e_5.
\]
If \(e_4=0\), its only geometric root is repeated five times, and the point is \(P\). Otherwise the derivative is the nonzero constant \(e_4\). If \(r\) is one root, the five roots are \(r+s\lambda\), \(\lambda\in\mathbb F_5\), where \(s^4=-e_4\). Thus every geometric point belongs to one of the six displayed lines. Outside \(P\) the coordinates are pairwise distinct, so the Jacobian matrix of the three power sums has rows proportional to \((1)_i\), \((X_i)_i\), \((X_i^2)_i\), of rank \(3\). The scheme is generically reduced. Since the equations give a pure one-dimensional complete intersection, it is Cohen--Macaulay and hence reduced. All six lines are distinct and meet only at \(P\). A permutation stabilizing a given line permutes its five values affinely; its stabilizer is \(\operatorname{AGL}_1(k)\), of order \(20\), giving the asserted \(S_5\)-set.

**2. Flatness and genus.** Eliminating the linear equation leaves an intersection of a quadric and a cubic in \(\mathbb P^3\). The special fiber is a reduced pure-dimensional complete intersection, so the element \(5\) is a nonzerodivisor on the homogeneous coordinate ring of the relative complete intersection. Flatness over \(\mathbb Z_{(5)}\) follows. Adjunction for a \((2,3)\)-complete-intersection curve in \(\mathbb P^3\) gives degree \(6\) and arithmetic genus \(1+6(2+3-4)/2=4\).

**3. The single six-branch singularity and its delta invariant.** On \(X_5=1\), translate \(P\) to the origin by writing \(X_i=1+u_i\) for \(1\le i\le4\). The linear equation is \(u_1+u_2+u_3+u_4=0\), and modulo it the remaining equations are exactly \(\sum u_i^2=\sum u_i^3=0\). After eliminating \(u_4\), the completed local ring is the completion of the standard graded algebra
\[
A_\mathrm{gr}=k[u_1,u_2,u_3]/(Q_2,Q_3),\quad
Q_j=\sum_{i=1}^4u_i^j,\quad u_4=-u_1-u_2-u_3.
\]
The two forms cut six distinct reduced directions in \(\mathbb P^2\) (the six line directions above), so they form a regular sequence. Its Hilbert series is
\[
\frac{(1-t^2)(1-t^3)}{(1-t)^3}=1+3t+5t^2+6t^3+6t^4+\cdots.
\]
Normalize the six branches, using a common parameter \(t=u_3\): \(\widehat{\widetilde A}=\prod_{i=1}^6k[[t]]\). In degree \(d\) the inclusion of the local ring has image equal to evaluation of degree-\(d\) homogeneous forms at the six directions; its dimensions are \(1,3,5,6,6,\ldots\). Surjectivity in degree \(3\), and multiplication by the linear coordinate \(u_3\) which equals \(t\) on each chosen branch, ensure that \(t^3\prod k[[t]]\) lies in the local ring. It follows that
\[
\delta_P=\operatorname{length}(\widehat{\widetilde A}/\widehat A)
=(6-1)+(6-3)+(6-5)=9.
\]
In particular \(p_a(B)=\delta_P-6+1=4\), independently confirming adjunction. Its seminormalization is the ring of six-tuples of power series with equal constant terms, so its quotient by \(\widehat A\) has dimension \((6-3)+(6-5)=4\).

**4. The connected Picard group as an actual additive group.** Let \(\nu:\coprod_{i=1}^6\mathbb P^1\to B\) be the normalization. The standard normalization exact sequence of invertible functions identifies the degree-zero Picard group with the quotient of the local units \(\widehat{\widetilde A}^{\times}/\widehat A^{\times}\) by global scalar units on the six components, modulo their common scalar. Those global scalars remove all five multiplicative parameters coming from unequal branch constants. What remains is the smooth connected group
\[
(1+t\prod_i k[[t]])/(1+\mathfrak m_{\widehat A}),
\]
where all terms may be reduced modulo \(t^3\prod k[[t]]\). Because the characteristic is \(5\) and cubes of these truncated nilpotents vanish, the polynomial logarithm \(\log(1+v)=v-v^2/2\), with inverse \(\exp(v)=1+v+v^2/2\), is a group isomorphism to the additive quotient of the degree-one and degree-two evaluation spaces. This quotient is a four-dimensional vector space over \(k\), by the ranks \(3\) and \(5\) established above. Hence it is \(\mathbb G_a^4\) **as a \(k\)-group**, not merely abstractly on rational points or up to isogeny.

**5. Arithmetic.** All six lines and their sole common point are \(k\)-rational. Over every \(\mathbb F_{5^n}\), inclusion--exclusion gives \(6(5^n+1)-5=6\cdot5^n+1\). Exponentiating the point-count series gives the displayed zeta function. The additive Picard group gives the stated finite rational-point group.

## Verification

The accompanying standalone script `verify_bring5.py` uses only exact arithmetic modulo \(5\). It independently enumerates the six points of the conic--cubic direction intersection in \(\mathbb P^2(k)\), verifies transversality by Jacobian ranks, checks that each direction vector is a permutation of the five field elements, and verifies the six cosets of the affine group. It evaluates homogeneous forms on the six branches in degrees \(0\) to \(6\) and recovers the ranks \((1,3,5,6,6,6,6)\), the local delta invariant \(9\), the seminormalization defect \(4\), and the predicted first four finite-field point counts. Run `python3 verify_bring5.py` from the directory containing the script. Its actual output is embedded as `verify_output.txt`.

The infinite-field and group-scheme assertions are proved above; finite enumeration alone is not used as their proof.

## Relationship to prior work

Braden and Northover (first public arXiv version 26 June 2012) present the characteristic-zero canonical power-sum Bring model, its period matrix, and theta-theoretic properties. Geisser's original 2007 paper, read with its corrected later version, develops general Picard torus and unipotent methods. Korchmáros, Lia, and Timpanella (first posted in 2021) study the power-sum model and related symmetric curves in positive characteristic under the explicit assumption \(p\ge7\), with \(m\le p-1\); their main results do not cover \(p=5,m=5\). Braden and Disney-Hogg (2023) treat the complex curve's geometry, symmetries, and theta characteristics. Conca, Krattenthaler, and Watanabe analyze regular sequences of power sums over characteristic zero, rather than this positive-characteristic fiber. These sources supply context and tools, not the evaluated six-component characteristic-five model and its exact additive Picard group. Literature and mathematical-record searches did not identify a theorem with the same evaluated conclusion; this is a qualified priority assessment, not a proof of global novelty.

## Limitations

The special fiber is **not semistable**: six smooth branches meet at one nonnodal point. No statement about the stable model after ramified base change, the Néron model of the generic Jacobian, or the reduction of alternative integral equations is made. The six-line conclusion is for this power-sum complete-intersection model only. The group isomorphism concerns \(\operatorname{Pic}^0\), not multidegree components. Although the generic curve has genus four, the special fiber is reducible and has geometric normalization genus zero on each component. The literature comparison includes a residual risk of a classical implicit calculation via Bring--Jerrard quintics or general regular-sequence methods.

## References

1. H. W. Braden and T. P. Northover, *Bring's Curve: its Period Matrix and the Vector of Riemann Constants*, arXiv:1206.6004 (first posted 2012-06-26), SIGMA 8 (2012), 065. https://arxiv.org/abs/1206.6004
2. T. Geisser, *The affine part of the Picard scheme*, arXiv:0704.0479 (first posted 2007-04-04); corrected version in the same arXiv record and corrigendum, Compositio Mathematica 157 (2021), 2338–2340. https://arxiv.org/abs/0704.0479
3. G. Korchmáros, S. Lia, and M. Timpanella, *A generalization of Bring's curve in any characteristic*, arXiv:2112.10886 (first posted 2021-12-20). https://arxiv.org/abs/2112.10886
4. H. W. Braden and L. Disney-Hogg, *Bring's curve: old and new*, European Journal of Mathematics 10 (2024), article 3, first published online 2023-12-18. https://doi.org/10.1007/s40879-023-00706-0
5. A. Conca, C. Krattenthaler, and J. Watanabe, *Regular Sequences of Symmetric Polynomials*, arXiv:0801.2662 (first posted 2008-01-17), Rend. Sem. Mat. Univ. Padova 121 (2009), 179–199. https://arxiv.org/abs/0801.2662
