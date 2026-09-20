# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The exact formulas are obtained by partitioning the (n-2)-clique according to adjacency to the two outside vertices, computing the Szeged contribution of each edge type, and subtracting the Wiener index. The equality classification then reduces to three elementary Diophantine equations under the exact two-connectivity constraints. The case analysis excludes all solutions of order at least 10 except the displayed infinite family and one order-10 sporadic type.

A standalone definition-level verifier independently constructs the graphs, computes all-pairs distances, evaluates the Wiener and Szeged indices directly, and compares with the formulas. It checked 1,160 connected parameter profiles for the closed forms and all 8,175 two-connected profiles through order 18 for the equality classification, with no discrepancy.

## Originality

The primary recent source, Zhang and Li (arXiv:2609.20025), proves the BKLPS lower bound and explicitly poses characterization of eta(G)=2n as Problem 7. Its Lemma 8 exhibits the infinite family with two outside adjacent vertices having distinct singleton neighborhoods in K_{n-2}, and the authors state that this sufficient condition is not necessary. The paper does not give a classification within graphs containing K_{n-2}, nor the exact formulas in the present result.

The full text of Bonamy, Knor, Lužar, Pinlou, and Škrekovski (Applied Mathematics and Computation 312 (2017), 202-213) was also inspected. It proves eta(G)>=2n-6 for 2-connected noncomplete graphs, characterizes equality there, and formulates the later-proved eta(G)>=2n conjecture. No two-outside-vertex clique classification appears there.

Searches using Szeged-Wiener gap, eta(G)=2n, clique of order n-2, near-complete graphs, clique deletion, and related Szeged-index terminology found no prior statement of the formulas or equality classification. The originality assessment is therefore to the best of our knowledge. No specific inaccessible paper was identified as especially likely to overturn it. Residual risk remains from older literature using different names for near-complete graph families and from recent unindexed work.

## Value

The result gives a complete equality classification in the same near-complete structural regime used by the sharpness construction in the new source paper, while also explaining the source's remark that its sufficient condition is not necessary: there is exactly one additional isomorphism type in this regime, at order 10. The formulas additionally determine eta for every 2-connected graph having a clique on all but two vertices.

## Limitations

The theorem is only a partial solution of the general equality problem: 2-connected equality graphs with clique number below n-2 are not classified. The computational checks are finite and support rather than replace the proof. No independent validation is asserted.
