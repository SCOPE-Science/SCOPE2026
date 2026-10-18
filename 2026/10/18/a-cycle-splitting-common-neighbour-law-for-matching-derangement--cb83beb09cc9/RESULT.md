# A cycle-splitting common-neighbour law for matching derangement graphs

## Finding

Let \(D_n\) denote the graph whose vertices are the perfect matchings of \(K_{2n}\), with two distinct matchings adjacent exactly when they have no edge in common. The superposition type of two matchings is the integer partition \(\lambda\vdash n\) whose parts are half the lengths of alternating cycles in their union; a common edge contributes a part of size one.

Fix \(m\ge 2\) and an integer partition \(\rho\vdash r\), where \(r\ge0\) and the empty partition is allowed when \(r=0\). Put \(n=2m+r\). Choose perfect matchings \(A,B_{\mathrm{split}},B_{\mathrm{join}}\) on \(2n\) vertices such that the respective superposition types with \(A\) are
\[
\lambda_{\mathrm{split}}=(m,m)\sqcup\rho,
\qquad \lambda_{\mathrm{join}}=(2m)\sqcup\rho.
\]
Let \(d(\rho)\) be the number of perfect matchings edge-disjoint from **both** matchings in any prescribed pair on \(2r\) vertices of superposition type \(\rho\). Define \(d(\varnothing)=1\). Then the exact difference of common-neighbour counts is
\[
\boxed{\ |N(A)\cap N(B_{\mathrm{split}})|-|N(A)\cap N(B_{\mathrm{join}})|=2d(\rho).\ }
\]
Moreover \(d(\rho)=0\) exactly when \(\rho=(1)\); the value is strictly positive for every other allowed \(\rho\), including the empty partition.

**Logical consequence.** For every odd \(n=2m+1\ge5\), there are two vertices in distinct orbits of the full automorphism group fixing a single marked matching \(A\) that have the **same colour after two complete rounds** of ordinary one-dimensional colour refinement. Their superposition types are \((m,m,1)\) and \((2m,1)\). Thus at least three rounds are necessary to recover the automorphism-orbit partition of a singly marked matching derangement graph of any such odd size. No assertion is made that a third round always suffices.

## Assumptions and scope

All graphs are finite, simple, undirected, and unweighted. A perfect matching comprises \(n\) pairwise vertex-disjoint edges covering \(2n\) vertices. A part \(k\ge2\) of a superposition type represents an alternating simple cycle of length \(2k\); a part one represents a common edge, counted only once in the forbidden simple edge set. Write \(N(X)\) for the set of graph-neighbours of \(X\) in \(D_n\).

Colour refinement starts at round zero with the vertex \(A\) uniquely coloured and all other vertices given a second common colour. A complete round replaces a colour by the ordered pair consisting of its old colour and its vector of neighbour counts into every old colour class. The definition does not assume any randomized tie-breaking. The claim concerns colours within one rooted graph, not distinguishability of two graphs or uniqueness of their isomorphism types.

## Proof

**Step 1: an exact inclusion-exclusion functional.** Given any pair of perfect matchings with superposition type \(\lambda\vdash n\), let \(F_\lambda\) be the simple graph formed by their union and put
\[
P_\lambda(z)=\sum_{j=0}^n a_jz^j,
\qquad a_j=\#\{\text{matchings of }j\text{ forbidden edges in }F_\lambda\}.
\]
For \(k\ge2\), write \(C_{2k}(z)\) for the matching-generating polynomial of a simple cycle of length \(2k\). Because distinct union components have disjoint vertex sets,
\[
P_\lambda(z)=(1+z)^{m_1(\lambda)}
\prod_{k\ge2} C_{2k}(z)^{m_k(\lambda)},
\]
where \(m_k(\lambda)\) is the multiplicity of part \(k\). By inclusion-exclusion over the forbidden edges, the number of common neighbours of the two original matchings is
\[
\mathcal D(\lambda)=\sum_{j=0}^{n}(-1)^j a_j(2n-2j-1)!!,
\qquad (-1)!!=1.
\tag{1}
\]
Indeed, a specified set of \(j\) disjoint forbidden edges extends to exactly \((2n-2j-1)!!\) perfect matchings, while overlapping forbidden edges have no common extension. In particular \(\mathcal D(\lambda)=|N(A)\cap N(B)|\) for any pair of type \(\lambda\). This proves that \(d(\rho)=\mathcal D(\rho)\) is well defined, including \(\rho=\varnothing\).

**Step 2: the cycle-splitting identity.** Introduce the transfer matrix
\[
T(z)=\begin{pmatrix}1&z\\1&0\end{pmatrix}.
\]
The ordinary matching polynomial of a cycle of length \(\ell\ge3\) is \(C_\ell(z)=\operatorname{tr}(T(z)^\ell)\): the transfer states encode whether the previous cycle edge was selected, so the trace counts cyclic choices of pairwise nonincident edges. For any two-by-two matrix \(U\),
\[
(\operatorname{tr}U)^2-\operatorname{tr}(U^2)=2\det U.
\]
Use \(U=T(z)^{2m}\) and \(\det T(z)=-z\) to obtain the polynomial identity
\[
C_{2m}(z)^2-C_{4m}(z)=2z^{2m}.
\tag{2}
\]
All cycles here have at least four edges, as \(m\ge2\). Multiplication by \(P_\rho(z)\) shows that
\[
P_{(m,m)\sqcup\rho}(z)-P_{(2m)\sqcup\rho}(z)
=2z^{2m}P_\rho(z).
\tag{3}
\]
Apply the inclusion-exclusion functional (1), now with \(n=2m+r\). If \(P_\rho(z)=\sum_{j=0}^r b_jz^j\), the difference becomes
\[
2\sum_{j=0}^{r}(-1)^{2m+j}b_j
\bigl(2(2m+r-(2m+j))-1\bigr)!!
=2\sum_{j=0}^{r}(-1)^jb_j(2r-2j-1)!!
=2d(\rho).
\]
This proves the boxed identity for all stated parameters.

