# The complete \(\mathsf{IS4}\) relation census on the four-element Boolean diamond

## Finding

Let \(B_2=\{0,a,b,1\}\), ordered by \(0<a<1\), \(0<b<1\), and \(a\parallel b\). Among all binary relations \(R\) on this labelled carrier, exactly
\[
\boxed{135}
\]
are reflexive and transitive and satisfy both Fischer--Servi interaction conditions. Of these, precisely \(27\) are invariant under interchange of the two middle worlds, giving exactly
\[
\boxed{81}
\]
isomorphism classes for this fixed ordered carrier. The four joint truth values of the two endpoint edges \(0R1\) and \(1R0\) occur, respectively, with multiplicities
\[
\boxed{76,\ 29,\ 29,\ 1}
\]
for patterns \((0,0),(1,0),(0,1),(1,1)\). The unique relation with both endpoint edges is the complete relation.

## Assumptions and scope

The world set is exactly \(W=\{0,a,b,1\}\), with the Boolean diamond order \(\le\) specified above. Every world is distinguished in the labelled count, and the only nonidentity order automorphism exchanges \(a\) and \(b\). A modal accessibility relation \(R\subseteq W\times W\) is admissible precisely if it is reflexive, transitive, and satisfies the following conditions for **all** \(x,y,z\in W\):

\[
\begin{aligned}
\mathsf{F_1}:\quad &xRy\ \land\ y\le z\ \Longrightarrow\ \exists u\in W\;(x\le u\ \land\ uRz),\\
\mathsf{F_2}:\quad &x\le z\ \land\ xRy\ \Longrightarrow\ \exists u\in W\;(zRu\ \land\ y\le u).
\end{aligned}
\]

These are the birelational frame conditions appearing in Girlando et al., Definition 2.1. Their \(\mathsf{IS4}\) frame class additionally requires modal reflexivity and transitivity. The count applies to this class on the fixed diamond, not to unrestricted classical \(\mathsf{S4}\) frames and not to all underlying intuitionistic posets.

## Proof

A reflexive relation on four labelled worlds has exactly twelve freely chosen off-diagonal edges. Therefore its entire domain is in bijection with the integers \(0\) through \(2^{12}-1=4095\). For every such integer, the attached verifier forms the associated four row-bitsets with diagonal bits set. It evaluates transitivity by checking \(R(y)\subseteq R(x)\) for each edge \(xRy\), then tests each of \(\mathsf{F_1},\mathsf{F_2}\) for every applicable ordered triple using the four fixed upward-order sets. The verifier exhibits the entire finite search by explicit nested loops; no heuristic, sampling, truncation, or external table is used. The accepted relations partition by endpoint-edge pattern into classes of respective cardinalities \(76,29,29,1\), summing to \(135\).

For a logically independent encoding, the verifier enumerates all set partitions of the four worlds, all partial orders on the quotient blocks, and lifts each order to a preorder on the original worlds. This yields exactly \(355\) distinct reflexive-transitive relations, the known total number of four-point labelled preorders. Applying the same explicit universal confluence predicates leaves **exactly the same set of 135 relations**, checked as a set identity rather than merely matching cardinalities. Hence the first enumeration is exhaustive and reproducible independently of its encoding.

For the orbit count, conjugate each admissible relation by the lattice automorphism \(a\leftrightarrow b\). The verifier checks that the admissible set is stable under this action and that precisely \(27\) elements are fixed. Burnside's lemma for the two-element automorphism group gives
\[
\frac{135+27}{2}=81.
\]

The singleton fourth endpoint-edge cell has a structural explanation: if \(0R1\) and \(1R0\), then \(\mathsf{F_1}\) applied to \(1R0\le w\) forces \(1Rw\) for every world \(w\), because \(1\) is the maximum of the intuitionistic order. Similarly \(\mathsf{F_2}\) applied to \(0\le w\) and \(0R1\) forces \(wR1\) for every \(w\). Transitivity then gives \(xR1Ry\), hence the complete relation.

## Verification

Run `python3 verify.py` with Python 3. The script is self-contained and returns `DIAMOND_IS4_CENSUS_VERIFY_OK` only after checking the full labelled count, both independent relation generators, the endpoint-edge distribution, the universal-relation boundary, the automorphism-fixed count, and the orbit count. The verifier uses a full finite enumeration and thus supplies a complete proof certificate for this exact four-world statement, not a statistical experiment.

## Relationship to prior work

Fernández-Duque (2026) gives a finite-model-property proof for Fischer--Servi-style intuitionistic \(\mathsf{K4}\), motivating finite birelational frame analysis. Girlando et al. (2023) provide the relevant \(\mathsf{IS4}\) semantics and confluence definitions. Previously studied chain and rooted-fork counts concern **different underlying orders** and do not determine this first Boolean-diamond count. OEIS A000798 records the unrestricted number of four-point preorders, \(355\), which is expressly **not** claimed as new. The contribution asserted here is the exact admissible \(\mathsf{IS4}\) subset and its complete endpoint-edge and automorphism-orbit profile on the Boolean diamond.

## Limitations

The proof is an exact finite exhaustive classification on \(B_2\). It provides no closed formula on larger Boolean lattices or arbitrary posets. Literature and research-record searches found no prior matching enumeration, but older unindexed frame censuses may exist. The recent motivating paper's abstract and metadata were available; its complete text could not be inspected. Independent scholarly priority review is not claimed.

## References

1. D. Fernández-Duque, *Fine Selection for Intuitionistic Modal Logic*, arXiv:2609.27078, first public version 2026-09-22; https://arxiv.org/abs/2609.27078.
2. M. Girlando, R. Kuznets, S. Marin, M. Morales, and L. Straßburger, *Intuitionistic S4 is decidable*, arXiv:2304.12094, 2023; Definition 2.1 and Theorem 2.5; https://arxiv.org/html/2304.12094v1.
3. OEIS A000798, labelled preorders, https://oeis.org/A000798 (baseline total, not a claim of novelty).
