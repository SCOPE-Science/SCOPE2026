# Sharp radius scaling for simultaneous Fourier-threshold correlations

## Finding

Let \(f:\mathbb T\to[-1,1]\) be a continuous, even, antipodal wave, strictly decreasing on \([0,1/2]\), with \(f(0)=1\) and \(f(t+1/2)=-f(t)\). Let \(A\) be any finite nonempty set of distinct positive integers. For \(0<r\le1/4\) define \(\alpha_r=f(r)\) and
\[
P_r(A)=\mu\left\{t\in\mathbb T:\text{either } f(at)>\alpha_r\text{ for every }a\in A,
\text{ or } f(at)<-\alpha_r\text{ for every }a\in A\right\},
\]
where \(\mu\) is normalized Haar measure.

**Sharp scale-interpolation theorem.** For arbitrary \(0<r\le s\le1/4\) and arbitrary finite nonempty \(A\),
\[
\boxed{\frac{P_r(A)}r\le\frac{P_s(A)}s.}\tag{1}
\]
The coefficient \(1\) in (1) is best possible for every cardinality \(n=|A|\) and every pair of radii: for
\[
A_n=\{1,3,3^2,\ldots,3^{n-1}\},\qquad P_r(A_n)=\frac{4r}{3^{n-1}}
\]
for **every** \(0<r\le1/4\). Moreover, for each fixed \(A\), the function \(r\mapsto P_r(A)\) is continuous and piecewise affine on \((0,1/4]\), with finitely many rational breakpoints and rational affine coefficients. Thus the threshold-dependence of any prescribed frequency set has a finite exact algebraic description.

As a sharp application, the optimal two-frequency value is determined on an **entire interval of nonreciprocal radii**:
\[
\boxed{\inf_{1\le a<b}P_r(\{a,b\})=\frac{4r}{3}\qquad\text{for every }\frac15\le r\le\frac14.}\tag{2}
\]
The pair \(\{1,3\}\), and each of its common positive-integer dilations, realizes (2). No classification of all optimizers for interior radii is asserted. In the cosine case \(f(t)=\cos(2\pi t)\), formula (2) covers the full threshold interval \(0\le\alpha\le\cos(2\pi/5)\), not just reciprocal sampling values.

## Assumptions and scope

All angles are modulo one. The assumed shape of \(f\) makes its positive and negative threshold sets, up to null boundaries, respectively the arcs \(\|t\|_{\mathbb T}<r\) and \(\|t-1/2\|_{\mathbb T}<r\). Therefore the theorem depends on the waveform only through its level radius \(r\). The upper constraint \(r\le1/4\) ensures the two sign sets do not overlap and each individual frequency's collection of component arcs is disjoint.

The exact interval formula (2) does **not** assert a solution for \(r<1/5\), for non-antipodal profiles, or for three or more optimal frequencies. The universal scaling statement (1) does apply to every finite positive-frequency set of arbitrary cardinality, whether or not its frequencies share a common factor.

## Proof

**1. Scale monotonicity of a single intersection component.** Fix the sign, either positive or negative. For each frequency \(a\in A\), the relevant lifted arcs on the real line have respective centers \(c_a=j/a\) or \(c_a=(j+1/2)/a\) with \(j\in\mathbb Z\), and half-length \(r/a\). Choose one center in the first frequency's orbit as a representative modulo simultaneous translation by an integer. For any resulting center tuple \(\mathbf c=(c_a)_{a\in A}\), the component intersection, if nonempty, has length
\[
L_{\mathbf c}(r)=\left[\min_{a\in A}\left(c_a+\frac ra\right)
-\max_{a\in A}\left(c_a-\frac ra\right)\right]_+,
\qquad [x]_+=\max\{x,0\}.
\]
There are only finitely many center tuples whose intervals can intersect for some \(0<r\le1/4\), modulo integral translation. Because component arcs of each fixed frequency are disjoint at these radii, the corresponding intersections are disjoint up to endpoints. Therefore their lengths sum exactly to the Haar measure of the common-positive or common-negative event, respectively.

