# All local prime parts are Dold for split companion Lucas sequences
## Finding
Let \(P,Q\in\mathbb Z\) satisfy \(\gcd(P,Q)=1\), \(PQ\neq0\), and suppose the companion discriminant
\[
D=P^2-4Q=s^2>0
\]
is a square. Let
\[
a=\frac{P+s}{2},\qquad b=\frac{P-s}{2},
\]
so \(a,b\in\mathbb Z\), \(a\neq b\), \(\gcd(a,b)=1\), \(ab=Q\), \(a+b=P\), and
\[
V_n(P,Q)=a^n+b^n.
\]
Assume \(P\neq0\), so no term \(V_n\) vanishes. For a prime \(p\), write \([m]_p=p^{\nu_p(m)}\) for the \(p\)-part of a nonzero integer \(m\).

Then for every prime \(p\), the local sequence
\[
A^{(p)}_n=[V_n(P,Q)]_p
\]
satisfies the Dold congruences. Equivalently,
\[
\mathbb G_{\rm D}(V)=\mathbb G_{\rm D}^{\rm almost}(V)=\mathbb P.
\]

For odd \(p\), the same local sequence is realizable exactly when either \(p\mid Q\), or \(p\nmid Q\) and the multiplicative order
\[
h_p=\operatorname{ord}_p(a b^{-1})
\]
is odd. If \(h_p\) is even, then \(p\) divides some \(V_n\), and the Möbius transform has a negative term, so neither realizability nor almost realizability holds.

At \(p=2\), local realizability holds exactly when \(Q\) is even or \(\nu_2(P)=1\). Therefore
\[
\mathbb G_{\rm R}(V)=\mathbb G_{\rm R}^{\rm almost}(V)
\]
with the explicit description above.

## Assumptions and scope
The statement treats the split, coprime, positive-square-discriminant branch of the companion Lucas family \(V(P,Q)\). The recent paper of Chuysurichay, Jaidee, Panraksa, and Ward asks how its local Dold and sign arguments extend from the classical Lucas and Fibonacci sequences to general companion Lucas sequences \(V(P,Q)\) and Lucas sequences \(U(P,Q)\). The present theorem resolves the full Dold-prime set and the local realizability set in the split branch \(D>0\) square under \(\gcd(P,Q)=1\) and \(P Q\neq0\).

The condition \(P\neq0\) excludes the degenerate case \(a=-b\), in which odd-indexed companion terms vanish and the p-part convention for nonzero integers does not apply.

## Proof
Fix a prime \(p\).

First suppose \(p\) is odd. If \(p\mid Q=ab\), coprimality implies that \(p\) divides exactly one of \(a,b\), so
\[
a^n+b^n\not\equiv0\pmod p
\]
for every \(n\ge1\). Thus \(A^{(p)}_n=1\) for every \(n\), which is realizable and Dold.

Now suppose \(p\nmid Q\). Put
\[
x\equiv a b^{-1}\pmod p,
\qquad h=\operatorname{ord}_p(x).
\]
Because \(x\in\mathbb F_p^\times\),
\[
h\mid p-1.
\]
If \(h\) is odd, then \(-1\notin\langle x\rangle\), so \(p\nmid V_n\) for every \(n\), and again \(A^{(p)}\) is the constant sequence \(1\).

Assume therefore that \(h\) is even and write
\[
h=2r.
\]
Then \(x^n=-1\) exactly when \(n/r\) is odd, so
\[
p\mid V_n\quad\Longleftrightarrow\quad n=rk\text{ with }k\text{ odd}.
\]
Let
\[
e=\nu_p(V_r)\ge1.
\]
For odd \(k\), the usual lifting-the-exponent identity gives
\[
\nu_p(V_{rk})=e+\nu_p(k).
\]
Consequently
\[
A^{(p)}_n=
\begin{cases}
p^{e+\nu_p(k)},&n=rk\text{ with }k\text{ odd},\\
1,&\text{otherwise}.
\end{cases}
\]

Use the prime-power form of the Dold criterion: for every prime \(q\), every \(m\) with \(q\nmid m\), and every \(s\ge1\), one must have
\[
A^{(p)}_{mq^s}\equiv A^{(p)}_{mq^{s-1}}\pmod{q^s}.
\]
If \(q=p\), the support condition is unchanged because \(p\nmid r\), and whenever the two terms are nontrivial their difference is
\[
p^{E+s-1}(p-1)
\]
for some \(E\ge1\), hence is divisible by \(p^s\).

