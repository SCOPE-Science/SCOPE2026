# Odd-power complete mappings of finite Clifford semigroups with nilpotent groups

## Finding

Let \(S\) be a nonempty finite Clifford semigroup whose maximal subgroups are nilpotent. For an odd integer \(k\ge3\), call a bijection \(\alpha:S\to S\) a \(k\)-complete mapping if \(\theta_k(x)=x\alpha(x)^k\) is also bijective. Then
\[
S\text{ has a }k\text{-complete mapping}\quad\Longleftrightarrow\quad
\text{the Sylow-}2\text{ subgroup of each maximal subgroup is trivial or noncyclic}.
\]
The criterion is independent of the chosen odd \(k\). Moreover, every \(k\)-complete mapping of a finite Clifford semigroup, for any integer \(k\ge1\), fixes each maximal subgroup setwise. In particular, cross-fiber permutations can never rescue a failed local power-complete mapping.

## Assumptions and scope

A finite Clifford semigroup is a strong semilattice of finite groups: \(S=\bigsqcup_{e\in E}G_e\), where \(E\) is a finite meet semilattice and \(G_eG_f\subseteq G_{e\wedge f}\). Equivalently, \(S\) is a semigroup that is both inverse and completely regular, or a semilattice of groups. Nilpotence is an assumption on each group \(G_e\), not on the semilattice or on the connecting homomorphisms. Nilpotent finite groups decompose as direct products of their Sylow subgroups. Trivial groups are permitted. We require \(S\) finite, nonempty, and \(k\) odd with \(k\ge3\) for the classification; the subgroup-preservation lemma applies to every \(k\ge1\).

The exponent \(\exp G\) is the least common multiple of the element orders of a finite group \(G\). The Sylow-\(2\) subgroup of an odd-order group is regarded as trivial.

## Proof

**1. Fiber rigidity.** Write \(\gamma(x)=e\) when \(x\in G_e\). If \(x\in G_e\) and \(\alpha(x)\in G_f\), then \(\gamma(\theta_k(x))=e\wedge f\), because positive powers of elements of \(G_f\) stay in \(G_f\). Let \(h(e)=|\{d\in E:d\le e\}|\), an integer strictly increasing under strict increases of semilattice order. Since \(e\wedge f\le e\),
\[
h(\gamma(\theta_k(x)))\le h(\gamma(x))\qquad (x\in S).
\]
As \(\theta_k\) is a permutation, summing over all \(x\) makes the two sides equal. Equality therefore holds termwise. Strict monotonicity on comparable elements implies \(e\wedge f=e\), hence \(e\le f\). Thus \(h(\gamma(\alpha(x)))\ge h(\gamma(x))\) for every \(x\). Since \(\alpha\) is also a permutation, summation and termwise equality now imply \(f=e\). This proves that \(\alpha(G_e)=G_e\) for each \(e\). The same is then true of \(\theta_k\). Conversely, combining arbitrary local \(k\)-complete maps on the disjoint groups yields a global \(k\)-complete map, since \(x\) and \(\alpha(x)\) lie in the same group. Consequently, for every \(k\ge1\),
\[
S\text{ has a }k\text{-complete map}\Longleftrightarrow
\text{each }G_e\text{ has one}.
\]
No property of the connecting homomorphisms is used.

**2. Positive construction for a nilpotent group.** Let \(G\) be nilpotent with trivial or noncyclic Sylow-\(2\) subgroup. Decompose \(G=P\times Q\) where \(P\) is its Sylow-\(2\) subgroup and \(Q\) has odd order. Suppose \(k\ge3\) is odd. If \(P\) is nontrivial, it is noncyclic, so the Hall--Paige theorem supplies a permutation \(\beta:P\to P\) such that \(p\mapsto p\beta(p)\) is a permutation. Set \(E_P=\exp P\). Because \(k\) is odd, \(\gcd(k,E_P)=1\); choose an integer \(\ell\) with \(k\ell\equiv1\pmod{E_P}\). Put \(\alpha_P(p)=\beta(p)^\ell\). Raising to the power \(\ell\) permutes \(P\), and
\[
p\alpha_P(p)^k=p\beta(p)^{k\ell}=p\beta(p).
\]
Thus \(\alpha_P\) is \(k\)-complete. If \(P\) is trivial, use the unique map.

