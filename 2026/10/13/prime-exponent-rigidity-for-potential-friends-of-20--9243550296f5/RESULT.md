# Prime-exponent rigidity for potential friends of 20

## Finding
Let \(N\) be a friend of \(20\), meaning
\[
N\ne20,
\qquad
\frac{\sigma(N)}{N}=\frac{21}{10}.
\]
Then every prime \(r\equiv1\pmod 3\) dividing \(N\) satisfies
\[
\nu_r(N)\equiv0\ \text{or}\ 4\pmod 6.
\]
Equivalently, no such prime occurs with exponent congruent to \(2\pmod6\).

There is a stronger consequence in the minimal \(5\)-adic layer. If
\[
\nu_5(N)=2,
\]
then
\[
31^6\mid N.
\]
Thus the exponent of \(31\) is not merely positive or even: it is at least \(6\).

## Assumptions and scope
The divisor-sum function is \(\sigma\), and \(\nu_p\) denotes the usual \(p\)-adic valuation on positive integers.

The proof uses the published structural facts that every friend \(N\) of \(20\) has the form
\[
N=2\cdot5^{2a}m^2,
\qquad
\gcd(N,21)=1,
\]
with \(a\ge1\), and hence every odd prime exponent in \(N\) is even. These facts are independently restated in the proof below only as hypotheses imported from the cited source; the new work is the mod-\(6\) restriction and the forced \(31^6\) consequence.

No claim is made that a friend of \(20\) exists.

## Proof
Write the odd prime-power part of a hypothetical friend as
\[
N=2\cdot5^{2a}\prod_i p_i^{2a_i},
\]
where none of the \(p_i\) equals \(3\), \(5\), or \(7\). The abundancy equation
\[
10\sigma(N)=21N
\]
and \(\sigma(2)=3\) give, after cancellation of the factor \(3\),
\[
\sigma(5^{2a})\prod_i\sigma(p_i^{2a_i})
=
7\cdot5^{2a-1}\prod_i p_i^{2a_i}.
\tag{1}
\]
Because \(3\nmid N\), the right-hand side of (1) is not divisible by \(3\). Consequently none of the individual positive factors on the left can be divisible by \(3\).

Let \(r\equiv1\pmod3\) be a prime divisor of \(N\). Its exponent is even, say
\[
\nu_r(N)=2e.
\]
Reducing its geometric divisor sum modulo \(3\) yields
\[
\sigma(r^{2e})
=
1+r+\cdots+r^{2e}
\equiv
2e+1
\pmod3.
\]
Equation (1) shows \(3\nmid\sigma(r^{2e})\), so
\[
2e+1\not\equiv0\pmod3.
\]
Hence \(e\not\equiv1\pmod3\). Multiplying by \(2\), the only possible residues of \(2e\) modulo \(6\) are
\[
0\quad\text{and}\quad4.
\]
This proves the general exponent restriction.

Now assume
\[
\nu_5(N)=2.
\]
Then \(a=1\), and
\[
\sigma(5^2)=31.
\]
Equation (1) therefore forces \(31\mid N\), because \(31\) is neither \(5\) nor \(7\). Since
\[
31\equiv1\pmod3,
\]
the first part gives
\[
\nu_{31}(N)\equiv0\ \text{or}\ 4\pmod6.
\]
The least positive possibilities are therefore \(4\) and \(6\).

