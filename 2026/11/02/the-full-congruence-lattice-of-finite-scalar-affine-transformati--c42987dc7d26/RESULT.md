# The full congruence lattice of finite scalar-affine transformation monoids

## Finding

Let \(q\) be any prime power, let \(r\ge 1\), and put \(V=\mathbb F_q^r\). The monoid
\[
S_{q,r}=\{(v,a):v\in V,\ a\in\mathbb F_q\},\qquad
(v,a)(w,b)=(v+aw,ab)
\]
consists of the scalar-affine self-maps \(x\mapsto ax+v\). Its **entire two-sided congruence lattice** has the following explicit description.

For every pair of \(\mathbb F_q\)-linear subspaces \(T\subseteq W\subseteq V\), define \(\rho_{T,W}\) by the following disjoint equivalence classes. Constants \((v,0)\) and \((w,0)\) are equivalent exactly when \(v-w\in W\). Invertible maps \((v,a)\) and \((w,b)\) are equivalent exactly when \(a=b\ne0\) and \(v-w\in T\). No constant is equivalent to a unit.

For every **nontrivial** subgroup \(H\le\mathbb F_q^\times\), define \(\sigma_H\) by declaring all constants equivalent and identifying two units \((v,a),(w,b)\) exactly when \(ab^{-1}\in H\), independently of their translations. No constant is equivalent to a unit. The preceding relations, together with the universal congruence, are **all** the congruences, each listed exactly once.

The inclusion order is the coordinatewise flag order \(\rho_{T,W}\subseteq\rho_{T',W'}\) if and only if \(T\subseteq T'\) and \(W\subseteq W'\), followed above its maximum \(\rho_{V,V}\) by the ordinary subgroup lattice of \(\mathbb F_q^\times\) (identify its trivial subgroup with \(\rho_{V,V}\)), followed by the universal congruence.

Write \({m\brack j}_q\) for a Gaussian binomial coefficient, \(\tau(m)\) for the positive-divisor count, and \(\Omega(m)\) for the number of prime factors counted with multiplicity (\(\Omega(1)=0\)). Then
\[
\boxed{\lvert\operatorname{Con}(S_{q,r})\rvert=
\sum_{w=0}^r{r\brack w}_q\sum_{t=0}^{w}{w\brack t}_q+\tau(q-1).}
\]
The longest strict inclusion chain has \(2r+\Omega(q-1)+1\) inclusions (and one more element than inclusions).

There is an additional sharp characteristic-two boundary in the **least commutative quotient**. For \(q>2\), it is the multiplicative monoid \((\mathbb F_q,\cdot)\), via \((v,a)\mapsto a\). For \(q=2\), it is the abelian translation group \((V,+)\) with a new absorbing zero, via \((v,1)\mapsto v\), \((v,0)\mapsto0_{\mathrm{abs}}\).

## Assumptions and scope

The two-sided congruences concern the associative multiplication of functions under composition, not vector-space congruences or monoid representations. All scalars in the linear part are from the *same base field* \(\mathbb F_q\), including zero. The rank \(r\) is any positive integer; arbitrary nonscalar linear transformations are **not** included. The field size is any prime power. The notation \(0_{\mathrm{abs}}\) denotes an adjoined absorbing point, distinct from the additive identity of \(V\).

## Proof

**1. The ideal and unit group.** The subset \(I=\{c_v=(v,0):v\in V\}\) is precisely the ideal of constants; the complement \(U=\{(v,a):a\in\mathbb F_q^\times\}\) is a group, \(U=V\rtimes\mathbb F_q^\times\). Left multiplication by \(g=(v,a)\in U\) sends \(c_x\) to \(c_{v+ax}\), while right multiplication of a constant by every element fixes that constant. The \(U\)-action on \(I\) is affine and transitive.

**2. Mixed classes force universality.** Suppose \(g\in U\) is congruent to a constant \(c_y\). Right multiplying by all constants \(c_x\) gives \(c_{g(x)}\sim c_y\); the bijectivity of \(g\) collapses every pair of constants. Left multiplying the original equivalence by \(g^{-1}\) shows the identity is congruent to some constant. Right multiplying this equivalence by an arbitrary \(s\in S_{q,r}\) now shows \(s\) is congruent to a constant, and hence everything is equivalent. Therefore any nonuniversal congruence has classes entirely inside \(I\) or entirely inside \(U\).

**3. The constant kernel is a subspace.** Invariance of the restricted equivalence on \(I\) under the affine group gives translation invariance and invariance under multiplication by every nonzero element of \(\mathbb F_q\). Thus the equivalence classes are exactly the cosets of a uniquely determined \(\mathbb F_q\)-linear subspace \(W\le V\): \(c_x\sim c_y\iff x-y\in W\).

**4. The unit kernel is a normal subgroup.** The restriction of the congruence to \(U\) is a group congruence, hence is described by a normal subgroup \(N\mathrel{\triangleleft}U\). If \(g\in N\), then \(g\sim1\). Multiplying this equality on the right by \(c_x\) shows \(g(x)-x\in W\) for every \(x\in V\). Write \(g=(v,a)\). This condition is \(v+(a-1)x\in W\) for every \(x\). If \(W\ne V\), then \(a=1\) necessarily, because any nonzero \(a-1\) multiplies \(V\) onto itself. Therefore \(N\le V\) consists precisely of translations in a subspace \(T\); normality under scalar dilations forces \(T\) to be \(\mathbb F_q\)-linear and the action condition forces \(T\subseteq W\). Conversely every such pair gives a two-sided congruence, verified directly from the displayed multiplication law.

