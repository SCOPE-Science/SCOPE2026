# Residue-rigid Fourier zeros and complete spectra of prime-square Frobenius graphs

## Finding
For every **odd prime** \(p\), put \(R=\mathbb Z/p^2\mathbb Z\), let \(h:\mathbb F_p\to\mathbb F_p\) be any function, and set
\[
f_h(x)=x^p+p h(x\bmod p)\pmod {p^2},\qquad E_h=\{(x,f_h(x)):x\in R\}\subset R^2.
\]
There are \(p^p\) distinct choices of \(h\). All these (generally nonaffine) graphs have exactly the **same Fourier-zero set**. For the unnormalized Fourier transform, with \(e_q(t)=\exp(2\pi i t/q)\),
\[
\boxed{\widehat{\mathbf1}_{E_h}(u,v)=0 \iff p\nmid u\ \text{or}\ [p\mid u,\ p\mid v,\ u+v\not\equiv0\pmod {p^2}].}
\]
Consequently the additive convolution operator by \(\mathbf1_{E_h}\) on \(\ell^2(R^2)\) has **exact rank**
\[
\boxed{p^3-p^2+p},\qquad
\frac{\operatorname{rank}}{p^4}=\frac1p-\frac1{p^2}+\frac1{p^3}\longrightarrow0.
\]
A frequency spectrum is an unordered set \(\Lambda\subset R^2\) of exactly \(p^2\) distinct labels such that the restrictions of \(p^{-1}e_{p^2}(ux+vf_h(x))\), indexed by \((u,v)\in\Lambda\), form an orthonormal basis of \(\ell^2(E_h)\) with the unnormalized counting inner product.

