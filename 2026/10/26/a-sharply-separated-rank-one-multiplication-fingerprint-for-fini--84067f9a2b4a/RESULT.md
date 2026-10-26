# A sharply separated rank-one multiplication fingerprint for finite transformation variants

## Finding
Let \(X\) be an \(n\)-element set, \(n\geq1\), and let \(a:X\to X\) be any full transformation. On the full transformation monoid \(\mathcal T_X\), define the sandwich product \(f\star_a g=f\circ a\circ g\). Use the *ordinary* permutation subgroup \(\mathfrak S_X\) as a distinguished set of possible outer factors, not as a subgroup of the variant. Define the mixed rank-one product count
\[
B_n(a)=\#\{(\pi,g)\in\mathfrak S_X\times\mathcal T_X:\operatorname{rank}(\pi\star_a g)=1\}.
\]
For each \(z\in\operatorname{im}a\), let \(\lambda_z=|a^{-1}(z)|\); the unordered list \(\lambda\) of these positive sizes partitions \(n\). Then
\[
\boxed{B_n(a)=n!\sum_{z\in\operatorname{im}a}\lambda_z^{\,n}.}
\]
For fixed \(n\), the single integer \(B_n(a)\) uniquely determines the entire kernel-block-size partition \(\lambda\). Consequently (using the independently established variant-isomorphism classification of Tsyaputa),
\[
\boxed{\mathcal T_X^{a}\cong\mathcal T_X^{b}\iff B_n(a)=B_n(b).}
\]
Moreover, if \(n\geq2\), the exact minimum positive separation among the values of this numerical fingerprint is
\[
\boxed{\min_{\substack{\lambda,\mu\vdash n\\\lambda\ne\mu}}
\big|B_n(\lambda)-B_n(\mu)\big|=n!(2^n-2).}
\]
The lower bound is attained by the discrete partition and the partition having one block of size two and all remaining blocks singleton. The displayed minimum is not asserted for \(n=1\), where there is only one partition.

## Assumptions and scope
Every map is a *total* map from \(X\) to itself. Composition is \(f\circ g\) (apply \(g\) first). The variant \(\mathcal T_X^{a}\) has the same underlying set of maps as \(\mathcal T_X\), but multiplication \(\star_a\). Rank is the size of the image. The distinguished outer permutation \(\pi\) is selected using the original action on \(X\); the count is therefore an invariant of a represented sandwich transformation system. It is not asserted that the set of ordinary permutations is intrinsically definable in the abstract variant. Nevertheless, the **numerical value** is constant on abstract variant-isomorphism classes and separates them, by the cited classification and the present injectivity theorem.

The proof holds for all positive integers \(n\), including boundary cases \(n=1\) and constant maps \(a\). The scalar occupies at most \(O(n\log n)\) binary digits because \(0<B_n(a)\le n!n^n\).

## Proof
**Exact count.** A permutation preserves image size, so \(\operatorname{rank}(\pi\circ a\circ g)=1\) if and only if \(a\circ g\) is constant. The latter occurs precisely when every one of the \(n\) values of \(g\) belongs to one common nonempty fiber \(a^{-1}(z)\). Different fibers give disjoint sets of maps \(g\), and a fiber of size \(\lambda_z\) contributes exactly \(\lambda_z^n\) maps. There are \(n!\) independent choices for the outer permutation. This proves the count.

**Separation inequality.** For integers \(2\le m\le n\), the binomial theorem gives
\[
 m^n=m((m-1)+1)^{n-1}
 \ge m(m-1)^{n-1}+m(n-1)(m-1)^{n-2}.
\]
Subtracting \(n(m-1)^{n-1}\) from the right side leaves
\[
(m^2-2m+n)(m-1)^{n-2}>0.
\]
Thus \(m^n>n(m-1)^{n-1}\).

Let \(S_n(\lambda)=\sum_i\lambda_i^n\). For two unequal partitions \(\lambda,\mu\vdash n\), let \(m\ge2\) be the largest part size whose multiplicities differ. Larger parts contribute equally. After exchanging the partitions, the \(m\)-part contribution to \(S_n(\lambda)-S_n(\mu)\) is at least \(m^n\). The remaining parts, all of size at most \(m-1\), have total contribution in each partition at most \(n(m-1)^{n-1}\), since \(k^n\le k(m-1)^{n-1}\) and the sum of their parts is at most \(n\). Therefore
\[
S_n(\lambda)-S_n(\mu)\ge m^n-n(m-1)^{n-1}>0.
\]
This proves injectivity.

