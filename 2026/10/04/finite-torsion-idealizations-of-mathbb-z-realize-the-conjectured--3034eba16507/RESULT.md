# Finite torsion idealizations of \(\mathbb Z\) realize the conjectured total-graph domination bound

## Finding

Let \(M\) be a nonzero finite abelian group of exponent \(n>1\), let \(p\) be the smallest prime divisor of \(n\), and let \(R=\mathbb Z\ltimes M\) be the Nagata idealization with multiplication \((a,m)(b,u)=(ab,au+bm)\). Then the domination number of the total graph is exactly \(\gamma(T_\Gamma(R))=p\). If \(n\) has at least two distinct prime divisors, then \(R\) is non-Artinian, \(Z(R)\) is not an ideal, and the finite-index maximal annihilator ideals are exactly \(q\mathbb Z\ltimes M\) for primes \(q\mid n\); hence the minimum such index is \(p\), so this family satisfies Chelvam--Asir Conjecture 2.8 exactly.

This supplies an infinite, non-Artinian torsion-idealization family for the domination conjecture posed for total graphs of commutative rings.

## Assumptions and scope

Let \(M\) be a nonzero finite abelian group, written additively, with exponent \(n>1\). The idealization
\[
R=\mathbb Z\ltimes M
\]
has addition componentwise and multiplication
\[
(a,m)(b,u)=(ab,au+bm).
\]
Its identity is \((1,0)\). The total graph \(T_\Gamma(R)\) has all elements of \(R\) as vertices, with distinct vertices adjacent exactly when their sum is a zero-divisor.

Let \(p\) denote the smallest prime divisor of \(n\).

## Proof

First characterize the zero-divisors. For \((a,m)\in R\),
\[
(a,m)\in Z(R)
\quad\Longleftrightarrow\quad
\gcd(a,n)>1.
\]

If \(q\mid\gcd(a,n)\), then \(M\) has a nonzero element \(u\) of order \(q\). Since \(q\mid a\),
\[
(a,m)(0,u)=(0,au)=(0,0),
\]
so \((a,m)\) is a zero-divisor.

Conversely, if \(\gcd(a,n)=1\), choose integers \(r,s\) with \(ra+sn=1\). Because \(nM=0\), multiplication by \(a\) on \(M\) is invertible with inverse multiplication by \(r\). If
\[
(a,m)(b,u)=(0,0),
\]
then \(ab=0\) in \(\mathbb Z\), hence \(b=0\), and then \(au=0\), hence \(u=0\). Thus \((a,m)\) is regular.

Therefore two distinct vertices \((a,m)\) and \((b,u)\) are adjacent exactly when
\[
\gcd(a+b,n)>1.
\]

For the upper bound, take
\[
D=\{(0,0),(1,0),\ldots,(p-1,0)\}.
\]
Given any vertex \((a,m)\notin D\), choose \(j\in\{0,\ldots,p-1\}\) with \(a+j\equiv0\pmod p\). Then \(p\mid n\) and \(p\mid a+j\), so \((a,m)\) is adjacent to \((j,0)\). Hence
\[
\gamma(T_\Gamma(R))\le p.
\]

For the lower bound, let
\[
D=\{(a_1,m_1),\ldots,(a_k,m_k)\}
\]
with \(k<p\). For each prime \(q\mid n\), at most \(k<p\le q\) residue classes modulo \(q\) are forbidden by the conditions
\[
x\equiv-a_i\pmod q.
\]
Choose a residue \(r_q\pmod q\) avoiding all of them. By the Chinese remainder theorem there is an integer \(x\) satisfying \(x\equiv r_q\pmod q\) for every prime \(q\mid n\). Adding a suitable multiple of the radical of \(n\), arrange also that \(x\ne a_i\) for every \(i\). Then
\[
\gcd(x+a_i,n)=1
\]
for every \(i\), so the vertex \((x,0)\notin D\) is adjacent to no element of \(D\). Thus no set of size less than \(p\) dominates, and
\[
\gamma(T_\Gamma(R))=p.
\]

