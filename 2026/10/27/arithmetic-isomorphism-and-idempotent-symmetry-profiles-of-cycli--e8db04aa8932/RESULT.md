# Arithmetic isomorphism and idempotent–symmetry profiles of cyclic evolution algebras

## Finding
Fix a prime power \(q\), a positive integer \(n\), and nonzero weights \(a_0,\ldots,a_{n-1}\in\mathbb F_q^\times\). Let \(E(\mathbf a)\) be the evolution algebra with natural basis \(e_0,\ldots,e_{n-1}\), all mixed products \(e_i e_j=0\) for distinct indices, and
\[
e_i^2=a_i e_{i+1\pmod n}.
\]
Write \(N=2^n-1\), \(g=\gcd(N,q-1)\), and \(G=\mathbb F_q^\times/(\mathbb F_q^\times)^N\), a cyclic group of odd order \(g\). Define its *cycle class*
\[
c(\mathbf a)=\left[a_0^{2^{n-1}}a_1^{2^{n-2}}\cdots a_{n-2}^{2}a_{n-1}\right]\in G.
\]
Let \(r_d\) be the multiplicative order of \(2\) modulo \(d\), with the convention \(r_1=1\). Then:

1. **Isomorphism criterion.** \(E(\mathbf a)\cong E(\mathbf b)\) over \(\mathbb F_q\) if and only if \(c(\mathbf b)=c(\mathbf a)^{2^j}\) for some \(0\le j<n\). Hence the total number of isomorphism classes is
\[
C(q,n)=\sum_{d\mid g}\frac{\varphi(d)}{r_d}
=\frac1n\sum_{j=0}^{n-1}\gcd(g,2^j-1).
\]
2. **Automorphism order.** If \(c(\mathbf a)\) has multiplicative order \(d\) in \(G\), then
\[
\left|\operatorname{Aut}_{\mathbb F_q}E(\mathbf a)\right|=\frac{gn}{r_d}.
\]
3. **Idempotents.** Counting zero, the number of solutions of \(x^2=x\) is \(1+g\) if \(c(\mathbf a)=1_G\), and exactly \(1\) otherwise.
4. **Uniform-weight joint law.** If the weights are independent and uniform on \(\mathbb F_q^\times\), the cycle class is uniform on \(G\), and the probability that its order equals \(d\mid g\) is \(\varphi(d)/g\). Therefore the preceding formulas give the exact joint law of idempotent count and automorphism-group order. Each isomorphism class associated to an order-\(d\) cycle class has probability \(r_d/g\) under this weighting.

For example, when \(q=7\) and \(n=2\), \(g=3\). One class has four idempotents and six automorphisms, with probability \(1/3\); the other has only zero as idempotent and three automorphisms, with probability \(2/3\).

## Assumptions and scope
All fields are finite and all cycle weights are nonzero. The dimension is any integer \(n\ge1\), including the one-loop case. Algebra isomorphisms and automorphisms are \(\mathbb F_q\)-linear and multiplicative, not required to preserve a chosen natural basis. Randomness refers to **uniform labeled nonzero structure coefficients**, not uniform isomorphism classes. All formulas hold in even and odd characteristic; no unproved genericity assumption is used.

## Proof
**Step 1 (every isomorphism is monomial).** The matrix of squares of the natural basis is a weighted permutation matrix and is invertible. For any algebra isomorphism, the images \(u_i\) of the basis satisfy \(u_i u_j=0\) for distinct \(i,j\). Writing their coefficient columns in the target natural basis, the coefficients of this product in the invertible square-basis matrix are the coordinatewise products of these columns, so they vanish coordinatewise. Thus distinct columns have disjoint supports. As there are \(n\) nonzero disjoint supports among \(n\) coordinate positions, every image has support one; the change-of-basis matrix is monomial. Its permutation must preserve the orientation of the directed \(n\)-cycle, hence is a cyclic shift.

**Step 2 (diagonal equivalence).** If \(f_i=t_i e_i\) with \(t_i\ne0\), then the transformed coefficient is \(a_i'=a_i t_i^2/t_{i+1}\). Multiplying with weights \(2^{n-1},2^{n-2},\ldots,1\), all intermediate factors cancel and the product changes by \(t_0^{2^n-1}\). Conversely, prescribed nonzero coefficients satisfying equality of cycle classes admit \(t_0\) solving the final power equation; recursively take \(t_{i+1}=a_i t_i^2/a_i'\). Its final consistency equation is exactly the class relation. Hence diagonal equivalence is equality in \(G\).

