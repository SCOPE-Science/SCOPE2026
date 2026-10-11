# Sharp fourth moments for linked-midpoint four-character spectra

## Finding
Let \(G\) be a compact abelian group with normalized Haar probability measure \(\mu\). Let \(\gamma\) and \(\chi\) be continuous characters of \(G\), with \(\chi\) of order at least \(9\) or infinite order. Define
\[
F(g)=\gamma(g)\bigl(c_0+c_1\chi(g)+c_2\chi(g)^2+c_4\chi(g)^4\bigr).
\]
Then for every \((c_0,c_1,c_2,c_4)\in\mathbb C^4\),
\[
\int_G|F(g)|^4\,d\mu(g)
\le \mathcal K\bigl(|c_0|^2+|c_1|^2+|c_2|^2+|c_4|^2\bigr)^2,
\qquad \mathcal K=2.299413862840329\ldots.
\]
Here is an exact algebraic specification of the constant and all equality cases. Let \(t\) be the unique real root in \((11287/10000,11288/10000)\) of
\[
8t^9+11t^8-10t^7-27t^6-14t^5+27t^4+19t^3-8t^2-7t-1=0.
\]
Set
\[
v=\frac{(t-1)(t^2+3t+1)}{t(2-t)},\quad
\lambda=\frac{t^2}{v}-v^2,\quad
B=2t-\lambda,\quad
T=1+B+t^2+v^2,\quad
\mathcal K=2+\frac{\lambda}{T}.
\]
These definitions give \(1.1287<t<1.1288\), \(0.740<v<0.742\), and \(B>1\).
**Every nonzero equality case** is exactly
\[
(c_0,c_1,c_2,c_4)=s\bigl(1,\sqrt B\,e^{i\vartheta},t e^{2i\vartheta},v e^{4i\vartheta}\bigr),
\qquad s\in\mathbb C\setminus\{0\},\quad\vartheta\in\mathbb R.
\]
The stable-order hypothesis is sharp: for each character order \(5\), \(6\), \(7\), or \(8\), four distinct frequencies remain, but the inequality with \(\mathcal K\) fails. No statement is made for the aliased supports at character orders at most \(4\).

## Assumptions and scope
No connectedness, finiteness, or torsion-freeness assumption is imposed on \(G\). The characters \(\gamma\) and \(\chi\) may be dependent; multiplication by \(\gamma\) has modulus one and is irrelevant to the fourth moment. Order at least nine makes all exponent sums from \(\{0,1,2,4\}+\{0,1,2,4\}\), which lie between zero and eight, distinct modulo the character order. In the infinite-order case the same orthogonality holds.

All four coefficients may have arbitrary complex magnitude and phase, including zero. The upper bound is homogeneous; its nonzero equality cases have all four magnitudes strictly positive. The measure is normalized and no Fourier normalization factors are hidden.

The object is the sparse four-mode Fourier subspace with *two linked midpoint collisions*: \(0+2=1+1\) and \(0+4=2+2\). Both collisions share the lowest frequency and one endpoint participates in the other relation; this differs from a four-term arithmetic progression, which has a different collision diagram. Computing a sharp norm and its equality geometry therefore probes how overlapping additive relations affect Fourier amplification.

## Proof
Write \(a=|c_0|\), \(b=|c_1|\), \(c=|c_2|\), \(d=|c_4|\), and \(E=a^2+b^2+c^2+d^2\). Orthogonality of distinct characters gives the exact fourth-moment convolution identity
\[
\int_G|F|^4\,d\mu
=\sum_{k=0}^8\left|\sum_{\substack{j,\ell\in\{0,1,2,4\}\\j+\ell=k}}c_jc_\ell\right|^2.
\]
The only nonsingleton collisions beyond symmetric interchange are the two midpoint relations. Triangle inequality in those fibers yields
\[
\int_G|F|^4\,d\mu
\le 2E^2-(a^4+b^4+c^4+d^4)+4acb^2+4adc^2.\tag{1}
\]
For positive \(t,v\), the elementary square inequalities
\[
0\le(\sqrt t\,a-c/\sqrt t)^2,\qquad
0\le(\sqrt v\,a-d/\sqrt v)^2
\]
give \(4acb^2\le2t a^2b^2+2t^{-1}b^2c^2\) and \(4adc^2\le2v a^2c^2+2v^{-1}c^2d^2\). Set \(z=(a^2,b^2,c^2,d^2)^{\mathsf T}\). Hence (1) implies
\[
\int_G|F|^4\,d\mu\le2E^2+z^{\mathsf T}Mz,
\qquad
M=\begin{pmatrix}
-1&t&v&0\\
t&-1&t^{-1}&0\\
v&t^{-1}&-1&v^{-1}\\
0&0&v^{-1}&-1
\end{pmatrix}.\tag{2}
\]
Use the exact parameters in the finding, and set \(z_*=(1,B,t^2,v^2)^{\mathsf T}\), whose component sum is \(T\). One verifies
\[
Mz_*=\lambda\mathbf 1.\tag{3}
\]
For completeness, the second and fourth row identities are automatic from \(B=2t-\lambda\) and \(\lambda=t^2/v-v^2\). Upon substituting \(v=(t-1)(t^2+3t+1)/(t(2-t))\) into the first and third row identities, multiplying by the denominators, and simplifying, both residuals reduce to the defining ninth-degree polynomial times \(t(2-t)\). The included exact-rational checker verifies both polynomial identities coefficient by coefficient, as well as the nonzero denominators.

A sign test at the rational interval endpoints gives opposite signs for the defining polynomial. Its derivative exceeds \(42\) throughout the interval (an explicit rational interval estimate in the checker). Thus the specified root exists and is unique **in that interval**, which is all that is needed. Here \(v(t)\) increases on the bracket, because its positive numerator increases and its positive denominator \(t(2-t)\) decreases for \(1<t<2\). Rational endpoint bounds give \(0.740<v<0.742\) and \(B>1\).

