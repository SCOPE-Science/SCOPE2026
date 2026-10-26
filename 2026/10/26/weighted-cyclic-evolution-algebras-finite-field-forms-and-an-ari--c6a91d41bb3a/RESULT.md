# Weighted cyclic evolution algebras: finite-field forms and an arithmetic splitting criterion

## Finding
Let \(K=\mathbb F_q\), where \(q\) is any prime power, and let \(n\ge2\). Consider the \(n\)-dimensional evolution algebras \(E_w\) with a natural basis \(e_0,\dots,e_{n-1}\), mixed products zero, and
\[
e_i^2=w_i e_{i+1\pmod n},\qquad w_i\in K^\times.
\]
Fix a generator \(\gamma\) of \(K^\times\); write \(w_i=\gamma^{A_i}\), with \(A_i\) modulo \(Q=q-1\). Define
\[
N=2^n-1,\quad g=\gcd(Q,N),\quad
 a(w)=\sum_{i=0}^{n-1}2^{n-1-i}A_i\pmod g.
\]
Then:

1. Two such algebras are isomorphic over \(K\) exactly when their invariants lie in the same orbit under multiplication by \(2\) on \(\mathbb Z/g\mathbb Z\). Every class has a representative with all weights \(1\) except \(w_{n-1}=\gamma^a\).
2. For each divisor \(d\mid g\), set \(h_d=\operatorname{ord}_d(2)\), with \(h_1=1\). Exactly \(\varphi(d)/h_d\) isomorphism classes have invariants of additive order \(d\). Thus the total number of classes is \(\sum_{d\mid g}\varphi(d)/h_d\).
3. For any such class the full \(K\)-linear automorphism group fits into
\[
1\longrightarrow C_g\longrightarrow \operatorname{Aut}_K(E_w)
\longrightarrow C_{n/h_d}\longrightarrow1,
\]
so its order is \(gn/h_d\). The quotient is the actual image of the automorphism group among rotations of the directed cycle, not necessarily the entire graph automorphism group.
4. This exact sequence **splits if and only if**
\[
\boxed{\gcd\!\left(q-1,\frac{2^n-1}{2^{h_d}-1}\right)
\ \bigm|\ \frac{g}{d}.}
\]
For the equivalent representative-dependent form, splitting is equivalent to divisibility of an integer representative \(a\) by \(\gcd(Q,(2^n-1)/(2^{h_d}-1))\). The criterion is independent of the chosen invariant within its orbit.

The algebras are perfect and simple because their weighted permutation structure matrices are invertible and their directed graphs are strongly connected.

## Assumptions and scope
All linear isomorphisms and automorphisms fix the finite field \(K\) pointwise; neither semilinear maps nor algebraic-group-scheme points over extension fields are included. The exponent group is \(\mathbb Z/Q\mathbb Z\). All multiplicative weights are nonzero. The only external structural input is monomiality of isomorphisms between perfect evolution algebras, which can also be checked directly because images of distinct natural-basis elements multiply to zero and their squares span the target. A permutation preserving the oriented single-cycle graph is necessarily a cyclic rotation.

For \(d=1\), interpret \(\operatorname{ord}_1(2)=1\). Since \(d\mid(2^n-1)\), the order \(h_d\) divides \(n\). In all formulas the quotient \((2^n-1)/(2^{h_d}-1)\) is an integer. The case \(g=1\) is included: there is one class with automorphism group \(C_n\), and the sequence splits.

