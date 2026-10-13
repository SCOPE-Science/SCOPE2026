# Minimum-cluster nuclei and complete retraction-rank spectra of finite S5 modal algebras

## Finding

Let \(X\) be a nonempty finite \(\mathsf{S5}\) Kripke frame, with equivalence classes (clusters) \(C_1,\ldots,C_m\), all nonempty, of cardinalities \(a_1,\ldots,a_m\). Let \(\mathcal A_X\) be the Boolean modal algebra \(\mathcal P(X)\), with the usual Boolean operations and \(\Diamond U=\{x\in X:\exists y\in U,\ xRy\}\). We classify its endomorphisms and idempotent endomorphisms by the cardinality of their algebraic images.

For \(1\le i,j\le m\), put
\[
q_{ij}=a_j!\left\{\begin{matrix}a_i\\a_j\end{matrix}\right\},
\]
where the braces are Stirling numbers of the second kind, defined to be zero when \(a_j>a_i\). For a set of cluster indices \(K\subseteq[m]\), define
\[
T(K)=\prod_{i=1}^m\left(\sum_{j\in K}q_{ij}\right),\qquad
s(K)=\sum_{j\in K}a_j.
\]
An empty inner sum is zero. The complete algebra-image-cardinality generating polynomials are
\[
\boxed{E_X(z)=\sum_{\varnothing\ne J\subseteq[m]}
\left[\sum_{K\subseteq J}(-1)^{|J|-|K|}T(K)\right]
 z^{2^{s(J)}}}
\]
for all modal-algebra endomorphisms, and
\[
\boxed{I_X(z)=\sum_{\varnothing\ne J\subseteq[m]}
\left[\prod_{i\notin J}\left(\sum_{j\in J}q_{ij}\right)\right]
 z^{2^{s(J)}}}
\]
for idempotent endomorphisms. The empty product is one. In either polynomial, the coefficient of \(z^d\) counts endomorphisms whose image has exactly \(d\) elements, combining terms if several sets \(J\) have the same sum \(s(J)\).

Write \(a=\min_i a_i\) and let \(r=|\{i:a_i=a\}|\). A nonempty union \(\bigcup_{j\in J}C_j\) is the **image of an idempotent bounded endomorphism of the dual frame** if and only if \(J\) contains at least one cluster of size \(a\). Thus there are exactly
\[
\boxed{2^m-2^{m-r}}
\]
distinct dual-frame retraction supports. Moreover, unrestricted endomorphisms and idempotent endomorphisms have **the same set of possible image cardinalities**. This common rank set is
\[
\boxed{\left\{2^{s(J)}:\varnothing\ne J\subseteq[m],\ J\cap\{i:a_i=a\}\ne\varnothing\right\}.}
\]
This statement is about *supports in the dual frame*, not about the number of distinct embedded retract subalgebras of \(\mathcal A_X\): distinct idempotents can have the same algebraic image.

If \(c_b\) is the number of clusters of size \(b\), then the number of **isomorphism types** represented by idempotent algebra images is exactly
\[
\boxed{c_a\prod_{b>a}(c_b+1)},
\]
where the finite product runs over distinct sizes of non-minimal clusters. In particular, for \(m\) clusters all of common size \(t\),
\[
\boxed{I_X(z)=\sum_{j=1}^{m}\binom{m}{j}(j\,t!)^{m-j}z^{2^{tj}}.}
\]

For the mixed cluster profile \((1,2,3)\), the exact polynomials are
\[
E_X(z)=z^2+20z^8+6z^{16}+12z^{64},
\qquad I_X(z)=z^2+7z^8+z^{16}+z^{64}.
\]
This six-world frame has \(39\) algebra endomorphisms but only \(10\) idempotents. Exactly four of its seven nonempty cluster unions are dual-frame retraction supports. Its only permitted retract image cardinalities are \(2,8,16,64\), rather than every Boolean-algebra image cardinality.

## Assumptions and scope

The frame is finite and nonempty. Its accessibility relation is an equivalence relation, not just a preorder. Its modal algebra has the complete powerset Boolean reduct; this is crucial for the correspondence between its Boolean endomorphisms and point maps. Endomorphisms preserve the Boolean operations and the indicated \(\Diamond\) operator. No assumption that a homomorphism is injective, surjective, or idempotent is made except in the section counting idempotents. The cluster sizes \(a_i\) may be unequal; clusters are individually indexed so distinct supports are counted as concrete subsets of \(X\).

