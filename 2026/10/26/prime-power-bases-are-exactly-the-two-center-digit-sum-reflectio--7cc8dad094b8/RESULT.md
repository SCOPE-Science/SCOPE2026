# Prime-power bases are exactly the two-center digit-sum reflection bases

## Finding

For a positive integer base \(b\), let \(s_b(u)\) denote the sum of the digits of \(u\) in base \(b\). For a fixed digit-length \(L\) and multiplier \(k\) with \(1\le k<b\), the increment \(s_b(kn)-s_b(n)\) has an exact complement-reflection law under \(n\mapsto b^L-n\). The paired increments have at most two possible totals for every multiplier and length **if and only if \(b\) is a prime power**. In the prime-power case the two exceptional frequencies and corresponding Laurent-polynomial reciprocities are explicit, as is the block mean.

Put \(Q=b^L\), \(F(n)=s_b(kn)-s_b(n)\), and, for positive \(u\), define \(v_b(u)=\max\{j\ge0:b^j\mid u\}\) (valid for composite \(b\), too). Then for each \(1\le n<Q\),
\[
F(n)+F(Q-n)=k-1-(b-1)\bigl(\min\{L,v_b(kn)\}-v_b(n)\bigr).\tag{1}
\]

If \(b=p^a\) for a prime \(p\), set \(c=v_p(k)\), so \(0\le c<a\). The defect in (1) is always \(0\) or \(1\). The number of integers \(1\le n<Q\) with defect \(1\) equals
\[
E_{b,k,L}=\frac{(p^c-1)(b^L-1)}{b-1}.\tag{2}
\]
The paired sums are thus \(k-1\) on the nonexceptional sector and \(k-b\) on the exceptional sector; when \(c=0\) the latter is empty.

Let \(\mathcal E_j\), for \(j\in\{0,1\}\), be the set of \(1\le n<Q\) with defect \(j\), and define the finite Laurent polynomials \(G_j(z)=\sum_{n\in\mathcal E_j}z^{F(n)}\). Then
\[
G_0(z)=z^{k-1}G_0(z^{-1}),\qquad
G_1(z)=z^{k-b}G_1(z^{-1}).\tag{3}
\]
In particular, for \(\gcd(k,b)=1\) the full distribution is reciprocal around \((k-1)/2\). Summing over all \(0\le n<Q\) yields
\[
\sum_{n=0}^{Q-1}\bigl(s_b(kn)-s_b(n)\bigr)
=\frac{(k-p^c)(Q-1)}2.\tag{4}
\]
Thus the exact block mean is \((k-p^c)(1-b^{-L})/2\).

Conversely, every non-prime-power base admits an allowed multiplier and a length-two window with at least three different paired sums. This makes the two-center property a characterization, not merely a feature of prime-power examples.

## Assumptions and scope

All variables are integers: \(b\ge2\), \(L\ge1\), \(1\le k<b\), and \(1\le n<b^L\), except that (4) includes \(n=0\) using \(s_b(0)=0\). This is the first-carry-free range for the leading quotient digits of \(kn\); arbitrary multipliers \(k\ge b\) are not asserted. A prime power includes a prime, so the case \(b=2\) has only \(k=1\) within this range. In (3), Laurent polynomials allow negative exponents because the digit-sum increment can be negative. \(v_p\) is the ordinary prime-adic valuation, distinct from the composite-base trailing-zero valuation \(v_b\).

## Proof

**Base-\(b\) complement lemma.** Let \(0<u<Q=b^L\), and put \(t=v_b(u)\). The lowest \(t\) digits of \(u\) vanish, its next digit is nonzero, and subtraction from \(Q\) gives a complementary next digit and \(b-1\) in every remaining lower position. Hence
\[
s_b(u)+s_b(Q-u)=1+(b-1)(L-t).\tag{5}
\]
This uses trailing zeros only and does not assume the base is prime.

**Pair identity.** Write \(kn=jQ+r\), where \(0\le j<k<b\) and \(0\le r<Q\). If \(r>0\), then \(k(Q-n)=(k-j-1)Q+(Q-r)\). Since the quotient digits \(j\) and \(k-j-1\) are each less than \(b\),
\[
s_b(kn)+s_b(k(Q-n))=k-1+s_b(r)+s_b(Q-r)
=k+(b-1)(L-v_b(r)).
\]
Here \(v_b(r)=v_b(kn)<L\), since \(r\equiv kn\pmod Q\). If \(r=0\), the two numbers are \(jQ\) and \((k-j)Q\) and their digit sums total exactly \(k\); this is the same expression with \(\min\{L,v_b(kn)\}=L\). Subtracting (5) for \(u=n\) proves (1). All boundary cases are covered because \(n\) and \(Q-n\) lie strictly between \(0\) and \(Q\).

