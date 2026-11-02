# A non-split order-63 automorphism group from a weighted evolution six-cycle

## Finding
Let \(q\) be a prime power satisfying \(21\mid(q-1)\) and \(9\nmid(q-1)\). Choose a primitive cube root of unity \(\zeta\in\mathbb F_q\). Define the six-dimensional, commutative (generally nonassociative) evolution algebra \(E\) over \(\mathbb F_q\) on basis \(e_0,\ldots,e_5\) by \(e_i e_j=0\) for \(i\ne j\), and
\[
e_0^2=\zeta e_1,\qquad e_i^2=e_{i+1}\ (1\le i\le4),\qquad e_5^2=e_0.
\]
Its structure matrix is invertible, and its support digraph is a single directed six-cycle. Its complete group of \(\mathbb F_q\)-linear algebra automorphisms is the nonabelian group
\[
\operatorname{Aut}_{\mathbb F_q}(E)\cong C_7\rtimes C_9,
\]
where a generator of \(C_9\) acts on \(C_7\) by an automorphism of order three (for example, multiplication by four on exponent labels). More precisely, the natural map sending an automorphism to its permutation of natural basis lines gives a **non-split** exact sequence
\[
1\longrightarrow C_{21}\longrightarrow\operatorname{Aut}_{\mathbb F_q}(E)\longrightarrow C_3\longrightarrow1.
\]
The diagonal subgroup has order \(21\); the image in the automorphism group of the support digraph consists exactly of rotations by \(0,2,4\) places, with \(21\) lifts of each. Every automorphism above rotation by two or four has order nine. The complete element-order distribution is: one identity, two elements of order three, six of order seven, forty-two of order nine, and twelve of order twenty-one.

