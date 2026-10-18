# An explicit cyclotomic-norm cutoff for minimal vanishing power sums

## Finding
Let \(n\ge2\) be an integer and \(p\) a prime such that \(n\mid p-1\). Write \(r\) for the smallest prime divisor of \(n\), \(d=\varphi(n)\), and \(T=(r-1)^d\). If \(p^k>T\), then **every** residue \(q\) of exact multiplicative order \(n\) modulo \(p^k\) satisfies
\[
m(q,p^k)=r.
\]
Here \(m(q,e)\) is the smallest number of terms in a nonempty sum of powers of \(q\), with repetitions allowed, that is divisible by \(e\).

In particular, if \(K_*(p,n)\) denotes the least positive integer \(K\) such that the cyclic subgroup of order \(n\) in \((\mathbb Z/p^K\mathbb Z)^\times\) has minimal zero-sum length \(r\), then
\[
K_*(p,n)\le 1+\left\lfloor\log_p((r-1)^{\varphi(n)})\right\rfloor\le\varphi(n).
\]
The first bound is equivalently the unique smallest \(K\ge1\) for which \(p^K>(r-1)^{\varphi(n)}\). Moreover, for \(p>(r-1)^{\varphi(n)}\), already \(K_*(p,n)=1\). These are upper bounds, not asserted to be sharp.

## Assumptions and scope
The integer \(n\) is at least two; the prime \(p\) satisfies \(n\mid p-1\); \(k\) is a positive integer. The unit group modulo \(p^k\) is cyclic, so residues of exact order \(n\) exist. They generate the same subgroup and hence have the same invariant \(m\). Every exponent in a defining sum is a nonnegative integer, and repeated powers are permitted. We use the following classical theorem: if \(r\) is the smallest prime factor of \(n\), then no positive sum of fewer than \(r\) complex \(n\)-th roots of unity can vanish (Lam–Leung [2]).

## Proof
**Step 1 (the cyclotomic specialization).** Let \(q\) have order \(n\) modulo \(p^k\). Reduction modulo \(p\) also has order \(n\), because the kernel of \((\mathbb Z/p^k\mathbb Z)^\times\to(\mathbb Z/p\mathbb Z)^\times\) is a \(p\)-group whereas \(n\mid p-1\). For every proper positive divisor \(h\) of \(n\), \(p\nmid q^h-1\). Since \(\Phi_h(q)\) divides \(q^h-1\), \(\Phi_h(q)\) is invertible modulo \(p^k\). Factoring \(q^n-1=\prod_{h\mid n}\Phi_h(q)\), we conclude that \(\Phi_n(q)\equiv0\pmod{p^k}\).

**Step 2 (integer resultant obstruction).** Suppose a sum of \(s\) powers of \(q\) vanishes modulo \(p^k\), with \(1\le s<r\). Reduce exponents modulo \(n\), obtaining a polynomial
\[
f(X)=X^{a_1}+\cdots+X^{a_s},\qquad 0\le a_j<n.
\]
Let \(\zeta\) be a primitive complex \(n\)-th root of unity. The Lam–Leung weight theorem implies \(f(\zeta)\ne0\). Consequently the integer resultant
\[
R=\operatorname{Res}(\Phi_n,f)=
\prod_{\substack{1\le a\le n\\\gcd(a,n)=1}}f(\zeta^a)
\]
is nonzero. The triangle inequality gives \(|f(\zeta^a)|\le s\), so
\[
0<|R|\le s^{\varphi(n)}\le(r-1)^{\varphi(n)}=T.
\]
The determinant identity for the Sylvester resultant gives polynomials \(A,B\in\mathbb Z[X]\) satisfying \(R=A(X)\Phi_n(X)+B(X)f(X)\). Evaluating at \(q\), Step 1 and the assumed zero sum imply \(p^k\mid R\), which contradicts \(p^k>T\). Thus no such sum with fewer than \(r\) terms exists.

**Step 3 (sharp number of terms).** Put \(v=q^{n/r}\). It has order \(r\) modulo \(p^k\), and \(v\not\equiv1\pmod p\), so \(v-1\) is invertible modulo \(p^k\). From \((v-1)(1+v+\cdots+v^{r-1})=v^r-1\equiv0\pmod{p^k}\), we obtain a sum of exactly \(r\) powers of \(q\) that vanishes. Steps 2–3 prove \(m(q,p^k)=r\).

**Step 4 (effective depth and exceptional primes).** The least integer \(k\ge1\) satisfying \(p^k>T\) is \(1+\lfloor\log_p T\rfloor\), with the convention \(\log_p1=0\). Because \(p\ge n+1>r-1\), \(p^{\varphi(n)}>T\), so this cutoff is at most \(\varphi(n)\). Taking \(k=1\) proves the explicit prime cutoff.

## Verification
The accompanying standalone file `verify.py` directly enumerates short sums in cyclic order-\(n\) subgroups for selected prime powers, constructs the roots by elementary Hensel lifting, and tests the displayed cutoff. It checks 21 prime-power instances for \((n,p)\) equal to \((5,11),(5,61),(7,29),(7,43),(11,23),(11,67),(13,53)\). The resulting sequences agree with the previously published numerical examples. The verifier is finite corroboration, not a proof for arbitrary \(n,p,k\). The unrestricted theorem is proved in Steps 1–4 from exact algebraic identities and the cited Lam–Leung theorem.

## Relationship to prior work
Jacob and Külshammer [1, Proposition 10] prove that for every \(n\mid p-1\) there is *some* modulus \(p^K\) at which the minimum equals the least prime divisor \(r\) of \(n\); their text explicitly requests an upper bound for \(K\). The present theorem provides a uniform closed-form bound depending only on \(p,n,r\), and simultaneously makes their exceptional-prime finiteness effective. Their Propositions 14–15 already classify the cases \(n=5\) and \(n=7\), including sharper thresholds, and are not claimed as new. Breuer, Héthelyi, Horváth and Külshammer [3, Proposition 2.25] prove qualitative finiteness for prime order and provide a resultant-based procedure, but neither that result nor [1, Corollary 13] states the uniform cutoff above. The weight obstruction used here is due to Lam and Leung [2].

## Limitations
The bound can be far from optimal: [1, Example 16] reports that \(n=11,p=23\) reaches the full value at \(k=5\), whereas the norm cutoff is \(k=8\). No statement is made for moduli \(p^k\) when the order of \(q\) includes a factor of \(p\), or for general composite moduli. Existing work already gives finer fixed-order classifications for several small \(n\); an unindexed quantitative norm bound is a remaining priority for external originality review.

## References
[1] L. Jacob and B. Külshammer, *Congruences for sums of powers of an integer*, arXiv:2204.09403v1, publicly posted 20 April 2022, especially Proposition 10, Corollary 13, and Example 16. https://arxiv.org/html/2204.09403v1

[2] T. Y. Lam and K. H. Leung, *On vanishing sums for roots of unity*, arXiv:math/9511209v1 (1995); published as *On Vanishing Sums of Roots of Unity*, J. Algebra 224 (2000), 91–109. https://arxiv.org/pdf/math/9511209

[3] T. Breuer, L. Héthelyi, E. Horváth and B. Külshammer, *The Loewy Structure of Certain Fixpoint Algebras, Part II*, International Electronic Journal of Algebra 30 (2021), 16–65, DOI 10.24330/ieja.969577, especially Proposition 2.25 and Example 2.26. https://www.ieja.net/files/papers/volume-30/2-V30-2021.pdf