**Explicit reconstruction.** Given \(S=B_n(a)/n!\), run \(m=n,n-1,\ldots,2\): set \(c_m=\lfloor S/m^n\rfloor\) and replace \(S\) by \(S-c_m m^n\). After the step at \(m=2\), set \(c_1=S\). The preceding separation bound shows inductively that the combined contribution of all parts smaller than \(m\) is strictly less than \(m^n\); hence each quotient \(c_m\) is exactly the multiplicity of the \(m\)-parts. The final remainder counts singleton parts. The recovered multiplicities sum with weights to \(n\).

**Sharp minimum gap.** If the largest differing part size is \(m=2\), the partitions have identical parts above two, and conservation of total part sum forces the singleton-count difference to be minus twice the doubleton-count difference. Hence
\[
|S_n(\lambda)-S_n(\mu)|=|c_2(\lambda)-c_2(\mu)|(2^n-2)\ge2^n-2.
\]
For \(m\ge3\), the lower bound above is \(h_n(m)=m^n-n(m-1)^{n-1}\). It is strictly increasing on integers \(m\ge2\), since the binomial theorem gives
\[
h_n(m+1)-h_n(m)
 =((m+1)^n-m^n)-n(m^{n-1}-(m-1)^{n-1})
 \ge n(m-1)^{n-1}>0.
\]
For \(n\ge3\), \(3^n>(n+2)2^{n-1}\), proved by the base case \(27>20\) and induction multiplying the left side by three and comparing \(3(n+2)>2(n+3)\). Thus \(h_n(3)=3^n-n2^{n-1}>2^n>2^n-2\). The case \(n=2\) admits no \(m\ge3\). The all-singleton partition and the one-doubleton partition differ by precisely \(2^n-2\). Multiplying by \(n!\) proves the asserted sharp bound.

**Abstract variant-isomorphism consequence.** Tsyaputa's Theorem 2 classifies full-transformation variants on an \(n\)-element set: they are isomorphic precisely when their sandwich transformations have the same unordered nonempty kernel-fiber sizes. The exact-count formula and injectivity above turn that existing partition classification into the scalar equivalence displayed in the finding. No new proof of Tsyaputa's general classification is claimed here.

## Verification
The accompanying executable `verify_kernel_fingerprint.py` uses direct function composition to check the image-rank-one count for each partition through \(n=6\), including actual outer permutations through \(n=4\). It independently enumerates all partitions through \(n=32\), checks greedy reconstruction and collisions, and computes the exact smallest adjacent gap. The recorded finite checks cover 29 direct composition profiles, 11 full outer-permutation profiles, and 43,819 partition reconstructions. Run `python3 verify_kernel_fingerprint.py`. Finite checks are consistency tests; the proof above establishes the unrestricted assertions.

## Relationship to prior work
Tsyaputa's foundational work established the abstract variant-isomorphism criterion from the full partition of nonempty kernel-class sizes, using sizes of equivalence classes in the variant. The new claim is the compression of that partition into one specifically defined rank-one product count, the explicit inverse algorithm, and a sharp universal integer separation. The scalar is not present as a stated classification invariant in the inspected source, even though it encodes the same information. Dolinka and East later studied Green relations, idempotent and regular elements, presentations and generator ranks; their discussion explains why coarse rank-based data alone do not resolve the kernel-partition variation. General elementary power-sum facts or an implicit unlocated treatment could predate this observation; see limitations.

## Limitations
This theorem assumes full transformations of a finite set and marked ordinary permutation outer factors. It does not assert an intrinsic first-order interpretation of the marked permutation set in an unrepresented variant, nor an analogue for partial maps or arbitrary sandwich semigroups. Tsyaputa's older classification is a necessary cited premise of the abstract-isomorphism corollary. The historical priority of using the single particular power sum as an encoding, including possible implicit derivations from the older classification, has not been exhaustively settled. Independent mathematical review has not been performed.

## References
1. G. Y. Tsyaputa, *Transformation Semigroups with the Deformed Multiplication*, arXiv:math/0508386v1, 20 August 2005, especially Theorem 2 and its preceding kernel-fiber equivalence-class count, https://arxiv.org/abs/math/0508386.
2. I. Dolinka and J. East, *Variants of finite full transformation semigroups*, arXiv:1410.5253, originally posted 20 October 2014, especially introduction and Section 4, https://arxiv.org/abs/1410.5253.