In particular the construction applies over \(\mathbb F_{43}\), where \(\zeta=6\) is a primitive cube root of unity. It gives a family over infinitely many prime fields (e.g. primes congruent to \(43\) modulo \(63\), by Dirichlet's theorem).

## Assumptions and scope
All algebra automorphisms are linear over the specified coefficient field (field automorphisms are not included). The field cardinality \(q\) is any prime power satisfying the two displayed divisibility assumptions; the cube root \(\zeta\) has multiplicative order exactly three. A natural basis is one in which products of distinct basis elements vanish. A diagonal automorphism fixes each natural basis line, while a rotation of the six-cycle maps \(e_i\) into the line of \(e_{i+r}\), with indices taken modulo six. Group splitting means existence of a group-homomorphic section of the displayed quotient map; it is not the assertion that the underlying abstract group is indecomposable.

## Proof
**1. All automorphisms are monomial, with cyclic permutations.** Write \(f(e_i)=\sum_j a_{ji}e_j\). As \(e_i e_k=0\) for \(i\ne k\),
\[
0=f(e_i)f(e_k)=\sum_j a_{ji}a_{jk}w_j e_{j+1},
\]
where \(w_0=\zeta\) and \(w_i=1\) otherwise. Because every \(w_j\) is nonzero and the six vectors \(e_{j+1}\) form a basis, each row of the invertible coefficient matrix has at most one nonzero entry. Consequently exactly one entry in every row and column is nonzero: \(f(e_i)=t_i e_{\sigma(i)}\), with \(t_i\ne0\). Multiplicativity forces \(\sigma(i+1)=\sigma(i)+1\) modulo six; hence \(\sigma(i)=i+r\), a rotation.

**2. Automorphism equations and the diagonal kernel.** Comparing \(f(e_i^2)\) with \(f(e_i)^2\) gives the necessary and sufficient equations
\[
t_{i+1}=t_i^2\frac{w_{i+r}}{w_i},\qquad i\in\mathbb Z/6\mathbb Z.
\]
For \(r=0\), these are \(t_i=t_0^{2^i}\), with consistency \(t_0^{63}=1\). The finite-field multiplicative group is cyclic, and
\[
\gcd(q-1,63)=21.
\]
Indeed \(63=7\cdot9\), while \(21\mid(q-1)\) and \(9\nmid(q-1)\). Thus the diagonal kernel \(D\) is exactly the cyclic group of \(21\) elements parametrized by \(t_0\in\mu_{21}(\mathbb F_q)\).

**3. Rotations that lift.** For \(r=2\), iterating the equations produces
\[
(t_0,t_1,t_2,t_3,t_4,t_5)
=(t,\ t^2\zeta^{-1},\ t^4\zeta^{-2},\ t^8\zeta^{-4},\ t^{16}\zeta^{-8},\ t^{32}),
\]
and consistency is exactly \(t^{63}=1\). Therefore rotation by two has \(21\) lifts; for example \(t=1\) yields \((1,\zeta^2,\zeta,\zeta^2,\zeta,1)\). Its square projects to rotation by four, which consequently also has \(21\) lifts.

For \(r=1\), the same recursion gives \(t_1=t^2\zeta^{-1},\ldots,t_5=t^{32}\zeta^{-16}\). Its final consistency equation is \(t^{63}=\zeta\). This equation has no solution in \(\mathbb F_q^\times\): since the highest power of three dividing \(q-1\) is exactly three, the image of the cube map, hence also the image of the sixty-third-power map, has order prime to three, whereas \(\zeta\) has order three. The rotation image is a subgroup of \(C_6\); it contains rotation by two and excludes rotation by one, so it is exactly \(\langle2\rangle\cong C_3\). Hence the automorphism group has order \(21\cdot3=63\).

**4. A forced cube and non-splitting.** Let \(g\) be *any* lift of rotation by two, determined by \(t\in\mu_{21}\) as in Step 3. Applying \(g\) three times to \(e_0\) multiplies it by
\[
t_0t_2t_4=t^{21}\zeta^{-10}=\zeta^{-1}\ne1.
\]
Thus every such lift has cube equal to a nonidentity element of \(D\) of order three, and consequently has order nine. An order-three element projecting to rotation by four would square to an order-three lift of rotation by two, which is impossible. Therefore no element of order three projects to a generator of the quotient \(C_3\); a section does not exist.

**5. Abstract group and order spectrum.** Let \(N\) be the unique order-seven subgroup of the cyclic group \(D\), and choose a lift \(g\) of rotation by two. Then \(|\langle g\rangle|=9\), its intersection with \(N\) is trivial, and \(N\langle g\rangle\) has \(7\cdot9=63\) elements. Thus the full group is \(N\rtimes\langle g\rangle\). The conjugation action of a rotation-by-two lift on a diagonal automorphism is exponentiation by the inverse of four (modulo \(21\)): if \(d_t(e_i)=t^{2^i}e_i\), then \(g d_tg^{-1}=d_{t^{16}}\), because \(4\cdot16\equiv1\pmod{21}\). On \(N\cong C_7\) this is a nontrivial automorphism of order three. Replacing \(g\) by \(g^{-1}\) expresses the action by four, proving the claimed isomorphism. Inside \(D\cong C_{21}\), the orders occur with multiplicities \(1,2,6,12\) for orders \(1,3,7,21\), respectively. The other \(42\) elements project nontrivially and all have order nine, giving the stated complete spectrum.

## Verification
The standalone file `verify.py` directly enumerates every monomial automorphism for three prime fields \(\mathbb F_{43},\mathbb F_{211},\mathbb F_{337}\). For each field it checks all six possible rotations and all nonzero initial coefficients, verifies every multiplication relation, checks closure under composition for the full set of \(63\) automorphisms, computes the complete order spectrum, and verifies that every lift of rotation by two has a nontrivial cube. It independently checks that replacing \(\zeta\) by one permits all six rotations. Run `python verify.py` using Python 3.8 or newer. The printed terminal line is `VERIFY_OK`. These finite checks corroborate but do not replace the general argument for every admissible prime power.

## Relationship to prior work
The monomiality of automorphisms of perfect evolution algebras, their description via graph symmetries and diagonal kernels, and general finite-field classification machinery are established facts. Wei and Zou (2023) classify arbitrary idempotent evolution algebras by monomial orbits and derive global counting results; that general orbit principle is used here, but it does not provide the present explicit nonabelian non-split extension for this fixed weighted six-cycle. Costoya, Muñoz, Tocino and Viruel (2023) prove general group-realization results, which do not prescribe this support graph and extension. Costoya, Mayorga and Viruel (2025; preprint 2024) study realizable permutation representations, not this extension. Kaygorodov, Martín González and Viruel (2026, Proposition 21) give a distinct six-dimensional non-split example with automorphism group \(C_9\) and a graph with extra edges; their example does not imply the nonabelian group \(C_7\rtimes C_9\) on a single weighted directed cycle considered here. Their Question 33 makes determining when the natural automorphism extension splits a specific mathematical problem. No claim is made that non-split extensions were previously unknown.

## Limitations
The family requires \(21\mid(q-1)\) and \(9\nmid(q-1)\); it does not classify the splitting behavior for all weighted cycles or arbitrary fields. The diagonal kernel and automorphism group describe rational points over \(\mathbb F_q\), not the full automorphism group scheme. The general algebraic proof is self-contained but the originality comparison is restricted to the cited accessible literature and searches; another unlocated classification may exist. The computations cover three prime fields only. No independent mathematical validation has been performed.

## References
1. S. Sriwongsa and Y. M. Zou, *On Automorphism Groups of Idempotent Evolution Algebras*, Linear Algebra Appl. 641 (2022), 143–155, preprint arXiv:2202.01333 (first posted 2022-02-02).
2. Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, Linear Algebra Appl. 675 (2023), 142–178, arXiv:2310.12368 (preprint posted 2023-10-18), especially Theorem 1.1 and Corollary 1.1.
3. C. Costoya, V. Muñoz, A. Tocino, and A. Viruel, *Automorphism groups of Cayley evolution algebras*, Rev. R. Acad. Cienc. Exactas Fís. Nat. Ser. A Mat. 117 (2023), article 82, DOI:10.1007/s13398-023-01414-w.
4. C. Costoya, P. Mayorga, and A. Viruel, *Permutation Representations and Automorphisms of Evolution Algebras*, Mediterr. J. Math. 22 (2025), article 149; arXiv:2401.05924 (first posted 2024-01-11).
5. I. Kaygorodov, C. Martín González, and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248 (2026), Proposition 21 and Question 33.
