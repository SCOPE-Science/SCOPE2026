# A binary-field criterion for simultaneously complete mappings of finite commutative rings

## Finding

For a finite nonzero commutative unital ring \(R\), call a bijection \(\alpha:R\to R\) *simultaneously complete for addition and multiplication* if both maps
\[
\sigma_\alpha(x)=x+\alpha(x),\qquad\theta_\alpha(x)=x\alpha(x)
\]
are bijections of the underlying set. Such a map selects a common transversal of the additive and multiplicative tables using the same rows and columns.

**Theorem.** Such an \(\alpha\) exists if and only if
\[
R\cong\prod_{i=1}^{t}\mathbb F_{2^{d_i}},\qquad t\ge1,\quad d_i\ge2\ \text{for every }i.
\]
Whenever the condition holds, take any \(a_i\in\mathbb F_{2^{d_i}}\setminus\{0,1\}\) and put
\[
\alpha((x_i)_{i=1}^{t})=(a_i x_i)_{i=1}^{t}.
\]
This explicitly realizes all rings in the classification.

**The two-operation obstruction is genuine.** On \(R=\mathbb F_2\times\mathbb F_4\), multiplication alone has the complete mapping \((u,v)\mapsto(u,av)\), for any \(a\in\mathbb F_4\setminus\{0,1\}\). Addition alone also has a complete mapping: as an additive group, \(R\) is a three-dimensional \(\mathbb F_2\)-vector space, which can be identified with the additive group of \(\mathbb F_8\); multiplication by a scalar \(b\in\mathbb F_8\setminus\{0,1\}\) makes both the chosen map and its sum with the identity invertible. Nevertheless the theorem forbids **one common** complete permutation, since \(R\) has an \(\mathbb F_2\) factor.

## Assumptions and scope

The ring is associative, commutative, finite, nonzero and possesses a multiplicative identity distinct from zero. No additivity, multiplicativity, or polynomiality is assumed of \(\alpha\). The three maps \(\alpha\), \(\sigma_\alpha\), and \(\theta_\alpha\) must be permutations of the *entire* finite underlying set, including zero divisors and zero. Repeated factors and arbitrary extension degrees are allowed. The trivial one-element ring is excluded; if included by a different convention, it vacuously has a simultaneous complete mapping and must be added separately.

## Proof

**1. Principal ideals cannot decrease along a permutation cycle.** For a finite commutative unital ring, write \((x)=xR\) for the principal ideal of \(x\). If a permutation \(\pi\) obeys \((\pi(x))\subseteq(x)\) for every \(x\), then every inclusion is equality: iterate along the finite \(\pi\)-cycle and obtain a cyclic chain of ideal inclusions.

Suppose \(\alpha\), \(\sigma=\sigma_\alpha\), and \(\theta=\theta_\alpha\) are permutations. Define a further permutation
\[
\delta(x)=x\alpha^{-1}(x)=\theta(\alpha^{-1}(x)).
\]
Both \(\theta(x)=x\alpha(x)\) and \(\delta(x)=x\alpha^{-1}(x)\) lie in \((x)\). By the preceding observation,
\[
(\theta(x))=(x)=(\delta(x)) \quad\text{for every }x\in R.
\]
Set \(x=\alpha(y)\) in the second equality and use \(\delta(\alpha(y))=\theta(y)\). It follows that
\[
(\alpha(y))=(\theta(y))=(y).
\]
In particular \(\alpha\) preserves each principal ideal class and \(\alpha(0)=0\). Moreover,
\[
(y)=(\theta(y))=(y\alpha(y))=(y)(\alpha(y))=(y^2).
\]
Thus for every \(y\in R\) there is \(b\in R\) such that \(y=y^2b\). Iterating gives \(y=y^k b^{k-1}\) for every positive integer \(k\). If \(y\) were nilpotent it would therefore be zero. Hence \(R\) is reduced.

Every finite commutative reduced unital ring is a finite direct product of fields. Indeed finite rings are Artinian, their Jacobson radical is nilpotent and here zero, and the commutative Artinian semisimple decomposition gives
\[
R\cong F_1\times\cdots\times F_t
\]
for finite fields \(F_i\) with \(|F_i|=q_i\).

**2. Factor supports are preserved.** For \(x=(x_i)_i\in R\), define \(\operatorname{supp}(x)=\{i:x_i\ne0\}\). Over a product of fields the ideal \((x)\) is uniquely determined by this support. Since \((\alpha(x))=(x)\), the map \(\alpha\) preserves \(\operatorname{supp}(x)\); the map \(\theta\) also preserves it by the equality above. For each coordinate \(i\), both maps restrict to permutations of the singleton-support stratum
\[
E_i=\{(0,\dots,0,u,0,\dots,0):u\in F_i^\times\}.
\]
These permutations obey \(\theta(u)=u\alpha(u)\) in the field \(F_i\), identifying elements of \(E_i\) with their unique nonzero coordinates.