If \(W=V\), the compatibility condition on \(N\) becomes vacuous. If the image of \(N\) under the scalar projection \(U\to\mathbb F_q^\times\) is trivial, then again \(N=T\) for a unique subspace \(T\le V\). If it contains \(a\ne1\), normality and the commutator of a scalar-\(a\) affine map with translations give every translation: indeed such commutators have translation components \((a-1)x\), which range over \(V\). Thus \(V\subseteq N\) and \(N=V\rtimes H\) for a subgroup \(H\le\mathbb F_q^\times\). These are all possible normal subgroups. For \(H=\{1\}\) the resulting congruence is the already counted flag \(\rho_{V,V}\); for larger \(H\) it is \(\sigma_H\). Again compatibility with multiplication is immediate because \(S_{q,r}/\sigma_H\) consists of an absorbing zero and the group \(\mathbb F_q^\times/H\). The universal congruence is the only remaining case.

**5. Lattice, size, and height.** Inclusions between flag relations are exactly inclusions in both of their subspaces. The number of dimension-\(w\) spaces \(W\) is \({r\brack w}_q\), and each contains \(\sum_{t=0}^w{w\brack t}_q\) possible \(T\), yielding the first sum. There are \(\tau(q-1)-1\) new scalar relations because \(\mathbb F_q^\times\) is cyclic, plus one universal relation. A maximal strict flag chain has \(2r\) steps: one can enlarge \(W\) to \(V\) in \(r\) steps and then enlarge \(T\) to \(V\) in another \(r\). A longest subgroup chain of the cyclic group has \(\Omega(q-1)\) steps, and the final universal step supplies one more.

**6. The least commutative quotient.** Any commutative congruence must identify every pair of constants, because \(c_vc_w=c_v\) and \(c_wc_v=c_w\). Thus it has \(W=V\). Its restriction to the group of units must contain the commutator subgroup \(U'\). For \(q>2\) there exists \(a\in\mathbb F_q^\times\setminus\{1\}\), and commutators between scalar dilations and translations generate all translations, so \(U'=V\), giving exactly \(\rho_{V,V}\) and quotient \(\mathbb F_q\) under multiplication. When \(q=2\), there is no nonidentity dilation; \(U=V\) is abelian, so the least commutative congruence is \(\rho_{\{0\},V}\). Its quotient is \(V\) with a new absorbing zero. The asserted sharp distinction follows.

## Verification

The accompanying `verify.py` independently builds the monoid multiplication table and the proposed partition relations, then checks stability under both left and right multiplication for every element. For monoids with at most nine elements, it independently enumerates **all set partitions** and retains exactly those satisfying both congruence axioms: the predicted list and exhaustive list agree for \((q,r)=(2,1),(2,2),(3,1)\). It also checks all predicted relations for \((q,r)=(3,2),(5,1)\), and over the extension field \(\mathbb F_4\) for ranks one and two, using a separate field-arithmetic implementation. The recorded output ends in `VERIFY_OK` and `EXTENSION_FIELD_VERIFY_OK`.

The complete statement for arbitrary \(q,r\) is proven in the preceding paragraphs; finite checks alone would not suffice. Example total congruence counts are \(4,13,5,17,6,5,20\) for the seven parameter cases in the order above.

## Relationship to prior work

Mesyan's 2025 work establishes the general least-commutative-congruence interpretation and calculates it for full/partial transformation monoids and other semigroup families, not for the restricted scalar-affine monoids here. The present complete lattice and its enumeration are stronger than a least-commutative-congruence determination alone. Shahzamanian and Steinberg study the affine monoid \(\operatorname{Aff}(\mathbb F_q)\) in its one-dimensional case, computing the quiver of the **complex monoid algebra**, not its two-sided congruence lattice; in particular, the representation-theoretic equivalence appearing in their paper is not the congruence on the transformation monoid classified here. Anagnostopoulou-Merkouri, Cirpons, Mitchell, and Tsalakou provide general algorithms for finite-index congruence enumeration, not this all-field-and-rank symbolic lattice formula.

The formulas for subspace counts, normal subgroups of affine unit groups, and the notion of a congruence itself are standard ingredients, not presented as new. The claimed contribution is their combination into an explicit complete two-sided congruence lattice with count, height, and exact least-commutative quotient for the whole scalar-affine family.

## Limitations

The proof is elementary and self-contained given standard finite-field linear algebra and the known correspondence between normal subgroups and group congruences. It does not classify **one-sided** congruences, nonscalar affine maps, or affine maps over arbitrary finite commutative rings with zero divisors. Any stronger historical theorem for an arbitrary group acting on a left-zero ideal might specialize to some or all of this result; the novelty comparison cannot establish absolute historical priority.

## References

1. Z. Mesyan, *Conjugacy and Least Commutative Congruences in Semigroups*, arXiv:2503.02148v1, first public 2025-03-04. https://arxiv.org/abs/2503.02148
2. M. H. Shahzamanian and B. Steinberg, *The quiver of an affine monoid*, arXiv:2009.12340v2 (2021). https://arxiv.org/abs/2009.12340
3. M. Anagnostopoulou-Merkouri, R. Cirpons, J. D. Mitchell, and M. Tsalakou, *Computing finite index congruences of finitely presented semigroups and monoids*, arXiv:2302.06295v4 (2025). https://arxiv.org/abs/2302.06295
