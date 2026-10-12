# Exact support and image-rank spectra for endomorphisms of finite bi-Gödel chain products

## Finding

Let \(k\geq1\) and let \(a_1,\ldots,a_k\) be positive integers. Write \(C_b\) for the \(b\)-element bounded distributive chain with its uniquely determined Heyting implication and co-Heyting subtraction, and set
\[
A=\prod_{i=1}^{k}C_{a_i+1},\qquad
w_{ij}=\begin{cases}\binom{a_i-1}{a_j-1},&a_i\ge a_j,\\0,&a_i<a_j.\end{cases}
\]

**Theorem (complete endomorphism and retraction image census).** Every endomorphism of \(A\), in the full bi-Heyting signature, is uniquely encoded by an independent choice for each source index \(i\): a target index \(j\) and an order-preserving surjection from an \(a_i\)-point chain onto an \(a_j\)-point chain. There are exactly \(w_{ij}\) maps of the latter kind. Therefore
\[
|\operatorname{End}_{\mathrm{biH}}(A)|=\prod_{i=1}^{k}\left(\sum_{j=1}^{k}w_{ij}\right).
\]

For a nonempty set of indices \(J\subseteq[k]\), the exact counts of all endomorphisms and of idempotent endomorphisms having **dual-image component support** exactly \(J\) are, respectively,
\[
E_J=\sum_{K\subseteq J}(-1)^{|J|-|K|}\prod_{i=1}^{k}\left(\sum_{j\in K}w_{ij}\right),
\qquad
I_J=\prod_{i\notin J}\left(\sum_{j\in J}w_{ij}\right).
\]
Empty inner sums are zero. Let \(m=\min_i a_i\). Then
\[
E_J>0\quad\Longleftrightarrow\quad I_J>0
\quad\Longleftrightarrow\quad\exists j\in J\;(a_j=m).
\]
Every morphism with support \(J\) has image of cardinality
\[
R(J)=\prod_{j\in J}(a_j+1).
\]
Consequently the two **exact** image-rank polynomials are
\[
H_A(z)=\sum_{\varnothing\ne J\subseteq[k]}E_Jz^{R(J)},\qquad
Q_A(z)=\sum_{\varnothing\ne J\subseteq[k]}I_Jz^{R(J)}.
\]
In particular, the attainable image-size spectra for arbitrary endomorphisms and for retracts coincide, despite different multiplicities. When distinct supports have the same numeric image size, their coefficients are added in these polynomials.

For the equal-length case \(a_i=a\), these specialize to
\[
H_A(z)=\sum_{t=1}^{k}\binom kt t!S(k,t)z^{(a+1)^t},
\qquad Q_A(z)=\sum_{t=1}^{k}\binom kt t^{k-t}z^{(a+1)^t},
\]
where \(S(k,t)\) is the Stirling number of the second kind. The total number of endomorphisms in this case is \(k^k\).

For example, \(A=C_3\times C_4\times C_4\) has exactly \(16\) endomorphisms, with image-size histogram \(\{3:4,12:10,48:2\}\); the corresponding idempotent histogram is \(\{3:4,12:6,48:1\}\).

## Assumptions and scope

We work with nontrivial finite chains \(C_{a_i+1}\), positive \(a_i\), finite nonempty \(k\), and endomorphisms preserving \(0,1,\wedge,\vee,\to,\leftarrow\), not merely the bounded lattice or the Heyting reduct. The dual poset \(P\) is the disjoint union of the \(a_i\)-point chains \(P_i\). The order has no comparisons across distinct \(P_i\). Index labels matter for enumeration even when two chain lengths coincide. The rank of an endomorphism means the number of distinct elements in its algebraic image (not matrix rank or cardinality of its dual map image).

## Proof

**Step 1: dual morphisms.** On a finite poset \(P\), the bi-Heyting algebra \(\operatorname{Up}(P)\) has operations
\[
U\to V=P\setminus\downarrow(U\setminus V),\qquad
U\leftarrow V=\uparrow(U\setminus V).
\]
The finite bi-Esakia duality identifies bi-Heyting homomorphisms \(\operatorname{Up}(P)\to\operatorname{Up}(P)\) with inverse-image maps \(f^{-1}\) of isotone self-maps \(f:P\to P\) satisfying both
\[
f[\uparrow x]=\uparrow f(x),\qquad f[\downarrow x]=\downarrow f(x)\quad(x\in P).
\]
These are the familiar upward and downward bounded-morphism conditions; the formulas for the two implications show why both conditions, rather than only one, are necessary. The duality is a bijection, so distinct dual maps give distinct algebra homomorphisms.

**Step 2: a chain must map onto a complete component.** An isotone image of a chain is itself a chain; it therefore lies in one connected component of the target disjoint union, say \(P_j\). For any \(x\in P_i\) the two bounded-morphism identities imply that the image of \(P_i\) contains every point comparable with \(f(x)\). But every point of \(P_j\) is comparable with \(f(x)\). Thus \(f[P_i]=P_j\). Conversely, an isotone surjection from one finite chain onto another satisfies both bounded-morphism identities: for \(y>f(x)\), any preimage of \(y\) lies above \(x\), while for \(y=f(x)\) one may choose \(z=x\); the downward clause is dual. No restriction couples different source components.

