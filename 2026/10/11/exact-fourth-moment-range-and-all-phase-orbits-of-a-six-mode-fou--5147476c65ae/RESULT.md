# Exact fourth-moment range and all phase orbits of a six-mode Fourier rectangle

## Finding
Let \(\mathbb T=\{z\in\mathbb C:|z|=1\}\) carry Haar probability measure. For any six coefficients \(c_{ij}\in\mathbb C\) satisfying \(|c_{ij}|=1\), \(0\le i\le2\), \(0\le j\le1\), set
\[
P(z,w)=\sum_{i=0}^{2}\sum_{j=0}^{1}c_{ij}z^i w^j,
\qquad M(P)=\int_{\mathbb T^2}|P(z,w)|^4\,dm(z,w).
\]
The exact attainable range is
\[
\boxed{50\le M(P)\le114}.
\]
Both extrema are attained, and every intermediate real value occurs. The maximum occurs exactly for coefficient arrays \(c_{ij}=\lambda\alpha^i\beta^j\), with \(\lambda,\alpha,\beta\in\mathbb T\).

For the minimum, use the same three-parameter action \(c_{ij}\mapsto\lambda\alpha^i\beta^jc_{ij}\). There are **exactly three** orbits of minimizers. Their unique representatives satisfying \(c_{00}=c_{10}=c_{01}=1\) are the following two-row arrays; each displayed row is indexed by \(i=0,1,2\), with the first row \(j=0\):
\[
\begin{array}{c|cc}
 & (c_{00},c_{10},c_{20})&(c_{01},c_{11},c_{21})\\\hline
\mathrm{I}&(1,1,1)&(1,-1,1)\\
\mathrm{II}_{+}&(1,1,-1)&(1,i,1)\\
\mathrm{II}_{-}&(1,1,-1)&(1,-i,1)
\end{array}
\]
where \(i\) in the last two entries denotes the imaginary unit, not an array index.

Equivalently, the least aperiodic off-origin autocorrelation energy is \(14\), and the largest aperiodic merit factor \(36/14=18/7\). Among arrays whose entries are \(q\)-th roots of unity, the minimum \(50\) is attainable if and only if \(2\mid q\). Its exact number of attaining arrays is \(q^3\) if \(q\equiv2\pmod4\), and \(3q^3\) if \(4\mid q\). In particular, there are eight binary minimizers and 192 quaternary minimizers.

## Assumptions and scope
All six coefficients have modulus exactly one; coefficients of arbitrary magnitude are **not** covered. Fourier moments are normalized using Haar probability. The theorem also applies unchanged to an expression \(\gamma(g)\sum_{i=0}^2\sum_{j=0}^1 c_{ij}\chi(g)^i\eta(g)^j\) on a compact abelian group \(G\), provided that \(\chi^r\eta^s\) for \(0\le r\le4\), \(0\le s\le2\) are fifteen pairwise distinct characters. Here \(\gamma,\chi,\eta\) are continuous characters and Haar measure is normalized. In particular, uniform averaging on \(\mathbb Z_m\times\mathbb Z_n\) agrees with the torus moment whenever \(m\ge5\) and \(n\ge3\).

The root-of-unity counts concern coefficient arrays with their coordinates fixed, not orbits of geometric rotations or reflections.

## Proof
**Step 1: Normalize phases.** Writing \(P(z,w)=A(z)+wB(z)\), multiplication by a scalar and replacing \((z,w)\) by \((\alpha z,\beta w)\) preserve \(M(P)\). These operations uniquely normalize \(c_{00}=c_{10}=c_{01}=1\). There are therefore real numbers \(u,v,t\), understood modulo \(2\pi\), such that
\[
A(z)=1+z+e^{iv}z^2,\qquad B(z)=1+e^{iu}z+e^{it}z^2.
\]

**Step 2: Exact Fourier identity.** Integrating first over \(w\) yields
\[
M(P)=\int_{\mathbb T}\bigl(|A|^4+|B|^4+4|A|^2|B|^2\bigr)\,dm(z).
\]
The nonzero positive-lag autocorrelations of \(A\) are \(L_A=1+e^{iv}\) and \(K_A=e^{iv}\); those of \(B\) are \(L_B=e^{iu}+e^{i(t-u)}\) and \(K_B=e^{it}\). Parseval gives
\[
M(P)=58+2\bigl(|L_A|^2+|L_B|^2\bigr)
 +8\operatorname{Re}\bigl(L_A\overline{L_B}+e^{i(v-t)}\bigr).
\]
Introduce the real variables
\[
x=\cos(v/2),\quad y=\cos(u-t/2),\quad z_0=\cos((v-t)/2),
\]
all in \([-1,1]\). Since \(L_A=2xe^{iv/2}\) and \(L_B=2ye^{it/2}\), the exact identity becomes
\[
\begin{aligned}
M(P)-50
 &=8\bigl(x^2+y^2+4xyz_0+2z_0^2\bigr)\\
 &=8\Bigl(2(z_0+xy)^2+x^2(1-y^2)+y^2(1-x^2)\Bigr)\ge0.
\end{aligned}
\]
This sum of nonnegative terms is a global certificate, without discretization or numerical minimization.

