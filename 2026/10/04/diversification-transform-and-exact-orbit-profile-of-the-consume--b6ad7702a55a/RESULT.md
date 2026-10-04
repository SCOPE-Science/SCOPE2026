# Diversification transform and exact orbit profile of the consumer-product Fraïssé limit

## Finding

Let \(\mathcal F\) be a relational Fraïssé class with strong amalgamation. For each \(p\geq 0\), suppose there are finitely many \(\mathcal F\)-structures on a fixed labeled \(p\)-element set, and call that number \(f_p\). Kubiś and Shelah define the diversification \(\mathbb D\mathcal F\) by splitting a finite structure into products \(P\) and consumers \(C\), with each consumer independently placing an \(\mathcal F\)-structure on the common product set. Their theorem makes \(\mathbb D\mathcal F\) a Fraïssé class.

If \(U_{\mathcal F}\) is its Fraïssé limit and \(a_n\) is the number of \(\operatorname{{Aut}}(U_{\mathcal F})\)-orbits on injective ordered \(n\)-tuples, then
\[
a_n=\sum_{{p=0}}^n {{n\choose p}} f_p^{{\,n-p}}.
\]
Thus diversification has an exact labeled-profile transform.

For the consumer-product class \(\mathscr{{CP}}=\mathbb D\mathcal L\), where \(\mathcal L\) is the class of finite linear orders, \(f_p=p!\). Therefore
\[
a_n=\sum_{{p=0}}^n {{n\choose p}}(p!)^{{n-p}}.
\]
The injective profile starts
\[
2,4,11,54,567,13928,837321,134985098.
\]
If repetitions are allowed, the complete ordered-tuple profile is the Stirling transform
\[
b_n=\sum_{{k=1}}^n {{n\brace k}}a_k,
\]
which starts
\[
2,6,25,150,1444,27059,1231654.
\]
Finally, the consumer-product injective profile has the sharp leading logarithmic growth
\[
\lim_{{n\to\infty}}\frac{{\log a_n}}{{n^2\log n}}=\frac14.
\]

## Assumptions and scope

The transform concerns the two-sorted diversification exactly as defined by Kubiś and Shelah, including the unary predicates distinguishing \(P\) from \(C\). The finiteness assumption on each labeled count \(f_p\) is needed if the conclusion is to be a finite orbit count. The source allows a countable relational signature, so without this assumption an orbit count can be infinite.

The consumer-product specialization uses the source's class \(\mathscr{{CP}}\), in which every consumer supplies a strict linear order on the product set. No relations occur among consumers themselves.

## Proof

Fix \(n\) distinct ordered coordinates. Because \(U_{\mathcal F}\) is ultrahomogeneous, two injective ordered tuples are in the same automorphism orbit exactly when their induced labeled \(\mathbb D\mathcal F\)-structures agree. Conversely, every finite \(\mathbb D\mathcal F\)-structure occurs in the age of \(U_{\mathcal F}\), so every labeled structure counted below is realized by an orbit.

Suppose exactly \(p\) of the \(n\) coordinates lie in \(P\). There are \({{n\choose p}}\) choices of those coordinate positions. The remaining \(n-p\) coordinates are consumers. For each consumer, the induced structure on the same labeled \(p\)-point product set can be any one of the \(f_p\) labeled \(\mathcal F\)-structures, independently of all other consumers. Hence there are
\[
{{n\choose p}}f_p^{{n-p}}
\]
induced labeled structures with exactly \(p\) products. Summing over \(p\) proves the transform.

For finite linear orders there are exactly \(p!\) orders on a labeled \(p\)-set, giving the consumer-product formula.

For an arbitrary ordered \(n\)-tuple with repetitions, its equality pattern is a set partition into \(k\) nonempty blocks. There are \({{n\brace k}}\) such partitions, and after collapsing equal coordinates the remaining ordered list of first occurrences is an injective \(k\)-tuple. Equality is preserved by automorphisms, so different partitions cannot fuse. This proves the Stirling transform.

For the asymptotic upper bound, \(p!\leq n^p\) and \(p(n-p)\leq n^2/4\), so
\[
a_n\leq\sum_{{p=0}}^n{{n\choose p}}n^{{p(n-p)}}\leq 2^n n^{{n^2/4}}.
\]
For the lower bound take \(p=\lfloor n/2\rfloor\). Stirling's estimate gives
\[
\log(p!)=p\log p-p+O(\log p),
\]
so
\[
\log a_n\geq (n-p)\log(p!)=\frac{{n^2}}4\log n-O(n^2).
\]
Dividing the lower and upper bounds by \(n^2\log n\) proves the limit \(1/4\).

## Verification

The bundled `verify.py` independently constructs all labeled consumer-product structures through \(n=6\) by choosing the product subset and then enumerating every linear order selected by every consumer. It compares the resulting census with the closed sum and checks the first eight formula values. It also computes the Stirling transform in two ways through arity seven and checks the two-sorted-set sanity case \(f_p=1\), where the transform reduces to \(2^n\). The script ends with `VERIFY_OK`.

## Relationship to prior work

Kubiś and Shelah introduce diversification, prove that strong-amalgamation Fraïssé classes remain Fraïssé after diversification, and single out the consumer-product class as the diversification of finite linear orders. Their stated application concerns non-universality of the automorphism group, not exact oligomorphic profile enumeration. In the inspected full text, searches for “profile” returned no occurrence, and “orbit” occurs in the group-action construction rather than as a tuple-orbit census.

The source also notes that Baudisch's earlier generic-variation construction is similar but lacks the two unary predicates \(P,C\). That makes it a useful neighboring construction, but not a source for the two-sorted transform above.

Targeted web searches used the source terminology, the exact consumer-product formula, and the initial sequence; semantic searches in the existing finding index likewise returned no covering result. The closest indexed findings concern unrelated random-poset, random-bipartite, and Rado-graph reduct profiles.

## Limitations

The transform is elementary once the diversification definition and ultrahomogeneity are in place, so an equivalent observation may exist as unindexed folklore. The originality claim is therefore limited to the exact profile transform, its consumer-product specialization, and the stated leading asymptotic; it does not claim novelty for diversification itself.

The verifier checks finite cases only. The all-arity result is proved symbolically from the Fraïssé age description, and the Fraïssé theorem itself is imported from the primary source.

## References

1. W. Kubiś and S. Shelah, “Homogeneous structures with non-universal automorphism groups,” *Journal of Symbolic Logic* 85 (2020), 817–827. arXiv:1811.09650. DOI: 10.1017/jsl.2020.10.
2. A. Baudisch, “Generic variations of models of T,” *Journal of Symbolic Logic* 67 (2002), 1025–1038. DOI: 10.2178/jsl/1190150146.
