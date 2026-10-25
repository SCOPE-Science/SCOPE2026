# Frobenius splitting and automorphism census in the squarefree cubic stratum of three-dimensional commutative algebras

## Finding
Let \(K=\mathbb F_q\) have characteristic greater than three. Among three-dimensional **unital commutative, not necessarily associative** \(K\)-algebras \(A\), consider those for which the binary cubic associated to the canonical trace-zero plane \(W=\ker(x\mapsto\operatorname{tr}L_x)\) has nonzero discriminant. There are **exactly**
\[
q^3+q^2+q
\]
\(K\)-algebra isomorphism classes in this stratum. Their full \(K\)-linear automorphism groups, including multiplicities of isomorphism classes, are
\[
\begin{array}{c|rrrr}
\operatorname{Aut}_K(A)&1&C_2&C_3&S_3\\\hline
\#\text{classes}&q^2(q-1)&2q^2-q&q&q.
\end{array}
\]
In particular, precisely \(2q^2+q\) classes have nontrivial automorphisms. The theorem holds for **every prime power** \(q\) of characteristic greater than three, not merely for prime fields.

More finely, the three distinct arithmetic types of the trace cubic (three rational roots; one rational root and a quadratic pair; irreducible cubic) have, respectively, \((q^3+3q^2+2q)/6\), \((q^3+q^2)/2\), and \((q^3+2q)/3\) algebra classes. The automorphism counts by type are determined in the proof.

## Assumptions and scope
Fix a finite field \(K=\mathbb F_q\) with \(\operatorname{char}K=p>3\). A \(K\)-algebra means a \(K\)-vector space with a bilinear multiplication; associativity and power-associativity are **not** assumed. A unital commutative three-dimensional algebra has a unique unit \(1\). For \(a\in A\), write \(L_a(x)=ax\), \(\tau(a)=\operatorname{tr}_K(L_a)\), and \(W=\ker\tau\). Since \(\tau(1)=3\ne0\), we have \(A=K1\oplus W\) with \(\dim_KW=2\).

For \(u,v\in W\), decompose their product uniquely as
\[
uv=\varphi(u,v)1+\mu(u,v),\qquad \varphi:W\times W\to K,\quad \mu:W\times W\to W,
\]
where both maps are symmetric bilinear and \(\operatorname{tr}(\mu(u,-))=0\) for every \(u\in W\). Choose any nonzero alternating form \(\omega\) on \(W\), and define
\[
F_{\mu,\omega}(x)=\omega(\mu(x,x),x).
\]
This is a homogeneous binary cubic. Replacing \(\omega\) scales the cubic by a nonzero scalar, so whether it has nonzero discriminant is well defined, independently of the choice. The theorem concerns exactly those algebras with \(\operatorname{disc}(F_{\mu,\omega})\ne0\).

## Proof
**1. Canonical trace kernel and cubic correspondence.** In the decomposition \(K1\oplus W\), the first diagonal entry of \(L_u\), for \(u\in W\), is zero, and the remaining diagonal block is \(\mu(u,-)\). Thus \(\tau(u)=\operatorname{tr}\mu(u,-)=0\). Conversely, every pair consisting of a traceless commutative multiplication \(\mu\) on a fixed two-plane and a symmetric scalar form \(\varphi\) defines a unital commutative algebra having precisely that canonical plane. Since every isomorphism fixes the unit and preserves traces, isomorphisms correspond exactly to changes of basis of \(W\) acting simultaneously on \(\mu\) and \(\varphi\).

