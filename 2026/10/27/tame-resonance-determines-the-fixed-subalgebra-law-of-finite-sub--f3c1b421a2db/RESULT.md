# Tame resonance determines the fixed-subalgebra law of finite substitution automorphisms

## Finding
Let \(q=p^e\) be a prime power, let \(d\mid(q-1)\), and fix integers \(2\le m\le p\). Put \(N=md+1\) and \(A=\mathbb F_q[t]/(t^N)\). Fix a scalar \(a\in\mathbb F_q^\times\) of exact multiplicative order \(d\). Choose \(\phi\) uniformly from the \(q^{N-2}\) \(\mathbb F_q\)-algebra automorphisms satisfying
\[
\phi(t)=at+a_2t^2+\cdots+a_{N-1}t^{N-1},
\]
where all higher coefficients are independent and uniform.

For \(1\le r\le m\), define the explicitly embedded unital algebra
\[
B_{m,r}=\mathbb F_q\,1\oplus z^{m-r+1}\bigl(\mathbb F_q[z]/(z^{m+1})\bigr)\subseteq\mathbb F_q[z]/(z^{m+1}).
\]
Then **the entire isomorphism-type distribution of the fixed algebra** is
\[
\Pr(A^\phi\cong B_{m,r})=
\begin{cases}
(q-1)q^{-r},&1\le r<m,\\
q^{-(m-1)},&r=m.
\end{cases}
\]
In particular, the algebras \(B_{m,r}\) are distinguished by their \(\mathbb F_q\)-dimensions \(r+1\). Thus the fixed-space dimension is \(r+1\) with exactly the displayed probability. The distribution is independent of \(d\), of the chosen order-\(d\) scalar, and of the particular finite field of size \(q\) beyond the displayed parameter \(q\).

For example, if \(m=3\) and \(p\ge3\), the three possible fixed-algebra dimensions are \(2,3,4\) with respective probabilities \(1-q^{-1}\), \(q^{-1}-q^{-2}\), and \(q^{-2}\). The dimension expectation equals \(1+\sum_{j=0}^{m-1}q^{-j}\).

## Assumptions and scope
All automorphisms fix \(\mathbb F_q\) pointwise. The integer \(m\) is at least two and at most the characteristic \(p\); the order \(d\) may equal one and need not be prime. This is a conditional uniform model with fixed linear coefficient, **not** a uniform distribution on conjugacy classes. Algebra isomorphisms are unital and \(\mathbb F_q\)-linear. Fixed means \(A^\phi=\{v\in A:\phi(v)=v\}\). The monomial-tail algebra \(B_{m,r}\) has the inherited multiplication, not a free product or a general square-zero extension.

## Proof
**1. Existence and measure-preserving triangular normal form.** Every series with nonzero linear coefficient defines an automorphism of the truncated algebra by recursive compositional inversion. For each \(j\) with \(2\le j<N\), conjugation of the substitution series by a change of variable \(h_j(t)=t+c_jt^j\) changes its coefficient at \(t^j\) by \(c_j(a^j-a)\), without changing any lower-degree coefficient. This follows by expanding \(h_j\circ f\circ h_j^{-1}\) modulo \(t^{j+1}\).

Since \(a\) has order \(d\), \(a^j-a\ne0\) precisely when \(j\not\equiv1\pmod d\). Successively eliminate every such nonresonant coefficient and take \(c_j=0\) at resonant indices. The resulting conjugate has the form
\[
f_\mathrm{nf}(t)=a t\left(1+\sum_{s=1}^{m-1}b_s t^{sd}\right)\pmod {t^{md+1}}.
\]
At each resonant degree \(sd+1\), the new coefficient \(b_s\) is a nonzero fixed scalar multiple of the original coefficient \(a_{sd+1}\) plus a function of strictly earlier original coefficients. Therefore the triangular coordinate change from original coefficients to the \(m-1\) resonant coefficients and the eliminated coordinates is bijective, and \(b_1,\dots,b_{m-1}\) are independent uniform elements of \(\mathbb F_q\). Conjugation of substitution series gives conjugate algebra automorphisms, hence isomorphic fixed algebras.

**2. Fixed algebras of resonant normal forms.** In normal form all monomials in \(f_\mathrm{nf}(t)^i\) have exponents congruent to \(i\pmod d\). Thus the vector-space decomposition of \(A\) by exponent residues modulo \(d\) is invariant. On a residue class other than zero, the substitution matrix is triangular with diagonal scalar \(a^i\ne1\), so the restriction of \(\phi-I\) is invertible and contributes no fixed elements. The residue-zero subalgebra is exactly \(\mathbb F_q[z]/(z^{m+1})\), with \(z=t^d\).

