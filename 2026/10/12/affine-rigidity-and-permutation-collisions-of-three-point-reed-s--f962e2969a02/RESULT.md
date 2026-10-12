# Affine rigidity and permutation collisions of three-point Reed–Solomon codes

## Finding
Let \(q=p^m\) be a prime power and let \(E\subseteq\mathbb F_q\) consist of exactly three distinct evaluation points. Consider the dimension-two Reed–Solomon encoder
\[
(a,b)\longmapsto\{ax+b:x\in E\}_{\mathrm{multiset}},\qquad (a,b)\in\mathbb F_q^2,
\]
where the receiver loses coordinate positions but receives the three symbols without any further error. Write \(H_E=\{x\mapsto ux+v:u\in\mathbb F_q^*,\ v\in\mathbb F_q,\ uE+v=E\}\). Every constant-polynomial output has exactly one preimage; every nonconstant-polynomial output has exactly \(|H_E|\) preimages, and there are \(q(q-1)/|H_E|\) distinct nonconstant outputs.

The complete distribution of the stabilizer sizes across the \(\binom q3\) possible **unlabeled evaluation sets** is as follows. All unspecified counts are zero.

* If \(p=2\): \(N_3(q)=q(q-1)/3\) when \(3\mid(q-1)\), otherwise \(N_3(q)=0\); and \(N_1(q)=\binom q3-N_3(q)\).
* If \(p=3\): \(N_6(q)=q(q-1)/6\) and \(N_1(q)=\binom q3-N_6(q)\).
* If \(p\) is odd and \(p\ne3\): \(N_2(q)=q(q-1)/2\), \(N_3(q)=q(q-1)/3\) when \(3\mid(q-1)\), otherwise \(N_3(q)=0\); and \(N_1(q)=\binom q3-N_2(q)-N_3(q)\).

Here \(N_h(q)=|\{E\subseteq\mathbb F_q:|E|=3,\ |H_E|=h\}|\). In particular, a dimension-two, length-three Reed–Solomon code distinguishable under **arbitrary coordinate permutation alone** exists exactly when \(N_1(q)>0\). The smallest possible field is \(\mathbb F_8\): every one of its \(56\) three-point evaluation sets has trivial affine stabilizer and gives \(64\) distinct unordered codeword outputs. No such code exists over a field with fewer than eight elements.

## Assumptions and scope
The alphabet is the finite field \(\mathbb F_q\), where \(q\) is any prime power. The three evaluation points are distinct, and the message space is the two-dimensional space of polynomials \(ax+b\) of degree less than two. Codeword coordinates can be arbitrarily permuted and no insertion, deletion, or substitution occurs. A set \(E\), rather than an ordering of \(E\), is the object being counted. The term 'collision' means distinct message polynomials having the same output multiset. The output of a nonconstant polynomial consists of three distinct symbols; a constant polynomial yields a triple with three equal symbols. A positive permutation-only separation result does not imply correction of any positive number of edit errors.

