# Sharp sixth moment and complete extremizers for the Fano Singer spectrum

## Finding
Let \(\omega=\exp(2\pi i/7)\). For every \((a,b,c)\in\mathbb C^3\) put
\[
F_{a,b,c}(j)=a+b\omega^j+c\omega^{3j},\qquad j\in\mathbb Z/7\mathbb Z.
\]
With normalized counting measure on the cyclic group, the following inequality is sharp:
\[
\frac17\sum_{j=0}^{6}|F_{a,b,c}(j)|^6
\le\frac{37}{9}(|a|^2+|b|^2+|c|^2)^3.
\]
For nonzero coefficients equality holds **if and only if**
\[
(a,b,c)=\lambda(1,\omega^h,\omega^{3h})
\quad\text{for some }\lambda\in\mathbb C\setminus\{0\},\ h\in\mathbb Z/7\mathbb Z.
\]
Thus the exact operator norm from coefficient \(\ell^2\) to normalized \(L^6\) is \((37/9)^{1/6}\), with exactly seven projective complex extremizers.

## Assumptions and scope
The frequency set is the Singer \((7,3,1)\) difference set \(\{0,1,3\}\subset\mathbb Z/7\mathbb Z\). Its differences are all six nonzero residues exactly once; its translates give the seven lines of the Fano plane. The input coefficients are arbitrary complex numbers with no prescribed magnitudes, and zero coefficients are allowed. The output is sampled only at the seven characters of the cyclic group. Norms are taken with normalized counting measure; in particular
\[
\|F_{a,b,c}\|_2^2=|a|^2+|b|^2+|c|^2.
\]
No continuous-circle or larger-Singer-set claim is made.

## Proof
Write \(R=|a|^2+|b|^2+|c|^2\). Orthogonality of seventh roots of unity says that the sixth moment is the sum of the squared moduli of the seven cubic-convolution coefficients. In order of residue \(0,1,\ldots,6\), those coefficients are
\[
a^3+3bc^2,\quad3a^2b,\quad3ab^2+c^3,\quad b^3+3a^2c,\quad6abc,\quad3b^2c,\quad3ac^2.
\]
In particular, with
\[
U=|a|^2|b|^2+|a|^2|c|^2+|b|^2|c|^2,
\quad V=|abc|^2,
\]
we obtain the exact identity
\[
\|F_{a,b,c}\|_6^6
=R^3+6RU+12V+6\operatorname{Re}\!\bigl(
 a^3\overline b\,\overline c^{\,2}
 +ab^2\overline c^{\,3}
 +b^3\overline a^{\,2}\overline c\bigr).
\tag{1}
\]
Set \(x=|a|\), \(y=|b|\), \(z=|c|\), so \(R=x^2+y^2+z^2\). The absolute value bound on the last line of (1) is \(6W\), where
\[
W=x^3yz^2+x^2y^3z+xy^2z^3
=xyz\bigl(x^2z+xy^2+yz^2\bigr).
\]
A useful cyclic identity is
\[
(x+y+z)(x^2+y^2+z^2)-3(x^2z+xy^2+yz^2)
=x(x-z)^2+y(y-x)^2+z(z-y)^2\ge0.
\tag{2}
\]
By (2) and Cauchy--Schwarz,
\[
x^2z+xy^2+yz^2\le\frac{(x+y+z)R}{3}
\le\frac{R^{3/2}}{\sqrt3}.
\]
Arithmetic--geometric mean also gives \(xyz\le(R/3)^{3/2}\), whence \(W\le R^3/9\). Finally,
\[
U\le R^2/3,\qquad V\le R^3/27.
\]
Substitution into (1) proves
\[
\|F_{a,b,c}\|_6^6
\le R^3\left(1+\frac{6}{3}+\frac{12}{27}+\frac{6}{9}\right)
=\frac{37}{9}R^3.
\]
If \(R>0\), equality in the bound for \(U\) requires \(x=y=z>0\). With these magnitudes, equality in the three complex real-part estimates in (1) requires
\[
3\alpha-\beta-2\gamma\equiv0,\quad
\alpha+2\beta-3\gamma\equiv0,\quad
3\beta-2\alpha-\gamma\equiv0\pmod{2\pi},
\]
where \(a=x e^{i\alpha}\), \(b=x e^{i\beta}\), \(c=x e^{i\gamma}\). On setting \(u=\beta-\alpha\), \(v=\gamma-\alpha\), the relations give \(v\equiv3u\) and \(7u\equiv0\pmod{2\pi}\). Therefore \(u=2\pi h/7\) and \(v=6\pi h/7\) for a unique \(h\in\mathbb Z/7\mathbb Z\). Conversely, all these phase choices align every collision fiber, attain equality in (1), and have equal magnitudes. The seven rays are distinct because their coefficient ratios \(b/a\) differ.

