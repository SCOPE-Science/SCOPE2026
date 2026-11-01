# Arithmetic spectral phase transitions for singular-tip Toeplitz operators on generalized Hartogs triangles

## Finding

Fix \(\gamma>0\) and the power-generalized Hartogs triangle
\[
\mathbb H_\gamma=\{(z,w)\in\mathbb C^2:|z|^\gamma<|w|<1\}.
\]
Let \(P_\gamma\) denote the orthogonal Bergman projection on the unweighted analytic Hilbert space \(A^2(\mathbb H_\gamma)\). For \(\beta>0\) and \(0<R<1\), consider the bounded, positive, self-adjoint Toeplitz compressions
\[
T_{\gamma,\beta}=P_\gamma M_{|w|^\beta}|_{A^2},\qquad
C_{\gamma,R}=P_\gamma M_{\mathbf1_{\{|w|<R\}}}|_{A^2}.
\]
Here \(\sigma\), \(\sigma_{\rm ess}\), and \(\sigma_{\rm p}\) denote ordinary spectrum, Fredholm essential spectrum, and point spectrum, respectively. Define \(\mathcal Q_\gamma=\{n+1+(m+1)/\gamma:m\in\mathbb Z_{\ge0},\ n\in\mathbb Z,\ n+1+(m+1)/\gamma>0\}\).

**Exact simultaneous spectral classification.** If \(\gamma=P/Q\in\mathbb Q_{>0}\), with coprime positive integers \(P,Q\), then
\[
\begin{aligned}
\sigma(T_{\gamma,\beta})=\sigma_{\rm ess}(T_{\gamma,\beta})
 &=\left\{\frac{k}{k+P\beta/2}:k=1,2,\ldots\right\}\cup\{1\},\\
\sigma(C_{\gamma,R})=\sigma_{\rm ess}(C_{\gamma,R})
 &=\{R^{2k/P}:k=1,2,\ldots\}\cup\{0\}.
\end{aligned}
\]
Every displayed \(k\)-indexed spectral value is an eigenvalue of **infinite multiplicity**. The endpoints \(1\) for \(T_{\gamma,\beta}\) and \(0\) for \(C_{\gamma,R}\) are accumulation points and not eigenvalues. Consequently,
\[
\|T_{\gamma,\beta}^{-1}\|=1+P\beta/2,
\qquad \|C_{\gamma,R}\|=R^{2/P},
\]
with the second norm attained by infinitely many mutually orthogonal unit vectors.

If \(\gamma\notin\mathbb Q\), then
\[
\sigma(T_{\gamma,\beta})=\sigma_{\rm ess}(T_{\gamma,\beta})=
\sigma(C_{\gamma,R})=\sigma_{\rm ess}(C_{\gamma,R})=[0,1],
\]
where the two point spectra are, respectively,
\[
\sigma_{\rm p}(T_{\gamma,\beta})=
\left\{\frac{t}{t+\beta/2}:t\in\mathcal Q_\gamma\right\},
\quad
\sigma_{\rm p}(C_{\gamma,R})=
\{R^{2t}:t\in\mathcal Q_\gamma\}.
\]
Both point spectra are countable dense subsets of \((0,1)\), and **every eigenvalue is simple**. In particular, \(T_{\gamma,\beta}\) is injective with dense but nonclosed range (and is not boundedly invertible), while \(\|C_{\gamma,R}\|=1\) is **not attained** by any unit vector.

The complete spectral-set discontinuity is quantitative. For \(d_H\), the Hausdorff distance on compact subsets of \(\mathbb R\),
\[
\begin{aligned}
d_H(\sigma(T_{\gamma,\beta}),[0,1])&=
\begin{cases}(1+P\beta/2)^{-1}&\gamma=P/Q\text{ reduced},\\0&\gamma\text{ irrational},\end{cases}\\
d_H(\sigma(C_{\gamma,R}),[0,1])&=
\begin{cases}1-R^{2/P}&\gamma=P/Q\text{ reduced},\\0&\gamma\text{ irrational}.\end{cases}
\end{aligned}
\]
For either fixed symbol parameter, \(\gamma\mapsto\sigma(T_{\gamma,\beta})\) and \(\gamma\mapsto\sigma(C_{\gamma,R})\) are Hausdorff-continuous at **every irrational** \(\gamma>0\) and discontinuous at **every rational** \(\gamma>0\).

