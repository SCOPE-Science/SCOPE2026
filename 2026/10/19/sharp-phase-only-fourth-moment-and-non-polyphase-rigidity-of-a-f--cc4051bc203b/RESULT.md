# Sharp phase-only fourth moment and non-polyphase rigidity of a five-site cross

## Finding
Let \(G\) be a compact abelian group with normalized Haar measure, and let \(\chi,\psi\) be continuous unitary characters such that the thirteen characters
\[
1,\quad \chi^{\pm1},\ \psi^{\pm1},\quad
\chi^{\pm2},\ \psi^{\pm2},\quad
\chi^{\pm1}\psi^{\pm1}
\]
are pairwise distinct. For arbitrary unit-modulus coefficients \(c,a_+,a_-,b_+,b_-\), set
\[
P=c+a_+\chi+a_-\chi^{-1}+b_+\psi+b_-\psi^{-1},
\qquad \mathcal E(P)=\int_G |P|^4\,d\mu.
\]
Then the **exact attainable fourth-moment interval** is
\[
\boxed{36\le\mathcal E(P)\le61,\qquad
\{\mathcal E(P):|c|=|a_+|=|a_-|=|b_+|=|b_-|=1\}=[36,61].}
\]
Write \(U=a_+a_-\overline c^{\,2}\) and \(V=b_+b_-\overline c^{\,2}\). The lower endpoint is attained **if and only if**
\[
\boxed{(U,V)=(\zeta,\overline\zeta),\quad
\zeta\in\left\{\frac{-1+i\sqrt{15}}4,\frac{-1-i\sqrt{15}}4\right\}.}
\]
The upper endpoint is attained **if and only if** \(U=V=1\). In coefficient phase space, the minimizers form precisely two disjoint three-dimensional tori, and the maximizers form one three-dimensional torus.

No finite root-of-unity coefficient alphabet attains \(36\). For coefficients restricted to the \(q\)-th roots of unity, the sharp fourth moment equals \(37\) for \(q\in\{2,3,4,6\}\), whereas the trivial one-phase case \(q=1\) has moment \(61\). Thus continuous phases give the sharp aperiodic autocorrelation merit factor \(25/11\), while the sharp binary, ternary, quaternary and six-phase merit factor is \(25/12\).

In particular, this entire statement holds for the cross \(\{(0,0),(\pm1,0),(0,\pm1)\}\) on the continuous two-torus and for the **unnormalized** Fourier synthesis average on every \(\mathbb Z_m\times\mathbb Z_n\) with \(m,n\ge5\). It also applies to the one-variable lacunary support \(\{0,\pm1,\pm k\}\subset\mathbb Z\) for every integer \(k\ge4\).

## Assumptions and scope
The moment uses normalized Haar probability measure. Fourier coefficients each have magnitude exactly one; no amplitude optimization is asserted. The stated thirteen-character hypothesis is equivalent to having no unexpected coincidences among the cross-support differences. For the discrete product group, the characters are the two standard coordinate characters and the fourth moment is the arithmetic mean of \(|P|^4\) over all pairs of roots of unity; no factor of \((mn)^{-1/2}\) is included inside \(P\). The corresponding zero-shift autocorrelation has magnitude \(5\) and squared magnitude \(25\). We define its merit factor as this number divided by the total squared nonzero-shift autocorrelation, i.e. \(25/(\mathcal E(P)-25)\).

The condition is not asserted at small periods with difference aliasing. For the one-variable specialization, the thirteen distinct differences are \(0,\pm1,\pm2,\pm k,\pm2k,\pm(k-1),\pm(k+1)\), which are indeed distinct for \(k\ge4\).

## Proof
For an abstract character expansion \(P=\sum_{x\in S}p_x\gamma_x\) on the five-site cross, the orthogonality of the thirteen difference characters gives the exact autocorrelation identity
\[
\mathcal E(P)=\sum_{d\in S-S}\left|\sum_{x-y=d}p_x\overline{p_y}\right|^2.
\tag{1}
\]
There are one zero difference, four single-pair differences \(\pm2e_1,\pm2e_2\), four adjacent differences \(\pm e_1,\pm e_2\) with two ordered representations apiece, and four diagonal differences \(\pm e_1\pm e_2\), also with two ordered representations apiece. Because all five coefficients are unimodular, the zero difference contributes \(25\), the single-pair differences contribute \(4\), and the other contributions simplify as follows:
\[
\begin{aligned}
|a_+\overline c+c\overline{a_-}|^2&=2+2\operatorname{Re}U,\\
|b_+\overline c+c\overline{b_-}|^2&=2+2\operatorname{Re}V,\\
|a_+\overline{b_-}+b_+\overline{a_-}|^2
&=2+2\operatorname{Re}(U\overline V).
\end{aligned}
\]
The second diagonal type has the same squared magnitude as the third displayed expression. Counting each orientation yields the **complete exact identity**
\[
\boxed{\mathcal E(P)=45+4\operatorname{Re}U+4\operatorname{Re}V
+8\operatorname{Re}(U\overline V).}
\tag{2}
\]
Conversely every pair \((U,V)\in\mathbb T^2\) is realized, for example by choosing \(c=a_+=b_+=1\), \(a_-=U\), and \(b_-=V\). Thus (2) is the entire optimization problem, not merely a necessary bound.

