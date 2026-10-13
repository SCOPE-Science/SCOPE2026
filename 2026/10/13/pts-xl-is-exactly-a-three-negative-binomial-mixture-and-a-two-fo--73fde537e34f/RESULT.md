# PTS-XL is exactly a three-negative-binomial mixture and a two-fold PXL convolution
## Finding
Let
\[
\theta>0,
\]
and let the XLindley mixing density used in the PTS-XL construction be
\[
f_{\mathrm{XL}}(t;\theta)
=
\frac{\theta^2}{(1+\theta)^2}
(2+\theta+t)e^{-\theta t},
\qquad t>0.
\]
Define
\[
a=
\frac{\theta(\theta+2)}{(1+\theta)^2},
\qquad
b=
\frac{1}{(1+\theta)^2}.
\]
Then
\[
a+b=1,
\]
and the density has the exact finite-mixture representation
\[
\boxed{
f_{\mathrm{XL}}
=
a f_{\Gamma(1,\theta)}
+
b f_{\Gamma(2,\theta)},
}
\]
where the second argument denotes the rate.

If
\[
Y=Y_1+Y_2
\]
for independent XLindley variables with the same parameter, then the common-rate gamma convolution rule gives
\[
\boxed{
Y\sim
a^2\Gamma(2,\theta)
+
2ab\Gamma(3,\theta)
+
b^2\Gamma(4,\theta).
}
\]

Now let
\[
X\mid Y\sim\operatorname{Poisson}(Y).
\]
For \(k=2,3,4\), write \(\mathrm{NB}_k\) for the negative-binomial law
\[
\Pr(\mathrm{NB}_k=x)
=
\binom{x+k-1}{x}
\left(\frac{\theta}{1+\theta}\right)^k
\left(\frac{1}{1+\theta}\right)^x,
\qquad x=0,1,2,\ldots .
\]
Poisson-gamma integration then gives the exact count-mixture identity
\[
\boxed{
X
\sim
a^2\mathrm{NB}_2
+
2ab\mathrm{NB}_3
+
b^2\mathrm{NB}_4.
}
\]

There is a second exact representation. Let \(U_1,U_2\) be independent Poisson-XLindley counts with the same parameter \(\theta\). Then
\[
\boxed{
X\overset d=U_1+U_2.
}
\]
Hence PTS-XL is precisely the two-fold convolution of the earlier PXL law.

Its probability generating function therefore factors as
\[
\boxed{
G_X(z)
=
G_{\mathrm{PXL}}(z)^2
}
\]
with
\[
G_{\mathrm{PXL}}(z)
=
\frac{
\theta^2
[\theta^2+3\theta+3-(\theta+2)z]
}{
(1+\theta)^2(1+\theta-z)^2
}.
\]
Thus
\[
G_X(z)
=
\frac{
\theta^4
[\theta^2+3\theta+3-(\theta+2)z]^2
}{
(1+\theta)^4(1+\theta-z)^4
},
\qquad |z|<1+\theta,
\]
which is exactly the PGF printed in Proposition 2 of the 2026 PTS-XL article.

The finite-mixture form gives an exact latent-state sampler: draw
\[
K\in\{2,3,4\}
\]
with probabilities
\[
a^2,\qquad 2ab,\qquad b^2,
\]
and then draw
\[
X\mid K\sim\mathrm{NB}_K.
\]
This avoids numerical integration of the two-sum XLindley mixing density and makes the relationship to the established PXL model explicit.

## Assumptions and scope
The parameter domain is
\[
\theta>0,
\]
matching the PTS-XL and PXL models.

The gamma distribution is parameterized by shape and rate. The negative-binomial convention counts failures before the \(k\)-th success, with success probability
\[
\theta/(1+\theta).
\]

The theorem is a distributional representation, not a claim that the PTS-XL model coincides with a single negative-binomial family. It is a three-component negative-binomial mixture and, equivalently, a convolution square of the PXL law.

No claim is made that the representation changes the source's likelihood, estimation, regression, or goodness-of-fit results.

## Proof
The shape-one and shape-two gamma densities with common rate \(\theta\) are
\[
f_{\Gamma(1,\theta)}(t)
=
\theta e^{-\theta t}
\]
and
\[
f_{\Gamma(2,\theta)}(t)
=
\theta^2 t e^{-\theta t}.
\]
Therefore
\[
a f_{\Gamma(1,\theta)}(t)
+
b f_{\Gamma(2,\theta)}(t)
=
\frac{\theta^2}{(1+\theta)^2}
(\theta+2+t)e^{-\theta t},
\]
which is the published XLindley density.

Because independent gamma variables with the same rate add their shapes, the sum of two independent copies has three possible latent shape sums:
\[
1+1=2,\qquad
1+2=3,\qquad
2+2=4.
\]
Their weights are respectively
\[
a^2,\qquad
2ab,\qquad
b^2.
\]

