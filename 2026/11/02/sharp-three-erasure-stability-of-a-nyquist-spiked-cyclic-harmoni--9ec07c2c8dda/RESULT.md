# Sharp three-erasure stability of a Nyquist-spiked cyclic harmonic frame

## Finding
For every integer \(m\ge3\), put \(N=2m\), \(\omega=\exp(2\pi i/N)\), and let
\[
 f_j=N^{-1/2}\bigl(1,\omega^j,(-1)^j\bigr)^{\mathsf T}\in\mathbb C^3,
 \qquad j\in\mathbb Z_N.
\]
The full system is Parseval. For any three-element set \(E\subset\mathbb Z_N\), define its retained frame operator
\[
 S_E=\sum_{j\notin E} f_jf_j^*,\qquad
 s_m=1+2\cos(2\pi/m),\qquad
 \Lambda_m=\frac{9+\sqrt{9+8s_m^2}}2.
\]
Then the **simultaneously sharp** spectral bounds over all three-site erasures are
\[
 \boxed{\left(1-\frac{\Lambda_m}{2m}\right)I_3\preceq S_E\preceq I_3.}
\]
The lower bound is attained precisely for parity-pure triples whose three indices are consecutively spaced within their parity class. Equivalently,
\[
 E=\{t,t+2,t+4\}\pmod{2m},\qquad t\in\mathbb Z_{2m}.
\]
There are exactly two distinct lower-extremizing sets for \(m=3\), and exactly \(2m\) for every \(m\ge4\). The upper eigenvalue \(1\) is attained precisely when all three erased sites have the same parity, giving \(2\binom m3\) such sets. Each lower-extremizing triple also attains the upper bound.

Consequently, **every** three-site erasure retains a frame exactly when \(m\ge4\); when \(m=3\), exactly the two parity-pure erasure sets destroy injectivity. For \(m\ge4\), the worst squared singular-value condition number of the retained analysis operator is
\[
 \boxed{\kappa_m^2=\left(1-\frac{\Lambda_m}{2m}\right)^{-1}
       =1+\frac9{2m}+O(m^{-2})}\qquad(m\to\infty),
\]
attained precisely by the same \(2m\) lower-extremizing sets. In particular, the worst missing sites form a step-two arithmetic progression, **not** three cyclically adjacent sites.

## Assumptions and scope
The ambient finite group is \(\mathbb Z_{2m}\), the selected Fourier frequencies are exactly \(\{0,1,m\}\), all weights are equal to \(1/\sqrt{2m}\), and erasures consist of three *distinct* labelled samples. Eigenvalue inequalities use the Hermitian Loewner order; the squared condition number is the largest divided by the smallest eigenvalue of \(S_E\), and is declared infinite for singular \(S_E\). Neither nonuniform weights nor arbitrary three-frequency selections are covered. The closed expressions are real numbers; \(s_3=0\) and \(s_m>0\) for \(m\ge4\).

## Proof
**1. Frame and erasure reduction.** The frequencies \(0,1,m\) are distinct modulo \(2m\), so character orthogonality gives \(\sum_j f_jf_j^*=I_3\). Let \(A_E\) be the unnormalized matrix with columns \((1,\omega^j,(-1)^j)^{\mathsf T}\) for \(j\in E\). Since \(|E|=3\), its square Gram matrix \(H_E=A_E^*A_E\) has the same eigenvalues as \(A_EA_E^*\). Hence
\[
 S_E=I_3-\frac1{2m}A_EA_E^*,\qquad
 \lambda_{\min}(S_E)=1-\frac{\lambda_{\max}(H_E)}{2m},\quad
 \lambda_{\max}(S_E)=1-\frac{\lambda_{\min}(H_E)}{2m}.
\]
Thus the sharp lower frame bound is equivalent to maximizing \(\lambda_{\max}(H_E)\) over erasure triples.

**2. Separate the Nyquist parity channels.** Apply the fixed unitary that replaces the zeroth and \(m\)-th frequency coordinates by their sum and difference. After this transformation, an unnormalized column is
\[
 j\text{ even}:\ (\sqrt2,\omega^j,0)^{\mathsf T},\qquad
 j\text{ odd}:\ (0,\omega^j,\sqrt2)^{\mathsf T}.
\]
Every triple is either parity-pure or has two sites in one parity and one in the other.