Let \(r=\operatorname{Re}U\) and \(t=|1+2\overline U|=\sqrt{5+4r}\). Rearranging (2) produces an explicit nonnegative deficit certificate:
\[
\boxed{\mathcal E(P)-36=(t-2)^2+
4\left(t+\operatorname{Re}\bigl(V(1+2\overline U)\bigr)\right)\ge0.}
\tag{3}
\]
The second summand is nonnegative by \(|V|=1\). Since \(t\ge1\), equality in (3) demands \(t=2\), or \(r=-1/4\), and
\[
V=-\frac{1+2U}{2}=\overline U.
\]
The only unit complex numbers with real part \(-1/4\) are the two specified values of \(\zeta\). Each leaves the three free phases \(c,a_+,b_+\), with the other two determined by their products, and the two components do not intersect.

The simple inequalities \(\operatorname{Re}U,\operatorname{Re}V,\operatorname{Re}(U\overline V)\le1\) in (2) give \(\mathcal E(P)\le61\), with equality precisely at \(U=V=1\). Continuity of (2) on the connected torus \(\mathbb T^2\) proves attainment of every intermediate real value.

If all coefficients are roots of unity, then \(U\) is a root of unity. Equality at the minimum would require \(U+U^{-1}=-1/2\). But the left side is an algebraic integer, whereas a rational algebraic integer must be an integer, contradiction. For \(q\in\{2,3,4,6\}\), every real part of a \(q\)-th root of unity is a half-integer, so (2) is an integer. The minimum is therefore at least \(37\). If \(q\) is even, the choice \((U,V)=(1,-1)\) yields \(37\); for \(q=3\), the choice \((U,V)=(\omega,\omega^2)\), with \(\omega=e^{2\pi i/3}\), also yields \(37\). For \(q=1\), \(U=V=1\) and (2) gives \(61\). This proves the claimed phase-alphabet boundary and, via the central correlation \(25\), the merit factors.

## Verification
The independent standalone checker `checker.py`, run with Python's standard library, reproduces the fourth moment by enumerating the thirteen distinct autocorrelation shifts, compares it with (2) for 300 sampled unimodular coefficient vectors, and separately evaluates unnormalized discrete Fourier averages on six nonaliased product groups. It checks the algebraic optimizer on a five-by-seven Fourier grid and exhaustively enumerates the finite alphabets of orders \(1,2,3,4,6\). The execution completed 368 checks without assertion failures. The analytic proof (1)--(3), not numerical sampling, establishes the unrestricted theorem and all equality cases.

## Relationship to prior work
Schmidt's 2011 study of binary arrays derived from quadratic characters defines two-dimensional aperiodic autocorrelation and merit factor and proves asymptotic results for complete character arrays. Its Lemma 3.1 relates fourth-power Fourier samples to autocorrelation, but it does not optimize continuous unimodular phases on a fixed five-point cross. Schmidt's 2013 work on unimodular Littlewood polynomials uses the analogous one-dimensional fourth-norm identity and establishes asymptotic results for long Chu and Frank sequences; it likewise does not determine the present finite-support optimum.

The published record *Sharp fourth moments for a five-point Ferrers Fourier spectrum* treats a geometrically different five-point set containing just one three-term progression and maximizes a fourth-moment-to-energy quotient with **unrestricted amplitudes**. Its theorem does not imply the minimum under unit amplitudes here. *The first phase-frustrated low-multiplicity Fourier support occurs at six points* explicitly assumes no three-term progression; the present cross has two and therefore lies outside its theorem. *Sharp fourth-moment phase rigidity for the six-point triangular Fourier aperture* optimizes a different six-frequency support with cubic-root phases. Finally, *Sharp fourth-moment extension and one-axis rigidity for finite abelian crosses* maximizes over unrestricted coefficients on two **whole** subgroup axes rather than minimizing over five nonzero prescribed phases. None of these inspected statements implies (2) together with the exact minimizer and root-of-unity obstruction.

## Limitations
No claim is made for shorter cyclic periods where additional difference relations arise, for other support shapes, for arbitrary unequal amplitudes, or for maximum sidelobe magnitude rather than total squared sidelobe energy. The result is a sharp isolated five-site model and does not imply an asymptotic array-design theorem. The standard autocorrelation identity is prior mathematics. An older equivalent calculation in polyphase-array or short filter-design tables, possibly under a different normalization, remains a bibliographic risk; the preceding comparisons do not certify global uniqueness.

## References
1. K.-U. Schmidt, *The merit factor of binary arrays derived from the quadratic character*, arXiv:1105.5176v1 (first public 2011-05-26), especially Sections 1--3 and the asymptotic array theorems, https://arxiv.org/abs/1105.5176.
2. K.-U. Schmidt, *On a problem due to Littlewood concerning polynomials with unimodular coefficients*, arXiv:1302.2766v1 (first public 2013-02-12), especially Section 2, equation (5), and Theorems 1--2, https://arxiv.org/abs/1302.2766.
3. *Sharp fourth moments for a five-point Ferrers Fourier spectrum*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moments-for-a-five-point-ferrers-fourier-spectrum--bb5fd3f72396.
4. *The first phase-frustrated low-multiplicity Fourier support occurs at six points*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-first-phase-frustrated-low-multiplicity-fourier-support-occu--355e59ad0dcf.
5. *Sharp fourth-moment phase rigidity for the six-point triangular Fourier aperture*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-phase-rigidity-for-the-six-point-triangular--bea9cf2ed885.
6. *Sharp fourth-moment extension and one-axis rigidity for finite abelian crosses*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-extension-and-one-axis-rigidity-for-finite-a--5b31463115dc.
