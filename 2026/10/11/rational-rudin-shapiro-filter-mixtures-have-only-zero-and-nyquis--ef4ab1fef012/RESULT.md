# Rational Rudin–Shapiro filter mixtures have only zero- and Nyquist-frequency defects
## Finding
For each \(m\ge1\), every nonzero rational linear combination of the two length-\(2^m\) Rudin–Shapiro filters has a full cyclic Fourier spectrum except possibly one endpoint frequency. The exact cyclic-convolution rank and kernel are classified by the parity of \(m\) and the rational mixing pair.

Let \(N=2^m\). The exact nullity is
\[
\dim_{\mathbb C}\ker T_{m;a,b}=
\begin{cases}
1,&m\text{ odd and }(a=0\text{ or }b=0),\\
1,&m\text{ even and }(a=-b\text{ or }a=b),\\
0,&\text{otherwise}.
\end{cases}
\]
For a nonzero mixing pair, the two exceptions on any given parity are disjoint. Thus the complex rank is always \(N\) or \(N-1\). If \(m\) is odd, \(a=0\) gives the constant-vector kernel and \(b=0\) the alternating-vector kernel. If \(m\) is even, \(a=-b\) gives the constant-vector kernel and \(a=b\) the alternating-vector kernel. No other eigenvalue can vanish.

The rationality restriction is sharp in type: there exist real, irrational mixing coefficients yielding nullity at least two already at \(N=8\).

## Assumptions and scope
For every integer \(j\ge0\) define the complementary Rudin–Shapiro polynomials by
\[
P_0(z)=Q_0(z)=1,\quad
P_{j+1}(z)=P_j(z)+z^{2^j}Q_j(z),\quad
Q_{j+1}(z)=P_j(z)-z^{2^j}Q_j(z).
\]
Fix \(m\ge1\), set \(N=2^m\), choose \((a,b)\in\mathbb Q^2\setminus\{(0,0)\}\), and write \(W(z)=aP_m(z)+bQ_m(z)=\sum_{j=0}^{N-1}w_jz^j\). The corresponding cyclic convolution is \((T_{m;a,b}f)(t)=\sum_{j=0}^{N-1}w_jf(t-j)\), where all arguments are reduced modulo \(N\). Rank and nullity are over \(\mathbb C\). The Fourier character \(f_k(t)=\exp(2\pi i kt/N)\) has eigenvalue \(W(\exp(-2\pi i k/N))\). This normalization fixes the labels of the constant and alternating kernels.

Neither non-rational mixing coefficients nor non-dyadic cycle lengths are included. The zero mixing pair is excluded: it would give the zero operator.

## Proof
**Step 1: no zero at any root of dyadic order at least four.** Let \(2\le r\le m\) and let \(\zeta\) be a primitive \(2^r\)-th root of unity. For \(j\ge r\), \(\zeta^{2^j}=1\), so successive recursion matrices acting on \((P_j(\zeta),Q_j(\zeta))^\mathsf T\) are the invertible rational matrix
\[
H=\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad H^2=2I.
\]
At step \(j=r-1\), \(\zeta^{2^{r-1}}=-1\); hence
\[
\begin{pmatrix}P_r(\zeta)\\ Q_r(\zeta)\end{pmatrix}
=\begin{pmatrix}1&-1\\1&1\end{pmatrix}
\begin{pmatrix}P_{r-1}(\zeta)\\Q_{r-1}(\zeta)\end{pmatrix}.
\]
Both matrices are invertible over \(\mathbb Q\). Therefore \(aP_m(\zeta)+bQ_m(\zeta)\) can be written as \(A P_{r-1}(\zeta)+B Q_{r-1}(\zeta)\) with \(A,B\in\mathbb Q\) not both zero.

The polynomials \(P_{r-1}\) and \(Q_{r-1}\) have degree at most \(2^{r-1}-1\) and are linearly independent over \(\mathbb Q\): both have constant term one, and their difference is
\[
P_{r-1}(z)-Q_{r-1}(z)=2z^{2^{r-2}}Q_{r-2}(z)\ne0.
\]
Thus \(F(z)=A P_{r-1}(z)+B Q_{r-1}(z)\) is nonzero with \(\deg F<2^{r-1}\). A primitive \(2^r\)-th root has irreducible minimal polynomial \(\Phi_{2^r}(z)=z^{2^{r-1}}+1\), of degree \(2^{r-1}\). Consequently \(F(\zeta)\ne0\). This proves \(W(\zeta)\ne0\). For completeness, irreducibility follows also from Eisenstein at two applied to \((z+1)^{2^{r-1}}+1\): every non-leading coefficient is even and the constant term is two, not divisible by four.

**Step 2: exact endpoint evaluations.** At \(z=1\) the matrix \(H\) applies at every level, with initial vector \((1,1)^\mathsf T\). At \(z=-1\) the first step has matrix \(\begin{pmatrix}1&-1\\1&1\end{pmatrix}\), followed by \(H\) at every later step. Since \(H^2=2I\), direct induction yields
\[
(P_m(1),Q_m(1))=
\begin{cases}
(2^{m/2},2^{m/2}),&m\text{ even},\\
(2^{(m+1)/2},0),&m\text{ odd},
\end{cases}
\]
and
\[
(P_m(-1),Q_m(-1))=
\begin{cases}
(2^{m/2},-2^{m/2}),&m\text{ even},\\
(0,2^{(m+1)/2}),&m\text{ odd}.
\end{cases}
\]
These formulas give exactly the stated conditions for \(W(1)=0\) and \(W(-1)=0\). The conditions cannot hold simultaneously unless \(a=b=0\), which was excluded.

