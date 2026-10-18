# Complete dyadic exponential spectra of the finite parabola

## Finding
For each integer \(k\ge1\), put \(q=2^k\), \(R_k=\mathbb Z/q\mathbb Z\), and
\[
E_k=\{(x,x^2):x\in R_k\}\subset R_k^2.
\]
An exponential spectrum is an unordered set \(\Lambda\subset R_k^2\) of \(q\) distinct frequency pairs such that the restricted characters
\[
\phi_{u,v}(x)=q^{-1/2}\exp\!\left(\frac{2\pi i(ux+vx^2)}q\right),
\qquad (u,v)\in\Lambda,
\]
form an orthonormal basis of complex-valued functions on \(E_k\).

**Complete recursive classification.** At level \(k=1\), the spectra consist of any one frequency pair with \(u+v\) even and any one with \(u+v\) odd, producing precisely four spectra. For \(k\ge2\), every spectrum is uniquely expressible as
\[
\boxed{\Lambda=\bigcup_{\epsilon=0}^{1}\{(\epsilon+2a,c_\epsilon+2b):(a,b)\in\Lambda_\epsilon\},}
\]
where \(c_0,c_1\in\{0,1\}\) are independently chosen, and each \(\Lambda_\epsilon\) is an arbitrary spectrum for \(E_{k-1}\). Conversely, each such choice produces a spectrum. All coordinates are interpreted modulo their respective powers of two.

In particular, the exact number of **distinct unordered frequency sets**, without identifying translates or affine images, is
\[
\boxed{\mathcal N_k=2^{2^{k+1}-2}}\qquad(k\ge1).
\]
The first three counts are \(4\), \(64\), and \(16384\). Every finite pairwise-orthogonal collection of restricted characters is contained in a complete exponential spectrum for the same \(E_k\).

## Assumptions and scope
All Fourier frequencies range over the full dual group \(R_k^2\). The spatial set has \(q\) points because the first coordinate is \(x\); the norm of the restricted characters is one. A spectrum is a set rather than an ordered basis, and two different sets of frequency pairs are counted separately even if related by a group action. The classification is valid for every integer exponent \(k\ge1\), including the degenerate-to-linear base case \(k=1\). No assertion is made for odd moduli or polynomial graphs of other degrees.

## Proof
**1. Exact Fourier zeros at every dyadic scale.** Define
\[
G_k(U,V)=\sum_{x\bmod2^k}\exp\!\left(\frac{2\pi i(Ux+Vx^2)}{2^k}\right).
\]
At \(k=1\), the two terms give \(G_1(U,V)=1+(-1)^{U+V}\), hence \(G_1(U,V)=0\) exactly when \(U+V\) is odd.

Suppose \(k\ge2\) and write \(q=2^k\). The translation \(x\mapsto x+q/2\) fixes \(x^2\pmod q\) but contributes the factor \((-1)^U\) to the linear character. Thus \(G_k(U,V)=0\) whenever \(U\) is odd. If \(V\) is odd, compute the squared modulus by substituting the difference \(h=x-y\):
\[
|G_k(U,V)|^2=\sum_{h\bmod q}e_q(Uh+Vh^2)
\sum_{y\bmod q}e_q(2Vhy),
\qquad e_q(t)=\exp(2\pi i t/q).
\]
The inner sum is \(q\) exactly when \(h\equiv0\pmod{q/2}\), and otherwise zero. Since \(k\ge2\), \((q/2)^2\equiv0\pmod q\), so
\[
|G_k(U,V)|^2=q(1+(-1)^U).
\]
In particular, if \(U\) is even and \(V\) is odd then \(|G_k(U,V)|^2=2q>0\). Finally, if both \(U\) and \(V\) are even, reduction modulo \(q/2\) gives
\[
G_k(U,V)=2G_{k-1}(U/2,V/2).
\]
These three cases exhaust all input pairs. Their recurrence is an exact zero/nonzero criterion, not an asymptotic Gauss-sum bound.

**2. Orthogonal basis blocks.** Two distinct restricted characters at frequencies \((u,v)\) and \((u',v')\) are orthogonal precisely when \(G_k(u-u',v-v')=0\). For \(k\ge2\), consider translation by \(q/2\) on functions of \(x\). Each \(\phi_{u,v}\) is an eigenvector with eigenvalue \((-1)^u\). The \(+1\) and \(-1\) eigenspaces have equal dimension \(q/2\): the permutation exchanges the two points in each pair \(\{x,x+q/2\}\).

An orthogonal basis must therefore have exactly \(q/2\) frequencies with even \(u\), and exactly \(q/2\) with odd \(u\). Within a fixed parity of \(u\), the Fourier-zero criterion above rules out any pair with different parities of \(v\): its difference would have even first coordinate and odd second coordinate and its inner product would be nonzero. Accordingly every frequency in the even-\(u\) block has the same second-coordinate parity \(c_0\), and every one in the odd-\(u\) block has parity \(c_1\).

