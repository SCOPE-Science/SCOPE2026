# Sharp fourth Fourier moment and phase rigidity of the five-frequency cross

## Finding
Let \(S=\{(0,0),(1,0),(-1,0),(0,1),(0,-1)\}\). On the probability two-torus \(\mathbb T^2\), or on \((\mathbb Z/N\mathbb Z)^2\) with uniform probability measure for any integer \(N\ge5\), consider
\[
P(z,w)=c+a_+z+a_-z^{-1}+b_+w+b_-w^{-1},
\quad M=|c|^2+|a_+|^2+|a_-|^2+|b_+|^2+|b_-|^2.
\]
On the finite grid, \(z,w\) range independently over the \(N\)-th roots of unity; on the continuous torus they are independent unit-modulus complex variables. Put
\[
W=|c|^2,\qquad U=|a_+|^2+|a_-|^2,\qquad V=|b_+|^2+|b_-|^2.
\]
Then the following quantitative **sharp fourth-moment inequality** holds for all five complex coefficients:
\[
\boxed{\frac{27}{11}M^2-\mathbb E|P|^4\;\ge\;\frac{11}{4}\left(W-\frac{3M}{11}\right)^2+\frac34(U-V)^2\;\ge0.}
\tag{1}
\]
In particular, the exact \(\ell^2\)-to-\(L^4\) synthesis norm to the fourth power is \(27/11\). Every nonzero equality case in the sharp norm inequality, and no others, is
\[
\boxed{(c,a_+,a_-,b_+,b_-)=\lambda\left(\sqrt{3/2},\eta,\eta^{-1},\xi,\xi^{-1}\right),\quad\lambda\in\mathbb C\setminus\{0\},\quad |\eta|=|\xi|=1.}
\tag{2}
\]
Thus the complete projective extremizer space is a two-dimensional phase torus. The central squared amplitude carries exactly \(3/11\) of the total mass, while each arm carries \(2/11\). The correction terms in (1) also quantify mandatory mass concentration and balance for near-extremizers. **The quantitative remainder is exact at every prescribed nonnegative mass triple:** given any \(W,U,V\ge0\), choosing real coefficients \(c=\sqrt W\), \(a_+=a_-=\sqrt{U/2}\), and \(b_+=b_-=\sqrt{V/2}\) makes the first inequality in (1) an equality. The numerical constant and all equality cases remain identical on every finite grid of order at least five.

## Assumptions and scope
The coefficients are arbitrary complex numbers, possibly zero. \(\mathbb E\) is normalized Haar integration on \(\mathbb T^2\) or normalized averaging over all \(N^2\) grid points. The five characters of \(S\) and the differences in \(S-S\) have precisely their integer-lattice coincidence structure for \(N\ge5\); no other frequency aliases arise. The \(N\ge5\) threshold is essential to the proof, and no equality classification for smaller grids is asserted. Multiplying \(P\) by any fixed character leaves both its fourth moment and coefficient mass unchanged, but the theorem uses the displayed symmetric five-point frequency set.

## Proof
**Autocorrelation orthogonality.** Denote the five coefficients by \(f_s\), where \(s\in S\). For any difference \(h\in S-S\) let
\[
R(h)=\sum_{s,t\in S\, :\, s-t=h}f_s\overline{f_t}.
\]
Fourier orthogonality gives
\[
\mathbb E|P|^4=\sum_{h\in S-S}|R(h)|^2.\tag{3}
\]
This holds on the torus and on every finite grid \(N\ge5\), since distinct integer differences in the range \([-2,2]^2\) do not collide modulo \(N\). In (3), \(R(0)=M\). The remaining differences comprise the pairs \(\pm e_1,\pm e_2,\pm2e_1,\pm2e_2\), and four diagonals \(\pm e_1\pm e_2\).

**Exact majorization.** Write \(u=|a_+|\), \(v=|a_-|\), \(s=|b_+|\), \(t=|b_-|\), \(p=uv\), \(q=st\), and \(W=|c|^2\). Then \(U=u^2+v^2\), \(V=s^2+t^2\), \(0\le2p\le U\), and \(0\le2q\le V\). For the four fundamental differences, the triangle inequalities yield
\[
|R(e_1)|\le |c|(u+v),\qquad |R(e_2)|\le|c|(s+t).
\]
The two doubled differences contribute \(2p^2+2q^2\). The diagonal differences have pairs of terms and contribute no more than
\[
2(ut+sv)^2+2(us+tv)^2=2UV+8pq.
\]
Summing this exhaustive list, including the opposite differences, proves
\[
\mathbb E|P|^4\le M^2+2W(U+V)+4W(p+q)+2p^2+2q^2+2UV+8pq.\tag{4}
\]
Every coefficient in (4) multiplying \(p\) or \(q\) is nonnegative. Substituting \(p\le U/2\) and \(q\le V/2\), and collecting terms, gives
\[
\mathbb E|P|^4\le M^2+4W(U+V)+\frac12(U^2+V^2)+4UV.\tag{5}
\]
Set \(T=U+V=M-W\). Since \(UV=(T^2-(U-V)^2)/4\), equation (5) becomes
\[
\mathbb E|P|^4\le M^2+4W(M-W)+\frac54(M-W)^2-\frac34(U-V)^2.
\]
The first three terms complete to a square **exactly**:
\[
M^2+4W(M-W)+\frac54(M-W)^2
=\frac{27}{11}M^2-\frac{11}{4}\left(W-\frac{3M}{11}\right)^2.
\]
This proves the quantitative inequality (1) for arbitrary coefficients, including zero coefficients and \(M=0\). For each fixed admissible \(W,U,V\), the real nonnegative coefficients \(c=\sqrt W\), \(a_+=a_-=\sqrt{U/2}\), and \(b_+=b_-=\sqrt{V/2}\) saturate every triangle and pair-product inequality. Thus the two-square remainder in (1) is not just a lower bound, but the exact optimal deficit after coarse-graining coefficients to their three masses.

