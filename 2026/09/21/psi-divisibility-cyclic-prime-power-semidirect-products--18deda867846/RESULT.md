# Prime-power action images obstruct psi-divisibility in cyclic-by-cyclic groups

For a finite group \(X\), write
\[
\psi(X)=\sum_{x\in X} o(x).
\]
Recall that \(X\) is **psi-divisible** if \(\psi(Y)\mid\psi(X)\) for every subgroup \(Y\le X\).

## A centralizer-difference criterion

Let \(P=C_{p^\alpha}\) with \(\alpha\ge 1\), and let
\[
G=P\rtimes H,\qquad (p,|H|)=1.
\]
Put \(A=\psi(P)\) and \(C=C_H(P)\). Then
\[
\boxed{\gcd(A,\psi(G))=\gcd\!\bigl(A,\psi(H)-\psi(C)\bigr).}
\tag{1}
\]

Indeed, the standard cyclic-normal-Sylow formula gives
\[
\psi(G)
=|P|\psi(H)+(A-|P|)\psi(C)
=A\psi(C)+p^\alpha\bigl(\psi(H)-\psi(C)\bigr).
\]
Also \(A\equiv1\pmod p\), so \(\gcd(A,p)=1\), and (1) follows.

This elementary identity is useful because it isolates exactly the obstruction coming from the action of \(H\) on \(P\).

## Prime-power cyclic complements

### Theorem

Let \(p\ne q\) be primes and let \(\alpha,\beta\ge1\). Suppose
\[
G=C_{p^\alpha}\rtimes C_{q^\beta}
\]
has nontrivial action, and suppose that the image of
\[
C_{q^\beta}\longrightarrow \operatorname{Aut}(C_{p^\alpha})
\]
has order \(q^\gamma\), where \(1\le\gamma\le\beta\). Then
\[
\boxed{
\gcd\!\bigl(\psi(C_{p^\alpha}),\psi(G)\bigr)
=
\gcd\!\left(
\psi(C_{p^\alpha}),
\frac{q^{2\gamma}-1}{q+1}
\right).
}
\tag{2}
\]
In particular,
\[
\boxed{\psi(C_{p^\alpha})\nmid\psi(G),}
\tag{3}
\]
so \(G\) is not psi-divisible.

### Proof

Let \(P=C_{p^\alpha}\), \(H=C_{q^\beta}\), and
\[
A=\psi(P).
\]
The centralizer \(C_H(P)\) is precisely the kernel of the action, hence
\[
C_H(P)\cong C_{q^{\beta-\gamma}}.
\]
Using
\[
\psi(C_{\ell^t})=\frac{\ell^{2t+1}+1}{\ell+1}
\qquad(t\ge1),
\]
with the convention \(\psi(C_1)=1\), we get
\[
\begin{aligned}
\psi(C_{q^\beta})-\psi(C_{q^{\beta-\gamma}})
&=
q^{2(\beta-\gamma)+1}
\frac{q^{2\gamma}-1}{q+1}.
\end{aligned}
\tag{4}
\]
By (1),
\[
\gcd(A,\psi(G))
=
\gcd\!\left(
A,
q^{2(\beta-\gamma)+1}\frac{q^{2\gamma}-1}{q+1}
\right).
\tag{5}
\]