The image of a modal-algebra endomorphism means its image as an algebra homomorphism, and its cardinality is a power of two. A *dual-frame retraction support* refers to the set-theoretic image of a bounded frame map \(f:X\to X\) satisfying \(f\circ f=f\). The two notions are related by Boolean duality but they are not the same concrete subset of the powerset algebra.

## Proof

**1. Elementary dual representation.** Every Boolean-algebra endomorphism \(h:\mathcal P(X)\to\mathcal P(X)\) equals inverse image \(h(U)=f^{-1}(U)\) for a unique function \(f:X\to X\). Indeed, the images \(h(\{y\})\), as \(y\) ranges over \(X\), are pairwise disjoint and partition \(X\). For each \(x\), the unique label \(y\) whose block contains \(x\) defines \(f(x)=y\). This also proves uniqueness. For any relation \(R\), preservation of \(\Diamond\) is equivalent to the bounded-morphism identity
\[
\forall x\in X,\qquad f[R(x)]=R(f(x)).
\]
For the forward implication, apply \(f^{-1}\Diamond=\Diamond f^{-1}\) to every singleton and compare membership at \(x\). Conversely, the equality of successor sets directly shows preservation for every subset. In an equivalence frame, \(R(x)=C_i\) for \(x\in C_i\), so the identity says that each source cluster is mapped *surjectively* onto exactly one target cluster.

Conversely, independently choosing for each \(C_i\) a target index \(j\) and a surjection \(C_i\twoheadrightarrow C_j\) produces a bounded endomorphism and thus an algebra endomorphism. Exactly \(q_{ij}\) surjections exist; no such map exists when \(a_j>a_i\). Distinct point maps give distinct inverse-image algebra maps.

**2. Algebra-image size and unrestricted rank polynomial.** The image of \(f\) is a union of complete clusters. If that union is \(\bigcup_{j\in J}C_j\), then \(|f[X]|=s(J)\). Two subsets of \(X\) have the same inverse image precisely when they agree on \(f[X]\). Therefore \(\operatorname{im}(f^{-1})\) contains exactly \(2^{s(J)}\) elements.

The number of bounded maps whose image lies in \(\bigcup_{j\in K}C_j\) is \(T(K)\), because each source cluster independently chooses a target \(j\in K\) and an onto map. By Boolean-lattice inclusion–exclusion, the number whose image uses exactly the target clusters \(J\) is \(\sum_{K\subseteq J}(-1)^{|J|-|K|}T(K)\). Multiplying by the corresponding image-rank monomial proves \(E_X\).

**3. Idempotence and the minimum-cluster criterion.** Since inverse image reverses function composition, \((f^{-1})^2=f^{-1}\) holds if and only if \(f^2=f\). For an idempotent set function, every point of \(f[X]\) is fixed. If its image is the union of target clusters indexed by \(J\), then each \(C_j\) for \(j\in J\) must be fixed pointwise. Each omitted cluster \(C_i\), for \(i\notin J\), independently maps onto one of those fixed clusters; it has \(\sum_{j\in J}q_{ij}\) possibilities. Their product proves \(I_X\), including boundary cases \(m=1\) and singleton classes.

This product is positive exactly when, for every omitted cluster \(C_i\), there is a selected cluster \(C_j\) no larger than \(C_i\). If \(J\) contains a globally smallest cluster, this is immediate. If it contains none, any omitted globally smallest cluster has no permissible target in \(J\). Hence the stated if-and-only-if criterion. Every bounded endomorphism, even a non-idempotent one, sends any globally smallest source cluster onto a globally smallest target cluster, so its image support also meets the minimum-size family. Conversely, every support meeting that family occurs already for an idempotent. Thus the two rank supports agree. Choosing an arbitrary subset of clusters but insisting on at least one of the \(r\) smallest gives \(2^m-2^{m-r}\) supports and the subset-sum description of all ranks.

**4. Image types and homogeneous formula.** As a finite modal algebra, the image of \(f^{-1}\) is isomorphic to the full modal powerset algebra on the induced equivalence frame \(f[X]\). Its isomorphism type is determined exactly by the multiset of cluster sizes in that frame: the Boolean atoms recover points, and the saturation of an atom recovers its equivalence class. To obtain an admissible multiset, choose between one and \(c_a\) of the minimum-size clusters, and independently between zero and \(c_b\) of each other size \(b\). This gives \(c_a\prod_{b>a}(c_b+1)\) isomorphism types.

