# All-order progression blindness and sharp four-site identification in generalized paperfolding shifts

## Finding
For an arbitrary sequence of fold signs \(\varepsilon=(\varepsilon_k)_{k\ge0}\in\{-1,1\}^{\mathbb N_0}\), let \(f_\varepsilon(n)=\varepsilon_{\nu_2(n)}\chi_4(n/2^{\nu_2(n)})\), \(n\ge1\), where \(\chi_4(u)=1\) for \(u\equiv1\pmod4\) and \(-1\) for \(u\equiv3\pmod4\). Every equally spaced correlation
\[
 C_{m,\varepsilon}(h)=\lim_{N\to\infty}\frac1N\sum_{n=1}^{N}\prod_{j=0}^{m-1}f_\varepsilon(n+jh)
\]
exists for every pair of integers \(m,h\ge1\), and **is independent of every fold sign**. Explicitly, for odd \(m\) or odd \(h\) it is zero; for even \(m\) and \(a=\nu_2(h)\ge1\), it equals
\[
 C_{m,\varepsilon}(h)=1-2^{1-a}+(-1)^{m/2}2^{-a}.
\]

In sharp contrast, the four-site observations with spatial offsets \((0,2^k,2^{k+1},2^{k+3})\) have correlations \(B_{k,\varepsilon}\) satisfying
\[
 B_{0,\varepsilon}=\varepsilon_0\varepsilon_1/8,\qquad
 B_{k,\varepsilon}=1-3\cdot2^{-k}+2^{-k-3}\varepsilon_k\varepsilon_{k+1}\quad(k\ge1).
\]
Hence all these four-site correlations recover every adjacent product \(\varepsilon_k\varepsilon_{k+1}\) and thus recover the entire fold-sign sequence up to simultaneous sign reversal. Moreover, **every four-site correlation with four distinct integer offsets of diameter strictly below eight is independent of the fold signs**, whereas the offset set \((0,1,2,8)\) distinguishes fold-sign sequences. The distinguishing diameter eight is optimal.

## Assumptions and scope
The signs \(\varepsilon_k\) are completely arbitrary (not assumed periodic, automatic, typical, or independently random). The correlations average over integer shifts of one fixed paperfolding word. Oddness, evenness and valuation statements refer to positive integers; the four offsets may be translated by any common integer without affecting the limiting correlation. The sign normalization is the standard generalized paperfolding convention with digit formula \(f_\varepsilon(2^ku)=\varepsilon_k\chi_4(u)\) for odd \(u\). Simultaneous global sign reversal sends \(f_\varepsilon\) to its negative and leaves every even-point correlation unchanged.

## Proof
**Existence and exact cylinder formula.** Extend \(f_\varepsilon\) to \(\mathbb Z_2\setminus\{0\}\) by the same valuation formula. This measurable function is locally constant away from the origin; its mean is zero, since for any valuation class the odd part is equidistributed between \(1\) and \(3\pmod4\). For fixed finite offsets, the product is locally constant away from finitely many points, so periodic cylinder approximation gives existence of the Cesàro mean, equal to the integral against normalized Haar measure. Equivalently, fix distinct offsets \(S\), diameter \(d\), and \(K\ge\max(3,\operatorname{bitlength}(d)+2)\). Partition by \(x\bmod2^K\). Each residue class with some \(x+s\equiv0\pmod{2^{K-1}}\) contributes zero: because the offsets differ by less than \(2^{K-1}\), at most one factor has this unresolved valuation, and its conditional mean is zero. For every other residue, each factor's valuation (at most \(K-2\)) and odd part modulo four are fixed; the product is an explicit monomial in the finitely many \(\varepsilon_j\). This proves an exact finite, not asymptotic, polynomial formula for any fixed correlation.

**Odd number of sites.** For an equally spaced progression of odd length \(m\), the Haar involution \(x\mapsto-x-(m-1)h\) reverses the offsets. Because \(f_\varepsilon(-x)=-f_\varepsilon(x)\) except on a null set, the integral is its own negative and is zero.

**Even number of sites, odd spacing.** Put \(m=2L\), let \(h\) be odd, and split \(x\) by parity. Exactly \(L\) sites in either half are odd and have consecutive modulo-four characters; the remaining \(L\) factors reduce, after division by two, to an \(L\)-site progression for the shifted instruction sequence \(\sigma\varepsilon=(\varepsilon_{k+1})_{k\ge0}\). If \(L\) is even, the odd factors multiply to the constant \((-1)^{L(L-1)/2}\), giving
\[
 C_{2L,\varepsilon}(h)=(-1)^{L(L-1)/2}C_{L,\sigma\varepsilon}(h).
\]
If \(L\) is odd, each half instead reduces (up to a constant and translation) to the twisted integral \(J=\int_{\mathbb Z_2}(-1)^y\prod_{j=0}^{L-1}f_{\sigma\varepsilon}(y+jh)\,dy\). The involution \(y\mapsto-y-(L-1)h\) leaves \((-1)^y\) unchanged because \(L-1\) is even, while reversing the sign of the odd number of paperfolding factors. Thus \(J=0\). Induction on the two-adic valuation of \(m\) proves \(C_{m,\varepsilon}(h)=0\) for every even \(m\) at odd \(h\).