Let \(q\neq p\). If the support condition does not change between \(mq^{s-1}\) and \(mq^s\), then the two p-parts are equal because multiplication by \(q\) does not change the p-adic valuation of the odd quotient. If the support condition changes, then \(q^s\) divides \(2r=h\): for odd \(q\), this is the step that completes the q-primary part of \(r\); for \(q=2\), support occurs at the unique 2-adic level \(\nu_2(r)\), and a change across two consecutive levels is still controlled by the full factor \(2^{\nu_2(r)+1}\mid2r\). Since
\[
2r=h\mid p-1,
\]
we have \(p\equiv1\pmod{q^s}\), hence every nontrivial p-power appearing in the changed term is congruent to \(1\pmod{q^s}\). The Dold congruence follows.

To decide realizability for odd \(p\), suppose \(h=2r\). Among the divisors of \(2r\), exactly \(r\) indexes a term divisible by \(p\). Therefore the Möbius transform satisfies
\[
\mathcal L_{2r}(A^{(p)})=1-p^e<0.
\]
Thus realizability, and hence almost realizability, fails whenever \(h\) is even. If \(h\) is odd, or \(p\mid Q\), the local sequence is constant \(1\), so it is realizable.

It remains to treat \(p=2\). Since \(\gcd(a,b)=1\), either \(a,b\) have opposite parity or both are odd. In the opposite-parity case every \(V_n\) is odd, so \(A^{(2)}_n=1\) for all \(n\). In the odd-odd case, set
\[
c=\nu_2(a+b)=\nu_2(P)\ge1.
\]
For odd \(n\), the 2-adic lifting identity gives
\[
\nu_2(a^n+b^n)=c,
\]
while for even \(n\), odd squares modulo \(8\) give
\[
\nu_2(a^n+b^n)=1.
\]
Hence
\[
A^{(2)}_n=
\begin{cases}
2^c,&n\text{ odd},\\
2,&n\text{ even}.
\end{cases}
\]
Its Möbius transform is zero away from \(n=1,2\), with
\[
\mathcal L_1=2^c,
\qquad
\mathcal L_2=2-2^c.
\]
This is always divisible by the relevant index, so the sequence is Dold. It is realizable exactly when \(c=1\). Since \(Q=ab\) is even exactly in the opposite-parity case, the stated 2-adic criterion follows.

## Verification
The standalone script `verify.py` exhaustively checks the Dold congruences through index \(120\) for every coprime ordered pair \((a,b)\) with \(-8\le a,b\le8\), \(ab(a+b)\neq0\), and every prime \(p\le29\). It also computes the Möbius transforms and checks the stated realizability criterion. The exact run returns

`VERIFY_OK 1700`

covering 1700 pair-prime cases. This finite replay is a consistency check; the proof above is infinite and does not rely on the enumeration.

## Relationship to prior work
Chuysurichay, Jaidee, Panraksa, and Ward, arXiv:2609.24544v1, determine the local Dold and realizability sets for the classical Lucas and Fibonacci sequences and explicitly ask how their arguments extend to general companion Lucas sequences \(V(P,Q)\) and \(U(P,Q)\). Their classical Lucas analysis permits bad local Dold primes, because in the nonsplit case the relevant rank can be controlled by \(p+1\) rather than \(p-1\).

The present split theorem identifies a contrasting rigid branch: when the characteristic roots are integers, the relevant ratio lies in \(\mathbb F_p^\times\), so its order divides \(p-1\), and this forces every local p-part to satisfy the Dold congruences.

Byszewski, Graff, and Ward prove that every integral matrix-trace sequence is globally Dold. Since \(V_n=a^n+b^n\) is a trace sequence, that result explains the global Dold property. It does not imply the present local statement: taking p-parts need not preserve the Dold property, as the recent classical-Lucas paper itself demonstrates. The new content here is the exact all-prime local classification for the split companion branch together with the local realizability criterion.

## Limitations
The theorem assumes coprime integer roots, equivalently \(\gcd(P,Q)=1\), and positive square discriminant. It does not classify nonsquare discriminants, repeated roots, the degenerate zero-term case \(P=0\), or the first-kind sequence \(U(P,Q)\). The originality search found no matching published-finding corpus record or directly covering publication, but absence from those searches is not a proof of bibliographic novelty.

## References
1. S. Chuysurichay, S. Jaidee, C. Panraksa, and T. Ward, *The local Dold congruence for Fibonacci and Lucas sequences*, arXiv:2609.24544v1, 21 September 2026.
2. J. Byszewski, G. Graff, and T. Ward, *Dold sequences, periodic points, and dynamics*, Bull. Lond. Math. Soc. 53 (2021), 1263–1298, DOI 10.1112/blms.12531.
3. P. Ribenboim, *The Fibonacci numbers and the Arctic Ocean*, in Proceedings of the 2nd Gauss Symposium, 1995, pp. 41–83.
