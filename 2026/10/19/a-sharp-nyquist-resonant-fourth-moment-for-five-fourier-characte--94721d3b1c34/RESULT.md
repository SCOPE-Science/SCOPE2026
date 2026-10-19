# A sharp Nyquist-resonant fourth moment for five Fourier characters on the eight-cycle

## Finding
Let \(\chi(k)=e^{2\pi i k/8}\) on \(\mathbb Z/8\mathbb Z\), and for arbitrary \(a_0,\ldots,a_4\in\mathbb C\) define
\[
F(k)=\sum_{j=0}^{4}a_j\chi(k)^j,\qquad S=\sum_{j=0}^{4}|a_j|^2.
\]
Let \(v_*\) denote the **unique positive real root** of
\[
P(v)=v^4+4v^3-7v-2=0,
\qquad v_*=1.274598610381937\ldots,
\]
and put
\[
u_*^2=\frac{2(v_*^4+3v_*^3+6v_*+2)}{3(v_*^2+4v_*+2)},\qquad u_*=1.189039944890622\ldots.
\]
Then the sharp fourth-moment inequality is
\[
\frac18\sum_{k=0}^7|F(k)|^4\ \le\ K_*S^2,
\qquad K_*=\frac{3(5v_*^4+24v_*^3+36v_*^2+48v_*+16)}{7v_*^4+24v_*^3+12v_*^2+48v_*+20}=3.527901483813720\ldots .
\]
Every nonzero equality coefficient vector, and no others, has the form
\[
(a_0,a_1,a_2,a_3,a_4)=\lambda(1,u_*e^{i\theta},v_*e^{2i\theta},u_*e^{3i\theta},e^{4i\theta}),
\quad\lambda\in\mathbb C\setminus\{0\},\quad\theta\in\left\{\frac{\pi k}{4}:k=0,\ldots,7\right\}.
\]
Thus there are precisely eight equality classes modulo nonzero complex scaling, whereas the unaliased fourth-moment problem allows a continuous modulation phase. The resonance is strict: the five equal coefficients give normalized fourth moment \(87/25\) on the eight-cycle, versus \(85/25\) on the circle.

## Assumptions and scope
The group is the eight-element cyclic group and the five frequencies are the consecutive residues \(\{0,1,2,3,4\}\); no coefficient sign, reality, phase, or nonvanishing restriction is assumed. The input uses counting \(\ell^2\) energy and the output uses normalized counting measure. The theorem does not state an optimum for other Fourier supports, group orders, or exponents. The angle \(\theta\) is interpreted modulo \(2\pi\). The upper moment is homogeneous, and \(S=0\) yields equality trivially.

## Proof
**1. The exceptional Nyquist correlation.** Extend the coefficient vector by zero to all of \(\mathbb Z/8\mathbb Z\), and let
\[
R_h=\sum_{j=0}^{4-h}a_{j+h}\overline{a_j},\quad h=1,2,3,4.
\]
Fourier orthogonality, after merging frequencies \(4\) and \(-4\) modulo eight, gives the exact identity
\[
\frac18\sum_{k=0}^7|F(k)|^4
=S^2+2\bigl(|R_1|^2+|R_2|^2+|R_3|^2\bigr)+4\bigl(\operatorname{Re}R_4\bigr)^2.\tag{1}
\]
The corresponding unaliased expression has \(2|R_4|^2\), not \(4(\operatorname{Re}R_4)^2\). This is the unique first Nyquist alias for five consecutive frequencies.