## Proof
**1. Fiber–stabilizer equivalence.** For \(a\ne0\), the unordered output of \(f(x)=ax+b\) is the three-element set \(aE+b\). Two such outputs \(aE+b\) and \(a'E+b'\) agree if and only if the affine bijection \(x\mapsto (a/a')x+(b-b')/a'\) maps \(E\) to itself. Consequently the free right-composition action of \(H_E\) on the \(q(q-1)\) nonconstant affine polynomials has orbits of size \(|H_E|\), precisely the output fibers. Constant outputs are mutually distinct and cannot equal any nonconstant output. This proves the fiber count and shows that loss of ordering is invertible exactly when \(H_E=\{\mathrm{id}\}\).

**2. Possible stabilizers.** Since an affine map is uniquely determined by its values on two distinct points, the action of \(H_E\) on the three points of \(E\) is faithful; thus \(H_E\) embeds into \(S_3\). Its possible orders are \(1,2,3,6\).

If \(p\ne2\), an affine involution is \(x\mapsto 2c-x\) for a unique fixed point \(c\). It preserves a three-set precisely when that set is \(\{c-d,c,c+d\}\) with \(d\ne0\), an arithmetic-progression triple. In characteristic two, every nonidentity affine involution is a translation, which has no fixed points and cannot preserve an odd-cardinality set. Thus there are no stabilizers of even order for \(p=2\).

If \(p\ne3\), an affine map of order three must have a multiplier \(\omega\ne1\) satisfying \(\omega^3=1\), and has a unique fixed point \(c\). Its three-point orbits are exactly \(\{c+d,c+\omega d,c+\omega^2 d\}\) with \(d\ne0\). These exist precisely when \(3\mid(q-1)\). For such a triple, the average of its three entries is \(c\), which is not an element of the triple. In contrast, the fixed point of an involution stabilizing an odd three-set must lie in the set; and the average of an arithmetic-progression triple is its midpoint when \(p\ne3\). Therefore order-two and order-three stabilizers cannot coexist when \(p\ne3\).

If \(p=3\), every affine map of order three is a nonzero translation, and its three-point orbit is a coset of a one-dimensional \(\mathbb F_3\)-subspace of the additive group of \(\mathbb F_q\). These are exactly the arithmetic-progression triples. Their affine stabilizer acts as the full affine group of \(\mathbb F_3\), of order six; all other three-sets have trivial stabilizer. Hence the only stabilizer sizes in characteristic three are \(1\) and \(6\).

It remains to count the exceptional sets. For odd \(p\ne3\), the midpoint of an arithmetic-progression triple is unique; choosing the midpoint and an unordered pair \(\{d,-d\}\) gives \(q(q-1)/2\) distinct triples. For \(p=3\), there are \((q-1)/2\) additive subgroups of order three and \(q/3\) cosets of each, giving \(q(q-1)/6\) exceptional triples. For \(p\ne3\) and \(3\mid(q-1)\), each three-cycle orbit has unique center \(c\), and the \(q-1\) nonzero offsets form \((q-1)/3\) three-element orbits per center. The number of such triples is \(q(q-1)/3\). The order-two and order-three exceptional families are disjoint by the fixed-point argument. Subtracting their cardinalities from \(\binom q3\) proves the distribution in the Finding.

**3. Sharp alphabet threshold.** The prime powers below eight are \(2,3,4,5,7\). For \(q=2\), three distinct evaluation points do not exist. For \(q=3\) the unique three-set has stabilizer size six; for \(q=4\), all four triples have stabilizer size three; for \(q=5\), all ten triples have stabilizer size two; and for \(q=7\), the thirty-five triples split into twenty-one with stabilizer size two and fourteen with stabilizer size three. Thus none works. For \(q=8\), characteristic two eliminates involutions and \(3\nmid7\) eliminates order-three elements; every three-set is rigid. The example \(E=\{0,1,\alpha\}\), with \(\alpha\) any element of \(\mathbb F_8\setminus\{0,1\}\), is explicit. Because the encoder has \(8^2=64\) messages, there are exactly 64 distinct unordered outputs. This completes the proof.

## Verification
The attached standalone `verify.py` uses finite-field polynomial arithmetic and independently enumerates each three-set, every nonzero affine transformation, and (for fields through order nine) the unordered codeword outputs. It checks the formula over fields of orders \(2,3,4,5,7,8,9,11,13,16\). Run `python3 verify.py` with Python 3 and no external packages; the expected terminal marker is `VERIFY_OK`. In particular, the direct unordered-output test checks each predicted collision-fiber size for every three-set over fields of order at most nine. The infinite-field claims follow from the symbolic proof above, not from these finite samples.

## Relationship to prior work
Zhang, Sun, Zhang and Ge (2026) study Reed–Solomon codes against adversarial coordinate permutations followed by insertion and deletion errors and motivate an obstruction that exists even before editing: two messages could have the same unordered evaluations. Their published abstract and introductory text concern asymptotic field size and robust decoding, not the three-point stabilizer census here. Camps-Moreno, Lau, López and Santos (2025/2026) study global **coordinate-permutation automorphisms** of Reed–Solomon codes. Their Theorem IV.6 identifies affine permutations for \(1<k<n-1\), a regime that excludes the present \((n,k)=(3,2)\) case. Their Proposition IV.2 supplies a related one-direction inclusion. Neither global automorphism classification nor its excluded boundary case directly states the unordered-message collision-fiber distribution derived here. Con, Shpilka and Tamo (2024) construct two-dimensional Reed–Solomon insertion/deletion codes but their reported main result does not provide these finite-field three-point counts.

## Limitations
The result addresses loss of coordinate identities only; no nonzero edit-error capability is asserted. It counts unlabelled three-element evaluation sets but does not count ordered evaluation vectors separately. It does not classify permutation collisions of higher-degree polynomials or longer evaluation sets. Source overlap is not ruled out absolutely: full text of the 2026 permutation–insdel manuscript and of all earlier conference proceedings was not available for complete comparison, so a previously unindexed finite-field orbit enumeration remains possible. The verified finite examples support, but do not replace, the uniform algebraic proof.

## References
1. Y. Zhang, Y. Sun, X. Zhang, and G. Ge, *Random Reed–Solomon Codes Correcting Permutations, Insertions, and Deletions over Polynomial-Size Alphabets*, arXiv:2606.22344, first submitted 2026-06-21, https://arxiv.org/abs/2606.22344.
2. E. Camps-Moreno, J. B. Lau, H. H. López, and W. Santos, *The permutation group of Reed–Solomon codes over arbitrary points*, arXiv:2601.00122v1, 2025-12-31, especially Proposition IV.2, Theorem IV.6, and Example IV.9, https://arxiv.org/html/2601.00122v1.
3. R. Con, A. Shpilka, and I. Tamo, *Optimal Two-Dimensional Reed–Solomon Codes Correcting Insertions and Deletions*, IEEE Trans. Inf. Theory 70 (2024), 5012–5016, DOI:10.1109/TIT.2024.3387848.