**3. Parity-pure triples.** For a parity-pure triple \(E\), let \(T_E=\sum_{j\in E}\omega^j\). The transformed matrix has a zero row and the two nonzero rows have squared norms \(6\) and \(3\), with cross term of modulus \(\sqrt2|T_E|\). Its nonzero squared singular values are therefore
\[
 L_\pm(E)=\frac{9\pm\sqrt{9+8|T_E|^2}}2,
\]
and the third is zero. The maximum of \(|T_E|\) over three distinct roots of unity in a single parity class equals \(s_m\), achieved precisely by three *consecutive* vertices of the regular \(m\)-gon. Indeed, for any nonzero resultant \(T_E\), project all available unit roots onto its direction: a maximizing triple must consist of the three roots with largest projection, which are three consecutive polygon vertices. The adjacent triple has resultant modulus \(|1+e^{2\pi i/m}+e^{4\pi i/m}|=s_m\). The case \(m=3\) consists of the unique triple, whose resultant is zero. The projection argument also establishes that no other triple is a maximizer. Hence the best parity-pure erased eigenvalue is exactly \(\Lambda_m\).

**4. Mixed-parity triples.** Suppose, without loss of generality, two erased sites have even parity and one has odd parity. Denote by \(u_1,u_2\) the two unit complex phases at the even sites, and by \(v\) the odd phase. The Gram matrix \(A_EA_E^*\), after diagonal unitary conjugation, is the real symmetric tridiagonal matrix
\[
 B(t)=\begin{pmatrix}4&\sqrt2t&0\\\sqrt2t&3&\sqrt2\\0&\sqrt2&2\end{pmatrix},\qquad t=|u_1+u_2|.
\]
The same formula applies after interchanging the parity channels. Since the two same-parity sites are distinct vertices of a regular \(m\)-gon, \(t\le2\cos(\pi/m)\). By the Perron principle for nonnegative symmetric matrices (or its Rayleigh quotient), the largest eigenvalue of \(B(t)\) is at most that of \(B(2\cos(\pi/m))\), with equality only at a nearest-neighbor pair within the parity class.

We now show that **all** mixed-parity erased eigenvalues are strictly below \(\Lambda_m\). For \(m=3\), \(B(2\cos(\pi/3))=B(1)\) and the leading principal minors of \(6I_3-B(1)\) are \(2,4,12\). Hence the mixed maximum is strictly below \(6=\Lambda_3\). For \(m=4\), \(B(2\cos(\pi/4))=B(\sqrt2)\), and the leading principal minors of \(6I_3-B(\sqrt2)\) are \(2,2,4\). Hence the mixed maximum is strictly below \(6<\Lambda_4=(9+\sqrt{17})/2\). Finally, for \(m\ge5\), the positive entries of the maximal mixed matrix are bounded above by those of \(B(2)\). The leading principal minors of \(7I_3-B(2)\) are \(3,4,14\), so \(\lambda_{\max}(B(2))<7\). But \(s_m\ge s_5=(1+\sqrt5)/2\), and thus \(\Lambda_m\ge\Lambda_5>7\). Sylvester's criterion justifies all three strict bounds. The parity-pure maximum therefore wins globally, with exactly the equality sets described in Step 3.

**5. Upper bound, injectivity, counts, and condition number.** For every parity-pure \(E\), the transformed \(A_E\) has rank at most two, so \(H_E\) has a zero eigenvalue and \(S_E\) has upper eigenvalue \(1\). For every mixed \(E\), the two same-parity columns are independent because their unit phases differ; the opposite-parity column adds an independent third coordinate. Hence \(A_E\) is invertible, \(H_E\) positive definite, and the upper eigenvalue of \(S_E\) is strictly less than \(1\).

For \(m=3\), the two parity classes each supply exactly one three-subset, giving two lower/upper extremizers. For \(m\ge4\), the consecutive three-subsets of each \(m\)-cycle are exactly its \(m\) translates, giving \(2m\) lower extremizers; every parity-pure three-subset gives an upper extremizer, totaling \(2\binom m3\). Since \(\Lambda_3=6=2m\), the lower bound vanishes exactly at \(m=3\). At \(m=4\), \(\Lambda_4<8\); for \(m\ge5\), \(\Lambda_m\le9<2m\), so every erased frame is positive definite. The two sharp eigenvalue bounds occur simultaneously at each worst parity-pure triple, proving the exact worst squared condition number.

