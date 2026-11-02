# The first two integer Fourier levels of the uniform Vicsek cross measure

## Finding

Let \(\mathcal D=\{(1,1),(0,1),(2,1),(1,0),(1,2)\}\), and let \(\mu\) be the probability law on \([0,1]^2\) of
\[
(X,Y)=\sum_{j=1}^{\infty}3^{-j}U_j,
\]
where the \(U_j\) are independent and uniformly distributed on \(\mathcal D\). Thus \(\mu\) is the canonical uniform measure on the **cross-form**, five-map planar Vicsek set. Define \(\widehat\mu(m,n)=\int e^{-2\pi i(mx+ny)}\,d\mu(x,y)\) for \((m,n)\in\mathbb Z^2\).

Put
\[
 A=\frac25\prod_{j=2}^{\infty}\frac{3+2\cos(2\pi/3^j)}5,
 \qquad
 B=\frac25\prod_{j=2}^{\infty}\frac{3+2\cos(4\pi/3^j)}5.
\]
Then \(A\approx0.3581726074759164252\), \(B\approx0.2550051230961402499\), and
\[
 A>B>\frac6{25}.
\]
The two largest **distinct** moduli among all nonzero integer Fourier coefficients are precisely \(A\) and \(B\), with all equality cases
\[
 |\widehat\mu(m,n)|=A
 \quad\Longleftrightarrow\quad
 (m,n)=3^r(\pm1,0)\ \text{or}\ 3^r(0,\pm1),\quad r\in\mathbb Z_{\ge0},
\]
\[
 |\widehat\mu(m,n)|=B
 \quad\Longleftrightarrow\quad
 (m,n)=3^r(\pm2,0)\ \text{or}\ 3^r(0,\pm2),\quad r\in\mathbb Z_{\ge0}.
\]
For **every** remaining nonzero \((m,n)\in\mathbb Z^2\),
\[
 \boxed{\ |\widehat\mu(m,n)|<\frac6{25}<B\ }.
\]
Consequently convolution by \(\mu\) on mean-zero \(L^2(\mathbb T^2)\) has exact operator norm \(A\); after excluding the first extremizing Fourier family it has exact norm \(B\). The latter follows by diagonalization in the standard character basis. No claim is made that \(6/25\) is the optimal third-level upper bound.

## Assumptions and scope

The measure has **equal independent digit weights** and exactly the centered cross digit set above. The Fourier convention has the negative exponential sign, irrelevant to the moduli. The set is the *cross*, not the corner-plus-center variant; the latter has a different integer-coordinate Fourier spectrum even though its geometric support is similarly called a Vicsek set. Frequencies are nonzero pairs of ordinary integers; all powers of \(3\) are included. The result is not a statement about arbitrary real frequencies, other digit weights, other contractions, scattering after angular averaging, or all variants of Vicsek fractals.

For convenience write
\[
 M_j(m,n)=\frac{1+2\cos(2\pi m/3^j)+2\cos(2\pi n/3^j)}5,
 \qquad j\ge1.
\]
The Fourier transform of a single digit has an additional phase \(e^{-2\pi i(m+n)/3^j}\). Independence and weak convergence therefore give
\[
 |\widehat\mu(m,n)|=\prod_{j=1}^{\infty}|M_j(m,n)|. \tag{1}
\]
Every factor has modulus at most one because it is the modulus of an average of five unit-modulus exponentials. For each fixed integer pair, the product converges: beyond a finite initial range, its factors are \(1+O((m^2+n^2)3^{-2j})\).

## Proof

**Step 1: remove powers of three.** If both frequency coordinates are divisible by \(3\), then \(M_1(m,n)=1\) and \(M_j(m,n)=M_{j-1}(m/3,n/3)\) for \(j\ge2\). The omitted phase has modulus one, hence
\[
 |\widehat\mu(3m,3n)|=|\widehat\mu(m,n)|. \tag{2}
\]
For a nonzero pair, repeatedly divide both coordinates by \(3\) until at least one coordinate is nonzero modulo \(3\). Call the resulting pair *primitive*.