Because the action has \(q\)-power image and \(q\ne p\), its image lies in the
\(p'\)-part of \(\operatorname{Aut}(C_{p^\alpha})\); consequently
\[
q^\gamma\mid p-1.
\tag{6}
\]
Moreover
\[
A
=
1+(p-1)\sum_{i=1}^{\alpha}p^{2i-1},
\]
so (6) implies \(A\equiv1\pmod q\). Hence \(\gcd(A,q)=1\), and (5) reduces to (2).

It remains to show that the right-hand side of (2) is strictly smaller than \(A\). Set
\[
E=\frac{q^{2\gamma}-1}{q+1}.
\]
Then
\[
E<q^{2\gamma}.
\tag{7}
\]
By (6), \(p\ge q^\gamma+1\), while
\[
A\ge\psi(C_p)=p^2-p+1
\ge q^{2\gamma}+q^\gamma+1
>q^{2\gamma}.
\tag{8}
\]
Thus \(0<E<A\), so \(\gcd(A,E)<A\). This proves (3). Since \(P\le G\), the subgroup \(P\) itself witnesses failure of psi-divisibility. \(\square\)

### A particularly sharp subfamily

If \(q=2\) and \(\gamma=1\), then
\[
\frac{2^{2}-1}{2+1}=1,
\]
so (2) becomes
\[
\boxed{\gcd\!\bigl(\psi(C_{p^\alpha}),\psi(G)\bigr)=1.}
\]
Thus every nontrivial order-two action in this family gives not merely nondivisibility but coprimality between the two relevant sums of element orders.

## A cyclic-by-cyclic consequence

Consider more generally
\[
G=C_{p^\alpha}\rtimes C_n,\qquad (p,n)=1,
\]
with nontrivial action image of order \(d>1\).

### Corollary

The group \(G\) is not psi-divisible in either of the following cases:

1. \(d\) is a prime power;
2. \(\gcd(d,n/d)=1\).

### Proof

If \(d=q^\gamma\), write \(n=q^\beta s\) with \((q,s)=1\). Every prime-to-\(q\) factor of \(C_n\) acts trivially, so
\[
G\cong
\bigl(C_{p^\alpha}\rtimes C_{q^\beta}\bigr)\times C_s,
\]
and the two direct factors have coprime orders. The first factor is not psi-divisible by the theorem. For direct products of coprime-order groups, psi-divisibility holds exactly when it holds in both factors; hence \(G\) is not psi-divisible.

Now suppose \(\gcd(d,n/d)=1\). The cyclic complement splits as
\[
C_n\cong C_d\times C_{n/d},
\]
where \(C_{n/d}\) is the action kernel and the restriction to \(C_d\) is faithful. Thus
\[
G\cong
\bigl(C_{p^\alpha}\rtimes C_d\bigr)\times C_{n/d}.
\]
Again the factors have coprime orders. It is therefore enough to rule out the faithful-action factor
\[
K=C_{p^\alpha}\rtimes C_d.
\]
Faithfulness and \((p,d)=1\) imply \(d\mid p-1\). Applying (1) with trivial centralizer gives
\[
\gcd\!\bigl(\psi(C_{p^\alpha}),\psi(K)\bigr)
=
\gcd\!\bigl(\psi(C_{p^\alpha}),\psi(C_d)-1\bigr).
\]
But
\[
\psi(C_d)-1<d^2\le(p-1)^2
<p^2-p+1\le\psi(C_{p^\alpha}),
\]
so \(\psi(C_{p^\alpha})\nmid\psi(K)\). Hence \(K\), and therefore \(G\), is not psi-divisible. \(\square\)

## Relation to earlier work

Harrington, Jones and Lamarche introduced the psi-divisible condition and proved that the finite abelian psi-divisible groups are exactly the cyclic groups of square-free order. They also reported that no nonabelian psi-divisible example was known.

Lazorec later studied ZM-groups and recorded the cyclic-normal-Sylow formula used above. For
\[
ZM(p^\alpha,n,r)
\]
with
\[
n=\prod_i q_i^{\beta_i},
\]
Proposition 2.4 of that work gives a sufficient nondivisibility criterion under the exponent-size hypothesis
\[
\alpha\ge \max_{\,q_i\mid p-1}\beta_i.
\]
The theorem above removes any comparison between \(\alpha\) and \(\beta\) when the cyclic complement is a prime power; the exact gcd in (2) is independent of the kernel depth \(\beta-\gamma\). The corollary also covers arbitrary faithful cyclic complements and every cyclic complement whose action image is a prime power.

As of the 2023 psi-divisibility-graph paper, the existence of a nonabelian psi-divisible finite group was still explicitly stated as open. A 2026 paper on extreme vertices of psi-divisibility graphs treats cyclic \(p\)-groups rather than resolving that existence problem.

## Limitations

The result does **not** settle the existence of nonabelian psi-divisible finite groups.

For \(C_{p^\alpha}\rtimes C_n\), the corollary leaves a genuine residual region: the action image \(d\) may have at least two distinct prime divisors while simultaneously sharing a prime divisor with the kernel size \(n/d\). The simple direct-product reductions above no longer apply there.

The originality claim is only to the best of our knowledge. The centralizer-difference identity (1) is a short consequence of a known sum-of-element-orders formula, so an equivalent observation could exist implicitly or under different terminology even though targeted searches did not locate the theorem, the exact gcd formula (2), or the action-image corollary.

## Reproducibility

The accompanying `artifacts/verify.py` uses exact integer arithmetic only. It checks (2), the strict obstruction (3), and the relevant inequalities for thousands of compatible small prime-power parameters. The computation is a finite sanity check; the proof above is the certificate for all parameters.

## References

1. J. Harrington, L. Jones, A. Lamarche, *Characterizing Finite Groups Using the Sum of the Orders of the Elements*, International Journal of Combinatorics (2014), Article ID 835125. DOI: 10.1155/2014/835125.
2. M.-S. Lazorec, *On a divisibility property involving the sum of element orders*, Bulletin of the Malaysian Mathematical Sciences Society 44 (2021), 941–951. DOI: 10.1007/s40840-020-00987-8; arXiv:2003.01678.
3. M.-S. Lazorec, *A graph related to the sum of element orders of a finite group*, Contributions to Discrete Mathematics 18 (2023), 113–128. DOI: 10.55016/ojs/cdm.v18i2.73182.
4. A. Kumar, V. Kumar, A. Sehgal, *Extreme Vertices of the Psi-Divisible Graph of the Group \(Z_{p^n}\)*, Journal of the Indonesian Mathematical Society 32 (2026), article 2145. DOI: 10.22342/jims.v32i2.2145.
