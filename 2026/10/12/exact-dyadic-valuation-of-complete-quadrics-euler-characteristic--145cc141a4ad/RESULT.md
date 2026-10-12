# Exact dyadic valuation of complete-quadrics Euler characteristics
## Finding
Let
\[
\overline{\mathcal Q}_n
\]
be the complex variety of complete quadrics on an \(n\)-dimensional vector space, with
\[
n\ge1.
\]
Let
\[
s_2(n)
\]
denote the number of ones in the binary expansion of \(n\), and let
\[
\nu_2(m)
\]
denote the exponent of \(2\) in a positive integer \(m\).

Then
\[
\boxed{
\nu_2\!\left(\chi_{\mathrm{top}}(\overline{\mathcal Q}_n)\right)
=
\left\lceil\frac n2\right\rceil-s_2(n)
+
\begin{cases}
\nu_2(n+1),&n\equiv3\pmod4,\\
0,&n\not\equiv3\pmod4.
\end{cases}
}
\]

In particular,
\[
\boxed{
\chi_{\mathrm{top}}(\overline{\mathcal Q}_n)\ \text{is odd}
\iff
n\in\{1,2\}.
}
\]

The first values of the Euler characteristic are
\[
1,\ 3,\ 12,\ 66,\ 450,\ 3690,\ 35280,\ldots
\]
for
\[
n=1,2,3,4,5,6,7,\ldots,
\]
and the corresponding two-adic valuations are
\[
0,\ 0,\ 2,\ 1,\ 1,\ 1,\ 4,\ldots.
\]

The extra term at
\[
n\equiv3\pmod4
\]
is a genuine dyadic spike: its size is exactly the two-adic order of \(n+1\).

## Assumptions and scope
The base field is \(\mathbb C\).

The indexing convention is that \(\overline{\mathcal Q}_n\) compactifies nondegenerate quadratic forms on an \(n\)-dimensional vector space, equivalently smooth quadrics in \(\mathbb P^{n-1}\), up to scale.

The classical variety of complete quadrics can be constructed by successively blowing up the projective space of quadratic forms along the rank strata. It is smooth and projective.

The result concerns the ordinary topological Euler characteristic. The exact formula for that Euler characteristic is a known fixed-point count; the new statement proved here is its exact two-adic valuation in every dimension.

## Proof
A known torus-fixed-point computation gives
\[
\chi_{\mathrm{top}}(\overline{\mathcal Q}_n)
=
n!\,
\frac{(1+\sqrt3)^{n+1}-(1-\sqrt3)^{n+1}}
{2^{n+1}\sqrt3}.
\]
Equivalently, if
\[
U_m
=
\frac{(1+\sqrt3)^m-(1-\sqrt3)^m}{2\sqrt3},
\]
then
\[
\chi_{\mathrm{top}}(\overline{\mathcal Q}_n)
=
\frac{n!}{2^n}U_{n+1}.
\]

The sequence \(U_m\) satisfies
\[
U_0=0,
\qquad
U_1=1,
\qquad
U_m=2U_{m-1}+2U_{m-2}.
\]

We first prove the exact auxiliary valuation
\[
\boxed{
\nu_2(U_m)
=
\left\lfloor\frac m2\right\rfloor
+
\begin{cases}
\nu_2(m),&4\mid m,\\
0,&4\nmid m.
\end{cases}
}
\qquad(m\ge1).
\]

The standard binomial expansion for this Lucas sequence is
\[
U_m
=
\sum_{j=0}^{\lfloor(m-1)/2\rfloor}
\binom{m-j-1}{j}2^{m-j-1}.
\]
For odd index
\[
m=2r+1,
\]
the last summand is exactly \(2^r\), while every earlier summand is divisible by \(2^{r+1}\). Hence
\[
\nu_2(U_{2r+1})=r.
\]

Introduce the companion sequence
\[
V_m=(1+\sqrt3)^m+(1-\sqrt3)^m.
\]
For odd index
\[
m=2r+1,
\]
its binomial expansion has lowest-power term
\[
(2r+1)2^{r+1},
\]
so
\[
\nu_2(V_{2r+1})=r+1.
\]

For even indices use
\[
V_{2r}=V_r^2-2(-2)^r.
\]
The binomial expansion of \(V_{2s}\) shows at once that
\[
2^{s+1}\mid V_{2s}.
\]
If \(r\) is even, the first term \(V_r^2\) is therefore divisible by at least
\[
2^{r+2},
\]
whereas the second term has exact valuation \(r+1\). Thus
\[
\nu_2(V_{2r})=r+1
\qquad(r\ \text{even}).
\]

If \(r\) is odd, then
\[
\nu_2(V_r)=\frac{r+1}{2}.
\]
After division of
\[
V_{2r}=V_r^2+2^{r+1}
\]
by \(2^{r+1}\), the first quotient is the square of an odd number. Every odd square is congruent to \(1\) modulo \(8\), so the normalized sum is congruent to \(2\) modulo \(8\). Therefore
\[
\nu_2(V_{2r})=r+2
\qquad(r\ \text{odd}).
\]

