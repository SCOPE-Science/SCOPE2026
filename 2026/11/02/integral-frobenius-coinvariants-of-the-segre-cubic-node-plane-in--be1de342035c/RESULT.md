# Integral Frobenius coinvariants of the Segre cubic node–plane incidence

## Finding

Let \(S\) be the Segre cubic threefold over a finite field \(\mathbb F_q\) of characteristic at least \(5\), or any of its \(\mathbb F_q\)-forms. Its ten geometric ordinary double points (nodes) form a finite étale scheme \(N\), and its fifteen geometric planes form a finite étale scheme \(M\). Form the integral incidence map
\[
I:\mathbb Z[M(\overline{\mathbb F}_q)]\longrightarrow\mathbb Z[N(\overline{\mathbb F}_q)],\qquad [P]\longmapsto\sum_{n\in N,\,n\in P}[n],
\]
and let \(Q=\operatorname{coker}(I)\). Then
\[
Q\cong (\mathbb Z/2\mathbb Z)^4\oplus \mathbb Z/4\mathbb Z.
\]
For geometric Frobenius \(F\) acting as a permutation \(\sigma\in S_6\) of the six labels, write \(c(\sigma)\) for the number of cycles (including fixed points), and \(\delta(\sigma)=1\) if at least one cycle has odd length, and \(0\) otherwise. The **integral Frobenius coinvariants** admit the uniform classification
\[
\boxed{Q_F=Q/(F-1)Q\cong \mathbb Z/4\mathbb Z\oplus(\mathbb Z/2\mathbb Z)^{\,c(\sigma)-1-\delta(\sigma)}.}
\]
In particular, every form has a canonical degree map \(Q_F\twoheadrightarrow\mathbb Z/4\mathbb Z\), and a nontrivial cyclic order-four summand persists for all eleven Frobenius cycle types.

The eleven invariant-factor lists (suppressing factors equal to one) are: \((1^6):(2,2,2,2,4)\); \((2,1^4):(2,2,2,4)\); \((2^2,1^2):(2,2,4)\); \((2^3):(2,2,4)\); \((3,1^3):(2,2,4)\); \((3,2,1):(2,4)\); \((3^2):(4)\); \((4,1^2):(2,4)\); \((4,2):(2,4)\); \((5,1):(4)\); and \((6):(4)\). Here cycle types and tuples of invariant factors are notation, not numerical exponentiation.

## Assumptions and scope

All geometric node and plane sets and their incidence relations are considered over an algebraic closure of a finite field of characteristic \(p\ge5\). The split Segre cubic has equation
\[
\sum_{i=0}^5 X_i=\sum_{i=0}^5 X_i^3=0\quad\text{in }\mathbb P^5.
\]
The group \(S_6\) permutes coordinates, acts on the ten nodes indexed by **unordered** partitions of six labels into two triples, and acts on the fifteen planes indexed by perfect matchings of six labels. Every finite-field form is represented by an \(S_6\)-conjugacy type (the result also applies to a given descent permutation without requiring existence of every type over every base field). The theorem concerns the abstract finite integral incidence module, **not** a Picard, Chow, cohomological Brauer, or divisor-class group of the singular threefold.

## Proof

**Step 1: Construct the geometric incidence.** Write \(E=\{0,1,2,3,4,5\}\). A node label \(T\) is an unordered partition \(\{T,E\setminus T\}\) with \(|T|=3\); the associated projective point has coordinates \(+1\) on \(T\) and \(-1\) on its complement. A plane label \(m\) is a matching \(\{\{a,b\},\{c,d\},\{e,f\}\}\), whose defining equations are \(X_a+X_b=X_c+X_d=X_e+X_f=0\). The node lies in the plane precisely when all three pairs cross \(T\). There are \(10\) nodes and \(15\) planes, with six planes through each node and four nodes on each plane. In lexicographic labeling, the resulting \(10\times15\) matrix \(I\) has \(0\)-\(1\) entries and
\[
II^{\mathsf T}=4\,\operatorname{Id}_{10}+2J_{10}.
\]
Consequently \(I\) has full row rank over \(\mathbb Q\), and \(Q\) is finite.

**Step 2: Determine the integral group.** Reduce \(I\) modulo two. Elementary elimination gives rank five. The explicit ten-column minor at zero-based matching indices \((0,1,2,3,4,5,6,7,9,12)\) has determinant \(64\), so the finite cokernel has order at most \(64\). The mod-two rank forces exactly five nonunit invariant factors, each even, hence their product is at least \(32\). Each plane is incident to four nodes, so the coordinate-sum map \(\mathbb Z^{10}\to\mathbb Z/4\mathbb Z\) kills the image of \(I\) and induces a surjective homomorphism \(Q\to\mathbb Z/4\mathbb Z\). Therefore at least one invariant factor is divisible by four, implying the product of the five nonunit factors is at least \(4\cdot2^4=64\). It follows that
\[
Q\cong (\mathbb Z/2\mathbb Z)^4\oplus\mathbb Z/4\mathbb Z,
\]
as claimed. The explicit index-\(64\) Hermite computation gives an independent numerical check of this deduction.