**Exactly two prime-power sectors.** Suppose \(b=p^a\). Because \(k<p^a\), \(0\le c=v_p(k)<a\). Write uniquely \(v_p(n)=at+r\) with \(0\le t<L\) and \(0\le r<a\). Then
\[
\min\{L,v_b(kn)\}-v_b(n)
=\left\lfloor\frac{r+c}{a}\right\rfloor,
\]
which is \(1\) precisely for \(a-c\le r<a\). For fixed \(t\), exactly \((p^c-1)p^{a(L-t-1)}\) integers in the range have such valuations: subtract the multiples of \(p^{a(t+1)}\) from the multiples of \(p^{at+a-c}\), with the latter strictly below \(Q\). Summing over \(t=0,\ldots,L-1\) gives
\[
E_{b,k,L}=(p^c-1)\sum_{h=0}^{L-1}p^{ah}
=\frac{(p^c-1)(b^L-1)}{b-1}.
\]
The identity \(v_p(Q-n)=v_p(n)\) for \(0<n<Q\) proves that \(n\mapsto Q-n\) preserves each sector \(\mathcal E_j\). Combining this invariance with (1) and reindexing the sum in \(G_j\) proves (3). Pairing every nonzero \(n\) once (fixed points count correctly because both sides have been summed over all \(n\)) proves
\[
2\sum_{n=1}^{Q-1}F(n)=(k-1)(Q-1)-(b-1)E_{b,k,L}=(k-p^c)(Q-1),
\]
and \(F(0)=0\) gives (4).

**Converse with explicit three-level witnesses.** Suppose \(b\) has at least two distinct prime factors. Choose its least prime divisor \(p\), put \(a=v_p(b)\), and write \(b=p^a m\). Since a distinct prime divisor of \(m\) exceeds \(p\), we have \(m>p\). Set \(k=p^{a+1}<b\) and \(L=2\), so \(Q=b^2\). For the three admissible integers
\[
n_0=1,\qquad n_1=m,\qquad n_2=Q/k=p^{a-1}m^2,
\]
the defects in (1) equal \(0\), \(1\), and \(2\), respectively: \(k\) has no base-\(b\) factor; \(km=pb\) has exactly one such factor whereas \(m\) has none; and \(kn_2=b^2\) has two whereas \(n_2\) has none (its \(p\)-valuation is \(a-1\)). Thus (1) gives three distinct paired sums, completing the equivalence.

## Verification

A standalone pure-Python verifier accompanies this result. It directly evaluates both sides of (1), the exact exceptional counts, the reciprocal sectors and the block sum (4), for the stated bounded test domain, and evaluates the converse witnesses in non-prime-power bases. The output is independent evidence for implementations and finite cases; the universal statements follow from the preceding proof, not from testing. In the analytic check performed before packaging, 12,760,901 direct paired values were compared across bases \(2\) through \(22\) and lengths up to \(4\), with a second direct check of non-prime-power witnesses through base \(50\).

## Relationship to prior work

Dartyge, Luca and Stănică (2009) establish general results on digit sums of multiples, including existence of equal digit-sum multiples and distributional questions associated with sturdy numbers. Their theorem statements and proofs concern those existence and asymptotic questions and do not state the finite-block complement identity, the two reciprocal sectors, or the prime-power characterization above. Their introduction discusses the older binary density results of Stolarsky and Schmidt, which have a different multiplier domain. Dartyge and Tenenbaum (2005) study joint digit-sum distributions via exponential-sum bounds; the accessible article abstract does not resolve the exact finite-block comparison. The novelty assessment is therefore conditional on the accessible literature: it is not a claim that an unlocated equivalent result cannot exist.

## Limitations

The theorem is confined to \(1\le k<b\) and cannot be directly applied to the classical binary \(k=3\) sturdy-number problem. It concerns exact finite-window reflected increments and does not determine full individual frequency distributions or a central-limit theorem. More general published digit-sum distribution theorems, older works on complement identities, or unindexed calculations may already imply some or all statements; in particular, complete text of all older related joint-distribution papers was not inspected. The presented review is not an independent mathematical audit.

## References

1. C. Dartyge, F. Luca and P. Stănică, *On digit sums of multiples of an integer*, Journal of Number Theory **129** (2009), 2820–2830, DOI: 10.1016/j.jnt.2009.04.003, available online May 29, 2009. Author-hosted complete text: https://faculty.nps.edu/pstanica/research/2009JNT_digit-sums-multiple.pdf.
2. C. Dartyge and G. Tenenbaum, *Sommes des chiffres de multiples d'entiers*, Annales de l'Institut Fourier **55** (2005), 2423–2474, DOI: 10.5802/aif.2166, https://www.numdam.org/item/AIF_2005__55_7_2423_0/.
3. K. B. Stolarsky, *Integers whose multiples have anomalous digital frequencies*, Acta Arithmetica **38** (1980), 117–128 (historical reference cited in [1]).
