# A sharp complementary-channel absorption bound for two separated dissipative sheets

## Finding
At a prescribed frequency, a pair of strictly absorbing point sheets with variable positive strengths has an exact coherent-perfect-absorption (CPA) budget transition. Among **all** parameter choices that have a perfectly absorbed nonzero two-sided illumination, the largest possible minimum absorbed fraction over **all** normalized coherent two-sided illuminations is precisely \(1/2\). This bound is sharp and has just two ordered realizations, interchanged by reversing the sheets.

Precisely, put \(L=a+b\), where \(a,b>0\) are dimensionless losses, and \(\theta=kd\), where \(k,d>0\) are wavenumber and sheet separation. A CPA exists if and only if either:

1. \(L=1\), \(0<a,b<1\), and \(\theta\in\pi\mathbb Z\); or
2. \(L>1\), \(\theta\in\pi(\mathbb Z+1/2)\), and
\[
\{a,b\}=\left\{\frac{L+\sqrt{(L-1)^2+1}}2,\frac{L-\sqrt{(L-1)^2+1}}2\right\}.
\]

There is no CPA for \(L<1\). For a CPA design, define the worst-input absorbed fraction by
\[
\mathcal A_{\mathrm{worst}}=\min_{v\in\mathbb C^2,\,\|v\|_2=1}\bigl(1-\|Sv\|_2^2\bigr)=1-\|S\|_2^2,
\]
where \(S\) is the flux-normalized two-port scattering matrix. Its *complete* CPA-branch law is
\[
\mathcal A_{\mathrm{worst}}=
\begin{cases}
0,& L=1,\\
\dfrac{2(L-1)}{L^2},&L>1.
\end{cases}
\]
Thus \(\mathcal A_{\mathrm{worst}}\le 1/2\), with equality if and only if \(L=2\), \(\theta\in\pi(\mathbb Z+1/2)\), and \(\{a,b\}=\{1+1/\sqrt2,1-1/\sqrt2\}\).

At any overcritical CPA (\(L>1\)), the required incoming powers from right and left have ratio \(|2a-1|^2\) (in the left-to-right transfer convention below). Exchanging sheets inverts this ratio. In particular, a CPA design optimized for the least-favorable illumination has unequal sheets and unequal incident powers.

## Assumptions and scope
Consider the scalar one-dimensional, stationary equation
\[
-u''(x)-2ik\bigl[a\,\delta(x)+b\,\delta(x-d)\bigr]u(x)=k^2u(x),
\qquad k,d,a,b>0.
\]
Its distributional matching conditions are continuity of \(u\) and jumps \(u'(0^+)-u'(0^-)=-2ika u(0)\), \(u'(d^+)-u'(d^-)=-2ikb u(d)\). The exterior medium is the same on both sides, so equal-amplitude incoming waves carry equal incident flux. The physical sheet strengths are \(2ka\) and \(2kb\); the dimensionless total loss \(L=a+b\) is the design resource at **fixed** \(k\). All results refer to monochromatic stationary scattering with freely selectable incident complex amplitudes and separation. No endpoint or reflector is present. The two absorbers must both have strictly positive strength; zero-strength limits are excluded.

## Proof
Write left and right exterior waves as \(u=A_L e^{ikx}+B_L e^{-ikx}\) and \(u=A_R e^{ik(x-d)}+B_R e^{-ik(x-d)}\), respectively, and let \(P=\mathrm{diag}(e^{i\theta},e^{-i\theta})\) transport amplitudes through the gap. The point-interaction matrix is
\[
U(c)=\begin{pmatrix}1-c&-c\\c&1+c\end{pmatrix}.
\]
Hence \(\binom{A_R}{B_R}=M\binom{A_L}{B_L}\), where \(M=U(b)P U(a)\), \(\det M=1\), and
\[
M_{11}=(1-a)(1-b)e^{i\theta}-ab e^{-i\theta},\qquad
M_{22}=(1+a)(1+b)e^{-i\theta}-ab e^{i\theta}.
\]
In particular \(|M_{22}|\ge1+a+b>0\). The scattering matrix that maps incoming \((A_L,B_R)\) to outgoing \((B_L,A_R)\) is
\[
S=\frac1{M_{22}}\begin{pmatrix}-M_{21}&1\\1&M_{12}\end{pmatrix},
\qquad \det S=-\frac{M_{11}}{M_{22}}.
\]
Thus CPA (a nonzero input in \(\ker S\)) holds exactly when \(M_{11}=0\), equivalent to
\[
e^{2i\theta}(1-a)(1-b)=ab.
\]
Since the right side is strictly positive, either \(e^{2i\theta}=1\) and \((1-a)(1-b)=ab\), giving \(L=1\), or \(e^{2i\theta}=-1\) and \((1-a)(1-b)=-ab\), giving \(L-2ab=1\). There is no solution with \(a=1\) or \(b=1\). In the second case \(ab=(L-1)/2>0\) forces \(L>1\) and yields the two indicated positive roots of \(z^2-Lz+(L-1)/2=0\). This proves the complete CPA classification including all boundaries.