Put \(u=1/r\) and write
\[
H_{\mathbf c}(u)=\min_{a\in A}(uc_a+1/a)-\max_{a\in A}(uc_a-1/a).
\]
The first term is concave in \(u\); the second is convex. Thus \(H_{\mathbf c}\) is concave on \([0,\infty)\). All its defining intervals have length at least the shortest interval, and the length of their intersection can never exceed \(2/\max A\). At \(u=0\), every center has collapsed to zero, so \(H_{\mathbf c}(0)=2/\max A\), its global maximum. A concave function on \([0,\infty)\) having its maximum at the left endpoint is nonincreasing. Hence
\[
\frac{L_{\mathbf c}(r)}r=[H_{\mathbf c}(1/r)]_+
\]
is nondecreasing in \(r\). Summing over the finitely many center tuples and both signs proves (1). Since all lifted centers are rational and all half-length endpoints depend affinely on \(r\), the same finite decomposition proves continuity and piecewise-affine dependence with rational coefficients and rational breakpoints.

**2. Sharpness at every cardinality.** Set \(A_n=\{3^j:0\le j<n\}\). If \(\|t\|_{\mathbb T}<r\) and \(\|3t\|_{\mathbb T}<r\), the central component is the only possible common positive component: the closest edge of a noncentral \(3\)-frequency arc is at \((1-r)/3\ge r\) for \(r\le1/4\). Inductively, after imposing the first \(j\) frequencies, the positive set is the central arc \(\|t\|_{\mathbb T}<r/3^{j-1}\); imposing \(3^j\) leaves \(\|t\|_{\mathbb T}<r/3^j\). All frequencies are odd, so translation by \(1/2\) carries this positive set onto the negative set, disjoint from it. Their combined measure is precisely \(4r/3^{n-1}\) for every claimed radius. This attains equality in (1) for any \(0<r\le s\le1/4\), so no larger universal multiplicative constant is possible.

**3. A self-contained reciprocal-radius input for the sharp interval.** We show
\[
\inf_{1\le a<b}P_{1/5}(\{a,b\})=\frac4{15}.\tag{3}
\]
Common integer factors can be divided out. For coprime \(a<b\), let \(B(x)=\{x\}^2-\{x\}+1/6\), the periodic second Bernoulli polynomial. It is even modulo integers and globally 1-Lipschitz. Fourier orthogonality for the two threshold arcs gives the exact identity
\[
P_{1/5}(\{a,b\})=\frac8{25}+
\begin{cases}
\displaystyle\frac2{ab}\left[B\!\left(\frac{b-a}{5}\right)-B\!\left(\frac{b+a}{5}\right)\right],&a,b\text{ odd},\\[3mm]
\displaystyle\frac1{2ab}\left[B\!\left(\frac{2(b-a)}5\right)-B\!\left(\frac{2(b+a)}5\right)\right],&a,b\text{ of opposite parity}.
\end{cases}\tag{4}
\]
To derive (4), the coefficient of the indicator of \(\|t\|_{\mathbb T}<1/5\) at a nonzero integer \(k\) is \(\sin(2\pi k/5)/(\pi k)\), while the negative arc introduces the factor \((-1)^k\). After integrating the product of the two series, the identity \(\sum_{k\ge1}\cos(2\pi k x)/k^2=\pi^2B(x)\) gives (4).

For odd \(a,b\), the common central positive arc and its antipodal negative translate yield \(P\ge4/(5b)\), which is at least \(4/15\) if \(b\le3\). The 1-Lipschitz property in (4) gives \(P\ge8/25-4/(5b)\), which is at least \(4/15\) if \(b\ge15\). The remaining odd values of \(b\), with their **exact minimum** over eligible coprime odd \(a<b\), are
\[
\begin{array}{c|ccccc} b&5&7&9&11&13\\\hline
\min P&8/25&32/105&4/15&52/165&4/13\end{array}.
\]
For opposite parity, the same arc argument gives \(P\ge2/(5b)\) and the Bernoulli estimate gives \(P\ge8/25-2/(5b)\ge4/15\) whenever \(b\ge8\). The remaining values \(2\le b\le7\) have exact minimum \(3/10\), again above \(4/15\), across all coprime opposite-parity \(1\le a<b\). The finite minima are complete arithmetic substitutions into (4), verified by the accompanying exact-rational checker. Finally, \(\{1,3\}\) has measure \(4/15\), proving (3).

