# Sharp finite-horizon power amplification under absolute Cesàro bounds

## Finding
For \(1\le p<\infty\) and \(K\ge1\), the sharp universal bound at each positive integer \(n\) for bounded operators with optimal \(p\)-absolute Cesàro constant \(K\) is
\[
\boxed{\ \|T^n\|^p\le B_n(K):=(K(n+1)-1)\prod_{j=2}^{n}\left(1-\frac1{Kj}\right).\ }
\]
The product is empty when \(n=1\). In particular,
\[
B_n(K)=\frac{(K(n+1)-1)\Gamma(n+1-1/K)}{\Gamma(2-1/K)\Gamma(n+1)}
\quad\text{and}\quad
B_n(K)\sim\frac{K}{\Gamma(2-1/K)}n^{1-1/K}.
\]
For every \(p,K\), one and the same positive backward shift \(W_{p,K}\) on \(\ell^p(\mathbb N_0)\) attains \(\|W_{p,K}^n\|^p=B_n(K)\) **for all** positive integers \(n\), and its optimal Cesàro constant equals \(K\). This is an exact finite-horizon extremal identity rather than only an order-of-growth estimate.

## Assumptions and scope
Let \(X\) be a nonzero real or complex Banach space, \(1\le p<\infty\), and \(T\in\mathcal L(X)\). Its optimal \(p\)-absolute Cesàro constant is
\[
C_{p,\mathrm{ac}}(T)=\sup_{x\ne0,\,N\ge1}\frac1{N\|x\|^p}\sum_{k=0}^{N-1}\|T^kx\|^p.
\]
Assume \(C_{p,\mathrm{ac}}(T)=K<\infty\). Then \(K\ge1\), since the length-one average equals \(\|x\|^p\). All bounds below are for every positive integer \(n\). No reflexivity, positivity or Hilbert-space hypothesis is made for the universal inequality. The extremizing example is on a classical \(\ell^p\) sequence lattice.

## Proof
**Universal inequality.** Fix \(n\ge1\) and \(x\in X\), and put \(a_k=\|T^kx\|^p\) and \(S_k=\sum_{j=k}^{n}a_j\), for \(0\le k\le n\). Applying the defining estimate to \(T^kx\) with horizon \(n-k+1\) gives
\[
S_k\le K(n-k+1)a_k.
\]
For \(0\le k<n\), this implies
\[
S_{k+1}\le (K(n-k+1)-1)a_k,
\quad S_k=a_k+S_{k+1}\ge\frac{K(n-k+1)}{K(n-k+1)-1}S_{k+1}.
\]
All denominators are positive because \(K\ge1\) and \(n-k+1\ge2\). Starting at \(k=1\), iteration gives
\[
a_n=S_n\le S_1\prod_{m=2}^{n}\left(1-\frac1{Km}\right).
\]
The estimate at \(k=0\) also gives \(S_1\le (K(n+1)-1)a_0\). Consequently \(a_n\le B_n(K)a_0\) for every \(x\). Taking the supremum over unit vectors establishes \(\|T^n\|^p\le B_n(K)\). This argument includes vectors with zero orbit terms; no division by an orbit norm occurs.

**A single simultaneous extremizer.** On \(\ell^p(\mathbb N_0)\), define \(W e_0=0\) and \(W e_j=w_j e_{j-1}\), with strictly positive weights
\[
w_1^p=2K-1,\qquad w_j^p=\frac{K(j+1)-1}{Kj}=1+\frac{K-1}{Kj}\quad(j\ge2).
\]
For \(K=1\), all weights are one. In general they are bounded and nonincreasing: \(w_1\ge w_2\ge\cdots\ge1\). Thus \(W\) is bounded, real-positive, and works over both scalar fields. Define \(P_0=1\) and \(P_j=\prod_{r=1}^{j}w_r^p\) for \(j\ge1\), and let
\[
A_j=\sum_{k=0}^{j}\|W^ke_j\|_p^p
=\sum_{r=0}^{j}\frac{P_j}{P_r}.
\]
The initial values are \(A_0=1\), \(A_1=1+w_1^p=2K\). For every \(j\ge2\),
\[
A_j=1+w_j^p A_{j-1}=1+\frac{K(j+1)-1}{Kj}\,Kj=K(j+1).
\]
For fixed \(j\), the successive nonzero orbit norms \(\|W^k e_j\|_p^p\) are nondecreasing in \(k\) because all weights are at least one. Thus every partial average of the first \(N\le j+1\) orbit terms is at most the full average \(A_j/(j+1)=K\), for \(j\ge1\). When \(N>j+1\), the later terms vanish, giving an average at most \(K(j+1)/N\le K\). For \(j=0\), the orbit averages are at most one. Therefore
\[
\sum_{k=0}^{N-1}\|W^ke_j\|_p^p\le KN\quad(j\ge0,\ N\ge1).
\]
For arbitrary \(x=(x_j)\in\ell^p\), coordinate disjointness in each \(W^kx\), followed by Tonelli's theorem for the nonnegative double series, gives
\[
\sum_{k=0}^{N-1}\|W^kx\|_p^p
=\sum_{j\ge0}|x_j|^p\sum_{k=0}^{N-1}\|W^ke_j\|_p^p
\le KN\sum_{j\ge0}|x_j|^p.
\]
Hence \(C_{p,\mathrm{ac}}(W)\le K\); equality holds by taking \(x=e_1\) and \(N=2\), because its average is \((1+w_1^p)/2=K\).