**Step 2: the first ternary digit.** On primitive pairs, \(\cos(2\pi h/3)\) equals \(1\) for \(h\equiv0\pmod3\) and \(-1/2\) otherwise. Thus
\[
 |M_1(m,n)|=
 \begin{cases}
 1/5,&m,n\not\equiv0\pmod3,\\
 2/5,&\text{exactly one of }m,n\text{ is nonzero modulo }3.
 \end{cases} \tag{3}
\]
Any pair of the first kind already has Fourier modulus at most \(1/5<6/25\).

**Step 3: the second ternary digit.** By coordinate exchange, suppose \(m\not\equiv0\pmod3\) and \(n\equiv0\pmod3\). If \(n\equiv\pm3\pmod9\), then \(\cos(2\pi n/9)=-1/2\), so
\[
 |M_2(m,n)|=\frac25\left|\cos(2\pi m/9)\right|\le\frac25.
\]
The full coefficient is at most \(4/25<6/25\). If \(n\equiv0\pmod9\), then
\[
 M_2(m,n)=\frac{3+2\cos(2\pi m/9)}5>0.
\]
For \(m\equiv\pm4\pmod9\), the cosine is negative and \(M_2<3/5\), so the Fourier modulus is below \(6/25\). The only surviving residue pairs, up to signs and coordinate exchange, are consequently
\[
 (m,n)\equiv(1,0)\pmod9\quad\text{and}\quad(m,n)\equiv(2,0)\pmod9. \tag{4}
\]
These statements use the ordinary signed representatives of the residue classes, so a negative representative is tracked consistently at subsequent levels.

**Step 4: first-divergence rigidity from level three onward.** Fix \(a\in\{1,2\}\) and an integer \(j\ge3\). Suppose modulo \(3^{j-1}\) that
\[
 (m,n)\equiv(\varepsilon a,0),\qquad \varepsilon\in\{-1,1\}.
\]
There are three lifts of each coordinate to modulo \(3^j\). If the lift is not exactly \((\varepsilon a,0)\), the factor \(|M_j|\) is strictly below \(3/5\):

* If the second coordinate is lifted away from zero, its cosine at level \(j\) is \(-1/2\). Hence \(|M_j|=(2/5)|\cos(2\pi m/3^j)|\le2/5\), whatever the first-coordinate lift.
* Otherwise the first coordinate is lifted to \(\varepsilon a\pm3^{j-1}\). Since \(3^j\ge27>6a\), the angles \(2\pi/3\pm2\pi a/3^j\) lie strictly between \(\pi/2\) and \(\pi\), so both cosines are negative. As the second-coordinate cosine is \(1\), we obtain \(0<M_j<3/5\).

The prefix through level \(j-1\) is at most \(2/5\), by (3) and the unit-modulus bound on later factors. A first divergence at level \(j\ge3\) therefore forces
\[
 |\widehat\mu(m,n)|<\frac25\cdot\frac35=\frac6{25}. \tag{5}
\]
In order to exceed \(6/25\), a primitive frequency must belong to one of the residue pairs in (4) and **never** diverge from that same signed pair at any higher ternary level. The only ordinary integers satisfying the resulting congruences for all levels are exactly \((\pm1,0)\), \((\pm2,0)\), and their coordinate exchanges. Equation (2) restores precisely their stated \(3\)-power multiples.

**Step 5: the two surviving products really exceed the cutoff, and are distinct.** For each \(j\ge2\), both \(\cos(2\pi/3^j)\) and \(\cos(4\pi/3^j)\) are positive; moreover the former is strictly larger. Consequently \(A>B>0\).

For the quantitative lower bound, \(\cos(4\pi/9)=\sin(\pi/18)>1/9\) follows from the strict chord bound \(\sin u>2u/\pi\) on \((0,\pi/2)\). Also, \(\cos u\ge1-u^2/2\) gives, for \(j\ge3\),
\[
 \frac{3+2\cos(4\pi/3^j)}5
 \ge1-\frac{16\pi^2}{5\,9^j}.
\]
Using \(\prod(1-b_j)\ge1-\sum b_j\) for nonnegative \(b_j\le1\), and \(\pi^2<10\), we obtain the **strict** rational certificate
\[
 B>\frac{58}{225}\left(1-\frac{2\pi^2}{405}\right)
 >\frac{58}{225}\cdot\frac{77}{81}
 =\frac{4466}{18225}>\frac6{25}. \tag{6}
\]
Thus the two frequencies in (4) do survive, all others fall strictly below the cutoff, and the two values are unequal in the asserted order. This completes the infinite-frequency classification.

