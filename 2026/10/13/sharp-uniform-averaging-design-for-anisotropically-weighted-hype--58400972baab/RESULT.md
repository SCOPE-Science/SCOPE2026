# Sharp uniform-averaging design for anisotropically weighted hypercubes

## Finding

**Theorem (signed-resonance classification and sharp integer-coupling design).** Fix an integer \(d\ge1\) and positive real couplings \(w_1,\ldots,w_d\). The weighted Boolean cube has vertex set \(\{0,1\}^d\), and its real symmetric Hamiltonian is
\[
H_w=\sum_{j=1}^d w_jX_j,
\]
where \(X_j\) flips the \(j\)-th bit. Write \(N=2^d\), \(U(t)=\exp(-itH_w)\), and \(M(t)_{xy}=|U(t)_{xy}|^2\). Let \(\widehat M=\lim_{T\to\infty}T^{-1}\int_0^T M(t)\,dt\), and let \(F_T=T^{-1}\int_0^T M(t)\,dt\) for \(T>0\). Let \(J_N\) denote the all-ones matrix.

1. For every subset \(S\subseteq\{1,\ldots,d\}\), the Boolean character \(\chi_S(x)=(-1)^{\sum_{j\in S}x_j}\) is an eigenvector of \(\widehat M\) with eigenvalue
   \[
   \mu_S=2^{-|S|}\#\left\{\epsilon\in\{-1,+1\}^S:\sum_{j\in S}\epsilon_jw_j=0\right\}.
   \]
   The empty subset contributes \(\mu_\varnothing=1\); multiplicities arise by counting the subsets with equal displayed eigenvalues. Thus
   \[
   \operatorname{rank}(\widehat M)=\#\{S\subseteq[d]:\exists\epsilon\in\{-1,+1\}^S,\ \sum_{j\in S}\epsilon_jw_j=0\}.
   \]
2. The exact long-time uniformity criterion is
   \[
   \widehat M=J_N/N\quad\Longleftrightarrow\quad
   \left|\left\{\sum_{j\in A}w_j:A\subseteq[d]\right\}\right|=2^d.
   \]
   That is, all subset sums must be distinct. This holds for every positive real coupling vector with no nonempty signed-zero resonance; it requires no rationality hypothesis.
3. If all \(w_j\) are **positive integers**, set \(g=\gcd(w_1,\ldots,w_d)\). A finite positive observation window has an *exactly uniform time-averaged transition matrix* precisely under the two simultaneous conditions
   \[
   F_T=J_N/N\quad\Longleftrightarrow\quad
   \bigl(\text{all subset sums are distinct}\bigr)
   \ \text{and}\ \ T\in\{k\pi/(2g):k\in\mathbb Z_{>0}\}.
   \]
   Whenever such a window exists, the first is exactly \(\pi/(2g)\).
4. Among all positive **integer** couplings realizing uniform long-time mixing, the minimum possible total coupling is exactly \(2^d-1\):
   \[
   \sum_{j=1}^d w_j\ge 2^d-1.
   \]
   Equality holds if and only if the multiset of weights is \(\{1,2,4,\ldots,2^{d-1}\}\). This minimum design has \(g=1\) and first exact uniform averaging window \(T=\pi/2\).
5. The *instantaneous* uniformity criterion for positive integer couplings is different:
   \[
   \exists t>0:\ M(t)=J_N/N\quad\Longleftrightarrow\quad
   v_2(w_1)=\cdots=v_2(w_d),
   \]
   where \(v_2(m)\) is the exponent of two in the positive integer \(m\). In particular, when \(d\ge2\), the unique minimum-budget averaging design cannot mix uniformly at an individual time, whereas the odd superincreasing design \(w_j=3^{j-1}\) attains both kinds of uniformity: instantaneous at \(t=\pi/4\) and exactly time-averaged over \(T=\pi/2\).

The theorem concerns full transition matrices, so its uniformity claims hold simultaneously for every initial vertex.

## Assumptions and scope

The cube is finite, the Hamiltonian has no on-site potential, and the coupling on each coordinate edge is identical at all vertices but may differ between coordinate directions. All weights are strictly positive; the signed-resonance spectrum and long-time equivalence allow arbitrary real weights. Only the finite-window arithmetic, coupling-budget, and two-adic instantaneous assertions require positive integer weights. The physical clock uses the evolution \(e^{-itH_w}\) with no additional normalization of \(H_w\). An overall scalar rescaling of all weights inversely rescales the time variable, so the *integer normalization* matters for the budget statement.

Here an exactly uniform *time average* means the integral of the instantaneous transition probabilities equals \(J_N/N\); this differs from instantaneous uniformity at a single time. Finite-window assertions are for windows beginning at time zero.

## Proof

