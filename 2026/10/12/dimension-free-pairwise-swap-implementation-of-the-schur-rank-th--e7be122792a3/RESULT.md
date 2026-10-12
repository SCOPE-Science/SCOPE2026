# Dimension-free pairwise-SWAP implementation of the Schur rank-threshold test
## Finding
Let \(n,d\ge 2\), let \(1\le r<\min\{n,d\}\), and let \(0<\varepsilon<1\). Consider the binary coarse weak-Schur measurement on a permutation-invariant \(n\)-qudit state whose low outcome collects exactly the Young sectors with first-column length \(\lambda'_1\le r\), and whose high outcome collects those with \(\lambda'_1\ge r+1\). Define the harmonic number \(H_r=\sum_{j=1}^r j^{-1}\),
\[
A_r=(r+2)H_r-r,
\]
and
\[
M_r=\left\lceil 2nA_r+2n(r+1)\ln\!\frac{2}{\varepsilon}\right\rceil.
\]
There is a protocol using only random pairwise SWAP tests and classical control whose binary output distribution is within total variation distance \(\varepsilon\) of this ideal Schur rank-threshold measurement on every permutation-invariant input. Every execution uses at most
\[
4(r+1)M_r\ln\!\frac{6M_r}{\varepsilon}
\]
pairwise SWAP tests. In particular, the bound is independent of the ambient local dimension \(d\) and is
\[
O\!\left(nr^2\bigl(\log(r+1)+\log(1/\varepsilon)\bigr)\log(nr/\varepsilon)\right).
\]
For the usual one-sided quantum rank tester, which accepts precisely when \(\lambda'_1\le r\), this gives a dimension-free pairwise-SWAP implementation of its Schur decision stage.

## Assumptions and scope
The input is permutation invariant; in particular, \(\rho^{\otimes n}\) satisfies this condition. The result concerns the binary first-column threshold, not full weak or unitary Schur sampling and not the copy complexity needed to make a statistical rank-testing promise sound. The parameter \(r\) is a fixed decision threshold with \(r<d\) and \(r<n\).

The protocol follows only the first antisymmetric block of the growth process of Brahmachari, Jakab, Pfister, and Marvian. Starting from a one-qudit antisymmetric block of size \(k=1\), it repeatedly chooses a fresh candidate qudit uniformly from the remaining qudits and tests whether the current block plus that qudit is fully antisymmetric. On success, \(k\) increases by one. The protocol outputs high as soon as \(k=r+1\). If \(M_r\) ideal growth calls have occurred without reaching \(r+1\), it outputs low. Unlike full Schur sampling, it never needs to certify the exact bottom of a column or traverse later columns.

## Proof
Fix a Young sector \(\lambda\vdash n\), and write \(h=\lambda'_1\) for its first-column length. Brahmachari et al. prove that the largest antisymmetric subsystem obtainable in this sector by the invariant growth procedure has size exactly \(h\). Thus if \(h\le r\), the ideal growth process can never reach \(r+1\), so the ideal truncated protocol always outputs low.

Now suppose \(h\ge r+1\). While the current antisymmetric block has size \(k\le r\), the first-column specialization of the growth bound of Brahmachari et al. gives, for every admissible preceding measurement history,
\[
p_k\ge
\frac{\sum_{i=k+1}^{d}\lambda_i}{(n-k)(k+1)}.
\]
Since \(\lambda\) has at least \(h\) nonzero rows,
\[
\sum_{i=k+1}^{d}\lambda_i\ge h-k\ge r+1-k.
\]
Therefore the waiting time \(X_k\) to grow from size \(k\) to size \(k+1\) is stochastically dominated by a geometric random variable \(Z_k\) with parameter
\[
p_k^{\star}=\frac{r+1-k}{n(k+1)}.
\]
The comparison theorem for history-dependent waiting times proved in the source lets the \(Z_k\) be taken independent for the purpose of an upper-tail bound. Their total mean satisfies
\[
\sum_{k=1}^{r}\frac{1}{p_k^{\star}}
=n\sum_{k=1}^{r}\frac{k+1}{r+1-k}
=n\bigl((r+2)H_r-r\bigr)
=nA_r,
\]
while
\[
\min_{1\le k\le r}p_k^{\star}\ge \frac{1}{n(r+1)}.
\]
Applying the geometric-sum concentration inequality used in the source with tail probability \(\varepsilon/2\) yields
\[
\Pr\!\left(\sum_{k=1}^{r}X_k>M_r\right)\le \frac{\varepsilon}{2}.
\]
Hence the ideal truncated protocol disagrees with the exact first-column threshold on a fixed sector with probability at most \(\varepsilon/2\); on sectors with \(h\le r\) its error is zero. Convexity gives the same bound for every permutation-invariant mixture of sectors.

It remains to replace ideal antisymmetric measurements by pairwise SWAP tests. Every growth call acts on an already antisymmetric block plus one candidate, so at most \(r+1\) qudits participate. The antisymmetric-measurement construction of Brahmachari et al. approximates such a call to diamond error \(\eta\) using at most
\[
4(r+1)\ln\!\frac{3}{\eta}
\]
SWAP tests. Set \(\eta=\varepsilon/(2M_r)\). A standard hybrid replacement of at most \(M_r\) calls contributes at most \(M_r\eta=\varepsilon/2\) to the output-distribution distance. Adding the ideal truncation error proves the claimed total variation error \(\varepsilon\), and substituting \(\eta\) gives the displayed SWAP-test bound.

## Verification
The analytic proof uses only: the source's identification of \(\lambda'_1\) with the maximal antisymmetric subsystem, its history-uniform first-column growth lower bound, its stochastic-domination theorem, its geometric-sum tail inequality, and its pairwise-SWAP realization of a promised antisymmetric measurement. The accompanying verifier checks the harmonic identity and exhaustively checks the deterministic mean bound over all integer partitions up to size \(12\); this finite check corroborates but does not replace the all-\(n\) proof.

Run:

`python artifacts/verify.py`

The expected terminal line is `VERIFY_OK`.

## Relationship to prior work
Brahmachari, Jakab, Pfister, and Marvian give a pairwise-SWAP implementation of full unitary Schur sampling with complexity \(O(n\min\{n,d\}^3\log^2(n/\varepsilon))\). They explicitly observe that quantum rank testing needs only the first-column length and state that improving the local-dimension dependence is an interesting future direction. Their full-diagram convergence proof does not state the threshold-dependent bound above. The new point is that for a binary threshold one may omit bottom certification and every later column, then use the exact first-column mass \(h-k\) to obtain the harmonic waiting-time sum \(n((r+2)H_r-r)\). This removes the ambient dimension and saves one power of the threshold compared with applying the full-diagram bound after a direct truncation.

O'Donnell and Wright prove that the optimal one-sided rank tester performs weak Schur sampling and accepts exactly when the sampled Young diagram has at most \(r\) rows, equivalently \(\lambda'_1\le r\). Their result determines the copy complexity of rank testing, but it does not provide the pairwise-SWAP implementation or the operation count proved here. The earlier qubit random-SWAP construction is the special low-dimensional case and does not cover arbitrary thresholds \(r\) in unbounded local dimension.

## Limitations
The theorem does not reduce the number of copies required by quantum rank testing; it reduces the elementary pairwise-SWAP cost of implementing its Schur decision stage. The error guarantee is for the binary classical output on permutation-invariant inputs. No claim is made that the truncated procedure implements the full post-measurement Schur instrument or preserves the canonical multiplicity output required by unitary Schur sampling. Logarithmic factors and constants are not claimed optimal. A differently organized partial-Schur implementation could conceivably improve the pairwise-SWAP count further.

## References
1. S. Brahmachari, D. Jakab, H. D. Pfister, and I. Marvian, *Unitary Schur Sampling of Qudits via Random SWAP Tests: Hunt for Antisymmetry*, arXiv:2610.02103v1, 2026. See especially the growth bound, Young-diagram traversal analysis, pairwise-SWAP realization, and discussion of rank testing.
2. R. O'Donnell and J. Wright, *Quantum Spectrum Testing*, arXiv:1501.05028; Communications in Mathematical Physics 387 (2021), 1–75. See Section 6.1 for the one-sided rank tester.
3. S. Janson, *Tail bounds for sums of geometric and exponential variables*, Statistics & Probability Letters 135 (2018), 1–6.