Suppose for contradiction that
\[
\nu_{31}(N)=4.
\]
An exact factorization is
\[
\sigma(31^4)
=1+31+31^2+31^3+31^4
=954305
=5\cdot11\cdot17351,
\]
and \(17351\) is prime. From (1), both \(11\) and \(17351\) must divide \(N\). Every odd prime exponent of \(N\) is even, so
\[
2\cdot5^2\cdot31^4\cdot11^2\cdot17351^2
\mid N.
\]
The abundancy index is nondecreasing under divisibility. For this forced divisor its exact value is
\[
I\!\left(2\cdot5^2\cdot31^4\cdot11^2\cdot17351^2\right)
=
\frac{120128746647}{56859400510}.
\]
Moreover,
\[
\frac{120128746647}{56859400510}-\frac{21}{10}
=
\frac{362002788}{28429700255}>0.
\]
Therefore \(I(N)>21/10\), contradicting that \(N\) is a friend of \(20\). Thus \(\nu_{31}(N)\ne4\), and the smallest remaining positive residue-compatible exponent is \(6\). Hence
\[
31^6\mid N.
\]

## Verification
The accompanying `verify.py` performs exact integer and rational checks of the nonstandard arithmetic used in the proof. It verifies that \(17351\) is prime by trial division, factors \(\sigma(31^4)\) exactly as
\[
5\cdot11\cdot17351,
\]
and reproduces the exact abundancy comparison above.

As a local regression test, it also checks every prime \(r\le10000\) with \(r\equiv1\pmod3\) and every even exponent \(2\le e\le30\), confirming
\[
3\mid\sigma(r^e)
\quad\Longleftrightarrow\quad
e\equiv2\pmod6.
\]
This finite test is not the proof of the all-prime congruence; that proof is the one-line geometric-sum reduction above.

## Relationship to prior work
Chatterjee, Mandal, and Mandal prove that a friend of \(20\), if one exists, has the form
\[
2\cdot5^{2a}m^2,
\qquad
\gcd(N,21)=1,
\]
and has at least six distinct prime factors. Their Theorem 4 gives a different exponent obstruction involving the multiplicative order of \(5\) modulo an auxiliary prime and a condition on \(\nu_5(N)\). Their Corollary 6 shows that if \(N=2F^2\) is a friend of \(20\), then \(F\) is not squarefree.

The present result is pointwise in every prime \(r\equiv1\pmod3\): it excludes the residue class \(2\pmod6\) for \(\nu_r(N)\), independently of the order of \(5\) modulo \(r\) and independently of \(\nu_5(N)\). In the minimal layer \(\nu_5(N)=2\), it strengthens the nonsquarefree conclusion by proving the concrete divisibility
\[
31^6\mid N.
\]

Haenel and Wood earlier proved for friends of \(20\) that \(2\) and \(5\) divide \(N\), \(3\) and \(7\) do not, and every odd prime exponent is even. Their Section 5 does not state the mod-\(6\) restriction or the forced lower bound on \(\nu_{31}(N)\).

Targeted searches for friends of \(20\), exponent congruences modulo \(6\), the phrase \(\nu_{31}\), the factorization of \(\sigma(31^4)\), and the bound \(\nu_{31}(N)\ge6\) did not locate an implication-equivalent result.

## Limitations
The theorem is conditional on the existence of a friend of \(20\); no such friend is currently known. It does not rule out the possibility that \(20\) is solitary.

The special bound \(31^6\mid N\) assumes the minimal case \(\nu_5(N)=2\). For larger \(5\)-adic exponent, the forced cyclotomic factors of \(\sigma(5^{2a})\) vary and are not classified here.

The general mod-\(6\) restriction is elementary once equation (1) and \(3\nmid N\) are available. Its value lies in applying that local rigidity uniformly to every prime \(r\equiv1\pmod3\) and combining it with a forced-factor abundancy argument to obtain the stronger \(31^6\) consequence.

## References
1. Tapas Chatterjee, Sagar Mandal, and Sourav Mandal, “On Characterizing Potential Friends of 20,” arXiv:2409.04451. First public version submitted 25 August 2024; current version also published in Annals of West University of Timisoara, Mathematics and Computer Science 61(1) (2025), 205–229.
2. Justin Haenel and Carson Wood, “Friends of Products of Two Primes and of Four Times an Odd Prime,” International Journal of Mathematics and Computer Science 14(4) (2019), 965–974.
