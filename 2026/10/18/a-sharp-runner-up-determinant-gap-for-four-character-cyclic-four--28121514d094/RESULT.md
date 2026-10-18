# A sharp runner-up determinant gap for four-character cyclic Fourier sampling

## Finding
Let \(N=4m\) for an integer \(m\ge2\), let \(\omega=e^{2\pi i/N}\), and let \(E=\{0,1,2,3\}\). For each four-element set \(B\subset\mathbb Z_N\), form the unnormalized Fourier matrix \(T_B=(\omega^{jk})_{j\in E,\,k\in B}\) and put \(D(B)=|\det T_B|\). The global maximum is \(16\), attained exactly when \(B\) is a translate of the order-four subgroup \(\{0,m,2m,3m\}\). Among **all other** four-element sampling sets, the *sharp second-largest determinant* is
\[
\boxed{\max_{B\text{ not a square translate}}D(B)=16\cos(\pi/N)\cos(2\pi/N).}
\]
Equality holds exactly when \(B\) arises from one of those optimal squares by moving exactly one of its four nodes one grid step clockwise or anticlockwise. Equivalently, its four positive cyclic gaps, read in order, are a rotation of \((m-1,m,m,m+1)\) or its reversal. There are exactly \(2N\) distinct second-best four-element sets. Thus the sharp multiplicative loss caused by forbidding every perfect square is \(1-\cos(\pi/N)\cos(2\pi/N)\), with the asymptotic law
\[
1-\cos(\pi/N)\cos(2\pi/N)=\frac{5\pi^2}{2N^2}+O(N^{-4})\quad(N\longrightarrow\infty,\ 4\mid N).
\]

## Assumptions and scope
Throughout, \(m\ge2\), the four columns correspond to distinct residues, and \(\omega\) is a primitive \(N\)-th root of unity. No Fourier-matrix normalization is used: the unrestricted Hadamard determinant bound is \(4^{4/2}=16\). The result concerns the absolute determinant (sampling volume), not the smallest singular value or condition number. A square translate means a set \(t+\{0,m,2m,3m\}\), of which there are \(m=N/4\), and exclusion is of **all** such sets. The sign of the Fourier exponential does not change the conclusion.

## Proof
**1. Positive cyclic gaps and chord product.** List \(B\) in cyclic increasing order as \(k_1<k_2<k_3<k_4\) in \(\{0,\ldots,N-1\}\). Write \((a,b,c,d)=(k_2-k_1,k_3-k_2,k_4-k_3,N+k_1-k_4)\); each is a positive integer, and \(a+b+c+d=N\). Because the matrix has rows of degrees zero through three, its determinant is a Vandermonde product of the four roots of unity. Writing \(\alpha=\pi/N\), the six chord lengths give the identity
\[
 D(B)=64\sin(\alpha a)\sin(\alpha b)\sin(\alpha c)\sin(\alpha d)\sin(\alpha(a+b))\sin(\alpha(b+c)).\tag{1}
\]
Every factor is strictly positive, since the relevant gaps and diagonal gap sums lie strictly between zero and \(N\).

**2. A factorization separating integer and half-integer defects.** Define
\[
p=\frac{a+c}{2},\qquad u=\frac{a-c}{2},\qquad v=\frac{b-d}{2},\qquad
T=\sin^2(\alpha p),\quad X=\sin^2(\alpha u),\quad Y=\sin^2(\alpha v).
\]
Because \(a+c+b+d=4m\), the gaps can be recovered as
\[
 a=p+u,\quad c=p-u,\quad b=2m-p+v,\quad d=2m-p-v.
\]
The elementary identity \(\sin(x+y)\sin(x-y)=\sin^2x-\sin^2y\) gives the first two opposite-gap products. The diagonal terms satisfy
\[
\sin(\alpha(a+b))\sin(\alpha(b+c))
=\cos(\alpha(u+v))\cos(\alpha(v-u))=1-X-Y.
\]
Consequently the **exact** determinant formula is
\[
\boxed{D(B)=64(T-X)(1-T-Y)(1-X-Y).}\tag{2}
\]
All three factors on the right are strictly positive. The integer-gap parity restriction implies exactly two cases: either \(p,u,v\) are all integers, or all are half-integers. We analyze both, without a continuum-relaxation assumption.

**3. Integral branch.** Suppose \(p,u,v\in\mathbb Z\). If \(u=v=0\), then \(a=c=p\), \(b=d=2m-p\), and (2) simplifies to
\[
D(B)=16\sin^2(2\alpha p).
\]
This equals \(16\) exactly at \(p=m\), which gives the square translates. At every other admissible integer \(p\), it is at most \(16\cos^2(2\alpha)\), strictly less than \(16\cos(\alpha)\cos(2\alpha)\), because \(0<\cos(2\alpha)<\cos(\alpha)\).

Now suppose at least one of \(u,v\) is nonzero. The positive-gap condition forces \(|u|,|v|<N/2\), so \(X+Y\ge\sin^2\alpha\). By the arithmetic–geometric mean inequality applied to the first two positive factors of (2),
\[
 \frac{D(B)}{16}\le(1-X-Y)^3\le\cos^6\alpha.
\]
We claim \(\cos^6\alpha<\cos\alpha\cos(2\alpha)\) for \(0<\alpha\le\pi/8\). Indeed, set \(h(t)=\log\cos(2t)-5\log\cos t\). Then
\[
 h'(t)=\frac{\tan t\,(1-5\tan^2 t)}{1-\tan^2 t}>0\quad(0<t\le\pi/8),
\]
since \(\tan^2(\pi/8)=3-2\sqrt2<1/5\) and \(h(0)=0\). This proves the claim and excludes **every** nonsquare in the integral branch from equality at the proposed runner-up value.

