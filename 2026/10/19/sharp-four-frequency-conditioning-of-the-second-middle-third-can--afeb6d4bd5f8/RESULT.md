# Sharp four-frequency conditioning of the second middle-third Cantor grid

## Finding
Let \(A=\{0,2,6,8\}\subset\mathbb Z/9\mathbb Z\). For a four-element frequency set \(F\subset\mathbb Z/9\mathbb Z\), form the normalized exponential matrix
\[
T_F=\left(\frac12 e^{2\pi i af/9}\right)_{a\in A,\,f\in F},
\qquad \kappa(F)=\frac{\sigma_{\max}(T_F)}{\sigma_{\min}(T_F)},
\]
with infinite condition number for singular matrices. The **sharp** condition number is
\[
\min_{|F|=4}\kappa(F)
=\sqrt{\frac{2+a+c+\Delta}{2+a+c-\Delta}}
=2.35841930748\ldots,
\qquad \Delta=\sqrt{(a-c)^2+4(b-1/2)^2},
\]
where
\[
 a=\tfrac12[\cos(4\pi/9)+\cos(8\pi/9)],\quad
 b=\tfrac12[\cos(8\pi/9)+\cos(16\pi/9)],\quad
 c=\tfrac12[\cos(16\pi/9)+\cos(32\pi/9)].
\]
Equality holds **exactly** when \(F=\{0,1,3,7\}+t\pmod 9\), with \(t\in\mathbb Z/9\mathbb Z\). These are nine distinct sets. Indeed, every other four-frequency set satisfies the strict, rationally certified gap \(\kappa(F)^2>57/10\), whereas the minimum squared condition number is less than \(57/10\).

## Assumptions and scope
The four spatial nodes are the two-stage ternary Cantor digit set \(A=\{2\varepsilon_0+6\varepsilon_1:\varepsilon_0,\varepsilon_1\in\{0,1\}\}\), sampled modulo nine. Frequency sets comprise **four distinct residues** of nine; entries have uniform amplitude and are unweighted. The theorem is an exact, finite-dimensional Riesz-basis conditioning result. No assertion is made for arbitrarily high stages, arbitrary real frequencies, or the limiting Cantor measure.

## Proof
**Step 1 (real Gram matrix).** Multiplying each column of \(T_F\) by an appropriate unit complex phase centered at the spatial midpoint \(4\) does not change singular values. In frequency order \(f_1,\ldots,f_4\), the resulting Gram matrix is real symmetric, with diagonal entry \(1\) and off-diagonal entry \(t_d=\tfrac12[\cos(4\pi d/9)+\cos(8\pi d/9)]\), where \(d=f_i-f_j\pmod9\). Symmetry gives \(t_{9-d}=t_d\), \(t_3=-1/2\), \(t_1=a\), \(t_2=b\), \(t_4=c\). For all \(F\), the squared condition number is the ratio of the extreme eigenvalues, or infinity when the least eigenvalue is zero.

**Step 2 (exact diagonalization of the proposed optimizer).** For \(F_*=\{0,1,3,7\}\), in the indicated order,
\[
G_*=
\begin{pmatrix}
1&a&-1/2&b\\
a&1&b&-1/2\\
-1/2&b&1&c\\ b&-1/2&c&1
\end{pmatrix}.
\]
The symmetric and antisymmetric vector sectors with respect to exchanging the first two and last two coordinates reduce this matrix to
\[
B_+=\begin{pmatrix}1+a&b-1/2\\b-1/2&1+c\end{pmatrix},
\qquad B_-=\begin{pmatrix}1-a&-1/2-b\\-1/2-b&1-c\end{pmatrix}.
\]
The two eigenvalues of \(B_+\) are \((2+a+c\pm\Delta)/2\). Direct rational enclosures of the trigonometric coefficients show both eigenvalues of \(B_-\) lie **strictly** between these two eigenvalues of \(B_+\). The same enclosures yield \(\lambda_{\max}(G_*)<177/100\) and \(\lambda_{\min}(G_*)>317/1000\), so \(\kappa(F_*)^2< (177/100)/(317/1000)<57/10\). The displayed sharp expression follows.

