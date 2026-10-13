# Quadratic onset of single-use private information at the hybrid BSC/BPC threshold
## Finding
Consider the hybrid binary classical--quantum wiretap channel in which Bob receives \(\mathrm{BSC}(p)\) and Eve receives one of two pure states with overlap \(a=1-2p\), for \(0<p<1/2\). Let
\[
F(a)=(1-a^2)\operatorname{atanh}(a)-a^3.
\]
There is a unique \(a_*\in(0,1)\) with \(F(a_*)=0\). Put \(p_*=(1-a_*)/2\). Numerically,
\[
a_*\approx0.751759503599112,
\qquad
p_*\approx0.124120248200444.
\]
With natural logarithms, so that information is measured in nats, the single-use private information satisfies
\[
C^{(1)}(p)=K_*(p_*-p)^2+o\!\left((p_*-p)^2\right)
\qquad (p\uparrow p_*),
\]
where
\[
K_*=
\frac{6F'(a_*)^2}{3-6a_*^2+3a_*^4-2a_*^6}
\approx136.236236139043.
\]
There is also a geometric companion law for the optimizing convex envelope. Write \(z=1-2x\), where \(x\) is the probability of input symbol \(1\). For \(p<p_*\) sufficiently close to \(p_*\), let \(z_p>0\) be the contact point at which the lower convex envelope leaves its central flat segment. Then
\[
z_p=L_*\sqrt{p_*-p}+o\!\left(\sqrt{p_*-p}\right),
\]
with
\[
L_*=
\sqrt{\frac{-12a_*F'(a_*)}{3-6a_*^2+3a_*^4-2a_*^6}}
\approx9.72830498723646.
\]
Thus the threshold is a quadratic convex-envelope bifurcation: the pooling interval opens at square-root scale, while the single-use private information opens at quadratic scale.

## Assumptions and scope
The result concerns only the one-parameter line in the hybrid wiretap family on which Bob's crossover probability and the parameter defining Eve's pure-state overlap are both \(p\). Entropies use natural logarithms. Let \(\Delta_p(z)\) denote the source entropy difference in the affine coordinate \(z=1-2x\):
\[
\Delta_p(z)=
 h\!\left(\frac{1+az}{2}\right)
 -h\!\left(\frac{1+r}{2}\right),
\qquad
r=\sqrt{a^2+(1-a^2)z^2},
\]
where \(a=1-2p\) and \(h(y)=-y\log y-(1-y)\log(1-y)\). The binary-input convex-envelope formula gives
\[
C^{(1)}(p)=\max_z\bigl(\Delta_p(z)-\Delta_{p,\mathrm{vex}}(z)\bigr).
\]
The statement is asymptotic as \(p\uparrow p_*\) from below. It does not assert any expansion for multi-use private information or private capacity.

## Proof
First, \(F(0)=0\), \(F(a)>0\) for sufficiently small positive \(a\), and \(F(a)\to-1\) as \(a\to1^-\). Moreover,
\[
F'(a)=1-3a^2-2a\operatorname{atanh}(a),
\]
\[
F''(a)=-6a-2\operatorname{atanh}(a)-\frac{2a}{1-a^2}<0
\qquad(0<a<1).
\]
Hence \(F'\) is strictly decreasing from \(1\), so \(F\) has exactly one positive zero \(a_*\).

The recent source gives, with \(u=a^2\), \(k=1-u\), \(t=z^2\), and \(r=\sqrt{u+kt}\),
\[
\Delta_p''(z)=
-\frac{u}{1-ut}
+\frac{ku\operatorname{atanh}(r)}{r^3}
+\frac{k^2t}{r^2(1-r^2)}.
\]
At \(z=0\), this becomes
\[
A(p):=\Delta_p''(0)=\frac{F(a)}{a}.
\]
Thus \(A(p_*)=0\), while \(A(p)<0\) for \(p<p_*\) sufficiently close to \(p_*\).

At the threshold, the first convexity condition in the source is an equality, \((1-a_*^2)\operatorname{atanh}(a_*)=a_*^3\). Its second condition is strict. Indeed, if \(b=\tanh 1\), then \(F(b)=1-b^2-b^3<0\): one may note that \(b>19/25\), while \(1-(19/25)^2-(19/25)^3<0\). Hence \(a_*<\tanh1\), so \(\operatorname{atanh}(a_*)<1\), and the threshold equation gives
\[
1-a_*^2=\frac{a_*^3}{\operatorname{atanh}(a_*)}>a_*^3.
\]
Consequently the source's second convexity inequality is strict. Its proof then gives \(\Delta_{p_*}''(z)>0\) for every \(z\ne0\), while \(\Delta_{p_*}''(0)=0\). Therefore the loss of convexity as \(p\) decreases through \(p_*\) is localized at the symmetric point \(z=0\).

Differentiate the displayed formula for \(\Delta_p''\) with respect to \(t=z^2\) and then impose \(F(a_*)=0\). This yields
\[
B_*:=\Delta_{p_*}^{(4)}(0)
=
\frac{3-6a_*^2+3a_*^4-2a_*^6}{a_*^2}>0.
\]
The positivity also follows from the strict second convexity condition because the numerator equals \(3(1-a_*^2)^2-2a_*^6\).

Set \(\delta=p_*-p\). Since \(a=a_*+2\delta\),
\[
A(p)=-c_*\delta+O(\delta^2),
\qquad
c_*=-\frac{2F'(a_*)}{a_*}>0.
\]
Analyticity near \((p_*,z)\) gives
\[
\Delta_p'(z)=A(p)z+\frac{B_*}{6}z^3+O\!\left(\delta z^3+z^5\right).
\]
For sufficiently small positive \(\delta\), strict convexity away from the origin and the preceding local expansion imply a unique positive local minimum \(z_p\to0\). Solving \(\Delta_p'(z_p)=0\) gives
\[
z_p^2=\frac{6c_*}{B_*}\delta+o(\delta),
\]
which is the claimed square-root law.

Because \(\Delta_p\) is even, decreases on \((0,z_p)\), is convex and increasing after \(z_p\), and has equal minima at \(\pm z_p\), its lower convex envelope is constant on \([-z_p,z_p]\) and agrees with \(\Delta_p\) immediately outside that interval. Hence the largest envelope gap is at \(z=0\):
\[
C^{(1)}(p)=\Delta_p(0)-\Delta_p(z_p).
\]
Taylor expansion gives
\[
\Delta_p(0)-\Delta_p(z_p)
=\frac{3A(p)^2}{2B_*}+o(\delta^2)
=\frac{3c_*^2}{2B_*}\delta^2+o(\delta^2).
\]
Substituting the formulas for \(c_*\) and \(B_*\) gives exactly
\[
K_*=
\frac{6F'(a_*)^2}{3-6a_*^2+3a_*^4-2a_*^6}.
\]

## Verification
The proof is analytic; no finite experiment is used to infer the asymptotic law. The accompanying checker independently bisects the unique root of \(F\), evaluates \(K_*\) and \(L_*\), and directly evaluates the entropy difference for several small deficits. The ratios \(C^{(1)}(p)/(p_*-p)^2\) approach the stated coefficient, while \(z_p/\sqrt{p_*-p}\) approaches the stated contact-width coefficient.

As an external numerical cross-check rather than proof, the recent source reports \(C^{(1)}\approx4.514\times10^{-8}\) nats at \(p=0.124102\). The leading formula above predicts approximately \(4.537\times10^{-8}\) nats, as expected at that finite distance from the threshold.

## Relationship to prior work
Tikku, Berta, and Renes identified the same hybrid channel and the threshold equation for \(p_*\), reporting \(p_*\approx0.1241\) and establishing convexity above it by a numerical check of the second derivative. Hayashi and Salek supplied the binary convex-envelope formula used here, an analytic expression for \(\Delta_p''\), a sufficient global convexity lemma, a rigorous zero-single-use witness at \(p=621/5000\), and numerical values close to the threshold. Neither inspected source states a one-sided expansion of \(C^{(1)}\), a critical exponent, the exact coefficient \(K_*\), or the square-root law for the convex-envelope contact point.

A quantitative channel-comparison paper by Kougang-Yombi and Hązła also characterizes convex-envelope advantages for the classical \(\mathrm{BSC}/\mathrm{BEC}\) pair. Its channel pair is different: Eve's output there is classical erasure rather than the pure-state channel considered here, so its formulas do not imply the coefficient above.

## Limitations
This is a local theorem near \(p_*\). It does not determine the multi-use private-information scaling, the private-capacity scaling, or the size of the nonadditivity gap. It also does not claim that the same quadratic law holds for arbitrary perturbations away from the one-parameter line. The numerical constants are evaluations of exact formulas; the asymptotic proof itself depends only on the displayed analytic identities and the cited convexity result.

## References
1. M. Hayashi and F. Salek, *From Symmetry to Secrecy: Covariant Classical--Quantum Wiretap Channels*, arXiv:2610.03580v1 (2026).
2. A. Tikku, M. Berta, and J. M. Renes, *Non-additivity in classical-quantum wiretap channels*, arXiv:2002.06580v2 (2020); IEEE Journal on Selected Areas in Information Theory 1, 526--535 (2020).
3. D. Kougang-Yombi and J. Hązła, *A Quantitative Version of More Capable Channel Comparison*, arXiv:2401.14214v1 (2024).
