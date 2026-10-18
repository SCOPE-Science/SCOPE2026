# Cycle-index census of forward-confluent relations on complete two-level intuitionistic frames

## Finding

Let \(p,q\geq2\), let \(A\) and \(B\) be disjoint labelled sets with \(|A|=p\) and \(|B|=q\), and let \(P=A\oplus B\) be their ordinal sum as antichains: every element of \(A\) is below every element of \(B\), and there are no other strict comparabilities. In the forward-confluent (FIK) frame semantics of Balbiani, Gao, Gencer, and Olivetti, an arbitrary binary modal relation \(R\subseteq P\times P\) is admissible precisely when
\[
x\leq x'\ \text{and}\ xRy\quad\Longrightarrow\quad
\exists y'\ (x'Ry'\ \text{and}\ y\leq y').
\]
No reflexivity, transitivity, seriality, or other condition is imposed on \(R\).

Define the set of targets reached from the bottom level by
\[
U=\{a'\in A:\exists a\in A\ (aRa')\},\qquad
T=\{b'\in B:\exists a\in A\ (aRb')\}.
\]
**Normal form.** Forward confluence holds if and only if every \(b\in B\) satisfies
\[
T\subseteq R(b)\cap B,
\qquad
R(b)\cap B=\varnothing\ \Longrightarrow\ U\subseteq R(b)\cap A.
\]
Here \(R(b)=\{y:bRy\}\). Thus all top targets used by bottom worlds must appear in **every** top row; if a top row contains any top target, all bottom-target demands are automatically witnessed. Only top rows without top targets must contain the entire bottom target set \(U\).

**Exact labelled count.** Put \(a=2^p-1\). The number \(L(p,q)\) of admissible relations on the fixed labelled poset is
\[
\boxed{L(p,q)=
\sum_{u=0}^{p}\binom pu a^u\left[2^p(2^q-1)+2^{p-u}\right]^q
+2^{p^2}\sum_{t=1}^{q}\binom qt a^t 2^{q(p+q-t)}.}
\]

**Exact isomorphism count.** Write \(\lambda\vdash p\) and \(\mu\vdash q\) for integer partitions viewed as multisets of cycle lengths, and define
\[
K_{\alpha}(d)=\sum_{e\in\alpha}\gcd(d,e),\qquad
S_{\alpha\beta}=\sum_{d\in\alpha}K_{\beta}(d),\qquad
z_{\alpha}=\prod_{j\geq1} j^{m_j(\alpha)}m_j(\alpha)!,
\]
where \(m_j(\alpha)\) is the multiplicity of part \(j\). If \(\lambda=(\lambda_1,\ldots,\lambda_r)\), define
\[
H_1(\lambda,\mu)=2^{S_{\lambda\lambda}+S_{\mu\lambda}}
\left[\prod_{d\in\mu}
\left(2^{K_\mu(d)}+2^{K_\lambda(d)}-1\right)
-2^{S_{\mu\mu}}\right]
\]
and
\[
H_0(\lambda,\mu)=
\sum_{I\subseteq\{1,\ldots,r\}}
\left(\prod_{i\in I}\bigl(2^{K_\lambda(\lambda_i)}-1\bigr)\right)
\prod_{d\in\mu}
\left[2^{K_\lambda(d)}\bigl(2^{K_\mu(d)}-1\bigr)
+2^{\sum_{i\notin I}\gcd(\lambda_i,d)}\right].
\]
Then the number \(N(p,q)\) of isomorphism classes, where isomorphisms must preserve both the intuitionistic order and the modal relation, is exactly
\[
\boxed{N(p,q)=\sum_{\lambda\vdash p}\sum_{\mu\vdash q}
\frac{H_0(\lambda,\mu)+H_1(\lambda,\mu)}{z_\lambda z_\mu}.}
\]
This is a finite integer-valued cycle-type formula for all positive level sizes, in particular for all \(p,q\geq2\).

Representative exact values are:

| \(p,q\) | Labelled relations \(L(p,q)\) | Isomorphism classes \(N(p,q)\) |
|---|---:|---:|
| \(2,2\) | 11,401 | 3,067 |
| \(2,3\) | 1,252,925 | 111,183 |
| \(3,2\) | 3,771,875 | 324,244 |
| \(3,3\) | 847,519,079 | 24,206,336 |
| \(2,4\) | 495,407,161 | 10,719,206 |

