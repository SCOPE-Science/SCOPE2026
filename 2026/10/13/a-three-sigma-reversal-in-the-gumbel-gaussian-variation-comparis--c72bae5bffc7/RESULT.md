# A three-sigma reversal in the Gumbel–Gaussian variation comparison
## Finding
Let \(Y\) have the standard Gumbel distribution
\[
F(y)=\exp(-e^{-y}),
\]
with mean \(\gamma\), Euler's constant, and standard deviation
\[
a=\frac{\pi}{\sqrt6}.
\]
Set
\[
G=\frac{Y-\gamma}{a},
\qquad
C_G(c)=\Pr\{|G|\le c\},
\]
and for a standard normal random variable \(Z\), set
\[
C_N(c)=\Pr\{|Z|\le c\}=2\Phi(c)-1.
\]
The published one-standard-deviation comparison gives \(C_G(1)>C_N(1)\). In contrast, for every \(c\ge3\),
\[
C_G(c)<C_N(c).
\]
Thus the Gumbel advantage reverses before three standard deviations and can never return after radius \(3\).

Writing
\[
T_G(c)=1-C_G(c),
\qquad
T_N(c)=1-C_N(c),
\]
the reversal strengthens asymptotically to
\[
\frac{T_G(c)}{T_N(c)}
\sim
\sqrt{\frac{\pi}{2}}\,c
\exp\!\left(
\frac{c^2}{2}-\frac{\pi c}{\sqrt6}-\gamma
\right)
\longrightarrow\infty
\qquad(c\to\infty).
\]
By continuity, since the ordering at \(c=1\) is the opposite of the ordering at \(c=3\), there is at least one crossover radius in \((1,3)\).

## Assumptions and scope
The theorem concerns the ordinary location-scale Gumbel family. Standardization removes its location and positive scale parameters, so it is enough to use the standard Gumbel law above. The comparison is between symmetric intervals about each distribution's arithmetic mean, measured in that distribution's own standard deviation. The theorem proves a permanent reversal for every \(c\ge3\) and existence of a crossover in \((1,3)\); it does not claim that the crossover is unique or identify its exact value.

## Proof
For \(c>0\), the exact Gumbel outside-central probability is
\[
T_G(c)
=
1-F(\gamma+ac)+F(\gamma-ac).
\]
Put
\[
x_c=e^{-\gamma-ac}.
\]
Because the left-tail term is positive,
\[
T_G(c)>1-e^{-x_c}.
\]
The elementary inequality \(e^x>1+x\) for \(x>0\) gives
\[
1-e^{-x} > \frac{x}{1+x},
\]
so
\[
T_G(c)>\frac{x_c}{1+x_c}.
\]
For the normal law, integration by parts in the standard Mills bound gives
\[
T_N(c)=2\overline\Phi(c)<\frac{2\varphi(c)}{c}.
\]
Hence it suffices to show
\[
R(c):=
\frac{c x_c}{2(1+x_c)\varphi(c)}>1.
\]
Differentiating the logarithm yields
\[
\frac{d}{dc}\log R(c)
=
c+\frac1c-a+\frac{a x_c}{1+x_c}.
\]
Since \(a=\pi/\sqrt6<4/3\), for every \(c\ge3\),
\[
\frac{d}{dc}\log R(c)
>
3+\frac13-\frac43
=2.
\]
Thus \(R\) is strictly increasing on \([3,\infty)\).

It remains to verify the left endpoint without relying on a floating-point calculation. The elementary estimates \(\gamma<1\), \(a<4/3\), and \(e<3\) give
\[
x_3=e^{-\gamma-3a}>e^{-5}>\frac1{243},
\]
so
\[
\frac{x_3}{1+x_3}>\frac1{244}.
\]
On the other hand,
\[
T_N(3)<\frac{2\varphi(3)}3
<\frac13e^{-9/2}.
\]
Also \(e>8/3\), and
\[
\left(3\left(\frac83\right)^{9/2}\right)^2
=
\frac{134217728}{2187}
>
244^2,
\]
so \(3e^{9/2}>244\), hence
\[
\frac13e^{-9/2}<\frac1{244}.
\]
Therefore \(T_G(3)>T_N(3)\), equivalently \(C_G(3)<C_N(3)\). Since \(R\) is increasing, the same strict inequality holds for every \(c\ge3\).

