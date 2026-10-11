# Transitive permutation invariants of free \(p\)-convex Banach lattices are isometric AM-spaces

## Finding
Let \(n\ge2\) and \(1\le p\le\infty\). Write \(E=\ell_1^n(\mathbb R)\), and let \(Z_p=\operatorname{FBL}^{(p)}[E]\), the free \(p\)-convex Banach lattice, with the usual convention that \(p=\infty\) denotes the free AM-space. Let \(G\le S_n\) be any **transitive** coordinate-permutation subgroup. Set \(S_p=\{u\in\mathbb R^n:\|u\|_p=1\}\), with its ordinary compact topology.

**Theorem.** The \(G\)-fixed sublattice \(Z_p^G\) is isometrically lattice isomorphic to \(C(S_p/G)\) under
\[
T_p f([u])=n^{1/p}f(u),\qquad u\in S_p,
\]
where \(n^{1/\infty}=1\), and where \(f\) is represented as a continuous positively homogeneous function on \(E^*=\mathbb R^n\). Equivalently, for all such invariant \(f\),
\[
\boxed{\|f\|_{Z_p}=n^{1/p}\max_{\|u\|_p=1}|f(u)|.}
\]
The invariant sublattice is the range of the positive projection \(P_G f=|G|^{-1}\sum_{g\in G}f\circ g\), and \(\|P_G\|=1\).

In contrast, for every finite \(p\), the entire \(Z_p\) fails the AM-space disjoint-supremum identity. For \(G=S_n\), if \(s_k(u)\) is the \(k\)-th largest member of \(\{|u_1|,\ldots,|u_n|\}\), then
\[
\|s_k\|_{Z_p}=(n/k)^{1/p},\qquad1\le k\le n.
\]

## Assumptions and scope
All functions, lattices and scalar fields are **real**. For a function \(f:\mathbb R^n\to\mathbb R\), positive homogeneity means \(f(tu)=tf(u)\) for every \(t\ge0\). The action permutes dual coordinates, and \(G\)-invariant means \(f(gu)=f(u)\) for every \(g\in G\). No assumption of full symmetric-group invariance is made: regular cyclic groups, for example, qualify. The canonical functions \(\delta_{e_i}(u)=u_i\) belong to \(Z_p\). The orbit space \(S_p/G\) is compact Hausdorff because \(G\) is finite.

## Proof
**1. Free-lattice norm reduction.** The functional representation of the free \(p\)-convex lattice [1] gives, for finite \(p\),
\[
\|f\|_{Z_p}=\sup\left\{\left(\sum_{r=1}^m|f(v_r)|^p\right)^{1/p}:m\ge1,\ \max_{1\le j\le n}\sum_{r=1}^m|v_{rj}|^p\le1\right\}.
\]
Indeed, \(\sup_{\|x\|_1\le1}\sum_r|\langle v_r,x\rangle|^p=\max_j\sum_r|v_{rj}|^p\), since a convex function on the finite-dimensional cross-polytope attains its maximum at a signed coordinate vector. Define \(M=\max_{\|u\|_p=1}|f(u)|\). Homogeneity gives \(|f(v)|\le M\|v\|_p\). For any admissible \((v_r)\),
\[
\sum_r|f(v_r)|^p\le M^p\sum_r\|v_r\|_p^p
=M^p\sum_{j=1}^n\sum_r|v_{rj}|^p\le nM^p.
\]
Hence \(\|f\|_{Z_p}\le n^{1/p}M\) for all homogeneous continuous \(f\), invariant or not.

**2. Sharp orbit witness.** Fix \(u\in S_p\) and place one dual row \(v_g=(n/|G|)^{1/p}gu\) for each \(g\in G\), repetitions included if \(u\) has a stabilizer. Transitivity gives
\[
\sum_{g\in G}|(gu)_j|^p=\frac{|G|}{n}\sum_{i=1}^n|u_i|^p=\frac{|G|}{n}
\]
for every column \(j\). Thus these rows meet the weak-summability constraint **with equality in every column**. Since \(f\) is invariant,
\[
\sum_{g\in G}|f(v_g)|^p=n|f(u)|^p.
\]
Taking the supremum over \(u\in S_p\) yields \(\|f\|_{Z_p}\ge n^{1/p}M\), proving the claimed exact equality. For \(p=\infty\), the free AM-space norm is directly \(\|f\|_{Z_\infty}=\max_{\|u\|_\infty\le1}|f(u)|=\max_{S_\infty}|f|\), giving the same formula.

