# Sharp derivative-intensity threshold for real polynomial covariance tomography

## Finding
Fix an integer \(N\ge1\). Let \(\mathcal S_N\) be the space of real symmetric \((N+1)\)-by-\((N+1)\) matrices. For a matrix \(C\in\mathcal S_N\), define the real polynomial \(v(x)=(1,x,\ldots,x^N)^T\), its ordinary derivative vector \(v_k(x)=d^kv(x)/dx^k\), and the derivative-intensity polynomial \(J_k^C(x)=v_k(x)^TCv_k(x)\). Let \(\mathcal T_{N,K}C=(J_0^C,\ldots,J_K^C)\) for integers \(0\le K\le N\).

**Theorem.** Write \(m=2K+2\) and \(r=N-m\). The kernel of \(\mathcal T_{N,K}\), viewed through its symmetric coefficient kernel \(B_C(X,Y)=v(X)^TCv(Y)\), consists **exactly** of the polynomials
\[
B_C(X,Y)=(X-Y)^m S(X,Y),
\]
where \(S\) is symmetric and has degree at most \(r\) in each variable (for \(r<0\), only the zero polynomial is allowed). Consequently
\[
\dim\ker\mathcal T_{N,K}=\begin{cases}(r+1)(r+2)/2,&r\ge0,\\0,&r<0.\end{cases}
\]
In particular \(\mathcal T_{N,K}\) determines **every** real symmetric covariance matrix, and therefore every positive semidefinite covariance matrix, if and only if
\[
\boxed{K\ge\lfloor N/2\rfloor.}
\]
If \(K<\lfloor N/2\rfloor\), the failure persists inside the **strictly positive definite** cone: there are two distinct positive definite covariance matrices with identical derivative-intensity polynomials for all orders \(0,\ldots,K\). At the sharp threshold, finite samples suffice: for each order \(k\), any \(2(N-k)+1\) distinct real points determine \(J_k^C\), hence the entire covariance.

## Assumptions and scope
This concerns real symmetric \(C\), with no rank restriction. A random real-coefficient polynomial \(P(x)=\sum_{j=0}^N A_jx^j\), with finite coefficient second moments and \(C_{ij}=\mathbb E[A_iA_j]\), has \(\mathbb E|P^{(k)}(x)|^2=J_k^C(x)\). Complex random coefficients cannot be reconstructed in full from these measurements: their invisible skew-imaginary covariance must not be conflated with the real symmetric matrix. There is no claim that \(\lfloor N/2\rfloor\) derivatives are needed for *rank-one or rank-two pure-state* phase retrieval; much lower derivative orders already suffice in known pure-signal results. Absolute-value squares and nonnegative second moments are the inputs; no assumptions about Gaussianity or independence of coefficients are made.

## Proof
**1. Diagonal derivative correspondence.** With independent variables \(X,Y\), define \(B_C(X,Y)=\sum_{i,j=0}^N C_{ij}X^iY^j\). It is symmetric and has separate degrees at most \(N\). Ordinary differentiation yields the exact identity
\[
J_k^C(x)=\left[\partial_X^k\partial_Y^k B_C(X,Y)\right]_{X=Y=x}.
\]
Each symmetric bivariate polynomial with separate degrees at most \(N\) arises from a unique real symmetric matrix \(C\).

**2. Vanishing jets are diagonal divisibility.** Put \(u=(X+Y)/2\) and \(w=(X-Y)/2\). Symmetry permits a unique even expansion \(B_C(u+w,u-w)=\sum_{j=0}^{N} f_j(u)w^{2j}\) (zero terms are allowed). The mixed derivative obeys \(\partial_X\partial_Y=(\partial_u^2-\partial_w^2)/4\). Therefore, for every \(k\ge0\),
\[
4^kJ_k^C(u)=\sum_{j=0}^k (-1)^j\binom{k}{j}(2j)!\,f_j^{(2k-2j)}(u).
\]
For \(k=0\), the condition \(J_0^C\equiv0\) forces \(f_0\equiv0\). Inductively, if \(f_0,\ldots,f_{k-1}\) vanish, the displayed equation becomes \(4^kJ_k^C=(-1)^k(2k)!f_k\); hence simultaneous vanishing of \(J_0^C,\ldots,J_K^C\) is **equivalent** to \(f_0=\cdots=f_K=0\), or divisibility of \(B_C\) by \((X-Y)^{2K+2}\). The converse follows immediately because any mixed derivative of order \(k\) drops the order of vanishing on the diagonal by at most \(2k\).