**Step 3 (rotations and classes).** Changing the initial cyclic index by one sends the representative \(P\) to \(P^2/a_0^{2^n-1}\) and therefore sends its class to \(c^2\). Because \(g\mid2^n-1\), the squaring action has order dividing \(n\) on \(G\). The orbit criterion follows. Elements of order \(d\) have orbit length \(r_d\); there are \(\varphi(d)\) such elements. This yields the divisor formula, while Burnside's lemma gives the second count because the fixed subgroup of the \(j\)-fold squaring map has order \(\gcd(g,2^j-1)\).

**Step 4 (automorphisms).** With rotation zero, a diagonal automorphism satisfies \(t_{i+1}=t_i^2\) and \(t_0^{2^n-1}=1\). The multiplicative group of \(\mathbb F_q\) has exactly \(g\) such initial scalars, giving \(g\) diagonal automorphisms. A rotation by \(j\) has a lift to a weighted-cycle automorphism exactly when \(c^{2^j}=c\). If \(c\) has order \(d\), this holds for precisely \(n/r_d\) shifts. Each lifted shift forms a coset of the diagonal automorphism subgroup, so the total order is \(gn/r_d\).

**Step 5 (idempotents).** Write \(x=\sum_i x_i e_i\). The equation \(x^2=x\) reads \(x_{i+1}=a_i x_i^2\) cyclically. If one coordinate is zero all are zero. Otherwise the coordinates are fixed by \(x_0\in\mathbb F_q^\times\), and the cycle condition is \(x_0^{2^n-1}=P^{-1}\), where \(P=a_0^{2^{n-1}}\cdots a_{n-1}\). A power equation in the cyclic group \(\mathbb F_q^\times\) has \(g\) solutions if \(P\) is an \(N\)-th power and zero otherwise. This is the known weighted-permutation idempotent mechanism; its inclusion is necessary for the joint distribution, not a claim of discovery.

**Step 6 (uniformity).** In \(P\), the last weight \(a_{n-1}\) occurs to exponent one. Conditional on all preceding weights, this makes \(P\) uniform on \(\mathbb F_q^\times\). Its quotient class is therefore uniform in \(G\). Exactly \(\varphi(d)\) of the \(g\) classes have order \(d\), and each squaring orbit of length \(r_d\) corresponds to one algebra isomorphism class. All formulas follow.

## Verification
A standalone standard-library checker (`verify.py`) constructs prime fields and the binary extensions \(\mathbb F_4\) and \(\mathbb F_8\); it directly evaluates algebra squares for every vector, independently enumerates monomial automorphisms, and compares exact structure-parameter isomorphism searches with the predicted squaring orbits. Exhaustive coefficient tests were run for \(q\in\{2,3,4,5,7,8,11\}\) and \(1\le n\le3\), as well as \(n=4\) and \(q\in\{2,3,4,5,7\}\). All \(26\) tested configurations, covering \(3557\) weighted coefficient tuples, passed. Run `python3 verify.py`. This finite verification is not a proof for all dimensions and fields.

## Relationship to prior work
Narkuziyev's work on evolution algebras attached to permutations already supplies equations for idempotents on weighted permutation cycles. Elduque and Labra prove the graph–monomial automorphism framework and describe diagonal automorphism groups of connected cycles, including small-dimensional examples. Wei and Zou's general theory characterizes perfect evolution-algebra isomorphism classes by group orbits. These established ingredients are used and acknowledged. The present claim concerns their **explicit finite-field specialization simultaneously yielding, for every cycle length and field size, a closed divisor formula for isomorphism-class number, each class's rational automorphism-group order, and its weighted joint distribution with idempotent count**. None of the inspected available statements explicitly supplies this coupled arithmetic profile. The full 2020 Narkuziyev preprint and the full 2023 Wei–Zou preprint were not accessible in this examination; an equivalent or directly implied enumeration there remains a priority risk.

## Limitations
The classification applies only to invertible single directed-cycle evolution algebras, not arbitrary multi-cycle or nonmonomial evolution algebras. The idempotent power equation is a known special case and not independently new. The formulas do not classify automorphism groups abstractly, only their orders. Finite experimental checks do not prove the theorem. The algebraic proof and originality comparison have received self-review only, not independent audit. Relevant inaccessible full texts could reduce or eliminate priority.

## References
- B. A. Narkuziyev, *Some remarks on evolution algebras corresponding to permutations*, arXiv:2005.05793 (first public 2020-05-09), DOI:10.1142/S0219498822501122.
- A. Elduque and A. Labra, *Evolution algebras, automorphisms, and graphs*, arXiv:1902.02191 (2019), especially Sections 2–3.
- B. A. Narkuziyev, *On absolute nilpotent and idempotent elements of an evolution algebra corresponding to permutations* (2014), Theorem 2 and its proof.
- Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368 (2023).
