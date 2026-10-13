# The generation-time growth shortcut first loses fertility monotonicity at net reproduction six
## Finding
Consider a two-age net maternity schedule with strictly positive integer survivorship-weighted reproductive contributions
\[
a
\]
at age \(1\) and
\[
b
\]
at age \(2\).

The exact Euler–Lotka equation is
\[
a e^{-r}+b e^{-2r}=1.
\]
Writing
\[
\lambda=e^r,
\]
this becomes
\[
\lambda^2=a\lambda+b.
\]
Hence
\[
\lambda=\frac{a+\sqrt{a^2+4b}}{2}.
\]
The exact growth factor, and therefore the exact intrinsic rate, is strictly increasing when either reproductive contribution increases.

Now use the common generation-time shortcut
\[
\widetilde r=\frac{\log R_0}{T},
\]
where
\[
R_0=a+b
\]
and
\[
T=\frac{a+2b}{a+b}.
\]
For this two-age schedule,
\[
\widetilde r(a,b)=\frac{(a+b)\log(a+b)}{a+2b}.
\]

On the strictly positive integer grid, adding one unit of age-2 reproductive output cannot decrease \(\widetilde r\) when the initial net reproductive rate satisfies
\[
R_0\le5.
\]

The first failure occurs at
\[
R_0=6,
\]
and is unique there. It is
\[
(a,b)=(5,1)
\quad\longrightarrow\quad
(5,2).
\]

The exact growth factor increases:
\[
\lambda(5,1)=\frac{5+\sqrt{29}}2
<
\frac{5+\sqrt{33}}2=\lambda(5,2).
\]
Numerically,
\[
r(5,1)\approx1.6472311464
<
1.6812526457\approx r(5,2).
\]

But the shortcut moves in the wrong direction:
\[
\widetilde r(5,1)=\frac{6\log6}{7}
\approx1.5357938308,
\]
while
\[
\widetilde r(5,2)=\frac{7\log7}{9}
\approx1.5134856715.
\]
Thus adding late reproduction raises true asymptotic population growth but lowers the generation-time approximation.

## Assumptions and scope
The schedule has exactly two reproductive ages, \(1\) and \(2\), and both survivorship-weighted reproductive contributions are strictly positive integers.

The exact intrinsic growth rate is the unique real solution of the Euler–Lotka equation. The shortcut uses the cohort mean age of reproduction
\[
T=\frac{\sum_x x p_x}{\sum_x p_x}.
\]

The finite boundary concerns one-unit additions to the later-age contribution on an integer grid. It does not claim that all demographic applications use integer reproductive contributions.

The result addresses the approximation \(\log(R_0)/T\), not the exact identity \(T=\log(R_0)/r\) sometimes used to define a growth-implied generation time after \(r\) has already been computed.

## Proof
The exact Euler–Lotka growth factor is
\[
\lambda(a,b)=\frac{a+\sqrt{a^2+4b}}2.
\]
Therefore
\[
\frac{\partial\lambda}{\partial b}
=
\frac1{\sqrt{a^2+4b}}>0.
\]
Adding late reproduction always increases the exact growth factor.

For the shortcut, let
\[
S=a+b.
\]
Then
\[
\widetilde r(a,b)=\frac{S\log S}{2S-a}.
\]
If one unit is added at age \(2\), the shortcut decreases exactly when
\[
\frac{(S+1)\log(S+1)}{2S+2-a}
<
\frac{S\log S}{2S-a}.
\]
Cross-multiplication gives
\[
S(2S+2-a)\log S
>
(S+1)(2S-a)\log(S+1).
\]
Exponentiating yields the exact integer criterion
\[
S^{S(2S+2-a)}
>
(S+1)^{(S+1)(2S-a)}.
\]

For every positive integer schedule with
\[
S\le5,
\]
direct exact evaluation of this finite criterion shows that the inequality never holds.

At
\[
S=6,
\]
it holds only for
\[
a=5,
\qquad
b=1.
\]
The certificate becomes
\[
6^{54}>7^{49}.
\]
This proves the sharp positive-integer boundary and uniqueness of the first failure.

