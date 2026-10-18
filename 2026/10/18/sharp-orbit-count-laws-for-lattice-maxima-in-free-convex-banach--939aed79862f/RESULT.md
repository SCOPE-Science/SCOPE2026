# Sharp orbit-count laws for lattice maxima in free convex Banach lattices

## Finding
For every integer \(n\geq1\), let \(G\leq S_n\) be a group of coordinate permutations with exactly \(r\) orbits on \(\{1,\ldots,n\}\). Fix \(1\leq p\leq\infty\), and let
\[
Z_{p,G}=\bigl(\operatorname{FBL}^{(p)}[\ell_1^n(\mathbb R)]\bigr)^G
\]
be the invariant closed Banach sublattice. For each integer \(k\geq1\), define its positive lattice-maximum constant
\[
\Gamma_k(Z_{p,G})=\sup\left\{\left\|\bigvee_{j=1}^k f_j\right\|:\ f_j\in (Z_{p,G})_+,\ \max_j\|f_j\|\leq1\right\}.
\]
Then the exact universal answer is
\[
\boxed{\Gamma_k(Z_{p,G})=\min\{k,r\}^{1/p}},
\]
with the convention that the right side equals \(1\) when \(p=\infty\). In particular, for finite \(p\), the fixed-point lattice is an AM-space **if and only if** the permutation action is transitive; when \(r\geq2\), its sharp two-function maximum constant equals \(2^{1/p}\). For fixed finite \(p\), the entire profile stabilizes at \(r^{1/p}\) once \(k\geq r\); neither the individual orbit sizes nor the internal permutation action affect it.

## Assumptions and scope
All Banach lattices and dual coordinates are real. The space \(\operatorname{FBL}^{(p)}[\ell_1^n]\) is the free \(p\)-convex Banach lattice with convexity constant one; for \(p=\infty\), it is the free AM-space. Coordinate permutations act by their canonical isometric lattice automorphisms. Positivity and the finite lattice supremum are pointwise in the standard representation by positively homogeneous functions on \(\mathbb R^n=(\ell_1^n)^*\). The action is allowed to be nontransitive and the exponent need not be an integer.

For finite \(p\), the representation theorem of Jardón-Sánchez et al. gives, for every such lattice function \(f\),
\[
\|f\|^p=\sup\left\{\sum_{s=1}^m|f(x^{(s)})|^p:\ m\geq1,\ \max_{1\leq i\leq n}\sum_{s=1}^m|x_i^{(s)}|^p\leq1\right\}.
\tag{1}
\]
The coordinate constraint follows directly because the weak \(p\)-summing norm on \((\ell_1^n)^*=\ell_\infty^n\) is attained on extreme points of the \(\ell_1\) unit ball. Every function under consideration is positively homogeneous.

## Proof
Suppose first that \(1\leq p<\infty\). Write the coordinate orbits as \(O_1,\ldots,O_r\), with sizes \(d_a=|O_a|\). Define their nonnegative costs on \(\mathbb R^n\) by
\[
c_a(x)=\frac{1}{d_a}\sum_{i\in O_a}|x_i|^p,\qquad C(x)=\max_{1\leq a\leq r}c_a(x).
\]
**Orbit lemma.** Every \(G\)-invariant lattice function \(f\) satisfies
\[
|f(x)|^p\leq\|f\|^p C(x)\qquad(x\in\mathbb R^n).\tag{2}
\]
Indeed, the assertion is trivial at \(x=0\). Otherwise, consider the \(|G|\) vectors \(|G|^{-1/p}g x\), \(g\in G\). For a fixed \(i\in O_a\), the sum of their \(p\)-th coordinate powers is \(c_a(x)\): the group action visits each position in its orbit equally often. After dividing each vector by \(C(x)^{1/p}\), this family satisfies the coordinate constraints in (1). Invariance and positive homogeneity give the left-hand expression \(|f(x)|^p/C(x)\), proving (2). This argument does not require the action to be free.

