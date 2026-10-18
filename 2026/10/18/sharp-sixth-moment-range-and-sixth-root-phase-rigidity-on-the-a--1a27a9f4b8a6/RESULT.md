# Sharp sixth-moment range and sixth-root phase rigidity on the \(A_2\) Fourier hexagon

## Finding

Let \(S=\{(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\}\subset\mathbb Z^2\), the six-vertex root hexagon in a lattice basis. For arbitrary coefficients \(|c_s|=1\), set
\[
P(z,w)=\sum_{s\in S}c_s z^{s_1}w^{s_2},\qquad (z,w)\in\mathbb T^2.
\]
For normalized Haar probability measure, the **exact attainable range** is
\[
\boxed{546\le\int_{\mathbb T^2}|P(z,w)|^6\,dm(z,w)\le2040.}
\]
Every intermediate real number is attained. The lower equality set comprises exactly **two** orbits under common-phase and two character-phase modulations; the upper equality set comprises exactly **one** orbit.

More explicitly, uniquely gauge the three coefficients at \((1,0),(0,1),(1,1)\) to one. In the resulting polynomial
\[
Q(z,w)=z+w+zw+a z^{-1}+b w^{-1}+c(zw)^{-1},
\qquad |a|=|b|=|c|=1,
\]
the minimum occurs exactly at
\[
\boxed{(a,b,c)=(e^{i\pi/3},e^{-i\pi/3},-1)
\ \text{or}\ (e^{-i\pi/3},e^{i\pi/3},-1)},
\]
and the maximum exactly at \((a,b,c)=(1,1,1)\). In particular, the minimizing coefficient phases are genuinely sixth roots of unity, not just signs or third roots.

For coefficients in the phase alphabet \(\mu_q\), the group of \(q\)-th roots of unity (\(q\ge2\)), the continuous sharp minimum \(546\) is attained **if and only if** \(6\mid q\); in that case exactly \(2q^3\) raw six-coefficient arrays attain it. The sharp maximum \(2040\) is attained for every \(q\), with exactly \(q^3\) raw arrays. All claims, including counts, hold for sampled Fourier averages on \(\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z\) whenever \(m,n\ge7\).

The fourth moment, in the same gauge, is
\[
\boxed{\int_{\mathbb T^2}|Q|^4\,dm=54+4|a+b+c|^2.}
\]
Thus the sixth-moment minimizers also minimize the fourth moment, but sixth-order rigidity selects just two phase orbits from the fourth-moment equilateral condition \(a+b+c=0\).

## Assumptions and scope

The six frequencies are all distinct lattice points, and **every** coefficient is constrained to have modulus one. Integration is with Haar probability measure, with \(\int|P|^2=6\). Character-phase modulation acts as \(c_s\mapsto\lambda\xi^{s_1}\upsilon^{s_2}c_s\) for \(\lambda,\xi,\upsilon\in\mathbb T\). This is an equivalence for the stated orbit classification only; the raw alphabet counts do not quotient by it. For a discrete alphabet, the same multipliers are in \(\mu_q\). The sampled average has normalization \((mn)^{-1}\) and uses the corresponding finite roots of unity.

## Proof

**1. The complete phase gauge.** The three equations setting the coefficients at \((1,0),(0,1),(1,1)\) equal to one have one and only one solution for \((\lambda,\xi,\upsilon)\). Indeed, dividing the third equation by the product of the first two determines \(\lambda\), then the first two determine \(\xi\) and \(\upsilon\). This preserves every even moment and all coefficient magnitudes. If the original coefficients are in \(\mu_q\), these gauge factors remain in \(\mu_q\).

**2. Exact Fourier coefficient enumeration.** For \(m=2,3\), expand \(Q^m\) as a Laurent polynomial. Orthogonality gives
\[
\int|Q|^{2m}dm=\sum_{r\in\mathbb Z^2}\left|
\sum_{\substack{s_1,\ldots,s_m\in S\\s_1+\cdots+s_m=r}}
 c_{s_1}\cdots c_{s_m}\right|^2.
\]
For \(m=2\), grouping the sum yields \(54+4|a+b+c|^2\). For \(m=3\), an exact grouping by phase monomial yields
\[
\begin{aligned}
M_6={}&996+288\operatorname{Re}(\bar a b+\bar a c+\bar b c)
+72\operatorname{Re}(c\bar a\bar b)\\
&+18\operatorname{Re}(\bar a+\bar b+c\bar a^2+c\bar b^2
+c^2\bar a^2\bar b+c^2\bar a\bar b^2).
\end{aligned}
\tag{1}
\]
This identity is a finite equality of Laurent polynomials with integer coefficients, not a numerical fit. The independent exact checker enumerates its 21 nonzero phase-monomial coefficients from the original six frequencies.

**3. Three real variables and one positive coefficient.** Choose real angles \(\alpha,\beta,\phi\) so that
\[
a=e^{i(\alpha+\beta)},\quad
b=e^{i(\alpha-\beta)},\quad
c=e^{i(\alpha+\phi)}.
\]
Every unimodular triple has such a representation. Write \(t=\cos\beta\), \(h=\cos\phi\) and \(X=t^2+th\). Substituting into (1), using elementary cosine identities, gives the **exact** identity
\[
\boxed{M_6=708+576X+36(1+2X)\cos(\phi-\alpha).}
\tag{2}
\]
As \(t,h\in[-1,1]\), we have \(X\ge t^2-|t|\ge-1/4\), so the coefficient \(1+2X\ge1/2\) is strictly positive. Therefore
\[
M_6\ge672+504X\ge672+504(t^2-|t|)\ge546.
\]
Equality forces \(|t|=1/2\), \(h=-\operatorname{sgn}(t)\), and \(\cos(\phi-\alpha)=-1\). If \(t=1/2\) one can take \(\beta=\pm\pi/3\), \(\phi=\pi\), and \(\alpha=0\), giving precisely \((a,b,c)=(e^{\pm i\pi/3},e^{\mp i\pi/3},-1)\). If \(t=-1/2\), shifting both \(\alpha\) and \(\beta\) by \(\pi\), together with the corresponding angle representation, gives the same two triples. Thus there are no additional equality points.

Similarly, \(X\le t^2+|t|\le2\), so
\[
M_6\le744+648X\le744+648(t^2+|t|)\le2040.
\]
Equality entails \(|t|=1\), \(h=\operatorname{sgn}(t)\), and \(\cos(\phi-\alpha)=1\), which reduces exactly to \(a=b=c=1\). Direct substitution attains both endpoints. Since the coefficient phase torus \(\mathbb T^6\) is connected and the moment map continuous, the entire closed interval is attained.

**4. Alphabet rigidity and exact counts.** Both minimizing triples contain a primitive sixth root of unity; thus no \(q\)-phase array attains \(546\) unless \(6\mid q\). Conversely both triples belong to \(\mu_q^3\) when \(6\mid q\). The unique complete phase gauge gives exactly \(q^3\) original coefficient arrays for each normalized triple, hence \(2q^3\) total. The single normalized maximizer yields \(q^3\) maximizers, with no overlap.

**5. Finite sampling.** The frequencies in \(Q^3\) have coordinates in \([-3,3]\). If \(m,n\ge7\), distinct such integer vectors have distinct residue classes modulo \((m,n)\). Fourier orthogonality on the finite torus therefore gives exactly the same squared-coefficient sum as in step 2. The fourth moment likewise has no aliasing, so the proofs and counts carry over unchanged. No assertion is made for grids below this threshold.

## Verification

Execute `python3 checker.py` using Python 3 standard library. It independently enumerates the Laurent coefficients of \(Q^2\) and \(Q^3\), reconstructs both moment identities, proves the trigonometric form as an equality of rational Laurent polynomials, and checks all \(6^3=216\) gauge-normalized sixth-root phase triples using exact arithmetic in \(\mathbb Z[e^{i\pi/3}]\). That exhaustive **finite-alphabet** check finds precisely two minimizers and one maximizer. It also checks triple-sum injectivity on sample grid orders \(7,8,11\). The all-phase lower and upper bounds and all-grid statement instead follow from steps 3–5, and are not inferred from the finite checker.

## Relationship to prior work

The standard even-exponent Fourier coefficient identity and coefficientwise-majorant viewpoint are explained by Mockenhaupt and Schlag (2002). Their general results concern majorant estimates and do not imply a sharp **lower** phase-constrained sixth moment on this fixed two-dimensional hexagonal support. Püschel and Rötteler (2007) place hexagonal-lattice Fourier transforms in an algebraic signal-processing setting, but their accessible abstract does not settle the present finite phase-extremal problem; the complete paper was not inspected. Blake, Hall and Tirkel (2013) construct perfect periodic and zero-correlation-zone root-of-unity arrays, whereas the present theorem concerns a single sparse six-frequency aperture and its exact sixth-moment range.

Published calculations on the degree-two **triangular** six-mode aperture describe a different frequency geometry and the **fourth**, not sixth, moment. Sharp sixth-moment Fourier inequalities for a **one-dimensional four-frequency** interval describe another spectrum and optimize a different coefficient constraint. Neither statement logically yields (1)–(2), the sixth-root rigidity, or the alphabet counts here. The compared full statements and remaining possible bibliographic overlap are recorded in the accompanying review.

## Limitations

The theorem is restricted to the full six-vertex \(A_2\) root hexagon with unimodular coefficients, to fourth and sixth moments as stated, and to alias-free finite grids. It does not give optimality among all six-frequency subsets, arbitrary coefficient magnitudes, higher moments, correlation peak minimization, or smaller finite tori. Some older hexagonal phased-array or polyphase sequence literature may contain an equivalent computation not indexed in the inspected sources. Independent mathematical and publication-priority audits have not been performed.

## References

- G. Mockenhaupt and W. Schlag, *On the Hardy--Littlewood majorant problem for random sets*, arXiv:math/0207226v1 (first public 2002-07-25), https://arxiv.org/abs/math/0207226.
- M. Püschel and M. Rötteler, *Algebraic Signal Processing Theory: 2-D Spatial Hexagonal Lattice*, IEEE Transactions on Image Processing 16 (2007), DOI:10.1109/TIP.2007.896626.
- S. Blake, T. Hall and A. Tirkel, *Arrays over roots of unity with perfect autocorrelation and good ZCZ cross-correlation*, Advances in Mathematics of Communications 7 (2013), DOI:10.3934/amc.2013.7.231.