**Step 3: the exact zero condition.** When \(r=0\), the empty matching on the empty ground set is the unique choice, hence \(d(\varnothing)=1\). When \(r=1\), the only prescribed pair is the same edge, and no perfect matching avoids it, so \(d((1))=0\). For \(r=2\), the union of the prescribed matchings is either two disjoint edges or a four-cycle. The complement of either union in \(K_4\) contains a perfect matching. For every \(r\ge3\), the complement of the union in \(K_{2r}\) has minimum degree at least \(2r-3\ge r\), because each vertex has at most two forbidden neighbours. Dirac's elementary Hamiltonicity criterion therefore supplies a Hamilton cycle and hence a perfect matching in that complement. Thus \(d(\rho)>0\) for all \(r\ge2\), finishing the zero classification.

**Step 4: the two-round obstruction.** Set \(\rho=(1)\), so \(n=2m+1\). The matchings \(B_{\mathrm{split}}\) and \(B_{\mathrm{join}}\) both share exactly one edge with \(A\); consequently both are non-neighbours of \(A\) and have the same first-round colour. At round two, their counts of neighbours in the first-round neighbour class \(N(A)\) are the respective common-neighbour counts in the boxed identity, and these are equal because \(d((1))=0\). Both have zero adjacency to the singleton \(A\) and, since \(D_n\) is regular, the same neighbour count into the remaining first-round class. Their second-round colours therefore coincide.

Their cycle types \((m,m,1)\) and \((2m,1)\) are distinct, so they lie in different orbits under the permutations of the \(2n\) underlying points that fix \(A\). In fact this is also a distinction for the *full* graph automorphism group: Godsil and Meagher, Lemma 10.1 of the cited paper, prove \(\operatorname{Aut}(D_n)\cong S_{2n}\) for \(n\ge3\), with the natural action. Hence the second-round refinement partition is strictly coarser than the full rooted orbit partition for all odd \(n\ge5\).

## Verification

For instance, the two superposition types \((2,2,1)\) and \((4,1)\) in \(D_5\) each have exactly \(328\) common neighbours with the anchor, while types \((2,2)\) and \((4)\) in \(D_4\) have respectively \(33\) and \(31\). The included `verify_switch.py` independently forms cycle matching polynomials through the path recurrence and applies inclusion-exclusion with exact integers. It checks the polynomial identity for \(2\le m\le74\), checks the switching formula against every integer partition of residual sizes \(0\le r\le8\) for \(2\le m\le16\), and computes an **exact finite census** of common-neighbour-count collisions for \(2\le n\le25\). The census is evidence for finite sizes only and is not used to claim an all-size classification of other collision types.

The included `verify_graph.py` uses an independent bitmask recursion to count common neighbours without polynomial inclusion-exclusion, checks thirteen switch instances, and constructs the derangement adjacency quotient under the natural rooted orbit action for \(3\le n\le7\). For sizes five and seven it confirms both the second-round collision and its separation at the third round. The last observation is intentionally **not** extrapolated to arbitrary odd \(n\).

Run from the directory containing these files:

```text
python3 verify_switch.py
python3 verify_graph.py
```

Outputs from executions of exactly these files are recorded in `verification_output.txt`. Neither finite check is needed to fill a gap in the infinite mathematical proof.

## Relationship to prior work

Godsil and Meagher, *An algebraic proof of the Erdős–Ko–Rado theorem for intersecting families of perfect matchings* (first publicly submitted 2015-06-29, arXiv:1506.08770), introduce and analyse the perfect-matching derangement graph, describe its perfect-matching association scheme, and prove the full automorphism-group statement (their Lemma 10.1). Their inspected results concern intersecting families, graph spectrum and automorphisms; they do not state the cycle-splitting common-neighbour law or the two-round refinement collision.

Kersting, Mladenov, Garnett and Grohe, *Power Iterated Color Refinement* (2014-06-21, DOI 10.1609/aaai.v28i1.8992), supply the general colour-refinement/equitable-partition context but do not investigate this matching graph. The present result links an elementary transfer-matrix identity to an exact orbit-recovery obstruction in that particular finite-model-theoretic setting. The matching polynomials and transfer-matrix identity are standard tools; neither is claimed as independently new.

## Limitations

This result does **not** classify all second-round coincidences at arbitrary size, prove that three rounds suffice for orbit recovery, determine the eventual stable partition, or assert global originality beyond the accessible comparisons. The finite collision census to size twenty-five is not an infinite uniqueness proof. Association-scheme formulae from earlier specialist literature may furnish another, possibly stronger expression from which this switching identity could be derived; publication-priority assessment remains open. Independent scientific verification has not been performed.

## References

1. C. Godsil and K. Meagher, *An algebraic proof of the Erdős–Ko–Rado theorem for intersecting families of perfect matchings*, arXiv:1506.08770 (first public version 2015-06-29), especially Sections 3–4 and Lemma 10.1. https://arxiv.org/abs/1506.08770
2. K. Kersting, M. Mladenov, R. Garnett and M. Grohe, *Power Iterated Color Refinement*, Proceedings of AAAI 2014, pp. 1904–1910 (published 2014-06-21). DOI: 10.1609/aaai.v28i1.8992. https://ojs.aaai.org/index.php/AAAI/article/view/8992