Let \(f_1,\ldots,f_k\in (Z_{p,G})_+\) with \(\|f_j\|\leq1\), and put \(F=\bigvee_{j=1}^k f_j\). For every admissible finite family \(x^{(s)}\), (2) gives
\[
\sum_s F(x^{(s)})^p\leq\sum_s C(x^{(s)})
\leq\sum_{a=1}^r\sum_s c_a(x^{(s)})\leq r.
\]
Independently, the pointwise inequality \(F^p\leq\sum_{j=1}^k f_j^p\), followed by (1), gives \(\|F\|^p\leq k\). Hence
\[
\Gamma_k(Z_{p,G})^p\leq\min\{k,r\}.\tag{3}
\]

For sharpness put \(q=\min\{k,r\}\). For each \(1\leq a\leq q\), the positive invariant lattice polynomial
\[
h_a(x)=\frac1{d_a}\sum_{i\in O_a}|x_i|
\]
belongs to \(Z_{p,G}\). Its norm is exactly \(1\): the triangle inequality for the lattice norm gives \(\|h_a\|\leq1\), since each generator \(|\delta_{e_i}|\) has norm \(1\). Conversely, the single vector equal to \(1\) on \(O_a\) and zero elsewhere is admissible in (1) and evaluates \(h_a\) to \(1\). Now test \(\bigvee_{a=1}^q h_a\) on the \(q\) vectors \(x^{(a)}=\mathbf1_{O_a}\), whose supports are disjoint. Every coordinate appears in at most one test vector, so the entire family is admissible; at its own orbit indicator, \(h_a(x^{(a)})=1\). Therefore
\[
\left\|\bigvee_{a=1}^q h_a\right\|^p\geq q.
\]
Appending zero lattice functions if \(k>q\) and combining with (3) proves the stated sharp identity for finite \(p\).

For \(p=\infty\), the free AM-space has the supremum norm of positively homogeneous functions on the dual unit ball, so every finite maximum of positive elements has norm equal to the largest input norm. Thus \(\Gamma_k=1\). Finally, a Banach lattice is an AM-space precisely when its positive binary maxima have norm the larger of the two norms. The \(k=2\) formula proves the stated classification for finite \(p\).

## Verification
The accompanying standalone program `verify_orbit_lattice.py` uses exact rational arithmetic. Across every ordered composition into coordinate blocks for dimensions \(1\) through \(7\), each exponent \(p\in\{1,2,3\}\), and every arity \(1\leq k\leq7\), it checks the pointwise orbit-cost certificate on all binary vectors and constructs exact disjoint-support attaining families. Its totals are \(229{,}362\) finite certificate tests and \(2{,}667\) witness tests. The universally quantified theorem, arbitrary real exponents and general invariant functions are established analytically above; finite checks alone are not an infinite proof.

## Relationship to prior work
The explicit norm representation (1) and the free \(p\)-convex universal construction are due to Jardón-Sánchez, Laustsen, Taylor, Tradacete and Troitsky. Oikhberg, Taylor, Tradacete and Troitsky study the structure of free \(p\)-convex lattices and their sublattices. The present result concerns the **sharp positive finite-join invariant of a coordinate-permutation fixed-point sublattice**. In particular, neither the existence of a \(p\)-convex functional representation nor the classical inequality \(\Gamma_k\leq k^{1/p}\) alone gives the orbit-count plateau \(\Gamma_k=r^{1/p}\) for all \(k\geq r\). The transitive case is the already-understood AM-space boundary; the quantitative classification for arbitrarily many nontransitive orbits is the substantive assertion.

## Limitations
The theorem concerns finite coordinate sets, real scalar fields, permutation actions and the standard free \(p\)-convex norm with convexity constant one. It does not classify the fixed lattices up to isometry, address arbitrary linear group actions, or assert an analogous formula for generators other than \(\ell_1^n\).

## References
1. H. Jardón-Sánchez, N. J. Laustsen, M. A. Taylor, P. Tradacete and V. G. Troitsky, *Free Banach lattices under convexity conditions*, arXiv:2101.03510v1 (first public 2021-01-10), especially Sections 1, 3 and 6. https://arxiv.org/abs/2101.03510 ; open full text: https://link.springer.com/article/10.1007/s13398-021-01155-8
2. T. Oikhberg, M. A. Taylor, P. Tradacete and V. G. Troitsky, *Free Banach lattices*, arXiv:2210.00614v1 (first public 2022-10-02), especially Sections 2 and 8. https://arxiv.org/abs/2210.00614 ; open full text: https://ems.press/content/serial-article-files/53326?nt=1
