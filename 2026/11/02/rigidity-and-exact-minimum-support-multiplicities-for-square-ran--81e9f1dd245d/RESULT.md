# Rigidity and exact minimum-support multiplicities for square-rank SPC product subcodes

## Finding

Let \(q\) be any prime power and \(m,n\ge2\). Let \(C_{m,n}(q)\) consist of the \(m\)-by-\(n\) matrices over \(\mathbb F_q\) with zero sum along each row and each column. For each integer \(1\le s<\min\{m,n\}\), an \(s^2\)-dimensional linear subcode \(D\) has joint coordinate support of size at least \((s+1)^2\). **Every equality case is rigid:** choose exactly \(s+1\) rows and \(s+1\) columns, then take the *whole* code of zero-row-sum, zero-column-sum arrays on the selected rectangle, setting every other entry to zero. These, and only these, attain equality.

Consequently, writing \(M_{s^2}\) for the number of distinct \(s^2\)-dimensional subcodes whose supports have minimum size,

\[
 d_{s^2}(C_{m,n}(q))=(s+1)^2,\qquad
 M_{s^2}=\binom{m}{s+1}\binom{n}{s+1}.
\]

The value of the generalized Hamming weight itself is **previously known**; the claim here is the all-field equality classification and the exact multiplicity. For example, at \(m=n=5\) and \(s=2\), precisely \(\binom53^2=100\) four-dimensional subcodes have the minimum support size nine, independently of the alphabet field.

**Rank-loss interpretation.** Suppose a codeword is sent through a coordinate-erasure channel and the erased positions are \(E\). The affine space of compatible codewords has direction \(C[E]=\{c\in C:\operatorname{supp}(c)\subseteq E\}\); hence its dimension is \(\dim C[E]\). If exactly \((s+1)^2\) positions are erased, then \(\dim C[E]\ge s^2\) holds precisely when \(E\) is one of the selected complete square subarrays. Thus a uniform erasure set of that size has probability

\[
 \frac{\binom{m}{s+1}\binom{n}{s+1}}{\binom{mn}{(s+1)^2}}
\]

of producing ambiguity dimension at least \(s^2\). For independent coordinate erasures with probability \(p\), with \(m,n,s,q\) fixed and \(p\downarrow0\), the corresponding leading probability is

\[
 \binom{m}{s+1}\binom{n}{s+1}p^{(s+1)^2}+O\bigl(p^{(s+1)^2+1}\bigr).
\]

## Assumptions and scope

A prime power \(q\), integers \(m,n\ge2\), and \(1\le s<\min\{m,n\}\) are arbitrary. Every statement is over \(\mathbb F_q\), including extensions of prime fields. A subcode's support is the union of the supports of all its words (not merely a union of supports of a chosen generating set). Entries outside the selected rectangle are zero. The count concerns distinct *linear subspaces*, not ordered generators and not individual words. The erasure conclusions concern linear-algebraic decoding ambiguity, not the difficulty of running a decoder.

## Proof

**1. Bipartite flow model.** Given a coordinate set \(E\subseteq[m]\times[n]\), make a bipartite graph \(H_E\): left vertices are the rows incident to \(E\), right vertices the incident columns, and edges are the coordinates in \(E\). Multiplying every column-vertex parity equation by \(-1\) transforms the unsigned row/column check matrix into an oriented vertex-edge incidence matrix over \(\mathbb F_q\). This remains valid in characteristic two. If \(H_E\) has \(e\) edges, \(v\) incident vertices, and \(c\) nonempty connected components, the rank of this incidence matrix is \(v-c\). Therefore

\[
 \dim C[E]=e-v+c=\sum_{i=1}^c(e_i-v_i+1).
\]

The rank formula follows directly by choosing a spanning forest: its incidence columns are independent by leaf elimination, and each additional edge adds a fundamental-cycle dependence. It requires no characteristic restriction. In particular, for a complete \(a\)-by-\(b\) rectangle the dimension is \((a-1)(b-1)\).

**2. No bridge belongs to the support of a subcode.** Let \(D\le C\) and put \(E=\operatorname{supp}(D)\). In any codeword, the sum of the oriented flow across any vertex cut vanishes. If an edge is a bridge of \(H_E\), take the cut defined by deleting it; it is the unique crossing edge, so its coefficient vanishes in *every* codeword supported inside \(E\). This contradicts membership in the joint support. Consequently every nonempty component of \(H_E\) has a cycle and at least four edges.

**3. Sharp cycle-rank inequality.** Let one component have \(e_i\) edges, \(a_i\) row vertices, and \(b_i\) column vertices. Its flow-space dimension is \(\beta_i=e_i-a_i-b_i+1\). Since \(e_i\le a_ib_i\), the arithmetic-geometric mean inequality gives

\[
 \beta_i\le e_i-2\sqrt{e_i}+1=:f(e_i).
\]

Equality requires simultaneously \(a_i=b_i=\sqrt{e_i}\) and \(e_i=a_ib_i\), which holds exactly for a complete balanced bipartite component \(K_{t,t}\).

For real \(x,y\ge4\),

