# Exact mean tuning and an entropy-deficit identity on a four-step skew-tent Markov curve

## Finding

For every real \(s>1\), put \(D=1+s+s^2\), \(N=s^2+2s+3\), \(a=D^{-1}\), and \(b=(1+s)/D\). Specialize the generalized skew-tent map of Moysis and collaborators [1, 2] to
\[
T_s(x)=\begin{cases}
a+sx,&0\le x\le b,\\
(1-x)/(1-b),&b<x\le1.
\end{cases}
\]
The critical endpoint itinerary is exactly \(0\mapsto a\mapsto b\mapsto1\mapsto0\), with four distinct positions; these equations uniquely specify this parameter curve among maps with \(0<a<b<1\) and positive left slope \(s>1\).

This map has a unique mixing physical absolutely continuous invariant probability \(\mu_s\). Its density, with values at the two breakpoints immaterial, is
\[
\rho_s(x)=\frac D N\begin{cases}
1,&0<x<a,\\
1+s^{-1},&a<x<b,\\
1+s^{-1}+s^{-2},&b<x<1.
\end{cases}
\]
Its invariant mean obeys the exact formula
\[
 m(s)=\int_0^1x\,d\mu_s(x)
 =\frac12+\frac{s+1}{(s^2+s+1)(s^2+2s+3)},
\]
and is a real-analytic strictly decreasing bijection from \((1,\infty)\) onto \((1/2,11/18)\). Thus each target mean in this open interval has a unique explicitly characterized parameter.

For all \(s>1\), the topological entropy is identically \(\log\lambda\), where \(\lambda\in(1,2)\) is the unique positive real root of \(\lambda^3=\lambda^2+\lambda+1\). Let
\[
q_j(s)=\frac{s^j}{D},\quad p_j=\lambda^{-(3-j)}\quad (j=0,1,2),
\qquad K(s)=\frac DN.
\]
Both \(q(s)\) and \(p\) are probability vectors. The metric entropy of the physical measure has the closed form
\[
h_{\mu_s}(T_s)=\frac{s+2}{N}\log s+\frac D N\log\frac D{s^2},
\]
and the following **exact, sharp entropy-deficit identity**:
\[
\boxed{\log\lambda-h_{\mu_s}(T_s)
 =K(s)\sum_{j=0}^{2}q_j(s)\log\frac{q_j(s)}{p_j}.}
\]
The entropy deficit is zero **if and only if** \(s=\lambda\). Consequently, the physical invariant measure is a maximal-entropy measure at exactly one point of the parameter curve, where the two slopes have equal absolute value. As \(s\to\infty\), the invariant mean tends to \(1/2\), the topological entropy stays \(\log\lambda\), while the metric entropy tends to zero, more precisely
\[
h_{\mu_s}(T_s)=\frac{\log s+1}{s}+O(s^{-2}).
\]

## Assumptions and scope

The phase space is the closed interval \([0,1]\), parameters are real \(s>1\), and the critical point \(b\) is assigned the left-branch value. Its right-hand limit equals the same value \(1\), so the map is continuous. Entropy is topological entropy of the continuous interval map, respectively Kolmogorov--Sinai entropy of its distinguished absolutely continuous invariant probability. All statements hold for **every** real \(s>1\), not merely sampled rational values. No claim is made about finite-precision implementations, different endpoint conventions at a discontinuity, or every invariant measure of the map.

## Proof

**1. The nonarbitrary postcritical Markov curve.** The source family with its right endpoint set to zero has slopes \((1-a)/b\) and \(-1/(1-b)\). Write the first slope as \(s\). Requiring \(T(a)=b\) gives \(b=a(1+s)\); together with \(1-a=sb\), this yields \(a=1/D\) and \(b=(1+s)/D\) uniquely. Conversely, these values give \(T(0)=a\), \(T(a)=b\), \(T(b)=1\), \(T(1)=0\). All four points are distinct because \(0<a<b<1\), and the two absolute slopes are \(s>1\) and \(t=(1-b)^{-1}=D/s^2>1\).

**2. A fixed mixing transition matrix.** The intervals \(I_0=[0,a]\), \(I_1=[a,b]\), and \(I_2=[b,1]\) have respective lengths \(1/D,s/D,s^2/D\), and their images are \(I_1,I_2,[0,1]\). The Markov adjacency matrix (rows indicate source intervals) is
\[
A=\begin{pmatrix}0&1&0\\0&0&1\\1&1&1\end{pmatrix}.
\]
It is primitive: every state leads to state \(2\) in at most two steps, and state \(2\) has a self-loop and reaches every state. The usual expanding interval Markov coding (with at most countable endpoint ambiguity) therefore gives a mixing interval map with topological entropy \(\log r(A)\). Since \(\det(zI-A)=z^3-z^2-z-1\), the Perron root is the asserted \(\lambda\).

**3. Density and uniqueness.** Write \(\mathcal P\) for the Frobenius--Perron operator. An output point in \(I_0\) has one preimage, in \(I_2\); a point in \(I_1\) has preimages in \(I_0,I_2\); a point in \(I_2\) has preimages in \(I_1,I_2\). Thus a step-density vector \((c_0,c_1,c_2)\) is fixed precisely when
\[
c_0=c_2/t,\qquad c_1=c_0/s+c_2/t,\qquad c_2=c_1/s+c_2/t.
\]
The displayed density solves all three equations; its normalization is the exact identity
\[
\sum_{j=0}^2 c_j|I_j|=\frac{1+(s+1)+D}{N}=1.
\]
Uniqueness, mixing, and almost-everywhere physicality follow from the standard primitive piecewise-expanding Markov interval-map theorem (or from the associated primitive expanding Markov partition; see [3]). The endpoint orbit itself is exceptional of Lebesgue measure zero.

