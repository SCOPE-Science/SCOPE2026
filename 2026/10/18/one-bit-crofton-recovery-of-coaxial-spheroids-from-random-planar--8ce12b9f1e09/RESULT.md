# One-bit Crofton recovery of coaxial spheroids from random planar sections

## Finding
Consider two disjoint, congruent solid spheroids with the same symmetry axis in Euclidean \(\mathbb R^3\). Their centers lie distance \(d\) apart on that axis, the axial semiaxis is \(a\), and the transverse semiaxis is \(b\), where \(a,b>0\) and \(d>2a\). Sample a motion-invariant affine plane conditioned to meet their union, and let \(N\in\{1,2\}\) be the number of connected components (elliptical disks) in its section.

Set \(c=\sqrt{|a^2-b^2|}\) and define \(I=I(a,b,d)\) and \(J=J(a,b)\) by
\[
I=\begin{cases}
\dfrac{b^2}{c}\operatorname{artanh}\!\left(\dfrac{2c}{d}\right),&a>b,\\
\dfrac{2a^2}{d},&a=b,\\
\dfrac{b^2}{c}\arctan\!\left(\dfrac{2c}{d}\right),&a<b,
\end{cases}
\qquad
J=\begin{cases}
\dfrac a2+\dfrac{b^2}{2c}\operatorname{arsinh}\!\left(\dfrac cb\right),&a>b,\\
a,&a=b,\\
\dfrac a2+\dfrac{b^2}{2c}\arcsin\!\left(\dfrac cb\right),&a<b.
\end{cases}
\]
Then the **complete section-topology law** is
\[
\Pr(N=2)=\frac{I}{4J-I},\qquad
\Pr(N=1)=\frac{4J-2I}{4J-I}.
\]
For each fixed \(a>0\) and \(d>2a\), the function \(b\mapsto\Pr(N=2)\) is continuous and **strictly increasing on \((0,\infty)\)**, from zero to one. Therefore this single binary section-topology probability uniquely determines the transverse semiaxis \(b\) when \(a\) and \(d\) are known. In particular the sphere case is \(\Pr(N=2)=a/(2d-a)\), and for fixed \(a,d\) the sharp two limiting rates are
\[
\Pr(N=2)=\frac{b^2}{2a^2}\operatorname{artanh}\!\left(\frac{2a}{d}\right)
 +O_{a,d}\!\left(b^4\log(a/b)\right)\quad(b\downarrow0),
\]
\[
1-\Pr(N=2)=\frac{2d}{\pi b}+O_{a,d}(b^{-2})\quad(b\to\infty).
\]

## Assumptions and scope
The two solids are \(E_\pm=\{(x,y,z): (x^2+y^2)/b^2+(z\mp d/2)^2/a^2\le1\}\). The restriction \(d>2a\) makes them disjoint for every \(b>0\). An unoriented plane has equation \(u\cdot X=t\), with \(u\in S^2\); the Euclidean-motion-invariant plane measure is proportional to \(d\sigma(u)\,dt\). Conditioning is on meeting \(E_+\cup E_-\). Tangency events have zero measure. The profile is a disk if precisely one spheroid is hit and two disjoint disks if both are hit. All probabilities are exact, not simulation estimates.

## Proof
Write \(x=|u_z|\). Under uniform direction on \(S^2\), \(x\) is uniform on \([0,1]\). The projected halfwidth of either spheroid on the normal direction is
\[
h_b(x)=\sqrt{b^2+(a^2-b^2)x^2}.
\]
Their projected offset intervals have length \(2h_b(x)\), with center separation \(dx\). Consequently their common offset interval has length \((2h_b(x)-dx)_+\), while the union has offset length \(4h_b(x)-(2h_b(x)-dx)_+\). Integrating against invariant plane measure and then conditioning gives
\[
I=\int_0^1(2h_b(x)-dx)_+\,dx,\qquad
J=\int_0^1h_b(x)\,dx,\qquad
\Pr(N=2)=\frac I{4J-I}.
\]
As \(d>2a\), the positive part switches off at the unique threshold
\[
x_0=\frac{2b}{\sqrt{d^2-4(a^2-b^2)}}\in(0,1).
\]
At that point \(h_b(x_0)=dx_0/2\). For \(a>b\), elementary integration of \(h_b\) gives
\[
I=\frac{b^2}{c}\operatorname{arsinh}\!\left(\frac{cx_0}{b}\right)
=\frac{b^2}{c}\operatorname{artanh}\!\left(\frac{2c}{d}\right),
\]
and the stated \(J\); for \(a<b\) the same cancellation gives the displayed \(\arctan\) and \(\arcsin\) expressions. At \(a=b\), integrate \(h_b=a\) directly. This proves the exact law for both prolate and oblate spheroids.

