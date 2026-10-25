# A sharp automorphism bound in dimension five for perfect evolution algebras

## Finding

**Theorem.** Let \(K\) be any field and let \(A\) be a five-dimensional *perfect evolution algebra* over \(K\): thus \(A\) has a basis \(e_1,\ldots,e_5\), mixed products \(e_ie_j=0\) for \(i\ne j\), and an invertible structure matrix \(M=(a_{ij})\) defined by \(e_i^2=\sum_j a_{ij}e_j\). Then

\[
|\operatorname{Aut}_K(A)|\le155.
\]

Over \(\mathbb C\), equality holds precisely for the single isomorphism class represented by the directed-cycle algebra

\[
e_i^2=e_{i+1}\quad (1\le i<5),\qquad e_5^2=e_1.
\]

Its automorphism group is \(C_{31}\rtimes C_5\) of order \(155\). The maximizing algebra is simple. Consequently the same sharp upper bound holds in the *simple* five-dimensional class. This settles the dimension-five cases of the perfect and simple maximum-automorphism conjectures stated in the 2026 survey [1].

## Assumptions and scope

The characteristic of \(K\) is unrestricted; \(\operatorname{Aut}_K(A)\) denotes **linear algebra automorphisms on \(K\)-points**, not the length of an automorphism group scheme in non-reduced characteristic. The equality and uniqueness assertion is over \(\mathbb C\), where the required roots of unity exist. The statement concerns perfect algebras only; non-perfect evolution algebras may have infinite automorphism groups.

Let \(\Gamma\) be the directed support graph of \(M\), with arrow \(i\to j\) whenever \(a_{ij}\ne0\). Loops are permitted, and distinct vertices may carry arrows in both directions. Because \(\det M\ne0\), at least one permutation \(\sigma\in S_5\) has all five arrows \(i\to\sigma(i)\) in \(\Gamma\). Such a permutation is called a supported matching.

## Proof

**Step 1: reduction to a diagonal group and a graph group.** Since the squares \(e_i^2\) form a basis, the condition \(f_if_j=0\) for \(i\ne j\), for another natural basis \(\{f_i\}\), forces disjoint coordinate supports of the \(f_i\). Hence every algebra automorphism is monomial. Let \(D\) be its diagonal subgroup and let \(H\le\operatorname{Aut}(\Gamma)\le S_5\) be the permutation image. Then

\[
|\operatorname{Aut}_K(A)|=|D||H|\le|D|\,|\operatorname{Aut}(\Gamma)|.
\]

A diagonal map \(e_i\mapsto t_i e_i\) belongs to \(D\) exactly when

\[
t_j=t_i^2\qquad\text{for every arrow }i\to j.
\]

Fix any supported matching \(\sigma\). On a cycle of length \(\ell\) in \(\sigma\), these relations determine all \(t_i\) from one value satisfying \(t^{2^\ell-1}=1\). Thus \(D\) embeds into a product of root-of-unity groups and its order divides the corresponding product. The seven possible cycle types of \(\sigma\), with the product \(P(\sigma)=\prod_{C}(2^{|C|}-1)\), are:

| Cycle type | \(P(\sigma)\) |
|---|---:|
| \(1+1+1+1+1\) | 1 |
| \(2+1+1+1\) | 3 |
| \(2+2+1\) | 9 |
| \(3+1+1\) | 7 |
| \(3+2\) | 21 |
| \(4+1\) | 15 |
| \(5\) | 31 |

In particular, \(D\) is a finite abelian group of order at most \(31\), with possible prime divisors only \(3,5,7,31\). The relations and the graph-permutation action are standard [2,3]; the case analysis below is the new bound on their *combined* orders.

**Step 2: an element of order \(31\).** If \(D\) contains such an element, the table forces \(\sigma\) to be a five-cycle. Its five diagonal coordinates are distinct primitive \(31\)st roots \(t,t^2,t^4,t^8,t^{16}\). For every vertex, the only possible target with coordinate equal to the square of its own is its successor in \(\sigma\). Therefore \(\Gamma\) is *exactly* that directed five-cycle. It has five graph automorphisms and \(|D|\le31\), so the product bound is \(155\).

**Step 3: an element of order \(5\).** The table forces a supported matching of type \(4+1\). For an order-five diagonal element, its four nontrivial coordinates are distinct and lie on the directed four-cycle, while the fifth coordinate is one. Squaring preserves the nontrivial-coordinate set and forces exactly the four cycle arrows there; the remaining vertex can have only a loop. Thus \(\Gamma\) is a disjoint four-cycle and a loop, its graph automorphism group has order four, and \(|D|\le15\). Their product is at most \(60\).

**Step 4: an element of order \(7\).** The supported matching has type \(3+1+1\) or \(3+2\), so \(|D|\le21\). An order-seven diagonal element takes three distinct nontrivial values \(t,t^2,t^4\), forming a forced directed three-cycle, and takes value one at the other two vertices. No arrows may cross between those two sets. The order-seven Sylow subgroup of the abelian group \(D\) is characteristic, and the graph permutation image normalizes \(D\), so every realized graph symmetry preserves these two sets. In fact the same bound applies to every graph symmetry: the three-cycle is the only directed component with three vertices, while the two other vertices support a graph having a perfect matching and no arrows to the three-cycle; a two-vertex component cannot be isomorphic to the directed three-cycle. The graph automorphism group therefore has order at most \(3\cdot2=6\). The product is at most \(126\).

**Step 5: only \(3\)-power torsion remains.** If \(D=1\), its product with the graph group is at most \(5!=120\). Otherwise, by the table, \(|D|\in\{3,9\}\).

