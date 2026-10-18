# Sharp collision constant for binary adjacent-pair multispectra
## Finding
Let \(X\) and \(Y\) be independent uniformly distributed binary words of the same length \(n\). For each word \(x=x_1\cdots x_n\), let \(M_2(x)\) be the **linear ordered-pair multiset** consisting of its \(n-1\) adjacent pairs \(x_ix_{i+1}\), retaining their multiplicities. Then, as \(n\to\infty\),
\[
\Pr\bigl(M_2(X)=M_2(Y)\bigr)
   =\frac{3}{4\pi n}+o(n^{-1}).
\]
Equivalently, the expected number of length-\(n\) words having the same adjacent-pair multiset as a uniformly random word, including the word itself, is
\[
\left(\frac{3}{4\pi}+o(1)\right)\frac{2^n}{n}.
\]
The coefficient \(3/(4\pi)\) is exact. Despite there being quadratically many possible profiles, their nonuniform distribution makes collisions of independent random profiles occur at order \(n^{-1}\), rather than order \(n^{-2}\).

## Assumptions and scope
The alphabet is \(\{0,1\}\). All \(2^n\) words are equiprobable and independently sampled. The adjacent-pair observation distinguishes \(01\) from \(10\) and uses consecutive positions in a **linear** word; there is no wraparound pair. The probability includes equal words. Write \(L=n-1\), and let \(a,b,c,d\) respectively count \(00,01,10,11\) occurrences. Thus \(a+b+c+d=L\). Only the regime \(n\to\infty\) is asserted for the asymptotic formula.

## Proof
**1. Reduction to two additive counts and an endpoint flag.** Let \(\delta=b-c\). Since every \(01\) transition raises the bit by one and every \(10\) transition lowers it by one, telescoping gives \(\delta=x_n-x_1\in\{-1,0,1\}\). Conversely, \(a,d,\delta,L\) determine the full profile, because \(b+c=L-a-d\), and hence
\[
 b=\frac{L-a-d+\delta}{2},\qquad
 c=\frac{L-a-d-\delta}{2}.
\]
The three values of \(\delta\) correspond respectively to endpoints \((0,1)\), equal endpoints, and endpoints \((1,0)\).

**2. Exact Fourier collision identity.** For angles \(\theta,\phi\), put \(z=e^{i\theta}\), \(w=e^{i\phi}\), and
\[
 T(z,w)=\frac12\begin{pmatrix}z&1\\1&w\end{pmatrix},\qquad
 F_{st}(\theta,\phi)=\frac12[T(z,w)^L]_{st},\quad s,t\in\{0,1\}.
\]
Each \(F_{st}\) is the joint characteristic function of \((a,d)\) with the first and last bits fixed to \((s,t)\); the initial factor \(1/2\) represents the uniformly chosen first bit. Let \(P_n=\Pr(M_2(X)=M_2(Y))\). By coefficient orthogonality on the two-dimensional integer lattice, and by grouping equal-endpoint paths under \(\delta=0\),
\[
 P_n=\frac{1}{(2\pi)^2}\int_{[-\pi,\pi]^2}
 \left( |F_{00}+F_{11}|^2+|F_{01}|^2+|F_{10}|^2\right)
 \;d\theta\,d\phi .\tag{1}
\]
This identity holds exactly for every \(n\ge2\).

**3. Identify every peripheral spectral point.** The entrywise absolute value of \(T(z,w)\) equals the stochastic irreducible matrix \(T(1,1)\), so all eigenvalues of \(T(z,w)\) have modulus at most one. If an eigenvalue has modulus one, equality in the triangle inequality in both row equations forces an eigenvector with equal coordinate moduli and, after writing its coordinates as \((u,v)\), forces \(v=zu\), \(w v=u\), and its eigenvalue to equal both \(z\) and \(1/z\). Therefore \(z=w\in\{1,-1\}\). These two points really have eigenvalues of modulus one. Away from neighborhoods of the two torus points \((1,1)\) and \((-1,-1)\), compactness gives a uniform spectral gap below one; hence the integral there is exponentially small in \(L\), up to a harmless polynomial factor.

