# Sharp collision constant for binary adjacent-pair spectra
## Finding
For a binary word \(w=w_1\cdots w_n\), let \(M_2(w)\) denote the multiset of its \(n-1\) contiguous ordered pairs. Let \(U_n,V_n\) be independent, uniformly distributed on \(\{0,1\}^n\). For every integer \(n\ge2\), define
\[
P_n=\Pr\bigl(M_2(U_n)=M_2(V_n)\bigr).
\]
Then
\[
\boxed{\displaystyle\lim_{n\to\infty}nP_n=\frac{3}{4\pi}.}
\]
In particular \(P_n\sim 3/(4\pi n)\), and the collision (Rényi-2) entropy of the observed spectrum is
\[
-\log_2 P_n=\log_2 n+\log_2(4\pi/3)+o(1).
\]
This is a probability over two independent words, *not* the probability that one randomly chosen word is uniquely reconstructible.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\). Reads are linear, contiguous, of length two, ordered internally, and observed with multiplicities. Neither endpoint is separately observed. Equality of spectra means equality of all four multiplicities \(c_{00},c_{01},c_{10},c_{11}\), not equality merely of the numbers of mixed reads. The limit uses uniform independent binary words of the same length.

Put \(N=n-1\). Let \(A(w)=c_{00}(w)\), \(B(w)=c_{11}(w)\), and \(\delta(w)=w_n-w_1\in\{-1,0,1\}\). The elementary flow identity gives \(c_{01}-c_{10}=\delta\), whereas \(c_{01}+c_{10}=N-A-B\). Consequently two words have the same spectrum if and only if their triples \((A,B,\delta)\) coincide.

## Proof
Use angles \((\theta,\phi)\in[-\pi,\pi]^2\) and the complex matrix
\[
T(\theta,\phi)=\frac12\begin{pmatrix}e^{i\theta}&1\\1&e^{i\phi}\end{pmatrix}.
\]
The matrix-weighted sum of probabilities for the transitions of a uniform word is \(T^N\), with initial-bit probability \(1/2\). Thus the joint Fourier transforms of \((A,B)\), for the three disjoint values of \(\delta\), are
\[
G_0=\tfrac12\operatorname{tr}(T^N),\qquad
G_1=\tfrac12(T^N)_{01},\qquad G_{-1}=\tfrac12(T^N)_{10}.
\]
By discrete Fourier orthogonality (Parseval for finitely supported integer distributions), independence gives the *exact* identity
\[
P_n=\frac1{(2\pi)^2}\int_{[-\pi,\pi]^2}\bigl(|G_0|^2+|G_1|^2+|G_{-1}|^2\bigr)\,d\theta\,d\phi.
\]
The matrix is symmetric, so the last two summands are equal.

We locate every unit-modulus eigenvalue of \(T\). Its entrywise absolute value is the rank-one stochastic matrix with all entries \(1/2\), so its spectral radius is at most one. If an eigenvalue has modulus one, equality in both rowwise triangle inequalities forces an eigenvector with two equal-modulus entries, their ratio equal to the eigenvalue, the reciprocal ratio equal to the same eigenvalue, and both diagonal phases equal to that eigenvalue. Therefore the eigenvalue is \(1\) at \((\theta,\phi)=(0,0)\), or \(-1\) at \((\pi,\pi)\), modulo \(2\pi\); there are no other unit-modulus points. Outside fixed neighborhoods of these points, the matrix powers are uniformly exponentially small.

Near the origin the simple dominant eigenvalue and its analytic spectral projector are \(\lambda\) and \(\Pi\). Direct diagonalization yields
\[
\lambda=\frac{e^{i\theta}+e^{i\phi}+\sqrt{(e^{i\theta}-e^{i\phi})^2+4}}4.
\]
The square-root branch equals \(2\) at the origin. Expanding the logarithm gives
\[
\log\lambda=\frac{i(\theta+\phi)}4
-\frac12(\theta,\phi)\Sigma(\theta,\phi)^{\mathsf T}
+O((|\theta|+|\phi|)^3),
\qquad
\Sigma=\frac1{16}\begin{pmatrix}5&-3\\-3&5\end{pmatrix}.
\]
Both eigenvalues of \(\Sigma\) are positive, and \(\det\Sigma=1/16\). At zero, \(\Pi=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}\); hence the leading amplitudes of \((G_0,G_1,G_{-1})\) are \((1/2,1/4,1/4)\lambda^N\). Their squared absolute values sum to \(3|\lambda|^{2N}/8\).

