# A dyadic phase law for hypercubical hyperdeterminant degrees
## Finding
For every integer
\[
d\ge2,
\]
let \(H_d\) be the degree of the hyperdeterminant of format
\[
2^{\times d},
\]
equivalently the degree of the projective dual hypersurface of the Segre variety
\[
X_d=(\mathbb P^1_{\mathbb C})^d.
\]
Let \(s_2(d)\) denote the number of \(1\)'s in the binary expansion of \(d\). Then
\[
\nu_2(H_d)=d-s_2(d)
\]
when \(d\) is even,
\[
\nu_2(H_d)=d-s_2(d)+1
\]
when
\[
d\equiv3\pmod4,
\]
and
\[
\nu_2(H_d)\ge d-s_2(d)+2
\]
when
\[
d\equiv1\pmod4.
\]

The Frobenius Euclidean-distance degree of the same Segre variety is
\[
\operatorname{EDdeg}_F(X_d)=d!,
\]
so Legendre's formula
\[
\nu_2(d!)=d-s_2(d)
\]
turns the result into a geometric comparison:
\[
\nu_2(H_d)-\nu_2(\operatorname{EDdeg}_F(X_d))
=
0
\]
for even \(d\),
\[
\nu_2(H_d)-\nu_2(\operatorname{EDdeg}_F(X_d))
=
1
\]
for
\[
d\equiv3\pmod4,
\]
and the difference is at least \(2\) for
\[
d\equiv1\pmod4.
\]

Thus the first two dyadic layers of the two natural degrees are governed solely by the residue class of the tensor order.

## Assumptions and scope
The Segre variety is over \(\mathbb C\) and uses the standard Segre embedding. For \(d\ge2\), its dual is a hypersurface, whose defining polynomial is the hyperdeterminant of format \(2^{\times d}\).

The statement determines the full two-adic valuation for even \(d\) and for \(d\equiv3\pmod4\). In the remaining class \(d\equiv1\pmod4\), it proves a uniform two-step excess above the factorial baseline but does not claim the higher valuation is constant.

The Euclidean-distance degree comparison uses the Frobenius inner product, not the generic ED degree.

## Proof
The classical generating function for hypercubical hyperdeterminant degrees is
\[
\sum_{d\ge0}H_d\frac{x^d}{d!}
=
e^{-2x}(1-x)^{-2}.
\]
Extracting the coefficient of \(x^d\) gives
\[
H_d
=
d!\,A_d,
\qquad
A_d
=
\sum_{j=0}^{d}(d-j+1)\frac{(-2)^j}{j!}.
\]

We analyze \(A_d\) in the \(2\)-adic integers. Legendre's formula gives
\[
\nu_2(j!)=j-s_2(j),
\]
hence
\[
\nu_2\!\left(\frac{2^j}{j!}\right)=s_2(j).
\]
In particular, every summand with \(j\ge1\) has at least one factor of \(2\) in the \(2\)-adic sense.

Suppose first that \(d\) is even. The \(j=0\) term is
\[
d+1,
\]
which is odd, while every term with \(j\ge1\) is even. Therefore
\[
A_d\equiv1\pmod2,
\]
so
\[
\nu_2(A_d)=0.
\]
Consequently
\[
\nu_2(H_d)=\nu_2(d!)=d-s_2(d).
\]

Now suppose that \(d\) is odd. For every \(j\ge2\), the \(j\)-th term has \(2\)-adic valuation at least \(2\). Indeed, if \(j\) is even, then
\[
d-j+1
\]
is even and \(s_2(j)\ge1\). If \(j\ge3\) is odd, then \(s_2(j)\ge2\). Hence modulo \(4\) only the terms \(j=0\) and \(j=1\) survive:
\[
A_d
\equiv
(d+1)-2d
=
1-d
\pmod4.
\]

