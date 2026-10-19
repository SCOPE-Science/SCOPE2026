# A sharp first STFT support gap and the two six-point strata on the four-cycle

## Finding
For every pair of nonzero complex signals \(f,g:\mathbb Z_4\to\mathbb C\), put \(s(f,g)=|\operatorname{supp}V_gf|\). Then
\[
\boxed{s(f,g)=4\quad\text{or}\quad s(f,g)\ge6.}
\]
Both alternatives occur, so six is the **sharp first support cardinality strictly above the uncertainty minimum**. More precisely, \(s(f,g)=6\) holds exactly for the following two, disjoint, families.

**Sparse family.** There exist \(u,v\in\mathbb Z_4\) with
\(\operatorname{supp}f=\{u,u+2\}\) and \(\operatorname{supp}g=\{v,v+2\}\). Write \(f(u)=a\), \(f(u+2)=b\), \(g(v)=c\), \(g(v+2)=d\), all nonzero. Exactly one of
\[
a\overline c=\pm b\overline d,
\qquad a\overline d=\pm b\overline c
\]
may hold (the signs may depend on the comparison). The two statements are evaluated as Boolean conditions; precisely one is required.

**Nowhere-zero family.** Both functions are nonzero at all four coordinates. For some \(k_0\in\mathbb Z_4\), translate the window to \(G(j)=g(j-k_0)\). There exist \(u,v,A\in\mathbb C^\times\), \(\varepsilon\in\{+1,-1\}\), \(r\in\{0,1\}\), and \(a\in\mathbb Z_4\) such that
\[
G=(u,v,\varepsilon u,\varepsilon(-1)^r v),\qquad
f(j)=\frac{A i^{aj}}{\overline{G(j)}}\quad(j\in\mathbb Z_4),
\qquad \boxed{(v/u)^4\ne(-1)^r}.
\]
In this family the four frequency-row support counts are \((1,2,1,2)\) after the time translation; when the boxed inequality is replaced by equality, the counts become \((1,1,1,1)\) and hence \(s=4\).

For example, \(f=g=(1,0,2,0)\) belongs to the sparse family, whereas \(f=g=(1,1,1,-1)\) belongs to the nowhere-zero family. Each has exactly six nonzero STFT coefficients.

## Assumptions and scope
All indices are residues modulo four, and every input coefficient is allowed to be any complex number. The window and signal are independently arbitrary and nonzero. We use the convention
\[
V_gf(k,\ell)=\frac12\sum_{j=0}^3 f(j)\overline{g(j-k)}i^{-j\ell},
\qquad (k,\ell)\in\mathbb Z_4^2.
\]
The factor one-half does not affect support. The claim concerns the **exact** zero/nonzero pattern, not near-zeros or numerically thresholded coefficients. A row with exactly one Fourier coefficient is a nonzero scalar times one of the four characters \(j\mapsto i^{aj}\), by inverse Fourier transform.

## Proof
**1. Small-support inputs.** Put \(F=\operatorname{supp}f\), \(H=\operatorname{supp}g\) and \(h_k(j)=f(j)\overline{g(j-k)}\). Its time support is \(F\cap(k+H)\), and the frequency row of \(V_gf\) is exactly one-half its Fourier transform. For any nonzero \(h\) on \(\mathbb Z_4\), if \(|\operatorname{supp}h|=1\), all four Fourier coefficients are nonzero; if its support has size two or three, at least two Fourier coefficients are nonzero. This last assertion follows because a one-frequency inverse transform is a character, which has support four. In addition, when the time support is an opposite pair \(\{j,j+2\}\), its Fourier transform has two nonzero frequencies exactly if its two values agree up to sign, and otherwise four.

If \(|F|=1\) or \(|H|=1\), each occupied shift contributes four nonzero frequencies, and the total is four times the size of the other support. If \(|F|,|H|\in\{2,3\}\) except for a pair of opposite-pair supports, the total is at least eight. Indeed, for two adjacent two-point supports, precisely three shifts are occupied: two singleton intersections and one two-point intersection, contributing at least \(4+4+2=10\); if exactly one support is an opposite pair, all four intersections are singletons and the total is sixteen. Any two/three-point-support combination, or two three-point supports, has all four shifts occupied and each intersection is nonempty, and either every row has Fourier support at least two or singleton rows contribute four. A full-support input paired with a two- or three-point support likewise has four occupied shifts, each contributing at least two frequencies. Therefore the only cases with fewer than eight STFT coefficients outside full/full supports are singleton/singleton (four) and two opposite-pair supports (four, six, or eight).

For the two opposite-pair supports, precisely two shifts are occupied. At shift \(u-v\) the two values of \(h_k\) are \(a\overline c,b\overline d\), and at shift \(u-v+2\) they are \(a\overline d,b\overline c\). Each row has two Fourier coefficients if and only if its two values agree up to sign, otherwise four. Thus the sum is exactly six if and only if precisely one of the two stated comparisons holds. This proves the sparse branch.

**2. Full/full supports and the five-point exclusion.** Assume henceforth all eight input coordinates are nonzero. All four \(h_k\) are nowhere zero, so their Fourier-support cardinalities \(t_k\) lie in \(\{1,2,3,4\}\). Suppose any two consecutive time rows \(k,k+1\) each have support one. Then \(h_k(j)\) and \(h_{k+1}(j)\) are scalar characters. Dividing them shows that \(\overline{g(j-k-1)}/\overline{g(j-k)}\) is a scalar character in \(j\). Translating and taking products of this identity shows, for every shift \(d\), that \(\overline{g(j-k-d)}/\overline{g(j-k)}\) is a scalar character. Consequently every \(h_{k+d}\) is a scalar character and all \(t_j=1\). Thus two adjacent pure Fourier rows force \(s=4\).