## Assumptions and scope

The area element on \(\mathbb C^2\) is ordinary four-dimensional Lebesgue measure. All spectral statements concern the positive Hilbert-space Toeplitz **compressions to** \(A^2(\mathbb H_\gamma)\), not their actions from \(L^p\) to \(A^p\) for \(p\ne2\). Parameters are arbitrary but fixed with \(\gamma,\beta>0\) and \(0<R<1\). The limiting and continuity statements concern spectral sets, not norm continuity between operators on spaces with different domains. The projection onto \(\{|w|<R\}\) is a near-singular-tip observation region, not a boundary collar at \(|w|=1\).

## Proof

**1. Complete monomial diagonalization.** For every \(m\ge0\) and integer \(n\), polar integration first in \(z\) and then in \(w\) gives, with \(t=n+1+(m+1)/\gamma\),
\[
\begin{aligned}
\|z^mw^n\|_{A^2}^2
 &=\frac{2\pi^2}{m+1}\int_0^1 r^{2t-1}\,dr
 =\frac{\pi^2}{(m+1)t},&&t>0.
\end{aligned}
\]
The norm is infinite when \(t\le0\). The standard Laurent expansion on the Reinhardt domain shows that the integrable monomials \(z^mw^n\) with \(t>0\) are a complete orthogonal basis. Every symbol that depends only on \(|w|\) is diagonal in this basis. Its diagonal entry is the mean under the radial probability density \(2t r^{2t-1}\,dr\), so
\[
\lambda_{\beta}(t)=2t\int_0^1 r^{2t+\beta-1}\,dr
 =\frac{t}{t+\beta/2},
\qquad
\lambda_R(t)=2t\int_0^Rr^{2t-1}\,dr=R^{2t}.
\]
Thus the two spectra are the closures of these values over \(t\in\mathcal Q_\gamma\). No finite experiment is needed for this identity.

**2. Rational exponents and infinite degeneracy.** For \(\gamma=P/Q\) in lowest terms,
\[
t=\frac{P(n+1)+Q(m+1)}P.
\]
Each positive integer \(k\) occurs as the numerator: choose \(m\ge0\) in the residue class satisfying \(Q(m+1)\equiv k\pmod P\), then solve uniquely for integer \(n\). Replacing \((m,n)\) by \((m+P,n-Q)\) preserves \(t=k/P\) and creates infinitely many distinct basis vectors. Hence \(\mathcal Q_\gamma=\{k/P:k\ge1\}\) with infinite multiplicities. Monotonicity of \(\lambda_\beta\) and \(\lambda_R\) yields both exact spectra and the norm and inverse formulas. Each eigenvalue of infinite multiplicity belongs to the Fredholm essential spectrum; the endpoint limits belong to it as well.

