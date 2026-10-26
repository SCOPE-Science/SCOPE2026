# A sharp modal ceiling and finite spectral-norm certificate for multi-annular Gaussian localization

## Finding
Let \(m\ge 1\) and \(0\le a_1<b_1<a_2<b_2<\cdots<a_m<b_m<\infty\). Put \(E=\bigcup_{j=1}^{m}[a_j,b_j]\). In the Gaussian Bargmann–Fock Hilbert space with measure \(e^{-|z|^2}\,dA(z)/\pi\), consider the positive localization (Toeplitz) operator with symbol \(\mathbf 1_{\{|z|^2\in E\}}\). Its eigenvalues, in the normalized monomial basis, are
\[
\lambda_n=\frac1{n!}\sum_{j=1}^m\int_{a_j}^{b_j} e^{-t}t^n\,dt,\qquad n=0,1,2,\ldots .
\]
The ordered eigenvalue sequence possesses at most \(m\) distinct local-maximum plateaux, counting a possible plateau beginning at index zero. The ceiling \(m\) is attained for some configuration of \(m\) separated annuli for every \(m\).

More strongly, define the real exponential sum for \(s\ge0\)
\[
F(s)=\sum_{j=1}^m\bigl(e^{-a_j}a_j^{s+1}-e^{-b_j}b_j^{s+1}\bigr),
\]
with \(0^{s+1}=0\). It has at most \(2m-1\) zeros on \([0,\infty)\), counted with multiplicity. Let \(Z\) denote those real zeros and set
\[
\mathcal S=\{0\}\cup\bigcup_{s\in Z}\{\lfloor s\rfloor,\lfloor s\rfloor+1\}.
\]
Then \(\mathcal S\subset\mathbb N_0\), \(|\mathcal S|\le4m-1\), and the **exact operator norm** is
\[
\|T_E\|=\max_{n\in\mathcal S}\lambda_n.
\]
Thus the number of indices needed to determine the exact norm is bounded solely by the number of annuli, independently of their radii or separation. The roots are defined intrinsically by the displayed exponential polynomial; this is a finite exact characterization, not a claim that all roots admit elementary closed forms.

## Assumptions and scope
The symbol is the indicator of a **finite** union of \(m\) nondegenerate, pairwise separated, concentric annuli in the Gaussian phase plane, with squared-radius endpoints exactly as specified. The associated localization operator is the Bargmann–Fock conjugate of the Gaussian-window short-time Fourier-transform localization operator, with radial coordinate scaled so its Gaussian density is \(e^{-t}\). The Hermite basis under that unitary conjugation corresponds to normalized analytic monomials. The claim includes all real endpoints in the stated range and all integers \(m\ge1\), including a disk component with \(a_1=0\). The spectral norm is the positive largest eigenvalue.

A local-maximum plateau means a maximal interval of consecutive indices on which \(\lambda_n\) is constant and neither available adjacent eigenvalue is greater. Strictly separated maxima count separately. As \(\lambda_n>0\) and \(\lambda_n\to0\), the operator norm is attained.

## Proof
**Diagonalization.** The normalized Fock monomial \(e_n(z)=z^n/\sqrt{n!}\) has squared mass \(e^{-|z|^2}|z|^{2n}\,dA/ (\pi n!)\). Angular orthogonality diagonalizes the radial symbol. Substituting \(t=|z|^2\) gives the stated \(\lambda_n\). Integration by parts, or the incomplete-gamma recurrence, gives exactly
\[
\lambda_{n+1}-\lambda_n=\frac{F(n)}{(n+1)!}.
\]
Since \(E\subset[0,b_m]\), the bound \(\lambda_{n+1}\le b_m\lambda_n/(n+1)\) implies \(\lambda_n\to0\) and eventual strict descent.