**Step 6: convolution interpretation.** Regard the measure modulo \(\mathbb Z^2\). Fourier characters form an orthonormal basis of \(L^2(\mathbb T^2)\), and convolution by \(\mu\) multiplies the character at \((m,n)\) by \(\widehat\mu(m,n)\). The zero Fourier mode is the constant eigenfunction. Removing it gives norm \(A\); additionally removing the four axis frequency families realizing \(A\) leaves norm \(B\). The remaining frequencies have norm bounded **strictly** below \(6/25\) individually; the operator norm on their closed span is at most \(6/25\), without asserting a strict operator-norm bound.

## Verification

The proof's decisive inequalities are (3)–(6); they are elementary and uniform in the frequency, with no numerical extrapolation. The standalone `checker.py` is supplied as *supplementary* reproducibility material. It reconstructs the digit masks, verifies the second-digit residue split and later off-path lift inequalities, checks the exact rational bound in (6), evaluates both products, and compares a finite box of integer frequencies against the classification. It checks **58,349 assertions** when run with Python 3 using only the standard library.

Command: `python checker.py` (from the extracted package directory). Expected final line begins `VICSEK_CROSS_FOURIER_CHECK_OK 58349`. The numerical frequency box is not an exhaustive proof of the theorem; the all-frequency proof is Step 4.

## Relationship to prior work

Vicsek's original fractal construction supplies the underlying canonical self-similar geometry. General affine-IFS Fourier theory, notably Dutkay–Jorgensen, establishes transform recursions and investigates orthogonal exponential bases, but does not give this exact integer-lattice ordered-modulus classification. The scattering studies of Cherny and collaborators and of Anitas and collaborators analyze reciprocal-space fractal intensities and form factors, but concern different models or observables and do not imply this two-level rigidity theorem. The Jayanthi–Wu work on the *frequency spectrum* of Vicsek fractals concerns mechanical vibrations, not the Fourier transform of the invariant probability measure.

The five-map cross mask here, \((1+2\cos u+2\cos v)/5\), differs from the masks of the middle-thirds Cantor measure and the eight-map Sierpiński carpet measure. Sharp integer Fourier coefficients for those other measures do not imply the present claims. A general prior theorem specialized to this mask would cover the result; the bounded literature comparison identified none, but older fractal-diffraction work remains a residual originality risk.

## Limitations

The theorem concerns integer frequencies for this one canonical equal-weight measure and its cross-form digit geometry; it does not classify every real-frequency maximum, the optimal third Fourier level, general Vicsek variants, arbitrary weights, or Fourier decay as frequency grows. The bound \(6/25\) is a strict separator, not claimed to be the best bound outside the two extremizing families. Verification and literature review reported here are not independent mathematical certification.

## References

1. T. Vicsek, *Fractal models for diffusion controlled aggregation*, Journal of Physics A 16 (1983), L647, doi:10.1088/0305-4470/16/17/003. A bibliographic index gives 1983-12-01; exact original public-release precision has not been independently established.
2. C. S. Jayanthi and S. Y. Wu, *Frequency spectrum of a general Vicsek fractal*, Physical Review B 48 (1993), 10188–10198, doi:10.1103/PhysRevB.48.10188.
3. D. E. Dutkay and P. E. T. Jorgensen, *Fourier frequencies in affine iterated function systems*, arXiv:math/0604547 (2006), https://arxiv.org/abs/math/0604547.
4. A. Yu. Cherny, E. M. Anitas, V. A. Osipov and A. I. Kuklin, *Deterministic fractals: extracting additional information from small-angle scattering data*, arXiv:1106.2089 (first submitted 2011-06-10), https://arxiv.org/abs/1106.2089.
5. E. M. Anitas et al., *Structural Properties of Vicsek-like Deterministic Multifractals*, Symmetry 11 (2019), 806, doi:10.3390/sym11060806; https://www.mdpi.com/2073-8994/11/6/806.
