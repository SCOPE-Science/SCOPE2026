# A mod-four law for Euler characteristics of stable pointed rational curves
## Finding
For every integer
\[
n\ge3,
\]
let
\[
c_n=\chi_{\mathrm{top}}(\overline{\mathcal M}_{0,n}),
\]
where \(\overline{\mathcal M}_{0,n}\) is the Deligne--Mumford moduli space of stable \(n\)-pointed genus-zero curves over \(\mathbb C\).

Then
\[
\boxed{
c_n\equiv
\begin{cases}
1\pmod4,&n\equiv3\pmod4,\\
2\pmod4,&n\text{ even},\\
3\pmod4,&n\equiv1\pmod4.
\end{cases}}
\]
Equivalently,
\[
\boxed{
\nu_2(c_n)=
\begin{cases}
0,&n\text{ odd},\\
1,&n\text{ even}.
\end{cases}}
\]
Thus no Euler characteristic in the genus-zero stable-pointed tower is divisible by \(4\).

The first values
\[
1,2,7,34,213,1630,14747,153946,1821473,\ldots
\]
for \(n=3,4,\ldots\) already display this rigid mod-four cycle, but the result is proved for all \(n\).

## Assumptions and scope
The base field is \(\mathbb C\), and the Euler characteristic is the ordinary topological Euler characteristic. Since \(\overline{\mathcal M}_{0,n}\) is smooth and projective, no compact-support convention is needed.

The classical input is Getzler's inversion relation between the Euler-characteristic exponential generating functions of \(\mathcal M_{0,n}\) and \(\overline{\mathcal M}_{0,n}\). McMullen gives an elementary stable-tree proof of the same relation and records
\[
\chi(\mathcal M_{0,n+1})=(-1)^n(n-2)!.
\]

The statement concerns only total Euler characteristics, not individual Betti numbers or the equivariant cohomology representations.

## Proof
Set
\[
b_m=\chi(\overline{\mathcal M}_{0,m+1}),
\qquad m\ge2,
\]
and define
\[
g(x)=x+\sum_{m\ge2}b_m\frac{x^m}{m!}.
\]
Getzler's inversion formula, together with
\[
\chi(\mathcal M_{0,m+1})=(-1)^m(m-2)!,
\]
says that \(g\) is the compositional inverse of
\[
f(x)=x-\sum_{m\ge2}(-1)^m(m-2)!\frac{x^m}{m!}.
\]
Summing the elementary series gives
\[
f(x)=2x-(1+x)\log(1+x).
\]
Hence
\[
f(g(x))=x.
\]
Differentiation yields
\[
g'(x)=\frac{1}{1-\log(1+g(x))}.
\]
Eliminating the logarithm by means of \(x=2g-(1+g)\log(1+g)\) gives
\[
g'(x)=\frac{1+g(x)}{1+x-g(x)}.
\]
Put
\[
h(x)=g(x)-x=\sum_{m\ge2}b_m\frac{x^m}{m!}.
\]
Then
\[
h'=x+2h+hh'.
\]
Comparing coefficients gives
\[
\boxed{
b_{m+1}=2b_m+\sum_{k=2}^{m-1}\binom{m}{k}b_kb_{m-k+1}}
\]
for \(m\ge2\), with \(b_2=1\).

We prove by induction that for every \(r\ge1\),
\[
\boxed{b_{2r}\equiv(-1)^{r+1}\pmod4},
\qquad
\boxed{b_{2r+1}\equiv2\pmod4}.
\]
The initial values are \(b_2=1\) and \(b_3=2\).

First take \(m=2r\). The term \(2b_m\) is congruent to \(2\pmod4\). In the convolution, every odd \(k\) gives a factor \(b_k\equiv2\pmod4\), while \(\binom{2r}{k}\) is even, so those terms vanish modulo \(4\). For even \(k\), the other \(b\)-factor has odd index and is \(2\pmod4\). Such a term can contribute \(2\pmod4\) only when \(\binom{2r}{k}\) is odd. By Lucas's theorem, all odd binomial entries in an even row occur at even \(k\), and their total number is
\[
2^{s_2(2r)}.
\]
After excluding the endpoints \(k=0,2r\), their number is
\[
2^{s_2(2r)}-2,
\]
which is even. Hence the whole convolution vanishes modulo \(4\), and
\[
b_{2r+1}\equiv2\pmod4.
\]