**Step 3: rank and kernel.** The discrete characters form a basis diagonalizing every cyclic convolution. Every eigenvalue is \(W(\zeta)\) for an \(N\)-th root \(\zeta\), and Steps 1–2 exhaust all such roots. Thus there are zero or one vanishing eigenvalues; the only possible kernel characters are \(1\) and \((-1)^t\), and the rank is \(N\) minus that number.

**Step 4: a sharp boundary beyond rational coefficients.** Let \(m=3\) and \(\zeta=\exp(\pi i/4)\). At this root, \(P_3(\zeta)=2\zeta^2(1-\zeta)\) and \(Q_3(\zeta)=2(1+\zeta)\), hence
\[
\frac{P_3(\zeta)}{Q_3(\zeta)}=\sqrt2-1.
\]
The nonzero real pair \((a,b)=(1,1-\sqrt2)\) therefore makes \(W(\zeta)=0\). As \(W\) has real coefficients, \(W(\overline\zeta)=0\) also. These two distinct primitive eighth roots give nullity at least two, which proves that the rationality assumption cannot simply be replaced by arbitrary real coefficients.

## Verification
The standalone file `verify.py` uses only Python's standard library. Run `python3 verify.py`. It constructs both polynomials exactly for all \(1\le m\le12\), tests every nonzero integer mixing pair in \(\{-3,-2,-1,0,1,2,3\}^2\), and checks the Fourier zeros by exact polynomial reduction modulo every dyadic cyclotomic polynomial \(\Phi_{2^r}\). It verifies the two endpoint conditions and performs independent exact rational Gaussian elimination on 24 full circulant matrices of order at most 16. The expected success string begins `VERIFY_OK`.

These finite tests do not prove the universal statement. The preceding irreducibility and recursion argument is the proof for all positive levels and all nonzero rational mixing pairs.

## Relationship to prior work
The Rudin–Shapiro recursion and its Fourier-analysis applications are classical. Brillhart–Carlitz (1970) gives strong algebraic information including a resultant for the two polynomials; coprimality alone does not determine which *rational combinations* have discrete-frequency zeros. Brillhart–Lomont–Morton (1976) investigates cyclotomic values; a later full-text account by Sobolewski (2019, §1 and §5) quotes its main root-of-unity recurrence for **odd-order** roots. The present statement concerns only dyadic roots and exact ranks of all rational two-channel combinations. Erdélyi (2014) proves Mahler-measure estimates and a grid-point recursion for individual polynomials, not the two-parameter rank classification. La Cour-Harbo (2007) studies a different orthogonal Rudin–Shapiro transform, while Abdollahi–Cheshmavar–Taghavi (2010/2011) use Rudin–Shapiro low-pass filters. El Abdalaoui (2016) studies their \(L^\alpha\)-flatness, not discrete cyclic-convolution kernels.

These distinctions refer to accessible statements, not an exhaustive historical-priority certification. The full original 1976 article, particularly any further discussion of even-order cyclotomic factors, remains an uninspected risk.

## Limitations
The theorem gives **exact rank and kernel**, not spectral condition numbers, lower nonzero singular-value bounds, or stable inversion. It concerns the classical two-polynomial pair with rational coefficients on cycles of order a power of two. A real irrational mixture can have a larger kernel; arbitrary complex mixtures are also outside scope. An equivalent historical statement might remain in uninspected literature; this text makes no priority-certification claim.

## References
1. A. la Cour-Harbo, *On the Rudin–Shapiro Transform*, Applied and Computational Harmonic Analysis 24 (2008), 310–328; first online 17 July 2007. DOI `10.1016/j.acha.2007.05.003`.
2. J. Brillhart and L. Carlitz, *Note on the Shapiro Polynomials*, Proceedings of the American Mathematical Society 25 (1970), 114–118. DOI `10.2307/2036537`.
3. J. Brillhart, J. S. Lomont and P. Morton, *Cyclotomic Properties of the Rudin–Shapiro Polynomials*, Journal für die reine und angewandte Mathematik 288 (1976), 37–65; record `JRAM_1976__288_151797`.
4. A. Abdollahi, J. Cheshmavar and M. Taghavi, *Wavelets Generated by the Rudin–Shapiro Polynomials*, Central European Journal of Mathematics 9 (2011), 441–448; first online 21 December 2010. DOI `10.2478/s11533-010-0094-4`.
5. T. Erdélyi, *The Mahler Measure of the Rudin–Shapiro Polynomials*, arXiv `1406.2233`, first posted 9 June 2014.
6. E. H. El Abdalaoui, *The Rudin–Shapiro Polynomials and the Fekete Polynomials Are Not \(L^\alpha\)-Flat*, arXiv `1603.04095`, first posted 13 March 2016.
7. B. Sobolewski, *Cyclotomic Properties of Polynomials Associated with Automatic Sequences*, arXiv `1909.12052`, first posted 26 September 2019.