## Verification
The standalone standard-library program `artifacts/verify.py` constructs the exact cubic group-algebra convolution over \(\mathbb Z/7\mathbb Z\), verifies (1) coefficient-by-coefficient as a polynomial in six independent formal variables representing the coefficients and their conjugates, checks the residue multiplicities \((4,3,4,4,6,3,3)\), and confirms energy \(111\) for the unit coefficient triple. It also samples \(250\) independent complex triples to compare direct seven-point sixth moments with cubic convolution and checks all seven exhibited extremizers. Run `python3 artifacts/verify.py`; the expected success line begins `VERIFY_OK`. The global inequality and its equality classification rest on the displayed algebraic proof, not on the finite tests.

## Relationship to prior work
The Singer/Fano difference-set structure and the even-exponent Fourier-convolution method are classical. Mockenhaupt--Tao, *Restriction and Kakeya phenomena for finite fields*, §5, Lemma 5.1, bound even moments by maximum sum-fiber multiplicities. Applied here with the largest cubic fiber of size \(6\), that method gives the weaker sixth-power coefficient bound \(6\), rather than the sharp \(37/9\), and does not classify optimizers. Stinson's Singer difference-set lecture explicitly identifies \(\{0,1,3\}\) with the Fano plane.

The publicly available result *Exact seven-sample phase minimax for the Fano frequency triple* analyzes the **same** support and computes the third moment of the squared modulus for three **unimodular** coefficients. Its formula already gives the sixth-moment value \(111\) at aligned unit phases, a fact **not claimed new here**. That result optimizes a different objective (sample peak minimization) and does not prove the inequality above for **arbitrary complex coefficient magnitudes**, nor its complete \(\ell^2\)-normalized extremizer classification. Neuwirth's *The maximum modulus of a trigonometric trinomial* solves continuous-circle maximum-modulus questions and Sidon constants, not this sampled \(L^6/\ell^2\) problem. The assessed contribution is specifically the unrestricted sharp sixth-moment inequality and all its equality cases.

## Limitations
The theorem concerns the seven-point cyclic group and its canonical three-point Singer spectrum. The fixed-unimodular subcase is closely related to an existing published calculation; novelty is not asserted for that subcase, for the classical difference-set geometry, or for the convolution method. No extension to arbitrary larger Singer difference sets, other even exponents, or continuous-circle norms is proved. A hidden equivalent sharp \(L^6\) computation in older small-spectrum norm tables cannot be excluded, and external independent validation remains unperformed.

## References
1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234, first submitted 2002-04-18; §5, Lemma 5.1. https://arxiv.org/abs/math/0204234
2. S. Neuwirth, *The maximum modulus of a trigonometric trinomial*, arXiv:math/0703236v1, first submitted 2007-03-08. https://arxiv.org/abs/math/0703236
3. D. R. Stinson, *Robust and Non-malleable Threshold Schemes, AMD codes and External Difference Families*, SAC 2023 slides, slide 10, Singer difference sets. https://sac-workshop.github.io/sac-2023/slides/Stinson.pdf
4. *Exact seven-sample phase minimax for the Fano frequency triple*, publicly available result (2026-10-04), section Proof (formula for \(m_3\)). https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-seven-sample-phase-minimax-for-the-fano-frequency-triple--d1f94e9a8add/RESULT.md