**Step 1: tensor factorization and Fourier diagonalization.** The commuting bit flips yield
\[
U(t)=\bigotimes_{j=1}^d\bigl(\cos(w_jt)I_2-i\sin(w_jt)X\bigr),\qquad
M(t)=\bigotimes_{j=1}^d
\begin{pmatrix}\cos^2(w_jt)&\sin^2(w_jt)\\\sin^2(w_jt)&\cos^2(w_jt)\end{pmatrix}.
\]
The one-bit stochastic factor has eigenvalues \(1\) on the constant vector and \(\cos(2w_jt)\) on the difference vector. Their tensor-product eigenvectors are the orthogonal Walsh characters \(\chi_S\), with eigenvalues
\[
\lambda_S(t)=\prod_{j\in S}\cos(2w_jt).
\]
All the matrices \(M(t)\) therefore have a *common real orthogonal eigenbasis*, and integration acts coefficientwise in this basis.

**Step 2: exact Cesàro spectrum.** For nonempty \(S\), expand each cosine into two exponentials and pair each signed frequency with its negative. The time average of \(\cos(2at)\) tends to zero for every real \(a\ne0\), while the time average of the constant frequency is one. Hence
\[
\lim_{T\to\infty}\frac1T\int_0^T\lambda_S(t)\,dt
=\frac1{2^{|S|}}\sum_{\epsilon\in\{-1,+1\}^S}
\mathbf1_{\{\sum_{j\in S}\epsilon_jw_j=0\}}.
\]
For \(S=\varnothing\), the empty product equals one. This proves every eigenvalue including multiplicity, and the rank count because every \(\mu_S\) is nonnegative.

**Step 3: why subset sums control uniformity.** The matrix \(J_N/N\) is the orthogonal projector onto the constant Walsh character. Thus \(\widehat M=J_N/N\) holds exactly when every nonempty character has zero eigenvalue, equivalently when no nonempty signed-zero relation among the weights exists. Such a relation partitions its support into disjoint positive-sign and negative-sign subsets of equal weight, giving a collision between two distinct subset sums. Conversely a collision between distinct subsets, after canceling their intersection, gives a nonempty signed-zero relation. This proves the if-and-only-if criterion without any restriction on real couplings.

**Step 4: exact finite observation windows.** Now assume all weights are positive integers. If \(F_T=J_N/N\), its Walsh eigenvalue indexed by the singleton \(\{j\}\) vanishes, hence
\[
0=\frac1T\int_0^T\cos(2w_jt)\,dt=\frac{\sin(2w_jT)}{2w_jT}.
\]
As \(T>0\), for each \(j\) the quantity \(2w_jT/\pi\) is an integer. By Bézout's identity, \(2gT/\pi\) is then an integer, and positivity of \(T\) makes it a positive integer: \(T=k\pi/(2g)\).

Conversely, at every such \(T\), each term in the product-to-sum formula for \(\lambda_S(t)\) has frequency \(2a\), where \(a\) is an integer multiple of \(g\). If \(a\ne0\), its integral as a cosine is \(\sin(2aT)/(2aT)=0\), since \(2aT=k\pi(a/g)\). Zero-frequency terms contribute exactly one. Therefore **every Walsh eigenvalue of \(F_T\) equals the corresponding eigenvalue of \(\widehat M\)**, not merely approximately; the entire matrices coincide. Step 3 now gives \(F_T=J_N/N\) exactly when all subset sums are distinct, and the first possible positive \(T\) is \(\pi/(2g)\).

**Step 5: optimal integer coupling budget.** If all \(2^d\) integer subset sums are distinct and \(W=\sum_j w_j\), they are \(2^d\) integers in \(\{0,1,\ldots,W\}\), so \(W\ge2^d-1\). Equality requires all integers in \(\{0,1,\ldots,2^d-1\}\) to occur *exactly once*. The smallest weight is then one, and the subset-sum generating polynomial satisfies
\[
\prod_{j=1}^d(1+z^{w_j})=1+z+\cdots+z^{2^d-1}=\prod_{j=0}^{d-1}(1+z^{2^j}).
\]
Since the first weight is one, divide both sides by \(1+z\). The quotient contains only even powers of \(z\) with nonnegative coefficients; therefore all remaining weights are even (an odd weight would itself contribute a positive odd-degree coefficient). After substituting \(z^2\mapsto z\), repeat inductively. The unique multiset is \(\{1,2,4,\ldots,2^{d-1}\}\). Conversely these binary weights have all subset sums \(0,\ldots,2^d-1\) exactly once, attaining the bound.

**Step 6: instantaneous distinction.** The time-dependent matrix \(M(t)\) is uniform exactly when each one-bit factor is uniform; equivalently \(\cos(2w_jt)=0\) for all \(j\). This demands \(4w_jt/\pi\) be an odd integer for every \(j\). For any indices \(i,j\), the ratio \(w_i/w_j\) must therefore be odd-over-odd in lowest terms, forcing \(v_2(w_i)=v_2(w_j)\). Conversely if the common valuation is \(r\), every weight is \(2^r\) times an odd integer, so \(t=\pi/(4\cdot2^r)\) makes all cosines zero. For \(d\ge2\), the binary weights have unequal two-adic valuations and hence cannot have instantaneous uniformity. The all-odd sequence \(w_j=3^{j-1}\) is superincreasing, so its subset sums are distinct, and it has common two-adic valuation zero; the displayed times follow.

