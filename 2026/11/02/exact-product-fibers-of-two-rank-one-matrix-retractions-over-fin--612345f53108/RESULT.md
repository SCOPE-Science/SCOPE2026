# Exact product fibers of two rank-one matrix retractions over finite fields

## Finding
Let \(K=\mathbb F_q\), where \(q\) is any prime power, and \(n\ge2\). Put
\[
\mathcal P=\{E\in M_n(K):E^2=E,\ \operatorname{rank}E=1\},\qquad
\mu:\mathcal P\times\mathcal P\longrightarrow M_n(K),\quad (E,F)\longmapsto EF.
\]
Write \([m]_q=(q^m-1)/(q-1)\), and \(P=q^{n-1}[n]_q=|\mathcal P|\). The fiber size \(\nu(A)=|\mu^{-1}(A)|\) is **completely determined** by the following mutually exclusive cases:
\[
\boxed{\begin{array}{c|c}
\text{target }A&\nu(A)\\\hline
A=0&P\,q^{n-1}[n-1]_q\\
\operatorname{rank}A=1,\ \operatorname{tr}A=0&q^{2n-3}\\
\operatorname{rank}A=1,\ \operatorname{tr}A=1&q^{n-1}+(q^{n-1}-1)q^{n-2}\\
\operatorname{rank}A=1,\ \operatorname{tr}A\notin\{0,1\}&(q^{n-1}-1)q^{n-2}\\
\operatorname{rank}A\ge2&0.
\end{array}}
\]
These cases exhaust all matrices, including characteristic two. Every rank-one target has a strictly positive fiber. A nonzero rank-one trace-zero matrix is square-zero; a rank-one trace-one matrix is idempotent; and the other nonzero-trace targets are scalar multiples of rank-one idempotents.

As a consequence, fixing either first factor \(E\), the number of second factors \(F\) for which \(EF\) is again idempotent is
\[
q^{n-1}[n-1]_q+q^{n-1}+(q^{n-1}-1)q^{n-2}.
\]
For fixed \(n\), the conditional probability is asymptotic to \(3/q\) when \(n=2\), and to \(2/q\) when \(n\ge3\), as \(q\) runs through prime powers tending to infinity.

## Assumptions and scope
All matrices act on the column space \(V=K^n\). Factors are ordered. Idempotent means \(E^2=E\), with rank **exactly one**, not rank at most one. No symmetry, self-adjointness, field-characteristic restriction, or invertibility assumption is made. The scalar \(\operatorname{tr}A\) lies in \(K\), and in the displayed table \(0\) and \(1\) are its additive and multiplicative identities. The zero target is separate from nonzero rank-one nilpotent targets.

## Proof
**1. Rank-one retraction parameterization.** For nonzero \(u\in V\) and \(\phi\in V^*\), write \(u\phi\) for the linear map \(x\mapsto \phi(x)u\). It has rank one and is idempotent precisely when \(\phi(u)=1\). Every rank-one idempotent has such a presentation. Choosing its image line (\([n]_q\) options) and then a nonzero spanning vector on the line, the admissible \(\phi\)'s form an affine hyperplane with \(q^{n-1}\) elements. Thus \(P=q^{n-1}[n]_q\).

**2. Every nonzero rank-one target.** Fix a factorization \(A=u\psi\) with \(u\ne0\), \(\psi\ne0\). Suppose \(EF=A\). Since \(\operatorname{im}(EF)=\operatorname{im}A=Ku\), necessarily \(\operatorname{im}E=Ku\), so there is a unique \(\phi\) with \(E=u\phi\) and \(\phi(u)=1\). Since \(A\)'s row space is contained in the one-dimensional row space of \(F\), there is a unique \(v\) with \(F=v\psi\) and \(\psi(v)=1\). The product equation then becomes \(\phi(v)=1\). Conversely, every pair \((v,\phi)\) satisfying
\[
\psi(v)=1,\qquad \phi(u)=1,\qquad\phi(v)=1
\]
gives exactly one ordered factorization of \(A\) by rank-one idempotents. The affine hyperplane \(H=\{v:\psi(v)=1\}\) has \(q^{n-1}\) elements. If \(u,v\) are independent, the two conditions on \(\phi\) have \(q^{n-2}\) solutions; if \(v=cu\), they are consistent precisely when \(c=1\), in which case there are \(q^{n-1}\) solutions.

