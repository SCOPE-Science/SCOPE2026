# The thirty-two quadratic descents of a six-branch Humbert–Edge curve over \(\mathbf F_7\)

## Finding

Let \(\eta=3\), a nonsquare in \(\mathbf F_7\). For each vector \(\epsilon=(\epsilon_0,\ldots,\epsilon_4)\in\{0,1\}^5\), put \(d_i=\eta^{\epsilon_i}\), and let \(X_\epsilon\subset\mathbf P^5_{\mathbf F_7}\) have coordinates \([U_0:U_1:U_2:U_3:U_4:Z]\) and equations

\[
U_i^2=\frac{d_i}{d_0}U_0^2-i d_iZ^2,\qquad i=1,2,3,4.
\]

Each \(X_\epsilon\) is smooth and geometrically connected of genus \(17\). Their zeta numerators have precisely three forms:

\[
L(X_\epsilon,T)=(1+7T^2)^9(1-4T+7T^2)^{m_\epsilon}
 (1+4T+7T^2)^{8-m_\epsilon},
\]

where \(m_\epsilon\in\{1,3,5\}\). Among the \(32\) distinct **coefficient-marked** vectors, exactly \(2\) have \(m_\epsilon=1\), exactly \(12\) have \(m_\epsilon=3\), and exactly \(18\) have \(m_\epsilon=5\). Equivalently, the counts of \(\mathbf F_7\)-points have spectrum