For the asymptotic statement,
\[
1-F(\gamma+ac)=1-e^{-x_c}\sim x_c=e^{-\gamma-ac},
\]
while
\[
F(\gamma-ac)=\exp\!\left(-e^{ac-\gamma}\right)
=o\!\left(e^{-\gamma-ac}\right).
\]
Thus
\[
T_G(c)\sim e^{-\gamma-ac}.
\]
Mills' asymptotic gives
\[
T_N(c)=2\overline\Phi(c)
\sim
\sqrt{\frac2\pi}\,\frac{e^{-c^2/2}}{c},
\]
and division gives the displayed tail-ratio equivalent.

Finally, the published result gives \(C_G(1)>C_N(1)\), whereas the theorem gives \(C_G(3)<C_N(3)\). Both central-mass functions are continuous, so their difference has a zero in \((1,3)\).

## Verification
The proof above is analytic and covers every real \(c\ge3\). The standalone script `verify_gumbel_radius_reversal.py` independently evaluates the exact Gumbel and normal central probabilities, checks the sign at representative radii, checks monotonicity of the lower-bound ratio on a deterministic mesh, and locates a numerical crossover only as a regression diagnostic. It prints
`VERIFY_OK root_locator=2.055935618225228 R3=4.005361355853`.

The numerical locator is not part of the theorem and is not used to prove existence, permanence of the reversal, or the asymptotic tail ratio.

## Relationship to prior work
Sun, Hu and Sun study the standardized one-standard-deviation variation comparison
\[
\Pr\{|X-\mathbb EX|\le\sqrt{\operatorname{Var}(X)}\}
\ge
\Pr\{|Z|\le1\}
\]
for familiar infinitely divisible distributions. For the Gumbel family they prove the inequality at radius \(1\), obtaining a central probability approximately \(0.723751\), compared with the normal value approximately \(0.682689\). Their result is therefore a fixed-radius statement.

The present finding changes the radius rather than the distribution family. It proves that the same standardized Gumbel law has strictly less central mass than the standard normal at every radius \(c\ge3\), and that the ratio of the corresponding outside-central probabilities diverges. Thus the one-standard-deviation comparison does not extend to an all-radius concentration ordering.

A secondary extreme-value text reports a one-sided comparison at three standard deviations, attributed to Gumbel's classical work: the Gumbel right-side cumulative percentage is smaller than the corresponding normal percentage. That observation is consistent with the heavy right tail, but it is not the symmetric central-mass theorem proved here and does not by itself establish the all-\(c\ge3\) statement or the tail-ratio equivalent.

## Limitations
The radius \(3\) is a rigorously convenient permanent-reversal threshold, not claimed to be the sharp crossover. Numerical evaluation suggests a crossing near \(2.05594\), but uniqueness and exact localization are deliberately left unclaimed. The originality search did not materially inspect the classical 1958 Gumbel source cited by a secondary text, so an older equivalent all-radius statement under different terminology remains a residual risk. The theorem concerns the Gumbel location-scale family only.

## References
1. P. Sun, Z.-C. Hu and W. Sun, *Variation comparison between infinitely divisible distributions and the normal distribution*, arXiv:2304.11459v1, first posted 2023-04-22; later published in *Statistical Papers* 65 (2024), 4405–4429. Primary MSC \(60E15\).
2. J. Pevsner, *Bioinformatics and Functional Genomics*, 3rd ed., Wiley-Blackwell, 2015. A figure discussion compares the normal and extreme-value distributions at three standard deviations and attributes the comparison to Gumbel (1958).
