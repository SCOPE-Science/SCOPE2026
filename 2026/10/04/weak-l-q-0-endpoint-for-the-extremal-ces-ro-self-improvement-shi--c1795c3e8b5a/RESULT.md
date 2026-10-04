# Weak-\(L^{q_0}\) endpoint for the extremal Cesàro self-improvement shift
## Finding
Fix \(1\le p<\infty\) and \(K>1\). Put
\[
\beta=1-K^{-1},\qquad \alpha=\frac{\beta}{p},\qquad q_0=\frac{p}{\beta}=\frac{pK}{K-1}.
\]
On \(\ell^p(\mathbb N)\), let \(W e_1=0\) and
\[
W e_j=\left(\frac{j}{j-1}\right)^{\alpha}e_{j-1}\qquad(j\ge2).
\]
For \(q\ge1\), call \(W\) weakly \(q\)-absolutely Cesàro bounded if there is \(A<\infty\) such that for every \(x\in\ell^p\), every integer \(N\ge1\), and every \(\lambda>0\),
\[
\#\left\{0\le k<N:\|W^k x\|_p>\lambda\right\}
\le A N\left(\frac{\|x\|_p}{\lambda}\right)^q.
\]
Then \(W\) is weakly \(q_0\)-absolutely Cesàro bounded. It is not strongly \(q_0\)-absolutely Cesàro bounded, and it is not weakly \(q\)-absolutely Cesàro bounded for any \(q>q_0\). Since Arnold proved that the same \(W\) is strongly \(q\)-absolutely Cesàro bounded exactly for \(1\le q<q_0\), the critical exponent is a genuine weak-Lorentz endpoint.

## Assumptions and scope
The scalar field may be real or complex. The result concerns the explicit positive weighted backward shifts above, not arbitrary \(p\)-absolutely Cesàro bounded operators. Arnold's normalization is used: the least constant in
\[
\frac1N\sum_{k=0}^{N-1}\|T^k x\|^p\le C_{p,\mathrm{ac}}(T)\|x\|^p
\]
is denoted \(C_{p,\mathrm{ac}}(T)\). For this shift, Arnold proves \(C_{p,\mathrm{ac}}(W)=K\) and strong \(q\)-absolute Cesàro boundedness exactly for \(q<q_0\).

## Proof
Let \(b_j=|x_j|^p\) and \(B=\sum_{j\ge1}b_j=\|x\|_p^p\). Telescoping the weights gives, for \(k\ge0\),
\[
(W^k x)_\ell=\left(\frac{\ell+k}{\ell}\right)^{\alpha}x_{\ell+k},
\]
and hence, with \(a_k=\|W^k x\|_p^p\),
\[
a_k=\sum_{\ell\ge1}\left(1+\frac{k}{\ell}\right)^{\beta}b_{k+\ell}.
\]
Because \(0<\beta<1\), subadditivity of \(t\mapsto t^\beta\) yields
\[
a_k\le B+k^\beta H_\beta b(k),\qquad
H_\beta b(k)=\sum_{\ell\ge1}\ell^{-\beta}b_{k+\ell}.
\]

Set \(r=1/\beta>1\). The one-sided fractional tail operator satisfies a weak estimate
\[
\sup_{t>0}t^r\#\{k\ge0:H_\beta b(k)>t\}\le C_\beta B^r.
\]
Here is a direct proof. Since \(H_\beta b(k)\le B\), only \(0<t\le B\) matters. Let
\[
L=\left\lceil\left(\frac{2B}{t}\right)^r\right\rceil.
\]
Split the kernel \(\ell^{-\beta}\) into \(\ell\le L\) and \(\ell>L\). The tail part is at most \(B L^{-\beta}\le t/2\). For the head part, Tonelli's theorem and Markov's inequality give
\[
\#\{H_\beta b>t\}
\le \frac{2B}{t}\sum_{\ell=1}^L\ell^{-\beta}
\le \frac{2B}{(1-\beta)t}L^{1-\beta}
\le C_\beta\left(\frac{B}{t}\right)^r,
\]
using \(1+r(1-\beta)=r\).

