# Sharp Haar endpoint law and complementary-dimension duality for cross-polytope projections

## Finding
Let \(1\le k<n\), put \(q=n-k\), \(m=kq\), and let \(E\) be Haar-uniform in the real Grassmannian \(\mathrm{Gr}(k,n)\). For the regular cross-polytope \(B_1^n=\{x\in\mathbb R^n:\sum_{i=1}^n|x_i|\le1\}\), define its *normalized shadow volume*
\[
X_{n,k}(E)=\frac{k!}{2^k}\operatorname{vol}_k(\operatorname{proj}_E B_1^n).
\]
The sharp projection inequality and its equality characterization give \(0<X_{n,k}\le1\), with equality precisely at the \(\binom nk\) coordinate \(k\)-planes [1].

**Theorem.** There exists \(\varepsilon_0(n,k)>0\) such that, for \(0<\varepsilon<\varepsilon_0(n,k)\),
\[
\Pr\{X_{n,k}\ge1-\varepsilon\}=\binom nk\Pr\left\{\prod_{i=1}^k B_i\ge(1-\varepsilon)^2\right\},\qquad
B_i\ \text{independent},\quad B_i\sim\operatorname{Beta}\!\left(\frac{k-i+1}{2},\frac q2\right).
\]
For fixed \(n,k\), this has the sharp two-term endpoint expansion
\[
\boxed{\Pr\{X_{n,k}\ge1-\varepsilon\}=C_{n,k}\varepsilon^{m/2}\left[1+\frac{m(k-2)(q-2)}{4(m+2)}\varepsilon+O_{n,k}(\varepsilon^2)\right],}
\]
where
\[
\boxed{C_{n,k}=\binom nk\frac{2^{m/2}\Gamma_k(n/2)}{\Gamma_k(k/2)\Gamma(m/2+1)},\quad
\Gamma_k(z)=\pi^{k(k-1)/4}\prod_{j=0}^{k-1}\Gamma(z-j/2).}
\]
In particular, if either \(k=2\) or \(q=2\), the first relative correction vanishes **exactly** and
\[
\Pr\{X_{n,k}\ge1-\varepsilon\}=\binom n2\varepsilon^{n-2}\bigl[1+O_n(\varepsilon^2)\bigr].
\]
There is also an **exact near-endpoint duality**, not just an asymptotic one: after shrinking \(\varepsilon_0\) if necessary,
\[
\boxed{\Pr\{X_{n,k}(E)\ge1-\varepsilon\}=\Pr\{X_{n,q}(E^\perp)\ge1-\varepsilon\}\quad (0<\varepsilon<\varepsilon_0).}
\]
The two events themselves agree under the orthogonal-complement coupling for all sufficiently small \(\varepsilon\).

## Assumptions and scope
All vector spaces and Haar measures are real; \(\operatorname{vol}_k\) is ordinary Euclidean \(k\)-volume, with \(\operatorname{vol}_k B_1^k=2^k/k!\). Integers \(n\ge2\), \(1\le k\le n-1\) are fixed before \(\varepsilon\downarrow0\). The \(O_{n,k}\)-bound makes **no** assertion uniform in growing dimensions. The beta distribution has density \(b^{a-1}(1-b)^{c-1}/\mathrm B(a,c)\) on \((0,1)\). The formula describes the endpoint germ, not the full shadow-volume distribution.

## Proof
**1. Local shadow identity.** Fix the coordinate space \(E_0=\mathbb R^k\oplus\{0\}\), identify \(\mathbb R^n=\mathbb R^k\oplus\mathbb R^q\), and write nearby planes as graphs \(E_T=\{(x,Tx):x\in\mathbb R^k\}\), where \(T\) is a real \(q\)-by-\(k\) matrix. The map \(x\mapsto(x,Tx)\) has Gram matrix \(I_k+T^\mathsf TT\). An orthonormal coordinate description of projected standard-basis vectors consequently gives
\[
\operatorname{proj}_{E_T}B_1^n\cong (I_k+T^\mathsf TT)^{-1/2}\operatorname{conv}\{\pm e_1,\dots,\pm e_k,\ \pm T_{1\bullet},\dots,\pm T_{q\bullet}\}.
\]
Whenever each row satisfies \(\|T_{j\bullet}\|_1\le1\), the extra generators lie in \(B_1^k\). In particular, throughout an open neighborhood of \(T=0\), the convex hull equals \(B_1^k\), and hence **exactly**
\[
X_{n,k}(E_T)=\det(I_k+T^\mathsf TT)^{-1/2}.
\tag{1}
\]
By the 2026 sharp global theorem [1], only the \(\binom nk\) coordinate \(k\)-planes attain \(X=1\). Since the Grassmannian is compact and \(X\) continuous, there is \(\varepsilon_0>0\) such that \(X\ge1-\varepsilon_0\) implies that the plane is in one of disjoint neighborhoods where (1) holds. Symmetry makes each neighborhood contribute identically.