## Assumptions and scope

The objects counted are **all** binary accessibility relations on the specified complete two-level intuitionistic poset that satisfy the single FIK forward-confluence axiom. No modal valuation is counted. Two relations are isomorphic only if an order-preserving bijection intertwines their accessibility relations. Every order automorphism of \(A\oplus B\) is a permutation of \(A\) together with a permutation of \(B\), hence the acting group is \(S_p\times S_q\).

The formulas do not count all FIK frames on a prescribed number of worlds, and they do not identify relations that induce the same modal theory or are related by bisimulation. For the displayed primary claims, both levels have at least two points; boundary cases of singleton levels are included only as additional checker controls.

## Proof

**1. Characterizing the relations.** The only distinct comparable pairs \(x<x'\) in the poset have \(x\in A\), \(x'\in B\). For a bottom-to-top target edge \(aRt\) with \(t\in B\), the only point above \(t\) is \(t\) itself, so each \(b\in B\) must have \(bRt\). These obligations are exactly \(T\subseteq R(b)\cap B\). For a bottom-to-bottom target \(aRu\) with \(u\in A\), a row \(R(b)\) can witness the obligation with any element of \(B\), since every such element lies above \(u\). If that row contains no element of \(B\), it must contain \(u\) itself, because the other bottom worlds are incomparable with \(u\). These obligations are exactly the second displayed inclusion. Conversely, either of these witnesses satisfies every nontrivial instance of forward confluence; instances \(x=x'\) use \(y'=y\). This proves the normal form in both directions, without further assumptions.

**2. Counting labelled relations.** Each target column in the bottom-source incidence matrix may be hit by any nonempty subset of its \(p\) source rows. Thus, for a prescribed support consisting of \(u\) bottom targets and \(t\) top targets, there are \(a^{u+t}\) possible bottom-source matrices, where \(a=2^p-1\).

If \(t=0\), fix the \(u\) supported bottom targets. Every top-source row either contains at least one top target, with \(2^p(2^q-1)\) choices, or contains no top target and is forced to contain those \(u\) bottom targets, with \(2^{p-u}\) choices. The rows are independent. Choosing the supported bottom targets and summing over \(u\) gives the first sum in \(L(p,q)\).

If \(t\geq1\), every top-source row must contain all \(t\) supported top targets, while its remaining \(p+q-t\) entries are independent. Hence the top-source choices number \(2^{q(p+q-t)}\). Summing freely over bottom-target support gives \((1+a)^p=2^{p^2}\); then choosing the \(t\) top targets gives the second sum. The cases are disjoint and exhaustive.

**3. Counting relations fixed by a level-preserving permutation.** Fix permutations \(\sigma\in S_p\) and \(\tau\in S_q\), with cycle-length multisets \(\lambda\) and \(\mu\). A Boolean incidence block between a source cycle of length \(d\) and a target cycle of length \(e\) has exactly \(\gcd(d,e)\) independent entries under the diagonal action. For a specified target cycle of length \(e\), the invariant bottom-source incidence choices are therefore \(2^{K_\lambda(e)}\), of which exactly one is identically zero. The set of active target cycles is a union of complete permutation cycles.

Separate fixed relations according to whether some top-level target occurs in the bottom-source matrix. If **at least one** such target cycle is active, bottom-to-bottom incidence can be chosen in \(2^{S_{\lambda\lambda}}\) invariant ways. Bottom-to-top incidence has per-target-cycle activation weight \(2^{K_\lambda(e)}-1\). The top-source rows must have every activated top-target column entirely filled with ones; the remaining top-to-top incidence has weight \(2^{K_\mu(e)}\) per inactive target cycle, and top-to-bottom incidence has \(2^{S_{\mu\lambda}}\) choices. Summing over nonempty sets of activated top cycles gives precisely \(H_1(\lambda,\mu)\).

If **no** top-level target is reached from below, let \(I\subseteq\{1,\ldots,r\}\) index the active bottom-target cycles. The bottom-source matrix contributes \(\prod_{i\in I}(2^{K_\lambda(\lambda_i)}-1)\). For each top-source cycle of length \(d\), there are two disjoint choices. With a nonempty top-target pattern the top and bottom portions contribute \((2^{K_\mu(d)}-1)2^{K_\lambda(d)}\). With an empty top-target pattern the row must contain every active bottom-target cycle, leaving exactly \(2^{\sum_{i\notin I}\gcd(\lambda_i,d)}\) choices. Multiply these alternatives over top-source cycles and sum over \(I\) to obtain exactly \(H_0(\lambda,\mu)\).

