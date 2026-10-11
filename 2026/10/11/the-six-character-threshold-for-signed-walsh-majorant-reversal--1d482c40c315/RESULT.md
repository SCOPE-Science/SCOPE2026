# The six-character threshold for signed Walsh majorant reversal

## Finding
Let \(G_d=\mathbb F_2^d\) and write the Walsh characters as
\[
\chi_\gamma(x)=(-1)^{\gamma\cdot x},\qquad x,\gamma\in G_d.
\]
For a nonempty support \(S\subseteq G_d\) of distinct characters and signs \(\varepsilon_\gamma\in\{-1,1\}\), define the normalized third absolute moment
\[
M_3(S,\varepsilon)=2^{-d}\sum_{x\in G_d}
\left|\sum_{\gamma\in S}\varepsilon_\gamma\chi_\gamma(x)\right|^3,
\qquad M_3(S,+)=M_3(S,(1)_{\gamma\in S}).
\]
**Theorem.** For every integer \(d\ge0\), whenever \(1\le |S|\le6\),
\[
M_3(S,\varepsilon)-M_3(S,+)\le3.
\]
If \(|S|\le5\), the difference is nonpositive. If \(|S|=6\), the difference is positive **precisely** if \(S\) is an affine six-circuit and the product of all its coefficients is negative. In those and only those reversal cases,
\[
M_3(S,+)=21,\quad M_3(S,\varepsilon)=24,\quad
M_3(S,\varepsilon)-M_3(S,+)=3.
\]
The least possible reversing support size is therefore \(6\), and the least ambient dimension is \(4\). More strongly, for \(d\le3\) and any \(S\subseteq G_d\) (without a cardinality restriction), no signing yields a reversal.

An explicit witness in every \(d\ge4\) is
\[
S=\{0,e_1,e_2,e_3,e_4,e_1+e_2+e_3+e_4\},
\]
with coefficient \(-1\) on the last character and \(+1\) on the other five.

## Assumptions and scope
All groups are finite vector spaces over \(\mathbb F_2\), with **uniform probability measure** on the spatial group; thus \(M_3\) is the cube of the normalized \(L^3\)-norm, not the norm itself. Frequency supports are sets, so no repetitions are allowed. All displayed coefficients have absolute value exactly one and are restricted to real signs. The result neither asserts the majorant property for arbitrary real magnitudes nor classifies unrestricted complex coefficients or other exponents.

An **affine dependence** here means an even-cardinality subset \(T\subseteq S\) whose vector sum is zero in \(G_d\); a **six-circuit** is a six-element set having exactly one nonempty affine dependence, namely \(T=S\). Equivalently, \(S\) has affine dimension \(4\) and its six vectors sum to zero. The affine dimension is the linear rank of \(\{\gamma-\gamma_0:\gamma\in S\}\) for any \(\gamma_0\in S\).

## Proof
**1. Reductions.** Translating all frequencies by \(v\in G_d\) multiplies either Walsh polynomial pointwise by \(\chi_v\), so it does not change its modulus. An invertible linear frequency transformation just permutes the spatial group. Multiplying the signed polynomial by an overall sign or a Walsh character likewise preserves its modulus; hence two signings differing by an affine-linear sign function on the support have identical moments. A support of affine rank \(r\) has the moment distribution of a corresponding subset of \(G_r\). Signs modulo these symmetries are classified by the linear relations among the frequency vectors after adjoining a constant coordinate.

Over \(\mathbb F_2\), a nonempty affine dependence is necessarily even in size. Distinct frequencies cannot produce a two-point dependence. Thus among at most six points every minimal dependence has size four or six. For an affine independent support any choice of signs extends to an affine-linear sign function, making its moment equal to that of the all-positive polynomial.

**2. Supports of four and five.** Three or fewer distinct points are affinely independent. At size four the sole non-independent shape is a four-circuit, with canonical signed polynomials
\[
P_\eta=1+X+Y+\eta XY,\qquad X,Y\in\{-1,1\},\quad\eta\in\{-1,1\}.
\]
Directly averaging the four possible pairs gives
\[
\mathbb E|P_+|^3=16,\qquad \mathbb E|P_-|^3=8.
\]
At size five the only dependent shape is a four-circuit plus an independent character. The canonical polynomials become
\[
Q_\eta=1+X+Y+\eta XY+Z,
\]
with independent uniform signs \(X,Y,Z\). Enumerating the eight values gives
\[
\mathbb E|Q_+|^3=\frac{79}{4},\qquad \mathbb E|Q_-|^3=14.
\]
No reversal occurs for at most five characters.

**3. Six frequencies of affine rank four or five.** For affine rank five the support is independent and all moments agree. At affine rank four there is exactly one independent affine relation, whose support must have size four or six. In the four-circuit case, after the reductions the canonical polynomial is
\[
R_\eta=1+X+Y+\eta XY+Z+W
\]
for four independent uniform signs; exact averaging gives
\[
\mathbb E|R_+|^3=25,\qquad \mathbb E|R_-|^3=20.
\]
Thus four-circuit sign changes only reduce the moment.

In the six-circuit case, the canonical form is
\[
T_\eta=1+X_1+X_2+X_3+X_4+\eta X_1X_2X_3X_4,
\quad \eta=\prod_{\gamma\in S}\varepsilon_\gamma.
\]
The plus polynomial has absolute value \(6\) at one of the sixteen inputs and \(2\) at the other fifteen. The minus polynomial has absolute value \(4\) at six of the sixteen inputs and zero at the other ten. Consequently,
\[
\mathbb E|T_+|^3=\frac{6^3+15\cdot2^3}{16}=21,
\qquad
\mathbb E|T_-|^3=\frac{6\cdot4^3}{16}=24.
\]
The one-dimensional sign quotient makes these the only possible moments in a six-circuit. This proves the claimed reversal classification within affine ranks four and five.