An isotone surjection from a chain of \(a_i\) elements to one of \(a_j\) elements corresponds to a composition of \(a_i\) into exactly \(a_j\) positive consecutive fiber lengths, giving \(\binom{a_i-1}{a_j-1}\) maps if \(a_i\ge a_j\), and none otherwise. Independent choices over source components give the claimed total product.

**Step 3: support and its exact count.** A self-map has dual image the union of exactly the target components whose indices are chosen at least once. Maps whose choices all lie in \(K\) number \(\prod_i\sum_{j\in K}w_{ij}\). Inclusion-exclusion over missing targets in a prescribed nonempty \(J\) yields \(E_J\).

Any source component of minimal length \(m\) can only map onto a target component of length \(m\), establishing necessity of the minimum-length support condition. Conversely, if \(J\) contains such a target \(j_0\), choose the identity map on every component in \(J\) and, for each \(i\notin J\), a surjection onto \(P_{j_0}\), possible since \(a_i\ge m\). This constructs an idempotent map with support exactly \(J\), so both counts are positive.

**Step 4: idempotent count.** For an idempotent \(f:P\to P\), every point of \(f[P]\) is fixed. Thus every component in the image support \(J\) must be mapped pointwise identically to itself; other source components may choose any target in \(J\) and any allowed surjection. This gives \(I_J\) and proves that every constructed map is idempotent. The inverse-image duality reverses composition but preserves idempotence.

**Step 5: algebraic image size.** The dual image \(f[P]\) is a union of whole chains. Two upsets of \(P\) have identical preimages under \(f\) precisely when they coincide on \(f[P]\). Every upset of \(f[P]\) extends to an upset of \(P\) by taking no points outside those occupied components. Hence the image algebra is in bijection with \(\operatorname{Up}(f[P])\). An \(a_j\)-point chain has exactly \(a_j+1\) upsets, so its image rank is \(R(J)\). Summing by supports yields \(H_A,Q_A\).

**Step 6: uniform specialization.** If every \(a_i=a\), then \(w_{ij}=1\), so endomorphisms correspond to all functions \([k]\to[k]\). Those with image size \(t\) number \(\binom kt t!S(k,t)\). Idempotent functions with image size \(t\) have \(\binom kt t^{k-t}\) choices. The image cardinality is \((a+1)^t\), giving the displayed formula.

## Verification

The standalone program `verify_bi_godel.py` independently enumerates **all** set maps for all 63 ordered positive length-vectors of total dual size at most six, filters them by the two bounded-morphism conditions, and compares the resulting exact support and image-rank histograms with the inclusion-exclusion and idempotent formulas. It evaluates 1,545,157 candidate functions and 57,970 valid dual endomorphisms. For all 15 vectors of total dual size at most four, it also explicitly builds the upset algebra and checks preservation of **both** residual operations for 2,165 candidate functions. The observed result is:

```text
VERIFY_OK length_vectors 63 candidate_maps 1545157 valid_endomorphisms 57970 direct_bi_Heyting_cases 15 direct_algebra_maps 2165
```

These finite exhaustive checks test the formulas only on the stated bounded domains; the proof above, not a finite extrapolation, establishes the theorem for arbitrary positive lengths and any positive number of factors.

## Relationship to prior work

Martins and Moraschini (2024) define finite bi-Esakia morphisms, prove their up/down lifting properties, and characterize bi-Gödel algebras via co-forests; their main topic is local tabularity and finite combs. This theorem uses that dual framework but adds an **explicit heterogeneous chain-product endomorphism and retraction rank census**. In particular the surjectivity mechanism on connected chains is standard duality rather than the asserted novelty.

Tasiou (2025) proves that finite simple bi-Heyting algebras have connected dual posets and discusses products of simple finite chains in a profinite context. The complete accessible article does not give the weighted binomial enumeration, exact component-support inclusion-exclusion, or paired endomorphism/retraction image-rank polynomials here. Earlier work on Heyting-only products of finite chains permits dual maps onto proper terminal subchains, which full bi-Heyting preservation forbids; its image-rank counts therefore do not directly imply these formulas.

## Limitations

No new duality theorem or surjectivity theorem is claimed; these are established facts used in the proof. The formulas concern **finite products of chains** in the full bi-Heyting signature, not arbitrary finite co-trees, arbitrary infinite products, or Heyting-only morphisms. An equivalent enumeration in earlier work on semigroups of monotone surjections or products of simple algebras cannot be excluded by the searches performed. No independent mathematical or historical-priority audit has been conducted.

## References

1. M. Martins and T. Moraschini, *Local Tabularity is Decidable for Bi-Intermediate Logics of Trees and of Co-Trees*, arXiv:2409.14998v1, first submitted 23 September 2024; especially Sections 2.5–2.6 and Proposition 2.4. https://arxiv.org/html/2409.14998v1
2. L. Tasiou, *Profinite bi-Heyting algebras*, Algebra Universalis 86 (2025), article 16; especially Definition 2.8, Proposition 3.11, Theorem 3.13, and Corollary 3.16. https://doi.org/10.1007/s00012-025-00892-w