**Step 3: Identify the mod-two permutation module.** Let \(V=\mathbb F_2^E\), with its natural \(S_6\)-action, and let \(\mathbf1\in V\) be the all-ones vector. Associate to each unordered triple partition its indicator vector \(\mathbf1_T\) in \(V/\langle\mathbf1\rangle\); replacing \(T\) by its complement changes the indicator by \(\mathbf1\), so this is well defined and \(S_6\)-equivariant. The four nodes on any matching-plane have sum of indicators equal to zero in \(V/\langle\mathbf1\rangle\): choose one node triple by selecting one endpoint in each matched pair modulo simultaneous complementation, and sum their indicators. Thus the indicator construction annihilates \(I\) modulo two and induces an \(S_6\)-equivariant homomorphism
\[
\psi:Q/2Q\longrightarrow V/\langle\mathbf1\rangle.
\]
The ten triple indicators together with \(\mathbf1\) span \(V\) (as confirmed by a rank-six explicit matrix over \(\mathbb F_2\)). Both vector spaces have dimension five by Step 2; hence \(\psi\) is an isomorphism.

**Step 4: Take Frobenius coinvariants.** The functor of coinvariants commutes with reduction modulo two, yielding
\[
Q_F/2Q_F\cong (V/\langle\mathbf1\rangle)_\sigma.
\]
The coinvariants \(V_\sigma\) have one basis element per cycle of \(\sigma\), so \(\dim V_\sigma=c(\sigma)\). The image of \(\mathbf1\) is the vector of the six-cycle lengths modulo two, viewed in these cycle coordinates. This vector is nonzero exactly when some cycle has odd length, and consequently
\[
\dim_{\mathbb F_2}(Q_F/2Q_F)=c(\sigma)-\delta(\sigma).
\]
The multiplication-by-two subgroup \(2Q\) has order two, and hence \(|2Q_F|\le2\). On the other hand, the coordinate-sum map in Step 2 is Frobenius-invariant and still surjects from \(Q_F\) to \(\mathbb Z/4\mathbb Z\). It forces \(|2Q_F|\ge2\). Therefore \(2Q_F\cong\mathbb Z/2\mathbb Z\), and \(Q_F\) has exactly one cyclic order-four invariant factor, with all other factors cyclic of order two. Combining this with the preceding mod-two dimension proves the boxed formula for every permutation \(\sigma\).

## Verification

Run `python -m pip install -r requirements.txt` and then `python verify_segre_incidence.py` using Python 3.10 or later. The program builds all node and plane labels without external data, verifies the geometric incidence parameters and matrix product, tests all \(720\) relabelings for equivariance, checks the mod-two indicator module, computes the Smith and Hermite forms, verifies the displayed determinant-\(64\) minor, and independently checks the eleven conjugacy-type coinvariant presentations as Smith normal forms of \([I\mid F-\operatorname{Id}]\). It reports `VERIFY_OK: all 11 Galois cycle types match the uniform formula`. The exact program is part of this research package. This finite verification proves the enumerated integral identities; the uniform formula additionally follows from the preceding module argument.

## Relationship to prior work

The Segre cubic, its ten nodes, fifteen planes, and coordinate-permutation symmetry are classical. Collino (2012) and Dolgachev (2015) discuss these objects explicitly; Avilov (2018) studies forms and the associated \(S_6\)-descent. Those geometric inputs are not new. The refinement here concerns the **integral cokernel** of the node–plane incidence map and its full family of **Frobenius coinvariants**; these are different from numerical point counts or rational Frobenius representations. Existing published classifications of Segre-cubic forms alone do not yield the stated integral invariant-factor lists without the additional calculation and mod-two module argument.

## Limitations

The calculation does not identify the incidence cokernel with a geometric cohomology, Picard, or Brauer group, nor does it determine any rational-point zeta function. The result assumes good characteristic at least five and classical geometrically split node/plane incidence after extension of scalars. The finite enumeration and a targeted primary-literature comparison support the novelty assessment but cannot certify exhaustive historical priority; a combinatorial-design reformulation of this Smith problem may have been recorded elsewhere. The arithmetic group depends only on the Frobenius permutation type, not on additional coefficients of a presentation.

## References

- Alberto Collino, *Remarks On the Topology of the Fano surface*, arXiv:1211.2621v1 (first publicly posted 2012-11-12), especially the Segre-primal configuration.
- Igor Dolgachev, *Corrado Segre and nodal cubic threefolds*, arXiv:1501.06432v1 (first publicly posted 2015-01-26), especially the ten nodes, fifteen planes, and symmetric model.
- Artem Avilov, *On forms of the Segre cubic*, arXiv:1812.11363v1 (2018-12-29), especially the coordinate symmetry and classification of forms.
- Piotr Pokora and Tomasz Szemberg, *A Pascal-type construction of the Segre cubic and the Cremona–Richmond configuration*, arXiv:2606.18387 (2026), additional geometric context, not an archival source for the theorem.
