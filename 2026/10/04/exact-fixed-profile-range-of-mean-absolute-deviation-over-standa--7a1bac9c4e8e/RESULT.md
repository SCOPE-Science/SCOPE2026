# Exact fixed-profile range of mean absolute deviation over standard deviation

## Finding

Let \(X\) be a nondegenerate discrete random variable with distinct ordered atoms
\[
x_1<\cdots<x_m
\]
and fixed positive masses
\[
p_i=\Pr(X=x_i),
\qquad
\sum_{i=1}^m p_i=1.
\]
Write
\[
P_j=\sum_{i=1}^j p_i,
\qquad
D=\mathbb E|X-\mathbb EX|,
\qquad
\sigma=\sqrt{\operatorname{Var}(X)}.
\]
Define
\[
L(\mathbf p)
=
2\sqrt{\frac{p_1p_m}{p_1+p_m}}
\]
and
\[
U(\mathbf p)
=
2\max_{1\le j<m}\sqrt{P_j(1-P_j)}.
\]

Then the complete range of the standardized mean absolute deviation is:

\[
\boxed{
\frac D\sigma=L(\mathbf p)=U(\mathbf p)
}
\]
when \(m=2\);

\[
\boxed{
\frac D\sigma\in[L(\mathbf p),U(\mathbf p))
}
\]
when \(m=3\); and

\[
\boxed{
\frac D\sigma\in(L(\mathbf p),U(\mathbf p))
}
\]
when \(m\ge4\).

For three atoms, the lower endpoint is attained exactly when the middle atom equals the mean:
\[
x_2=\mathbb EX.
\]
Equivalently,
\[
p_1(x_2-x_1)=p_3(x_3-x_2).
\]

For \(m\ge4\), the lower endpoint is not attained. It is approached by supports in which every interior atom collapses toward the mean while the two endpoint atoms remain separated.

For every \(m\ge3\), the upper endpoint is not attained. It is approached by collapsing the support to two levels across any cut
\[
\{1,\ldots,j\}\mid\{j+1,\ldots,m\}
\]
that maximizes
\[
P_j(1-P_j).
\]

Thus the sharp minimum remembers only the two endpoint masses, whereas the sharp maximum remembers only the cumulative probability cut closest to one half.

For equal masses \(p_i=1/m\), the formulas become
\[
L=\sqrt{\frac2m}
\]
and
\[
U=
\begin{cases}
1,&m\text{ even},\\[1mm]
\sqrt{1-\dfrac1{m^2}},&m\text{ odd}.
\end{cases}
\]
Hence a uniformly weighted support with many distinct atoms can make mean absolute deviation as small as approximately \(\sqrt{2/m}\) standard deviations, while an even number of equal masses can make the ratio arbitrarily close to one.

## Assumptions and scope

The atom probabilities and their order are fixed. Only the numerical support locations vary.

Every mass is strictly positive and every displayed support atom is distinct. Boundary configurations with coincident support levels are used only to identify sharp infima or suprema.

The theorem concerns mean absolute deviation about the arithmetic mean, not median absolute deviation.

No bounded-support diameter is prescribed. The ratio \(D/\sigma\) is invariant under positive affine transformations of the support.

## Proof

Set
\[
Y=X-\mathbb EX.
\]
Let
\[
a=-\min Y>0,
\qquad
b=\max Y>0,
\]
and put
\[
A=\mathbb E(Y_+)=\mathbb E((-Y)_+).
\]
The equality of the two one-sided first moments follows from
\[
\mathbb EY=0.
\]
Also
\[
D=2A.
\]

For every \(y\in[-a,0]\),
\[
y^2\le a(-y),
\]
while for every \(y\in[0,b]\),
\[
y^2\le by.
\]
Taking expectations gives
\[
\sigma^2
\le
A(a+b).
\tag{1}
\]

The left endpoint atom contributes \(p_1a\) to the negative one-sided first moment, so
\[
p_1a\le A.
\]
Likewise the right endpoint atom contributes \(p_mb\) to the positive one-sided first moment, so
\[
p_mb\le A.
\]
Therefore
\[
a\le\frac A{p_1},
\qquad
b\le\frac A{p_m}.
\]
Substitution into (1) yields
\[
\sigma^2
\le
A^2
\left(
\frac1{p_1}+\frac1{p_m}
\right).
\]
Since \(D=2A\),
\[
\frac D\sigma
\ge
2\sqrt{\frac{p_1p_m}{p_1+p_m}}
=
L(\mathbf p).
\tag{2}
\]

Equality in (2) forces equality at every preceding step. Thus all negative mass must lie at the left endpoint, all positive mass at the right endpoint, and every remaining atom must lie at the mean. With distinct support this is possible precisely when \(m\le3\). For \(m=3\), it is exactly the condition
\[
x_2=\mathbb EX.
\]
For \(m\ge4\), strict distinctness prevents equality, while a sequence with all interior atoms tending to the mean shows that the lower constant remains sharp.