The second peak is congruent to the first: with \(D=\operatorname{diag}(1,-1)\),
\[
T(\pi+\theta,\pi+\phi)=-D T(\theta,\phi)D.
\]
This changes only signs of the three Fourier transforms, leaving their squared moduli unchanged. Thus both peaks contribute equally. Analyticity, the positive-definite quadratic form, and the strict spectral gap away from the peaks permit dominated Gaussian rescaling \((\theta,\phi)=N^{-1/2}(x,y)\). For each peak,
\[
\int_{\mathbb R^2} e^{-N (\theta,\phi)\Sigma(\theta,\phi)^{\mathsf T}}\,d\theta\,d\phi
=\frac\pi{N\sqrt{\det\Sigma}}=\frac{4\pi}{N}.
\]
Consequently
\[
P_n=2\cdot\frac1{(2\pi)^2}\cdot\frac38\cdot\frac{4\pi}{N}
+o(N^{-1})=\frac3{4\pi(n-1)}+o(n^{-1}).
\]
The stated limit and entropy formula follow.

## Verification
There is also an exact all-length integer expression. For \(N=n-1\), write
\[
L_{a,b,t}=\binom{a+t}{t}\binom{b+t-1}{t-1}+\binom{a+t-1}{t-1}\binom{b+t}{t},\quad t\ge1,
\]
\[
R_{a,b,t}=\binom{a+t}{t}\binom{b+t}{t},\quad t\ge0.
\]
Positive-run compositions give the number of words in a spectrum with \(c_{01}=c_{10}=t\) as \(L_{a,b,t}\), and with \(c_{01}=t+1,c_{10}=t\) (or the reversed imbalance) as \(R_{a,b,t}\). The two constant-word profiles have size one. Therefore the exact collision count is
\[
4^nP_n=2+
\sum_{t=1}^{\lfloor N/2\rfloor}\sum_{a+b=N-2t}L_{a,b,t}^{\,2}
+2\sum_{t=0}^{\lfloor (N-1)/2\rfloor}\sum_{a+b=N-2t-1}R_{a,b,t}^{\,2},
\]
with both inner sums over nonnegative integers. The separate verification program directly enumerates binary words, independently performs a transfer dynamic program indexed by endpoints and loop counts, and evaluates this binomial sum. All agree through length sixteen. At lengths \(60,100,160\), the respective values of \(nP_n\) are approximately \(0.2446063,0.2421977,0.2408783\), consistent with the proved limit \(3/(4\pi)\approx0.2387324\). The finite tests are not used as an infinite proof.

Reproduce with `python3 verify.py` using the standard library.

## Relationship to prior work
Gabrys and Milenkovic (2018) define exactly the linear ordered multiset substring spectrum and reconstruction-code setting. Their inspected paper focuses on encoded reconstruction with longer reads, not collision asymptotics for independently sampled words with read length two. Jacquet, Knessl and Szpankowski (2010) study counts of cyclic Markov types, rather than the probability that two independent linear strings share a type.

A published exact count and individual-fiber formula for binary two-multispectra already determine all the finite summands above in principle. The present claim is **not** that those fiber sizes are newly derived: the new quantitative statement is their aggregated probabilistic collision law with the explicit leading constant \(3/(4\pi)\). Establishing it requires accounting for endpoint-flow classes, lattice parity and both Fourier unit-modulus points. An equivalent earlier asymptotic may exist in unindexed Markov-type or information-spectrum literature.

## Limitations
The result covers independent *uniform* binary words with complete ordered adjacent-pair multispectra. It does not cover nonuniform Markov or iid sources, missing/noisy reads, larger alphabets, unordered pair compositions, cyclic words, or longer-read spectra. It does not give a sharp rate of convergence beyond the displayed \(o(n^{-1})\). Mathematical review here is not independent validation.

## References
1. R. Gabrys and O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548v1 (12 April 2018), revised 2019.
2. P. Jacquet, C. Knessl and W. Szpankowski, *Counting Markov Types*, Discrete Mathematics & Theoretical Computer Science proceedings (2010), DOI: 10.46298/dmtcs.2768.
3. *Exact binary two-multispectrum code size and singleton classification*, publicly available result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-binary-two-multispectrum-code-size-and-singleton-classific--13779c08da71.
4. *Exact binary length-limited composition reconstruction*, publicly available result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-binary-r-2-length-limited-composition-reconstruction--a98561a7f27e (a different, unordered-read model).
