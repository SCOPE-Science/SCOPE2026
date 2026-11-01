# Exact Lucas-cube Fourier precision and parity-split sharp frame conditioning

## Finding
Let \(n\ge5\), and let \(\mathcal L_n\subset\{0,1\}^n\) consist of all cyclic binary strings with no adjacent pair of ones, including across the last--first boundary. Equip \(\mathcal L_n\) with the uniform probability measure. Put \(X_j(x)=x_j\), \(\psi_j(x)=(-1)^{x_j}-\mathbb E[(-1)^{X_j}]\), and define the normalized evaluation map \(E_n:\mathbb C^n\to L^2(\mathcal L_n)\) by \(E_n c=\sum_{j=0}^{n-1}c_j\psi_j\). Define
\[
 s=\frac{3-\sqrt5}{2},\quad r=-s,\quad
 B_n=\frac{(1-s^2)(1-r^n)}{5(1+r^n)},\quad
 d_{n,k}=1+s^2+2s\cos\frac{2\pi k}{n}.
\]
Every eigenvalue of the Gram matrix \(E_n^*E_n\), with its Fourier-mode index \(0\le k<n\), is exactly
\[
 \boxed{\gamma_{n,k}=4\left(\frac{B_n}{d_{n,k}}+
 \mathbf1_{\{k=0\}}\frac{n r^n}{5(1+r^n)^2}\right).}
\]
These eigenvalues are strictly positive. They are smallest exactly at \(k=0\), and largest exactly at \(k=\lfloor n/2\rfloor\), together with the conjugate mode \(k=\lceil n/2\rceil\) when \(n\) is odd. Thus the sharp condition number is
\[
 \boxed{\kappa_n=\sqrt{\gamma_{n,\lfloor n/2\rfloor}/\gamma_{n,0}}<\sqrt5},
 \qquad \sup_{n\ge5}\kappa_n=\sqrt5.
\]
Writing \(C_n=\operatorname{Cov}(X_0,\ldots,X_{n-1})\), \(A_n\) for the unweighted adjacency matrix of the \(n\)-cycle, and \(J_n\) for the all-ones matrix, the complete precision matrix is
\[
 \boxed{C_n^{-1}=\frac{(1+s^2)I+sA_n}{B_n}
 +\frac1n\left(\Lambda_{n,0}^{-1}-\frac{(1+s)^2}{B_n}\right)J_n},
 \qquad \Lambda_{n,0}=\gamma_{n,0}/4.
\]
In particular, the inverse covariance is a local cyclic tridiagonal operator plus a single rank-one correction. The squared-condition deficit has sharply different parity asymptotics:
\[
 \boxed{5-\kappa_n^2=\begin{cases}
 5\sqrt5\,n s^n+O(n^2s^{2n}),&n\to\infty\text{ even},\\
 5\pi^2/n^2+O(n^{-4}+ns^n),&n\to\infty\text{ odd}.
 \end{cases}}
\]

## Assumptions and scope
Indices are reduced modulo \(n\). The Fourier coordinates are indexed by \(k\in\{0,\ldots,n-1\}\), with characters \(j\mapsto e^{2\pi i k j/n}\). Inner products on \(L^2(\mathcal L_n)\) use probability measure, not counting measure. The centered Walsh characters \(\psi_j\) are not separately normalized to unit variance; this common variance scaling leaves \(\kappa_n\) unchanged. The two small integers \(n=3,4\) are not needed for the stated theorem. The matrix \(A_n\) has precisely two neighboring ones per row. Every claimed bound and asymptotic is for all integers \(n\ge5\) of the indicated parity, not only the tested values.

