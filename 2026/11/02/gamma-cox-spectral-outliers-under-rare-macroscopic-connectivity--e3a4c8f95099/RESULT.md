# Gamma–Cox spectral outliers under rare macroscopic connectivity in Pólya threshold graphs

## Finding

Consider the Pólya threshold graph defined below, with fixed urn parameters \(a,b>0\). Let \(\kappa_n\) be the second-smallest eigenvalue of its ordinary graph Laplacian, and let \(k_n\in\{1,\ldots,n-1\}\) satisfy \(k_n/n\to\theta\in(0,1)\). Condition on the rare high-connectivity event \(E_n=\{\kappa_n\ge k_n\}\). Then:

1. The event probability has the sharp power law
   \[
   \Pr(E_n)=\frac{(a)_{k_n}}{(a+b)_{k_n}}
   \sim\frac{\Gamma(a+b)}{\Gamma(a)}(\theta n)^{-b}.
   \]
2. There is a latent \(Y\sim\operatorname{Gamma}(b,\text{rate }\theta)\) such that the locations \(j/n\) of non-universal vertices, excluding the first creation vertex, converge jointly with \(n(1-P)\) to a Cox point process on \([0,1-\theta]\), conditionally Poisson with intensity \(Y\,dx\). The corresponding nonzero *defect-mode* Laplacian eigenvalues divided by \(n\) converge to the reflected Cox process on \([\theta,1]\). Every other nonzero eigenvalue is asymptotically at \(1\) after division by \(n\).
3. The limiting number of defect eigenvalues is negative binomial:
   \[
   \Pr(M=m)=\frac{(b)_m}{m!}\,\theta^b(1-\theta)^m,
   \qquad m=0,1,2,\ldots.
   \]
4. The conditioned normalized algebraic connectivity converges to \(V_\theta\) with
   \[
   \Pr(V_\theta\ge s)=\left(\frac{\theta}{s}\right)^b
   \quad(\theta\le s<1),
   \qquad\Pr(V_\theta=1)=\theta^b.
   \]
   Thus \(V_\theta\) has density \(b\theta^b s^{-b-1}\) on \((\theta,1)\) and an atom at \(1\), representing a complete graph. The conditional limiting law depends on \(b\) and \(\theta\) but not on \(a\); \(a\) remains in the sharp probability prefactor.

Here \((x)_r=x(x+1)\cdots(x+r-1)\) and \((x)_0=1\). The Cox-process convergence is weak convergence of finite point measures; the count and gap conclusions are part of the same rare-event spectral-structure theorem.

## Assumptions and scope

Take initial red and black urn masses \(R>0\) and \(B>0\), with reinforcement \(\Delta>0\), and write \(a=R/\Delta\), \(b=B/\Delta\). At times \(j=1,\ldots,n\), the classic two-color Pólya urn generates \(Z_j\in\{0,1\}\), with red coded as \(1\). Add vertex \(j\); for distinct \(i<j\), the edge \(\{i,j\}\) is present exactly when \(Z_j=1\). As in the source's loop-inclusive model, self-loop indicators may also be recorded, but they cancel in the Laplacian. Hence the ordinary loopless graph Laplacian and the source's Laplacian \(D-A\) coincide.

A standard Pólya/de Finetti representation gives a random \(P\sim\operatorname{Beta}(a,b)\), conditional on which the \(Z_j\) are independent Bernoulli-\(P\). The event \(E_n\) is imposed on the *unconditioned* Pólya graph law, not on a graph already conditioned on its last vertex being universal. This distinction matters for the first prefactor.

Let \(L_n\) be the \(n\)-vertex Laplacian and let \(\kappa_n=\lambda_2(L_n)\), with ordered eigenvalues \(0=\lambda_1\le\lambda_2\le\cdots\le\lambda_n\). Set
\[
N_n=n-k_n-1,\qquad
\Xi_n=\sum_{j=2}^{n-k_n}(1-Z_j)\delta_{j/n},\qquad
\Omega_n=\sum_{j=2}^{n-k_n}(1-Z_j)\delta_{\lambda_j^*/n},
\]
where the unsorted, creation-indexed eigenvalues are
\[
\lambda_j^*=jZ_j+\sum_{\ell=j+1}^n Z_\ell\quad(2\le j\le n).
\]
The notation \(\lambda_j^*\) does not assert that \(j\) is its rank in the ordered spectrum. Under \(E_n\), \(\Omega_n\) records precisely the eigenvalue modes corresponding to zero creation bits. All time parameters, spatial coordinates and asymptotics in the theorem are deterministic; no random choice of conditioning threshold is made.

## Proof

### 1. Deterministic gap identity and conditioning event

The exact Laplacian eigenbasis and eigenvalues are given in Theorem 4 of Yu–Alajaji–Gharesifard (2026). They can also be checked by applying the Laplacian to the orthogonal vectors supported on the first \(j\) vertices with coordinates \((1,\ldots,1,-(j-1),0,\ldots,0)\). The associated eigenvalue is \(\lambda_j^*\) above; the remaining eigenvalue is \(0\).

