# Rational Richelot kernels and Frobenius splitting in the \(D_4\) genus-two pencil

## Finding

For any finite field \(K=\mathbb F_q\) of odd order, any \(s\in K\setminus\{-2,2\}\), and \(c\in K^\times\), consider the smooth genus-two curve
\[
Z_{c,s}:\quad y^2=c(x^2+1)(x^4+sx^2+1),\qquad J_{c,s}=\operatorname{Jac}(Z_{c,s}).
\]
Write \(r_q(s)\) for the number of **distinct \(K\)-defined maximal Weil-isotropic subgroup schemes** of \(J_{c,s}[2]\); equivalently these are the distinct \(K\)-rational Richelot \((2,2)\)-isogeny kernels, without identification of isomorphic targets. Such a subgroup need not consist of \(K\)-rational points. Let \(w_q(s)\) denote the Frobenius cycle partition of the six geometric Weierstrass points, and let \(a_q(s)=\#J_{c,s}[2](K)\). Exactly the following rows occur:

| Congruence | Frobenius cycle partition | Number of literal \(s\)-parameters | \(a_q(s)\) | \(r_q(s)\) | Degree-two Frobenius orbits of other kernels |
|---|---|---:|---:|---:|---:|
| \(q\equiv1\pmod4\) | \(1^6\) | \((q-5)/4\) | 16 | 15 | 0 |
| \(q\equiv1\pmod4\) | \(1^2 2^2\) | \(3(q-1)/4\) | 4 | 3 | 6 |
| \(q\equiv3\pmod4\) | \(1^4 2\) | \((q-3)/4\) | 8 | 3 | 6 |
| \(q\equiv3\pmod4\) | \(2^3\) | \((3q-5)/4\) | 4 | 7 | 4 |

Each table row is to be read only in its indicated congruence. The first row is empty for \(q=5\), and the third row is empty for \(q=3\). The numbers of literal \((c,s)\)-pairs are the displayed counts multiplied by \(q-1\). All Weierstrass points and all fifteen geometric maximal isotropic kernels are defined over \(\mathbb F_{q^2}\), and this field is minimal unless the corresponding Frobenius action is already trivial. In particular, two strata have the same \(\#J[2](K)=4\) but respectively **three and seven** rational Richelot kernels.

## Assumptions and scope

The base field has odd characteristic (including characteristic three). The excluded values \(s=\pm2\) are exactly where the sextic has multiple geometric roots. For each \(c\ne0\), the multiplicative constant is a quadratic twist and does not change the branch points, their Frobenius action, or the subgroup scheme \(J[2]\) with its pairing. Counts refer to distinct parameters, not curves up to \(K\)-isomorphism. A kernel gives an isogeny to a principally polarized abelian surface, which can be a product of elliptic curves; no assertion that every target is a genus-two Jacobian is made. Distinct kernels may give isomorphic target surfaces.

## Proof

**(1) Splitting and degree two.** Put \(f_s(x)=(x^2+1)(x^4+sx^2+1)\). Since \(s\ne\pm2\), the reciprocal quartic has four distinct roots, disjoint from the two roots of \(x^2+1\). If \(t\ne0\) is a root of the reciprocal quartic, then
\[
s=-(t^2+t^{-2}),\qquad \{\text{quartic roots}\}=\{t,-t,t^{-1},-t^{-1}\}.
\]
These four roots are distinct. One of them belongs to \(K\) if and only if all four do. To see that they always belong to \(K_2=\mathbb F_{q^2}\), set \(u=t^2\), so that \(u^2+su+1=0\). If \(u\in K\), every square root of \(u\) lies in \(K_2\). Otherwise \(u^q=u^{-1}\), hence \(u^{q+1}=1\). The norm-one subgroup of the cyclic group \(K_2^\times\) has elements \(g^{(q-1)j}\), where \(g\) generates \(K_2^\times\); since \(q\) is odd, \(q-1\) is even, so every element of that subgroup is a square in \(K_2\). Thus \(t\in K_2\). The quartic contributes precisely \(1^4\) or \(2^2\). The roots of \(x^2+1\) contribute \(1^2\) if \(\chi_q(-1)=1\) and a single \(2\)-cycle otherwise. This yields the four listed cycle partitions, all with Frobenius of order at most two.

**(2) Counts of parameter values.** The map
\[
\varphi:K^\times\longrightarrow K,\qquad t\longmapsto-(t^2+t^{-2})
\]
has exactly four preimages \(\{t,-t,t^{-1},-t^{-1}\}\) for each \(s\ne\pm2\) with split reciprocal quartic. Its excluded points satisfy \(t^4=1\), of which there are \(\gcd(4,q-1)\). Thus the number of split-quartic parameters is exactly
\[
A_q=\frac{q-1-\gcd(4,q-1)}4.
\]
Among the \(q-2\) permitted \(s\)'s, the other \(q-2-A_q\) have quartic cycle partition \(2^2\). Substituting \(\gcd(4,q-1)=4\) or \(2\) according to \(q\pmod4\) proves all four frequency formulas.

**(3) Rational two-torsion.** The standard geometric description of \(J[2]\) is the set of even subsets of six branch points modulo the equivalence \(S\sim S^c\); there are \(16\) classes. Frobenius fixes a class precisely if \(F(S)=S\) or \(F(S)=S^c\). For each partition with at least one fixed branch point, the second possibility is impossible, because a fixed branch point cannot change membership under Frobenius. For partition \(2^3\), the condition \(F(S)=S^c\) would require choosing one point from each of three transposed pairs, which gives odd cardinality, again impossible. Thus rational classes correspond to Frobenius-stable even subsets, divided by complementation. For cycles \(1^6,1^4 2,1^2 2^2,2^3\) the numbers are respectively \(16,8,4,4\), as asserted.

**(4) Rational maximal isotropic kernels.** By the standard Weil-pairing description, the fifteen geometric maximal isotropic subgroups of \(J[2]\) correspond bijectively, Galois-equivariantly, to the fifteen unordered partitions of the six branch points into three disjoint pairs. A partition represents a subgroup scheme defined over \(K\) if and only if Frobenius preserves the *collection* of its three pairs; its constituent quadratic factors need not each be rational. Counting fixed matchings is elementary but sensitive to cycle type:

- For \(1^6\), every one of the fifteen matchings is fixed.
- For \(1^4 2\), the two transposed points must be paired, leaving three matchings on the four fixed points.
- For \(1^2 2^2\), the two fixed points must be paired, leaving three matchings of the remaining two transposed pairs.
- For \(2^3\), there is the matching of the three internal transposed pairs; any other stable matching retains one of those three pairs and matches the other two Frobenius pairs crosswise, in one of two ways. This gives \(1+3\cdot2=7\).

Since every branch point lies in \(K_2\), Frobenius squared acts trivially on all matchings. Of fifteen kernels, the nonfixed kernels therefore form \((15-r_q(s))/2\) orbits of length two. This finishes the proof for all odd prime powers.

## Verification

Run \(python3 verify_richelot.py\) with the Python standard library. The included self-contained checker constructs \(\mathbb F_{p^2}\), locates all six Weierstrass roots, computes their Frobenius permutation, enumerates all fifteen perfect matchings and all even-subset two-torsion classes, and checks the full formulas for every permitted \(s\) over the prime fields \(p\in\{3,5,7,11,13,17,19,23,29,31\}\) (\(138\) parameters). It ends with `D4_RICHELOT_FROBENIUS_FREQUENCIES_PASS`. This is a finite consistency check only. The result for every odd prime power, including nonprime powers, follows from the group-theoretic proof above.

## Relationship to prior work

Arul, Booher, Groen, Howe, Li, Matei, Pries, and Springer give the pencil in their equation (2.1), and treat full rational Weierstrass splitting using the parameter \(s=-(t^4+1)/t^2\), particularly in Section 3. They investigate doubled isogenies, unramified elementary abelian covers and related arithmetic. The curve equation and split-branch parametrization are prior results; this note does not claim them. Bruin and Doerksen give the general Galois-equivariant theory of quadratic splittings and Richelot kernels, including kernels not pointwise rational, in their Section 4. The identification of kernels with perfect matchings and the generic count fifteen are prior results. The present **family-specific joint stratification** computes, uniformly in the odd prime power, the exact distribution of \(K\)-rational maximal isotropic kernels alongside rational two-torsion and Frobenius permutations; in particular it separates the two strata with equal rational two-torsion order.

## Limitations

This is a coefficient-parameter census, not an isomorphism-class census and not a census of distinct Richelot codomains. The classical matching description and parts of the splitting mechanism are standard; a previously recorded equivalent family-specific census in another parametrization remains a priority risk. No assertion about distinct target isomorphism classes, numerical zeta functions of the genus-two curves, or the geometry of all codomains is made. The finite checker is not an infinite proof. Independent validation has not been performed.

## References

1. V. Arul, J. Booher, S. R. Groen, E. W. Howe, W. Li, V. Matei, R. Pries, C. Springer, *Doubly isogenous genus-2 curves with \(D_4\)-action*, arXiv:2102.11419, first submitted 22 February 2021, equation (2.1) and Sections 2, 3, 5. https://arxiv.org/abs/2102.11419
2. N. Bruin, K. Doerksen, *The arithmetic of genus two curves with (4,4)-split Jacobians*, arXiv:0902.3480, first submitted 19 February 2009, Section 4 (quadratic splittings and descent of Richelot isogenies). https://arxiv.org/abs/0902.3480
3. *Magma Computational Algebra System*, Handbook, “Richelot Isogenies,” description of maximal-isotropic two-torsion kernels through quadratic splittings. https://magma.maths.usyd.edu.au/magma/handbook/text/1615
