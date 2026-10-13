# Idempotent retraction spectra of powers of finite Gödel chains

## Finding

Let \(C_{n+1}\) be the \((n+1)\)-element Heyting chain and \(G_{m,n}=C_{n+1}^{\,m}\), for integers \(m,n\geq1\). Write
\[
 b_n(k)=\sum_{j=0}^{k-1}\binom{n-1}{j}\qquad(1\leq k\leq n).
\]
An endomorphism is called a *retraction* when it is idempotent. For each multiset \(\{k_1,\ldots,k_r\}\) of \(r\) integers in \(\{1,\ldots,n\}\), where \(1\leq r\leq m\), let \(c_t=|\{i:k_i=t\}|\). The number of retractions of \(G_{m,n}\) whose images are isomorphic to \(\prod_{i=1}^r C_{k_i+1}\) is exactly
\[
 \boxed{\frac{m!}{(m-r)!\prod_{t=1}^n c_t!}
 \left(\sum_{i=1}^r b_n(k_i)\right)^{m-r}.}
\]
All these image types occur, and no other retraction-image types occur. Thus the number of distinct image **isomorphism types** is
\[
 \boxed{\binom{m+n}{m}-1.}
\]
The set of possible retraction image sizes is precisely
\[
 \left\{\prod_{i=1}^r(k_i+1):1\leq r\leq m,\ 1\leq k_i\leq n\right\}.
\]
In particular, the complete image-rank polynomial of idempotent Heyting endomorphisms is
\[
 \boxed{I_{m,n}(z)=\sum_{r=1}^m\binom mr
 \sum_{k_1,\ldots,k_r=1}^n
 \left(\sum_{i=1}^r b_n(k_i)\right)^{m-r}
 z^{\prod_{i=1}^r(k_i+1)}.}
\]
The multiset formula above resolves ranks that coincide numerically but correspond to nonisomorphic images.

For the smallest non-Boolean two-factor power, \(G_{2,2}=C_3^2\), this becomes
\[
 I_{2,2}(z)=2z^2+4z^3+z^4+2z^6+z^9,
\]
so there are ten idempotent endomorphisms, with possible image sizes \(2,3,4,6,9\). For \(G_{3,2}=C_3^3\), there are 59 idempotents.

## Assumptions and scope

The algebra is a **finite direct power of one nontrivial Gödel (prelinear Heyting) chain** with operations \(0,1,\wedge,\vee,\to\); all endomorphisms preserve these operations. The integers \(m,n\) are positive and there is no restriction on idempotent maps being injective or surjective. The claimed counts are about endomorphisms, not arbitrary bounded-lattice maps, and the images are classified **up to Heyting-algebra isomorphism**, not as individually embedded subalgebras.

This power family is a natural explicit subfamily of the finite Heyting algebras forming the age considered by Yamamoto. For the purpose of this result the only fact needed from general Heyting theory is finite poset duality with open (bounded) p-morphisms.

## Proof

**Dual normal form.** Let \(P_{m,n}\) be the disjoint union of \(m\) linearly ordered \(n\)-point chains \(L_1,\ldots,L_m\). Its algebra of upward-closed subsets is \(G_{m,n}\). By finite Heyting duality, an endomorphism of \(G_{m,n}\) is precisely the inverse-image action of a unique map \(f:P_{m,n}\to P_{m,n}\) satisfying
\[
 x\leq y\Longrightarrow f(x)\leq f(y),
 \qquad f[\uparrow x]=\uparrow f(x).
\]
Because the image of a totally ordered set is ordered, each source component \(L_i\) maps into a single target component. Applying the second condition at the least point of \(L_i\) shows that its image must be a final segment of that target chain. If this segment has \(k\) points, the restriction is a nondecreasing surjection from \(n\) ordered points onto \(k\) ordered points. Such surjections correspond to compositions of \(n\) into \(k\) nonempty consecutive blocks, and hence number \(\binom{n-1}{k-1}\). Conversely, all these maps obey the displayed p-morphism condition at every point: after any point, the remaining blocks visit every target level from its current level to the top. This proves the normal form.

**Idempotence.** Suppose \(f^2=f\) and let \(S=f(P_{m,n})\). Then \(f\) is the identity on \(S\). By the normal form, \(S\) is a union of nonempty final segments from exactly \(r\) target chains. Write their lengths \(k_1,\ldots,k_r\). On each **active** source chain (that is, one containing points of \(S\)), the map must fix its selected final segment. All points below that segment must map to its least point: they are below that fixed point, and their images must lie inside \(S\). Thus its entire restriction is forced uniquely.

Every **inactive** source chain may map into any one of these \(r\) selected final segments. To land inside the selected segment of length \(k_i\), its image may be any final segment of length \(j\), with \(1\leq j\leq k_i\). The number of choices is therefore
\[
 \sum_{j=1}^{k_i}\binom{n-1}{j-1}=b_n(k_i).
\]
The choices for different inactive chains are independent; they contribute \(\bigl(\sum_i b_n(k_i)\bigr)^{m-r}\) in total. Conversely, every map so constructed fixes every point of its image, so is idempotent and a p-morphism.