**Even number of sites, even spacing.** Write \(h=2^a u\) with \(a\ge1\) and \(u\) odd. For \(\nu_2(x)\le a-2\), the \(m\) factors agree, giving product one and Haar mass \(1-2^{1-a}\). For \(\nu_2(x)=a-1\), successive factors alternate in sign, giving product \((-1)^{m/2}\) with Haar mass \(2^{-a}\). For \(\nu_2(x)\ge a\), dividing all arguments by \(2^a\) gives an even-length progression of odd spacing \(u\) with shifted fold instructions; this has mean zero by the preceding paragraph and mass \(2^{-a}\). Adding yields the formula.

**Four-site correlations and sharp diameter.** Apply the exact cylinder formula to \((0,1,2,8)\), using \(K=6\): its polynomial is exactly \(\varepsilon_0\varepsilon_1/8\). For \(k\ge1\), split \(x\) into \(\nu_2(x)\le k-2\), \(\nu_2(x)=k-1\), and \(\nu_2(x)\ge k\). The first two contributions are respectively \(1-2^{1-k}\) and \(-2^{-k}\); the last is \(2^{-k}B_{0,\sigma^k\varepsilon}\). This yields the stated \(B_k\) exactly. The exact cylinder formula also gives, for each of the \(\sum_{d=3}^7\binom{d-1}{2}=35\) normalized shapes \((0,a,b,d)\) with \(0<a<b<d<8\), a constant polynomial in the instruction signs. This is an exhaustive finite classification of every four-site shape with diameter less than eight; the supplied independently replayable exact-rational verifier reproduces each of the 35 certificates. Translation invariance completes the sharp cutoff. The adjacent products are recovered by rearranging the displayed \(B_k\) identities; fixing \(\varepsilon_0\) then recursively determines the entire instruction sequence, leaving only global sign.

## Verification
Run `python3 verify.py` using Python's standard library. The checker independently constructs finite dyadic cylinder polynomials with exact rational coefficients, tests 448 equally spaced parameter pairs, all 35 short-diameter four-site shapes, the diameter-eight witness, seven scaled witness identities, and 27 independently averaged finite prefix cases. Expected summary: `VERIFY_OK: 448 exact symbolic progression identities; 35 short-diameter four-point shapes; first distinguishing witness and 7 scaled witnesses; 27 independently averaged dyadic-prefix comparisons`. The unrestricted all-order formula follows from the Haar involutions and valuation partition; finite tests alone do not establish it.

## Relationship to prior work
Mendès France and van der Poorten (1981) give the standard generalized-paperfolding digit formula and analyze Fourier–Bohr coefficients and almost-periodic correlation/diffraction structure. The paper supplies the mathematical framework but does not explicitly evaluate the displayed complete arbitrary-order progression family or classify the shortest four-site instruction-identifying arrangement in the inspected full text. Van Enter and de Groote (2010) compute pairwise overlaps of paperfolding states; overlap of two configurations is not a single-word four-site shift correlation. Barbé and von Haeseler (2005) concern correlation and spectral structure of higher-dimensional paperfolding and Rudin–Shapiro sequences; only the abstract was available here, so exact higher-order coverage there remains a genuine historical-priority risk. The classical two-point special case of the progression formula is not asserted to be new.

## Limitations
Historical priority is not independently certified; general Fourier-expansion methods may already imply some formulas, and one plausible earlier full text remained inaccessible. This result concerns shift averages of sign products of a single paperfolding word, not all multi-sequence overlap observables. The uniqueness assertion is restricted to the specified family of four-site measurements and is exactly up to global sign, as forced by even-order observations. Self-review has been performed; no independent audit has been performed.

## References
- M. Mendès France and A. J. van der Poorten, *Arithmetic and analytic properties of paper folding sequences*, Bulletin of the Australian Mathematical Society 24 (1981), 123–131, doi:10.1017/S0004972700007486 (original paper, full text inspected).
- A. C. D. van Enter and E. de Groote, *An ultrametric state space with a dense discrete overlap distribution: Paperfolding sequences*, arXiv:1010.2338v1, first posted 2010-10-12 (full text inspected).
- A. Barbé and F. von Haeseler, *Correlation and spectral properties of higher-dimensional paperfolding and Rudin-Shapiro sequences*, Journal of Physics A 38 (2005), 2599–2622, doi:10.1088/0305-4470/38/12/005 (abstract inspected; full text unavailable).