When all clusters have size \(t\), a map between two clusters exists only as a bijection, with \(t!\) choices. Fixing a set of \(j\) anchor clusters, every other cluster has \(j\,t!\) choices, giving \(\binom mj(j\,t!)^{m-j}\) idempotents of algebra-image cardinality \(2^{tj}\). This proves the final closed formula.

## Verification

The standalone program `verify.py` enumerates every function on sixteen small finite partition frames, testing the successor-set bounded-morphism condition directly rather than using the counting formula. Independently, it computes the polynomial coefficients by inclusion–exclusion and the idempotent product formula, compares both complete rank distributions, and compares all dual retraction supports. For frames of at most five points it also checks preservation of the \(\Diamond\) operation by inverse image on **every subset**.

A completed replay returned

```text
VERIFY_OK {'shapes': 16, 'candidate_tables': 197086, 'bounded_maps': 1059, 'direct_algebra_subset_checks': 10874, 'rank_checks': 48}
```

These finite computations corroborate the direct proof for all positive cluster profiles. They are not a substitute for the general proof, do not search the literature, and do not constitute independent audit.

## Relationship to prior work

Bezhanishvili and Fernández-Duque's *The Baire closure and its logic* (first public preprint February 6, 2021) supplies the motivating \(\mathsf{S5}\) algebraic perspective and explicitly formalizes frames as unions of clusters, including their lower and upper cluster sizes; its objective is completeness and the Baire quotient, rather than enumerating morphism ranks or idempotent retractions. The cluster decomposition, classical Boolean duality, and Stirling numbers are not claimed as new.

Adams and Dziobiak's *Endomorphisms of monadic Boolean algebras* (2007) is the closest named structural prior work. Its accessible abstract establishes reconstruction of finite monadic Boolean algebras from endomorphism monoids. The full article was access-restricted at the publisher, and no verified open copy was located during this comparison. It is possible that its proof makes some of the present map descriptions implicit. Monteiro, Abad, Savini, Sewald, and Zander (2006) already characterize and enumerate **subalgebras** of finite monadic Boolean algebras; that problem is different from counting idempotent endomorphisms by image rank, although a full-text comparison remains an originality risk.

The proposed precise contribution is the simultaneous heterogeneous-cluster **minimum-support criterion**, **all-idempotent image-rank polynomial**, **unrestricted rank polynomial**, and **retract image-type count**, with an explicit distinction between dual supports and embedded algebraic subalgebras. The formulas make no priority claim over any inaccessible equivalent statement.

## Limitations

The theorem is finite, requires an equivalence frame, and concerns full powerset modal algebras. It does not enumerate distinct embedded retract subalgebras (which need not equal the number of idempotents or of dual support subsets). No extension to infinite frames, arbitrary Boolean S4 algebras, or arbitrary monadic Boolean algebra presentations beyond finite powerset representations is asserted. The published-literature comparison is not exhaustive, particularly because an apparently relevant 2007 article and a 2006 subalgebra article could not be inspected in full. No independent mathematical audit has been performed.

## References

1. G. Bezhanishvili and D. Fernández-Duque, *The Baire closure and its logic*, arXiv:2102.03564v1 (first submitted February 6, 2021); *Journal of Symbolic Logic* 89 (2024), 27–49, DOI: 10.1017/jsl.2024.1. Sections 2–3, especially Definition 2.10.
2. M. E. Adams and W. Dziobiak, *Endomorphisms of monadic Boolean algebras*, *Algebra Universalis* 57 (2007), 131–142, DOI: 10.1007/s00012-007-2028-y (abstract and publisher preview inspected; full text unavailable).
3. L. F. Monteiro, M. Abad, S. Savini, J. Sewald, and M. A. Zander, *Subalgebras of a finite monadic Boolean algebra*, *Reports on Mathematical Logic* 40 (2006), 199–206 (abstract and bibliographic information inspected; full text unavailable).
4. P. Blackburn, M. de Rijke, and Y. Venema, *Modal Logic*, Cambridge University Press, 2001 (standard bounded morphism and relational semantics background; cited by the 2024 primary source).