To prove global sharpness rather than merely stationarity, let \(h=z-(E/T)z_*\); then \(\sum_j h_j=0\). Equation (3) gives
\[
z^{\mathsf T}Mz=\frac{\lambda}{T}E^2+h^{\mathsf T}Mh.
\]
Represent \(h\) by its first three coordinates in the zero-sum basis \(e_0-e_3,e_1-e_3,e_2-e_3\). The corresponding symmetric matrix is
\[
D=\begin{pmatrix}
-2&t-1&v-1-v^{-1}\\
t-1&-2&t^{-1}-1-v^{-1}\\
v-1-v^{-1}&t^{-1}-1-v^{-1}&-2-2v^{-1}
\end{pmatrix}.
\]
The exact rational bounds \(11287/10000<t<11288/10000\) and \(0.740<v<0.742\) imply that \(-D\) is strictly diagonally dominant with positive diagonal. Indeed, the respective off-diagonal absolute-value row sums are strictly less than \(2\), \(2\), and \(2+2/v\). Thus \(D\) is negative definite. Combining this with (2) proves the asserted inequality; equality forces \(h=0\), so the magnitudes are a common multiple of \((1,\sqrt B,t,v)\).

Conversely this positive vector attains both square inequalities. Equality in the two complex triangle inequalities in (1) forces \(c_0c_2\) and \(c_1^2\) to have the same argument, and independently forces \(c_0c_4\) and \(c_2^2\) to have the same argument. Dividing by the common phase of \(c_0\) gives exactly \((1,e^{i\vartheta},e^{2i\vartheta},e^{4i\vartheta})\) for the relative phase factors, with the fixed magnitudes above. Every such vector attains equality, proving the full classification.

Finally, to see that the character-order threshold is sharp, take all four coefficients equal to their displayed positive extremal magnitudes and let \(A_k\) be the nonnegative coefficient of the square of \(1+\sqrt B\,z+t z^2+v z^4\) at degree \(k\). In order \(N\) the fourth moment becomes \(\sum_{r\bmod N}|\sum_{k\equiv r\bmod N}A_k|^2\). For \(N=5\), \(A_0\) merges with \(A_5\); for \(N=6\), \(A_0\) merges with \(A_6\); for \(N=7\), \(A_1\) merges with \(A_8\); and for \(N=8\), \(A_0\) merges with \(A_8\). Each pair is strictly positive, so each collision strictly increases the normalized fourth moment above \(\mathcal K\).

## Verification
Run `python3 checker.py` using only the Python standard library. It checks the exact coefficient identities in (3), the signs of the ninth-degree polynomial at the rational endpoints, a positive derivative certificate, the strict diagonal-dominance inequalities, and positivity of \(B\). The execution returned `CERTIFICATE_PASS`, with \(1500\) supplemental random complex coefficient tests, direct finite Fourier computations for six nonaliased character orders, and strict witnesses for the four smaller distinct-support orders. The proof above uses exact identities and inequalities; numerical tests alone would not establish an inequality for all coefficients or all groups.

## Relationship to prior work
De Dios Pont and Madrid investigate sharp autoconvolution and autocorrelation inequalities motivated by additive combinatorics and questions about extremizers. Their 2021 preprint supplies the convolution-optimization motivation, but its main real-line weighted inequalities are not this four-character sharp \(L^2\)-to-\(L^4\) norm or its equality classification. Schmidt studies small fourth moments of unimodular trigonometric polynomials, with an autocorrelation formula directly related to the identity above; his results concern a *minimum* over phase-restricted polynomials, not the unrestricted weighted *maximum* here.

The published four-point support-geometry classification for prime cyclic groups also minimizes the fourth moment among *equal-magnitude* coefficients. It includes supports of this additive type but neither its statement nor its proof determines the present unrestricted weighted maximum. The published missing-third-harmonic Carathéodory–Fejér theorem optimizes one Fourier coefficient under positivity; it does not optimize a nonlinear fourth-moment norm. These were compared as implications, not merely by title. Searches using alternative descriptions such as weighted additive energy, sparse polynomial, four-tap autocorrelation, and finite cyclic extension did not locate an equivalent statement; this absence is not a proof of novelty.

## Limitations
The result concerns precisely the linked-midpoint spectrum \(\{0,1,2,4\}\) and fourth moments. It does not evaluate other four-point spectra, higher moments, or character orders at most eight; orders five through eight instead provide the stated counterexamples to the stable constant. The exact algebraic definition is more informative than its decimal approximation. The equality classification is mathematical, not an independent external certification. A residual bibliographic risk remains from older sparse-filter or \(\Lambda(4)\)-set norm calculations indexed under different vocabulary.

## References
1. J. de Dios Pont and J. Madrid, *On classical inequalities for autocorrelations and autoconvolutions*, arXiv:2106.13873v1, first public 2021-06-25, https://arxiv.org/abs/2106.13873 .
2. K.-U. Schmidt, *On a problem due to Littlewood concerning polynomials with unimodular coefficients*, arXiv:1302.2766v1, first public 2013-02-12, https://arxiv.org/abs/1302.2766 .
3. *Four-point support geometry quantizes the phase-only fourth Fourier moment*, published research record `2b7f859e0b5c`, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-four-point-support-geometry-quantizes-the-phase-only-fourth-four--2b7f859e0b5c .
4. *Exact Carathéodory–Fejér constant with the third harmonic missing*, published research record `b301e7223b2c`, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-carath-odory-fej-r-constant-with-the-third-harmonic-missin--b301e7223b2c .