**4. Half-integral branch.** Suppose \(p,u,v\in\mathbb Z+\tfrac12\). Then \(|u|,|v|\ge1/2\), while \(|u|,|v|<N/2\). Thus \(X,Y\ge s:=\sin^2(\alpha/2)\). For fixed \(T\), the positive-factor product in (2) decreases strictly as either \(X\) or \(Y\) increases. Therefore
\[
\frac{D(B)}{64}\le(T-s)(1-T-s)(1-2s)
=\bigl((1/2-s)^2-(T-1/2)^2\bigr)(1-2s).
\]
Here \(p\) is a half-integer with \(0<p<2m\), and \(T=\sin^2(\alpha p)\) is strictly increasing from zero to one. It is closest to \(1/2\) exactly when \(p=m\pm1/2\). Equality in the preceding bounds therefore requires **simultaneously** \(p=m\pm1/2\) and \(|u|=|v|=1/2\). At these values,
\[
(T-s)(1-T-s)=\frac{\cos(2\alpha)}4,
\qquad1-2s=\cos\alpha,
\]
so (2) gives \(D(B)=16\cos\alpha\cos(2\alpha)\). The four reconstructed gaps have exactly two entries \(m\), one entry \(m-1\), and one entry \(m+1\), with the exceptional smaller and larger gaps adjacent in cyclic order. Conversely any such gap tuple realizes equality. It is exactly the cyclic geometry obtained by moving one node of a perfect square by one grid step.

**5. Sharpness, distinctness, count, and asymptotics.** The integral branch has a unique global optimum: \(a=b=c=d=m\), namely a square translate; all remaining integer-branch determinants lie strictly below the half-integer maximum. Each of the \(N/4\) square translates has four choices of the moved node and two directions. Because \(m\ge2\), every resulting set contains exactly three nodes in the original residue class modulo \(m\) and a fourth node outside that class, so the source square is uniquely recovered; for \(m=2\) it is the majority residue class. Thus exactly \((N/4)\cdot4\cdot2=2N\) distinct sets attain the runner-up bound. Taylor's formula for the two cosine factors gives the asserted asymptotic relative loss, with error \(O(N^{-4})\).

## Verification
The accompanying standard-library Python program `verify.py` independently evaluates the six complex chord lengths of every four-node sample, compares them with the trigonometric gap expression (1), and checks the exact two-level maximum classification and all equality sets. It exhausts every subset for \(N=8,12,16,\ldots,52\): **825,642** subsets over 12 different cyclic orders, with square counts \(N/4\) and runner-up equality counts \(2N\) in each case. Run `python3 verify.py`; the recorded final line is `CHECK_OK 825642 configurations; all 12 cyclic orders checked`. The general theorem is proved by steps 1–5 rather than extrapolated from these finite floating-point checks.

## Relationship to prior work
Ferguson, Mayeli, and Sothanaphan, *Riesz bases of exponentials and multi-tiling in finite abelian groups*, arXiv:1904.04487, Definitions 3.9–3.10 and Proposition 4.10, define the determinant tightness invariant for Fourier sampling and identify its maximum with orthogonal sampling. They do not determine the **second** largest determinant after all optimal sampling sets have been forbidden, nor all runner-up configurations. The published mathematical result *Exact four-frequency determinant optimum on every cyclic grid* (2026) gives exactly the unrestricted maximum and all optimizers for the same four-row matrix for every \(N\); its formula at \(4\mid N\) is \(16\). Its claim **does not imply** the precise runner-up value or the count and classification of the next-best sets. The present theorem is a strict stability refinement, not a restatement of its maximum.

Dubickas and Pritsker, *Weighted Fekete points on the real line and the unit circle*, arXiv:1902.08348, recall the continuous-circle four-point Fekete maximum (a square), but do not impose the finite root-of-unity grid or classify discrete second-best configurations. Batenkov, Demanet, Goldman, and Yomdin, *Conditioning of Partial Nonuniform Fourier Matrices with Clustered Nodes*, arXiv:1809.00658, study singular-value estimates under arbitrary clustered sampling; such inequalities do not determine a second-largest determinant with equality or multiplicity. Direct searches under Fourier minor, discrete Fekete, Vandermonde runner-up, optimal sampling, and logarithmic-energy terminology found no previously documented covering theorem, though this is a best-knowledge comparison rather than proof of historical uniqueness.

## Limitations
The result covers exactly four consecutive Fourier rows and orders divisible by four and at least eight; there is no assertion for other residue classes, a general number of rows, or weighted nodes. The exact determinant ratio does not determine the worst singular value or spectral condition number. The finite numerical verifier is corroborative, not a universal certificate. A previous equivalent one-step discrete-Fekete calculation under different terminology remains a bibliographic possibility. This is a self-review only; no independent mathematical audit or validation has been performed.

## References
1. S. Ferguson, A. Mayeli, N. Sothanaphan, *Riesz bases of exponentials and multi-tiling in finite abelian groups*, arXiv:1904.04487v1 (first publicly posted 2019-04-09), https://arxiv.org/abs/1904.04487.
2. A. Dubickas, I. E. Pritsker, *Weighted Fekete points on the real line and the unit circle*, arXiv:1902.08348v1 (first publicly posted 2019-02-22), https://arxiv.org/abs/1902.08348.
3. D. Batenkov, L. Demanet, G. Goldman, Y. Yomdin, *Conditioning of Partial Nonuniform Fourier Matrices with Clustered Nodes*, arXiv:1809.00658v1 (first publicly posted 2018-09-03), https://arxiv.org/abs/1809.00658.
4. *Exact four-frequency determinant optimum on every cyclic grid*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-four-frequency-determinant-optimum-on-every-cyclic-grid--bb69c4d14769.