**4. Six frequencies of affine rank three.** An affine three-space has exactly eight points; a six-point subset is the complement of two distinct points. Its all-positive polynomial has absolute values \(6\) at one point, \(2\) at three points and \(0\) at four, so its third absolute moment equals
\[
\frac{6^3+3\cdot2^3}{8}=30.
\]
For an arbitrary signing let \(U(x)\) be its real Walsh polynomial on the eight-point affine span. The sum of its six frequencies is the sum of the two omitted frequencies, which is nonzero. Hence the product of its six signed summands is a nonconstant character times a fixed sign. On exactly four inputs the number of negative summands is even, forcing \(|U(x)|\in\{2,6\}\); on the other four it is odd, forcing \(|U(x)|\in\{0,4\}\).

Let \(a\) count the \(6\)-magnitude inputs in the first class and \(b\) the \(4\)-magnitude inputs in the second. Walsh orthogonality gives \(\sum_x U(x)^2=8\cdot6=48\). Therefore
\[
4\cdot 2^2+a(6^2-2^2)+b\cdot4^2=48,
\quad\text{hence }2a+b=2.
\]
Thus either \((a,b)=(1,0)\) and the third moment is \(30\), or \((a,b)=(0,2)\) and it is \(20\). No reversal is possible. Affine rank at most two cannot contain six distinct points. Combining all cases proves the sharp bound and its equality-for-reversal statement in every ambient dimension.

**5. Excluding reversal in dimensions at most three at larger supports.** Supports of cardinality at most six are already handled. The only remaining ambient case is \(d=3\), with seven or eight frequencies. For seven frequencies the positive polynomial equals the full Walsh sum with one character removed: its absolute values are \(7\) at one input and \(1\) at seven others. Its moment is \(350/8=175/4\).

For any signing \(U\) on seven frequencies, the values \(|U(x)|\) are odd integers between \(1\) and \(7\), and \(\sum_x|U(x)|^2=8\cdot7=56\). The convex function \(t\mapsto t^{3/2}\) lies below the chord joining \((1,1)\) and \((49,343)\) for \(1\le t\le49\). Hence
\[
|U(x)|^3\le1+\frac{57}{8}(|U(x)|^2-1),
\quad\sum_x|U(x)|^3\le8+\frac{57}{8}(56-8)=350.
\]
At eight frequencies the positive polynomial is the full Walsh sum, of third moment \(64\). Any signed eight-term polynomial obeys \(\|U\|_\infty\le8\) and \(\mathbb E|U|^2=8\), so \(\mathbb E|U|^3\le64\). Smaller dimensions embed into dimension three. The minimum ambient dimension for strict reversal is therefore four.

## Verification
`checker.py` is standalone Python using only the standard library and integer arithmetic. Running `python checker.py` checks every nonempty support and every signing in \(G_3\); for \(G_4\) it checks every support of size at most five containing zero, every signing up to overall negation, and all \(3003\) six-point supports containing zero with all \(32\) normalized signings. The exact output identifies \(168\) six-support circuits and \(2688\) reversing normalized signed instances. All reversing instances have exact moments \(21\) and \(24\). The computations are finite corroboration; unrestricted dimensions follow from the proof above, not from extrapolation.

## Relationship to prior work
The Hardy–Littlewood majorant problem asks when coefficientwise Fourier domination forces norm domination. Krenedits (arXiv:1006.0409) analyzes signed idempotent trigonometric polynomials on the **circle**, including three-term examples. Gressman, Guo, Pierce, Roos and Yung (arXiv:2106.12538) classify supports with the strict majorant property for **integer-lattice frequencies on continuous multidimensional tori**, with unrestricted real coefficient magnitudes and exponents. Their theorems neither state nor directly give the present exact \(L^3\), equal-magnitude, sign-only classification on Boolean groups, where character squares are identically one and even affine relations govern the phenomenon. General finite-group or older Walsh majorant formulations may overlap and need independent bibliographic scrutiny.

## Limitations
The sharp classification concerns real signs at unit magnitude and exponent \(3\). It does not determine majorant thresholds for arbitrary magnitudes, complex unit phases, general finite abelian groups or other exponents. The dimensional bound beyond \(d=3\) pertains to supports of size at most six only. Finite numerical checks do not replace the dimension-free proof. Originality is based on inspected accessible literature and repository comparisons, not a proof that unindexed equivalent work does not exist. Independent external mathematical validation remains outstanding.

## References
1. P. T. Gressman, S. Guo, L. B. Pierce, J. Roos and P.-L. Yung, *On the strict majorant property in arbitrary dimensions*, arXiv:2106.12538 (first submitted 2021-06-23); *Quarterly Journal of Mathematics* 74 (2023), 139–161.
2. S. Krenedits, *Three-term idempotent counterexamples in the Hardy–Littlewood majorant problem*, arXiv:1006.0409 (first submitted 2010-06-02).
3. G. H. Hardy and J. E. Littlewood, *Notes on the theory of series (XIX): a problem concerning majorants of Fourier series*, *Quarterly Journal of Mathematics* 6 (1935), 304–315.