The trilinear map \(T(u,v,w)=\omega(\mu(u,v),w)\) is symmetric in its first two entries. The two-dimensional symplectic identity
\[
\omega(Mv,w)-\omega(Mw,v)=\operatorname{tr}(M)\omega(v,w)
\]
shows that \(T\) is totally symmetric precisely when \(\mu\) is traceless. Because \(2\) and \(3\) are invertible in \(K\), polarization identifies totally symmetric trilinear maps with binary cubics \(F(x)=T(x,x,x)\). Explicitly, relative to a symplectic basis \((u,v)\), writing
\[
F(Xu+Yv)=\alpha X^3+\beta X^2Y+\gamma XY^2+\delta Y^3
\]
gives the uniquely corresponding multiplication
\[
\mu(u,u)=\tfrac{\beta}{3}u-\alpha v,\quad
\mu(u,v)=\tfrac{\gamma}{3}u-\tfrac{\beta}{3}v,\quad
\mu(v,v)=\delta u-\tfrac{\gamma}{3}v.
\]
Thus algebras in question are pairs \((F,\varphi)\), with \(F\) a squarefree binary cubic and \(\varphi\in\operatorname{Sym}^2(W^*)\), modulo a simultaneous \(\mathrm{GL}_2(K)\)-action. With the convention \(\mu^g(x,y)=g^{-1}\mu(gx,gy)\), the cubic action is
\[
F^g(x)=\det(g)^{-1}F(gx).
\]

**2. Three rational cubic orbits.** The geometric zero divisor of a squarefree cubic is an unordered triple of distinct points of \(\mathbf P^1(\overline K)\), stable under Frobenius. Frobenius permutes the triple with cycle type \((1,1,1)\), \((1,2)\), or \((3)\), and each occurs (split cubics, a product of one linear and one irreducible quadratic factor, and irreducible cubics). Two such triples with the same cycle type are related by a unique projective transformation carrying a chosen Frobenius-compatible ordering to another: \(\mathrm{PGL}_2(\overline K)\) acts sharply three-transitively on ordered distinct triples. The uniqueness makes the transformation Frobenius-fixed, hence defined over \(K\).

To pass from projective triples to the actual twisted \(\mathrm{GL}_2(K)\)-action on cubic forms, take a lift \(g\) of the projective transformation. If \(F(gx)=\lambda F(x)\), then the uniquely determined scalar \(c=\det(g)/\lambda\) makes \(cg\) fix \(F\) under the twisted action, because \(F^{cg}=c\,F^g\). The same argument transports one cubic to another with the same root triple, after adjusting a nonzero scalar. Thus there are precisely three twisted \(\mathrm{GL}_2(K)\)-orbits of squarefree binary cubics. Their stabilizers are the groups of Frobenius-compatible permutations of the root triple, namely \(S_3\), \(C_2\), and \(C_3\), in this order. No nonidentity scalar fixes a cubic, so these are **exactly** the automorphism groups of the corresponding traceless multiplications, not just projective quotients.

**3. Fixed spaces on scalar forms.** The remaining free parameter \(\varphi\) ranges over the three-dimensional space \(B=\operatorname{Sym}^2(W^*)\). Its action is the change-of-basis action of the relevant cubic stabilizer. A transposition acts on \(W\) with eigenvalues \(1,-1\), hence fixes a two-dimensional subspace of \(B\). A three-cycle acts over an algebraic closure with eigenvalues \(\zeta,\zeta^2\) for a primitive cube root \(\zeta\), hence fixes a one-dimensional subspace of \(B\). These fixed-space dimensions hold over \(K\) even when \(\zeta\notin K\). For \(S_3\), the line fixed by a three-cycle is also fixed by every transposition (equivalently, \(B\cong\mathbf1\oplus\mathrm{Std}\) as an \(S_3\)-module in characteristic greater than three). Consequently the full \(S_3\)-invariant subspace has dimension one. Distinct transposition-fixed planes intersect in that same line.

For a split cubic, \(B\) therefore contains \(q\) points with stabilizer \(S_3\), \(3(q^2-q)\) points with stabilizer a unique \(C_2\), and \(q^3-3q^2+2q\) points with trivial stabilizer. Dividing by the respective orbit lengths \(1,3,6\), the algebra-class counts for this cubic type are
\[
\begin{array}{c|rrr} \operatorname{Aut}_K(A)&1&C_2&S_3\\\hline
\#\text{classes}&\frac{q(q-1)(q-2)}6&q(q-1)&q.\end{array}
\]
For a \((1,2)\)-type cubic, \(C_2\) fixes \(q^2\) scalar forms, yielding \(q^2\) classes with automorphism group \(C_2\) and \((q^3-q^2)/2\) with trivial group. For an irreducible cubic, \(C_3\) fixes \(q\) scalar forms, yielding \(q\) classes with automorphism group \(C_3\) and \((q^3-q)/3\) with trivial group.

