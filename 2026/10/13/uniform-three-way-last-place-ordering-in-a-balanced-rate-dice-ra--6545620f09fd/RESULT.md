# Uniform three-way last-place ordering in a balanced-rate dice race

## Finding

Consider the three-player race in which the respective integer goals are \(1\), \(2\), and \(n\), where \(n\ge 2\). On each turn exactly one player advances one unit, with selection probabilities proportional to the respective goals. Let \(\tau_1(n)\), \(\tau_2(n)\), and \(\tau_n(n)\) be the probabilities that each player is the **last** to attain their goal.

For **every integer** \(n\ge 3\),
\[
\boxed{\tau_1(n)+\frac1{200}<\tau_2(n),\qquad
       \tau_2(n)+\frac1{100}<\tau_n(n).}
\]
Consequently the last-place ranking is the strict goal ordering, with **uniformly positive** gaps. At the boundary \(n=2\), the second and third players tie as the most likely to finish last, and
\[
\tau_1(2)=\frac{352}{1125},\qquad
\tau_2(2)=\tau_n(2)=\frac{773}{2250},\qquad
\tau_2(2)-\tau_1(2)=\frac{23}{750}.
\]
The displayed uniform constants are convenient certified margins, not assertions of optimality.

## Assumptions and scope

The race has exactly three players. The successive choices of which player advances are independent and identically distributed, with probabilities \(1/(n+3)\), \(2/(n+3)\), and \(n/(n+3)\). Each player stops advancing upon attaining its goal. All claims quantify over **integer** \(n\ge2\); the two strict-gap inequalities are for \(n\ge3\). There are no simultaneous finishes because a turn advances only one player.

A standard Poissonization embeds the turns as arrivals of a unit-rate Poisson process. Independent thinning gives independent exponential-clock completion times
\[
X_1\sim\operatorname{Gamma}(1,\mathrm{rate}\ 1),\quad
X_2\sim\operatorname{Gamma}(2,\mathrm{rate}\ 2),\quad
X_n\sim\operatorname{Gamma}(n,\mathrm{rate}\ n),
\]
where the common time scaling by \(n+3\) does not change finishing ranks. The last-place probability \(\tau_i(n)\) is exactly the probability that \(X_i\) is the maximum of these independent, continuous variables.

## Proof

**1. Exact probability formulas.** For integers \(c\ge1\) define
\[
 r_c(n)=\left(\frac{n}{n+c}\right)^n,\qquad
 A_n=\frac{3n+2}{n+2},\quad B_n=\frac{4n+3}{n+3},\quad
 C_n=\frac{3n+3}{n+3}.
\]
The density of \(X_2\) is \(4x e^{-2x}\) on positive \(x\), and the first two distribution functions are \(F_1(x)=1-e^{-x}\) and \(F_2(x)=1-e^{-2x}(1+2x)\). The Laplace transform of \(X_n\) satisfies
\[
 \mathbb E(e^{-cX_n})=r_c(n),\qquad
 \mathbb E(X_n e^{-cX_n})=\frac{n}{n+c}r_c(n).
\]
Therefore multiplying \(F_1(X_n)F_2(X_n)\) and taking expectations yields
\[
 \boxed{\tau_n(n)=1-r_1(n)-A_n r_2(n)+C_n r_3(n).}\tag{1}
\]
For the second player, the Erlang distribution function
\[
 F_n(x)=1-e^{-nx}\sum_{j=0}^{n-1}\frac{(nx)^j}{j!}
\]
gives
\[
 \tau_2(n)=\int_0^\infty4xe^{-2x}(1-e^{-x})F_n(x)\,dx.
\]
Termwise integration uses
\(\int_0^\infty x^{j+1}e^{-ax}\,dx=(j+1)!/a^{j+2}\) and the exact finite-series identity
\[
 \sum_{j=0}^{n-1}(j+1)z^j
 =\frac{1-(n+1)z^n+n z^{n+1}}{(1-z)^2}.
\]
Substitution and cancellation give
\[
 \boxed{\tau_2(n)=A_n r_2(n)-\frac49 B_n r_3(n).}\tag{2}
\]
Finally \(\tau_1(n)=1-\tau_2(n)-\tau_n(n)\). Writing
\(D_{21}(n)=\tau_2(n)-\tau_1(n)\) and
\(D_{n2}(n)=\tau_n(n)-\tau_2(n)\), we obtain the *exact* rational functions
\[
 \begin{aligned}
 D_{21}(n)
   &=\left(3-\frac4{n+2}\right)r_2(n)-r_1(n)
    -\frac{5n-3}{9(n+3)}r_3(n),\\
 D_{n2}(n)
   &=1-r_1(n)-2\left(3-\frac4{n+2}\right)r_2(n)
    +\left(\frac{43}{9}-\frac{10}{n+3}\right)r_3(n).
 \end{aligned}\tag{3}
\]

