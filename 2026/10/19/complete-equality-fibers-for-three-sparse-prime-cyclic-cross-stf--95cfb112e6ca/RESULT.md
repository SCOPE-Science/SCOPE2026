# Complete equality fibers for three-sparse prime-cyclic cross-STFT uncertainty

## Finding
Fix a prime \(p\ge7\). For functions \(f,g:\mathbb Z_p\to\mathbb C\) each with **exactly three nonzero coefficients**, set
\[
 V_g f(x,k)=\sum_{y\in\mathbb Z_p}f(y)\overline{g(y-x)}e^{-2\pi i k y/p}.
\]
The sharp support inequality \(|\operatorname{supp}V_g f|\ge5p-4\) is already a consequence of Krahmer–Pfander–Rashkov [1, Proposition 4.4]; its numerical value is **not** a new claim. The finding here is the following complete characterization of **every equality pair**, including its support geometry and its complex coefficient parameters.

Equality \(|\operatorname{supp}V_g f|=5p-4\) holds if and only if the supports of \(f\) and \(g\) are three-term arithmetic progressions with a common nonzero step and, after separately translating them, applying the same invertible index dilation, and multiplying them by independent nonzero constants, they are supported on \(\{0,1,2\}\), normalized by \(f(2)=g(2)=1\), and their coefficient triples have **exactly** this form:
\[
 \begin{aligned}
 &\eta,\theta,\rho\in\mu_p,\qquad \eta\ne\theta,\qquad
 T=-(\eta+\theta),\qquad \sigma=\eta\theta/\rho,\qquad t\in\mathbb C^\times,\\
 &(f(0),f(1),f(2))=\left(-\frac{\rho t^2}{T},\ t,\ 1\right),\\
 &(g(0),g(1),g(2))=\left(\overline{-\frac{\sigma T}{t^2}},\ \overline{\frac{T}{t}},\ 1\right),
 \end{aligned}
\]
where \(\mu_p=\{e^{2\pi i j/p}:0\le j<p\}\). All coefficients are nonzero: \(T\ne0\), because the quotient of two distinct odd-order roots of unity cannot be \(-1\). The same family may be parameterized without redundancy by taking \(\{\eta,\theta\}\) as an **unordered** two-element subset of \(\mu_p\), together with \(\rho\in\mu_p\) and \(t\ne0\).

Consequently, for the fixed normalized supports \(\{0,1,2\}\) and fixed normalization \(f(2)=g(2)=1\), the entire equality locus is a disjoint union of exactly
\[
 \boxed{\frac{p^2(p-1)}2}
\]
parameter families, each bijectively parameterized by \(\mathbb C^\times\). In fact these are its connected components in the usual coefficient topology, since the two central Fourier-zero locations and the designated side-zero location take values in finite sets and are locally constant on the equality locus.

## Assumptions and scope
The modulus \(p\) is any prime at least seven. Both functions have exactly three nonzero entries with arbitrary complex values; neither is required to equal the other. The displayed STFT uses the unnormalized discrete Fourier convention; a nonzero scalar transform normalization cannot change support. The reductions allowed in the theorem preserve support cardinality: independent spatial translations of \(f\) and \(g\), one shared multiplication of spatial indices by an element of \(\mathbb Z_p^\times\), and independent nonzero scalar multiplication. The classification is for the normalized triple in the **given coordinate order** \(0,1,2\); the orientation change of a progression can give another valid normalization without affecting the theorem. No classification is asserted for \(p=2,3,5\), composite orders, or larger time-support sizes.

## Proof
Write \(A=\operatorname{supp}f\), \(B=\operatorname{supp}g\), and \(X=A-B\). For each \(x\in X\), let
\[
 h_x(y)=f(y)\overline{g(y-x)},\qquad r_x=|\operatorname{supp}h_x|=|A\cap(x+B)|.
\]
The \(x\)-row of \(V_gf\) is exactly the discrete Fourier transform of \(h_x\). The prime-order Fourier uncertainty theorem \(|\operatorname{supp}h_x|+|\operatorname{supp}\widehat h_x|\ge p+1\) yields
\[
 |\operatorname{supp}V_gf|\ge |X|(p+1)-\sum_{x\in X}r_x.
\]
Every ordered pair in \(A\times B\) contributes to exactly one \(r_x\), so \(\sum r_x=|A||B|=9\). The Cauchy–Davenport inequality gives \(|X|\ge5\), and hence the classical bound \(5p-4\). If equality holds, the integer \(|X|\) must equal five, since \(p+1>0\) and increasing \(|X|\) raises the displayed lower bound. Vosper's inverse theorem, applicable because \(2\le|A|,|B|=3\) and \(|A-B|=5\le p-2\), then implies that \(A\) and \(-B\), and therefore \(A\) and \(B\), are progressions with a common step up to its sign. A common invertible dilation and independent translations reduce both to \(\{0,1,2\}\). These transformations only reindex and unimodularly rescale STFT entries, preserving their zero pattern cardinality.