## Proof
**Diagonal normalization and invariant.** A diagonal basis change \(e'_i=\gamma^{v_i}e_i\) replaces \(A_i\) by \(A'_i=A_i+2v_i-v_{i+1}\), with indices modulo \(n\) and all exponents modulo \(Q\). In the weighted sum defining \(a\), all \(v_i\) contributions cancel except \((2^n-1)v_0\). Thus \(a\pmod g\) is unchanged. Conversely, the equations \(A'_i=0\) for \(0\le i\le n-2\) determine \(v_1,\dots,v_{n-1}\) from an arbitrary \(v_0\). The remaining exponent then changes by an arbitrary multiple of \(N\) modulo \(Q\), giving precisely the residue class \(a\pmod g\). This proves complete diagonal classification and the canonical form.

**Rotations and isomorphisms.** In canonical coordinates, let the source and target last-edge exponents be \(a,b\). An isomorphism with permutation part the rotation by \(k\), written \(f(e_i)=\gamma^{u_i}e'_{i+k}\), obeys
\[
u_{i+1}=2u_i+B_{i+k}-A_i\pmod Q.
\]
Iterating around the cycle yields
\[
Nu_0=a-2^k b\pmod Q.
\]
The modular equation is solvable precisely when \(g\mid a-2^k b\), proving assertion 1. The doubling action partitions the \(\varphi(d)\) elements of additive order \(d\) into cycles each of length \(h_d\); this proves assertion 2.

**Exact automorphism sequence.** For an automorphism, \(a=b\), so rotation \(k\) lifts exactly when \(g\mid(2^k-1)a\). Put \(d=g/\gcd(g,a)\). This is equivalent to \(d\mid2^k-1\), hence the image of the permutation homomorphism consists of rotations by multiples of \(h=h_d\), and has order \(m=n/h\). Over a fixed allowable rotation, the congruence in the preceding paragraph has exactly \(g\) solutions \(u_0\pmod Q\), determining all other \(u_i\). In particular the kernel is the cyclic group of \(g\) diagonal maps \(u_i=2^i u_0\) with \(Nu_0=0\pmod Q\). This proves assertion 3.

**Splitting.** If \(h=n\), the quotient is trivial and the criterion holds because the relevant ratio equals \(1\). Suppose \(h<n\), put \(m=n/h\ge2\) and \(S=(2^n-1)/(2^h-1)\). An automorphism lifting the rotation by \(h\) is specified by \(u_0\) subject to
\[
Nu_0=a(1-2^h)\pmod Q.
\]
For the canonical representative \(A_i=0\) except \(A_{n-1}=a\), its intermediate exponents satisfy \(u_{jh}=2^{jh}u_0\) for \(0\le j\le m-2\), and \(u_{(m-1)h}=2^{(m-1)h}u_0+a\). Applying the lift \(m\) times gives a diagonal map whose coefficient on \(e_0\) is \(\gamma^{Su_0+a}\). A diagonal map is the identity exactly when its first coefficient is \(1\). Thus an order-\(m\) lift of the quotient generator exists if and only if
\[
Su_0\equiv-a\pmod Q.
\]
Any solution to this congruence automatically satisfies the preceding lift congruence after multiplying by \(2^h-1\). Existence is therefore equivalent to \(\gcd(Q,S)\mid a\). Finally \(\gcd(Q,S)\mid g\), and \(a\) has additive order \(d\) modulo \(g\); prime-adic valuations show that \(\gcd(Q,S)\mid a\) is equivalent to \(\gcd(Q,S)\mid g/d\). A section of a cyclic quotient exists exactly when its generator has a lift of the same order, completing the proof.

## Verification
The accompanying standalone `verify_cycle_q.py` uses exponent arithmetic in \(\mathbb Z/(q-1)\mathbb Z\). It independently enumerates all weighted tuples for 42 small parameter pairs, checks the isomorphism-class orbits, checks every rotation's exact number of lifts for each canonical invariant, and checks the splitting congruence. Six larger modulus/dimension pairs are also checked by exhaustive congruence sweeps. It prints `VERIFY_OK` on success. The computation is finite corroboration, not the proof for all fields and dimensions.

Two discriminating examples: for \(q=7,n=6\), the nonzero class in \(\mathbb Z/3\mathbb Z\) has \(h=2\), a cyclic diagonal kernel of order \(3\), a quotient of order \(3\), and a nonsplit extension of order \(9\); for \(q=19,n=6\), the class of additive order \(3\) modulo \(9\) has \(h=2\), an order-\(9\) diagonal kernel, an order-\(3\) quotient, and a split extension of order \(27\). This distinction does not follow solely from graph rotation symmetry.

## Relationship to prior work
The monomiality theorem and automorphism exact sequence are due to Elduque and Labra (arXiv:1902.02191). Their Example 3.5 gives an earlier non-splitting phenomenon in the two-dimensional cyclic graph; this work does not claim that non-splitting itself is new. Wei and Zou (arXiv:2310.12368) establish the general monomial-orbit framework for classifying perfect evolution algebras and derive aggregate finite-field class counts through dimension four. The present result supplies explicit arithmetic classification, exact automorphism orders, and a split/nonsplit criterion for every cycle length and every finite field. Cabrera Casado et al. (arXiv:2505.14584) give a general theory of diagonal and monomial automorphisms, including algebras satisfying the 2LI condition; potential implicit coverage of the specialized formulas remains a literature risk because its complete manuscript was not accessible during this analysis. The October 2026 survey (arXiv:2610.22248v1) poses the splitting question explicitly as Question 33 and gives a different non-split example. The \(\mathbb F_4\) subcase of the present classification has also been worked out separately; the new scope here is the arithmetic dependence on arbitrary \(q\), particularly the class-by-class splitting formula.

## Limitations
Only one oriented cycle with nonzero edge weights is treated; disconnected or branching graphs are outside the theorem. Automorphism groups refer to finite-field rational points, not group schemes over all extensions. The result does not classify all perfect evolution algebras. Its originality against the full 2LI literature requires subsequent independent scholarly comparison, especially where general descriptions may imply individual special cases.

## References
- Ivan Kaygorodov, Cándido Martín González, Antonio Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first public 2026-10-15), especially Theorem 4 and Question 33.
- Alberto Elduque, Alicia Labra, *Evolution algebras, automorphisms, and graphs*, arXiv:1902.02191, especially Theorem 3.2 and Example 3.5.
- Yangjiang Wei, Yi Ming Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368, especially Theorem 1.1 and the orbit-counting sections.
- Yolanda Cabrera Casado et al., *Solenoids in automorphism groups of evolution algebras*, arXiv:2505.14584 (abstract accessible; full text inaccessible in this comparison).
