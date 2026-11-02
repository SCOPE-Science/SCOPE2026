# Embedded monogenic transformation submonoids, refined by tail depth and cycle period

## Finding
For each integer \(n\ge1\), let \(\mathcal T_n\) be the full transformation monoid on \([n]\). Count *actual subsets*, not isomorphism types, among the monogenic submonoids \(\langle f\rangle_1=\{\operatorname{id},f,f^2,\ldots\}\). Write \(h(f)\) for the greatest distance in the functional digraph of \(f\) from a point to a directed cycle, and \(p(f)\) for the least common multiple of its directed cycle lengths.

For every \(h\ge0\), \(p\ge1\), define formal exponential generating functions
\[
T_0(z)=z,\qquad T_{h+1}(z)=z\exp(T_h(z)),\qquad
F_{h,d}(z)=\exp\left(\sum_{j\mid d}\frac{T_h(z)^j}{j}\right),
\]
with \(F_{-1,d}(z)=1\). Let \(\mu\) be the number-theoretic Möbius function and \(\varphi\) Euler's totient. The exact number of distinct embedded monogenic submonoids whose generators have tail depth \(h\) and cycle period \(p\) is
\[
\boxed{N_{n,h,p}=\frac{n!}{c_{h,p}}[z^n]
\sum_{d\mid p}\mu(p/d)\bigl(F_{h,d}(z)-F_{h-1,d}(z)\bigr),\quad
c_{h,p}=\begin{cases}\varphi(p),&h=0,1,\\1,&h\ge2.\end{cases}}
\]
The pair \((h,p)\) is constant across all generators of the same submonoid, so this is a nonoverlapping classification.

Writing \(N_n=\sum_{h,p}N_{n,h,p}\), there is also an independent exact finite formula
\[
\boxed{N_n=n^n-\sum_{m=1}^{n}\binom nm m^{n-m}
\sum_{\sigma\in S_m}\left(1-\frac1{\varphi(\operatorname{ord}\sigma)}\right).}
\]
The term with \(m=n\) includes permutations. For \(n=1,\ldots,12\), the values are respectively
\[
1,4,26,237,2842,42488,759166,15712098,368357033,9630273372,277566391522,8741608793888.
\]
Moreover,
\[
0\le1-\frac{N_n}{n^n}
=O\!\left(\sqrt n\left(\frac2e\right)^n\right),
\]
so the proportion of transformations which are the unique generator of their own embedded monogenic submonoid tends to one exponentially fast.

## Assumptions and scope
An embedded submonoid always contains the identity transformation on \([n]\), even when it also contains a different idempotent acting as the identity of its cyclic nonunit subgroup. We identify two embedded submonoids only when they are *the same subset* of \(\mathcal T_n\); we do not quotient by relabeling or by abstract isomorphism. The depth of a cyclic vertex is zero. The order of a permutation is the least common multiple of its disjoint-cycle lengths. Every \(n\), \(h\), and \(p\) in the displayed formula is integral with \(n\ge1\), \(h\ge0\), \(p\ge1\); the coefficient extraction is finite and automatically zero for impossible parameters. Formal power series are over \(\mathbb Q\).

## Proof
**1. Functional-digraph normal form.** A transformation is a disjoint labeled set of connected functional digraphs, each consisting of one directed cycle with a rooted in-tree attached at each cyclic vertex. Let \(T_h(z)\) enumerate labeled rooted in-trees of height at most \(h\), including their root. A height-zero tree is a single vertex, so \(T_0=z\). A root has an unordered labeled set of child trees of height at most \(h-1\); the labeled exponential formula yields \(T_h=z\exp(T_{h-1})\) for \(h\ge1\).

A directed cycle of length \(j\) with an independent such rooted tree at each cyclic vertex has exponential generating function \(T_h(z)^j/j\). Requiring all directed-cycle lengths to divide \(d\), then allowing an unordered set of cycles, gives precisely \(F_{h,d}(z)\). This counts all maps whose maximum tail depth is at most \(h\) and whose cycle period divides \(d\).

**2. Exact height and period.** For a functional digraph, \(f^{h+p}=f^h\) once \(h\) is at least its maximum tail depth and \(p\) is a multiple of all directed-cycle lengths. Conversely, a vertex at maximum positive depth witnesses that no exponent below \(h\) can initiate a periodic power sequence, while the restriction to the periodic vertices forces the period to be a multiple of each directed-cycle length. Thus the least threshold of the powers \(f^k\), starting with \(k=0\), is exactly \(h(f)\) and their least eventual period exactly \(p(f)\). Subtracting \(F_{h-1,d}\) isolates maps of exact depth \(h\); Möbius inversion over divisors isolates maps of exact period \(p\). This proves that the numerator in the first boxed formula is the *number of generating transformations* with the indicated parameters.

