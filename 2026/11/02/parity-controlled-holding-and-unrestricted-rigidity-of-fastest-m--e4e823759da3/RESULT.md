# Parity-controlled holding and unrestricted rigidity of fastest mixing on discrete tori

## Finding

For every integer \(d\ge1\) and every tuple of cycle lengths \(n_1,\ldots,n_d\ge3\), the symmetric fastest-mixing Markov chain supported on the Cartesian product \(G=C_{n_1}\square\cdots\square C_{n_d}\), with allowed self-loops, is **unique even without any translation-invariance assumption**. Define
\[
c_j=2-2\cos(2\pi/n_j),\quad
L_j=2-2\cos\bigl(2\pi\lfloor n_j/2\rfloor/n_j\bigr),\quad
H=\sum_{j=1}^d\frac{2}{c_j},\quad E=\sum_{j=1}^d\frac{L_j}{c_j},\quad
\tau=\min\left\{\frac{2}{E+1},\frac1H\right\}.
\]
The unique minimizer puts probability \(\tau/c_j\) on **each** of the two cycle-neighbor transitions in direction \(j\) and probability \(1-\tau H\) on the self-loop at every state. Its optimal nonconstant second-largest eigenvalue modulus is
\[
\boxed{\mu_*(G)=1-\tau.}
\]
Let \(k=|\{j:n_j\text{ is odd}\}|\). The optimal holding probability is strictly positive if and only if **\(k\le2\), or \(k=3\) and at least one of the three odd lengths is greater than \(3\)**. It is exactly zero for \(k\ge4\), or for precisely three odd factors all of length \(3\), regardless of the number or lengths of the other even factors.

## Assumptions and scope

Each cycle \(C_{n_j}\) has vertices \(\mathbb Z/n_j\mathbb Z\) and two distinct neighbors \(x_j\pm1\) because \(n_j\ge3\). The torus vertex set is \(V=\prod_j\mathbb Z/n_j\mathbb Z\), of cardinality \(N=\prod_j n_j\). Admissible matrices \(P\in\mathbb R^{N\times N}\) are symmetric, entrywise nonnegative and stochastic: \(P\mathbf1=\mathbf1\); off-diagonal entries vanish off graph edges. Self-loops are permitted but not required. No individual edge probability is constrained to be equal to any other. For the rank-one stationary projector \(J=\mathbf1\mathbf1^\mathsf T/N\), the minimized objective is \(\mu(P)=\|P-J\|_2\), the SLEM on the subspace orthogonal to constants.

The focal source is the publicly dated arXiv version of Boyd, Diaconis, Parrilo and Xiao (2007); an earlier technical-report incarnation is listed with month-level (May 2007) rather than verified day-level public dating. The first-public-date field identifies the dated arXiv version, not an assertion that no earlier version existed.

## Proof

**1. Symmetry reduction without a uniqueness assumption.** The operator norm \(P\mapsto\|P-J\|_2\) is convex and is unchanged by graph automorphisms. Averaging any feasible \(P\) over all independent coordinate translations and reversals produces a feasible matrix \(\bar P\) with no larger SLEM. Each coordinate direction is a separate edge orbit under this subgroup. Consequently \(\bar P\) has one nonnegative edge probability \(a_j\) per direction and holding probability \(1-2\sum_j a_j\ge0\). In particular, a globally optimal matrix exists of this form, but this observation alone does *not* prove uniqueness among all admissible matrices.

**2. Complete Fourier spectral reduction.** The cycle Laplacian eigenvalues are \(2-2\cos(2\pi k/n_j)\), with smallest positive value \(c_j\) and largest value \(L_j\). For \(\bar P\), the eigenvalues indexed by frequency vectors \((k_1,\ldots,k_d)\) are
\[
\lambda_{\boldsymbol k}=1-\sum_{j=1}^d a_j\bigl(2-2\cos(2\pi k_j/n_j)\bigr).
\]
Let \(t=\min_j a_j c_j\). The largest eigenvalue on nonconstant modes is exactly \(1-t\), and the smallest is \(1-\sum_j a_j L_j\). Hence
\[
\mu(\bar P)=\max\left\{1-t,\sum_j a_j L_j-1\right\},\quad
0\le t\le H^{-1},\quad \sum_j a_j L_j\ge tE.
\]
It follows that \(\mu(\bar P)\ge\max\{1-t,Et-1\}\). This two-line piecewise-linear function decreases up to the intersection \(t=2/(E+1)\) and increases thereafter. Over \([0,H^{-1}]\), its unique minimizing value is \(t=\tau\). Choosing \(a_j=\tau/c_j\) respects \(2\sum_j a_j=H\tau\le1\) and attains both the relevant extremal eigenvalue constraints, proving \(\mu_*=1-\tau\).

Moreover this is the **unique translation-and-reversal-invariant optimizer**: when \(\tau=H^{-1}\), the stochastic budget forces every \(a_j=\tau/c_j\); when \(\tau<H^{-1}\), both spectral branches are tight, so increasing any \(a_j\) beyond \(\tau/c_j\) would make \(\sum_j a_jL_j-1>\mu_*\).

