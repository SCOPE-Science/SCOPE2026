# Secure-domination polynomial of generalized windmill graphs
## Finding
For integers \(r\ge 2\) and \(m\ge 2\), let
\[
W_{{r,m}}=K_1\vee rK_m
\]
be the graph with universal center \(c\) and pairwise disjoint clique blades \(B_1,\ldots,B_r\), each of order \(m\). A set \(S\subseteq V(W_{{r,m}})\) is secure dominating if and only if exactly one of the following conditions holds:

1. \(c\notin S\) and \(S\cap B_i\neq\varnothing\) for every \(1\le i\le r\);
2. \(c\in S\) and at most one blade \(B_i\) is disjoint from \(S\).

Put
\[
A_m(x)=(1+x)^m-1.
\]
Then the complete secure-domination polynomial is
\[
D_s(W_{{r,m}};x)=A_m(x)^r+x\left(A_m(x)^r+rA_m(x)^{{r-1}}\right)
=A_m(x)^{{r-1}}\left((1+x)A_m(x)+rx\right).
\]
In particular,
\[
\gamma_s(W_{{r,m}})=r,
\qquad
[x^r]D_s(W_{{r,m}};x)=m^{{r-1}}(m+r).
\]
Thus there are exactly \(m^{r-1}(m+r)\) minimum secure dominating sets. Moreover the polynomial determines the parameters within this family: its least nonzero exponent is \(r\), while its degree is \(rm+1\), so \(m=(\deg D_s-1)/r\).

## Assumptions and scope
Graphs are finite, simple, and undirected. A dominating set \(S\) is secure dominating when every vertex \(v\notin S\) has a neighbor \(u\in S\) such that \(S-\{{u\}}\cup\{{v\}}\) is again a dominating set. The polynomial counts all secure dominating sets by cardinality. The result concerns the uniform clique-blade windmill \(K_1\vee rK_m\) with \(r,m\ge2\); it does not assert a formula for nonuniform block sizes.

## Proof
Suppose first that \(c\notin S\). Domination already forces every blade to meet \(S\): a vertex in an empty blade has no neighbor in any other blade. Conversely, assume every blade meets \(S\). If \(v\notin S\) lies in \(B_i\), choose \(u\in S\cap B_i\). Replacing \(u\) by \(v\) leaves every blade occupied, hence leaves a dominating set. If the outside vertex is \(c\), replace any selected blade vertex by \(c\); the resulting set contains the universal center and is dominating. Thus the center-free secure dominating sets are exactly those meeting every blade, contributing \(A_m(x)^r\).

Now suppose \(c\in S\). If every blade is occupied, an outside vertex in \(B_i\) can be defended by any selected vertex in the same blade; the center remains selected. If exactly one blade \(B_i\) is empty, an outside vertex \(v\in B_i\) has the center as a defender: after replacing \(c\) by \(v\), every blade is occupied, so the new set dominates. Vertices outside \(S\) in occupied blades are defended within their blade as before. Hence zero or one empty blade is sufficient.

If at least two blades are empty, choose \(v\) in one empty blade. Its only selected neighbor is \(c\). Replacing \(c\) by \(v\) leaves another empty blade with no selected neighbor, so the replacement set is not dominating. Hence secure domination fails. This proves the classification.

For the enumerator, center-free sets contribute \(A_m(x)^r\). Sets containing the center with no empty blade contribute \(xA_m(x)^r\), and those with exactly one empty blade contribute \(rxA_m(x)^{r-1}\). Summing gives the displayed formula. Since \(A_m(x)\) has least degree \(1\) with coefficient \(m\), the least degree of the full polynomial is \(r\), with coefficient \(m^r+rm^{r-1}=m^{r-1}(m+r)\). Its top degree is \(rm+1\), proving the reconstruction statement.

## Verification
A standalone exhaustive checker accompanies this result. It constructs \(W_{{r,m}}\), evaluates the secure-domination definition directly, compares it with the structural criterion above for every vertex subset, and compares all polynomial coefficients with the closed formula. It covers every pair \((r,m)\) with \(2\le r,m\le4\) and \(1+rm\le13\), totaling \(18{,}720\) subsets. The replay result was:

`VERIFY_OK parameter_pairs=8 subset_checks=18720 secure_sets=15399 structural_checks=18720 coefficient_checks=81 max_order=13`

This finite computation checks boundary behavior and the implementation of the formula; the proof above, not the finite enumeration, establishes the statement for all \(r,m\ge2\).

## Relationship to prior work
Secure domination was already part of the graph-protection literature by 2003. A primary manuscript dated 11 September 2003 treats finite-order domination and explicitly identifies secure domination as previously studied, while recording classification 05C69. Ordinary domination polynomials of friendship graphs treat the specialization \(K_1\vee rK_2\), and later work studies ordinary domination polynomials for generalized friendship and book graphs. Those ordinary-domination formulas do not imply the defender-swap criterion above.

A later algorithmic paper gives a linear-time method for finding a minimum secure dominating set in block graphs. Generalized windmills are block graphs, so that work is relevant broader algorithmic coverage of the minimum problem, but the accessible abstract does not provide an all-set classification or a secure-domination polynomial. Separate work on secure-domination polynomials treats cycles, not windmills. Targeted database searches under secure-domination, windmill, friendship, block-graph, and polynomial formulations found no statement implying the classification or enumerator here.

## Limitations
The block-graph algorithm paper was available only through bibliographic metadata and abstract-level material in this review, so a hidden special-case closed formula in inaccessible full text remains a residual originality risk. Bibliographic sources also identify an earlier 2003 paper on secure domination but do not provide an exact day for that earlier item; no day has been imputed. The exact-day source date recorded here is the 11 September 2003 date printed on the inspected primary manuscript. No claim is made about nonuniform windmills or other block graphs.

## References
- *Finite Order Domination in Graphs*, Journal of Combinatorial Mathematics and Combinatorial Computing 49 (2004), 159–175; inspected manuscript dated 11 September 2003.
- *On the Domination Polynomials of Friendship Graphs*, arXiv:1401.2092v1.
- *Domination polynomial of generalized friendship and generalized book graphs*, arXiv:1501.05856v1.
- *Edge stability in secure graph domination*, DOI:10.46298/dmtcs.2120.
- *On computing a minimum secure dominating set in block graphs*, DOI:10.1007/s10878-017-0197-y.
- *Secure Dominating Sets and Secure Domination Polynomials of Cycles*, DOI:10.17654/0974165822006.