**3. Separate-degree bound and exact nullity.** If \(B_C=(X-Y)^mS\ne0\), multiplication by \((X-Y)^m\), a monic polynomial of degree \(m\) in \(X\) and also in \(Y\), raises each separate polynomial degree by precisely \(m\). Thus \(S\) must have separate degrees at most \(r=N-m\). Because \(m\) is even, symmetry of \(B_C\) is equivalent to symmetry of \(S\). The vector space of such \(S\) has dimension \((r+1)(r+2)/2\) when \(r\ge0\): one free coefficient for each \((i,j)\) with \(0\le i\le j\le r\). If \(r<0\), there is no nonzero such \(S\). Therefore the kernel formula and the sharp uniqueness threshold follow.

**4. Strictly positive definite ambiguity below threshold.** Whenever \(m\le N\), take \(S\equiv1\) to obtain the nonzero symmetric matrix \(D\) with \(v(X)^TDv(Y)=(X-Y)^m\). Choose \(0<\varepsilon<1/\|D\|_{\mathrm{op}}\). The distinct matrices \(I+\varepsilon D\) and \(I-\varepsilon D\) are strictly positive definite, yet their data agree for every order \(0\le k\le K\). Hence restricting to positive definite states cannot improve the threshold.

**5. Finite sampling.** The polynomial \(J_k^C\) has degree at most \(2(N-k)\), so \(2(N-k)+1\) distinct real evaluations determine it by ordinary interpolation. Applying the preceding unique inversion for all orders through the threshold recovers \(C\). No minimality is claimed for the individual number or placement of sample points.

## Verification
The standalone `checker.py` forms the exact rational linear measurement matrices and checks the predicted kernel dimensions for \(1\le N\le12\), with each available derivative order through \(7\). It also constructs the nonzero diagonal-divisibility kernel polynomial whenever possible, checks its annihilation by all measurements, and verifies explicit positive-definite ambiguity pairs by strict diagonal dominance. It passed 111 exact assertions. These finite checks corroborate, but do not replace, the all-integer proof above.

## Relationship to prior work
Chen and Wang (2023, arXiv:2304.06206), especially Theorem 4.1 and Lemma 4.2, establish conjugate phase retrieval of pure complex spline/polynomial signals from value and first-derivative magnitudes. Their result already shows that the pure-signal conclusion for high derivative orders is not new. The theorem here is instead a **sharp all-rank real covariance (mixed-state) identifiability classification**, and gives every linear kernel dimension plus explicit positive-definite counterpairs below the threshold. Pure conjugate phase retrieval permits a nonzero measurement nullspace as long as it misses certain low-rank differences; all-rank covariance recovery requires zero nullspace and is strictly stronger as a linear tomography requirement. Grohs, Liehr, and Rathmair (2022, arXiv:2207.10620) motivate multi-measurement phaseless sampling in a different infinite-dimensional STFT setting and do not provide this polynomial covariance kernel formula. Related two-ray and two-circle polynomial intensity results concern different measurement sets and primarily rank-one phase recovery, not covariance of arbitrary rank.

## Limitations
The theorem is finite-dimensional and concerns exact noiseless intensity polynomials, not quantitative conditioning under noise. Its sharp order threshold is for reconstruction of *every real covariance*, not for pure-phase retrieval; phase/conjugation ambiguity cannot be resolved from real-line values alone. The recovery statement treats covariance, not the full probability law of a random polynomial. Literature-priority uncertainty remains for possible older diagonal-jet tomography formulations using different vocabulary.

## References
1. Y. Chen and Y. Wang, *Conjugate phase retrieval in a complex shift-invariant space*, arXiv:2304.06206v1 (first public 2023-04-13), Sections 3–4, Theorem 4.1, Lemma 4.2; https://arxiv.org/abs/2304.06206.
2. P. Grohs, L. Liehr, and M. Rathmair, *Multi-window STFT phase retrieval: lattice uniqueness*, arXiv:2207.10620 (first public 2022-07-21), Sections 1–2; https://arxiv.org/abs/2207.10620.
3. J. N. McDonald, *Phase retrieval and magnitude retrieval of entire functions*, Journal of Fourier Analysis and Applications 10 (2004), 259–267 (cited in Reference 1; full text not inspected here).
