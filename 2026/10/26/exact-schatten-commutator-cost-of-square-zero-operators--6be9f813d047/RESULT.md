# Exact Schatten commutator cost of square-zero operators

## Finding
Let \(H\) be a complex Hilbert space. For \(1\le p<\infty\) and nonzero \(T\in\mathcal S_p(H)\) satisfying \(T^2=0\), define
\[
\kappa_p(T):=\inf\{\|X\|_{2p}\|Y\|_{2p}:X,Y\in\mathcal S_{2p}(H),\ XY-YX=T\}.
\]
Then the exact infimum, always attained, is
\[
\boxed{\kappa_p(T)=2^{1/(2p)-1}\|T\|_p.}
\]
An attaining pair may be chosen with the first factor square-zero and the second self-adjoint. The sharp factor is independent of the rank, individual singular values, and dimension.

## Assumptions and scope
Here \(\mathcal S_r(H)\), \(1\le r<\infty\), denotes the Schatten ideal of compact operators with norm \(\|Z\|_r=(\operatorname{Tr}|Z|^r)^{1/r}\), and \(\mathcal S_\infty=\mathcal B(H)\) with the operator norm. The commutator convention is \([X,Y]=XY-YX\). No separability assumption on \(H\) is needed: every Schatten operator has separable essential support. The hypothesis \(T^2=0\) is essential to this exact formula; no assertion is made for general nilpotents or general compact targets. The trivial zero target has cost zero.

## Proof
Set \(q=2p\ge2\). Write \(T=JD\) for its polar decomposition, \(D=|T|\), where \(J\) is a partial isometry from \(V=\overline{\operatorname{ran}T^*}\) onto \(U=\overline{\operatorname{ran}T}\). The assumption \(T^2=0\) implies \(U\perp V\). In particular, \(J^2=0\), \(J^*J\) projects onto \(V\), and \(JJ^*\) onto \(U\).

**Attained upper bound.** Define the operators
\[
X=JD^{1/2},\qquad Y=\frac12\bigl(D^{1/2}-JD^{1/2}J^*\bigr).
\]
The two terms in \(Y\) occupy orthogonal diagonal corners, so \(Y\) is self-adjoint, and \(X^2=0\). Their products are \(XY=T/2\) and \(YX=-T/2\). Moreover,
\[
\|X\|_q=\|T\|_p^{1/2},\qquad
\|Y\|_q=2^{1/q-1}\|T\|_p^{1/2},
\]
using \(q=2p\) and the fact that the two diagonal corners of \(Y\) have identical nonzero singular values. Thus \(\kappa_p(T)\le2^{1/q-1}\|T\|_p\).