**3. Irrational exponents and simplicity.** When \(1/\gamma\) is irrational, the fractional parts of \((m+1)/\gamma\), \(m\ge0\), are dense in \([0,1]\). For any \(x\in(0,1)\), infinitely many \(m\) have fractional part arbitrarily close to \(x\), and choosing \(n+1=-\lfloor(m+1)/\gamma\rfloor\) gives corresponding \(t\in(0,1)\). Integer shifts of \(n\) show that \(\mathcal Q_\gamma\) is dense in \((0,\infty)\). If two monomial indices gave the same \(t\), their difference would force \((m-m')/\gamma\) to be an integer, hence \(m=m'\) and \(n=n'\). Both scalar eigenvalue functions are strictly monotone, so all irrational eigenvalues are simple and dense in \((0,1)\). Every point of \([0,1]\) is a limit of eigenvalues at distinct mutually orthogonal basis vectors and therefore lies in the Fredholm essential spectrum. Their closures are all of \([0,1]\). The positive sequence \(\lambda_\beta(t)\) approaches zero along \(t\downarrow0\), so the power operator is injective with nonclosed dense range. The collar eigenvalues approach \(1\) as \(t\downarrow0\) but are individually less than \(1\), and strict positivity of the coefficients in a unit-vector expansion prevents attainment of its norm.

**4. Exact Hausdorff gaps.** Write \(b=P\beta/2>0\). The rational power spectrum is \(\{k/(k+b)\}_{k\ge1}\cup\{1\}\). The largest distance from \([0,1]\) arises at \(0\), at distance \(1/(1+b)\), because each intervening interval has length
\[
\frac{k+1}{k+1+b}-\frac{k}{k+b}
=\frac{b}{(k+b)(k+1+b)}\le\frac1{1+b}.
\]
For the rational collar put \(s=R^{2/P}\in(0,1)\). Its spectrum is \(\{s^k:k\ge1\}\cup\{0\}\). The missing top interval \((s,1]\) has maximal distance \(1-s\), whereas each interior gap has length \(s^k(1-s)\le1-s\) and thus maximal nearest-spectrum distance at most \((1-s)/2\). This proves both exact Hausdorff formulas.

**5. Arithmetic continuity.** If reduced positive rational exponents \(P_j/Q_j\) converge to a positive irrational number, then \(P_j\to\infty\), because bounded numerators and denominators tending to infinity would force the rational values toward zero. Hence both rational Hausdorff gaps tend to zero; the irrational gaps equal zero. Both spectral-set maps are therefore continuous at every irrational exponent. At each rational exponent, irrational approximants have full spectrum \([0,1]\), whose positive Hausdorff distance from the rational spectrum is given above. Thus both maps are discontinuous at every rational exponent.

## Verification

A standalone Python 3 checker, `checker.py`, independently integrates representative monomial radial moments, verifies rational admissibility congruences and power/collar eigenvalue ordering, checks finite gap inequalities, and samples irrational rotations. It prints `PASS: 1334 finite assertions` with its bundled parameters. These calculations are supplementary diagnostics; the infinite-dimensional, arithmetic and continuity assertions follow from the exact arguments above and not from the finite samples.

## Relationship to prior work

The domain, monomial lattice and arithmetic dichotomy in Bergman \(L^p\) projection regularity are established in Edholm–McNeal, *Bergman subspaces and subkernels: degenerate \(L^p\) mapping and zeroes* (2016 preprint). In particular, monomial integrability and the distinction between rational and irrational \(\gamma\) are **prior results**; they are not new here. Balay–Neutgens–Rosen–Wagner–Zeytuncu (2020 preprint) study Toeplitz operators with the **same power symbol** \(|w|^\beta\) but establish \(L^p\) regularity bounds rather than these explicit Hilbert-space spectra, Fredholm essential spectra, sharp inverse and concentration norms, or the everywhere discontinuous/irrational-continuous Hausdorff law. The present calculation derives those operator invariants from the prior monomial framework. Lusky's 2001 work treats essential spectra for radial operators on generalized one-dimensional Bergman–Hardy spaces, a different function-space setting; it provides general radial Toeplitz background, not the two-index arithmetic classification.

## Limitations

This is a theorem only for the stated radial power and singular-tip indicator symbols on unweighted Hilbert Bergman spaces. It makes no assertion about arbitrary nonradial symbols, weighted or vector-valued spaces, or \(L^p\) mapping for \(p\ne2\). In the irrational case, an interval spectrum does not mean that the spectral measure is absolutely continuous: the operator has a complete orthogonal basis of eigenvectors with dense pure-point spectral values. Historical priority is provisional; an earlier general radial-Toeplitz diagonalization theorem might subsume individual steps, even though no directly covering arithmetic spectral classification was identified. The related 2023 special-Toeplitz article has an author-posted full-text version, whose main theorems concern \(L^p\)-to-\(L^q\) mapping for integral-exponent domains rather than the spectral formulas here.

## References

1. M. Balay, T. Neutgens, N. Rosen, N. A. Wagner and Y. E. Zeytuncu, *\(L^p\) Regularity of Toeplitz Operators on Generalized Hartogs Triangles*, first public preprint 2020-09-15, arXiv:2009.07260, https://arxiv.org/abs/2009.07260 .
2. L. D. Edholm and J. D. McNeal, *Bergman Subspaces and Subkernels: Degenerate \(L^p\) Mapping and Zeroes*, first public preprint 2016-05-20, arXiv:1605.06223, https://arxiv.org/abs/1605.06223 .
3. W. Lusky, *Toeplitz operators on generalized Bergman–Hardy spaces*, Mathematica Scandinavica 88 (2001), 96–110, DOI:10.7146/math.scand.a-14316 .
4. H. Liu, Y. Tang, Z. Tu and S. Zhang, *Special Toeplitz Operators on n-Dimensional Generalized Hartogs Triangles*, DOI:10.1007/s11785-023-01331-1 (author-posted full text and main results inspected).