**4. Summation.** Summing over the three disjoint Frobenius types gives
\[
\begin{aligned}
\#\{\operatorname{Aut}=1\}&=\frac{q(q-1)(q-2)}6+\frac{q^3-q^2}2+\frac{q^3-q}3=q^2(q-1),\\
\#\{\operatorname{Aut}\cong C_2\}&=q(q-1)+q^2=2q^2-q,\\
\#\{\operatorname{Aut}\cong C_3\}&=q,\\
\#\{\operatorname{Aut}\cong S_3\}&=q.
\end{aligned}
\]
Their sum is \(q^3+q^2+q\), as claimed. Each automorphism group here is the full automorphism group of the original unital algebra, because every automorphism fixes \(1\), stabilizes the canonical trace kernel, and must stabilize both \(\mu\) and \(\varphi\). \(\square\)

## Verification
The accompanying standard-library Python checker `verify.py` independently enumerates \(\mathrm{GL}_2(\mathbb F_p)\), the twisted cubic orbit of one representative of each of the three Frobenius types, each stabilizer, and **every** symmetric form for each type for \(p=5,7,11\). It verifies disjointness and completeness of the three cubic orbits, computes orbit stabilizers of symmetric forms, and checks the cubic-to-multiplication covariance directly on basis pairs. Its output ends in `VERIFY_OK`.

The respective total algebra-class counts are \(155\), \(399\), and \(1463\), with automorphism-size distributions \((100,45,5,5)\), \((294,91,7,7)\), and \((1210,231,11,11)\) in the order \((1,2,3,6)\). This is exhaustive for the indicated **prime fields**, not a proof by finite testing for all fields. The argument above establishes the result uniformly for every finite field of characteristic greater than three.

## Relationship to prior work
Eraliyeva and Kaygorodov's October 2026 complex classification introduces the canonical trace-zero complement and identifies its traceless multiplication with binary cubic data, then classifies symmetric scalar forms over \(\mathbb C\). This structural framework is credited rather than claimed here. It does **not** enumerate \(\mathbb F_q\)-isomorphism classes, distinguish the three Frobenius splitting types, or derive their exact automorphism distributions. Algebraically closed classification alone does not identify non-isomorphic finite-field forms: Galois descent and finite rational orbit counts are essential. The present statement is the arithmetic finite-field classification and census of the open squarefree-cubic stratum, not a new complex classification and not a classification of the discriminant-zero boundary.

Related work on three-dimensional simple unital commutative algebras over algebraically closed fields studies isotopy and nil-elements rather than the finite-field isomorphism-class census. Finite-field actions on irreducible polynomials concern the cubic coordinate alone; the additional symmetric-form orbit problem is indispensable here.

## Limitations
The theorem excludes characteristics two and three and excludes trace cubics of zero discriminant. It counts \(K\)-linear algebra isomorphism classes, not based multiplication tables and not equivalence under semilinear field automorphisms. Associativity is not imposed; associative examples are included but are not separately classified. The finite verification tests prime fields only. Unindexed literature on finite-field forms and invariant theory could contain an equivalent count; the present literature comparison is not an independent novelty certification. Independent mathematical audit has not been performed.

## References
1. M. Eraliyeva and I. Kaygorodov, *Classification of 3-dimensional unital commutative algebras*, arXiv:2610.18689v1 (first submitted 13 October 2026), especially Lemma 1, Lemma 3, Proposition 10 and Theorem 11; https://arxiv.org/html/2610.18689v1.
2. V. Glizburg and S. Pchelintsev, *On commutative isotopes of Jordan algebra of a symmetric bilinear nondegenerate form on a two-dimensional vector space*, arXiv:2504.00868 (2025); https://arxiv.org/html/2504.00868.
3. L. da Silva Reis, *The action of GL2(Fq) on irreducible polynomials over Fq, revisited*, Journal of Symbolic Computation (2018), institutional repository abstract at https://repositorio.ufmg.br/items/093e3d93-4f68-4240-bb1c-8cd6f6f78214.