If \(Z_n=0\), the final vertex is isolated and \(\kappa_n=0\). If \(Z_n=1\), let \(j_*\) be the largest index in \(\{2,\ldots,n-1\}\) with \(Z_{j_*}=0\), if one exists. Since every creation bit after \(j_*\) equals one, \(\lambda_{j_*}^*=n-j_*\). Every earlier zero index has at least these later universal vertices and hence eigenvalue at least \(n-j_*\); every one index has an additional positive own-index term, while later one indices give eigenvalue \(n\). Consequently
\[
\kappa_n=\begin{cases}
 n-j_*,&j_*\text{ exists},\\
 n,&\text{all }Z_2,\ldots,Z_n\text{ equal }1.
\end{cases}
\]
For every integer \(1\le k\le n-1\), therefore,
\[
\{\kappa_n\ge k\}=\{Z_{n-k+1}=\cdots=Z_n=1\}.
\]
The last identity includes the complete-graph exceptional value \(\kappa_n=n\), rather than incorrectly assigning it \(n-1\).

### 2. Rare probability and Gamma posterior

Conditionally on \(P\), the event \(E_n\) has probability \(P^{k_n}\). Beta integration yields the exact mass
\[
\Pr(E_n)=\mathbb E[P^{k_n}]
=\frac{B(a+k_n,b)}{B(a,b)}
=\frac{(a)_{k_n}}{(a+b)_{k_n}}.
\]
Using \(\Gamma(x+b)/\Gamma(x)\sim x^b\) at large \(x\) gives the displayed sharp asymptotic.

Bayes' rule shows
\[
P\mid E_n\sim\operatorname{Beta}(a+k_n,b).
\]
Put \(Y_n=n(1-P)\). Its conditional density is
\[
 f_n(y)=\frac{n^{-b}}{B(a+k_n,b)}
 y^{b-1}(1-y/n)^{a+k_n-1}\,\mathbf 1_{(0,n)}(y).
\]
For fixed \(y>0\), the coefficient tends to \(\theta^b/\Gamma(b)\) and the remaining power tends to \(e^{-\theta y}\). Moreover \(\mathbb E[Y_n\mid E_n]=nb/(a+b+k_n)\to b/\theta\), so the family is tight; the density limit is the Gamma probability density. Hence
\[
Y_n\mid E_n\Rightarrow Y,\qquad
f_Y(y)=\frac{\theta^b}{\Gamma(b)}y^{b-1}e^{-\theta y},\quad y>0.
\]

### 3. Sparse-defect Cox-process convergence

Given \(P\) and \(E_n\), the unconditioned prefix variables \(Z_2,\ldots,Z_{n-k_n}\) remain independent Bernoulli-\(P\); they are not fixed by the suffix event. Let \(f\ge0\) be continuous on \([0,1]\). Conditional on \(Y_n\),
\[
\mathbb E\left[e^{-\langle f,\Xi_n\rangle}\mid Y_n,E_n\right]
=\prod_{j=2}^{n-k_n}\left[1-\frac{Y_n}{n}(1-e^{-f(j/n)})\right].
\]
Uniformly for \(Y_n\) in each bounded set, the logarithm of this product is
\[
-Y_n\,\frac1n\sum_{j=2}^{n-k_n}(1-e^{-f(j/n)})+O(Y_n^2/n),
\]
which converges to \(-Y\int_0^{1-\theta}(1-e^{-f(x)})dx\) after using the Gamma-posterior convergence and tightness. Testing simultaneously against any bounded continuous function of \(Y_n\) gives joint convergence of \((Y_n,\Xi_n)\) to \((Y,\Xi)\), where \(\Xi\mid Y\) is a Poisson point process of intensity \(Y\,dx\) on \([0,1-\theta]\). Since the expected number of points remains bounded, the process is finite almost surely and no mass escapes.

Let \(M_n=\Xi_n([0,1])\). Its conditional expectation is
\[
\mathbb E[M_n\mid E_n]=\frac{(n-k_n-1)b}{a+b+k_n}
\longrightarrow\frac{b(1-\theta)}{\theta}.
\]
Thus \(M_n=O_{\Pr}(1)\). At any defect index \(j\) with \(Z_j=0\),
\[
\lambda_j^*=\sum_{\ell=j+1}^nZ_\ell
=(n-j)-\sum_{\ell=j+1}^n(1-Z_\ell),
\qquad\left|\frac{\lambda_j^*}{n}-(1-j/n)\right|\le\frac{M_n}{n}.
\]
Reflection \(x\mapsto1-x\), together with the bounded defect count, therefore transfers the Cox convergence to \(\Omega_n\). For a nondefect index \(Z_j=1\), \(\lambda_j^*=n-\sum_{\ell>j}(1-Z_\ell)\), so all such eigenvalues divided by \(n\) lie in \([1-M_n/n,1]\). This establishes completeness of the outlier description away from the upper endpoint, after excluding the structurally forced zero Laplacian eigenvalue.

