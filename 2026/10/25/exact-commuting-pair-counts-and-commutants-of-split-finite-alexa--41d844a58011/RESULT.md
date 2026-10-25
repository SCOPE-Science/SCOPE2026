# Exact commuting-pair counts and commutants of split finite Alexander quandle algebras

## Finding
Let \(A\) be a finite abelian group, \(\varphi\in\operatorname{Aut}(A)\), and assume that \(1-\varphi\) is also an automorphism. Let \(k=\mathbb F_q\) be a finite field containing a primitive root of unity of order \(\exp(A)\). Let \(E=k[\operatorname{Alex}(A,\varphi)]\) be the nonassociative quandle algebra, where the basis elements multiply by
\[
e_x e_y=e_{\varphi(x)+(1-\varphi)(y)}.
\]
Write \(N=|A|\). On the character group \(\widehat A\), let \(T\) act by precomposition with \(\varphi^{-1}(1-\varphi)\), and let \(c_m\) denote the number of cycles of length \(m\) of \(T\). Set \(U_0(q)=2\), \(U_1(q)=q\), and, for \(m\ge2\),
\[
U_m(q)=qU_{m-1}(q)+q(q-1)U_{m-2}(q),\qquad T_m(q)=U_m(q)+q(q-1)^m.
\]
Then **the exact number of ordered commuting pairs** is
\[
\boxed{\#\{(u,v)\in E^2:uv=vu\}=\prod_{m\ge1}T_m(q)^{c_m}.}
\]
In particular, the probability that two uniformly chosen elements commute equals this product divided by \(q^{2N}\). The commuting center
\[
Z_{\mathrm{comm}}(E)=\{u\in E:uv=vu\ \text{for every }v\in E\}
\]
has dimension \(\boxed{\dim_k Z_{\mathrm{comm}}(E)=|\ker(1-2\varphi)|}\). Moreover, the following **complete centralizer-dimension rule** holds. For \(u\in E\), write its Fourier coefficients along each \(T\)-cycle as a cyclic word \(a_0,\ldots,a_{m-1}\) over \(k\). Its commuting centralizer \(C_E(u)=\{v:uv=vu\}\) has dimension equal to the sum of contributions \(d(a_0,\ldots,a_{m-1})\) from all cycles, where:

* for \(m=1\), the contribution is \(1\);
* for \(m\ge2\) and all coefficients zero, it is \(m\); for all coefficients nonzero, it is \(1\);
* otherwise it is the number of cyclic maximal nonzero runs plus \(\sum \max\{L-2,0\}\), the sum ranging over cyclic maximal zero runs of lengths \(L\).

This is a characterization, not merely a bound; the Fourier map makes every coordinate assignment attainable. All formulas hold in every characteristic allowed by the splitting hypothesis.

## Assumptions and scope
A finite abelian group is written additively. Here \(1\) denotes the identity endomorphism of \(A\). The hypotheses \(\varphi\) and \(1-\varphi\) invertible mean that the Alexander quandle is latin. The splitting assumption \(\exp(A)\mid(q-1)\) ensures that all characters have values in \(k^\times\) and that \(\operatorname{char}(k)\nmid N\). We use the unnormalized Fourier transform \(\widehat u(\chi)=\sum_{x\in A}u_x\chi(x)\); this is a \(k\)-linear isomorphism \(E\to k^{\widehat A}\) because \(1/N\in k\). There is no assumption that \(E\) is associative or has an identity. The commuting center is explicitly defined above and is not asserted to be the associative nucleus.

The cycle counts can be computed directly from \(A,\varphi\) without constructing characters. If \(g=\varphi^{-1}(1-\varphi)\), the number of points fixed by \(T^d\) equals \(|\ker(g^d-1)|\), by finite-abelian character duality. Consequently, for every \(m\ge1\),
\[
c_m=\frac1m\sum_{d\mid m}\mu(m/d)|\ker(g^d-1)|.
\]
Here \(\mu\) is the classical Möbius function, and the summation is finite. In the core/Takasaki specialization \(\varphi=-1\) on an odd-order \(A\), \(g=-2\), and the commuting-center dimension becomes \(|A[3]|\). For \(A=\mathbb Z/5\mathbb Z\), \(\varphi=2\), and \(q=11\), there is one fixed character and one cycle of length four. As \(T_1(11)=121\) and \(T_4(11)=202081\), the number of commuting pairs is exactly \(24{,}451{,}801\), out of \(11^{10}\) ordered pairs.

## Proof
**1. Fourier reduction.** Because character values lie in \(k\), the Fourier transform is invertible. Bilinearity and character multiplicativity give, for \(u,v\in E\),
\[
\widehat{uv}(\chi)=\widehat u(\chi\circ\varphi)\widehat v(\chi\circ(1-\varphi)).
\]
This identity is established in the prior literature; it also follows directly by substituting the basis multiplication and separating the finite sum. Put \(s=\chi\circ\varphi\). Then \(\chi\circ(1-\varphi)=T(s)\), since the defining endomorphisms commute. Thus \(uv=vu\) if and only if
\[
\widehat u(s)\widehat v(Ts)-\widehat v(s)\widehat u(Ts)=0\quad\text{for every }s\in\widehat A.
\]
For each \(T\)-cycle this says that the two-vectors \(w_s=(\widehat u(s),\widehat v(s))\in k^2\) have determinant zero on every cyclic adjacency edge. Different cycles are independent, as the Fourier map is surjective onto all coordinate functions.

**2. Counting one cycle.** Put an adjacency matrix \(B_q\) on the \(q^2\) vectors of \(k^2\), with \((B_q)_{w,z}=1\) exactly when \(\det(w,z)=0\). The number of cyclic words of length \(m\) satisfying all determinant equations is \(\operatorname{tr}(B_q^m)\), including the adjacency from the last vector back to the first. We calculate its spectrum over \(\mathbb R\) (a purely combinatorial auxiliary matrix). The zero vector is adjacent to everything; each nonzero vector is adjacent exactly to zero and to the \(q-1\) nonzero vectors on its one-dimensional line. There are \(q+1\) such lines. Differences of vector coordinates within a line produce eigenvalue zero with multiplicity \((q+1)(q-2)\). On the \(q\)-dimensional space of differences of line totals the eigenvalue is \(q-1\). The residual invariant two-space, consisting of the zero coordinate and a common nonzero-line coordinate, has matrix
\[
\begin{pmatrix}1&q^2-1\\1&q-1\end{pmatrix},
\]
with characteristic polynomial \(\lambda^2-q\lambda-q(q-1)\). Its two eigenvalues \(\lambda_+,\lambda_-\) therefore have power sum \(U_m(q)=\lambda_+^m+\lambda_-^m\), with the recurrence stated above. The zero eigenvalues contribute nothing to the trace for \(m\ge1\), so
\[
\operatorname{tr}(B_q^m)=U_m(q)+q(q-1)^m=T_m(q).
\]
The decomposition accounts for \((q+1)(q-2)+q+2=q^2\) dimensions, including \(q=2\), where the zero-eigenspace is absent. Multiplying independent cycle counts proves the formula for commuting pairs.

**3. The commuting center.** Fix a Fourier vector \(a_s=\widehat u(s)\), and let the other vector \(b_s=\widehat v(s)\) vary independently. If \(s\ne Ts\), the equation \(a_s b_{Ts}-a_{Ts}b_s=0\) for all \(b\) forces \(a_s=a_{Ts}=0\). Conversely, Fourier coefficients supported on fixed points of \(T\) commute with every \(v\). Hence \(\dim Z_{\mathrm{comm}}(E)=|\operatorname{Fix}(T)|\). A character is fixed precisely when it annihilates the image of \(\varphi^{-1}(1-2\varphi)\), which has the same image as \(1-2\varphi\); character duality and the finite endomorphism count give \(|\operatorname{Fix}(T)|=|\ker(1-2\varphi)|\).

**4. Every centralizer dimension.** On an \(m\)-cycle with \(m\ge2\), the linear constraints on \(b_i\) are \(a_i b_{i+1}-a_{i+1}b_i=0\), with indices modulo \(m\). If all \(a_i=0\) there is no constraint; if none vanishes, all ratios \(b_i/a_i\) agree. Otherwise, within a maximal consecutive nonzero run all \(b_i\) are a common scalar multiple of the corresponding \(a_i\), contributing one free scalar. Every zero position touching a nonzero neighbor is forced to have \(b_i=0\), while each interior position of a maximal zero run (distance at least one from its ends) is free. A zero run of length \(L\) therefore contributes \(\max\{L-2,0\}\) free scalars. The free parameters lie in distinct coordinates or runs and are independent. If \(m=2\), the two cyclic determinant equations are negatives of one another and the same reasoning remains valid. Fixed-point cycles contribute one unconstrained \(b_i\). Summing proves the stated exact dimension rule.

**5. Cycle census.** A point lies in a cycle of length dividing \(d\) precisely when fixed by \(T^d\). For a finite abelian group, the number of fixed characters of precomposition by \(g^d\) equals the size of \(A/\operatorname{im}(g^d-1)\), namely \(|\ker(g^d-1)|\). Möbius inversion yields the displayed \(c_m\). No enumeration over infinite objects is used.

## Verification
Run `python3 verify.py` in this directory. It prints `VERIFY_OK` if all assertions pass. The script enumerates every Fourier first-vector coordinate word for several small \((q,m)\), compares centralizer dimensions with modular matrix ranks for prime \(q\), and verifies the trace/count polynomial for all tested pairs including \((11,4)\). It separately tests the original quandle multiplication and its Fourier identity on thousands of reproducibly sampled coefficient pairs for \(\mathbb F_{11}[\operatorname{Alex}(\mathbb Z/5,\varphi)]\) with \(\varphi=2,3,4\), and for the three-point case. A nine-point example checks that the commuting center can have dimension three. These finite tests are supplementary; the proofs above establish the unrestricted finite-group statement.

## Relationship to prior work
The Fourier product identity is not claimed as new: see Elhamdadi–Ta–Virgin (September 2026), Theorem 3.2, and Ta (October 2026), Proposition 5.1. Sangare–Ta (August 2026) study commutator widths and automorphisms of quandle algebras. Zhang (October 2026), Theorem 2.3, identifies the nonunital commutator subalgebra with a group-ring ideal, but does not compute the bilinear zero-fiber count or the individual commuting-centralizer dimensions. Churchill et al. (August 2026) study a different invariant, the directed zero-divisor graph, among other topics. Prior Fourier-support classifications of square-zero elements and prior results on commutator width do not, by their statements, determine the sizes of fibers of the equation \(uv=vu\); a surjective commutator map need not have equicardinal fibers. The assessed result is the **cycle-factorized exact commuting-pair census and complete commutant-dimension rule**, not the underlying Fourier identity, the existence of the character cycles, nor the classical fact that projectively dependent vectors have zero determinant.

## Limitations
The splitting condition \(\exp(A)\mid(q-1)\) is essential to the present product of independent \(k\)-coordinate cycles. The proof does not assert the same formula over nonsplitting or modular coefficient fields. The centralizing subspace is distinguished from the potentially smaller associative nucleus. The literature comparison is bounded; equivalent prior enumerations may be unindexed or described using different invariants. The finite verifier is not an independent mathematical audit and does not replace the proof.

## References
1. B. Sangare and L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550 (first public 2026-08-03), especially Section 5, https://arxiv.org/abs/2608.01550.
2. M. Elhamdadi, L. Ta, and B. Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799 (first public 2026-09-03), Theorem 3.2, https://arxiv.org/abs/2609.03799.
3. L. Ta, *The zero divisor and augmentation conjectures for medial quandle rings*, arXiv:2610.20306 (first public 2026-10-14), Proposition 5.1, https://arxiv.org/abs/2610.20306.
4. G. Churchill, I. R. Churchill, N. Fernando, and B. Kousik, *A further study of quandles and quandle rings*, arXiv:2608.09149 (first public 2026-08-10), Section 6, https://arxiv.org/abs/2608.09149.
5. Z.-L. Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204 (first public 2026-10-06), Theorem 2.3 and Section 5, https://arxiv.org/abs/2610.08204.
