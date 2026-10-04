# Exact two-test calibration and weight extremum for independent harmonic-mean p-values
## Finding
Let \(U\) and \(V\) be independent exact null p-values, each uniform on \([0,1]\). For a normalized weight \(w\in[0,1]\), define
\[
H_w=\left(\frac{w}{U}+\frac{1-w}{V}\right)^{-1}.
\]
For \(0<h<1\) and \(0<w<1\),
\[
\Pr(H_w\le h)=h+h^2w(1-w)\log\!\left(1+\frac{1-h}{h^2w(1-w)}\right).
\]
For \(w=0\) or \(w=1\), the statistic is one of the original uniform p-values, so \(\Pr(H_w\le h)=h\).

For every fixed \(h\in(0,1)\), the excess \(\Pr(H_w\le h)-h\) is strictly positive for \(0<w<1\) and is uniquely maximized at \(w=1/2\). Thus equal weighting is the unique worst normalized two-test weighting for direct type-I error inflation under independent exact null p-values.

At \(h=0.05\), equal weighting gives exact rejection probability
\[
0.05457945205766206,
\]
which is about \(9.1589\%\) larger than the nominal level. Solving the exact equal-weight distribution equation for size \(0.05\) gives the calibrated cutoff
\[
0.04602921464598153.
\]

## Assumptions and scope
The claim concerns exactly two independent p-values that are continuously and exactly uniform under the joint null. The weight is deterministic and normalized to \(w\) and \(1-w\). The result is a finite-sample null calculation; it does not cover dependent p-values, conservative or discrete p-values, estimated or data-dependent weights, more than two inputs, or power under alternatives.

The equal-weight specialization itself is not claimed as new. An exact distribution for the ordinary harmonic mean of two uniform variables appears in Rui Li's 2018 thesis. The contribution here is the arbitrary normalized two-weight law together with the strict ordering in the weight and its exact calibration consequence for the two-test harmonic-mean p-value.

## Proof
Fix \(0<h<1\) and \(0<w<1\). Write \(u\) and \(v\) for realized values of \(U\) and \(V\). The event \(H_w>h\) is equivalent to
\[
uv>h\{wv+(1-w)u\},
\]
or
\[
v(u-hw)>h(1-w)u.
\]
There are no solutions when \(u\le hw\). When \(u>hw\), the inequality becomes
\[
v>\frac{h(1-w)u}{u-hw}.
\]
The right side is below one exactly when
\[
u>a:=\frac{hw}{1-h(1-w)}.
\]
Therefore independence and uniform density give
\[
\Pr(H_w>h)=\int_a^1\left(1-\frac{h(1-w)u}{u-hw}\right)\,du.
\]
Using
\[
\frac{u}{u-hw}=1+\frac{hw}{u-hw},
\]
direct integration yields
\[
\Pr(H_w>h)=1-h-h^2w(1-w)\log\!\left(\frac{(1-hw)(1-h(1-w))}{h^2w(1-w)}\right).
\]
Since
\[
(1-hw)(1-h(1-w))=1-h+h^2w(1-w),
\]
subtracting from one gives the stated distribution formula.

For the weight comparison put \(t=w(1-w)\in(0,1/4]\) and \(A=(1-h)/h^2>0\). Apart from the positive factor \(h^2\), the type-I error excess is
\[
g(t)=t\log(1+A/t).
\]
Its derivative is
\[
g'(t)=\log(1+A/t)-\frac{A}{A+t}.
\]
With \(x=A/t>0\), the bracket is \(\log(1+x)-x/(1+x)\). This is strictly positive because it vanishes at \(x=0\) and its derivative is \(x/(1+x)^2>0\). Hence the excess is strictly increasing in \(t\), and \(t=w(1-w)\) has its unique maximum \(1/4\) at \(w=1/2\).

At \(w=1/2\), simplification gives
\[
\Pr(H_{1/2}\le h)=h+\frac{h^2}{2}\log\!\left(\frac{2-h}{h}\right),
\]
which agrees with the previously published equal-weight two-uniform formula.

## Verification
A standalone checker evaluates the closed form against direct numerical integration of the defining region at several interior parameter pairs, verifies symmetry under \(w\mapsto1-w\), verifies strict growth from \(w=0.1\) through \(w=0.5\) at \(h=0.05\), checks the equal-weight specialization, and solves the exact \(5\%\) calibration equation. The checked equal-weight values are \(0.05457945205766206\) at direct threshold \(0.05\) and calibrated cutoff \(0.04602921464598153\).

The proof, not the numerical checker, establishes the formula and the all-\(h\), all-interior-weight strict extremum.

## Relationship to prior work
Wilson introduced the weighted harmonic-mean p-value and explained that direct interpretation is anti-conservative while asymptotic calibration becomes accurate in suitable regimes. The inspected preprint defines the weighted statistic and develops Landau-based large-group calibration, but does not supply the exact arbitrary-weight two-input null law or the weight extremum above.

Chen, Wang, Wang, and Zhu prove strict sub-uniformity of weighted harmonic means under independence and related dependence assumptions and emphasize the need for threshold or multiplier adjustment. Their result supplies broader qualitative coverage of the sign of the calibration error, whereas the present two-input calculation gives its exact finite-sample magnitude and orders every deterministic two-test weight.

Li's 2018 thesis derives the equal-weight two-uniform distribution
\[
h+\frac{h^2}{2}\log\!\left(\frac{2-h}{h}\right).
\]
That specialization is therefore prior art and is used here as an independent consistency check, not as part of the originality claim. Chen et al. also point to an older risk-management example concerning the harmonic mean of two uniforms; the exact weighted extension was not located in the inspected material.

## Limitations
The novelty assessment is bounded by the literature and database searches reported in the review material. A generic probability reference could contain the same weighted two-uniform transformation without harmonic-mean p-value terminology. The 2002 risk-management chapter cited by Chen et al. was only available through an extract in the inspected source; it is a residual literature risk, although the accessible descriptions concern the unweighted two-uniform case.

No claim is made that equal weights are undesirable for power, that this ordering extends to more than two p-values, or that the formula gives valid calibration under dependence.

## References
D. J. Wilson, “The harmonic mean p-value for combining dependent tests,” bioRxiv 171751, first public version 7 February 2018; later published in Proceedings of the National Academy of Sciences, 2019. DOI: 10.1101/171751.

Y. Chen, R. Wang, Y. Wang, and W. Zhu, “Sub-uniformity of harmonic mean p-values,” arXiv:2405.01368, first version 2 May 2024.

R. Li, *Some Contributions to Distribution Theory*, PhD thesis, University of Manchester, 2018, Chapter 7.

P. Embrechts, A. J. McNeil, and D. Straumann, “Correlation and Dependence in Risk Management: Properties and Pitfalls,” in *Risk Management: Value at Risk and Beyond*, Cambridge University Press, 2002.