\[
 f(x+y)-f(x)-f(y)
 =2\bigl(\sqrt x+\sqrt y-\sqrt{x+y}\bigr)-1>0.
\]

Indeed the expression is increasing in each variable, and its value at \(x=y=4\) is \(7-4\sqrt2>0\). Inductively, any graph with at least two nonempty components satisfies \(\sum_i f(e_i)<f(\sum_i e_i)\). Thus, for every nonzero subcode \(D\) with joint support size \(e\),

\[
 \dim D\le\dim C[E]\le f(e)=(\sqrt e-1)^2.
\]

If equality holds in the second inequality, its support graph is necessarily connected and complete balanced bipartite.

**4. Square-rank equality and uniqueness.** Set \(\dim D=s^2\). The bound above, with \(e\ge4\), forces \(e\ge(s+1)^2\). Conversely a complete \((s+1)\)-by-\((s+1)\) subarray has cycle-space dimension \(s^2\). At \(e=(s+1)^2\), the inequalities \(s^2\le\dim C[E]\le f(e)=s^2\) are all equalities. Their equality conditions compel \(H_E=K_{s+1,s+1}\). Moreover \(D\subseteq C[E]\) and both spaces have dimension \(s^2\), so \(D=C[E]\). Every such rectangular code has full support: each coordinate belongs to a supported \(2\)-by-\(2\) cycle flow with coefficients \(1,-1,-1,1\). Distinct row/column choices give distinct supports and therefore distinct subcodes. There are exactly \(\binom m{s+1}\binom n{s+1}\) choices.

**5. Erasure laws.** For every erased set \(E\) of cardinality exactly \((s+1)^2\), \(\dim C[E]\ge s^2\) if and only if \(E\) is one of the square rectangles by Step 4. Divide their number by the number of all equally likely sets to obtain the uniform exact formula. Under independent erasures, each such minimal set has probability \(p^{(s+1)^2}(1-p)^{mn-(s+1)^2}\); all larger sets contribute \(O(p^{(s+1)^2+1})\) at fixed blocklength. This proves the stated leading coefficient.

## Verification

Run the included standard-library program with `python3 verify_spc_square_ranks.py`. It enumerates **every** bipartite edge subset for shapes \(2\times4\), \(3\times3\), \(3\times4\), and \(4\times4\), computes its exact cycle rank, and compares the complete collection of optimum edge supports at square ranks with the predicted complete subarrays. It also independently checks parity-check ranks by modular row reduction over the prime fields of orders \(2,3,5,7\). All checks passed and ended with `SPC_SQUARE_RANK_VERIFICATION_OK` (see the attached output). The general result follows from the graph-theoretic proof; finite enumeration is a cross-check only. The modular program does not construct extension-field arithmetic, since that generality is instead established symbolically by the incidence-rank proof.

## Relationship to prior work

Ribeiro Alves and Cardell's August 26, 2026 preprint, *Weight Distributions of Single Parity-Check Product Codes via Character Sums* [1], studies these binary product codes and explicitly obtains their entire generalized Hamming-weight hierarchy (Theorem 7), using the established product formula of Wei–Yang and Schaathun [2]. Therefore **the numeric distance \(d_{s^2}\) is not new**. The preprint also derives the ordinary (one-dimensional codeword) weight enumerator, which must not be confused with the counts of higher-dimensional optimizing subcodes here. The asserted addition is the all-finite-field equality rigidity and the exact number of higher-dimensional support minimizers, together with the minimum-size erasure rank-loss law.

Cardell and Climent [3] previously count uncorrectable patterns of several specified weights for square SPC product codes using bipartite graphs. This is notably relevant to the erasure interpretation. Its accessible abstract does not assert a general rank-at-least-\(s^2\) rigidity theorem or enumerate all such minimal patterns for arbitrary rectangular dimensions and all prime powers; full-text comparison was not possible, so implicit prior coverage remains a risk. The present erasure coefficient is a consequence of the central subcode rigidity and is not asserted to settle general erasure enumeration.

## Limitations

The rigidity and enumerator are proved only for **square subcode dimensions** \(s^2\). No uniqueness classification is claimed for other ranks, no new generalized Hamming-weight *values* are claimed, and no general decoder or all-erasure-pattern enumeration is supplied. For fixed parameters the small-erasure probability is an asymptotic as \(p\downarrow0\), not an assertion uniform in growing \(m\) or \(n\). Older product-code and erasure-enumeration literature could contain an implicit equivalent; independent priority and mathematical audit have not been performed.

## References

1. M. M. Ribeiro Alves and S. D. Cardell, *Weight Distributions of Single Parity-Check Product Codes via Character Sums*, arXiv:2608.26457, initial public submission 2026-08-26; especially §3.1 and Theorem 7. https://arxiv.org/abs/2608.26457
2. H. Schaathun, *The weight hierarchy of product codes*, IEEE Transactions on Information Theory 46(7) (2000), 2648–2651, DOI: 10.1109/18.887876.
3. S. D. Cardell and J.-J. Climent, *An approach to the performance of SPC product codes on the erasure channel*, Advances in Mathematics of Communications 10(1) (2016), 11–28, DOI: 10.3934/amc.2016.10.11.
