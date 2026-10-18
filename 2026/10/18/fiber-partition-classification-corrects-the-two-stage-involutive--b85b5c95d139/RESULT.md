# Fiber-partition classification corrects the two-stage involutive-bisemilattice census

## Finding

Let \(a,b\geq 1\). Consider involutive bisemilattices that are Płonka sums of exactly two **nontrivial** Boolean algebras \(B_0=\mathcal P([a])\) and \(B_1=\mathcal P([b])\), with index chain \(0<1\). The only nonidentity structure map is an arbitrary Boolean homomorphism \(p:B_0\to B_1\). Let \(f:[b]\to[a]\) be its finite Stone-dual function, so \(p(S)=f^{-1}(S)\).

**Complete classification.** Two such Płonka sums with the same \(a,b\) are isomorphic if and only if the multisets of *positive sizes* of the fibers of their dual functions coincide. Thus the isomorphism classes are indexed by integer partitions \(\lambda\vdash b\) having at most \(a\) parts, not merely by the number of nonempty fibers. The exact number of types is

\[
N(a,b)=\sum_{r=1}^{\min(a,b)}p_r(b)=[z^b]\prod_{j=1}^{a}(1-z^j)^{-1},
\]

where \(p_r(b)\) counts partitions of \(b\) into exactly \(r\) positive parts. The generating product includes a formal constant term, but only \(b\geq1\) is in the theorem's scope.

**Automorphisms.** Write \(r=\ell(\lambda)\) and \(m_s=|\{i:\lambda_i=s\}|\). For the corresponding Płonka sum \(P_\lambda\),

\[
|\operatorname{Aut}(P_\lambda)|=(a-r)!\prod_{s\geq1}(s!)^{m_s}m_s!.
\]

Consequently its labeled transition maps form an orbit of cardinality \(a!b!/|\operatorname{Aut}(P_\lambda)|\).

**Sharp rank-only failure.** The formula \(N(a,b)=\min(a,b)\) holds if and only if \(a=1\) or \(b\leq3\). The first counterexample measured by the sum of component cardinalities has \(a=2,b=4\): the two functions

\[
f=(1,1,1,2),\qquad g=(1,1,2,2)
\]

both have image size \(2\), but fiber partitions \((3,1)\) and \((2,2)\). Their two Płonka sums both have \(2^2+2^4=20\) elements, yet are not isomorphic. For this fixed shape there are **three**, not two, isomorphism classes, corresponding to partitions \((4)\), \((3,1)\), and \((2,2)\).

## Assumptions and scope

Every Boolean algebra is finite and nontrivial, its homomorphisms preserve zero, unit, joins, meets and complementation, and the Płonka index semilattice is the fixed two-point chain \(0<1\). All transition homomorphisms are allowed, including noninjective and nonsurjective maps. The operation signature is the standard involutive-bisemilattice signature \((\vee,\wedge,\neg,0,1)\), with constants in the lower-index component. The classification is of isomorphism types (not merely equivalence classes under a preselected arbitrary relabeling). No classification of systems with three or more fibers is asserted.

## Proof

**1. Intrinsic recovery of the two Boolean components.** In the Płonka sum, if \(x\) belongs to component \(B_i\), then \(x\vee\neg x=1_i\), the top of that Boolean component. The two values \(1_0,1_1\) are the only solutions of \(u\vee\neg u=u\). Moreover \(1_0\vee1_1=1_1\) but \(1_1\vee1_0\neq1_0\). Thus an isomorphism must preserve the two distinct designated tops, hence must preserve each set of elements having a specified value of \(x\vee\neg x\). Each restricted map is a Boolean isomorphism. The transition map is also recovered algebraically by \(p(x)=x\vee0_1\) for \(x\in B_0\), where \(0_1=\neg1_1\). Accordingly two sums are isomorphic precisely if there are Boolean isomorphisms \(\alpha_0,\alpha_1\) with \(\alpha_1\circ p=q\circ\alpha_0\). Conversely any such commuting pair defines an isomorphism of Płonka sums since the mixed operations are computed by transporting both inputs to their join-index component.

**2. Dualization and classification.** Every unital Boolean homomorphism \(\mathcal P([a])\to\mathcal P([b])\) is uniquely the inverse-image map \(f^{-1}\) for a function \(f:[b]\to[a]\), and Boolean automorphisms of the two powerset algebras act as permutations of their atoms. Therefore the diagram in step 1 commutes if and only if a pair of permutations \(\sigma\in S_a\), \(\tau\in S_b\) carries the dual function \(f\) to \(g\), equivalently \(g\circ\tau=\sigma\circ f\). Such a pair preserves the multiset of nonempty fiber cardinalities. Conversely, if two functions have identical multisets of nonzero fiber cardinalities, match corresponding fibers of equal size by a permutation \(\sigma\) of their occupied target points; extend \(\sigma\) to unused target points, then choose \(\tau\) as a bijection within each matched domain fiber. This gives the commuting diagram. Every partition \(\lambda\vdash b\) with \(\ell(\lambda)\leq a\) is realized by assigning \(\lambda_i\) domain points to target point \(i\). The integer-partition enumeration and the displayed generating function follow.