All steps hold for arbitrary finite \(d\) and the exact stated parameter domains.

## Verification

The companion standalone Python program `verify.py` requires only the Python standard library. Run `python3 verify.py` in the directory containing that file. Its recorded successful check is:

```
VERIFY_OK exact_profiles=21 exact_entries=5124 integer_budget_profiles=3164 finite_window_modes=88 max_midpoint_error=7.772e-16
```

It independently constructs Walsh eigenvalues from signed-zero counts and the average mixing matrix from the Hamiltonian's eigenspace projectors, compares them entrywise as exact fractions for 21 integer coupling profiles in dimensions one through five (5,124 total entries), and uses exact Gaussian elimination to verify ranks. It also examines 3,164 bounded integer profiles for the budget equality case through dimension five. A separate numerical integration corroborates finite-window averaging for 88 Walsh modes. These are finite consistency tests only; the unrestricted proof is in Steps 1–6.

## Relationship to prior work

Ce Wang, *The uniform measure for quantum walk on hypercube: a quantum Bernoulli noises approach* (2022, arXiv:2211.07948v1), proves uniform-measure results for a **discrete-time coined** hypercube walk. That model has a separate coin space and does not provide the stated weighted continuous-time Hamiltonian classification.

Moore and Russell, *Quantum Walks on the Hypercube* (2001, arXiv:quant-ph/0104137), analyze unweighted continuous-time instantaneous uniform mixing. Adamczak and coauthors, *Non-uniform mixing of quantum walk on cycles* (2007, arXiv:0708.2096), establish nonuniform *average* mixing for ordinary unweighted Abelian Cayley graphs (in Section 4 their adjacency selector takes values in \(\{0,1\}\)). The present real-weighted Hamiltonians, notably the binary weight choice with nondegenerate eigenvalues, lie outside that binary-adjacency condition and instead give exactly uniform average mixing.

Godsil, *Average Mixing of Continuous Quantum Walks* (arXiv:1103.2578), supplies the general spectral-projector Schur-square framework. Carlson and coauthors, *Universal Mixing of Quantum Walk on Graphs* (arXiv:quant-ph/0608044), study spectral obstructions to mixing. Baptista, Coutinho and Marques, *Unexpected Averages of Mixing Matrices* (2023, arXiv:2308.16378), develop Cartesian-product and averaging identities. Those methods supply a general backdrop; the result here specializes the cube to determine every signed-resonance eigenvalue, the exact finite observation windows, the uniquely minimal integer budget, and the incompatible instantaneous-mixing arithmetic in one theorem. General spectral and subset-sum ideas are not represented as new.

## Limitations

The sharp coupling budget assumes positive integers with a fixed unit; without that normalization, scaling makes any positive lower bound impossible. The finite-window time classification is asserted for integer couplings only. The average limit can converge arbitrarily slowly near small nonzero signed resonances; this theorem does not establish finite-time approximation error bounds for arbitrary irrational weights, noise robustness, or experimental feasibility of exponentially spread couplings. Replacing coherent unitary propagation with decoherence or a discrete-time coin changes the problem. While the primary comparisons found no equivalent full classification, the underlying Walsh and spectral-projector tools are standard, and a stronger already-known general theorem could imply portions of the statement; independent literature evaluation remains appropriate.

## References

1. C. Wang, *The uniform measure for quantum walk on hypercube: a quantum Bernoulli noises approach*, arXiv:2211.07948v1 (first posted 15 November 2022), https://arxiv.org/html/2211.07948v1.
2. C. Moore and A. Russell, *Quantum Walks on the Hypercube*, arXiv:quant-ph/0104137 (2001), https://arxiv.org/abs/quant-ph/0104137.
3. W. Adamczak, K. Andrew, L. Bergen, D. Ethier, P. Hernberg, J. Lin, and C. Tamon, *Non-uniform mixing of quantum walk on cycles*, arXiv:0708.2096v1 (2007), https://arxiv.org/html/0708.2096v1.
4. C. Godsil, *Average Mixing of Continuous Quantum Walks*, arXiv:1103.2578 (2011), https://arxiv.org/abs/1103.2578.
5. P. Baptista, G. Coutinho, and V. Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378v1 (2023), https://arxiv.org/html/2308.16378v1.
6. W. Carlson et al., *Universal Mixing of Quantum Walk on Graphs*, arXiv:quant-ph/0608044 (2006), https://arxiv.org/abs/quant-ph/0608044.