| \(\#X_\epsilon(\mathbf F_7)\) | Number of marked vectors |
| ---: | ---: |
| \(0\) | \(18\) |
| \(16\) | \(12\) |
| \(32\) | \(2\) |

Every member has exactly \(160\) points over \(\mathbf F_{49}\). The Jacobian of every member has \(7\)-rank \(8\), \(a\)-number \(9\), and Newton slopes \(0^{[8]},(1/2)^{[18]},1^{[8]}\).

The complete zeta function is \(Z(X_\epsilon/\mathbf F_7,T)=L(X_\epsilon,T)/((1-T)(1-7T))\); its coefficients determine point counts over **every** finite extension. The multiplicities concern the explicitly marked equations, not classes of projective isomorphism.

## Assumptions and scope

The ground field has characteristic \(7\). The five residues \(0,1,2,3,4\) are distinct, and \(3\) is a fixed nonsquare. For \(Z\ne0\), writing \(t=U_0^2/(d_0Z^2)\) makes the function field

\[
\mathbf F_7(t)\big(\sqrt{d_0t},\sqrt{d_1(t-1)},\sqrt{d_2(t-2)},\sqrt{d_3(t-3)},\sqrt{d_4(t-4)}\big).
\]

The geometric branch set of the resulting \((\mathbf Z/2)^5\)-cover of \(\mathbf P^1\) is exactly \(\{0,1,2,3,4,\infty\}\). It is the complement of two points of \(\mathbf P^1(\mathbf F_7)\); all unordered pairs of rational points are projectively equivalent, so this branch configuration is natural up to projective change of base coordinates. The \(32\) square-class choices above label arithmetic descents with fixed branch-point ordering and coordinate choices; no claim is made that they represent \(32\) different abstract curves.

## Proof

**Geometry.** The five classes of \(t-i\), \(0\le i\le4\), are linearly independent in \(\overline{\mathbf F}_7(t)^\times/\overline{\mathbf F}_7(t)^{\times2}\), as their valuations at the five distinct zeros are independent. Thus the cover has degree \(32\) and is geometrically connected. It is tame; each of the five finite branch points and infinity has inertia of order \(2\). Riemann–Hurwitz yields

\[
2g(X_\epsilon)-2=32(-2)+6\cdot16=32,
\qquad g(X_\epsilon)=17.
\]

The homogeneous equations form a smooth complete intersection: away from infinity at most one of \(U_0,\ldots,U_4\) vanishes, and differentiating the four quadrics gives rank \(4\), using \(Z\ne0\) if an equation's distinguished coordinate vanishes. At infinity \(Z=0\), all five \(U_i\) are nonzero and the same rank condition holds. Hence the displayed complete intersection is the smooth projective model of the field extension.

**Character factors.** Let \(S\) run through the nonempty subsets of \(\{0,1,2,3,4\}\). The quadratic character indexed by \(S\) has quotient

\[
H_{S,\epsilon}:\quad v^2=\bigg(\prod_{i\in S}d_i\bigg)
\prod_{i\in S}(t-i),
\]

with the smooth projective completion understood. The genus is \(\lfloor(|S|-1)/2\rfloor\). The representations of the elementary abelian Galois group on first étale cohomology decompose into its one-dimensional characters (the group order \(32\) is prime to \(7\)). The zeta numerator of \(X_\epsilon\) is consequently the product of those of \(H_{S,\epsilon}\). There are \(10\) genus-one quotients for \(|S|=3\), another \(5\) for \(|S|=4\), and one genus-two quotient for \(|S|=5\); smaller subsets contribute no first cohomology. Their genera sum to \(15+2=17\).

For the untwisted case \(d_i=1\), enumerate the \(7\) finite values of \(t\) and the infinity fiber on each elliptic quotient. The trace \(a_S=8-\#H_{S,0}(\mathbf F_7)\) is:

| \(S\) | \(a_S\) | \(S\) | \(a_S\) | \(S\) | \(a_S\) |
|---|---:|---|---:|---|---:|
| \(012\) | 0 | \(013\) | 4 | \(014\) | 0 |
| \(023\) | -4 | \(024\) | 0 | \(034\) | 0 |
| \(123\) | 0 | \(124\) | 4 | \(134\) | -4 |
| \(234\) | 0 | \(0123\) | 0 | \(0124\) | -4 |
| \(0134\) | 0 | \(0234\) | -4 | \(1234\) | 0 |

Thus \(9\) elliptic factors have trace \(0\), \(4\) have trace \(-4\), and \(2\) have trace \(+4\). Twisting a subset quotient by the nonsquare \(3\) changes the sign of its elliptic trace according to \((-1)^{\sum_{i\in S}\epsilon_i}\). The genus-two quotient \(H_{\{0,1,2,3,4\},0}\), whose equation is \(v^2=t(t-1)(t-2)(t-3)(t-4)\), has exactly \(8\) points over \(\mathbf F_7\) and \(46\) over \(\mathbf F_{49}\). Newton's identities and the genus-two functional equation give its numerator

\[
1-2T^2+49T^4=(1-4T+7T^2)(1+4T+7T^2).
\]

Its nonsquare quadratic twist has the same numerator, since that polynomial is even. Therefore the genus-two contribution always supplies one trace-\(+4\) and one trace-\(-4\) ordinary elliptic factor. Collecting the \(15\) elliptic factors and these two quadratic factors establishes the asserted zeta formula, with \(m_\epsilon\) the number of trace-\(+4\) factors.

**All thirty-two twists.** Direct counting over the base line gives a short exhaustive arithmetic proof of the multiplicity distribution. For each finite \(t\) the number of points in the fiber is the product over \(i\) of the number of square roots of \(d_i(t-i)\). For \(t=0,1,2,3,4\), a nonempty fiber occurs for exactly two bit vectors each, with patterns respectively `*1101`, `0*110`, `00*11`, `100*1`, and `0100*`, with the `*` bit arbitrary. Each of these fibers contains \(16\) points. The fibers over \(t=5\) and \(t=6\) are nonempty only for `10100` and `11010`, respectively, and have \(32\) points each. Infinity has \(16\) points only for `00000` and `11111`. These \(14\) vectors are pairwise distinct: twelve give \(16\) points, two give \(32\), and the other eighteen give none. Since the zeta formula has first trace \(4m_\epsilon-4(8-m_\epsilon)=8m_\epsilon-32\), it gives

\[
\#X_\epsilon(\mathbf F_7)=8-(8m_\epsilon-32)=40-8m_\epsilon.
\]

This determines \(m_\epsilon=5,3,1\) in the asserted multiplicities. Over \(\mathbf F_{49}\), every element of \(\mathbf F_7^\times\) becomes a square and the \(32\) models are all isomorphic as marked quadratic extensions. Squaring Frobenius eigenvalues yields \(9(-14)+8(2)=-110\), hence \(\#X_\epsilon(\mathbf F_{49})=1+49-(-110)=160\), independently verified by direct square-root fiber enumeration.

**Newton slopes and integral invariants.** Over \(\mathbf F_7\), an elliptic factor of trace \(0\) is supersingular, while trace \(\pm4\) is ordinary. The genus-two factor is ordinary, because its numerator factors into two ordinary elliptic Weil polynomials; its \(7\)-rank is \(2\) and its \(a\)-number is zero. The character projectors have denominator dividing \(32\), so they give an isogeny to the quotient Jacobians with kernel of \(2\)-power order. The associated \(7\)-divisible groups are therefore isomorphic. The nine supersingular elliptic factors contribute \(a\)-number \(9\), and the eight ordinary elliptic components contribute \(7\)-rank \(8\). Their Newton slopes are exactly the stated multiset.

## Verification

The supplied standalone `verify.py` uses only Python's standard library. It enumerates every coefficient-marked twist over \(\mathbf F_7\), counts all \(15\) elliptic quotient traces independently, counts the genus-two quotient over \(\mathbf F_7\) and \(\mathbf F_{49}\), and cross-checks each of the \(32\) base-field counts using three independent routes, including direct enumeration of the homogeneous four-quadric model in projective five-space. It also explicitly enumerates all \(32\) models over \(\mathbf F_{49}\) using field arithmetic with \(i^2=-1\). Running `python3 verify.py` yields `VERIFY_OK` after all assertions. This finite verification supplements, rather than replaces, the function-field, Riemann–Hurwitz and character-decomposition arguments.

## Relationship to prior work

Castorena and Frías-Medina (arXiv:2106.00813, first public June 1, 2021) established the geometry and genus of type-five Humbert–Edge curves and related their moduli to genus-two hyperelliptic curves. Auffarth, Lucchini Arteche and Rojas (arXiv:1905.12690) established the general Jacobian isogeny decomposition. Martínez-Núñez (arXiv:2303.18056) generalized decomposition techniques. Their underlying constructions and group-theoretic decomposition are prior work, not new claims here. The contribution here is the complete explicit arithmetic classification of the \(32\) marked descents attached to this six-rational-branch configuration over \(\mathbf F_7\), including the three Frobenius spectra and their exact multiplicities. A separate earlier calculation for a different type-five Humbert–Edge model over \(\mathbf F_5\) does not imply the \(\mathbf F_7\) twist spectrum.

## Limitations

This is an exact result for the specified geometric six-branch configuration over \(\mathbf F_7\) and the \(32\) marked quadratic descents. The labels can yield abstractly isomorphic curves; counts are not an isomorphism-class census. The general decomposition is not new, nor is a claim made about all Humbert–Edge curves over arbitrary finite fields. The zeta polynomial is derived mathematically from finitely verified quotient data, so there is no assertion that finite experiments prove an infinite identity on their own. Previously unindexed arithmetic calculations may overlap with this specific finite-field census.

## References

1. A. Castorena and J. B. Frías-Medina, *Geometric aspects on Humbert-Edge's curves of type 5, Kummer surfaces and hyperelliptic curves of genus 2*, arXiv:2106.00813 (v1, 2021-06-01), https://arxiv.org/abs/2106.00813.
2. R. Auffarth, G. Lucchini Arteche and A. M. Rojas, *A decomposition of the Jacobian of a Humbert-Edge curve*, arXiv:1905.12690 (first public 2019-05-29), https://arxiv.org/abs/1905.12690.
3. G. Martínez-Núñez, *Decomposition of Jacobians of Generalized Fermat Curves*, arXiv:2303.18056 (first public 2023-03-31), https://arxiv.org/abs/2303.18056.
