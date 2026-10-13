# Fixed-prime-factor law for non-arithmetic squarefree numbers
## Finding
For an integer \(n\), write
\[
A(n)=\frac{\sigma(n)}{\tau(n)}.
\]
Call \(n\) arithmetic when \(A(n)\) is an integer.

Fix an integer \(r\ge2\). Let \(E_r(x)\) be the number of squarefree integers
\(n\le x\) having exactly \(r\) prime factors and not arithmetic, and let \(S_r(x)\)
be the number of all squarefree integers \(n\le x\) having exactly \(r\) prime
factors. Then
\[
E_r(x)\sim
\frac{x(\log\log x)^{r-2}}{2^r(r-2)!\log x}.
\]
Since Landau's theorem gives
\[
S_r(x)\sim
\frac{x(\log\log x)^{r-1}}{(r-1)!\log x},
\]
it follows that
\[
\frac{E_r(x)}{S_r(x)}
\sim
\frac{r-1}{2^r\log\log x}.
\]

Thus, in every fixed squarefree prime-factor layer, arithmetic numbers have
relative density \(1\), and the exceptional proportion has an explicit
first-order decay law.

## Assumptions and scope
The number of prime factors is counted without multiplicity; because every
integer under consideration is squarefree, this is also the number counted
with multiplicity.

The result is for each fixed \(r\) as \(x\to\infty\). It does not assert
uniformity when \(r\) grows with \(x\).

Two prior theorems are used.

First, Ore's squarefree characterization, as explicitly recalled by
Oller-Marcén, says that every odd squarefree integer is arithmetic, whereas an
even squarefree integer is arithmetic if and only if at least one of its odd
prime divisors is congruent to \(3\pmod4\).

Second, Prabhu's fixed-prime-factoresidue refinement of Landau's theorem says that for a
fixed modulus \(N\), a fixed \(k\)-tuple of reduced residue classes modulo \(N\),
and fixed \(k\ge2\), the number of squarefree products of \(k\) distinct primes
occupying those residue classes is asymptotic to
\[
\frac1{\varphi(N)^k}
\frac{X(\log\log X)^{k-1}}{(k-1)!\log X}.
\]
For \(k=1\), the corresponding statement is the prime number theorem in
arithmetic progressions.

## Proof
By Ore's characterization, a squarefree non-arithmetic integer must be even.
Write it as
\[
n=2m.
\]
If \(n\) has exactly \(r\) prime factors, then \(m\) is odd and squarefree with
exactly \(r-1\) prime factors. Moreover,
\[
n\text{ is non-arithmetic}
\quad\Longleftrightarrow\quad
p\equiv1\pmod4\quad\text{for every prime }p\mid m.
\]
Consequently,
\[
E_r(x)=
\#\left\{
m\le\frac x2:
m\text{ squarefree},\
\omega(m)=r-1,\
p\mid m\Rightarrow p\equiv1\pmod4
\right\}.
\]

Put \(k=r-1\). When \(k\ge2\), apply Prabhu's residue-class theorem with
\[
N=4,\qquad (m_1,\ldots,m_k)=(1,\ldots,1).
\]
Because
\[
\varphi(4)=2,
\]
the restricted squarefree count at height \(X\) is
\[
\sim
\frac1{2^k}
\frac{X(\log\log X)^{k-1}}{(k-1)!\log X}.
\]
Taking
\[
X=\frac x2
\]
and using
\[
\log(x/2)\sim\log x,\qquad
\log\log(x/2)\sim\log\log x,
\]
gives
\[
E_r(x)\sim
\frac{x(\log\log x)^{r-2}}
{2^r(r-2)!\log x}.
\]

For \(r=2\), the same calculation uses only the prime number theorem in the
progression \(1\pmod4\):
\[
E_2(x)=\pi(x/2;4,1)
\sim\frac{x}{4\log x},
\]
which agrees with the displayed formula.

Finally, Landau's squarefree \(r\)-almost-prime theorem gives
\[
S_r(x)\sim
\frac{x(\log\log x)^{r-1}}{(r-1)!\log x}.
\]
Dividing the two asymptotics yields
\[
\frac{E_r(x)}{S_r(x)}
\sim
\frac{r-1}{2^r\log\log x}.
\]

## Verification
The accompanying checker enumerates all squarefree integers through a fixed
finite cutoff, computes \(\sigma(n)/\tau(n)\) directly from the prime
factorization, and verifies the exact Ore criterion on every tested squarefree
integer.

It also tabulates \(E_r(x)\) for several fixed \(r\) and compares the finite
counts with
\[
\frac{x(\log\log x)^{r-2}}{2^r(r-2)!\log x}.
\]
The finite ratios converge slowly, as expected for Landau-type asymptotics.
The computation is corroborative only; the infinite statement follows from the
two cited theorems and the exact reduction above.

## Relationship to prior work
Ore characterized squarefree arithmetic numbers. Oller-Marcén explicitly
records that characterization and develops a general criterion for arithmetic
numbers. That source gives the exact structural reduction used here but does
not state a fixed-prime-factor asymptotic.

Prabhu proves a Dirichlet-type density theorem for squarefree integers with a
fixed number of prime factors subject to prescribed prime congruence classes.
Her Theorem 1.3 supplies precisely the restricted Landau asymptotic needed
after the Ore reduction, but the paper concerns congruence densities and
quadratic congruences rather than arithmetic divisor means.

A published global result on squarefree arithmetic numbers gives a
Landau--Ramanujan-scale secondary term after summing over all prime-factor
layers. That global asymptotic does not determine any fixed-\(r\) layer: its
main contribution comes from prime-factor counts that grow with \(x\), whereas
the present theorem fixes \(r\) and exhibits a different
\[
\frac{x(\log\log x)^{r-2}}{\log x}
\]
scale and an explicit layer-dependent relative deficit.

A separate published result studies arithmetic numbers with two prime-power
blocks of prescribed exponents. Its hypotheses do not include the squarefree
equal-exponent case treated here.

## Limitations
The theorem does not give an error term and is not uniform in \(r\). In
particular, it cannot be summed over growing \(r\) to recover the unrestricted
squarefree secondary term without additional uniform estimates.

The novelty claim is the fixed-layer asymptotic and its explicit relative
deficit, not Ore's squarefree characterization, Landau's theorem, or Prabhu's
residue-class theorem.

Ore's 1948 paper is historically earlier than the exact date stored in
metadata, but the inspected bibliographic records supplied only the year, not
an exact public calendar day. The stored date is the earliest exact public
date verified here for an archival source used in the proof.

## References
1. A. M. Oller-Marcén, "On arithmetic numbers", arXiv:1206.1823v1,
   submitted 8 June 2012; later *Mathematische Nachrichten* 288 (2015),
   665--669. Primary MSC 11A25.
2. N. Prabhu, "Density of solutions to quadratic congruences",
   arXiv:1605.00088v1, submitted 30 April 2016; later
   *Czechoslovak Mathematical Journal* 67 (2017), 439--455.
3. O. Ore, "On the averages of the divisors of a number",
   *American Mathematical Monthly* 55 (1948), 615--619.
4. E. Landau, "Sur quelques problèmes relatifs à la distribution des
   nombres premiers", *Bulletin de la Société Mathématique de France* 28
   (1900), 25--38.
5. OEIS Foundation, A003601, "Arithmetic numbers".