**2. Exact beta-product law near one maximizer.** Let \(Q\) be an \(n\)-by-\(k\) matrix with orthonormal columns spanning Haar \(E\), and let \(Q_0\) comprise its first \(k\) rows. Put \(D=|\det Q_0|\). In the graph neighborhood, \(Q_0=(I_k+T^\mathsf TT)^{-1/2}\) after a harmless right orthogonal transformation, so \(D=X_{n,k}(E_T)\).

To determine the *global* law of \(D\), let \(Z\) be \(n\)-by-\(k\) with independent standard normal entries and use its QR decomposition \(Z=QR\). Then \(Q\) is Haar-Stiefel and independent of \(R\). If \(G\) denotes the first \(k\) rows of \(Z\),
\[
|\det G|^2=D^2\det(Z^\mathsf TZ).
\]
The Gaussian QR/Gram–Schmidt decomposition of an \(N\)-by-\(k\) matrix has independent squared diagonal lengths with chi-square degrees \(N,N-1,\ldots,N-k+1\). Therefore, for every \(s\ge0\),
\[
\mathbb ED^{2s}=\frac{\Gamma_k(k/2+s)\Gamma_k(n/2)}{\Gamma_k(k/2)\Gamma_k(n/2+s)}
=\prod_{i=1}^k\frac{\Gamma((k-i+1)/2+s)\Gamma((n-i+1)/2)}{\Gamma((k-i+1)/2)\Gamma((n-i+1)/2+s)}.
\]
The product on the right is the Mellin transform of \(\prod_iB_i\) with the stated independent beta laws. Both variables lie in \([0,1]\); equality of all integer moments implies equality in distribution. Since the near-max event consists of disjoint coordinate neighborhoods on each of which \(X=D\), the beta-product formula follows.

**3. Leading constant and the second correction.** The same Gaussian block argument yields the normalized Haar graph-coordinate density
\[
f(T)=f(0)\det(I_k+T^\mathsf TT)^{-n/2},\qquad
f(0)=\frac{\Gamma_k(n/2)}{\pi^{m/2}\Gamma_k(k/2)}.
\tag{2}
\]
Indeed, for blocks \(Z=(G^\mathsf T,H^\mathsf T)^\mathsf T\), the change \(H=TG\) has Jacobian \(|\det G|^q\). Integrating the Gaussian density over \(G\) gives the determinant power \(-n/2\), and evaluating the density at zero using the Gaussian determinant moment gives the constant in (2).

Use polar coordinates \(T=rW\) in \(\mathbb R^m\), where \(\|W\|_F=1\). Let \(a(W)=\operatorname{tr}[(W^\mathsf TW)^2]\). Uniformly over the compact unit sphere,
\[
\log\det(I_k+r^2W^\mathsf TW)=r^2-\tfrac12a(W)r^4+O(r^6),
\quad -2\log(1-\varepsilon)=2\varepsilon+\varepsilon^2+O(\varepsilon^3).
\]
Thus the radial boundary of the event is
\[
r_{\max}(W)^2=2\varepsilon+(1+2a(W))\varepsilon^2+O(\varepsilon^3).
\]
Also \(f(rW)/f(0)=1-\tfrac n2r^2+O(r^4)\). Consequently, integrating in \(r\), dividing by \(f(0)\operatorname{vol}(B_2^m)(2\varepsilon)^{m/2}\), and averaging \(W\) gives
\[
1+\frac m4\left(1+2\mathbb E_Wa(W)-\frac{4n}{m+2}\right)\varepsilon+O(\varepsilon^2).
\tag{3}
\]
To calculate the sphere moment, take a standard Gaussian \(q\)-by-\(k\) matrix \(G\). Wick pairings of the four entries in \(\operatorname{tr}[(G^\mathsf TG)^2]\) give
\[
\mathbb E\operatorname{tr}[(G^\mathsf TG)^2]=qk(q+k+1)=m(n+1).
\]
Independence of the Gaussian radius and direction, together with \(\mathbb E\|G\|_F^4=m(m+2)\), yields \(\mathbb E_Wa(W)=(n+1)/(m+2)\). Inserting this into (3) and using \(n=k+q\) reduces the relative coefficient to
\[
\frac{m}{4(m+2)}\bigl(m+4-2n\bigr)=\frac{m(k-2)(q-2)}{4(m+2)}.
\]
The leading radial integral per coordinate maximizer is \(f(0)\operatorname{vol}(B_2^m)(2\varepsilon)^{m/2}\), where \(\operatorname{vol}(B_2^m)=\pi^{m/2}/\Gamma(m/2+1)\). Multiplying by \(\binom nk\) produces \(C_{n,k}\). For \(k=2\) or \(q=2\), gamma ratios simplify exactly to \(C_{n,k}=\binom n2\), and the linear relative coefficient vanishes.