Let \(m=\exp Q\), an odd integer. For each odd prime \(r\mid m\), choose a residue \(a_r\in\mathbb Z/r\mathbb Z\) with \(a_r\ne0\) and \(1+ka_r\ne0\). At most two residues are forbidden, so such a choice exists even for \(r=3\). The Chinese remainder theorem produces a positive integer \(a\) with \(a\equiv a_r\pmod r\) for all \(r\mid m\). Hence \(\gcd(a,m)=\gcd(1+ka,m)=1\). Both power maps \(q\mapsto q^a\) and \(q\mapsto q^{1+ka}\) permute \(Q\): their inverses are other power maps, since exponents are invertible modulo \(m\). Set \(\alpha_Q(q)=q^a\). For \(m=1\), choose \(a=1\) instead. The product map
\[
\alpha_G(p,q)=(\alpha_P(p),q^a),\qquad
\theta_k(p,q)=(p\beta(p),q^{1+ka})
\]
is a pair of permutations, as required.

**3. Sharp obstruction when the Sylow-\(2\) subgroup is cyclic.** Conversely, suppose \(G=P\times Q\) where \(P=C_{2^r}\), \(r\ge1\), and \(Q\) has odd order. Let \(\pi:G\to P\) be projection and denote
\[
U=\prod_{g\in G}\pi(g)\in P.
\]
The product is well defined because \(P\) is abelian. Every element of \(P\) occurs exactly \(|Q|\) times, so \(U=(\prod_{p\in P}p)^{|Q|}=z\), the unique involution of \(P\). If \(\alpha\) and \(\theta_k\) were permutations, their projected products would each equal \(U\). Multiplying the factors in \(P\) and using \(\theta_k(g)=g\alpha(g)^k\) yields \(U=U^{k+1}\) and therefore \(U^k=1\). For odd \(k\), however, \(U^k=z\ne1\), a contradiction.

**4. Assemble over the semilattice.** Every finite nilpotent group has one of the three Sylow-\(2\) types: trivial, nontrivial cyclic, or noncyclic. Steps 2 and 3 provide the exact local criterion for odd \(k\); Step 1 makes it equivalent to the global criterion for every finite Clifford semigroup in the statement. \(\square\)

## Verification

The accompanying standard-library Python file `verify.py` constructs witnesses for \(45\) group/exponent combinations, including nonabelian dihedral and Heisenberg factors; exhaustively rejects \(8\) cyclic group/exponent instances; exhaustively enumerates all permutations of four two-level Clifford semigroups; and checks \(765\) CRT residue cases. Its output is:

```text
PRODUCT_WITNESSES=45 CYCLIC_OBSTRUCTIONS=8 CLIFFORD_EXHAUSTIVE=4 CRT_CASES=765 VERIFY_OK
```

Run with `python3 verify.py`. These are independent finite checks of the explicit construction and obstruction, not a substitute for the all-orders proof above. The proof assumes the established Hall--Paige theorem for ordinary group complete mappings; it does not reprove that theorem.

## Relationship to prior work

Araújo, Bentz, Cameron, Hendrey and Kinyon introduce power-exponent \(k\)-complete maps in Definition 15.1 and identify their classification for classes including Clifford semigroups as Problem 15.8. Their group Hall--Paige statement and inverse-semigroup existence theorem concern ordinary complete mappings (\(k=1\)), and do not classify odd exponents \(k\ge3\). Eberhard, Manners and Mrazović supply a modern source for the established Hall--Paige theorem used in the construction. The earlier \((K,\lambda)\)-complete maps of Hsu and Keedwell concern cycle-length sequences and are a different notion despite their similar name.

The new assertion combines (i) a permutation rigidity argument in the idempotent semilattice and (ii) an explicit factorwise conversion between ordinary and odd-power complete mappings for all finite nilpotent groups. It neither asserts a classification for arbitrary nonnilpotent maximal subgroups nor addresses infinite semigroups.

## Limitations

This gives existence, not the number or cycle-type distribution of all admissible permutations. It invokes Hall--Paige as a known theorem rather than supplying a new proof of that theorem. The extension to groups that are not nilpotent is open in this statement. Finite computational checks cover examples only. Equivalence to an older result formulated using a different kind of orthomorphism cannot be absolutely excluded by a literature search.

## References

1. J. Araújo, W. Bentz, P. J. Cameron, K. Hendrey, and M. Kinyon, *Complete Mappings of Semigroups*, arXiv:2608.25092v1 (first public posting 2026-08-25), Definition 15.1, Problem 15.8, Theorem 1.1, Theorem 10.1. https://arxiv.org/abs/2608.25092
2. S. Eberhard, F. Manners, and R. Mrazović, *An asymptotic for the Hall--Paige conjecture*, arXiv:2003.01798v2 (2022), Introduction and Theorem 1.1. https://arxiv.org/abs/2003.01798
3. D. F. Hsu and A. D. Keedwell, *Generalized complete mappings, neofields, sequenceable groups and block designs. I*, Pacific J. Math. 111 (1984), 317--335, Definitions 2.4--2.5. https://msp.org/pjm/1984/111-2/pjm-v111-n2-p05-s.pdf