Let \(r<m\) be the first index with \(b_r\ne0\). Writing \(f_\mathrm{nf}(t)=at(1+\sum_s c_s z^s)\) with \(c_s=b_s\), we have
\[
\phi(z)=z+\gamma z^{r+1}+O(z^{r+2}),\qquad\gamma=dc_r\ne0,
\]
because \(d\) is prime to \(p\). If a nonconstant polynomial \(u(z)\) has lowest nonconstant term \(u_jz^j\) with \(u_j\ne0\), then \(\phi(u)-u\) has leading term \(j\gamma u_j z^{j+r}\) whenever \(j+r\le m\). Here \(1\le j\le m-r\le m-1<p\), so that term is nonzero. Conversely, every monomial \(z^j\) with \(j\ge m-r+1\) is fixed because substitution first changes it in degree at least \(m+1\). Therefore the entire fixed algebra is precisely \(B_{m,r}\).

If all \(m-1\) resonant coefficients vanish, the normalized map is \(t\mapsto at\), which fixes the full \(z\)-subalgebra and no other residue class. This gives \(B_{m,m}\). In both cases these statements identify actual subalgebras, not just their dimensions.

**3. Distribution.** The first nonzero among \(m-1\) independent uniform coordinates occurs at position \(r\) with probability \(q^{-(r-1)}(1-q^{-1})=(q-1)q^{-r}\). The probability that all are zero is \(q^{-(m-1)}\). The events partition the sample space and give the stated complete law. Finally, \(\dim_{\mathbb F_q}B_{m,r}=r+1\), while summing tail probabilities gives \(\mathbb E\dim A^\phi=1+\sum_{j=0}^{m-1}q^{-j}\).

## Verification
Run the bundled standalone script `checker.py` with Python 3; no external dependencies are required. It directly constructs the finite fields, computes the substitution operator on the basis \(1,t,\dots,t^{N-1}\), and finds its fixed-vector dimension by modular Gaussian elimination. It exhaustively enumerates **38,674** automorphisms across ten configurations, including \(\mathbb F_4\), \(\mathbb F_9\), and multipliers of orders one, two, and three. For each configuration it also tests canonical representatives of every normal-form stratum and the predicted monomial-tail fixed basis. All ten distributions agree with the exact formula.

The script further checks the explicit boundary \((q,p,d,m)=(2,2,1,3)\) outside the hypothesis. There the four automorphisms yield three fixed spaces of dimension three and one of dimension four, showing why a characteristic restriction is mathematically relevant. These are finite consistency checks, not a proof for infinitely many fields or truncation lengths.

## Relationship to prior work
M. M. Cohen's 2018 exposition of formal substitution groups (arXiv:1804.00059), including the earlier Muckenhoupt normal form summarized in its Section 5.2, provides the classical conjugacy perspective. Cohen's results concern characteristic zero and the classification of finite-order series, not this distribution of fixed subalgebras over finite fields. Byszewski–Cornelissen–Tijsma (arXiv:2008.04971, 2020) study finite-order elements, break sequences, and automata for the characteristic-two Nottingham group; that is a different invariant from the fixed algebra of a randomly chosen finite jet. The present proof uses finite, explicitly normalized substitution operators and obtains a complete algebra-isomorphism-type law in the indicated tame range.

## Limitations
The formula is not asserted when \(m>p\), where factors \(j\gamma\) can vanish and additional fixed vectors appear. It makes no claim about unrestricted random linear multipliers, automorphisms of multivariate local algebras, or isomorphism classes of automorphisms. The use of the classical normal-form framework is not an originality claim. Search coverage cannot exclude an equivalent result in an unexamined treatment of Nottingham filtrations or finite jet invariant rings, and no external independent audit has been performed.

## References
1. Marshall M. Cohen, *Elements of Finite Order in the Group of Formal Power Series Under Composition* (first public version March 30, 2018), arXiv:1804.00059, https://arxiv.org/abs/1804.00059. See Theorem 2 and Section 5.2 (earlier Muckenhoupt normal form).
2. Jakub Byszewski, Gunther Cornelissen, Djurre Tijsma, *Automata and finite order elements in the Nottingham group* (first public version August 11, 2020), arXiv:2008.04971, https://arxiv.org/abs/2008.04971.