## Proof
**Transfer moments.** Set \(T=\begin{pmatrix}1&1\\1&0\end{pmatrix}\) and \(D=\operatorname{diag}(0,1)\). The identity \(\operatorname{tr}(T^n)=|\mathcal L_n|\) follows by multiplying the allowed-neighbor transition entries around the cycle. Its eigenvalues are \(\alpha=(1+\sqrt5)/2\) and \(\beta=(1-\sqrt5)/2\), with ratio \(\beta/\alpha=r\). In the orthonormal spectral basis of \(T\), the diagonal entries of \(D\) are \(p=(5-\sqrt5)/10\) and \(1-p\); its off-diagonal entry has squared modulus \(p(1-p)=1/5\). Thus, for \(0\le d<n\),
\[
 \mathbb E[X_0X_d]=\frac{p^2+(1-p)^2r^n+
 \tfrac15(r^d+r^{n-d})}{1+r^n},\quad
 \mathbb E[X_0]=\frac{p+(1-p)r^n}{1+r^n}.
\]
This formula includes \(d=0\) because \(D^2=D\). Subtracting the square of the mean, and using \((2p-1)^2=1/5\), gives the exact covariance row
\[
 C_n(0,d)=\frac15\left(\frac{r^d+r^{n-d}}{1+r^n}
 +\frac{r^n}{(1+r^n)^2}\right).
\]
The enumerative normalization also equals \(|\mathcal L_n|=L_n\), the \(n\)th Lucas number.

**Fourier diagonalization.** The covariance is real symmetric circulant. At the discrete cyclic Fourier frequencies \(\theta_k=2\pi k/n\), the geometric sum identity
\[
 \sum_{d=0}^{n-1}(r^d+r^{n-d})e^{-i\theta_kd}
 =\frac{(1-r^n)(1-r^2)}{1-2r\cos\theta_k+r^2}
\]
yields its eigenvalues \(\Lambda_{n,k}=\gamma_{n,k}/4\), proving the spectral formula because \(\psi_j=-2(X_j-\mathbb EX_j)\). The vectors \(0,e_0,\ldots,e_{n-1}\) all belong to \(\mathcal L_n\); a linear combination of the centered coordinate functions constant on this set must have every coefficient zero. Hence the Gram matrix is strictly positive definite, without any appeal to numerical spectral tests.

**Precision structure.** The Fourier symbol of \((1+s^2)I+sA_n\) is \(d_{n,k}\). At every nonzero mode, \(\Lambda_{n,k}^{-1}=d_{n,k}/B_n\); only the zero mode differs. Since \(J_n/n\) is the projection onto the zero Fourier mode, the asserted rank-one correction is exactly the difference of the zero-mode inverse eigenvalues.

**Extremal modes.** Write \(d_{n,k}=1+s^2+2s\cos(2\pi k/n)\). For \(1\le k\le\lfloor n/2\rfloor\), these strictly decrease, hence \(\Lambda_{n,k}\) strictly increase. When \(n\) is odd, \(r^n<0\) makes the zero-mode correction negative, so \(\Lambda_{n,0}<\Lambda_{n,1}\). For even \(n\ge6\), put \(u=s^n\), \(d_0=(1+s)^2\), and \(d_1=d_0-4s\sin^2(\pi/n)\). Then
\[
 \Lambda_{n,1}-\Lambda_{n,0}=
 \frac{4B_ns\sin^2(\pi/n)}{d_0d_1}
 -\frac{nu}{5(1+u)^2}.
\]
The elementary bounds \(3/8<s<2/5\), \(B_n>18/125\), \(d_0d_1<(7/5)^4\), and \(\sin(\pi/n)\ge2/n\) make the first term strictly greater than \(540/(2401n^2)>1/(5n^2)\). The second is less than \(n(2/5)^n/5<1/(5n^2)\), since \(n^3(2/5)^n<1\) at \(n=6\) and decreases thereafter. Thus the zero mode is uniquely minimal in both parities, and the most alternating available mode is maximal.

**Sharp universal bound.** Observe \((1-s)^2=s\) and \((1+s)^2=5s\). For even \(n\), the maximum is \(B_n/s\), while the minimum is strictly greater than \(B_n/(5s)\); hence \(\kappa_n^2<5\). For odd \(n\), put \(\delta=2(1-\cos(\pi/n))\). Then
\[
 5\Lambda_{n,0}-\Lambda_{n,\lfloor n/2\rfloor}
 =\frac{B_n\delta}{s(1+\delta)}
 -\frac{ns^n}{(1-s^n)^2}.
\]
For odd \(n\ge7\), \(\delta\ge4/n^2\), \(\delta<2/5\), \(B_n>4/25\), and \(s<2/5\) imply that the first term exceeds \(8/(7n^2)\). The magnitude of the second is smaller because
\[
 n^3(2/5)^n<\tfrac87(1-(2/5)^n)^2
\]
at \(n=7\), with the left side decreasing and the right side increasing thereafter. At \(n=5\), the exact covariance first row is \((24,-9,2,2,-9)/121\), with least eigenvalue \(10/121\) and largest eigenvalue \((5+\sqrt5)/22<50/121\). This completes the strict bound for every \(n\ge5\).