**3. Onto a full continuous-function lattice.** For finite-dimensional \(E\), restriction to the dual unit sphere identifies the underlying vector lattice of \(\operatorname{FBL}^{(p)}[E]\) with \(C(S_{E^*})\) for finite \(p\) [2, Proposition 9.1; 3, Proposition 3.2]. The same conclusion for \(p=\infty\) follows from its continuous homogeneous function model [2]. Consequently every \(a\in C(S_p/G)\) extends homogeneously to \(f\in Z_p\) by \(f(ru)=r\,n^{-1/p}a([u])\) for \(r\ge0\) and \(u\in S_p\), assigning \(f(0)=0\). The exact norm equality proves \(\|f\|_{Z_p}=\|a\|_\infty\), and \(T_p\) is an onto lattice isometry. In particular \(Z_p^G\) is an AM-space with an order unit, given by the preimage of the constant function \(1\).

**4. Complementation.** Each coordinate permutation induces an isometric lattice automorphism of \(Z_p\), by the norm's row/column formula and its \(p=\infty\) counterpart. Averaging these maps yields the positive idempotent \(P_G\), with range precisely \(Z_p^G\) and \(\|P_G\|\le1\). Its restriction to any nonzero fixed function is the identity, so \(\|P_G\|=1\). There is no claim that the average is itself a lattice homomorphism.

**5. The ambient contrast and exact examples.** Let \(h(u)=(|u_1|-|u_2|)_+\) and \(k(u)=(|u_2|-|u_1|)_+\). These are positive, pointwise disjoint, and satisfy \(h\le|\delta_{e_1}|\), \(k\le|\delta_{e_2}|\). The singleton rows \(e_1,e_2\) show \(\|h\|=\|k\|=1\). On the other hand,
\[
(h\vee k)(u)=\big||u_1|-|u_2|\big|,
\qquad (h\vee k)(u)^p\le |u_1|^p+|u_2|^p.
\]
Thus \(\|h\vee k\|\le2^{1/p}\), and the admissible rows \(e_1,e_2\) attain equality. For finite \(p\), this exceeds \(\max\{\|h\|,\|k\|\}=1\), so \(Z_p\) is not an AM-space. For the \(k\)-th absolute-coordinate statistic, \(k\,s_k(u)^p\le\sum_i|u_i|^p\), with equality for a vector having \(k\) equal nonzero absolute coordinates and the rest zero; the norm formula gives \(\|s_k\|=(n/k)^{1/p}\). The \(p=\infty\) case gives \(\|s_k\|=1\).

Finally, transitivity is essential to the uniform multiplier: for the trivial group and finite \(p\), the coordinate function \(f(u)=u_1\) satisfies \(\|f\|_{Z_p}=1\) but \(n^{1/p}\max_{S_p}|f|=n^{1/p}>1\).

## Verification
The central exact identities are the equality of each orbit column sum with \(1\), the resulting equality of the attained free-lattice norm with \(n^{1/p}M\), and the admissible pair of rows \(e_1,e_2\) witnessing ambient non-AM behavior. A standalone standard-library Python checker, `verify_orbit.py`, checks 14,109 integer/rational test identities for dimensions \(2\) through \(5\), integer exponents \(1,2,3\), cyclic transitive groups, and several invariant test functions. These computations are **not** a substitute for the all-dimensions/all-exponents proof given above.

## Relationship to prior work
Jardón-Sánchez–Laustsen–Taylor–Tradacete–Troitsky [1] supply the general free \(p\)-convex norm model; Oikhberg–Taylor–Tradacete–Troitsky [2] develop the full free-lattice function-space model and show general finite-dimensional lattice isomorphisms; Laustsen–Tradacete [3] identify underlying finite-dimensional continuous-function lattices, but not the exact isometric norm on transitive fixed points. Their general results are used explicitly. The additional orbit-saturation argument is what gives the **exact multiplier** and the unexpected isometric AM structure of fixed points for finite \(p\). Oikhberg [4] studies convex geometry of full free-lattice balls, a different invariant.

## Limitations
This is a statement for finite \(n\), real scalars, and coordinate-transitive permutation actions on \(\ell_1^n\). It does not classify arbitrary nontransitive fixed-point sublattices, free lattices over other base spaces, or nonsymmetric norms. No assertion of independent mathematical certification is made. Equivalently stated results in less indexed literature cannot be categorically excluded by a literature search.

## References
[1] H. Jardón-Sánchez, N. J. Laustsen, M. A. Taylor, P. Tradacete, V. G. Troitsky, *Free Banach lattices under convexity conditions*, arXiv:2101.03510 (first submitted 2021-01-10), especially the free \(p\)-convex norm and Theorem 6.1.

[2] T. Oikhberg, M. A. Taylor, P. Tradacete, V. G. Troitsky, *Free Banach lattices*, arXiv:2210.00614 (first submitted 2022-10-02), especially its function model, Proposition 2.2 and Proposition 9.1.

[3] N. J. Laustsen, P. Tradacete, *Banach lattices of positively homogeneous functions induced by a Banach space*, arXiv:2404.06497 (first submitted 2024-04-09), especially Proposition 3.2 and Theorem 3.5.

[4] T. Oikhberg, *Geometry of unit balls of free Banach lattices, and its applications*, arXiv:2303.05209 (first submitted 2023-03-09).