Consequently, \(H_0+H_1\) is the number of forward-confluent relations fixed by any permutation pair of cycle types \((\lambda,\mu)\). Burnside's lemma and the fact that the number of permutations having cycle type \(\alpha\vdash n\) is \(n!/z_\alpha\) yield the displayed formula for \(N(p,q)\). Every step is exact for arbitrary finite level sizes.

## Verification

Run `python3 verify.py` from the directory containing the present result. The verifier uses only Python's standard library and computes both closed formulas with exact integers and rational Burnside summation. Independently of either formula, it exhaustively tests the original quantified forward-confluence condition for **every** binary relation on each two-level poset of total size at most four in six displayed control profiles. It also independently enumerates possible top-row relations from all bottom-row assignments for profiles \((2,2)\), \((2,3)\), and \((3,2)\), testing the original axiom rather than the support classification. Finally, for \((1,3)\), \((2,2)\), and \((2,3)\), it enumerates invariant relations directly by the orbits of ordered pairs under every nonidentity level permutation, checks the original axiom on each relation, and applies Burnside's lemma directly. All these independent routes agree with the exact formulas. The program prints `VERIFY_OK` only after all assertions pass.

These finite checks validate implementations and detect errors in small cases; the proof for all sizes is the combinatorial argument above, not an inference from the checked samples.

## Relationship to prior work

Balbiani, Gao, Gencer, and Olivetti define forward confluence and establish axiomatization, proof search, and finite countermodel extraction for FIK. Their 2023 preprint (2024 proceedings) is the source of the frame condition; its inspected semantic definitions and concluding discussion do not provide the present normal form or two-level labelled/isomorphism census.

A published mathematical record, *Gaussian-binomial census of FIK relations on finite chains*, gives a distinct exact chain result. Its complete RESULT document was inspected: all counted intuitionistic carriers there are **chains**, with nonempty successor rows controlled by weakly increasing maxima. The current two-level carriers with \(p,q\geq2\) are **not** chains, and their top-target witness condition and nontrivial order-automorphism group cannot be obtained by restricting that chain theorem. In particular, the cycle-index isomorphism count is not covered by that record.

Balbiani, Diéguez, and Fernández-Duque study S4-related logics with additional modal preorder axioms and different semantic restrictions. General finite-model properties and decidability theorems do not imply an exact enumeration of arbitrary FIK-forward-confluent relations on this carrier. The present count is limited to precisely specified posets and should not be read as a completeness or complexity result.

## Limitations

No claim is made that the numerical sequences lack entries in every external table or that no unpublished or unindexed equivalent formula exists. FIK forward confluence alone is weaker than adding modal reflexivity, transitivity, or the second Fischer–Servi interaction condition; the formulas must not be applied to those smaller frame classes. The labelled count and isomorphism count concern accessibility relations, not valuations or bisimulation classes. The proof for all sizes is combinatorial and does not depend on extrapolating finite enumerations.

## References

[1] Philippe Balbiani, Han Gao, Çiğdem Gencer, and Nicola Olivetti, “A Natural Intuitionistic Modal Logic: Axiomatization and Bi-nested Calculus,” arXiv:2309.06309v1 (12 September 2023); *Leibniz International Proceedings in Informatics* 288, 13:1–13:21 (2024), DOI:10.4230/LIPIcs.CSL.2024.13. https://arxiv.org/abs/2309.06309

[2] “Gaussian-binomial census of FIK relations on finite chains,” published published-finding corpus finding record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-gaussian-binomial-census-of-fik-relations-on-finite-chains--75c9508e987d (complete RESULT document inspected).

[3] Philippe Balbiani, Martín Diéguez, and David Fernández-Duque, “Some constructive variants of S4 with the finite model property,” arXiv:2104.15053v1 (30 April 2021), DOI:10.1109/LICS52264.2021.9470643. https://arxiv.org/abs/2104.15053

[4] Han Gao and Nicola Olivetti, “Taming Complexity in Intuitionistic Modal Logic: The Case of FIK and Its Shallow Calculus,” arXiv:2606.31877 (30 June 2026), DOI:10.4204/EPTCS.447.23; abstract consulted for context only. https://arxiv.org/abs/2606.31877