There are \(m!/(m-r)!\prod_t c_t!\) ways to select and assign the \(r\) image-component lengths to distinct labelled target components. Multiplying proves the stated multiset count.

**The algebraic image.** As \(S\) is an upward-closed union of final segments, the restrictions to \(S\) of upsets of \(P_{m,n}\) run over all upsets of \(S\). Surjectivity of \(f:P_{m,n}\to S\) makes inverse image injective on upsets of \(S\). Therefore the image of the dual algebra endomorphism is isomorphic to the upset algebra of \(S\), namely \(\prod_{i=1}^r C_{k_i+1}\). Distinct multisets yield nonisomorphic algebras: their finite dual posets decompose uniquely into these nonempty connected chain components. Conversely any allowed multiset can be realized by selecting target segments, taking the forced maps on active chains, and sending all inactive chains into one selected segment.

There are \(\binom{n+r-1}{r}\) multisets of cardinality \(r\) from \(n\) lengths. Summing over \(1\leq r\leq m\) gives \(\binom{m+n}{m}-1\). Summing the multiset counts by their image cardinalities yields the polynomial stated in the finding.

**Boundary and comparison checks.** For \(n=1\) this specializes to \(G_{m,1}=C_2^m\); the dual maps are ordinary functions on an \(m\)-element antichain and the idempotent count reduces to \(\sum_{r=1}^m\binom mr r^{m-r}\). For \(m=1\), exactly one retraction occurs at each image rank \(2,\ldots,n+1\). As an ungraded consistency check, omitting the idempotence condition gives \(|\operatorname{End}(G_{m,n})|=(m2^{n-1})^m\) from the unrestricted normal form; this latter total is not the asserted new invariant.

## Verification

The included standalone Python verifier independently enumerates all functions on the dual poset for ten parameter pairs with at most six dual points, filters them by the order and exact p-morphism back condition, tests idempotence, and calculates algebraic image ranks from actual images. It compares the resulting rank distributions with the two formulae derived by the normal form and tests the image-type count at additional parameters. A second independent check explicitly constructs the upsets and verifies preservation of Heyting implication by the inverse-image maps through six dual points. Replay result:

`VERIFY_OK 19555 exact comparisons; exhaustive maps for ten parameter pairs; algebraic implication preservation through 6 dual points`

The finite calculations supplement the proof; they cannot establish the general formulas for unbounded \(m,n\).

## Relationship to prior work

Yamamoto, *The automorphism group of the Fraïssé limit of finite Heyting algebras* (arXiv:2105.01291), supplies the finite p-morphism duality and identifies combinatorics of the age of finite Heyting algebras as a topic of interest. It does not give the above idempotent-image enumeration. The duality itself is standard and is not presented as new.

Aguzzoli and Mordonini, *Counting Homomorphisms Between Finite Gödel Algebras* (DOI:10.1007/978-3-031-74000-8_30; conference proceedings dated 2025), already give a recurrence for total hom-set cardinalities across general finite Gödel algebras. The present result does **not** claim novelty for counting all endomorphisms. Its claimed refinement constrains endomorphisms to be idempotent and classifies their image isomorphism types and ranks. The accessible abstract does not state such a refinement; the publisher chapter full text was not accessible for a definitive line-by-line comparison. Earlier work on automorphism groups treats invertible maps, not the idempotent retraction distribution.

## Limitations

The theorem is specific to equal-factor powers of finite Gödel chains, not arbitrary finite Gödel algebras or arbitrary finite Heyting algebras. It gives isomorphism classes of algebraic images, not a census of separately embedded retract subalgebras. The associated general total-endomorphism count and p-morphism duality are known or straightforward prior consequences and are not claimed as new. A similar idempotent-type formula may appear implicitly in currently inaccessible or unindexed literature. The proof has undergone internal mathematical reconstruction and finite checks, not independent mathematical audit.

## References

1. K. Yamamoto, *The automorphism group of the Fraïssé limit of finite Heyting algebras*, arXiv:2105.01291v4 (first public version 2021-05-04); https://arxiv.org/html/2105.01291v4 . Primary MSC 03C15 is recorded for the journal publication at DOI:10.1017/jsl.2022.43.
2. S. Aguzzoli and M. Mordonini, *Counting Homomorphisms Between Finite Gödel Algebras*, in *Information Processing and Management of Uncertainty in Knowledge-Based Systems*, pp. 365–377 (2025); DOI:10.1007/978-3-031-74000-8_30; accessible abstract: https://air.unimi.it/handle/2434/1166075 .
3. S. Aguzzoli, B. Gerla and V. Marra, *The automorphism group of finite Gödel algebras*, Proceedings of the 40th International Symposium on Multiple-Valued Logic (2010), pp. 21–26; cited in the reference list of the 2025 chapter.
