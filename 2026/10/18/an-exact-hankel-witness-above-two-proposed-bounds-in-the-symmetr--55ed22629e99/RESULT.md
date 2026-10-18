# An exact Hankel witness above two proposed bounds in the symmetric H-domain class

## Finding
Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), let
\[
\Phi(w)=1+w+\frac{w^2}{3}-\frac{w^3}{9},
\qquad
\omega(z)=\frac{z(9z^2-3z+1)}{z^2-3z+9},
\]
and write \(P=\Phi\circ\omega\). Define \(P_e(z)=(P(z)+P(-z))/2\) and \(P_o(z)=(P(z)-P(-z))/2\), and let
\[
u(z)=z\exp\left(\int_0^z \frac{P_e(t)-1}{t}\,dt\right),
\qquad
v(z)=\int_0^z\frac{u(t)P_o(t)}{t}\,dt,
\qquad f=u+v.
\]
The integrands have removable singularities at zero. Then \(f\) is normalized, univalent, and belongs to the symmetric H-domain Sakaguchi class
\[
\mathcal S^*_{\mathrm{sym}}(\Phi)=\left\{F\in\mathcal S:\ \frac{2zF'(z)}{F(z)-F(-z)}=\Phi(\sigma(z))\ \text{for some Schwarz function }\sigma\right\},
\]
where \(\mathcal S\) is the normalized univalent class. Nevertheless, its third-order Hankel determinant equals
\[
H_{3,1}(f)=\det\begin{pmatrix}1&b_2&b_3\\b_2&b_3&b_4\\b_3&b_4&b_5\end{pmatrix}
=-\frac{173595619}{2754990144},
\quad f(z)=z+\sum_{j\ge2}b_jz^j.
\]
Consequently
\[
|H_{3,1}(f)|-\frac{769}{12288}
=\frac{75810133}{176319369216}>0,
\qquad
|H_{3,1}(f)|-\frac1{16}
=\frac{1408735}{2754990144}>0.
\]
Thus this single explicit member of the class contradicts the universal upper bound of Theorem 1 in Tayyah--Hadi--Lupaş (2026) and the smaller bound proposed in Conjecture 1 of Lupaş--Tayyah--Sokół (2025). This is a counterexample, not a determination of the optimal upper bound.

## Assumptions and scope
The only variable domain is the open unit disk \(\mathbb D\). A Schwarz function is holomorphic \(\sigma:\mathbb D\to\mathbb D\) with \(\sigma(0)=0\). A normalized univalent function is holomorphic and injective with \(f(0)=0\) and \(f'(0)=1\). The assertions use the ordinary coefficient Hankel determinant, not an inverse-coefficient or logarithmic determinant. All rational numbers and strict comparisons are exact. The source class and the normalized \(H_{3,1}\) convention agree with those stated in the two cited papers.

## Proof
**Schwarz property.** Put
\[
B_2(z)=\frac{z-3/10}{1-(3/10)z},\qquad
B_1(z)=\frac{1/9+zB_2(z)}{1+(1/9)zB_2(z)}.
\]
Both maps \(z\mapsto B_2(z)\) and \(t\mapsto (1/9+t)/(1+t/9)\) are disk automorphisms. Hence \(zB_2(z)\) maps \(\mathbb D\) into \(\mathbb D\), as does \(B_1\). Elementary cancellation gives \(\omega(z)=zB_1(z)\), proving that \(\omega\) is Schwarz. In particular its displayed denominator has no zero on \(\mathbb D\).

**Positive real part and univalence.** For \(x=\cos\theta\), direct trigonometric simplification yields
\[
\operatorname{Re}\Phi(e^{i\theta})
=\frac29\left(3(1+x)^2-2x^3\right)>0,
\qquad -1\le x\le1.
\]
Indeed the expression is strictly positive for \(x\le0\), since its two nonnegative summands cannot vanish together; for \(0\le x\le1\), the bracket is at least \(3-2=1\). By the harmonic minimum principle, \(\operatorname{Re}\Phi(w)>0\) on \(\mathbb D\). Consequently \(\operatorname{Re}P(z)>0\), and averaging the values at \(z\) and \(-z\) gives \(\operatorname{Re}P_e(z)>0\).

Since \(P_e-1=O(z^2)\) and \(P_o=O(z)\), the defining integrals are holomorphic. The parity construction gives \(u(-z)=-u(z)\), \(v(-z)=v(z)\), and
\[
\frac{zu'(z)}{u(z)}=P_e(z),\qquad
\frac{zv'(z)}{u(z)}=P_o(z),\qquad
\frac{zf'(z)}{u(z)}=P(z).
\]
The first identity and \(\operatorname{Re}P_e>0\) make \(u\) starlike. The last identity and \(\operatorname{Re}P>0\) make \(f\) close-to-convex with respect to the starlike function \(u\); the classical close-to-convex univalence criterion thus makes \(f\) univalent. Moreover \(f(z)-f(-z)=2u(z)\), giving the class identity
\[
\frac{2zf'(z)}{f(z)-f(-z)}=P(z)=\Phi(\omega(z)).
\]
The identities at \(z=0\) are interpreted by analytic continuation; clearly \(f(0)=0\) and \(f'(0)=1\).

**Exact determinant.** Rational power-series division and substitution give
\[
\begin{aligned}
\omega(z)&=\tfrac19 z-\tfrac8{27}z^2+\tfrac89z^3+\tfrac{80}{243}z^4+O(z^5),\\
P(z)&=1+\tfrac19z-\tfrac{71}{243}z^2+\tfrac{5687}{6561}z^3+\tfrac{2792}{6561}z^4+O(z^5).
\end{aligned}
\]
Writing \(P(z)=1+\sum_{j\ge1}p_jz^j\) and \(f(z)=z+\sum_{j\ge2}b_jz^j\), the class identity and the parity of \(f(z)-f(-z)\) yield
\[
p_1=2b_2,\quad p_2=2b_3,\quad
p_3=4b_4-2b_2b_3,\quad p_4=4b_5-2b_3^2.
\]
Thus
\[
(b_2,b_3,b_4,b_5)=\left(\frac1{18},-\frac{71}{486},\frac{11161}{52488},\frac{55297}{472392}\right).
\]
Expanding the displayed determinant as
\[
2b_2b_3b_4-b_3^3-b_4^2+b_3b_5-b_2^2b_5
\]
and substituting gives precisely \(-173595619/2754990144\). Subtracting the two published/proposed constants gives the positive fractions in the finding. No numerical approximation enters the argument.

## Verification
Run `python3 verify_witness.py` from the directory containing this document. The self-contained standard-library program uses Python rational arithmetic to reconstruct the rational Schwarz coefficients, finite-Blaschke identity through order four, H-domain series, determining coefficient identities, third Hankel determinant, and both strictly positive gaps. The analytic facts used to establish global disk mapping and univalence are proved above, not inferred from finite calculations. The verifier prints `PASS` upon successful completion.

## Relationship to prior work
Lupaş--Tayyah--Sokół (2025), Section 5, introduced the exact problem for this class and conjectured \(|H_{3,1}|\le1/16\), after proving a weaker valid upper bound \((239+41\sqrt{41})/4800\). Tayyah--Hadi--Lupaş (2026), Theorem 1, claimed the stronger universal estimate \(|H_{3,1}|\le769/12288\). The explicit admissible witness contradicts both latter universal statements, but does not address the original weaker estimate. The papers' coefficient conventions and class definitions were checked directly against the construction; this is not a mere parameter renaming or special case of the published inequalities.

## Limitations
Only a strict, constructive lower bound for the unknown optimal supremum is established. The exact supremum and full family of extremizers are not determined, and no assertion is made about the precise origin of the discrepancy in the prior bound's proof. The construction uses a specific degree-three Blaschke function; it does not classify all possible Schwarz parameters. The local series through order five is sufficient for this determinant but supplies no higher-order coefficient claims. The literature check may miss an independently discovered counterexample; no independent audit has been performed.

## References
1. A. A. Lupaş, A. S. Tayyah, J. Sokół, *Sharp Bounds on Hankel Determinants for Starlike Functions Defined by Symmetry with Respect to Symmetric Domains*, Symmetry **17** (2025), article 1244. DOI: 10.3390/sym17081244. Published 5 August 2025.
2. A. S. Tayyah, S. H. Hadi, A. A. Lupaş, *Sharp Bound of the Third-Order Hankel Determinant for a Symmetric Domain*, Symmetry **18** (2026), article 1307. DOI: 10.3390/sym18081307. Published 3 August 2026.
3. W. Kaplan, *Close-to-convex schlicht functions*, Michigan Math. J. **1** (1952), 169–185. Used for the standard close-to-convex univalence implication.
