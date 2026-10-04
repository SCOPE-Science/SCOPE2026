# The simple annihilator-compressed graph determines chain lengths of finite principal ideal rings, except for one \(K_2\) ambiguity

## Finding

Let \(R\) and \(S\) be nonzero finite commutative principal ideal rings with identity. Write their canonical decompositions into finite chain rings as \(R\cong\prod_{i=1}^{r}R_i\) and \(S\cong\prod_{j=1}^{s}S_j\), and let \(L(R)=\{\ell_i\}\) and \(L(S)=\{m_j\}\) be the multisets of nilpotency lengths of the maximal ideals, counting a field factor as length \(1\). For the simple annihilator-compressed zero-divisor graph \(\Gamma_E\), one has \(\Gamma_E(R)\cong\Gamma_E(S)\) if and only if either \(L(R)=L(S)\), or \(\{L(R),L(S)\}=\{\{3\},\{1,1\}\}\). Thus, apart from the unique \(K_2\) collision between a length-three chain ring and a product of two fields, the graph recovers the number of local factors and all their nilpotency lengths; residue-field cardinalities are not recovered.

This sharpens the known sufficiency statement for exponent patterns: within finite commutative principal ideal rings, the standard simple annihilator-compressed graph loses exactly one piece of chain-length information, namely the exceptional \\(K_2\\) collision.

## Assumptions and scope

For a commutative ring \\(R\\), two elements are annihilator-equivalent when \\(\\operatorname{ann}(x)=\\operatorname{ann}(y)\\). The graph \\(\\Gamma_E(R)\\) used here is the simple graph of Spiroff--Wickham: its vertices are the annihilator classes of nonzero zero-divisors, and two distinct classes are adjacent exactly when their product is zero.

A nonzero finite commutative principal ideal ring decomposes as a finite product of finite chain rings,
\[
R\\cong R_1\\times\\cdots\\times R_r.
\]
For each factor choose a generator \\(\\pi_i\\) of its maximal ideal and let \\(\\ell_i\\ge1\\) be its length, so \\(\\pi_i^{\\ell_i}=0\\) and \\(\\pi_i^{\\ell_i-1}\\ne0\\); a field has length \\(1\\). Define the chain-length multiset by
\[
L(R)=\\{\\ell_1,\\ldots,\\ell_r\\}.
\]

## Proof

Every element in a finite chain ring has the form \\(u\\pi^a\\) with \\(u\\) a unit and \\(0\\le a\\le\\ell\\), where \\(a=\\ell\\) denotes zero. Its annihilator is determined exactly by \\(a\\). Consequently an annihilator class in the product ring is represented by a valuation vector
\[
a=(a_1,\\ldots,a_r)\\in\\prod_{i=1}^r\\{0,1,\\ldots,\\ell_i\\}.
\]
The all-zero vector is the regular/unit class and the top vector \\((\\ell_1,\\ldots,\\ell_r)\\) is the zero class, so neither is a vertex. Thus
\[
|V(\\Gamma_E(R))|+2=\\prod_{i=1}^r(\\ell_i+1)=:T.
\]
For two distinct vertex vectors \\(a,b\\), coordinatewise multiplication in the chain factors gives
\[
a\\sim b
\\quad\\Longleftrightarrow\\quad
 a_i+b_i\\ge\\ell_i\\text{ for every }i.
\]
This already proves that equal chain-length multisets give isomorphic graphs and that residue-field sizes do not enter the graph.

For reconstruction, the degree of a vertex \\(a\\) is
\[
d(a)=\\prod_i(a_i+1)-1-\\delta(a),
\]
where \\(\\delta(a)=1\\) exactly when \\(2a_i\\ge\\ell_i\\) for every \\(i\\). Indeed, there are \\(a_i+1\\) choices of \\(b_i\\) satisfying \\(a_i+b_i\\ge\\ell_i\\); the zero class is always among these choices and must be deleted, and the vertex itself must also be deleted precisely when its square is zero.

Assume first that \\(r\\ge2\\). A vertex has degree one exactly when it is one of
\[
e_i=(0,\\ldots,0,1,0,\\ldots,0).
\]
Hence the number of leaves is exactly \\(r\\). The unique neighbor of \\(e_i\\) is
\[
c_i=(\\ell_1,\\ldots,\\ell_{i-1},\\ell_i-1,\\ell_{i+1},\\ldots,\\ell_r).
\]
Its degree is
\[
d(c_i)=
\\begin{cases}
T/2-1,&\\ell_i=1,\\\\
T\\ell_i/(\\ell_i+1)-2,&\\ell_i\\ge2.
\\end{cases}
\]
Therefore, once \\(T\\) is known from the graph, the degree of the neighbor of each leaf recovers the corresponding \\(\\ell_i\\). The only numerical overlap between the two displayed cases with \\(T\\ge4\\) occurs when
\[
T/2-1=T m/(m+1)-2
\]
for an integer \\(m\\ge2\\). This rearranges to \\(T=2(m+1)/(m-1)\\), yielding only \\((T,m)=(6,2)\\) or \\((4,3)\\). At \\(T=6\\), having at least two factors forces the unique factorization \\(6=2\\cdot3\\), hence \\(L(R)=\\{1,2\\}\\) anyway. The case \\(T=4\\) is the exceptional case considered below.