**3. Automorphism orders and a census identity.** Fix \(f\) with nonempty fibers of partition \(\lambda\). A stabilizing target permutation may permute the \(a-r\) unused target points, and it may permute the \(m_s\) target fibers of each equal size \(s\). Each such fiber correspondence has \(s!\) choices for the domain-point bijection. All choices are independent and necessary, yielding \((a-r)!\prod_s(s!)^{m_s}m_s!\) stabilizing pairs. Orbit-stabilizer gives the orbit size. As a check, the orbits partition all \(a^b\) functions, hence

\[
\sum_{\lambda\vdash b,\,\ell(\lambda)\leq a}\frac{a!b!}{(a-\ell(\lambda))!\prod_s(s!)^{m_s}m_s!}=a^b.
\]

**4. Exact boundary and smallest witness.** If \(a=1\), only one nonempty image fiber is possible. If \(b\leq3\), every admissible length \(r\leq\min(a,b)\) admits exactly one partition of \(b\), so \(N(a,b)=\min(a,b)\). If \(a\geq2,b\geq4\), there are at least two distinct length-two partitions, namely \((b-1,1)\) and \((b-2,2)\), and at least one partition for every other admissible length. Therefore \(N(a,b)>\min(a,b)\). The least possible component-sum cardinality in this failure range is \(2^2+2^4=20\). For \(a=2,b=4\), the partitions with at most two parts are exactly \((4)\), \((3,1)\), and \((2,2)\); the last two functions displayed in the finding have equal image size, but their fiber partitions differ, hence their Płonka sums are nonisomorphic.

## Verification

Execute `python3 verify.py` from the directory containing the standalone verifier. It enumerates all \(a^b\) functions and their full permutation orbits for \(1\leq a\leq4\), \(1\leq b\leq5\), matching every actual orbit with its fiber partition, the partition-count prediction and the automorphism/order sum. It also explicitly checks that the two exhibited 20-element Płonka sums satisfy all eight defining involutive-bisemilattice identities and checks the sharp smallest-component-size boundary. Recorded successful output:

`VERIFY_OK parameter_pairs 20 maps 1794 orbits 48 strictly_smaller_shapes 11 counterexample_shape (4, 16) rank 2 distinguished_fibers ((3, 1), (2, 2)) corrected_types 3 rank_only_types 2 axioms_checked 8`

This is a finite computational cross-check, not the proof for unbounded \(a,b\); the proof above establishes that assertion.

## Relationship to prior work

Bonzio, Pra Baldi and Valota (2018), *Counting Finite Linearly Ordered Involutive Bisemilattices*, establish the Płonka/finite-Stone setup and propose an isomorphism test using only the cardinality of each dual map's kernel quotient (conference Lemma 10; arXiv:2107.10540v1, Lemma 1), followed by the formula \(N(a,b)=\min(a,b)\) (conference Lemma 11; arXiv Lemma 2). These claims do not distinguish different sizes of kernel blocks. The present theorem isolates the first explicit failure and supplies the correct two-stage orbit classification and automorphism counts. The underlying elementary theorem that set-function orbits under independent domain/codomain permutations are classified by fiber-size partitions is a standard combinatorial ingredient; originality is **not** claimed for that general group-action fact. The new scoped finding applies it to identify and correct an unsupported isomorphism implication and enumeration in the cited specific algebraic census. General Płonka representation and Boolean–finite-set duality are also existing results, not claimed here.

## Limitations

The result concerns **only two nontrivial Boolean fibers of specified cardinalities**; it does not recompute the overall fine spectrum of all linearly ordered involutive bisemilattices, nor validate or invalidate every other formula in the 2018 paper. The integer partitions classify unlabelled isomorphism types, not distinct labeled algebra tables. We do not infer unpublished priority or universal absence of equivalent earlier treatments from unsuccessful searches. No independent mathematical or originality audit has been performed.

## References

1. S. Bonzio, M. Pra Baldi, D. Valota, *Counting Finite Linearly Ordered Involutive Bisemilattices*, in *Relational and Algebraic Methods in Computer Science*, LNCS 11194, 166–183 (2018), DOI: 10.1007/978-3-030-02149-8_11; open full text: https://arxiv.org/html/2107.10540v1 (especially Sections 2–4 and Lemmas 1–2).
2. S. Bonzio, A. Loi, L. Peruzzi, *A Duality for Involutive Bisemilattices*, *Studia Logica* 107 (2019), 423–444; preprint arXiv:1611.09560 (general duality background, not a cited two-fiber enumeration).
3. Publication date of the 2018 conference work: https://expertise.unimi.it/resource/item/662649 (6 October 2018).