**All spectra, uniquely:** choose an arbitrary function \(b:\mathbb F_p\to\mathbb F_p\). For each \(a\in\mathbb F_p\), independently choose an arbitrary function \(s_a:\mathbb F_p\to\mathbb F_p\). Taking all field values in their canonical integer representatives \(0,\ldots,p-1\), form
\[
\boxed{\Lambda(b,s)=\bigcup_{a\in\mathbb F_p}\left\{\left(a+p s_a(c),\ b(a)+p(c-s_a(c))\right):c\in\mathbb F_p\right\}\subset R^2.}
\]
Every such set is a spectrum of every \(E_h\), and every spectrum arises **once and only once** this way. In particular,
\[
\boxed{\#\{\text{unordered spectra of }E_h\}=p^{p^2+p}.}
\]
Exactly \(p^3(p-1)\) spectra are affine graphs \(\{(u,\alpha u+\beta):u\in R\}\); this is equivalent to \(\alpha\not\equiv-1\pmod p\). The result counts ambient frequency sets without identifying shifts, permutations, or affine equivalences. For \(p=3\) the convolution rank is \(21\) in dimension \(81\), while there are \(3^{12}=531441\) distinct spectra. For \(p=5\) the rank is \(105\) in dimension \(625\), and the number of spectra is \(5^{30}\).

## Assumptions and scope
The prime \(p\) is odd and \(h\) is an arbitrary function on the residue field, not necessarily a polynomial. The graph is formed modulo \(p^2\), and there are no restrictions on \(h\). The label pairing is the standard additive dot product on \(R^2\). An orthonormal basis has \(p^2\) vectors because \(|E_h|=p^2\). The convolution normalization is the unnormalized sum \((Tf)(y)=\sum_{z\in E_h}f(y-z)\). The rank count is over \(\mathbb C\). No assertion is made for higher prime powers or for arbitrary functions with nonlinear reduction modulo \(p\). The prime \(p=2\) is omitted from the novelty claim because its four-point instance belongs to an already studied dyadic parabola case.

## Proof
**1. Frobenius constancy on residue fibres.** Write \(x=a+pt\), with \(0\le a,t<p\). The binomial theorem gives \((a+pt)^p\equiv a^p\pmod {p^2}\), while \(f_h(a)\equiv a\pmod p\) by Fermat's congruence. Hence \(f_h(a+pt)=f_h(a)\) in \(R\) and \(f_h(a)\bmod p=a\).

**2. The complete Fourier-zero criterion.** Define \(S_h(u,v)=\sum_{x\in R}e_{p^2}(ux+vf_h(x))\). If \(p\nmid u\), the \(p\)-point sum over \(t\) from Step 1 is \(\sum_{t=0}^{p-1}e_p(ut)=0\). Now suppose \(u=ps\). If also \(v=pt\), reduction modulo \(p\) gives
\[
S_h(ps,pt)=p\sum_{a\in\mathbb F_p}e_p((s+t)a)=\begin{cases}p^2,&s+t=0\text{ in }\mathbb F_p,\\0,&s+t\ne0\text{ in }\mathbb F_p.\end{cases}
\]
Finally, if \(p\nmid v\), write \(r_a=psa+vf_h(a)\pmod{p^2}\). Its residues \(r_a\bmod p=va\bmod p\) run through every residue class once. Consider \(P(X)=\sum_aX^{r_a}\), with each exponent represented between \(0\) and \(p^2-1\). If \(P(e^{2\pi i/p^2})=0\), the minimal polynomial \(\Phi_{p^2}(X)=1+X^p+\cdots+X^{(p-1)p}\) divides \(P\) in \(\mathbb Q[X]\). Since \(\deg P<p^2\), the quotient would have degree at most \(p-1\), implying for each fixed residue \(j\bmod p\) that the coefficients of \(X^{j},X^{j+p},\ldots,X^{j+(p-1)p}\) in \(P\) are all equal. But exactly one such coefficient equals one and all others equal zero. This contradiction proves \(S_h(ps,v)\ne0\). All cases have been exhausted, giving the displayed zero criterion. Counting nonzero frequencies yields \(p(p^2-p)+p=p^3-p^2+p\); Fourier characters diagonalize finite abelian convolution, proving the rank claim.

**3. Necessary structure of every spectrum.** A set \(\Lambda\) of \(p^2\) frequencies is a spectrum exactly when each nonzero difference of its frequencies belongs to the zero set in Step 2. Partition \(\Lambda\) by the residue \(a=u\bmod p\). Distinct parts are automatically orthogonal because their first-coordinate differences are units. Inside one part, \(u\)-differences are divisible by \(p\). The Step 2 criterion forces all second-coordinate residues to agree, say \(b(a)\). Write each point uniquely as \((a+ps,b(a)+pt)\). Two distinct points in this part are orthogonal exactly when their labels \(s+t\bmod p\) differ. Therefore each part contains at most \(p\) points. There are at most \(p\) parts and \(p^2\) frequencies, so all \(p\) parts must occur and each contains exactly \(p\) points. The labels \(c=s+t\) run through \(\mathbb F_p\), determining exactly one function \(s_a(c)\) for each \(a\), and giving the displayed parameterization with no duplication.

**4. Sufficiency, count, and affine subclass.** Conversely any specified \(b\) and \(s_a\) yield distinct frequencies, and pairs from different parts have unit first-coordinate difference while those from the same part have different \(c\)-labels. They are orthogonal by Step 2 and have number \(p^2\), hence form a basis. There are \(p^p\) possibilities for \(b\) and \(p^{p^2}\) independent choices for all \(s_a\), giving \(p^{p^2+p}\). For an affine graph \(v=\alpha u+\beta\), every \(u\in R\) appears exactly once. The only potentially forbidden differences are \(\Delta u=ps\ne0\), where \(\Delta v=p(\alpha\bmod p)s\). Orthogonality holds exactly when \(1+\alpha\not\equiv0\pmod p\). There are \(p(p-1)\) slopes and \(p^2\) intercepts, giving \(p^3(p-1)\). This also proves that the classification is uniform over all \(h\).

## Verification
The standalone `verify.py` in this package performs exact cyclotomic divisibility calculations without floating-point zero tests. It exhaustively checks all Fourier frequencies for every one of the \(3^3=27\) residue perturbations at \(p=3\), and for three independently chosen perturbations each at \(p=5,7\). It checks three constructed complete spectra for each perturbation and counts all affine spectra by exact character-sum tests at \(p=3,5\). An independent exhaustive four-point test at \(p=2\) yields \(64\) spectra, as a boundary consistency check only. Running `python3 verify.py` prints `ALL_EXACT_CERTIFICATES_OK`, `AFFINE_SPECTRA_ENUMERATION_OK 3 54`, and `AFFINE_SPECTRA_ENUMERATION_OK 5 500`. No finite computation substitutes for Steps 1–4, which establish the claims for all odd primes and all functions \(h\).

## Relationship to prior work
Heilbronn exponential sums, including the sum indexed by \(a\mapsto a^p\pmod{p^2}\), have been studied for nontrivial magnitude bounds by Shkredov (2012), following Heath-Brown and Konyagin. Those results concern magnitude estimates and Fermat quotients; they do not identify all Fourier-zero frequencies of two-coordinate graphs or classify exponential basis partners. A published general theorem of Zhou (2024 first posting, 2026 revision) establishes that spectral sets and translational tiles coincide in \(\mathbb Z/p^2\mathbb Z\times\mathbb Z/p^2\mathbb Z\), but its general equivalence does not supply the present fixed-graph Fourier-zero formula, universality across arbitrary digit perturbations, enumeration of **all** spectra, or affine-subclass count. Separate published classifications of the prime-square cubic graph (for \(p\ge5\)) and odd-prime-power parabola yield different derivative-driven and strictly contracting frequency geometries; neither statement covers \(x^p+p h(x\bmod p)\) or implies the displayed count. The cyclotomic-divisibility criterion is standard, not claimed new; the contribution is its exact synthesis with residue-fibre saturation for the canonical Frobenius graph class.

## Limitations
The theorem is restricted to odd prime squares, standard additive characters, and residue-constant lifts with identity reduction. It does not determine the magnitudes of the surviving primitive coefficients, classify arbitrary two-dimensional spectral sets, imply injectivity of ambient convolution, or extend automatically to prime cubes. The analysis is not a priority certification: an equivalent general spectral-partner classification in historical work on finite abelian tilings, cyclotomic masks, or Butson matrices remains possible. Independent validation has not been performed.

## References
1. I. D. Shkredov, *On Heilbronn's exponential sum*, arXiv:1208.6124v1, first posted 2012-08-30, https://arxiv.org/abs/1208.6124 (Introduction, Preliminaries and proof, especially the subgroup \(\{a^p\}\) and Fourier methods).
2. W. Zhou, *On Tiling and Spectral Sets in \(\mathbb Z_{p^2}\times\mathbb Z_{p^2}\)*, arXiv:2412.18132v1, first posted 2024-12-24; relevant full-text comparison to the 2026 v4 Theorem 1 and Sections 3–5, https://arxiv.org/abs/2412.18132.
3. *All exponential spectra of the cubic graph over prime-square cyclic rings*, published full statement and proof, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-all-exponential-spectra-of-the-cubic-graph-over-prime-square-cyc--a783058468ac.
4. *Complete exponential spectra of the parabola over odd prime-power rings*, published full statement and proof, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-complete-exponential-spectra-of-the-parabola-over-odd-prime-powe--2cf08dd7e325.