**2. Reduction to palindromic nonnegative coefficients.** First replace every coefficient by its absolute value. Term-by-term triangle inequalities in the cyclic self-convolution show that this cannot lower the left side of (1), while preserving \(S\). Now set \(x_j=|a_j|\) and make the reflection root-mean-square replacement
\[
y_j=\sqrt{\frac{x_j^2+x_{4-j}^2}{2}},\qquad j=0,\ldots,4.
\]
It preserves \(S\), has support in the same five residues, and increases every cyclic autocorrelation \(\sum_j x_jx_{j+h}\), by Cauchy--Schwarz and reflection \(j\mapsto4-j\). More explicitly, for each \(h\), Cauchy--Schwarz compares \(2y_jy_{j+h}\) with \(x_jx_{j+h}+x_{4-j}x_{4-(j+h)}\), and the latter terms sum to twice the original autocorrelation. The full fourth moment therefore does not decrease. Strictness follows whenever any reflected magnitudes differ: if they do, the sum of coefficients strictly increases, so some nonzero autocorrelation strictly increases; since the zero-shift autocorrelation equals \(S>0\), its squared contribution increases the moment. Hence every nonzero maximizer has
\[
(|a_0|,\ldots,|a_4|)=(x,y,z,y,x),\qquad x,y,z\ge0.\tag{2}
\]
The reflected-RMS reduction is an established general technique; the new calculation below determines the exceptional eight-point sharp value.

**3. Polynomial optimization.** For nonnegative coefficients in (2), compute the eight cyclic convolution sums, equivalently use (1), to obtain
\[
\frac18\sum |F|^4
=8x^4+24x^2y^2+12x^2z^2+24xy^2z+6y^4+12y^2z^2+z^4,\qquad S=2x^2+2y^2+z^2.\tag{3}
\]
There is a positive competitor \((x,y,z)=(1,1,1)\) of ratio \(87/25\). Every boundary candidate has smaller ratio: if \(x=0\), the surviving three consecutive frequencies have ratio at most \(15/7\); if \(y=0\), writing \(t=z^2/x^2\) gives ratio \((8+12t+t^2)/(2+t)^2\le7/3\); and if \(z=0\) with \(x,y>0\), the right derivative toward \(z>0\) of (3) is \(24xy^2>0\), with zero denominator derivative. All remaining corner cases are included in these bounds. Thus a maximizer has \(x,y,z>0\).

Normalize \(x=1\), put \(u=y/x>0\), \(v=z/x>0\), and define
\[
H(u,v)=\frac{6u^4+12u^2v^2+24u^2v+24u^2+v^4+12v^2+8}{(2+2u^2+v^2)^2}.\tag{4}
\]
Writing \(D=2+2u^2+v^2\), direct exact differentiation gives
\[
D^3\frac{\partial H}{\partial u}=-8u\bigl((3v^2+12v+6)u^2-2v^4-6v^3-12v-4\bigr),\tag{5}
\]
\[
D^3\frac{\partial H}{\partial v}=8\bigl(3u^4v+6u^4-2u^2v^3-9u^2v^2+6u^2-2v^3+2v\bigr).\tag{6}
\]
The positive stationary solutions of (5) satisfy
\[
u^2=\frac{2(v^4+3v^3+6v+2)}{3(v^2+4v+2)}.\tag{7}
\]
Substitute (7) into the parenthesis in (6) and factor exactly:
\[
-\frac{2(v^4+4v^3-7v-2)(7v^4+24v^3+12v^2+48v+20)}{3(v^2+4v+2)^2}.\tag{8}
\]
The second factor of the numerator is strictly positive at all \(v>0\). The first has exactly one positive root by Descartes' rule of signs (one sign change) and by \(P(0)=-2\) with \(P(v)\to+\infty\). Thus there is precisely one positive critical point. Compactness of the fixed-energy sphere, the boundary exclusion, and the existence of that unique critical point establish that it is the global maximum. Substitution of (7) into (4) reduces exactly to the stated rational expression for \(K_*\).

**4. All phases.** At any maximum the strict symmetrization argument gives (2), with all three magnitudes positive. To attain the positive-polynomial bound, the four summands in \(R_1\) must have a common argument, which forces all successive phase increments \(\arg a_{j+1}-\arg a_j\) to equal one \(\theta\) modulo \(2\pi\). Moreover, (1) is sharp relative to the magnitude bound only if \(\operatorname{Re}R_4=\pm|R_4|\); for affine phases this is \(\sin(4\theta)=0\), equivalent to \(\theta=\pi k/4\). Conversely, the eight listed coefficient vectors make every preceding bound an equality. Their projective classes are distinct, since the ratio of second to first coefficients determines \(\theta\).