Finally, \(s_m=3+O(m^{-2})\), so \(\Lambda_m=9+O(m^{-2})\). Expanding \((1-\Lambda_m/(2m))^{-1}\) proves the stated asymptotic formula.

## Verification
Running `python3 verify.py` with Python 3 and NumPy enumerates every erased three-element set for each \(3\le m\le21\), computes the original complex Fourier Gram matrices independently, and compares their largest eigenvalues and the full set of maximizing masks with the closed formula. The completed replay reported `VERIFY_OK 64676 mask_spectra`; all tested dimensions achieved exactly the asserted maxima and cardinalities. The script also lists the exact positive leading principal minors in the three comparison matrices used in the proof. Finite numerical checks support the exact all-\(m\) proof; they are not a proof by extrapolation.

## Relationship to prior work
Bodmann and Paulsen's frame-erasure work establishes general criteria and many sharp estimates for two-uniform frames, but does not give the three-character Nyquist-spiked cyclic frame's all-parameter erasure spectrum. Ferreira studies spectral convergence of bandlimited missing-sample recovery and notes that worst low-pass erasures are often contiguous, whereas bandpass arrangements can behave differently. The present theorem gives an exact *noncontiguous* worst-case family and its complete equality classification; the fully detailed Ferreira article was not available for direct comparison, so an implicit earlier reduction remains a residual risk. Osgood, Siripuram, and Wu treat universal exact interpolation for discrete bandlimited spaces rather than a sharp uniform lower spectral bound. Marshall and Waldron classify harmonic frames up to equivalence, rather than adversarial deletion spectra.

Published complementary mathematical results give an all-count formula for **two-character** cyclic-frame erasures, a full-spark criterion for **three-row** patterns \(\{0,1,r\}\), and sharp conditioning for square Vandermonde samples of the **consecutive** frequency triple \(\{0,1,2\}\). The first does not control the additional Nyquist parity channel or the mixed-parity comparison; the second concerns three-column singularity rather than deletion of three columns from a long frame; the third has different frequencies and a different optimization quantifier. These distinctions do not constitute an independent certification of originality.

## Limitations
The theorem treats exactly three erased labelled sites in the equal-weight Parseval frame with frequencies \(\{0,1,m\}\) at even cyclic order \(2m\), with \(m\ge3\). It neither gives sharp bounds for arbitrary erasure counts nor covers arbitrary bandpass triples, unequal sampling weights, or optimal nonlinear decoders. The elementary regular-polygon rearrangement lemma is not claimed as new. The computational replay is finite and uses floating-point eigenvalues. An equivalent historical bandpass-frame or discrete missing-sample result, particularly in older signal-processing literature, could exist. Independent mathematical validation and publication-priority verification have not been carried out.

## References
1. B. G. Bodmann and V. I. Paulsen, *Frames, Graphs and Erasures*, arXiv:math/0406134v1, first public 2004-06-08; Linear Algebra and Its Applications 404 (2005), 118–146.
2. P. J. S. G. Ferreira, *Interpolation and the Discrete Papoulis-Gerchberg Algorithm*, IEEE Transactions on Signal Processing 42 (1994), 2596–2606, DOI:10.1109/78.324726.
3. B. Osgood, A. Siripuram, and W. Wu, *Discrete Sampling and Interpolation: Universal Sampling Sets for Discrete Bandlimited Spaces*, arXiv:1204.0992v1, first public 2012-04-04.
4. S. Marshall and S. Waldron, *On the Number of Harmonic Frames*, arXiv:1611.07121v1, first public 2016-11-22.
5. *Exact adversarial-erasure spectra for two-character cyclic harmonic frames*, published mathematical result, `2026/10/11/SCOPE-exact-adversarial-erasure-spectra-for-two-character-cyclic-harmo--e1e03f96b6f0`.
6. *A complete full-spark criterion for every three-row Fourier pattern*, published mathematical result, `2026/10/4/SCOPE-a-complete-full-spark-criterion-for-every-three-row-fourier-patt--843fec171d5a`.
7. *Sharp Riesz conditioning for consecutive triples on finite cycles*, published mathematical result, `2026/10/11/SCOPE-sharp-riesz-conditioning-for-consecutive-triples-on-finite-cycle--1200745c9cae`.