If
\[
d\equiv3\pmod4,
\]
then
\[
1-d\equiv2\pmod4,
\]
so
\[
\nu_2(A_d)=1.
\]
Thus
\[
\nu_2(H_d)=d-s_2(d)+1.
\]

If
\[
d\equiv1\pmod4,
\]
then
\[
1-d\equiv0\pmod4,
\]
so
\[
\nu_2(A_d)\ge2,
\]
and therefore
\[
\nu_2(H_d)\ge d-s_2(d)+2.
\]

The cited Segre-product computation also gives
\[
\operatorname{EDdeg}_F(X_d)=d!,
\]
which yields the equivalent comparison with the Frobenius ED degree.

## Verification
The bundled exact checker constructs \(H_d\) from the recurrence implied by the generating function,
\[
H_{d+1}=d\bigl(H_d+2H_{d-1}\bigr),
\]
with
\[
H_0=1,
\qquad
H_1=0.
\]
It independently checks the coefficient-sum formula using exact rational arithmetic on an initial range, and then checks the claimed valuation law over a much larger range.

For the first few nontrivial tensor orders,
\[
H_2=2,\quad
H_3=4,\quad
H_4=24,\quad
H_5=128,\quad
H_6=880,\quad
H_7=6816,\quad
H_8=60032,\quad
H_9=589312.
\]
Their excess valuations above \(\nu_2(d!)\) are respectively
\[
0,1,0,4,0,1,0,2,
\]
consistent with the theorem.

These finite calculations are regression evidence only. The infinite result is the direct \(2\)-adic argument above.

## Relationship to prior work
Gel'fand, Kapranov, and Zelevinsky established the generating function for degrees of hyperdeterminants. A modern full-text treatment by Ottaviani, Sodomaco, and Ventura reproduces that generating function, specializes it to
\[
(\mathbb P^1)^d,
\]
derives the exact coefficient formula used here, and separately records
\[
\operatorname{EDdeg}_F((\mathbb P^1)^d)=d!.
\]

Kohn's work identifies hyperdeterminants as equations of coisotropic hypersurfaces of Segre varieties and supplies an archival algebraic-geometric source for the duality framework.

A public sequence record for these degrees lists the same exponential generating function, exact coefficient formula, recurrence, and initial values. It also records a general divisibility theorem for permanents of sign matrices, but that bound is weaker than the residue-sensitive valuation law proved here.

Claim-specific searches for \(2\)-adic valuations, parity, divisibility by powers of two, the sequence identifier, and equivalent factorial-baseline formulations did not locate the three-case theorem above.

## Limitations
For
\[
d\equiv1\pmod4,
\]
the result gives only the first guaranteed excess of two powers of \(2\). The additional valuation varies with \(d\); for example the excess is \(4\) at \(d=5\), \(2\) at \(d=9\), and \(7\) at \(d=13\).

The proof uses the classical degree generating function as input. It does not give a direct intersection-theoretic explanation for the residue classes.

The original 1992 hyperdeterminant paper is a plausible place for arithmetic corollaries of the degree formula, but its full text was not available for claim-level inspection in this run. The later full-text source reproduces the exact formula, and no inspected source states the valuation theorem; nevertheless an older unindexed statement remains the principal originality risk.

## References
I. M. Gel'fand, M. M. Kapranov, and A. V. Zelevinsky, *Hyperdeterminants*, Advances in Mathematics 96 (1992), 226--263. DOI: 10.1016/0001-8708(92)90056-Q.

Kathlén Kohn, *Coisotropic Hypersurfaces in Grassmannians*, arXiv:1607.05932, first submitted 20 July 2016.

Giorgio Ottaviani, Luca Sodomaco, and Emanuele Ventura, *Asymptotics of degrees and ED degrees of Segre products*, arXiv:2008.11670; Advances in Applied Mathematics 130 (2021), 102242.

OEIS A087981, sequence record for the degrees of hyperdeterminants of multilinear forms on \((\mathbb P^1)^d\).