**Parity asymptotics.** As \(n\to\infty\), \(B_n\to(1-s^2)/5\), \(\Lambda_{n,0}\to1/(5\sqrt5)\), and the maximal eigenvalue tends to \(1/\sqrt5\). For even \(n\), the maximum is exactly \(B_n/s\), while the zero-mode additive term is \(ns^n/(5(1+s^n)^2)\). Expanding the quotient gives \(5-\kappa_n^2=5\sqrt5\,ns^n+O(n^2s^{2n})\). For odd \(n\), the largest-mode denominator is \(s[1+2(1-\cos(\pi/n))]\), and the zero-mode correction is \(O(ns^n)\). Taylor expansion of \(\cos(\pi/n)\) yields \(5-\kappa_n^2=5\pi^2/n^2+O(n^{-4}+ns^n)\).

## Verification
Run `python3 check_lucas_frame.py` using only the Python standard library. The checker independently enumerates cyclic admissible bitstrings, calculates Fibonacci-number two-coordinate moments with exact fractions, Fourier-transforms the resulting covariance rows, checks all entries of the stated inverse covariance, and compares the extremal modes. The recorded execution passed 138 exact independent-set moment comparisons, 1265 Fourier-eigenvalue comparisons, 2079 precision-identity entry comparisons, and 90 extremal comparisons, plus exact rational inequality boundary tests. Finite checks support reproducibility but are not substitutes for the all-integer proof above.

## Relationship to prior work
Lucas cubes are the independent-set configurations of finite cycle graphs. Ashrafi, Azarija, Fathalikhani, Klavžar and Petkovšek (2014) describe their dihedral orbit structure, while Codara and D'Antona (2014) develop independent-set and edge-enumeration formulas for generalized Lucas cubes. These supply the natural cyclic configuration and Fibonacci--Lucas counts, not its centered first-Walsh-band Gram spectrum. The standard transfer-matrix treatment of a one-dimensional hard-core lattice gas supplies a mechanism for two-point correlations; the theorem here additionally identifies the exact finite-ring Fourier precision matrix, the global sharp sampling condition bound and its unequal parity convergence rates. Earlier physical literature on lattice-gas direct correlations may overlap parts of the limiting inverse-covariance picture; equivalence of the full finite-cycle theorem has not been independently excluded.

## Limitations
The result concerns the uniformly measured periodic independent-set support at activity one, centered degree-one Walsh characters and dimension \(n\ge5\). It does not give sharp spectra for higher Walsh bands, other activities, open chains, or arbitrary independent-set graphs. Its full finite-ring originality against older physical correlation-function literature remains subject to further literature examination; the theorem and proof do not rely on an unverified uniqueness claim.

## References
- A. R. Ashrafi, J. Azarija, K. Fathalikhani, S. Klavžar, M. Petkovšek, *Vertex and edge orbits of Fibonacci and Lucas cubes*, arXiv:1407.4962 (first public version 2014-07-18), §§1--2 and 5.
- P. Codara and O. M. D'Antona, *Generalized Fibonacci and Lucas cubes arising from powers of paths and cycles*, arXiv:1410.4080 (first public version 2014-10-15), §§1 and 4--5.
- K. Tanaka, T. Morita, K. Hiroike, *Correlation Functions of a One-Dimensional Lattice Gas with Nearest-Neighbor and Next-Nearest-Neighbor Interactions*, *Progress of Theoretical Physics* **77** (1987), 68--83, doi:10.1143/PTP.77.68 (abstract consulted; complete text not accessible during this study).