The phenomenon has a continuous mechanism. At fixed \(a\), differentiating with respect to \(b\) gives
\[
\frac{\partial\widetilde r}{\partial b}
=
\frac{2S-a(1+\log S)}{(2S-a)^2}.
\]
Thus the shortcut is locally decreasing in late reproduction precisely when
\[
a(1+\log S)>2S.
\]
The witness \((5,1)\) lies in this region.

Finally, the shortcut is intrinsically a lower approximation in the growing, nondegenerate case. Normalize the age distribution by
\[
q_x=\frac{p_x}{R_0}.
\]
For
\[
r_0=\frac{\log R_0}{T},
\]
convexity of \(e^{-r_0 x}\) gives
\[
\sum_x q_x e^{-r_0x}
>
e^{-r_0T}
=
\frac1{R_0}
\]
when reproduction occurs at more than one age. Since the Euler–Lotka left side decreases with \(r\), the exact solution satisfies
\[
r>r_0.
\]
The new point is that this lower approximation can move in the opposite direction under an increase in late fertility.

## Verification
The embedded `verify_generation_time_shortcut_monotonicity.py` uses only the Python standard library.

It exhausts every positive integer two-age schedule with initial
\[
R_0\le6,
\]
checks the one-unit late-fertility move exactly through integer exponent comparisons, and confirms that the unique first shortcut decrease is
\[
(5,1)\to(5,2).
\]

It separately checks that the exact Euler–Lotka growth factor increases for every tested move and verifies the exact witness certificate
\[
6^{54}>7^{49}.
\]

Run:

`python3 verify_generation_time_shortcut_monotonicity.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Demographic theory distinguishes net reproductive output from the timing of that output because both affect asymptotic population growth. de-Camino-Beck and Lewis emphasize that interpreting \(R_0\) without generation time can be misleading and develop explicit reproductive-timing calculations for structured populations.

Clavijo-Baquet and coauthors use
\[
r\approx\frac{\log R_0}{T_g}
\]
in an ecological life-table study and explicitly note that this is an approximation that works acceptably when \(R_0\) is near replacement or when generation-time variation is small. Their empirical results also show that \(R_0\), generation time, and growth rate can respond differently to environmental conditions.

Steiner, Tuljapurkar, and Coulson likewise treat reproductive level and timing as joint determinants and approximators of population growth.

The present result does not challenge the usefulness of the approximation near its intended regime. It isolates a qualitative failure mode outside that regime: the shortcut can violate the basic monotonicity that exact Euler–Lotka growth has with respect to added fertility, and the smallest strictly positive two-age integer schedule where this happens is identified exactly.

Targeted searches using the approximation formula, late reproduction, monotonicity, added fertility, Euler–Lotka growth, and the exact witness did not locate this sharp failure boundary.

## Limitations
The sharp cutoff is for two reproductive ages and strictly positive integer reproductive contributions.

The shortcut can be accurate in many empirically relevant schedules, especially near replacement; the witness is a structural stress test, not a claim of typical empirical error.

The older demographic literature is broad, and an unindexed exercise could contain a numerically similar example without identifying the monotonicity mechanism or the exact first integer boundary.

The result concerns deterministic age-structured growth and does not incorporate density dependence, environmental stochasticity, or uncertainty in estimated vital rates.

## References
1. T. de-Camino-Beck and M. A. Lewis, “On Net Reproductive Rate and the Timing of Reproductive Output,” *The American Naturalist* 172(1), 128–139, electronically published 28 May 2008. DOI: 10.1086/588060.
2. S. Clavijo-Baquet et al., “Differential responses to thermal variation between fitness metrics,” *Scientific Reports* 4:5349, published 23 June 2014. DOI: 10.1038/srep05349.
3. U. K. Steiner, S. Tuljapurkar, and T. Coulson, “Generation Time, Net Reproductive Rate, and Growth in Stage-Age-Structured Populations,” *The American Naturalist* 183(6), 771–783, published online 21 April 2014. DOI: 10.1086/675894.