Now fix \(N\ge1\). For \(0\le k<N\),
\[
a_k\le B+N^\beta H_\beta b(k).
\]
If \(0<s\le2B\), then trivially
\[
s^r\#\{0\le k<N:a_k>s\}\le 2^r N B^r.
\]
If \(s>2B\), then \(a_k>s\) implies \(H_\beta b(k)>s/(2N^\beta)\), so the weak estimate above gives
\[
s^r\#\{0\le k<N:a_k>s\}\le C'_\beta N B^r.
\]
Taking \(s=\lambda^p\) and observing that \(pr=q_0\) proves
\[
\#\{0\le k<N:\|W^k x\|_p>\lambda\}\le C'_\beta N\left(\frac{\|x\|_p}{\lambda}\right)^{q_0}.
\]

The endpoint is proper. Arnold's Example 3.2 computes, for \(x=e_j\) and \(N=j\),
\[
\frac1j\sum_{k=0}^{j-1}\|W^k e_j\|_p^{q_0}
=\sum_{\ell=1}^j\frac1\ell\longrightarrow\infty,
\]
so strong \(q_0\)-absolute Cesàro boundedness fails. If \(q>q_0\), take \(x=e_j\), \(N=j\), and any \(\lambda<j^\alpha\). Since \(\|W^{j-1}e_j\|_p=j^\alpha\), the weak expression is at least \(\lambda^q/j\). Choosing \(\lambda=(1-\varepsilon)j^\alpha\) and letting \(j\to\infty\) gives divergence because \(\alpha q>\alpha q_0=1\). Thus weak \(q\)-absolute Cesàro boundedness fails for every \(q>q_0\).

## Verification
The proof was checked at the level of the exact iterate formula, the exponent identities \(r=1/\beta\), \(q_0=pr\), and \(\alpha q_0=1\), and the two threshold regimes \(s\le2B\) and \(s>2B\). The fractional-tail estimate is proved directly, so no unverified endpoint convolution theorem is being imported. Finite numerical spot checks on random nonnegative sequences were used only as a sanity check and are not part of the proof.

## Relationship to prior work
Arnold's 2026 paper proves the optimal strong self-improvement interval \(1\le q<q_0\) for every \(p\)-absolutely Cesàro bounded operator with constant \(K\), and its Example 3.2 gives exactly the weighted shift used here together with failure of strong \(q_0\)-absolute Cesàro boundedness. The paper does not state a weak-Lorentz endpoint; searches in its full text found no occurrence of “Lorentz” or “weak type”. Abbar--Arnold--Coine characterize strong \(q\)-absolute Cesàro boundedness of weighted backward shifts; their result is the strong theory used by Arnold's Example 3.2. Earlier work of Cohen--Cuny--Eisner--Lin develops \(p\)-absolute Cesàro boundedness and power-growth estimates but does not provide this orbit-distribution endpoint classification.

## Limitations
No weak-endpoint theorem is asserted for an arbitrary \(p\)-absolutely Cesàro bounded operator with constant \(K\). The proof uses the explicit telescoping weight structure of the extremal shift. The constant \(C'_\beta\) is finite and depends only on \(K\) through \(\beta\), but its optimal numerical value is not determined here. A broader theorem under different weak-orbit terminology could exist; the searches and inspected sources below did not reveal one.

## References
1. L. Arnold, *Self-improvement for absolutely Cesàro bounded operators*, arXiv:2610.00271v1, 2026.
2. A. Abbar, L. Arnold, C. Coine, *On absolutely Cesàro bounded operators*, arXiv:2609.24601v1, 2026.
3. G. Cohen, C. Cuny, T. Eisner, M. Lin, *Resolvent conditions and growth of powers of operators*, Journal of Mathematical Analysis and Applications 487 (2020), 124035, DOI:10.1016/j.jmaa.2020.124035.