**4. Local spectral expansion.** Near \((z,w)=(1,1)\), the dominant eigenvalue is the analytic branch
\[
 \lambda(\theta,\phi)=\frac{e^{i\theta}+e^{i\phi}
   +\sqrt{(e^{i\theta}-e^{i\phi})^2+4}}{4},
 \qquad \lambda(0,0)=1.
\]
Its logarithm has the Taylor expansion
\[
 \log\lambda=\frac{i(\theta+\phi)}4
  -\frac{5\theta^2-6\theta\phi+5\phi^2}{32}
  +O\bigl((|\theta|+|\phi|)^3\bigr).
\]
Define the positive definite matrix
\[
 \Sigma=\frac1{16}\begin{pmatrix}5&-3\\-3&5\end{pmatrix},
 \qquad\det\Sigma=\frac1{16}.
\]
Then \(|\lambda|^{2L}=\exp(-L(\theta,\phi)\Sigma(\theta,\phi)^{\mathsf T}+O(L\|(\theta,\phi)\|^3))\). At the origin the spectral projection onto the dominant eigenspace is \(\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}\). Consequently, in the central-limit scaling \((\theta,\phi)=(u,v)/\sqrt L\),
\[
 |F_{00}+F_{11}|^2+|F_{01}|^2+|F_{10}|^2
 =\left(\frac38+o(1)\right)
 \exp\bigl(-(u,v)\Sigma(u,v)^{\mathsf T}\bigr),
\]
pointwise for fixed \((u,v)\). The coefficient \(3/8=1/4+1/16+1/16\) reflects the three possible endpoint-difference classes. The spectral gap for the other eigenvalue and positivity of \(\Sigma\) provide an integrable Gaussian majorant in a sufficiently small neighborhood, so dominated convergence applies.

The second peripheral point contributes **the same** amount: with \(D=\mathrm{diag}(1,-1)\), we have \(T(-z,-w)=-D T(z,w)D\), which changes only the overall sign and off-diagonal signs of \(F_{st}\) and leaves the integrand in (1) unchanged. Each peak therefore contributes, to leading order,
\[
 \frac{1}{(2\pi)^2}\frac{3}{8L}
 \int_{\mathbb R^2}\exp\bigl(-(u,v)\Sigma(u,v)^{\mathsf T}\bigr)\,du\,dv
 =\frac{1}{(2\pi)^2}\frac{3}{8L}
 \frac{\pi}{\sqrt{\det\Sigma}}
 =\frac{3}{8\pi L}.
\]
Adding both peaks and using \(L=n-1\) proves \(P_n=3/(4\pi n)+o(n^{-1})\). Finally, if \(A(x)=|\{y:M_2(y)=M_2(x)\}|\), direct double-counting gives \(\mathbb E A(X)=2^nP_n\), proving the interpretation.

## Verification
The accompanying standalone `verify.py` enumerates every word of each length \(2\le n\le17\), groups words by literal adjacent ordered pairs, and compares each entire class-size dictionary and collision second moment with an independent positive-run-composition formula. It also checks total mass exactly at lengths \(25,50,100,200,400,800\). The finite ratios \(nP_n\) are \(0.245842430908\) at \(n=50\), \(0.240443874204\) at \(n=200\), and \(0.239156430499\) at \(n=800\), approaching \(3/(4\pi)=0.238732414638\). These checks corroborate but do not prove the infinite limit: the complete Fourier and Gaussian-localization argument above is the proof.

## Relationship to prior work
Jacquet, Knessl, and Szpankowski count **cyclic balanced Markov types**, not the collision second moment of *linear free-endpoint* binary bigram spectra. Karhumäki, Saarela, and Zamboni study \(2\)-Abelian equivalence, which retains unigram counts as well as bigram counts; our multispectrum can merge \(010\) and \(101\), whose unigram counts differ. Gabrys and Milenkovic explicitly define ordered adjacent multispectra, but their code-reconstruction analysis does not give this random collision asymptotic.

The published note *Exact binary two-multispectrum code size and singleton classification* gives the exact count of feasible binary pair spectra and a formula for **every individual ambiguity-class size**. Consequently the exact finite collision probability can in principle be written as a sum of squares of its class-size formula; that prior classification is not being claimed as new. The present assertion is the sharp asymptotic evaluation of that global second moment, including the leading constant, requiring the two-peak Fourier analysis above. This logical dependence is a residual priority risk: an unstated derivation of the same asymptotic from those counts may exist. The comparison is to scientific implications, not merely titles.

## Limitations
Only i.i.d. fair binary words and complete linear ordered-bigram multispectra are covered. The calculation does not provide an error term stronger than \(o(n^{-1})\), a general biased-source or larger-alphabet formula, or an audit by an independent researcher. The published class-size formulas imply a finite sum representation of the collision probability, and unindexed Markov-type literature could conceivably have evaluated its asymptotic; the current literature comparison does not rule out such sources.

## References
1. P. Jacquet, C. Knessl, W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM (public source dated 2009-12-31), DOI:10.46298/dmtcs.2768, https://dmtcs.episciences.org/en/articles/2768 .
2. J. Karhumäki, A. Saarela, L. Q. Zamboni, *On a generalization of Abelian equivalence and complexity of infinite words*, arXiv:1301.5104v1 (first posted 2013-01-22), https://arxiv.org/abs/1301.5104 .
3. R. Gabrys, O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548v1 (2018-04-12), https://arxiv.org/abs/1804.04548 .
4. *Exact binary two-multispectrum code size and singleton classification*, published research note, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-binary-two-multispectrum-code-size-and-singleton-classific--13779c08da71 .