At a CPA, \(M_{12}M_{21}=-1\) by \(\det M=1\), and the rank-one matrix \(S\) has singular values \(0\) and
\[
\sigma_{\mathrm{bright}}=\frac{|M_{21}|+|M_{21}|^{-1}}{|M_{22}|}.
\]
On the \(L=1\) branch, \(|M_{21}|=1\) and \(|M_{22}|=2\), whence \(\sigma_{\mathrm{bright}}=1\). On the \(L>1\) branch, \(|M_{22}|=2L\) and \(|M_{21}|=|2a-1|\). If \(q=L-1\), set \(h=\sqrt{q^2+1}\); the two choices for \(|2a-1|\) are \(h+q\) and \(h-q=1/(h+q)\). Consequently \(\sigma_{\mathrm{bright}}=h/L\), and
\[
1-\sigma_{\mathrm{bright}}^2=\frac{2(L-1)}{L^2}.
\]
Differentiating yields \(d[2(L-1)/L^2]/dL=-2(L-2)/L^3\), positive below \(2\) and negative above \(2\) throughout \(L>1\). The unique maximizing budget is \(L=2\), and its ordered sheets and phases follow from the classification. Finally, for perfect absorption \((B_L,A_R)=(0,0)\), so \(B_R=M_{21}A_L\), proving the incident power ratio statement. For arbitrary input \(v\), absorbed fraction is \(1-\|Sv\|_2^2/\|v\|_2^2\); its minimum is determined by the largest singular value as claimed.

## Verification
Execute \(\texttt{python3 verify_cpa.py}\) using Python 3 standard-library modules only. The standalone checker multiplies independent \(2\times2\) transfer matrices rather than reusing the closed-form scattering entries. It tests the exact CPA branches, their zero singular values, the bright-channel formula and sharp bound; it also samples non-CPA parameters to verify reciprocity, scattering contractivity and the transfer/scattering determinant identity. The checker reports 4,743 successful scalar/matrix assertions. The exhaustive claims for all real positive parameters and all input vectors follow from the preceding algebra, not from sampling.

## Relationship to prior work
Chong, Ge, Cao and Stone (2010) establish the general two-port CPA scattering-zero condition and analyze a uniform lossy slab. The present result applies that framework to **two distinct positive delta absorbers**, completely classifies the separated-sheet CPA loci at a fixed total loss, and optimizes the absorption guaranteed to the input *orthogonal* to the perfectly absorbed channel. Li and coauthors (2014) derive coherent perfect absorption for **one** ultrathin conductive sheet. Luo and coauthors (2014) study single thin absorbers with reflectors (and a symmetric, co-located double-layer equivalent); they do not impose two separated freely optimized point losses. Martínez-Argüello and colleagues (2012) analyze a single lossy delta potential facing a hard wall, a one-port geometry. Roger and colleagues (2015) experimentally treat a single subwavelength absorber with quantum illumination. These are physically and mathematically related, but their stated results do not give the two-positive-sheet sharp minimax \(1/2\) law. This comparison is not a claim of a complete historical priority search; see the limits below.

## Limitations
The optimum \(1/2\) is **conditional on exact CPA**; no claim is made that it is optimal among devices without CPA. The point sheets are zero-width scalar imaginary potentials, without dispersive, nonlinear or finite-thickness electromagnetic effects. The frequencies and sheet strengths are linked through the fixed-\(k\) normalization; no broadband assertion follows. The two-port singular-value metric assumes unrestricted coherent inputs of fixed total incident flux. Wider multilayer and impedance-matching literature may contain equivalent special cases not identified in the inspected papers. Numerical checks do not independently certify the infinite statements.

## References
1. Y. D. Chong, L. Ge, H. Cao, A. D. Stone, *Coherent Perfect Absorbers: Time-reversed Lasers*, arXiv:1003.4968v1 (first posted 2010-03-25), especially the general two-port transfer discussion.
2. A. M. Martínez-Argüello, R. A. Méndez-Sánchez, M. Martínez-Mares, *Wave systems with direct processes and localized losses or gains: the non-unitary Poisson kernel*, arXiv:1207.2716v1 (2012-07-11), Section III.
3. J. Luo, S. Li, B. Hou, Y. Lai, *A unified theory for perfect absorption in ultra-thin absorptive films with constant tangential electric or magnetic fields*, arXiv:1405.6475 (2014-05-26), Sections II–III.
4. S. Li et al., *Broadband perfect absorption of ultrathin conductive films with coherent illumination*, arXiv:1406.1847v1 (2014-06-07), Sections 1–2.
5. T. Roger et al., *Coherent perfect absorption in deeply subwavelength films in the single-photon regime*, Nat. Commun. 6, 7031 (2015), doi:10.1038/ncomms8031.