Since the weights are nonincreasing, the norm of the \(n\)-fold weighted backward shift is attained on \(e_n\) and satisfies
\[
\|W^n\|^p=\sup_{j\ge n}\prod_{r=j-n+1}^{j}w_r^p=\prod_{r=1}^{n}w_r^p
=(K(n+1)-1)\prod_{r=2}^{n}\left(1-\frac1{Kr}\right)=B_n(K).
\]
This simultaneously proves attainability and sharpness for every horizon.

**Closed form.** The identity \(\prod_{r=2}^{n}(1-1/(Kr))=\Gamma(n+1-1/K)/(\Gamma(2-1/K)\Gamma(n+1))\) follows by the Gamma recurrence; the asymptotic follows from the usual Gamma quotient formula. For \(K=1\), this reduces exactly to \(B_n(1)=1\), consistent with the contraction boundary.

## Verification
The estimates above are analytic for all stated \(p\), \(K\), \(n\), and Banach spaces. The included `verify_finite.py` independently evaluates the rational recurrences exactly for \(K\in\{1,5/4,3/2,2,7/2,17/3\}\) and horizons through eleven; it checks coordinate Cesàro inequalities, monotonicity, products and attained power norms without floating-point rounding. These finite checks test implementation and normalization but do not prove the universal or infinite claims, which are established above.

## Relationship to prior work
Cohen, Cuny, Eisner and Lin (2019 preprint; 2020 publication), Proposition 3.1 and Lemma 3.2, give a polynomial upper growth estimate with the same previously known exponent but with a non-sharp constant depending also on the operator norm. Abbar, Arnold and Coine (2026), Theorem 3.4 and Section 3.3, characterize \(p\)-absolute Cesàro bounds for weighted backward shifts and exhibit multiple rates of power growth, but do not state this exact universal finite-horizon envelope or a single shift attaining all its values. Arnold (2026), Theorem 3.1 and Example 3.2, gives the exact self-improvement exponent threshold and a different power-law shift. The present claim is the *universal sharp coefficient-and-horizon profile* and its common extremizer, not a claim to discover the growth exponent or the underlying Cesàro condition.

## Limitations
The theorem does not assert uniqueness of extremizers, stability of near-extremizers, sharp control of arbitrary spectral quantities, or any corresponding statement for stronger \(q\)-Cesàro assumptions. It is for ordinary positive-integer powers and \(1\le p<\infty\); finite experiments do not extend the parameter range. Literature coverage may be incomplete, and an unindexed earlier extremal inequality could coincide with the statement. No independent audit has been performed.

## References
1. A. Abbar, L. Arnold and C. Coine, *On absolutely Cesàro bounded operators*, arXiv:2609.24601v1, first public 21 September 2026; notably Theorem 3.4, Proposition 3.15 and Section 3.3. https://arxiv.org/abs/2609.24601
2. L. Arnold, *Self-improvement for absolutely Cesàro bounded operators*, arXiv:2610.00271v1, first public 24 September 2026; notably Theorem 3.1 and Example 3.2. https://arxiv.org/abs/2610.00271
3. G. Cohen, C. Cuny, T. Eisner and M. Lin, *Resolvent conditions and growth of powers of operators*, arXiv:1912.10507, Proposition 3.1 and Lemma 3.2; Journal of Mathematical Analysis and Applications 487 (2020), 124035, DOI:10.1016/j.jmaa.2020.124035.