Now take \(m=2r+1\). The leading term \(2b_m\) vanishes modulo \(4\). If \(k\) is odd, both \(b\)-factors are \(2\pmod4\), so the product vanishes modulo \(4\). If \(k=2a\), the induction hypothesis gives
\[
b_{2a}b_{2(r-a+1)}\equiv(-1)^{r+1}\pmod4,
\]
independent of \(a\). Therefore the convolution is
\[
(-1)^{r+1}\sum_{a=1}^{r}\binom{2r+1}{2a}\pmod4.
\]
The sum of all even-indexed binomial coefficients in row \(2r+1\) is \(2^{2r}\), so
\[
\sum_{a=1}^{r}\binom{2r+1}{2a}=2^{2r}-1\equiv-1\pmod4.
\]
Thus
\[
b_{2r+2}\equiv(-1)^r\pmod4,
\]
which is exactly the claimed even-index formula at \(r+1\).

Finally, \(c_n=b_{n-1}\). Translating the two congruences gives the stated three residue classes modulo \(4\).

## Verification
The bundled checker constructs the exact integers \(b_m\) from the recurrence through \(m=150\). It verifies the mod-four theorem term by term.

Independently, it represents the truncated exponential series with exact rational coefficients and checks that the resulting \(g\) satisfies
\[
f(g(x))=x
\]
through the full truncation range. The initial values agree with the published sequence
\[
1,2,7,34,213,1630,14747,153946,1821473.
\]

These finite checks are regression evidence only. The all-\(n\) theorem follows from the symbolic recurrence and induction above.

## Relationship to prior work
Getzler's operadic study of genus-zero moduli spaces contains the inversion theorem relating the Poincare/Euler data of \(\mathcal M_{0,n}\) and \(\overline{\mathcal M}_{0,n}\). McMullen later gives a short stable-tree proof and explicitly records the Euler sequence and the compositional inverse relation.

A recent paper of Aluffi, Marcolli, and Nascimento gives explicit formulas for the Grothendieck classes and Betti numbers of \(\overline{\mathcal M}_{0,n}\), and discusses its Euler characteristic in detail. Its inspected Euler section gives the differential equation for the generating function and a Stirling-number formula, but targeted full-text searches found no parity, mod-four, two-adic, or divisibility statement.

Targeted literature searches using \(\overline{\mathcal M}_{0,n}\), Euler characteristic, parity, mod \(4\), and two-adic valuation did not locate the congruence classification above. The new step is the reduction of the inversion equation to an integral recurrence whose convolution collapses modulo \(4\).

## Limitations
The theorem determines only the exact power of \(2\) dividing the total Euler characteristic. It does not give odd-prime valuations or congruences of individual Betti numbers.

The proof is elementary once the classical inversion formula is available, so an older or unindexed combinatorial source may contain the same congruence without moduli-space terminology.

No analogous claim is made here for positive-genus Deligne--Mumford spaces.

## References
Ezra Getzler, *Operads and moduli spaces of genus 0 Riemann surfaces*, arXiv:alg-geom/9411004, first submitted 9 November 1994; in *The Moduli Space of Curves*, Progress in Mathematics 129 (1995), 199--230.

Curtis T. McMullen, *Moduli spaces in genus zero and inversion of power series*, *L'Enseignement Mathematique* 60 (2014), 25--30, DOI 10.4171/LEM/60-1/2-2; manuscript dated 1 October 2012.

Paolo Aluffi, Matilde Marcolli, and Eduardo Nascimento, *Explicit formulas for the Grothendieck class of \(\overline{\mathcal M}_{0,n}\)*, *Moduli* 2 (2025), e19, DOI 10.1112/mod.2025.10012.