Set \(t=\psi(u)=\operatorname{tr}A\). If \(t=0\), the line \(Ku\) misses \(H\), so all \(q^{n-1}\) vectors in \(H\) are independent of \(u\) and \(\nu(A)=q^{2n-3}\). If \(t=1\), exactly \(v=u\) lies in \(H\cap Ku\), giving \(q^{n-1}\) choices of \(\phi\); the other \(q^{n-1}-1\) vectors give \(q^{n-2}\) choices each. If \(t\notin\{0,1\}\), the unique point \(v=t^{-1}u\in H\cap Ku\) is inconsistent with \(\phi(u)=\phi(v)=1\), so only the remaining \(q^{n-1}-1\) vectors contribute. This proves the three nonzero-target rows.

**3. Zero target and support.** Given \(E\in\mathcal P\), \(EF=0\) exactly when the image line of \(F\) lies inside the \((n-1)\)-dimensional kernel of \(E\). There are \([n-1]_q\) such lines, each admitting \(q^{n-1}\) rank-one idempotent projections. Multiplying by \(P\) proves the zero row. Rank submultiplicativity rules out any target of rank at least two. All positive values in the nonzero-target rows prove the asserted support statement.

**4. Idempotent-product frequency.** For rank-one \(A=u\psi\), \(A^2=(\operatorname{tr}A)A\); thus a product \(EF\) is idempotent exactly when it is zero or is rank one with trace one. For fixed \(E\), the number of zero products is \(q^{n-1}[n-1]_q\). All rank-one idempotent targets form one \(\operatorname{GL}_n(K)\)-conjugacy class; simultaneous conjugation fixes the size of their product fibers, so the number of \(F\)'s producing a rank-one idempotent is the trace-one fiber size from Step 2. (Equivalently, double-count the triples \((E,F,A=EF)\) and use \(|\mathcal P|=P\).) Add the two contributions and divide by \(P\). When \(n=2\), the numerator equals \(3q-1\) and \(P=q(q+1)\). When \(n\ge3\), its highest-order term is \(2q^{2n-3}\) while \(P\) has highest-order term \(q^{2n-2}\), proving the stated limits.

## Verification
Run `python verify.py` in the same directory as this document. The standalone standard-library checker constructs all rank-one idempotents from projective-normalized image vectors and dual covectors, multiplies every ordered pair, and compares **every populated target fiber** with the formula. It also constructs all rank-one targets independently to check that none is missing. Checks pass for \((n,q)=(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,2)\). Field \(\mathbb F_4\) uses an explicit polynomial-basis multiplication table. These finite tests are not a substitute for Steps 1–4, which prove the formula for all prime powers and dimensions.

## Relationship to prior work
Products of idempotents are classical in matrix semigroups. Jain and Leroy [1], first public 17 July 2024, address **whether** matrices over certain rings admit decompositions into products of idempotents, and their main results concern existence and multiplication with elementary/permutation factors. Their paper does not state a finite-field multiplication-map fiber distribution with both factors restricted to rank one. The earlier work of Fountain and Lewin [2] concerns the generation of endomorphism monoids by idempotent products, again a distinct existence problem. A closely related public result [3] counts factorizations of \(2\times2\) matrices into one idempotent and one **nilpotent**; the present result requires both factors to be rank-one idempotents, handles all dimensions, and distinguishes zero, nonzero nilpotent, trace one and the remaining traces.

## Limitations
The theorem concerns only products of **two** rank-one idempotents. It makes no claim about products of more factors, arbitrary-rank idempotents, rings that are not finite fields, or the minimal number of arbitrary idempotents necessary to factor a matrix. The novelty comparison is to the sources actually inspected and retrieved, not an assertion of exhaustive publication priority. An equivalent result might appear in the literature under pair-orbit geometry, projection-factorizations, or semigroup multiplication-fiber terminology. There has been no independent audit.

## References
[1] S. K. Jain and A. Leroy, *Decomposition of matrices into product of idempotents and separativity of regular rings*, arXiv:2407.12231 (first posted 2024-07-17), full arXiv text inspected at https://arxiv.org/abs/2407.12231 .

[2] J. Fountain and A. Lewin, *Products of idempotent endomorphisms of an independence algebra of finite rank*, Proc. Edinburgh Math. Soc. (online 2009), accessible abstract at https://www.cambridge.org/core/journals/proceedings-of-the-edinburgh-mathematical-society/article/products-of-idempotent-endomorphisms-of-an-independence-algebra-of-finite-rank/487CE1D6DFCF98FBFBC005E9F0548337 (publisher abstract consulted; full text not inspected).

[3] published-finding corpus, *Exact fibers of idempotent–nilpotent factorizations in two dimensions*, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-fibers-of-idempotent-nilpotent-factorizations-in-two-dimen--376b6f723a17 (published searchable summary inspected; full source not read).