Finally, conditioned on \(Y\), \(M=\Xi([0,1-\theta])\) is Poisson with mean \((1-\theta)Y\). Integrating its probability generating function against the Gamma density gives
\[
\mathbb E[t^M]=\left(\frac{\theta}{1-(1-\theta)t}\right)^b,
\qquad 0\le t\le1,
\]
whose generalized binomial expansion yields the claimed negative-binomial law.

### 4. Sharp conditional gap profile and complete-graph atom

For every \(k_n\le t\le n-1\), the nested suffix events give the *exact* conditional survival probability
\[
\Pr(\kappa_n\ge t\mid E_n)
=\frac{(a+k_n)_{t-k_n}}{(a+b+k_n)_{t-k_n}}
=\frac{\Gamma(a+t)\Gamma(a+b+k_n)}
{\Gamma(a+k_n)\Gamma(a+b+t)}.
\]
For fixed \(s\in(\theta,1)\), taking \(t=\lceil sn\rceil\) yields \((\theta/s)^b\). At \(s=\theta\), the limiting survival is one. A complete graph occurs precisely when every bit \(Z_2,\ldots,Z_n\) is one; conditional on \(E_n\) its exact probability is
\[
\frac{(a+k_n)_{n-k_n-1}}{(a+b+k_n)_{n-k_n-1}}
\longrightarrow\theta^b.
\]
The distribution of \(\kappa_n/n\) consequently converges weakly to the described law: its continuous part has density \(b\theta^bs^{-b-1}\), and the remaining mass \(\theta^b\) sits at \(1\). The same law follows by taking the smallest reflected Cox point, with the value \(1\) when the point process is empty. This cross-check also identifies the atom as the zero-defect probability from the negative-binomial law. \(\square\)

## Verification

A standalone script `verify.py` independently constructs the ordinary Laplacian from creation bits, computes all its eigenvalues numerically, and checks the exact indexed spectrum, deterministic gap identity and suffix-event equivalence for every binary creation vector through ten vertices. It also exhaustively enumerates finite Pólya/Beta-mixture path probabilities with exact rational arithmetic for four choices of positive urn-shape parameters, checking the rare-event mass, posterior beta-binomial defect counts, conditional gap tails and complete-graph atom. Large but finite Gamma-limit checks are numerical diagnostics only.

Run `python verify.py` with Python 3 and NumPy. The verified output is in `verification_output.txt`. The analytic argument above, rather than finite enumeration, establishes weak convergence and the sharp limits.

## Relationship to prior work

Yu, Alajaji and Gharesifard (arXiv:2603.18452v1, March 19, 2026) introduce the Pólya threshold graph and derive its exact creation-bit law and finite Laplacian eigenbasis/spectrum. Those are the input identities credited above; their inspected Sections 2–4 do not study conditioning on an eigenvalue of order \(n\) or the resulting Gamma–Cox outlier process.

Reilly and Scheinerman (2009, Corollaries 5.9–5.10) obtain algebraic-connectivity formulas for a different random threshold model with independent fair creation bits; the deterministic last-zero mechanism is already present there. Diaconis, Holmes and Janson (2008, Theorem 6.4 and Section 9) identify the fixed-probability limiting degree and Laplacian spectrum of random threshold graphs. Neither source supplies the rare, \(k_n\asymp n\) conditioning and the resulting random finite outlier spectrum. The standard Beta-to-Gamma endpoint limit and Poisson approximation are not claimed as new individually; their combined, spectrally tagged conditional law is the contribution.

## Limitations

The statement assumes fixed positive \(a,b\) and \(\theta\in(0,1)\); it does not address changing urn parameters, the endpoints \(\theta=0\) or \(\theta=1\), normalized graph Laplacians, or graph ensembles with a different creation mechanism. The Cox outlier process is finite and random; it does not describe the microscopic spacing of the large bulk eigenvalues near \(1\). No independence or priority certification is asserted. A general conditioned-exchangeability point-process theorem might encompass the probabilistic step; the closest inspected source statements were compared at the level of their hypotheses and conclusions.

## References

1. J. Yu, F. Alajaji, B. Gharesifard, *Pólya Thresholds Graphs*, arXiv:2603.18452v1, first public March 19, 2026. https://arxiv.org/abs/2603.18452
2. E. P. Reilly and E. R. Scheinerman, *Random Threshold Graphs*, Electronic Journal of Combinatorics **16** (2009), R130, especially Section 5.1. https://doi.org/10.37236/219
3. P. Diaconis, S. Holmes and S. Janson, *Threshold Graph Limits and Random Threshold Graphs*, Internet Mathematics **5** (2008), 267–320, Theorem 6.4 and Section 9. https://pmc.ncbi.nlm.nih.gov/articles/PMC2930250/
4. P. Manna, S. Mandal and F. C. Tura, *The Spectral Theory of Threshold Graphs: A Survey*, arXiv:2610.22838v1 (2026), contextual survey. https://arxiv.org/abs/2610.22838