For the upper bound, let \(j\) be the last index for which
\[
x_j\le\mathbb EX.
\]
Let
\[
I=\mathbf 1_{\{X>\mathbb EX\}}.
\]
Then
\[
\Pr(I=1)=1-P_j.
\]
Because \(\mathbb EY=0\),
\[
\operatorname{Cov}(Y,I)
=
\mathbb E[YI]
=
A.
\]
Cauchy--Schwarz gives
\[
A
\le
\sigma\sqrt{P_j(1-P_j)}.
\]
Consequently
\[
\frac D\sigma
=
\frac{2A}{\sigma}
\le
2\sqrt{P_j(1-P_j)}
\le
U(\mathbf p).
\tag{3}
\]

Equality in the first inequality of (3) requires \(Y\) to be affine in the binary indicator \(I\), so \(X\) can take only two distinct values. Therefore the upper bound is strict whenever \(m\ge3\). Conversely, if the atoms below a maximizing cut collapse to one level and the atoms above it collapse to another, the ratio tends to the corresponding two-point value
\[
2\sqrt{P_j(1-P_j)},
\]
proving sharpness of the supremum.

For \(m=2\), every support shape is a positive affine image of every other and direct substitution gives
\[
\frac D\sigma=2\sqrt{p_1p_2}=L=U.
\]

Finally, the strict-support cone
\[
\{(x_1,\ldots,x_m):x_1<\cdots<x_m\}
\]
is connected, and \(D/\sigma\) is continuous on it. Its image is therefore an interval. Combining this with the sharp endpoint constructions and the equality analysis gives the three cases stated above.

For equal masses, the lower formula simplifies immediately to
\[
L=\sqrt{\frac2m}.
\]
The quantity \(P_j(1-P_j)\) is largest at the cumulative mass nearest \(1/2\), which gives the displayed even--odd formula for \(U\).

## Verification

The accompanying exact-rational checker generates random rational probability profiles and strictly increasing rational supports.

For every case it checks
\[
D^2\ge L(\mathbf p)^2\sigma^2
\]
and
\[
D^2<U(\mathbf p)^2\sigma^2
\]
for \(m\ge3\), with exact equality in the two-point case.

It separately constructs the exact three-point lower-endpoint support, checks the equal-weight formulas, and follows explicit strict-support collapse sequences toward both sharp endpoints.

The finite checks are supplementary. The universal theorem follows from the one-sided second-moment bound, Cauchy--Schwarz, equality reconstruction, and connectedness argument above.

## Relationship to prior work

Korwar develops mean-absolute-deviation inequalities for functions of discrete random variables and uses them to characterize distribution families. The inspected paper is concerned with derivative/difference bounds and distributional characterization, not with optimizing the ratio of mean absolute deviation to standard deviation over support geometry at a fixed atom-probability profile.

Aghili-Ashtiani studies upper bounds on mean absolute deviation using the range, the mean, and the numbers of observations above and below the mean. The inspected MAD section explicitly decomposes the sample into lower, upper, and boundary segments and proves sharp range-based upper bounds. Those results do not state a lower bound relative to standard deviation, do not retain arbitrary unequal atom probabilities, and do not identify the exact fixed-profile attainable interval.

Berend and Kontorovich obtain sharp non-asymptotic estimates for the mean absolute deviation of a binomial random variable. Their optimized object is the binomial family itself; the support is fixed by the binomial model rather than varied under a prescribed arbitrary probability vector.

The present theorem instead fixes the complete ordered mass profile and varies only support geometry. The two endpoint mechanisms are different: the lower constant is forced by the two endpoint masses, while the upper constant is forced by the cumulative cut nearest one half.

Targeted searches using fixed probability profiles, mean absolute deviation, standard deviation, finite support, frequencies, and support optimization did not locate these endpoint formulas or the full attainable-set classification.

## Limitations

The theorem requires finite discrete support and fixed atom probabilities.

The sharp lower and upper configurations are boundary coarsenings; except for the three-point lower endpoint and the two-point case, they are not attained by distinct supports.

The originality assessment was targeted. Older finite-population or deviation-inequality literature could contain an equivalent fixed-profile ratio theorem under different terminology.

## References

1. R. M. Korwar, “On characterizations of distributions by mean absolute deviation and variance bounds,” *Annals of the Institute of Statistical Mathematics* 43 (1991), 287–295, DOI 10.1007/BF00118636.
2. D. Berend and A. Kontorovich, “A sharp estimate of the binomial mean absolute deviation with applications,” *Statistics & Probability Letters* 83 (2013), 1254–1259, DOI 10.1016/j.spl.2013.01.023.
3. A. Aghili-Ashtiani, “Upper bounds on deviations from the mean and the mean absolute deviation,” *Italian Journal of Pure and Applied Mathematics* 45 (2021), 940–951.