Finally,
\[
U_{2r}=U_rV_r.
\]
Strong induction on \(r\), using the odd-index formula for \(U_r\) and the just-proved formulas for \(V_r\), gives
\[
\nu_2(U_{2r})
=
\begin{cases}
r,&r\ \text{odd},\\
r+\nu_2(2r),&r\ \text{even}.
\end{cases}
\]
Together with the odd-index case this is precisely the boxed auxiliary formula.

Now Legendre's identity gives
\[
\nu_2(n!)=n-s_2(n).
\]
Hence
\[
\nu_2\!\left(\chi_{\mathrm{top}}(\overline{\mathcal Q}_n)\right)
=
\nu_2(U_{n+1})+\nu_2(n!)-n
=
\nu_2(U_{n+1})-s_2(n).
\]

If \(n\) is even, then \(n+1\) is odd and
\[
\nu_2(U_{n+1})=\frac n2.
\]
If
\[
n\equiv1\pmod4,
\]
then
\[
n+1\equiv2\pmod4
\]
and
\[
\nu_2(U_{n+1})=\frac{n+1}{2}.
\]
If
\[
n\equiv3\pmod4,
\]
then
\[
4\mid n+1
\]
and
\[
\nu_2(U_{n+1})
=
\frac{n+1}{2}+\nu_2(n+1).
\]
These three cases yield the claimed formula.

For the parity corollary, \(n=1,2\) give valuation zero directly. If \(n\ge4\) is even, write \(n=2m\) with \(m\ge2\); then
\[
\frac n2-s_2(n)
=
m-s_2(m)\ge1.
\]
If \(n\ge5\) and \(n\equiv1\pmod4\), write
\[
n=2m+1
\]
with \(m\ge2\); then
\[
s_2(n)=s_2(m)+1
\]
and again the valuation is
\[
m-s_2(m)\ge1.
\]
For
\[
n\equiv3\pmod4,
\]
the additional term is positive, including \(n=3\). Thus no further odd cases occur.

## Verification
The bundled checker computes the Euler-characteristic sequence from its published recurrence
\[
\kappa(n)
=
n\kappa(n-1)+\binom n2\kappa(n-2),
\qquad
\kappa(0)=\kappa(1)=1.
\]

For every
\[
1\le n\le1000,
\]
it compares the exact two-adic valuation of \(\kappa(n)\) with the closed formula above.

Independently, it computes the Lucas sequence
\[
U_m=2U_{m-1}+2U_{m-2}
\]
and verifies the auxiliary valuation formula through
\[
1\le m\le1001.
\]

These computations are regression evidence only. The infinite statement follows from the symbolic Lucas-sequence argument and Legendre's factorial valuation formula.

## Relationship to prior work
The variety of complete quadrics is classical. An archival algebraic-geometry source describes it as an iterated blowup of the projective space of quadrics along the rank loci and studies its birational geometry.

Later work identifies torus fixed points with barred permutations and derives the recurrence
\[
\kappa(n)
=
n\kappa(n-1)+\binom n2\kappa(n-2).
\]
A subsequent complete-quadrics paper explicitly records both the closed form for \(\kappa(n)\) and the fact that this sequence is the Euler characteristic of the variety.

The same integer sequence is catalogued as OEIS A080599. Its normalization uses the Lucas sequence OEIS A002605, which in turn factors as
\[
2^{\lfloor m/2\rfloor}
\]
times OEIS A002530, the denominator sequence for convergents to \(\sqrt3\).

The inspected geometric papers and all three relevant sequence records state recurrences, closed forms, combinatorial interpretations, or continued-fraction identities, but do not state the exact two-adic valuation proved here. Targeted searches for the valuation in complete-quadrics, barred-permutation, Lucas-sequence, and \(\sqrt3\)-convergent language did not locate an equivalent formula.

## Limitations
The theorem determines only the power of \(2\) dividing the Euler characteristic. It does not describe the odd part.

The number-theoretic auxiliary sequence is a classical Lucas or Lehmer-type sequence. General valuation theorems for such sequences may subsume the auxiliary lemma in a different notation even though no covering statement was located. The complete-quadrics specialization and the final binary-digit formula were separately checked against the relevant geometric and sequence sources.

No claim is made about odd-prime valuations of the Euler characteristic.

## References
César Lozano Huerta, *Birational Geometry of the Space of Complete Quadrics*, arXiv:1401.8050, first submitted 31 January 2014.

Soumya Banerjee, Mahir Bilen Can, and Michael Joyce, *Combinatorial Models for the Variety of Complete Quadrics*, arXiv:1610.02698, first submitted 9 October 2016.

Mateusz Michałek, Leonid Monin, and Jarosław A. Wiśniewski, *Maximum likelihood degree, complete quadrics and \(\mathbb C^*\)-action*, arXiv:2004.07735, first submitted 16 April 2020; *SIAM Journal on Applied Algebra and Geometry* 5 (2021), 60--85.

OEIS Foundation Inc., sequence A080599, the Euler-characteristic sequence for complete quadrics.

OEIS Foundation Inc., sequence A002605, the recurrence \(U_m=2U_{m-1}+2U_{m-2}\).

OEIS Foundation Inc., sequence A002530, denominators of convergents to \(\sqrt3\).