**4. Exact duality of endpoint germs.** The orthogonal complement of \(E_T\) is the graph of \(-T^\mathsf T\) over the complementary coordinate \(q\)-plane. Both graphical volume identities apply simultaneously near \(T=0\), giving
\[
X_{n,k}(E_T)=\det(I_k+T^\mathsf TT)^{-1/2}
=\det(I_q+TT^\mathsf T)^{-1/2}=X_{n,q}(E_T^\perp).
\]
The matrix-determinant equality follows from Sylvester's identity. Compactness and sharp equality in [1] exclude any near-max event outside the simultaneous graph neighborhoods when \(\varepsilon\) is sufficiently small. Hence the two endpoint events agree **pointwise** under complementation, proving the exact duality.

## Verification
The included `verify.py` uses only the standard Python library and performs 1,400 independent two-dimensional projected-polygon hull tests against (1), 198 beta-product moment checks, 105 gamma/symmetry/correction identities, and a seeded 130,000-draw numerical beta-product sanity test for \(n=4,k=2\). It reports `VERIFY_OK`. The checks validate finite algebra and independent geometry samples, **not** the uniform remainder or global maximizer theorem, which are established analytically above with the cited antecedent [1].

As independent exact boundary examples, \(n=2,k=1\) gives \(C_{2,1}=4\sqrt2/\pi\) and relative correction \(1/12\), agreeing with the elementary arc length of \(|\cos\theta|\) or \(|\sin\theta|\) near one. At \(n=3,k=1\) and \(n=3,k=2\), the endpoint law equals \(3\varepsilon\) for all sufficiently small \(\varepsilon\). At \(n=4,k=2\), it equals \(6\varepsilon^2\) for all sufficiently small \(\varepsilon\). Indeed, the beta variables there have laws \(\operatorname{Beta}(1,1)\) and \(\operatorname{Beta}(1/2,1)\); their product has tail \(\Pr(B_1B_2\ge t)=(1-\sqrt t)^2\), giving exactly \(\varepsilon^2\) per coordinate maximizer.

## Relationship to prior work
Ivanov [1] proved the sharp **maximum** of these projected volumes, and, crucially, the exact coordinate-subspace equality set in all dimensions. The 2018 antecedent [2] established the maximal inequality in dimensions two and three and studied other volume extremizers. Neither inspected paper determines the Haar probability of *near-maximal* volume, the exact beta-product endpoint germ, its two-term expansion, or the complementary-dimension event identity. The beta-product law of coordinate-minor determinants and Gaussian QR determinants are standard probability tools; novelty is **not** asserted for those standalone identities. The contribution is their exact geometric transfer to the near-maximum projection law, including the universal correction cancellation.

## Limitations
The endpoint threshold \(\varepsilon_0(n,k)\) is proved to exist but is not evaluated explicitly. The formula does not describe the middle or lower tails. Constants in the remainder may depend on both fixed dimensions. This result uses the published extremal equality characterization [1]; it does not independently reprove that sharp global theorem. No claim of exhaustive historical priority or independent external audit is made.

## References
1. G. Ivanov, *The maximal volume of projections of the cross-polytope*, arXiv:2607.12072, first submitted 2026-07-13. https://arxiv.org/abs/2607.12072
2. G. Ivanov, *On the volume of projections of the cross-polytope*, arXiv:1808.09165, first submitted 2018-08-28. https://arxiv.org/abs/1808.09165