**2. A finite exact certificate.** For each of the \(498\) integers \(2\le n\le499\), `check.py` evaluates all three last-place probabilities and the differences in (3) as exact Python rational numbers. It checks \(D_{21}(n)>1/200\) throughout and \(D_{n2}(n)>1/100\) for \(3\le n\le499\); at \(n=2\) it checks equality \(\tau_n(2)=\tau_2(2)\). The checker also independently integrates the finite Erlang density expansions for \(2\le n\le32\) to cross-check both closed-form formulas. These are exhaustive finite tests for the **specified finite parameter range**; the next step separately handles all larger integers.

**3. Uniform infinite-range estimates.** The elementary logarithm inequalities
\[
 u-\frac{u^2}2\le\log(1+u)\le u\quad(u\ge0)
\]
and \(e^v\le(1-v)^{-1}\) for \(0\le v<1\) imply
\[
 e^{-c}<r_c(n)\le e^{-c+c^2/(2n)}
       \le\frac{e^{-c}}{1-c^2/(2n)}
       \qquad\bigl(c^2<2n\bigr).\tag{4}
\]
Finite Taylor sums with a geometric bound for the omitted tail establish the strict rational estimates
\[
 e^{-1}<\frac{46}{125},\qquad
 \frac{1353}{10000}<e^{-2}<\frac{17}{125},\qquad
 \frac{49}{1000}<e^{-3}<\frac1{20}.\tag{5}
\]
For reproducibility, the underlying rational comparisons in (5), including the Taylor bound \(e<27183/10000\), are checked in `check.py`.

For every integer \(n\ge500\), the first line of (3), together with (4) and (5), gives
\[
 \begin{aligned}
 D_{21}(n)
 &>\left(3-\frac4{502}\right)\frac{1353}{10000}
   -\frac{46}{125}\frac{1000}{999}
   -\frac59\frac1{20}\frac{1000}{991}\\
 &=\frac{20931734927}{2484922590000}>\frac1{200}.
 \end{aligned}\tag{6}
\]
Here \((3n+2)/(n+2)\ge3-4/502\) and
\((5n-3)/(9(n+3))<5/9\) were used.

For the second line of (3), apply the weaker bounds already valid for \(n\ge60\):
\(r_1(n)<(46/125)(120/119)\),
\(r_2(n)<(17/125)(30/29)\), and
\(r_3(n)>49/1000\). Since \(2(3-4/(n+2))<6\) and
\(43/9-10/(n+3)\ge43/9-10/63\), for all \(n\ge500\),
\[
 \begin{aligned}
 D_{n2}(n)
 &>1-\frac{46}{125}\frac{120}{119}
      -6\frac{17}{125}\frac{30}{29}
      +\left(\frac{43}{9}-\frac{10}{63}\right)\frac{49}{1000}\\
 &=\frac{114949}{10353000}>\frac1{100}.
 \end{aligned}\tag{7}
\]
The finite certificate and inequalities (6)–(7) cover **every** integer \(n\ge2\) in the stated domains and complete the proof.

## Verification

Run `python3 check.py` with an ordinary Python 3 interpreter; it uses only the standard library. It checks \(498\) integer instances exactly, tests \(31\) separate Erlang-integral identities, and reproduces both positive infinite-tail rational constants. The analytic derivations of the Erlang integral formulas and of the exponential majorants are essential: the finite tests alone would not prove an infinite statement.

## Relationship to prior work

Leobacher and Steinicke, *A dice game, a multinomial walk, and the inverted Dirichlet distribution*, arXiv:2605.21424v1, Proposition 30 and equation (13), give the gamma-variable representation of general finishing probabilities. Section 6 reports numerical last-place orderings including the single configuration \((1,2,3)\), presents other goal triples for which ordering reverses, and discusses asymptotic comparisons. Those distributional representations, isolated numerical examples, and asymptotic limits do not themselves establish the quantitative full-integer assertion for \((1,2,n)\). The exact finite-sum formulas and the exhaustive-to-infinite bounds above supply that additional inequality proof.

## Limitations

The theorem applies to the first strictly unequal goal pattern with fixed first two goals \(1\) and \(2\), and **all** integer third goals \(n\ge3\). It is not a classification of arbitrary goal triples, and counterexamples in the source show that a universal ordering for all triples would be false. The constants \(1/200\) and \(1/100\) are certified lower bounds, not claimed to be sharp. The analytical proof depends on the stated exponential-series bounds, and the finite parameter comparisons depend on reproducible exact-rational arithmetic.

## References

G. Leobacher and A. Steinicke, *A dice game, a multinomial walk, and the inverted Dirichlet distribution*, arXiv:2605.21424v1 (20 May 2026), https://arxiv.org/abs/2605.21424, especially Proposition 30 and Section 6.