If
\[
\Lambda\sim\Gamma(k,\theta)
\]
and
\[
X\mid\Lambda\sim\operatorname{Poisson}(\Lambda),
\]
then direct integration gives
\[
\Pr(X=x)
=
\frac{1}{x!}
\int_0^\infty
e^{-\lambda}\lambda^x
\frac{\theta^k}{\Gamma(k)}
\lambda^{k-1}e^{-\theta\lambda}\,d\lambda.
\]
Evaluating the gamma integral yields
\[
\Pr(X=x)
=
\binom{x+k-1}{x}
\left(\frac{\theta}{1+\theta}\right)^k
\left(\frac{1}{1+\theta}\right)^x.
\]
Applying this calculation to each latent gamma component proves the three-negative-binomial mixture.

For the convolution statement, condition on independent XLindley variables \(Y_1,Y_2\), and let
\[
U_i\mid Y_i\sim\operatorname{Poisson}(Y_i)
\]
independently. Then
\[
U_1+U_2\mid(Y_1,Y_2)
\sim
\operatorname{Poisson}(Y_1+Y_2).
\]
Marginalizing both sides proves
\[
U_1+U_2\overset d=X.
\]

The PGF of the negative-binomial component is
\[
\left(
\frac{\theta}{1+\theta-z}
\right)^k.
\]
Hence the PXL PGF is
\[
a\frac{\theta}{1+\theta-z}
+
b\left(
\frac{\theta}{1+\theta-z}
\right)^2.
\]
Algebraic simplification gives the displayed \(G_{\mathrm{PXL}}\), and squaring gives the PTS-XL PGF. This independently reconstructs Proposition 2 of the source.

## Verification
The accompanying symbolic checker verifies four identities from the exact package path.

First, it confirms that the two gamma-mixture weights are positive and sum to one.

Second, it expands the three negative-binomial components and proves symbolically that their PMF equals the PTS-XL PMF in Eq. (2.9) of the source.

Third, it simplifies the single-PXL gamma-mixture PGF and proves that its square is exactly the PTS-XL PGF in Eq. (3.15).

Fourth, it checks normalization of the three component weights and compares numerical PMF values from the mixture and source formula at several positive parameter values and count values.

No finite computation is used to infer an infinite-domain identity; all distributional identities are proved algebraically above.

## Relationship to prior work
Ahmad and El-Awady define PTS-XL by first convolving two independent XLindley variables and then using the sum as a Poisson mixing variable. They derive a polynomial-exponential mixing density, the count PMF, and the squared-rational PGF. The inspected article does not state the three-gamma latent mixture, the resulting three-negative-binomial count mixture, or the equality in distribution with the sum of two independent PXL counts.

Ahsan-ul-Haq et al. introduced the one-parameter PXL count distribution by mixing Poisson with XLindley and derived its PGF and other properties. The inspected full text does not state that the 2026 PTS-XL law is its convolution square.

Chouia and Zeghdoudi introduced XLindley as a finite mixture of exponential and Lindley distributions. The density itself makes the simpler common-rate gamma decomposition above exact. Combining that decomposition with Poisson-gamma integration exposes a finite latent count representation that is not displayed in the inspected PTS-XL or PXL sources.

The classical facts that common-rate gamma variables add their shapes and that gamma mixing of a Poisson law gives a negative-binomial law are standard ingredients. The finding is the model-specific exact synthesis: the particular PTS-XL distribution collapses to three negative-binomial components and to a two-fold PXL convolution, with the published PGF recovered as an independent certificate.

## Limitations
The representation does not imply that a single negative-binomial model is equivalent to PTS-XL; three latent shapes are generally present.

The structural decomposition is mathematically elementary once the gamma form of the XLindley density is noticed. Its value is in making the latent finite mixture and convolution relation explicit for this newly proposed count law, rather than in introducing a new general compounding theorem.

No claim is made that the finite-mixture representation yields uniformly better numerical inference than the formulas in the source. It does, however, provide a direct exact sampler and an independent algebraic check of the published PMF and PGF.

## References
1. H. Haj Ahmad and M. M. El-Awady, “The Poisson two-sum XLindley distribution: Statistical properties, estimation, regression modeling, and applications,” AIMS Mathematics 11 (2026), 28121–28160. DOI: 10.3934/math.20261122.
2. M. Ahsan-ul-Haq, A. Al-Bossly, M. El-Morshedy, and M. S. Eliwa, “Poisson XLindley Distribution for Count Data: Statistical and Reliability Properties with Estimation Techniques and Inference,” Computational Intelligence and Neuroscience (2022), 6503670. DOI: 10.1155/2022/6503670.
3. S. Chouia and H. Zeghdoudi, “The XLindley Distribution: Properties and Application,” Journal of Statistical Theory and Applications 20 (2021), 318–327. DOI: 10.2991/jsta.d.210607.001.