Now consider annihilator ideals. If \(y\in M\) has order \(d>1\), then
\[
\operatorname{Ann}_R(0,y)=d\mathbb Z\ltimes M,
\]
which has index \(d\). If the first coordinate of a nonzero element of \(R\) is nonzero, its annihilator has infinite index, because every annihilator element has first coordinate zero. Hence the finite-index maximal annihilator ideals occur precisely when \(d=q\) is prime, namely
\[
q\mathbb Z\ltimes M
\qquad(q\mid n),
\]
and the minimum finite index is the smallest prime divisor \(p\) of \(n\).

The ring \(R\) is not Artinian because
\[
R/(0\ltimes M)\cong\mathbb Z.
\]
If \(n\) has at least two distinct prime divisors, the zero-divisors are not closed under addition. Indeed, by the Chinese remainder theorem there is a nontrivial idempotent residue \(e\pmod n\) with \(e\) divisible by one prime-power component of \(n\) and congruent to \(1\) on the complementary components. Then both \((e,0)\) and \((1-e,0)\) are zero-divisors, while their sum \((1,0)\) is a unit. Thus the hypotheses of Chelvam--Asir Conjecture 2.8 are met in the genuinely mixed-prime cases, and the conjectured bound is attained.

## Verification

The proof is symbolic and does not depend on finite enumeration. The accompanying `verify.py` is a stress test of the residue-covering core: for every exponent \(2\le n\le30\), it checks that translates indexed by \(0,\ldots,p-1\) cover all residue classes by nonunits and exhaustively confirms that no smaller family does so in each composite case. Its output is:

```text
VERIFY_OK
checked_exponents=2..30
statement=minimum translate-cover number of nonunits in Z/nZ equals the smallest prime divisor
```

The computational check is corroborative only; the lower bound for arbitrary \(n\) is the Chinese-remainder argument above.

## Relationship to prior work

Axtell and Stickles studied zero-divisor graphs of idealizations, and Anderson and Winders developed the idealization construction systematically. Chelvam and Asir later proved an upper bound for the domination number of the total graph and posed Conjecture 2.8 asserting equality with the minimum finite index of a maximal annihilator ideal in the non-Artinian, non-ideal-zero-divisor setting.

Shariatinia, Maimani, and Yassemi subsequently studied domination of total graphs and idealizations. Their idealization comparison assumes either a torsion-free module or a base ring satisfying \(R=Z(R)\cup U(R)\), and concerns total domination in the idealization. The present family has base ring \(\mathbb Z\) and a nonzero finite torsion module, so neither assumption applies; the parameter proved here is the ordinary domination number. Targeted searches found no prior formula for ordinary domination of \(T_\Gamma(\mathbb Z\ltimes M)\) with finite torsion \(M\).

## Limitations

The theorem is specific to idealizations over \(\mathbb Z\) by finite abelian groups. It does not settle Conjecture 2.8 for arbitrary non-Artinian commutative rings or for idealizations over general domains. The mixed-prime condition is needed only for the statement that \(Z(R)\) is not an ideal; the formula \(\gamma(T_\Gamma(R))=p\) holds for every exponent \(n>1\), including prime powers.

The later 2016 idealization paper was used as a close comparison, not as archive-cohort ownership evidence.

## References

1. M. Axtell and J. Stickles, “Zero-divisor graphs of idealizations,” *Journal of Pure and Applied Algebra* 204 (2006), 235–243. DOI: 10.1016/j.jpaa.2005.04.004.
2. D. D. Anderson and M. Winders, “Idealization of a module,” *Journal of Commutative Algebra* 1 (2009), 3–56. DOI: 10.1216/JCA-2009-1-1-3.
3. T. Tamizh Chelvam and T. Asir, “Domination in the total graph of a commutative ring,” *Journal of Combinatorial Mathematics and Combinatorial Computing* 87 (2013), 147–158.
4. A. Shariatinia, H. R. Maimani, and S. Yassemi, “Domination number of total graphs,” *Mathematica Slovaca* 66 (2016), 1527–1535. DOI: 10.1515/ms-2016-0241.