**Step 3: All minimizing phases.** Equality in the last line forces \(z_0=-xy\), \(x^2(1-y^2)=0\), and \(y^2(1-x^2)=0\). Thus either \(x=y=z_0=0\), or \(|x|=|y|=1\) with \(z_0=-xy\). In the first case, the angle relations imply \(e^{iv}=-1\), \(e^{it}=1\), and \(e^{iu}=i\) or \(-i\), yielding the two \(\mathrm{II}\) representatives. In the second case they imply \(e^{iv}=e^{it}=1\) and \(e^{iu}=-1\), yielding representative \(\mathrm I\). Conversely all three substitutions make the displayed sum of squares vanish. The normalization fixes exactly three coefficients, so these are distinct and exhaustive modulation orbits.

**Step 4: Maximum and complete range.** For support \(S=\{0,1,2\}\times\{0,1\}\), write the aperiodic autocorrelation \(R(h)=\sum_{s,s-h\in S}c_s\overline{c_{s-h}}\). Orthogonality gives \(M(P)=\sum_h|R(h)|^2\). If \(N_h=|S\cap(S+h)|\), then \(|R(h)|\le N_h\), so
\[
M(P)\le\sum_hN_h^2
 =\bigl(3^2+2\cdot2^2+2\cdot1^2\bigr)
  \bigl(2^2+2\cdot1^2\bigr)=19\cdot6=114.
\]
At equality, all products for each shift align. For horizontal shift \((1,0)\), this forces all four neighboring horizontal ratios to be one common \(\alpha\); for vertical shift \((0,1)\), all three vertical ratios equal one \(\beta\). It follows that \(c_{ij}=\lambda\alpha^i\beta^j\). Such arrays indeed attain \(114\). The coefficient torus \(\mathbb T^6\) is connected and its moment map is continuous, so the entire interval between the attained endpoints is attained.

**Step 5: Phase alphabets and sampling.** Each of the three normalized minimizers contains either \(-1\) (type I) or \(\pm i\) (types II). Hence a \(q\)-phase minimizer exists precisely when \(q\) is even. Normalization by the first three unit entries determines each \(q\)-phase orbit element uniquely by a triple \((\lambda,\alpha,\beta)\) of \(q\)-th roots, giving \(q^3\) elements per admissible orbit. Type I exists for every even \(q\), and types II exactly when \(4\mid q\). Finally, for the general compact-group version, expand \(P^2\). Its Fourier support is contained in \(\{\chi^r\eta^s:0\le r\le4,\,0\le s\le2\}\); the stated fifteen-character separation allows Parseval term-by-term, recovering the identical convolution formula.

## Verification
Run `python3 checker.py` using the Python standard library. The checker independently evaluates the two-dimensional aperiodic autocorrelation energy for all \(2^6=64\) binary and \(4^6=4096\) quaternary arrays. Exact Gaussian-integer arithmetic gives binary energies \(50,58,66,114\) with multiplicities \(8,32,16,8\), and verifies 192 quaternary minimizers, 64 quaternary maximizers, and the three normalized minimum representatives. It also tests the polynomial square-completion equality with exact rational arithmetic and numerically compares aperiodic moments with finite Fourier averages on grids of sizes \((5,3)\), \((7,5)\), and \((11,7)\). These finite checks are supplementary to the preceding unrestricted proof.

## Relationship to prior work
Zhang, Fan, and Mesnager (2021) formulate two-dimensional aperiodic autocorrelation and construct **pairs** of arrays with vanishing *combined* autocorrelations inside prescribed zones. Das, Banerjee, and Parampalli (2023) instead construct **quads** and bound column peak-to-mean power ratios. Those results do not supply the sharp *single-array* full-aperiodic sidelobe energy or its complex equality orbits for the \(3\times2\) rectangle. Svalbe and Tirkel (2017) investigate large two-dimensional perfect-array families with chiefly periodic correlation and cross-correlation objectives, rather than this six-cell continuous-phase extremal problem. Related four-frequency and triangular-six-frequency fourth-moment calculations concern different supports; the present three-orbit classification does not follow simply by restricting their statements.

## Limitations
This result concerns exactly six unimodular coefficients on the full rectangular support, not arbitrary amplitude weights, arbitrary array shapes or larger rectangles. The finite-character version requires the explicit no-alias condition. A literature search and inspection of closely related papers cannot rule out an older equivalent calculation under aperiodic merit-factor or array-correlation terminology, including unpublished engineering tables. No independent mathematical audit is claimed.

## References
1. H. Zhang, C. Fan, S. Mesnager, *New constructions of q-Ary 2-D Z-Complementary Array Pairs*, arXiv:2107.11599v1 (first submitted 2021-07-24), https://arxiv.org/html/2107.11599v1 .
2. S. Das, A. Banerjee, U. Parampalli, *Two-Dimensional Z-Complementary Array Quads with Low Column Sequence PMEPRs*, arXiv:2308.06690v1 (first submitted 2023-08-13), https://arxiv.org/html/2308.06690v1 .
3. I. D. Svalbe, A. Z. Tirkel, *Extended families of 2D arrays with near optimal auto and low cross-correlation*, EURASIP Journal on Advances in Signal Processing 2017, article 18, https://doi.org/10.1186/s13634-017-0455-2 .