## Verification
Execute `python3 checker.py` using Python 3's standard library. The checker verifies exactly, with integer-polynomial convolution, the factorization (8) after clearing denominators; isolates \(v_*\) in a rational interval by sign and bisection; checks (3) on 48 integer positive/zero boundary triples; checks the exact discrete convolution identity against an independent eight-point Fourier average on 3,000 fixed-seed Gaussian-integer vectors; verifies their claimed bound; and checks all eight extremizer phases. It prints `VERIFY_OK`. The finite random tests corroborate but do not prove the theorem; the universal statement is proved by (1)--(8) and the boundary and equality arguments.

## Relationship to prior work
The Hardy--Littlewood even-exponent majorant principle and the cyclic correlation identity are classical, as discussed by Green--Ruzsa. The general reflection root-mean-square improvement of even Fourier moments has also been established for reflection-invariant supports; it supplies the symmetry reduction in Step 2, **not** the algebraic constant or the eight equality classes.

Brown--Goldstein--McDonald (1988) study maximizing the squared \(L^2\) norm of a **continuous** nonnegative trigonometric polynomial of bounded degree with constant term one. Via Fejér--Riesz factorization that is equivalent to the continuous unaliased sharp \(L^2\)-to-\(L^4\) polynomial problem, and it is therefore a serious same-object comparator for a circle result. It does **not** directly give the eight-point Nyquist alias term in (1); the normalizing geometry here is discrete and gives the different constant \(K_*\). This article's full text was not accessible, so any internal treatment of cyclic sampling cannot be conclusively excluded.

Published exact results for four consecutive Fourier characters use order at least seven and produce a different two-modulus stationary equation; they cannot imply the five-character eight-point equation. Published five-point Ferrers-spectrum results have a two-dimensional additive-collision pattern, not a one-dimensional cyclic Nyquist collision. An older Goldstein--McDonald paper concerns extremal nonnegative trigonometric polynomials but was available only bibliographically; the same bibliographic caution applies.

## Limitations
The theorem concerns only five consecutive characters on the eight-cycle and the fourth moment; it is not an assertion for arbitrary five-point supports or all cyclic orders. The first-alias interpretation and degree-four optimization are elementary once set up, but a prior tabulation of this exact finite sampled constant under nonnegative-trigonometric, filter-energy, or Nikolskii terminology remains possible. The historical literature comparison, including inaccessible 1984 and 1988 full texts, is not an independent priority certification. The numerical checker is diagnostic; no external or independent mathematical audit has been performed.

## References
1. B. Green and I. Z. Ruzsa, *On the Hardy--Littlewood majorant problem*, first arXiv posting 2003-03-19, https://arxiv.org/abs/math/0303244.
2. K.-U. Schmidt, *On a problem due to Littlewood concerning polynomials with unimodular coefficients*, first arXiv posting 2013-02-12, https://arxiv.org/abs/1302.2766.
3. J. Brown, M. Goldstein and J. N. McDonald, *A sequence of extremal problems for trigonometric polynomials*, J. Math. Anal. Appl. **130** (1988), 545--551, https://doi.org/10.1016/0022-247X(88)90330-7.
4. M. Goldstein and J. N. McDonald, *An extremal problem for non-negative trigonometric polynomials*, J. London Math. Soc. **29** (1984), 81--88, https://doi.org/10.1112/jlms/s2-29.1.81.
5. *Reflection root-mean-square majorization of every even Fourier moment*, published research note (2026), theorem on reflection-invariant finite spectra.
6. *Exact fourth moment and all extremizers for four consecutive Fourier characters*, published research note (2026), four-character cyclic threshold theorem.
7. *Sharp fourth moments for a five-point Ferrers Fourier spectrum*, published research note (2026), five-character nonrectangular two-dimensional support.