**3. An odd-order residue field is impossible.** Suppose \(q_i\) is odd. The product of all elements of \(F_i^\times\) is \(-1\): pair each non-self-inverse element with its inverse, leaving only \(1\) and \(-1\). Because \(\alpha\) and \(\theta\) both permute \(E_i\), multiplying the relation \(\theta(u)=u\alpha(u)\) over \(F_i^\times\) gives
\[
-1=\prod_{u\in F_i^\times}\theta(u)
=\Big(\prod_{u\in F_i^\times}u\Big)
\Big(\prod_{u\in F_i^\times}\alpha(u)\Big)
=(-1)^2=1,
\]
a contradiction in odd characteristic. Thus every factor has characteristic two.

**4. A two-element residue field is impossible.** If \(F_i=\mathbb F_2\), the stratum \(E_i\) contains just one element \(e_i\), the coordinate idempotent. Support preservation implies \(\alpha(e_i)=e_i\); also \(\alpha(0)=0\). In characteristic two,
\[
\sigma(0)=0=\sigma(e_i)=e_i+e_i,
\]
contradicting injectivity. Therefore \(q_i\) is a power of two strictly larger than two, hence \(q_i=2^{d_i}\) with \(d_i\ge2\).

**5. Sufficiency.** Conversely, let \(R=\prod_i\mathbb F_{2^{d_i}}\) with \(d_i\ge2\). Choose \(a_i\ne0,1\) in each factor. The map \(\alpha((x_i))=(a_i x_i)\) is bijective. Also
\[
\sigma_\alpha((x_i))=((1+a_i)x_i),\qquad
\theta_\alpha((x_i))=(a_i x_i^2).
\]
All \(1+a_i\) and \(a_i\) are nonzero, while squaring is a field automorphism in characteristic two. Both maps are therefore bijective. This establishes both directions. \(\square\)

## Verification

The accompanying standalone script `verification.py` uses only the Python standard library. It enumerates **every permutation** on twelve finite rings without the property and two with it, all of cardinality at most nine. The negative cases are \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb Z/4,\mathbb Z/6,\mathbb Z/8,\mathbb Z/9,\mathbb F_2[\epsilon]/(\epsilon^2),\mathbb F_2\times\mathbb F_2,\mathbb F_2\times\mathbb F_3,\mathbb F_2\times\mathbb F_4,\mathbb F_3\times\mathbb F_3\). The two positive cases are \(\mathbb F_4\) and \(\mathbb F_8\), admitting respectively two and six simultaneous complete permutations. The script also verifies *all scalar witnesses* in \(\mathbb F_4,\mathbb F_8,\mathbb F_{16}\), and explicit coordinatewise witnesses in \(\mathbb F_4\times\mathbb F_4,\mathbb F_4\times\mathbb F_8,\mathbb F_8\times\mathbb F_8\). Execute `python3 verification.py` in the directory containing that file. These finite checks are supplementary sanity tests, **not** substitutes for the argument over arbitrary finite rings.

## Relationship to prior work

Araújo, Bentz, Cameron, Hendrey and Kinyon [1] prove multiplicative regularity for finite semigroups with complete mappings (Theorem 2.1) and preservation of Green-class structure (Theorem 3.3). Their Problem 15.12 specifically asks for simultaneous completeness with multiple operations, including addition and multiplication of finite rings. Those established one-operation facts inform the principal-ideal argument but do not by themselves classify a *common* permutation for both operations. The theorem above establishes precisely the commutative-unital finite-ring existence criterion, and it provides explicit witnesses in every affirmative case.

Classical complete permutation-polynomial work, such as Zieve [2], studies bijectivity of \(f\) and \(x+f(x)\) in finite fields, without requiring the extra bijection \(x f(x)\) in the abstract consulted. The result here imposes all three requirements simultaneously and treats finite products and nilpotent obstructions. An equivalent unindexed theorem under other terminology remains possible; no uniqueness or priority assertion follows just from unsuccessful searches.

## Limitations

The theorem is an **existence classification** for finite nonzero commutative rings with identity; it does not enumerate all successful permutations, analyze arbitrary infinite rings, or classify noncommutative finite rings. Computation is exhaustive only for each explicitly listed small ring, not for the infinite class. The independent audit has not been performed. Bibliographic completeness beyond the inspected sources is not guaranteed.

## References

[1] J. Araújo, W. Bentz, P. J. Cameron, K. Hendrey, and M. Kinyon, *Complete Mappings of Semigroups*, arXiv:2608.25092v1 (25 August 2026), §§2–3 and Problem 15.12. https://arxiv.org/html/2608.25092v1

[2] M. E. Zieve, *Permutation polynomials induced from permutations of subfields, and some complete sets of mutually orthogonal Latin squares*, arXiv:1312.1325 (2013), https://arxiv.org/abs/1312.1325 (abstract used for scope comparison).
