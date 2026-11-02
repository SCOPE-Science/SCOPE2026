# The labelled census of bounded-morphic S5 frame retractions

## Finding
Fix a finite labelled set \(W\) of cardinality \(n\). Let \(a_n\) count ordered pairs \((R,f)\), where \(R\) is an equivalence relation on \(W\) and \(f:W\to W\) is an idempotent bounded morphism of \((W,R)\) to itself. In the formal power-series ring \(\mathbb Q[[z]]\),
\[
\boxed{\sum_{n\ge0}a_n\frac{z^n}{n!}=\exp\!\left(\sum_{t\ge1}\frac{z^t}{t!}\exp\bigl((e^z-1)^t\bigr)\right).}
\]
The empty frame contributes \(a_0=1\), included solely to state the exponential formula. For positive sizes the first counts are \(a_1,\ldots,a_7=1,4,17,107,747,6365,61196\).

More precisely, for a nonempty fixed \(R\) with (distinguishable) equivalence classes \(C_1,\ldots,C_k\) of sizes \(s_1,\ldots,s_k\), the number of its idempotent bounded self-morphisms is
\[
\boxed{E(R)=\sum_{\varnothing\ne J\subseteq[k]}\prod_{i\notin J}\left(\sum_{\substack{j\in J\\s_j\le s_i}}s_j!\,{s_i\brace s_j}\right).}
\]
Here \({s\brace t}\) is the Stirling number of the second kind and the empty inner sum equals zero. The possible image subframes are exactly the unions of classes indexed by subsets \(J\) containing at least one class of globally minimum size. If there are \(g\) smallest classes, their number is \(2^k-2^{k-g}\). For \(k\) equal-size classes of size \(s\),
\[E(R)=\sum_{r=1}^{k}\binom kr (r s!)^{k-r}.\]
All counts distinguish labels and functions, and count actual Kripke-frame relations, not validity theories or isomorphism classes.

## Assumptions and scope
A bounded morphism \(f:(W,R)\to(W,R)\) satisfies both (forth) \(xRy\Rightarrow f(x)Rf(y)\), and (back) \(f(x)Rz\Rightarrow\exists y\,(xRy\land f(y)=z)\). It is idempotent if \(f(f(x))=f(x)\) for all \(x\). An S5 frame is a frame whose relation is an equivalence relation. The theorem holds for each integer \(n\ge0\), with the fixed-partition statement applying to \(n\ge1\). The empty-frame convention is not an assertion about nonempty epistemic models.

## Proof
Forth makes the image of any source class \(C_i\) lie inside one target class \(C_j\). Back makes it cover all of \(C_j\): for any \(z\in C_j\), choose any \(x\in C_i\); since \(f(x)Rz\), back produces a predecessor in \(C_i\) mapping to \(z\). Conversely, these classwise-surjection requirements imply forth and back.

For an idempotent \(f\), every point of its image is fixed. Since its image is the union of complete target classes, the map fixes each class in its image pointwise. Let \(J\) index these classes. Every source class outside \(J\) independently chooses an image class \(C_j\), \(j\in J\), of size at most its own size and a surjection onto it. The number of these surjections is \(s_j!\,{s_i\brace s_j}\). This decomposition is unique and reversible, proving \(E(R)\). If \(J\) misses every globally smallest class, one of those omitted classes has no possible target, whereas if \(J\) contains a globally smallest class every omitted class can surject onto it. Thus the image count follows. For equal sizes, every admissible surjection is a bijection, giving the displayed specialization.

For the all-frame enumeration, record each chosen image class (a *root class*) together with all non-root classes mapping onto it. A root class of size \(t\) is pointwise fixed and carries an unordered set of satellite classes. With the root points already labelled, a satellite of size \(s\) has \(t!\,{s\brace t}\) surjections to the root, and is possible only for \(s\ge t\). Its exponential generating series is
\[\sum_{s\ge t}t!\,{s\brace t}\frac{z^s}{s!}=(e^z-1)^t.\]
An unordered set of satellites therefore has series \(\exp((e^z-1)^t)\). Attaching the \(t\)-point root gives \(z^t\exp((e^z-1)^t)/t!\). Finally, every pair \((R,f)\) decomposes uniquely into an unordered set of these rooted components, and any such unordered set reconstructs exactly one \((R,f)\). Applying the labelled set-construction rule a second time proves the claimed generating function. Every coefficient is finite, as a rooted component has positive size. The argument is a bijection, not an extrapolation from initial counts.

## Verification
Run `python3 checker.py` using Python 3 standard library. The program (i) enumerates every equivalence relation on carriers with one through five labels and independently tests all functions for idempotency, forth and back, checking the fixed-partition counts and image characterization, (ii) verifies the equal-block specialization, and (iii) derives coefficients through order seven independently by rational formal-series multiplication/exponentiation, matching a direct sum over all set partitions. Its final lines contain `ALL_CHECKS_OK` and `ALL_SERIES_CHECKS_OK`. The finite tests support but do not replace the all-order combinatorial bijection.

## Relationship to prior work
Van Benthem, ten Cate and Yang (2026) study preservation and bounded morphic images of finite Kripke frames; their work motivates counting split bounded morphisms but does not provide the census here. Dolinka and East (2014/2015) and Dolinka, East and Mitchell (2015) classify and enumerate idempotent transformations preserving, respectively, uniform and nonuniform partitions; these are **ordinary partition-preserving maps**, not necessarily bounded morphisms. Their general structural criteria are closely related to the fixed-point decomposition used here. In contrast, bounded morphisms impose surjectivity on each source class's target class; the result counts exactly that smaller class and then sums over every labelled S5 partition by a two-level combinatorial construction. In particular the prior count for all partition-preserving idempotents is not the number \(a_n\) here. This does not assert historical priority over all transformation-semigroup enumerations.

## Limitations
The theorem concerns finite, classical, one-agent S5 frames, without atom valuations; it does not enumerate multi-agent frames, approximate bisimulations, ordinary endomorphisms, or unlabelled isomorphism types. No claim is made about independent verification. Similar formulas may exist in earlier literature phrased in terms of surjective block maps or partitioned transformation semigroups; the cited semigroup characterizations are substantial prior overlap. No asymptotic estimate for \(a_n\) is asserted.

## References
1. J. van Benthem, B. ten Cate, X. Yang, *When do modal definability and preservation theorems transfer to the finite?*, arXiv:2603.12171v1 (public 2026-03-12), Sections 3.2 and 3.5, https://arxiv.org/html/2603.12171v1.
2. I. Dolinka and J. East, *Idempotent generation in the endomorphism monoid of a uniform partition*, arXiv:1407.3312v2, especially Proposition 3.1, https://arxiv.org/pdf/1407.3312.
3. I. Dolinka, J. East and J. D. Mitchell, *Idempotent rank in the endomorphism monoid of a non-uniform partition*, arXiv:1504.02520v1, especially Propositions 3.1 and 3.2, https://arxiv.org/pdf/1504.02520.
