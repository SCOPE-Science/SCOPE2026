# Equivariant commuting-idempotent spectra of finite incidence algebras and crown rotations

## Finding

Let \(P\) be any nonempty finite partially ordered set, \(H\leq\operatorname{Aut}(P)\) any subgroup, \(q\) any prime power, and \(t\geq1\). Write \(A=I(P,\mathbb F_q)\), and let \(\mathcal E_t(A)\) be the set of **ordered, pairwise commuting, idempotent** \(t\)-tuples in \(A\). The group \(H\) acts entrywise on the tuples by permuting incidence-algebra matrix units. Let \(V_H=P/H\) be its vertex-orbit set and \(E_H=\{(x,y):x<y\}/H\) its strict-comparability-orbit set. For any coloring \(c:V_H\to\{0,1\}^{t}\), put

\[
 b_H(c)=\#\{[(x,y)]\in E_H:c([x])\neq c([y])\}.
\]

Then the number of tuples fixed by **every** element of \(H\) is exactly

\[
 \boxed{\#\mathcal E_t(A)^H=\sum_{c:V_H\to\{0,1\}^{t}}q^{b_H(c)}.}
\]

This formula is characteristic-free; in particular it does not require the order of \(H\) to be invertible in \(\mathbb F_q\). It also gives exact orbit counts for any subgroup \(G\leq\operatorname{Aut}(P)\), by

\[
 \boxed{\#(\mathcal E_t(A)/G)=\frac1{|G|}\sum_{g\in G}\sum_{c:P/\langle g\rangle\to\{0,1\}^{t}}q^{b_{\langle g\rangle}(c)}.}
\]

There is an explicit infinite-family evaluation. Define the height-two **crown poset** \(C_m\), \(m\geq3\), with minimal elements \(b_i\), maximal elements \(u_i\), and only strict relations \(b_i<u_i\) and \(b_i<u_{i+1}\), with indices modulo \(m\). Let \(R_m\cong\mathbb Z/m\mathbb Z\) act by simultaneous rotation of the subscripts. Set \(r=2^{t}\). Then

\[
 \boxed{\#\bigl(\mathcal E_t(I(C_m,\mathbb F_q))/R_m\bigr)
  =\frac1m\sum_{d\mid m}\varphi(m/d)
  \left(\left[1+(r-1)q\right]^{2d}+(r-1)(1-q)^{2d}\right).}
\]

Here \(\varphi\) is Euler's totient function, and orbits are **only** under the indicated poset rotations, not under conjugation by the full unit group. The general result is a Potts-type weighted coloring identity for commuting projections in incidence algebras; the crown formula evaluates the induced symmetry-reduced count in closed form.

**Geometric refinement (the same classification).** Over an algebraically closed field \(K\), the **reduced** affine variety of ordered commuting idempotent tuples in the fixed algebra \(I(P,K)^H\) has precisely one geometrically irreducible component for each coloring \(c:V_H\to\{0,1\}^t\). This component is the entire prescribed-diagonal fiber, with dimension exactly \(b_H(c)\). Consequently the dimension of the variety is \(\max_c b_H(c)\), and its number of top-dimensional irreducible components is the number of maximizing colorings. For the trivial subgroup \(H=\{1\}\), if \(2^t\geq\operatorname{height}(P)\), the maximum dimension is the number of strict comparable pairs of \(P\), and the number of top-dimensional components is the number of proper \(2^t\)-colorings of the comparability graph of \(P\). No claim about possible nonreduced scheme structure is made.

## Assumptions and scope

An element of \(I(P,\mathbb F_q)\) is a function on comparable ordered pairs. In its standard basis \(e_{xy}\), for \(x\leq y\), multiplication is \(e_{xy}e_{zw}=\delta_{yz}e_{xw}\). The strict-comparability span \(J\) is a nilpotent ideal, and the diagonal subalgebra \(D\) is naturally \(\mathbb F_q^{P}\), with \(A=D\oplus J\) as vector spaces. The action of \(H\) preserves both subspaces and multiplication. A tuple belongs to \(\mathcal E_t(A)\) when each \(E_i^2=E_i\) and \(E_iE_j=E_jE_i\) for all indices. No connectedness or characteristic assumption is made. Color coordinates refer to the \(t\) ordered idempotents. A strict pair orbit always has unambiguously defined endpoint vertex orbits.

## Proof

**1. Pass to the invariant algebra.** Since the diagonal/strict decomposition is preserved, the fixed algebra \(B=A^H\) has a vector-space decomposition \(B=D^H\oplus J^H\). Its ideal \(J^H\) is nilpotent. Moreover, \(D^H\cong\mathbb F_q^{V_H}\); in particular a diagonal idempotent in \(B\) is the indicator of a subset of vertex orbits. An \(H\)-fixed commuting-idempotent tuple in \(A\) is exactly such a tuple in \(B\).

**2. Simultaneous conjugacy within each diagonal fiber.** For a tuple \((E_1,\ldots,E_t)\) in \(B\) and each bit vector \(\alpha\in\{0,1\}^t\), define

\[
 P_\alpha=\prod_{i:\alpha_i=1}E_i\prod_{i:\alpha_i=0}(1-E_i).
\]

These are pairwise orthogonal idempotents whose sum is \(1\). Let \(d_\alpha\) be the diagonal of \(P_\alpha\), viewed as an element of \(D^H\). The \(d_\alpha\) also form an orthogonal partition of \(1\), and determine precisely a coloring \(c:V_H\to\{0,1\}^t\). Put \(u=\sum_\alpha P_\alpha d_\alpha\). Its diagonal is \(1\), so \(u\in1+J^H\) and is invertible. Orthogonality gives \(P_\alpha u=u d_\alpha\), hence \(P_\alpha=u d_\alpha u^{-1}\). Summing those \(P_\alpha\) with \(\alpha_i=1\) shows that the original tuple is simultaneously conjugate by \(u\) to its diagonal bit-coordinate tuple. Conversely every such conjugate is a commuting idempotent tuple with that diagonal. This argument is explicit and valid even when the field characteristic divides \(|H|\).

**3. Orbit-stabilizer over a fixed coloring.** The finite group \(1+J^H\) has cardinality \(q^{|E_H|}\): for every \(H\)-orbit of strict comparable pairs one may independently choose a constant coefficient. The stabilizer of the diagonal coordinate tuple is the subgroup \(1+K_c\), where

\[
 K_c=\{X\in J^H:X d_\alpha=d_\alpha X\text{ for every }\alpha\}.
\]

Since the coefficient of \([X,d_\alpha]\) on \((x,y)\) equals \((d_\alpha(y)-d_\alpha(x))X_{xy}\), the stabilizer has one free coefficient precisely at a strict-pair orbit whose endpoint colors agree. Thus \(|1+K_c|=q^{|E_H|-b_H(c)}\). Its conjugacy orbit has exactly \(q^{b_H(c)}\) elements. Fibers with different diagonal colors are disjoint, giving the first boxed identity. Burnside's lemma for the action of \(G\) immediately gives the second.

**Geometry of the same fibers.** Over any algebraically closed \(K\), the same conjugation map from \(1+J^H\), an affine space of dimension \(|E_H|\), surjects onto each diagonal-color fiber. This makes the fiber irreducible. The stabilizer is the closed smooth subgroup \(1+K_c\), of dimension \(|E_H|-b_H(c)\), so the orbit dimension is \(b_H(c)\). Every diagonal coordinate of an idempotent satisfies \(z(z-1)=0\), hence the possible diagonal-color fibers form a finite disjoint partition into subsets that are both closed and open in the reduced idempotent-tuple variety. Each such irreducible fiber is therefore exactly one irreducible component. Its maximum dimension and top-component count follow. For \(H=\{1\}\), the strict-pair graph is the poset comparability graph. Its chromatic number equals the maximum chain size: each chain needs different colors, and a rank-by-longest-chain coloring uses that many. Thus whenever \(2^t\) is at least the height, proper colorings attain all strict comparable pairs, and are exactly the maximizing colorings.

**4. Crown evaluation.** A rotation by \(s\) steps on \(C_m\) has \(d=\gcd(m,s)\) orbits among bottom vertices and \(d\) among top vertices. Its orbits of strict comparable pairs form the cycle multigraph on \(2d\) vertex orbits; at \(d=1\) the cycle consists of two parallel edges, which are kept as distinct orbits. Weight an edge by \(1\) for equal endpoint colors and by \(q\) for unequal colors. On \(r=2^t\) colors the transfer matrix is \(W=(1-q)I_r+q\mathbf 1\mathbf 1^\top\). Its eigenvalues are \(1+(r-1)q\) once and \(1-q\) with multiplicity \(r-1\). Therefore the fixed-tuple number for this rotation is \(\operatorname{tr}(W^{2d})=[1+(r-1)q]^{2d}+(r-1)(1-q)^{2d}\). There are \(\varphi(m/d)\) rotations with this value of \(d\). Averaging proves the third boxed formula.

## Verification

The accompanying standalone file `verify.py` constructs incidence-algebra multiplication literally from the relation pairs, identifies idempotents by direct squaring, and tests commuting pairs by both product orders. It compares these actual algebra counts with the independent vertex-orbit/strict-pair-orbit formula for several chains and height-two posets, including a nontrivial order-two automorphism, over \(\mathbb F_2\) and \(\mathbb F_3\). It also compares the divisor/transfer formula against direct orbit-color enumeration for crowns with \(3\leq m\leq5\), including the parallel-edge case at \(d=1\). Run `python3 verify.py`; successful completion prints `VERIFY_OK_EQUIVARIANT_INCIDENCE_IDEMPOTENTS`.

For the three-crown over \(\mathbb F_2\), there are \(730\) individual idempotents, but only \(250\) rotation orbits. For ordered commuting pairs there are \(117652\) tuples and \(39252\) rotation orbits. These are exact consequences of the displayed formulas, not assumptions in the proof. The finite tests are corroboration; the proof above applies to arbitrary finite posets, prime powers, automorphism subgroups and tuple lengths.

## Relationship to prior work

The standard incidence-algebra/path-algebra viewpoint is explained by Quinn (2013). Gargate and Gargate (2019) enumerate single involutions in incidence algebras in odd characteristic; their work supplies a close antecedent for diagonal-constrained element counting. Their (2020) full-text preprint explicitly develops single \((k+1)\)-potent counts for triangular and incidence algebras. The formulas here **do not claim** novelty for the single-idempotent diagonal-fiber method or ordinary graph-coloring transfer matrices. Instead, the final claim is the characteristic-free **simultaneous commuting-idempotent fixed-point law for arbitrary poset automorphism subgroups**, with the resulting symmetry-reduced crown formula. Graph automorphism coloring invariants, including Burnside chromatic polynomials, supply related graph-theoretic background but do not alone count incidence-algebra commuting-idempotent tuples. Older ring-theoretic conjugacy/lifting lemmas may subsume the algebraic step; the explicit counting synthesis and its exact priority require further external assessment.

## Limitations

The theorem counts commuting **idempotents**, not arbitrary commuting elements. The geometric result concerns the reduced variety, not its potentially nonreduced defining scheme. The invariant is under finite poset automorphisms; it does not give classes under the full algebra-automorphism group or general unit conjugation. The crown formula concerns simultaneous rotations, not all dihedral graph symmetries. The statement is a complete exact count, not an asymptotic approximation. A general idempotent-lifting theorem makes one main proof ingredient classical, and historical priority of the combined invariant is not independently certified.

## References

- D. Quinn, “The incidence algebra of posets and acyclic categories,” *Kyushu J. Math.* 67 (2013), 117–127, DOI: 10.2206/kyushujm.67.117; electronic release 2013-07-25. https://www.jstage.jst.go.jp/article/kyushujm/67/1/67_117/_article/-char/en
- I. Gargate and M. Gargate, “Involutions on incidence algebras of finite posets,” arXiv:1907.06805 (2019). https://arxiv.org/abs/1907.06805
- I. Gargate and M. Gargate, “\((k+1)\)-potent matrices in triangular matrix groups and incidence algebras of finite posets,” arXiv:2009.04243 (2020). https://arxiv.org/abs/2009.04243
- J. A. White, “Burnside chromatic polynomials of group-invariant graphs,” *Discuss. Math. Graph Theory*, DOI: 10.7151/dmgt.2385 (2020). https://doi.org/10.7151/dmgt.2385