If \(|D|=3\), let \(d\) generate \(D\) and let \(V_0,V_+,V_-\) be the vertex sets carrying the coordinates \(1,\omega,\omega^2\) of \(d\), respectively. Each arrow goes within \(V_0\) or switches \(V_+\) and \(V_-\). A supported matching consequently gives \(|V_+|=|V_-|=k\), where \(k=1\) or \(2\). Because the diagonal subgroup is normal, a graph permutation coming from an algebra automorphism preserves \(V_0\) and either preserves or exchanges \(V_+,V_-\). Hence the **realized permutation subgroup** (which is all that is needed in the bound) has order at most

\[
2(k!)^2(5-2k)!\le12.
\]

Thus \(|\operatorname{Aut}_K(A)|\le3\cdot12=36\) in this case. (The same setwise bound need not hold for every graph symmetry without reference to \(D\).)

If \(|D|=9\), a supported matching must have type \(2+2+1\), and \(D\) is the entire \(C_3\times C_3\) diagonal group allowed by that matching. Its five coordinate characters on \(D\) are the distinct characters \(\chi,-\chi,\psi,-\psi,0\). The relation \(t_j=t_i^2\) **for every element of \(D\)** allows only the two matching two-cycles and the fifth loop. Hence \(\Gamma\) is exactly two disjoint directed two-cycles and one loop; its graph automorphism group has order \(8\). Thus \(|\operatorname{Aut}_K(A)|\le9\cdot8=72\).

The exhaustive cases yield \(155,60,126,36,72,120\) as respective upper bounds, proving the claimed universal inequality.

**Step 6: attainment and uniqueness over \(\mathbb C\).** For the unweighted directed five-cycle, the diagonal relations admit exactly \(31\) choices, parametrized by a \(31\)st root of unity; the five rotations also act as algebra automorphisms. Hence the group has order \(31\cdot5=155\). The diagonal subgroup is normal and the rotation conjugates it nontrivially, giving \(C_{31}\rtimes C_5\). Any complex equality case must have a directed five-cycle as support by the strict bounds in Steps 3–5. For a weighted cycle \(e_i^2=a_i e_{i+1}\), \(a_i\ne0\), choose nonzero scalars recursively by \(s_{i+1}=a_i s_i^2\); cycle closure reduces to one equation \(s_1^{31}=c\) with \(c\ne0\). Over \(\mathbb C\) it has a solution. The rescaled basis satisfies the unweighted cycle equations, so the maximizing isomorphism class is unique. Finally, every nonzero ideal of the cycle algebra contains a basis vector (multiply any of its nonzero elements by a suitable basis vector) and then all five basis vectors by repeated squaring; thus it is simple.

## Verification

The accompanying `verify.py` independently performs an **exhaustive finite support-graph check**, not an unbounded search or a substitute for the field-uniform argument. A supported matching constrains any nontrivial prime-order diagonal element to one of four patterns: a \(2+2+1\) or \(2+1+1+1\) coloring for order three, a \(4+1\) coloring for order five, a \(3+2\) or \(3+1+1\) coloring for order seven, or a five-cycle for order thirty-one. The script generates *all* allowed support graphs for such patterns, retains only supports containing a perfect matching, computes the exact diagonal-kernel order by linear algebra modulo \(3,5,7,31\), and checks all \(120\) vertex permutations for graph automorphisms.

It finds \(3304\) labeled supports with nontrivial diagonal group, maximum product \(|D|\,|\operatorname{Aut}(\Gamma)|=155\), attained by exactly the \(24\) labeled directed five-cycles. Graphs with trivial diagonal group are covered directly by the bound \(5!=120\). Run `python3 verify.py`; success prints `VERIFY_OK`.

## Relationship to prior work

Elduque and Labra [3] established the graph-theoretic diagonal group and exact-sequence framework. Sriwongsa and Zou [2, Theorem 4.1] proved that the **diagonal subgroup alone** has maximal order \(2^n-1\), and classified its maximizers. Their theorem identifies the candidate directed five-cycle and its group of order \(155\), but does not exclude a different five-dimensional graph with a smaller diagonal group and a larger permutation factor. The present work supplies exactly that missing comparison.

Costoya, Mayorga and Viruel [4] restrict highly transitive permutation images, rather than bounding all five-dimensional automorphism groups. Hu [5] identifies a five-dimensional perfect algebra with group \(A_5\), of order \(60\); this does not dominate \(155\). Most directly, the October 2026 survey [1, Conjectures 3 and 4] explicitly lists \(155\) as the conjectural dimension-five maximum and reports verification only in dimensions at most four. The proof above establishes that remaining case without enumerating structure-constant matrices.

## Limitations

The bound is about ordinary algebra automorphism groups, not nonreduced group-scheme lengths. Equality classification is asserted over \(\mathbb C\); over other fields a directed five-cycle need not have all \(31\) diagonal automorphisms. This does not classify all five-dimensional evolution algebras or settle the maximum-order conjectures in dimensions greater than five. Unindexed equivalent arguments remain a possible originality risk.

## References

1. I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248 (first posted 15 October 2026), §2.3, Conjectures 3–4.
2. S. Sriwongsa and Y. M. Zou, *On Automorphism Groups of Idempotent Evolution Algebras*, arXiv:2202.01333 (2022), Theorems 2.2 and 4.1.
3. A. Elduque and A. Labra, *Evolution algebras, automorphisms, and graphs*, arXiv:1902.02191 (2019), §§2–3.
4. C. Costoya, P. Mayorga and A. Viruel, *Permutation Representations and Automorphisms of Evolution Algebras*, Mediterranean Journal of Mathematics **22**, 149 (2025), doi:10.1007/s00009-025-02924-0, Theorem A.
5. X. Hu, *Triply Transitive Natural Permutation Images of Idempotent Evolution Algebras*, preprints.org manuscript 202610.0914, posted 13 October 2026, Main Theorem and §1.