**4. Interpolation gives the entire sharp interval.** For \(1/5\le r\le1/4\), apply (1) with the smaller radius \(1/5\) and the pair \(\{a,b\}\). By (3), every pair satisfies
\[
P_r(\{a,b\})\ge5rP_{1/5}(\{a,b\})\ge\frac{4r}{3}.
\]
Step 2 with \(n=2\) gives equality for \(\{1,3\}\). Thus (2) follows. \(\square\)

## Verification

The standalone `CHECK.py` compares the exact rational interval-intersection construction to the two-frequency Bernoulli formula (4), validates every finite exceptional case used in (3), and checks the general all-cardinality scale inequality for a deterministic family of finite frequency sets at rational radii. It verifies the powers-of-three sharpness identity and the sharp continuous interval formula at multiple rational radii. The finite calculations test the formulas and exceptional arithmetic tables; the general inequality for all cardinalities and all real radii follows from the concavity argument, not from finite enumeration.

## Relationship to prior work

The classical cosine-sign two-frequency bound at \(r=1/4\), as proved by Gonçalves, Oliveira e Silva and Steinerberger (2019), determines the sign-only endpoint. Dou, Goh, Liu, Legate and Pettigrew (2022) investigate larger frequency families at the same threshold. Zang, Zhao, Zhao and Zhou's *Extremal cosine sign correlations* (first public 2026-10-23) establishes sharp four-frequency sign-only results and general frequency-count bounds. Giannitsi and Madrid's *Exponential decay of threshold correlations for symmetric periodic functions* (first public 2026-10-28) defines the continuous-threshold problem and establishes a universal \(F_\alpha(n)\) lower bound and asymptotic exponential decay, but does not state a sharp all-cardinality linear radius-comparison inequality, rational radius stratification, or an exact two-frequency formula on a nontrivial interval of positive thresholds. The latter publication is used only as later scientific context; the motivating sign-correlation source predates it.

The reciprocal-radius two-frequency result at \(r=1/5\) is treated as prior mathematical coverage, **not** a novel claim. Step 3 reproduces a complete independent proof of that input so the continuous-radius result needs no earlier package. The new contributions assessed here are the all-cardinality sharp scale-interpolation theorem and its continuum sharpness consequence. No novelty claim is made for individual Fourier-series or interval-overlap identities.

## Limitations

The comparison requires *unshifted* integer dilates with a common symmetric threshold radius, and applies to threshold radii at most \(1/4\). It does not compare arbitrary phase-shifted waves, solve the sharp multi-frequency minimization for \(n\ge3\), or determine the optimum outside the exhibited two-frequency interval. Finite checker runs are supplementary, not a proof for unbounded frequencies. An older unindexed version of the geometric normalized-overlap monotonicity remains a residual priority risk.

## References

1. F. Gonçalves, D. Oliveira e Silva, S. Steinerberger, *A Universality Law For Sign Correlations of Eigenfunctions of Differential Operators*, arXiv:1903.06826 (2019), https://arxiv.org/abs/1903.06826.
2. S. Dou, A. Goh, K. Liu, M. Legate, G. Pettigrew, *Cosine Sign Correlation*, arXiv:2212.02496 (2022), https://arxiv.org/abs/2212.02496.
3. S. Zang, Y. Zhao, Y. Zhao, C. Zhou, *Extremal cosine sign correlations*, arXiv:2610.33190, first public 2026-10-23, https://arxiv.org/abs/2610.33190.
4. C. Giannitsi, J. Madrid, *Exponential decay of threshold correlations for symmetric periodic functions*, arXiv:2610.38135, first public 2026-10-28, https://arxiv.org/abs/2610.38135.