**4. Exact mean and full range.** Integrating the step-density gives
\[
m(s)=\frac12\bigl(c_0a^2+c_1(b^2-a^2)+c_2(1-b^2)\bigr)
=\frac12+\frac{s+1}{DN}.
\]
The derivative is
\[
m'(s)=-\frac{3s^4+10s^3+15s^2+12s+2}{D^2N^2}<0.
\]
The two endpoint limits are \(m(1+)=11/18\) and \(m(+\infty)=1/2\). Strict monotonicity and continuity give the asserted bijection without a simulation-based statistical estimate.

**5. Metric entropy and KL rigidity.** The stationary probabilities of the three Markov intervals are
\[
\pi=(1,s+1,D)/N.
\]
The only nondeterministic transition is out of \(I_2\). Its conditional probabilities are exactly the geometric relative lengths \(q=(1,s,s^2)/D\), since the right branch maps \(I_2\) affinely onto \([0,1]\). Consequently the symbolic entropy rate is \((D/N)H(q)\), equal to the usual entropy formula \(\int\log|T_s'|\,d\mu_s\) because the interval partition generates under uniform expansion. Substitution gives the displayed explicit formula.

The vector \(p=(\lambda^{-3},\lambda^{-2},\lambda^{-1})\) sums to one by \(\lambda^3=1+\lambda+\lambda^2\). The expected return time from \(I_2\) is \(3q_0+2q_1+q_2=N/D\). Hence, writing \(D_{\rm KL}(q\Vert p)=\sum q_j\log(q_j/p_j)\),
\[
D_{\rm KL}(q\Vert p)
=-H(q)+(3q_0+2q_1+q_2)\log\lambda.
\]
Multiplication by \(D/N\) proves the entropy-deficit identity. Gibbs' inequality makes this nonnegative, with equality only if \(q=p\). The ratio \(q_1/q_0=s\) and \(p_1/p_0=\lambda\) proves the unique equality condition \(s=\lambda\). Finally, \((s+2)/N=s^{-1}+O(s^{-3})\) and \(\log(D/s^2)=s^{-1}+O(s^{-2})\), which yield the stated metric-entropy decay.

## Verification

A dependency-free Python script, `verify.py`, checks the postcritical orbit, branch lengths, Frobenius--Perron fixed-point equations, normalization, interval masses, integral mean formula, and analytic mean derivative at 190 distinct rational parameters greater than one. It also checks the tribonacci equation and the entropy-deficit identity numerically at nine parameter values. The exact identities for **all real parameters**, uniqueness, entropy classification, and limiting laws are established by the proof above, not by extrapolating those finitely many checks. To reproduce: run `python verify.py` from the directory containing this document and script.

## Relationship to prior work

The originating 2023 conference contribution [1] introduces tunable-statistics piecewise maps; the expanded full article [2, Secs. 2, 3.1, 5] defines precisely the affine map used here, studies mean variation numerically, and explicitly identifies theoretical mean tuning as a direction for further research. Its published numerical diagrams alone do not imply the four-step critical orbit locus or invariant mean formula.

The full preprint of Alsedà--Misiurewicz--Pérez [3, especially Secs. 2, 3, 5, 7] provides general invariant-density and **entropy-flexibility** theorems for skew-tent maps. In particular, flexibility of metric entropy at fixed topological entropy is **not** asserted to be new here. Our claim instead determines, for the specifically sourced endpoint-tuned family and its canonical period-four postcritical curve, the exact density, strictly monotone physical mean, common tribonacci entropy and finite-state KL deficit with its unique equality parameter. The general flexibility theorem neither states nor numerically supplies these particular formulas. Bruin--Keszthelyi [4] treat a zero-intercept skew-tent family and almost-everywhere critical-orbit density and beta-transformation matching; these are different statements and do not provide the present physical-mean calibration.

## Limitations

The older four-page conference paper [1] was located and its publication date verified, but its complete text was unavailable for direct inspection; its scientific overlap beyond the available abstract therefore remains a priority risk. The full 2023 journal article [2] acknowledges it as a shorter antecedent, but that relationship is not a substitute for reading its complete text. Classical postcritical Markov and entropy methods are acknowledged rather than claimed as newly invented. An unlocated source could still contain an equivalent exact parameter curve or invariant-mean formula. No statistical control is claimed outside the stated one-dimensional parameter curve or for finite-precision iterates. The entropy-flexibility phenomenon by itself is already known from [3]. No independent audit has been performed.

## References

[1] L. Moysis, M. Lawnik, M. S. Baptista, S. K. Goudos, and C. Volos, *Construction of Piecewise Chaotic Maps With Tunable Statistical Mean*, MOCAST 2023, published 17 July 2023, doi:10.1109/MOCAST57943.2023.10176612.

[2] L. Moysis, M. Lawnik, C. Volos, M. S. Baptista, and S. K. Goudos, *Chaotic Maps with Tunable Mean Value—Application to a UAV Surveillance Mission*, Symmetry 15 (2023), 2138, doi:10.3390/sym15122138.

[3] L. Alsedà, M. Misiurewicz, and R. A. Pérez, *Flexibility of Entropies for Piecewise Expanding Unimodal Maps*, arXiv:2004.01813 (2020), especially Theorems 3.1, 5.1 and A.

[4] H. Bruin and G. Keszthelyi, *On co-σ-porosity of the parameters with dense critical orbits for skew tent maps and matching on generalized β-transformations*, arXiv:2106.04711 (2021), Sections 1–2.