**Step 3 (exhaustive sharpness certificate).** Translating all frequencies preserves the Gram entries. Exactly \(\binom94=126\) quadruples fall into **14** translation classes, each of size nine. The script `verify.py` enumerates all \(126\) quadruples, canonically chooses the lexicographically smallest translate of each and checks the class count, with no assumed orbit classification. For each of the other thirteen representatives, it supplies two fixed, nonzero integer vectors: one witnesses a small Rayleigh quotient and one a large quotient. The exact-rational interval checker proves for all thirteen classes
\[
10\,\frac{u^{\mathsf T}G_Fu}{\|u\|_2^2}
>57\,\frac{v^{\mathsf T}G_Fv}{\|v\|_2^2}
\]
under certified enclosures of every entry. Since the smallest eigenvalue does not exceed the second Rayleigh quotient, while the largest is at least the first, it follows that \(\kappa(F)^2>57/10\), also for any singular case. The strict gap and the characterization of equality follow.

**Step 4 (rigorous trigonometric arithmetic).** The only transcendentals required are \(\pi\) and the three cosine combinations. `verify.py` encloses \(\pi\) by Machin's arctangent identity and alternating rational series; it then encloses each cosine using a rational Taylor partial sum with a proven remainder and the Lipschitz bound \(|\cos x-\cos y|\le|x-y|\). With denominator \(10^{12}\), it certifies the integer-bracketed intervals
\[
\begin{aligned}
10^{12}a&\in(-383022221560,-383022221559),\\
10^{12}b&\in(-86824088834,-86824088833),\\
10^{12}c&\in(469846310392,469846310393).
\end{aligned}
\]
Every comparison and discriminant square-root enclosure is implemented with integer or rational arithmetic and checked by exact inequalities; printing approximations is not used in any decision.

## Verification
Run `python3 verify.py` using Python's standard library. The program verifies all \(126\) cases via their \(14\) translation classes, all \(13\) strict Rayleigh barriers, the optimizer's eigenvalue ordering, and the sharp constant bracket. Its final interval for the squared optimal condition number is 
\[
\frac{3537628961215}{636019216451}
<\kappa_*^2<
\frac{3537628961221}{636019216445}.
\]
The source code and input test vectors are embedded in this finding; verification needs no network, floating-point tolerance, or external theorem prover. The numerical printout is diagnostic only, not a substitute for the finite exact-rational certificate.

## Relationship to prior work
De Dios Pont, Liehr and Taylor (2026) prove **nonexistence of Fourier frames for the limiting odd-base Cantor measures** and discuss finite-stage Cantor spaces. That statement is not a finite-level optimal conditioning theorem. Dutkay, Emami and Lai (2018) establish existence of Riesz sequences for fractal measures but do not classify the best four-frequency discretization here. Batenkov, Demanet, Goldman and Yomdin (2018/2020) give general partial-Fourier conditioning estimates, not this sharp finite minimax constant. Existing work on minimum tight exponential-frame cardinalities over prime-power cyclic groups concerns zero condition-number **defect**, i.e., exact tightness, and does not determine the best *non-tight* four-character basis. A separate optimal Riesz-conditioning result for three consecutive sites uses a different support and dimension. These comparisons distinguish theorem implications, not merely terminology.

## Limitations
The enumeration concerns the unweighted \(9\)-character grid and only the second Cantor stage. Weighted frames, continuously variable real frequencies, and higher levels could behave differently. The result does not imply an infinite frame for the Cantor measure and does not identify any asymptotic conditioning rate. Historical-priority risk remains for unindexed finite-grid optimization tables; no independent audit has been performed.

## References
1. J. de Dios Pont, L. Liehr, M. A. Taylor, *Cantor measures with odd base do not admit Fourier frames*, arXiv:2607.08656 (first available 2026-07-09), https://arxiv.org/abs/2607.08656.
2. D. E. Dutkay, S. Emami, C.-K. Lai, *Existence and exactness of exponential Riesz sequences and frames for fractal measures*, arXiv:1809.06541 (2018), https://arxiv.org/abs/1809.06541.
3. D. Batenkov, L. Demanet, G. Goldman, Y. Yomdin, *Conditioning of partial nonuniform Fourier matrices with clustered nodes*, arXiv:1809.00658 (2018), https://arxiv.org/abs/1809.00658; *SIAM J. Matrix Anal. Appl.* 41 (2020), 199–220.
4. *Minimum tight exponential-frame size on cyclic prime-power groups*, public research record `2026/10/4/SCOPE-minimum-tight-exponential-frame-size-on-cyclic-prime-power-group--b7a941dc4a7d` (comparison based on available indexed theorem statement).
5. *Sharp Riesz conditioning for consecutive triples on finite cycles*, public research record `2026/10/11/SCOPE-sharp-riesz-conditioning-for-consecutive-triples-on-finite-cycle--1200745c9cae` (comparison based on available indexed theorem statement).