**An interpolation lemma.** Let \(P\) and \(Q\) be mutually orthogonal projections, and let \(Z=QZP\). For every \(2\le q<\infty\), put \(r=q/(q-2)\) (interpret \(r=\infty\) at \(q=2\)) and \(q'=q/(q-1)\). Then
\[
\boxed{\|[Z,A]\|_{q'}\le2^{1-1/q}\|Z\|_r\|A\|_q}
\]
for all admissible \(Z,A\). Here is a proof including the endpoint that supplies the nontrivial constant. The trace-class ideal property gives
\(\|[Z,A]\|_1\le2\|Z\|_1\|A\|_\infty\).
For the other endpoint, decompose \(H=PH\oplus QH\oplus (P+Q)^\perp H\). Since the only possible nonzero block of \(Z\) is from \(P H\) to \(Q H\), all blocks of \([Z,A]\) are singly bounded by \(\|Z\|_\infty\) times the corresponding block of \(A\), except the \((Q,P)\) block, bounded by \(\sqrt2\|Z\|_\infty\) times the Hilbert-space norm of the two diagonal blocks; the input block \(A_{PQ}\) contributes separately to the two output blocks \((Q,Q)\) and \((P,P)\). Orthogonality of these matrix blocks yields
\(\|[Z,A]\|_2\le\sqrt2\|Z\|_\infty\|A\|_2\).
Complex bilinear interpolation between the bounded maps \(\mathcal S_\infty(QH,PH)\times\mathcal S_2\to\mathcal S_2\) and \(\mathcal S_1(QH,PH)\times\mathcal B(H)\to\mathcal S_1\), with parameter \(\theta=1-2/q\), gives the asserted \(\mathcal S_r\times\mathcal S_q\to\mathcal S_{q'}\) estimate and interpolated constant \((\sqrt2)^{1-\theta}2^\theta=2^{1-1/q}\). The corner spaces interpolate isometrically as contractively complemented Schatten corners. The same proof applies to finite and infinite Hilbert spaces, by standard finite-rank approximation and duality.

**Lower bound and endpoint \(p=1\).** Let \(P\) project onto \(U\) and \(Q\) onto \(V\). Choose a Schatten-dual norming functional \(W=PWQ\) for \(T=PTQ\): when \(p>1\), take \(W=JD^{p-1}/\|T\|_p^{p-1}\in\mathcal S_{p'}\); when \(p=1\), take \(W=J\in\mathcal B(H)\). Thus \(\|W\|_{p'}=1\) (with \(p'=\infty\) at \(p=1\)) and \(\operatorname{Tr}(W^*T)=\|T\|_p\). For every factorization \(T=[A,B]\) with \(A,B\in\mathcal S_q\), cyclicity of trace and Schatten Hölder give
\[
\|T\|_p=|\operatorname{Tr}([W^*,A]B)|
\le\|[W^*,A]\|_{q'}\|B\|_q
\le2^{1-1/q}\|A\|_q\|B\|_q.
\]
The interpolation lemma applies because \(W^*=QW^*P\) and \(p'=q/(q-2)\). For \(p=1\) trace cyclicity is valid because products of two Hilbert–Schmidt operators are trace class. Rearranging gives \(\kappa_p(T)\ge2^{1/q-1}\|T\|_p\); together with the explicit upper bound, this proves the claim.

## Verification
The accompanying self-contained `verify.py` reconstructs the factors from arbitrary positive singular values in orthogonal corners and checks \([X,Y]=T\), both Schatten norms, and 504 randomly sampled finite-matrix consequences of the sharp corner commutator inequality across seven exponents and six dimensions. These numerical tests supplement but do not establish the universal interpolation proof. The mathematical proof covers arbitrary Hilbert dimension, all finite \(p\ge1\), and infinite-rank square-zero compact targets.

## Relationship to prior work
Dykema and Krishnaswamy-Usha, *Nilpotent elements of operator ideals as single commutators* (2017), establish qualitative factorization of nilpotents into prescribed fractional ideals; their theorem does not supply the present exact infimum of the product of two Schatten norms. Marcoux, Radjavi, and Zhang, *On commutators of square-zero Hilbert space operators* (2024), classify commutators **of two square-zero factors**, a different problem from optimizing unconstrained factors for a square-zero target. Recent quantitative Schatten-commutator and Schur-multiplier estimates of Hytönen--Quan (2026) and Long (2026) motivate seeking sharp ideal-norm constants but do not imply this factorization cost: their operators, input/output spaces, and optimizations differ. Related exact rank-free estimates for **normal** finite-rank commutator targets have a distinct target class: a nonzero square-zero operator cannot be normal. The later 2026 study of single commutators in Schatten ideals proves general factorization existence and non-sharp universal bounds, rather than the square-zero optimal constant here.

## Limitations
The theorem concerns nonzero square-zero Schatten targets only; it does not solve optimal commutator factorization for general nilpotents, arbitrary compact operators, or mixed-exponent factors. The originality assessment is based on inspected accessible primary texts, mathematical-result searches and available historical statements, not a proof of global publication priority. A later broad commutator paper was accessible only through its indexed summary, creating an explicit residual publication-priority uncertainty. No independent mathematical audit has been performed.

## References
1. T. Hytönen and X. Quan, *Schatten--Lorentz properties of commutators with matrix weights* (2026), arXiv:2610.16476v1, first public 2026-10-12.
2. Z. Long, *Sharp Hilbert transform norms on Schatten classes: classification and optimal spectral corrections* (2026), arXiv:2610.10158v1, first public 2026-10-07.
3. K. Dykema and A. Krishnaswamy-Usha, *Nilpotent elements of operator ideals as single commutators* (2017), arXiv:1706.03465.
4. L. W. Marcoux, H. Radjavi, and Y. Zhang, *On commutators of square-zero Hilbert space operators* (2024), arXiv:2402.15676.
5. Z. Liu and S. Yang, *Single commutators in Schatten ideals* (2026), arXiv:2610.27024v1 (first public 2026-10-19; comparative supporting literature only).