Write the three nonzero values as \(f=(a,b,c)\), \(g=(d,e,h)\) in ascending coordinate order. Independent scalar normalizations arrange \(c=h=1\). For \(z=e^{-2\pi ik/p}\), the five potentially nonzero STFT rows, after discarding harmless nonzero monomial factors, are precisely
\[
 \begin{array}{c|c}
 x&\text{row polynomial}\,\\\hline
 -2& a\\
 -1& a\overline e+bz\\
 0& a\overline d+b\overline e z+z^2\\
 1& b\overline d+\overline e z\\
 2& \overline d
 \end{array}.
\]
There are no other nonzero rows, and the outer rows contain no frequency zeros. The two linear rows have at most one zero each on \(\mu_p\); the quadratic central row has at most two. As the target support is \(5p-4\), equality holds **if and only if** both linear polynomials have a root in \(\mu_p\) and the quadratic has two distinct roots there. Denote these roots by \(\rho\) at shift \(-1\), \(\sigma\) at shift \(1\), and \(\eta,\theta\) at shift zero. The respective factor identities are
\[
 -\frac{a\overline e}{b}=\rho,\qquad
 -\frac{b\overline d}{\overline e}=\sigma,\qquad
 a\overline d=\eta\theta,\qquad b\overline e=-(\eta+\theta)=T.
\]
Multiplying the first two identities yields \(\rho\sigma=a\overline d=\eta\theta\), proving \(\sigma=\eta\theta/\rho\). Put \(t=b\ne0\). The equation \(b\overline e=T\) gives \(\overline e=T/t\); the first linear root gives \(a=-\rho t^2/T\); and the other gives \(\overline d=-\sigma T/t^2\). This reconstructs the claimed parameterization and proves necessity. Since \(p\) is odd, \(\eta+\theta=0\) cannot occur for two \(p\)-th roots, so all formulas are well-defined.

Conversely, choose any permitted \(\{\eta,\theta\},\rho,t\) and construct the triples. The five-row identities then have exactly the prescribed roots in \(\mu_p\), two in the central row and one in each neighboring row, while both outer rows are nowhere zero. Their total support is \(5p-4\). This proves sharpness and sufficiency.

For fixed normalized supports, the two unordered central roots and the root \(\rho\) are recoverable uniquely from the STFT, and \(t=f(1)\) is recoverable from the coefficients. Thus the parameterization is one-to-one. There are \(\binom p2\cdot p\) discrete root choices. Each corresponding \(t\)-fiber is a copy of \(\mathbb C^\times\) and is connected. Along a continuous path in the equality locus, the distinct exact sampled zero indices cannot jump, since each nonzero row entry remains nonzero and the support count is fixed at its maximal cancellation value. Therefore the distinct root-choice fibers are distinct connected components.

## Verification
The accompanying standalone `verify.py` directly evaluates the cyclic STFT as a double finite sum, rather than relying on the five-row factorization used in the proof. It checked 962 parameter triples for primes from seven up to 61, including all \(\binom p2 p\) root configurations at orders seven and eleven with one nontrivial coefficient parameter. It also exhaustively checked the inverse-sumset geometry for every ordered pair of three-point sets at orders seven and eleven, finding 752 cases of the sharp five-shift geometry and verifying that each admits a shared progression step. The output was:

`VERIFY_OK 962 direct cross-STFT extremizers; 752 equal-sumset supports at p=7,11`

The finite tests do not prove the universal statement. The proof uses the prime Fourier uncertainty theorem, Vosper's inverse theorem, and exact low-degree polynomial factorization. Numerical zero thresholds in the checker are only finite corroboration.

## Relationship to prior work
Krahmer, Pfander and Rashkov [1, Proposition 4.4, arXiv version] prove the general prime-cyclic STFT lower bound, which specializes to \(5p-4\) when both supports have size three. Their proof already uses prime Fourier uncertainty and Cauchy–Davenport, so **neither the numerical inequality nor these general ingredients are newly asserted**. The present result instead classifies exactly which pairs attain that previously known bound, including a necessary support geometry and a complete explicit complex-amplitude/phase parameterization.

Nicola [2, Theorem 1.2] classifies equality in the universal lower bound \(|\operatorname{supp}V_gf|\ge p\), which is a different support level and does not provide the equality fibers for exact three-sparse pairs. Bartusel [3] uses STFT uncertainty principles for phase-retrieval conditions but does not state this sharp sparse-pair equality classification.

The published result *Parity-rigid ambiguity-support spectra for primitive three-tap cyclic signals* [4] gives a sharp classification for the **self-ambiguity** subcase \(g=f\) on three-term progressions, not for two independently chosen complex-valued three-sparse signals, nor the necessity of the common progression geometry for attaining the cross-transform bound. The published *Exact support trichotomy for two-sparse prime cyclic STFTs* [5] concerns two nonzero taps in each signal/window and has a different support law. These results were compared by their hypotheses and conclusions, not by title alone.

## Limitations
This theorem is an equality-case result for a known inequality, not a new stronger uncertainty inequality. It does not classify nearly minimizing pairs, quantify robustness to perturbations, treat primes five or below, or cover composite groups. Its topological component count uses the specified fixed normalized coordinate labels and is not a count after quotienting by all symmetries. Although the closest relevant primary papers and publicly available specialized findings were inspected, an equivalent unpublished or unindexed equality classification cannot be excluded; there is no claim of independent historical-priority certification.

## References
1. F. Krahmer, G. E. Pfander and P. Rashkov, *Uncertainty in time–frequency representations on finite Abelian groups and applications*, arXiv:math/0611493v1 (16 November 2006), Section 4, Proposition 4.4; *Applied and Computational Harmonic Analysis* 25 (2008), 209–225. https://arxiv.org/html/math/0611493v1
2. F. Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality*, arXiv:2204.14176v1 (29 April 2022), Theorem 1.2. https://arxiv.org/html/2204.14176v1
3. D. Bartusel, *Uncertainty Principles as a Tool for STFT Phase Retrieval*, arXiv:2605.31507 (first submitted 29 May 2026). https://arxiv.org/abs/2605.31507
4. *Parity-rigid ambiguity-support spectra for primitive three-tap cyclic signals*, published mathematical result (11 October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-parity-rigid-ambiguity-support-spectra-for-primitive-three-tap-c--4fe8e5c0fab7
5. *Exact support trichotomy for two-sparse prime cyclic STFTs*, published mathematical result (4 October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-support-trichotomy-for-two-sparse-prime-cyclic-stfts--5b84852d543c
