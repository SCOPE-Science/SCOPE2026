# Exact harmonic finite-horizon profile at the extremal Cesàro endpoint
## Finding
Fix \(1\le p<\infty\) and \(K>1\), and write
\[
\beta=1-K^{-1},\qquad \alpha=\beta/p,\qquad q_0=\frac{pK}{K-1}=\frac p\beta.
\]
On \(\ell^p(\mathbb N)\), consider the positive weighted backward shift
\[
W e_1=0,\qquad W e_j=\left(\frac{j}{j-1}\right)^\alpha e_{j-1}\quad(j\ge2).
\]
For every integer \(N\ge1\), define
\[
\mathcal C_N(W,q_0)=\sup_{x\ne0}\frac{1}{N\|x\|_p^{q_0}}\sum_{k=0}^{N-1}\|W^k x\|_p^{q_0}.
\]
Then the exact value is
\[
\mathcal C_N(W,q_0)=H_N:=\sum_{\ell=1}^N\frac1\ell.
\]
The value is attained by \(e_N\). Thus the failure of strong \(q_0\)-absolute Cesàro boundedness for this extremal shift has the exact finite-horizon harmonic profile.

## Assumptions and scope
The scalar field may be real or complex. The parameters satisfy \(1\le p<\infty\) and \(K>1\), so \(0<\beta<1\) and \(q_0>p\). The result concerns the specific extremal positive weighted shift above. It does not assert a universal endpoint formula for arbitrary \(p\)-absolutely Cesàro bounded operators.

The quantity \(\mathcal C_N(W,q_0)\) is the optimal unrooted \(q_0\)-moment constant on the first \(N\) iterates. If one instead normalizes with an outer \(q_0\)-th root, the corresponding optimal constant is \(H_N^{1/q_0}\).

## Proof
Let \(x=(x_j)_{j\ge1}\in\ell^p\) and set \(b_j=|x_j|^p\). Telescoping the weights gives, for every \(k\ge0\),
\[
\|W^k x\|_p^p=
\sum_{j>k}\left(\frac{j}{j-k}\right)^\beta b_j.
\]
Put \(r=q_0/p=1/\beta>1\). For fixed \(N\), define a nonnegative vector \(a^{(j)}\in\ell^r(\{0,\ldots,N-1\})\) by
\[
a^{(j)}_k=
\begin{cases}
\left(\dfrac{j}{j-k}\right)^\beta b_j,&0\le k<\min\{N,j\},\\
0,&\text{otherwise}.
\end{cases}
\]
Then
\[
\sum_{k=0}^{N-1}\|W^k x\|_p^{q_0}
=\left\|\sum_{j\ge1}a^{(j)}\right\|_{\ell^r}^{r}.
\]
Minkowski's inequality yields
\[
\left(\sum_{k=0}^{N-1}\|W^k x\|_p^{q_0}\right)^{1/r}
\le \sum_{j\ge1}\|a^{(j)}\|_{\ell^r}.
\]
Since \(\beta r=1\),
\[
\|a^{(j)}\|_{\ell^r}
=b_j A_{j,N}^{\beta},
\qquad
A_{j,N}:=j\sum_{\ell=\max\{1,j-N+1\}}^j\frac1\ell.
\]
Therefore
\[
\left(\sum_{k=0}^{N-1}\|W^k x\|_p^{q_0}\right)^\beta
\le \left(\sup_{j\ge1}A_{j,N}\right)^\beta\sum_{j\ge1}b_j.
\]
For \(j\le N\), one has \(A_{j,N}=jH_j\le NH_N\). For \(j\ge N\),
\[
A_{j,N}=\sum_{k=0}^{N-1}\frac{j}{j-k}.
\]
For every fixed \(k\), the summand is nonincreasing in \(j\ge N\), so this expression is maximized at \(j=N\). Hence
\[
\sup_{j\ge1}A_{j,N}=NH_N.
\]
Raising the preceding inequality to the power \(1/\beta=r\) gives
\[
\sum_{k=0}^{N-1}\|W^k x\|_p^{q_0}
\le NH_N\|x\|_p^{q_0}.
\]
Finally, for \(x=e_N\), telescoping gives
\[
\frac1N\sum_{k=0}^{N-1}\|W^k e_N\|_p^{q_0}
=\frac1N\sum_{k=0}^{N-1}\frac{N}{N-k}=H_N.
\]
This proves both sharpness and the stated formula. The countable use of Minkowski follows by applying it to finite coordinate truncations and passing to the monotone limit.

## Verification
The critical exponent identities used in the proof are \(q_0/p=1/\beta\) and \(\alpha q_0=1\). The finite-horizon maximization is exact: the auxiliary coefficient \(A_{j,N}\) is bounded by \(NH_N\) on both regimes \(j\le N\) and \(j\ge N\), with equality at \(j=N\). The boundary case \(N=1\) gives \(\mathcal C_1(W,q_0)=1=H_1\), as required.

No finite experiment is used to infer the result. The proof is a direct infinite-dimensional inequality, with finite-coordinate truncation used only to justify the countable Minkowski step.

## Relationship to prior work
Abbar, Arnold and Coine characterize \(q\)-absolute Cesàro boundedness of weighted backward shifts and identify the exact global constant when it is finite. Arnold then uses the shift above to prove the optimality of the self-improvement range and observes, on the basis vectors \(e_j\), the endpoint lower bound
\[
\frac1j\sum_{k=0}^{j-1}\|W^k e_j\|_p^{q_0}=H_j\longrightarrow\infty.
\]
That computation proves endpoint failure but does not determine the supremum over all vectors at each fixed horizon. The result here supplies the matching upper bound and hence the exact finite-horizon profile for every \(N\).

A related published result gives a weak-\(L^{q_0}\) endpoint for the same shift. Such a weak estimate implies only logarithmic-order control of strong finite moments with non-sharp constants; it does not imply the exact value \(H_N\). Another published result classifies the feasible supremal strong exponents at fixed \(p\)-Cesàro constant, but does not determine finite-horizon endpoint constants.

## Limitations
No classification of all extremizing vectors is claimed; \(e_N\) is an explicit extremizer. No corresponding exact endpoint formula is asserted for arbitrary \(p\)-absolutely Cesàro bounded operators, for general weighted shifts, or for weak endpoint constants. An older equivalent finite-section inequality could exist under weighted Hardy-matrix terminology; the inspected sources and targeted searches did not reveal one.

## References
1. A. Abbar, L. Arnold and C. Coine, *On absolutely Cesàro bounded operators*, arXiv:2609.24601v1, first public 21 September 2026.
2. L. Arnold, *Self-improvement for absolutely Cesàro bounded operators*, arXiv:2610.00271v1, first public 24 September 2026.