For strict monotonicity, set \(\beta=b^2\), \(J_\beta=\int_0^1h_\beta(x)\,dx\), and define a probability density \(p_\beta(x)=h_\beta(x)/J_\beta\) on \([0,1]\). Put \(\phi_\beta(x)=(2-dx/h_\beta(x))_+\). Then \(I/J_\beta=\int\phi_\beta p_\beta\). For \(\beta>0\),
\[
\partial_\beta\log h_\beta(x)
=\frac{1-x^2}{2\{\beta+(a^2-\beta)x^2\}}
\]
is strictly decreasing in \(x\in(0,1)\): its derivative equals \(-a^2x/h_\beta(x)^4<0\). Thus if \(\beta_2>\beta_1\), the likelihood ratio \(p_{\beta_2}/p_{\beta_1}\) decreases strictly in \(x\), so the former distribution is stochastically smaller. On the other hand, \(x/h_\beta(x)\) strictly increases with \(x\) (derivative \(\beta/h_\beta^3>0\)) and decreases with \(\beta\), so \(\phi_\beta\) is nonincreasing in \(x\) and nondecreasing in \(\beta\), with strict growth on a nonempty open interval. Stochastic ordering followed by pointwise strict growth shows that \(I/J_\beta\) is strictly increasing in \(\beta\). Since \(y\mapsto y/(4-y)\) strictly increases on \((0,2)\), so does the two-component probability.

For \(b\downarrow0\), the prolate formula gives \(I=(b^2/a)\operatorname{artanh}(2a/d)+O_{a,d}(b^4)\) and \(J=a/2+O_a(b^2\log(a/b))\). For \(b\to\infty\), the oblate formula gives \(I=\pi b/2-d/2+O_{a,d}(b^{-1})\) and \(4J=\pi b+O_a(b^{-1})\). Substitution proves both rates and the limiting values. The intermediate-value theorem and strict monotonicity prove global inverse uniqueness.

## Verification
The accompanying `check.py` evaluates independently the normal-offset integrals by quadrature in eleven prolate, spherical, and oblate cases; checks strict increase on three grids of 151 transverse semiaxes; numerically inverts the probability in four examples; checks both limiting rates; and conducts a total of 3,300,000 samples in two distinct random-plane tests, including direct offset sampling and rejection on union hits. It prints `SPHEROID_PAIR_CROFTON_OK` when all tests pass. All infinite and uniqueness claims follow from the exact calculus and likelihood-ratio argument, not from finite sampling.

## Relationship to prior work
Classical stereology develops invariant flat-sampling measures and second-moment formulas; see Voss and Cruz-Orive (2009), especially their Sections 1–2 and Appendix A. Rigaut (1985) studies co-observation of paired **spheres**, a strict special case of the present family. The spherical probability is acknowledged here as background rather than a new theorem. The present contribution is the full non-spherical closed form, the strictly monotone continuous passage from prolate to oblate shapes, the global binary-observation inverse theorem, and the two sharp degeneration rates. A complete priority examination of older paired-particle stereology is not claimed.

## Limitations
The bodies must be congruent, coaxial spheroids separated along their common axis. The inverse theorem assumes the axial semiaxis and center separation are known; it does not reconstruct their positions or rotations without those calibrations. It yields exact population identifiability, not finite-sample statistical stability or independent validation. Some older paired-sphere literature was not accessible in full text.

## References
- F. Voss and L. M. Cruz-Orive, *Second moment formulae for geometric sampling with test probes*, Statistics 43 (2009), 329–365, DOI 10.1080/02331880802399783. Public full-text preprint: https://www.uni-ulm.de/fileadmin/website_uni_ulm/mawi.inst.110/mitarbeiter/voss/Voss-CruzOrive.07.11.pdf.
- J.-P. Rigaut, *The 'bi-corpuscle' stereological problem: estimation of distributions of distances between paired spheres*, Journal of Microscopy 138 (1985), 189–201, DOI 10.1111/j.1365-2818.1985.tb02612.x (abstract consulted; full text not verified).
- L. A. Santaló, *Integral Geometry and Geometric Probability*, Addison-Wesley (1976), background on invariant plane measures.