It remains to distinguish one-factor rings from products. If the graph has no vertices, then \\(T=2\\) and \\(L(R)=\\{1\\}\\). If it has one vertex, then \\(T=3\\) and \\(L(R)=\\{2\\}\\). If it has three vertices, then \\(T=5\\) is prime and \\(L(R)=\\{4\\}\\). For a one-factor ring with at least four vertices, there is exactly one leaf, whereas every product with at least two factors has at least two leaves. Hence all cases with \\(T\\ne4\\) reconstruct the chain-length multiset uniquely.

When \\(T=4\\), there are exactly two multiplicative decompositions into integers at least two: \\(4\\) and \\(2\\cdot2\\). They correspond to \\(L=\\{3\\}\\) and \\(L=\\{1,1\\}\\). In both cases the two nontrivial valuation vectors are adjacent, so the simple compressed graph is \\(K_2\\). This is exactly the collision already exhibited for \\(\\mathbb Z/(p^3)\\) and \\(\\mathbb Z/(pq)\\). No other collision remains.

## Verification

The accompanying `verify.py` constructs the valuation-vector graph directly, independently checks the degree formula at every vertex, implements the reconstruction from graph order, leaves, and leaf-neighbor degrees, and tests every sorted length multiset with at most five factors, each length at most six, subject to graph order at most \\(500\\). It also explicitly checks both exceptional models are \\(K_2\\).

Exact output:

```text
VERIFY_OK
length_multisets_checked=225
maximum_graph_order_checked=498
exception=(3)<->(1,1)=K2
```

The finite computation is a stress test only. The classification for arbitrary finite commutative principal ideal rings is proved by the symbolic reconstruction above.

## Relationship to prior work

Spiroff and Wickham formalized the annihilator-equivalence graph \\(\\Gamma_E(R)\\), motivated by recovering ring-theoretic information from a compressed zero-divisor graph. Their definition is explicitly a simple graph.

Alvir studied the same annihilator-compressed graph for quotients of unique factorization domains. Her Theorem 8 proves that matching irreducible-exponent patterns are sufficient for graph isomorphism, and she explicitly observed that the condition is not necessary for the unlooped graph because
\[
\\Gamma_C(\\mathbb Z/(p^3))\\cong\\Gamma_C(\\mathbb Z/(pq)).
\]
She then proved necessity only in the pure-prime-power and square-free subfamilies. The theorem here shows that, after passing to the full finite commutative principal-ideal-ring class, that displayed \\(K_2\\) phenomenon is the only failure of exponent-pattern recovery.

Anderson and LaGrange later studied structural properties of the annihilator-compressed graph. A different 2018 compression by associatedness was designed to preserve categorical products and characterize finite principal ideal rings; that graph is finer than annihilator compression and therefore does not subsume the present simple-graph reconstruction problem.

## Limitations

The theorem is restricted to finite commutative principal ideal rings and to the simple annihilator-compressed graph. It does not classify arbitrary finite commutative rings, noncommutative principal ideal rings, or looped variants of the compressed graph.

The graph cannot recover residue-field cardinalities: different finite chain rings with the same length have the same annihilator-compressed valuation model. The 2016 Anderson--LaGrange paper was available here at abstract/rendered-summary level rather than as a fully inspected publisher manuscript; because its stated scope is broad compressed-graph structure, an unadvertised isomorphism theorem there remains a residual originality risk.

## References

1. S. Spiroff and C. Wickham, “A Zero Divisor Graph Determined by Equivalence Classes of Zero Divisors,” *Communications in Algebra* 39 (2011), 2338–2348. DOI: 10.1080/00927872.2010.488675. A public preprint was available on 2007-12-29.
2. R. Alvir, “Zero-Divisor Graphs of Quotient Rings,” arXiv:1508.02432, submitted 2015-08-10.
3. D. F. Anderson and J. D. LaGrange, “Some remarks on the compressed zero-divisor graph,” *Journal of Algebra* 447 (2016), 297–321. DOI: 10.1016/j.jalgebra.2015.08.021.
4. A. Đurić, S. Jevđenić, and N. Stopar, “Categorial properties of compressed zero-divisor graphs of finite commutative rings,” arXiv:1807.11283; *Journal of Algebra and Its Applications* 20 (2021), 2150069.
5. B. R. McDonald, *Finite Rings with Identity*, Marcel Dekker, 1974.