**3. Saturated Fourier characters force every individual edge.** Let \(P\) be any unrestricted global optimizer. Its group average equals the unique invariant optimizer above. For each coordinate \(j\), define \(f_j(x)=\exp(2\pi i x_j/n_j)\), a nonconstant Fourier character. The identity for weighted graph Laplacian quadratic forms, together with the edge orbit total of the averaged matrix, gives
\[
\frac{f_j^*Pf_j}{\|f_j\|_2^2}
=1-c_j a_j=1-\tau=\mu_*.
\]
Since \(f_j\perp\mathbf1\) and \(\mu(P)=\mu_*\), the Hermitian matrix \(\mu_*I+J-P\) is positive semidefinite and has zero quadratic form on \(f_j\). Therefore \(Pf_j=\mu_*f_j\).

At vertex \(x\), denote the probabilities on the two edges \(x\to x\pm e_j\) by \(w_j^\pm(x)\). The eigenvector identity becomes
\[
(1-e^{2\pi i/n_j})w_j^+(x)
+(1-e^{-2\pi i/n_j})w_j^-(x)=\tau.
\]
Its imaginary part, using \(\sin(2\pi/n_j)\ne0\) for \(n_j\ge3\), forces \(w_j^+(x)=w_j^-(x)\). Its real part then gives \(c_j w_j^+(x)=\tau\). Thus every original edge probability is \(\tau/c_j\), for every vertex and direction. Row sums force the same diagonal \(1-\tau H\). This proves **unrestricted uniqueness**, including at zero-holding boundaries.

**4. Parity-only holding frontier.** The holding value \(1-H\tau\) is positive exactly when \(2H<E+1\), or
\[
\sum_j\frac{4-L_j}{c_j}<1.
\]
For even \(n_j\), \(L_j=4\), so the contribution is zero. For odd \(n_j\ge3\), \(L_j=2+2\cos(\pi/n_j)\), and elementary double-angle identities give
\[
\frac{4-L_j}{c_j}=\frac1{4\cos^2(\pi/(2n_j))}
\in(1/4,1/3],
\]
with equality at the upper endpoint only for \(n_j=3\). At most two odd factors contribute less than one. Three contribute at most one and reach one only for three triangles. Four or more contribute strictly more than one. This is precisely the holding classification stated above.

## Verification

The included `verify_torus.py` computes the exact defining trigonometric quantities, enumerates Fourier eigenvalues and compares them with full transition-matrix eigenspectra for small examples. It independently solves the symmetrized linear program and tests the Fourier eigenvector equations, including zero-holding cases. Run `python verify_torus.py` with Python 3 and NumPy/SciPy installed. It passed **3,138 assertions on 28 graph shapes**. These finite checks are supplementary: the proof above, not finite enumeration or the solver, establishes the all-size unrestricted statement.

For an exact boundary illustration, on \(C_3\square C_3\square C_3\) the transition probability in each edge direction is \(1/6\), holding is zero, and \(\mu_*=1/2\). On four copies of \(C_3\), each edge probability is \(1/8\), holding is zero, and \(\mu_*=5/8\). Replacing one of three triangular factors by \(C_5\) makes the optimum hold with strictly positive probability.

## Relationship to prior work

Boyd, Diaconis and Xiao (2004) formulate fastest symmetric Markov mixing as a convex semidefinite optimization problem, but do not give this torus classification. Boyd, Diaconis, Parrilo and Xiao (2007), §§2–3, establish automorphism averaging and Cartesian-product Laplacian spectra, and derive an explicit optimum for **two identical cycle factors** \(C_n\square C_n\), as well as homogeneous Hamming graphs. Those results are **prior coverage of the corresponding special cases**, not new claims here. In contrast, the present statement treats arbitrary independent cycle lengths and arbitrarily many factors, gives an explicit holding frontier depending only on odd-factor count, and proves that no nonsymmetric edge assignment can tie the optimal value. The original source's statement that graph products can be analyzed using its methods does not supply this general independent-direction solution or edgewise rigidity proof.

## Limitations

The claim is for real symmetric stochastic chains with **uniform** stationary law and nearest-neighbor/self-loop support. It does not claim optimization over directed/nonreversible kernels, auxiliary lifted chains, nonuniform stationary measures, time-varying kernels, or total-variation mixing at a fixed finite number of steps. The date attached to the arXiv focal source is a verified precise release date; an earlier May 2007 technical report exists without a verified release day in the consulted material. The literature comparison cannot exclude every unpublished or poorly indexed equivalent formula. No independent mathematical audit is claimed.

## References

1. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689. DOI: https://doi.org/10.1137/S0036144503423264 ; public PDF: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf .
2. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1 (precise public date 2007-09-06), https://arxiv.org/pdf/0709.0955 ; see especially §§2, 3.1–3.3. An earlier MSR-TR-2007-52 technical-report version is catalogued as May 2007 without a verified day.