**A generalized Descartes lemma.** If \(0<x_1<\cdots<x_q\) and all \(c_i\ne0\), then the number of positive real roots, including multiplicity, of \(H(t)=\sum_{i=1}^q c_i t^{x_i}\) is no larger than the number of sign changes in \((c_1,\ldots,c_q)\). The same holds for arbitrary strictly increasing real exponents. Here is an induction proof: divide by the first monomial to obtain \(G(t)=c_1+\sum_{i\ge2}c_i t^{x_i-x_1}\). Its derivative has the same ordered coefficient signs as \((c_2,\ldots,c_q)\), so the induction hypothesis bounds its positive roots by their sign variations. If \(c_1\) and \(c_2\) have opposite signs, Rolle's theorem bounds the roots of \(G\) by one plus those of \(G'\). If they have the same sign, then \(G\) starts with sign \(c_1\) and moves initially away from zero; before its first positive root, \(G'\) must already have a zero, giving the stronger bound without the extra one. Rolle's theorem with multiplicities justifies both inequalities, completing the induction. Terms with an endpoint zero are deleted before application.

Apply this lemma with \(t=e^s\) to the \(2m\) ordered bases \(a_1,b_1,\ldots,a_m,b_m\). Coefficients alternate positive, negative, positive, negative. If \(a_1=0\), the initial positive term is absent; the remaining list has \(2m-2\) sign variations. Hence \(F\) has at most \(2m-1\) zeros for \(s\ge0\). In fact the same bound applies throughout the real domain when \(a_1>0\).

**Modal bound.** The signs of the discrete first differences are the signs of \(F\) at nonnegative integer arguments. Every new local maximum after a preceding minimum requires an alternation from nonpositive to positive differences and then back to nonpositive differences. Equivalently, when \(a_1>0\), \(F\) starts positive as \(s\to-\infty\) and ends negative, so each local-maximum plateau consumes a distinct positive-to-negative sign crossing (possibly through a zero). Because at most \(2m-1\) zeros occur, there are at most \(m\) such plateaux. When \(a_1=0\), \(F\) begins negative as \(s\downarrow-1\) (the first remaining base is \(b_1\)), and has at most \(2m-2\) zeros; a maximum at the boundary index zero can occur, but each subsequent distinct maximum requires two further sign reversals, again giving at most \(m\). The argument also covers equal consecutive eigenvalues by counting their zero-valued differences as roots, with multiplicity when necessary.

**Finite candidates.** A global maximum at \(n\ge1\) satisfies \(F(n-1)\ge0\ge F(n)\). Continuity produces a root in \([n-1,n]\), including either endpoint in the equality cases. That maximum index equals either \(\lfloor s\rfloor\) or \(\lfloor s\rfloor+1\) for such a root \(s\). The index-zero case is in \(\mathcal S\) by definition. The root bound gives at most \(1+2(2m-1)=4m-1\) candidates, proving the norm formula.

**Sharpness for every number of rings.** Fix \(m\). For large positive integers \(L\), take \(a_j=jL\) and \(b_j=jL+1\) for \(1\le j\le m\). For the contribution of the \(j\)-th interval to \(F(n)\), write \(a=jL\) and divide the upper-endpoint contribution by the lower-endpoint contribution. The ratio equals \(R=\exp[-1+(n+1)\log(1+1/a)]\). At \(n=a-2\), \(\log R=-3/(2a)+O(a^{-2})<0\), whereas at \(n=a+2\), \(\log R=5/(2a)+O(a^{-2})>0\). These two contributions to \(\lambda_{n+1}-\lambda_n\) therefore have respectively positive and negative signs with magnitudes bounded below by fixed multiples of \(L^{-3/2}\) for fixed \(j\). Every other interval contributes only \(e^{-cL}\) times a polynomial factor, by strict positivity of \(k-j-j\log(k/j)\) for \(k\ne j\), the large-deviation exponent of the Poisson kernel. Consequently \(F(a_j-2)>0>F(a_j+2)\) simultaneously for all \(j\) once \(L\) is large. Each disjoint index block then contains a separate maximum, proving that the upper bound \(m\) is sharp.

## Verification
The standalone file `verify.py` evaluates independent incomplete-gamma eigenvalue differences against the exact endpoint expression, tests mode ceilings on reproducible random finite interval families, and constructs sharply separated configurations for \(m=1,\ldots,6\). Run with Python 3 and SciPy via `python verify.py`. The recorded result is `VERIFY_OUTPUT.txt`, reporting 1,843 successful numerical checks. This is corroboration only: neither finite parameter samples nor root scans prove the universal root bound, which is supplied by the Descartes lemma, or its sharpness, which is supplied by the large-separation argument.

## Relationship to prior work
Knutsen's 2019 preprint studies Gaussian localization and, in Section 3.1 of its full published text, estimates the norm for one ring; its later sections treat Cantor-type unions. The exact single-ring eigenvalue representation is prior knowledge. Galbis (2021 preprint), Sections 2–3, establishes general radial Fock Toeplitz norm estimates and the Bargmann/STFT identification but not a sharp bound on the number of eigenvalue modes for an arbitrary finite union of rings. Dewage–Ólafsson (2021 preprint), Sections 1–2, analyzes the general algebra and eigenvalue maps for quasiradial Fock Toeplitz symbols without the displayed finite modal and root-candidate certificates. The existing two-ring large-radius result describes a different asymptotic question: the number and relative heights of peaks at Gaussian-scale separation; it does not cover arbitrary finite ring sets or the universal at-most-\(m\) mode bound. The proof uses classical generalized Descartes variation, and an unnoticed prior application of this principle specifically to annular localization remains possible.

## Limitations
Only the one-complex-dimensional Gaussian localization operator with a finite union of truly radial annuli is covered. General smooth, signed, nonradial, or infinitely disconnected masks need not satisfy the same modal ceiling. The certificate does not provide a universally elementary closed form for its exponential-polynomial roots, numerical root isolation still requires care, and it does not assert anything about ordered singular values for nonradial operators. The Descartes principle itself is classical and is not claimed as original. The novelty assessment is best-knowledge, not independent priority certification.

## References
1. H. Knutsen, *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets I*, arXiv:1907.00848 (first public 2019-07-01); *Journal of Fourier Analysis and Applications* 26, 47 (2020), https://doi.org/10.1007/s00041-020-09751-9 (full open-access text, Sections 2–4 inspected).
2. A. Galbis, *Norm estimates for selfadjoint Toeplitz operators on the Fock space*, arXiv:2102.02031 (first public 2021-02-03), https://arxiv.org/html/2102.02031v1 (full open text, Sections 2–3 inspected).
3. J. P. G. Dewage and G. Ólafsson, *Toeplitz operators on the Fock space with quasi-radial symbols*, arXiv:2107.01465 (first public 2021-07-03), https://arxiv.org/abs/2107.01465 (full open HTML, Sections 1–2 inspected).
4. F. Nicola and P. Tilli, *The norm of time-frequency and wavelet localization operators*, arXiv:2207.08624 (2022-07-18); abstract inspected for broader norm coverage, full text not accessed in this comparison.