**3. Multiplicity of generators.** If \(h=0\), \(f\) is a permutation of order \(p\). Exactly \(\varphi(p)\) elements of its cyclic group generate the same embedded monoid. If \(h=1\), the positive powers \(\{f,f^2,\ldots,f^p\}\) themselves form a cyclic group, whose identity is \(f^p\) (possibly different from the ambient identity). Adjoining the ambient identity produces \(\langle f\rangle_1\); exactly \(\varphi(p)\) positive powers generate this submonoid as an ambient monoid. Each such positive power still has depth one and period \(p\). If \(h\ge2\), a generator \(g\) of the same embedded monoid must be a power \(f^k\). Powers with \(k\ge2\) cannot regenerate \(f\), since \(f\) is distinct from all higher powers before the threshold \(h\ge2\), and \(g=\operatorname{id}\) also cannot do so. Hence \(f\) is the *unique* generator. Dividing the transformation counts by precisely \(c_{h,p}\) proves the first boxed formula, and also establishes that \((h,p)\) is well-defined on each embedded monoid.

**4. An exact unrefined sum.** Begin with \(n^n\) generating transformations. Correct for the overcount of each embedded monoid by replacing its \(c_{h,p}\) generating transformations with one. Only maps of depth zero or one require correction. Such a map is specified uniquely by its nonempty cyclic set \(C\subseteq[n]\), of cardinality \(m\), a permutation \(\sigma\in S_C\), and arbitrary images in \(C\) of the \(n-m\) vertices outside \(C\). There are \(\binom nm m^{n-m}\) choices outside the permutation and its period is \(\operatorname{ord}\sigma\). Subtracting \(1-1/\varphi(\operatorname{ord}\sigma)\) for each such map proves the second boxed formula.

**5. Exponential rarity of nonunique generators.** Let \(H_n\) be the number of transformations with tail depth at most one. Discarding period restrictions in step 1 gives
\[
\sum_{n\ge0}H_n\frac{z^n}{n!}=\frac1{1-ze^z}.
\]
All coefficients are nonnegative, and at \(z=1/2\) the right side equals the finite constant \(C=(1-e^{1/2}/2)^{-1}\). Hence \(H_n/n!\le C2^n\). Since \(0\le n^n-N_n\le H_n\), Stirling's bound \(n!=O(\sqrt n(n/e)^n)\) proves the final displayed estimate. No independence or distributional hypothesis is used.

## Verification
Two standalone Python programs are included. `verify.py` forms all \(n^n\) transformations for \(1\le n\le6\), constructs every embedded monoid as a literal set of power maps, classifies its generators by \((h,p)\), independently extracts the formal-series coefficients, and checks every class and generator multiplicity. It reports `VERIFY_OK`. `counts.py` uses an independent integer-partition cycle-index summation to evaluate the second boxed formula through \(n=12\), reports the displayed sequence, and checks the first six totals against enumeration. It reports `FORMULA_OK`. These finite tests corroborate but do not replace the all-\(n\) arguments above.

## Relationship to prior work
Elliott, Levine and Mitchell (arXiv:2303.12387, first public version March 22, 2023) count *isomorphism types* of monogenic submonoids of \(\mathcal T_n\), classified by existence of an index–period pair. Their 2023 article does not count distinct embedded subsets, their generator multiplicities, or provide a bivariate labeled count. The present result fixes the ambient set and counts distinct subsets with exact multiplicities, not just realizable pairs. Standard labeled functional-digraph decomposition supplies a counting method, but not by itself the required quotient by the number of generators of a specific embedded monoid.

A published enumeration of finite polymorphism-homogeneous monounary algebras also uses rooted functional digraphs and the pole of \(1/(1-ze^z)\); its defining restriction is *all sources at one common height*, not our *maximum tail depth* and *monoid equality*. Accordingly neither its labeled counts nor its asymptotic theorem implies the period-refined embedded-submonoid numbers here. A separate embedded enumeration for monogenic inverse submonoids of partial permutations concerns a different ambient semigroup and a chain/cycle rather than rooted-tree decomposition. It does not yield the present full-transformation counts without new combinatorics.

## Limitations
The exact formulas are fully proved, while literature priority has not been independently audited. The Möbius/EGF expansion is explicit and effective but not a simple product for arbitrary prescribed period. We claim neither that the basic functional-digraph exponential formula is new nor that the existence of threshold–period isomorphism classes is new. Equivalent embedded enumerations under different cyclic-subsemigroup terminology might exist outside the inspected sources; this remains a residual novelty risk. The asymptotic statement supplies an exponential upper bound, not a sharp equivalent for the number of overcounted transformations.

## References
1. L. Elliott, A. Levine and J. D. Mitchell, “Counting monogenic monoids and inverse monoids,” arXiv:2303.12387 (first submitted March 22, 2023); *Communications in Algebra* 51 (2023), 4654–4661. DOI: 10.1080/00927872.2023.2214821.
2. P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press (2009), labeled functional digraphs, cycles and rooted-tree enumeration.
3. “Labeled enumeration and asymptotic rarity of finite polymorphism-homogeneous monounary algebras,” publicly available research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-labeled-enumeration-and-asymptotic-rarity-of-finite-polymorphism--396b39babc15 (2026), compared for the functional-digraph restriction and common pole, not treated as a source of the present count.