**All equality cases.** If \(P\ne0\) saturates the sharp moment inequality, (1) first forces \(W=3M/11>0\) and \(U=V=4M/11>0\). Since the right side of (4) is strictly increasing in \(p\) and \(q\) when \(W>0\), equality in (5) further requires \(p=U/2\), \(q=V/2\), that is, \(u=v=s=t=\sqrt{2M/11}>0\). Equality in \(|R(e_1)|\le|c|(u+v)\) forces
\[
\arg a_++\arg a_-\equiv2\arg c\pmod{2\pi},
\]
and equality in the analogous vertical bound forces \(\arg b_++\arg b_-\equiv2\arg c\pmod{2\pi}\). Conversely, those two antipodal phase identities also align both terms in each diagonal correlation, and therefore make every inequality (3)--(5) an equality. Dividing out a common nonzero complex scalar gives precisely the two phases \(\eta\) and \(\xi\) in (2). Substitution gives \(M=11|\lambda|^2/2\), \(\mathbb E|P|^4=(27/11)M^2\), proving both sharpness and completeness.

## Verification
The standalone Python program `artifacts/verify.py` implements the difference-autocorrelation identity without external source files, checks the exact rational mass balance, independently averages the fourth powers over grids of orders \(5,6,7,8,9,11\), tests \(240\) random complex coefficient vectors, reproduces \(72\) phase-modulated maximizers, checks \(100\) prescribed mass triples for exact deficit saturation, and exhausts all nonzero \(\{-1,0,1\}^5\) coefficient vectors on three grids. Its precise output is included as `artifacts/verification_output.txt`. SymPy is optional and was available for the exact square-completion check. The analytic proof above, not finite numerical testing, proves (1)--(2) for every \(N\ge5\) and for the continuous torus.

## Relationship to prior work
Iosevich--Koh--Lee--Pham--Shen (2018) develop finite-field Fourier-extension estimates for zero- and nonzero-radius spheres (chiefly in higher dimensions); their main theorems do not state the exact five-character cross norm or its all-complex equality family. Ciccone--Gonçalves (2022) prove a sharp \(L^6(\mathbb R^2)\) circle-extension theorem under arithmetic spectral hypotheses; that is neither the \(L^4\) two-torus character synthesis problem nor its five-point frequency collision geometry. González-Riquelme--Oliveira e Silva (2024) establish sharp Fourier extension on finite-field parabolae and related quadratic varieties, not the stated nonaliased cross theorem.

More directly, the published *Sharp fourth moments for a five-point Ferrers Fourier spectrum* studies a different five-frequency set, with a row-midpoint collision and two linked diagonal collisions rather than the symmetric four-arm cross; its constant is \(2.646915\ldots\), versus \(27/11\) here. The published *Sharp fourth-moment extension and nine phase-rigid optimizers on the ternary split cone* treats exactly the five-point cross **over \(\mathbb F_3^2\)**, where low-order aliases change the convolution and yield a different sharp constant and discrete optimizer classes; it cannot imply the no-alias result here. *Sharp fourth-moment extension and one-axis rigidity for finite abelian crosses* treats a substantially larger support, the entire pair of intersecting subgroups, with equality on a whole axis; its norm is not sharp on the five-point subset and its equality cases do not give (2). These comparisons involve mathematical claims and their different assumptions, not merely title matching.

## Limitations
The theorem does not treat finite grid orders \(2,3,4\), arbitrary nonsymmetric five-point frequency sets, all fourth moments of sparse functions, or other exponents. Near-extremizer control in (1) concerns the center mass and imbalance between axes; it alone does not quantify every individual amplitude and phase deviation. The originality assessment is best-knowledge: an older equivalent extremal-polynomial computation may remain unindexed. No independent scientific audit has been performed.

## References
1. A. Iosevich, D. Koh, S. Lee, T. Pham, and C.-Y. Shen, *On restriction estimates for the zero radius sphere over finite fields*, arXiv:1806.11387v1, first public 2018-06-29; https://arxiv.org/abs/1806.11387.
2. V. Ciccone and F. Gonçalves, *Sharp Fourier Extension on the Circle Under Arithmetic Constraints*, arXiv:2208.09441v1, first public 2022-08-19; https://arxiv.org/abs/2208.09441.
3. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1, first public 2024-05-26; https://arxiv.org/abs/2405.16647.
4. *Sharp fourth moments for a five-point Ferrers Fourier spectrum*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moments-for-a-five-point-ferrers-fourier-spectrum--bb5fd3f72396.
5. *Sharp fourth-moment extension and nine phase-rigid optimizers on the ternary split cone*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-extension-and-nine-phase-rigid-optimizers-on--d65b0e8eea36.
6. *Sharp fourth-moment extension and one-axis rigidity for finite abelian crosses*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-extension-and-one-axis-rigidity-for-finite-a--5b31463115dc.