If \(s\le5\), because there are four nonempty rows, at least three of the four are pure whenever \(s=5\). Among three residues modulo four there must be two adjacent ones. Their purity forces all four pure, contradicting \(s=5\). Thus support five is impossible. If \(s=6\), there must be at least two pure rows. They cannot be adjacent, so they occur at opposite shifts, while the other two have support counts two apiece.

**3. Exact reconstruction from two opposite pure rows.** Relabel shifts to take the pure rows as zero and two, and denote the translated window by \(G\). Because the zero row is pure, for some \(A\ne0\) and \(a\in\mathbb Z_4\),
\[
f(j)\overline{G(j)}=A i^{aj},
\qquad f(j)=\frac{A i^{aj}}{\overline{G(j)}}.
\]
The second pure row forces the ratio \(\overline{G(j-2)}/\overline{G(j)}\) to be \(C i^{dj}\) for some \(C\ne0\), \(d\in\mathbb Z_4\). Since translating by two twice is the identity, evaluating the product of this ratio at \(j\) and \(j+2\) yields
\[
C^2(-1)^{d(j+1)}=1\qquad(j\in\mathbb Z_4).
\]
Comparing \(j=0\) and \(j=1\) gives \(d\) even, and then \(C\in\{\pm1\}\). Write \(d=2r\) and \(C=\varepsilon\). These ratio conditions are exactly
\[
G=(u,v,\varepsilon u,\varepsilon(-1)^r v),
\quad u,v\ne0,\quad r\in\{0,1\}.
\]
For \(k=1\), the quotient \(\overline{G(j-1)}/\overline{G(j)}\) obeys \(R(j+2)=(-1)^rR(j)\), so it lies in the span of exactly two characters (or just one if the two-term coefficient degenerates). In fact it is itself a character exactly when \(R(1)/R(0)\) is a fourth root of unity with its square \((-1)^r\). From the displayed four coordinates,
\[
R(0)=\varepsilon(-1)^r\overline v/\overline u,
\quad R(1)=\overline u/\overline v,
\]
and the pure-character condition reduces precisely to \((v/u)^4=(-1)^r\). Multiplying by the pure character \(A i^{aj}\) does not change the number of Fourier frequencies.

Finally the quotient for shift three is the product of the quotient for shift one and the shift-two quotient translated by one. Because the latter is a character, row three has exactly the same Fourier-support cardinality as row one. Consequently if \((v/u)^4=(-1)^r\), all four rows are pure and \(s=4\); otherwise their Fourier-support counts are \((1,2,1,2)\) and \(s=6\). This also proves sufficiency for the entire full-support family and exhausts every possibility for six nonzero coefficients.

## Verification
`verify_z4.py` independently implements the four Fourier rows using Gaussian integer arithmetic, with roots \(1,i,-1,-i\). It exhausts every pair of nonzero four-coordinate signals whose entries lie in \(\{0,1,2,-1\}\): exactly \(255^2=65{,}025\) signal/window pairs. The output reports no support of size five, support-six counts 64 sparse and 80 full, and matches the structural classification for every enumerated pair. The script also tests a witness for each family. The finite sample is **not** used as proof for arbitrary complex coefficients: the preceding algebraic case analysis supplies that proof. The recorded output is included in `verification_output.txt`.

## Relationship to prior work
Nicola's 2022 paper proves the exact universal support lower bound and describes **equality at four**, including the metaplectic form of extremizers, but does not give the first nonminimal cardinality or classify **six-point** signal/window pairs. Krahmer, Pfander and Rashkov (2008) prove support constraints and present numerical diagrams for fixed generic windows; their order-four diagram does not classify exceptional arbitrary windows or the full six-point fibers. Previously described fixed equal two-point-window support formulas and odd-prime second-gap results are related but do not imply this all-window four-cycle classification. The present result supplements those theorems, not their general-order equality classification.

## Limitations
Only the first nonminimal support value on \(\mathbb Z_4\) and its complete pair classification are established. No assertion concerns other cyclic orders, all attainable support cardinalities, approximate concentration, stability, or optimally sparse windows. The novelty comparison includes primary full texts and nearby specialized records, but an unindexed earlier equivalent finite classification cannot be excluded. The algebraic proof is self-contained; numerical replay tests only a finite coefficient alphabet.

## References
1. F. Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality*, arXiv:2204.14176v1 (first public 2022-04-29); *Journal of Functional Analysis* 284 (2023), 109924. https://arxiv.org/html/2204.14176v1.
2. F. Krahmer, G. E. Pfander and P. Rashkov, *Uncertainty in time–frequency representations on finite Abelian groups and applications*, arXiv:math/0611493, *Applied and Computational Harmonic Analysis* 25 (2008), 209–225. https://www.mathematik.uni-marburg.de/~pfander/pubs/uncertaintytimefrequency.pdf.
3. *Exact support geometry for a two-point cyclic short-time Fourier window*, published mathematical note, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-support-geometry-for-a-two-point-cyclic-short-time-fourier--f7682ff5d741.
4. *A sharp support gap above the odd-prime short-time Fourier uncertainty minimum*, published mathematical note, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-support-gap-above-the-odd-prime-short-time-fourier-uncer--c42ba46f36bb.