Every frequency in block \(\epsilon\) consequently has a *unique* representation \((\epsilon+2a,c_\epsilon+2b)\), where \((a,b)\in R_{k-1}^2\). The common parity factors disappear from the difference, and the reduction identity for \(G_k\) shows that the \(q/2\) reduced pairs are pairwise orthogonal exactly when they form a spectrum at level \(k-1\). Conversely, choose any two smaller spectra and any two parities; within each block the reduced orthogonality holds, and all cross-block inner products vanish because their first-coordinate difference is odd. There are \(q\) frequencies, so the resulting orthonormal family is a basis. The parity blocks, their second-coordinate parities, and the reduced sets are uniquely determined by the resulting frequency set. This completes the classification by induction.

**3. Exact counting.** At \(k=1\), two even-sum and two odd-sum frequency pairs offer \(2\cdot2=4\) spectra. For \(k\ge2\), the two \(c\)-bits and the two independently chosen smaller spectra yield the exact recurrence
\[
\mathcal N_k=4\mathcal N_{k-1}^{2}.
\]
Writing \(\mathcal N_k=2^{a_k}\), we get \(a_1=2\) and \(a_k=2+2a_{k-1}\). Solving gives \(a_k=2^{k+1}-2\). No overcounting occurs because Step 2 constructs an invertible parametrization.

**4. Extension of all orthogonal subfamilies.** A partial pairwise-orthogonal family separates by first-coordinate parity. In either nonempty parity block containing at least two frequencies, the second-coordinate parity is forced by the nonvanishing case of Step 1; if it contains just one frequency, its second-coordinate parity is known; if it is empty, either parity may be chosen. Dividing the two coordinates of each nonempty block as in Step 2 produces a smaller pairwise-orthogonal family. The base case \(k=1\) extends every orthogonal subfamily by taking one frequency of each sum parity. Apply the induction hypothesis independently to the two reduced blocks, then lift them by the chosen \(c\)-bits. The resulting complete spectrum contains every original frequency. This proves the extension assertion.

## Verification
The standalone Python 3 checker `check_dyadic.py` makes Fourier-zero decisions independently using the exact cyclotomic polynomial \(\Phi_{2^k}(X)=X^{2^{k-1}}+1\). For each frequency pair, it compares the number of occurrences of exponents separated by \(2^{k-1}\). It checks all \(21844\) pairs of coefficients for \(1\le k\le7\). It also builds exact orthogonality graphs for \(k=1,2,3\) and enumerates **all maximal cliques** using an independent bitset search, obtaining only full spectra, with counts \(4,64,16384\); this exhaustively verifies \(16452\) maximal cliques for those three sizes. Run `python3 check_dyadic.py` and compare with `check_output.txt`. The infinite-family theorem follows from the proof, not these finite tests.

## Relationship to prior work
Hickman and Wright study Fourier restriction over modular rings and include arithmetic Fourier analysis of parabolas, but the investigated restriction estimates do not classify the orthogonal frequency bases of the dyadic parabola or count them. Frederick and Mayeli provide constructions and transfer results for frame spectral pairs, without an exact dyadic quadratic-frequency basis census. Gabardo, Lai, and Oussa study exponential bases with nonlinear phase functions in a general harmonic-analytic framework, not this complete finite-ring classification. A complete spectrum theorem for parabola graphs over **odd** prime powers explicitly assumes odd characteristic and does not entail the displayed characteristic-two recursion. The existing sharp dyadic parabola fourth-moment result calculates an extension norm, not the discrete spectral partners; its proof does not imply the classification here. The new result is the complete characteristic-two orthogonal-basis theorem, exact enumeration, and extension of all partial families, rather than the elementary parity cancellation in isolation.

## Limitations
The classification concerns the standard dyadic quadratic graph only, not its arbitrary perturbations, arbitrary spectral sets, or other moduli. It does not classify spectra modulo isometries or other group actions. The arithmetic zero test is elementary, but the asserted novelty of the full tree classification remains subject to older literature in finite Butson–Hadamard matrices or modular chirp orthogonality. All numerical checks are finite, and no independent mathematical audit has been performed.

## References
- Jonathan Hickman and James Wright, *The Fourier restriction and Kakeya problems over rings of integers modulo N*, arXiv:1801.03176v1, first public 2018-01-09, https://arxiv.org/abs/1801.03176.
- C. Frederick and A. Mayeli, *Frame spectral pairs and exponential bases*, arXiv:2010.05667, first public 2020-10-12, https://arxiv.org/abs/2010.05667.
- Jean-Pierre Gabardo, Chun-Kit Lai, and Vignon Oussa, *On exponential bases and frames with non-linear phase functions and some applications*, arXiv:2007.03736, first public 2020-07-07, https://arxiv.org/abs/2007.03736.
- *Complete exponential spectra of the parabola over odd prime-power rings*, published mathematical result (2026), odd-prime spectral classification.
- *Parity-sharp fourth moments of the dyadic quadratic graph*, published mathematical result (2026), exact dyadic restriction norm.
