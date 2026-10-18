# Antipodal convolution and reciprocal degree recurrences for inverse odd-cycle Cremona maps

## Finding
For every odd \(n=2s+1\ge3\), the inverse of the standard quadratic odd-cycle monomial Cremona map has a closed all-iterate degree formula, an order-\(s\) linear recurrence on each parity subsequence, and a simple algebraic dynamical degree. Specifically, put \(L=s+1\), \(A(u)=1+u+\cdots+u^s\), \(b_{r,k}=\sum_{a\equiv k\pmod n}[u^a]A(u)^r\), and \(k_r=\lfloor(rs+n)/2\rfloor\pmod n\). Then
\[
 d_r=L^r-nb_{r,k_r}\qquad (r\ge0).
\]
The coefficient at \(k_r\) is always a **minimum**, not an arbitrarily chosen sample. Define
\[
 P_s(T)=\sum_{j=0}^s(-1)^j\binom{2s-j}{j}T^{s-j},\qquad R_s(T)=(-1)^sT^sP_s(T^{-1})=T^s+c_1T^{s-1}+\cdots+c_s.
\]
Then
\[
 d_{r+2s}+c_1d_{r+2s-2}+\cdots+c_sd_r=0\quad\text{for every }r\ge0,
\]
and \(R_s\) is the **minimal** characteristic polynomial of each individual parity subsequence. Moreover
\[
 \lambda_1(G_n)=\lim_{r\to\infty}d_r^{1/r}=\frac1{2\sin(\pi/(2n))}.
\]

## Assumptions and scope
Let \(K\) be any field, and \(n=2s+1\) any odd integer at least three. All coordinate indices are taken modulo \(n\). The map
\[
 F_n:[x_0:\ldots:x_{n-1}]\dashrightarrow[x_0x_1:x_1x_2:\ldots:x_{n-1}x_0]
\]
is birational. Set \(G=F_n^{-1}\); \(G^0\) is the identity. Projective degree means common total degree **after cancelling the greatest common monomial factor** of a monomial coordinate presentation. No smooth extension to the boundary is presumed. The eigenvalue computation uses complex roots of unity to derive identities among integers and therefore imposes no characteristic restriction on \(K\).

## Proof
**1. Inverse monomials and the degree of an iterate.** Let \(S\) denote the cyclic permutation matrix on \(n\) coordinates. The exponent matrix of \(F\) is \(B=I+S\), and put \(H=\sum_{j=0}^sS^{2j}\). Since \(2(s+1)=n+1\), multiplication and a cyclic count give \((I+S)H=I+J\), with \(J\) the all-ones matrix. The common \(J\) factor is projectively irrelevant. Thus
\[
 G_i(y)=\prod_{j=0}^s y_{i+2j},\qquad \deg(G)=s+1.
\]
Writing \(U=S^2\), we have \(H=A(U)\). Consequently the exponent matrix of the unreduced \(r\)-th iterate is
\[
 H^r=\sum_{k=0}^{n-1}b_{r,k}U^k.
\]
Every coordinate has total degree \(L^r\). As \(U\) is an \(n\)-cycle, every variable occurs across coordinates with exponent multiset \(\{b_{r,0},\ldots,b_{r,n-1}\}\). Thus the greatest common monomial factor has total degree \(n\min_k b_{r,k}\), giving \(d_r=L^r-n\min_kb_{r,k}\). This formula remains valid for \(r=0\).

**2. The antipodal minimum for every convolution power.** Embed residue indices as equally spaced points on a circle of circumference \(n\). A nonnegative function on these points is *circularly symmetric unimodal around a center* \(c\in\frac12\mathbb Z\) when it depends only on shortest circular distance from \(c\) and is nonincreasing with that distance. Such a function is a nonnegative linear combination of indicators of consecutive centered arcs (take successive differences between radial levels). If \(a,b\le n\) are the arc lengths, the overlap of their circular translates whose centers are distance \(0\le t\le n/2\) apart is
\[
 I_{a,b}(t)=\max\{0,\min(a,b,(a+b)/2-t)\}+\max\{0,(a+b)/2+t-n\}.
\]
For arcs made of unit cells, the permitted discrete distances make the right side integral. This expression is nonincreasing in \(t\): the first term is constant then decreases at slope \(-1\) until zero, and the second can start increasing only during that decreasing part (or after the first reaches zero, when their sum stays at the unavoidable overlap \(a+b-n\)). Indeed if \(a+b>n\), the second starts at \(t=n-(a+b)/2\), while the first reaches zero at \(t=(a+b)/2\), and \(n-(a+b)/2<(a+b)/2\); in their common linear regime the slopes cancel. If \(a+b\le n\), the second is zero for \(t\le n/2\). Therefore convolution preserves circular symmetric unimodality and adds centers.

The coefficients of \(A(u)\) form the unit-height arc of length \(s+1\), centered at \(s/2\). By repeated convolution, \(b_{r,k}\) is symmetric unimodal around \(rs/2\) modulo \(n\). Its smallest value is at a residue most distant from this center. Because \(n=2s+1\) is odd, \(k_r=\lfloor(rs+n)/2\rfloor\pmod n\) is such a residue (when the center is integral there are two antipodes). Substitution proves the asserted exact degree formula.

**3. Root-of-unity reduction and the reciprocal polynomial.** Let \(\zeta=e^{2\pi i/n}\). The cyclic Fourier filter gives
\[
 b_{r,k}=\frac1n\sum_{h=0}^{n-1}\zeta^{-hk}A(\zeta^h)^r,
\qquad
 d_r=-\sum_{h=1}^{n-1}\zeta^{-hk_r}A(\zeta^h)^r.
\]
For every nontrivial \(n\)-th root \(u\), the identity \(2s+2=n+1\) implies \(A(u)(1+u^{s+1})=1\). Moreover, \(A(\zeta^h)=\zeta^{hs/2}\sin((s+1)\pi h/n)/\sin(\pi h/n)\). Put
\[
 \beta_h=\zeta^{-hs}A(\zeta^h)^2
 =\left[\frac{\sin((s+1)\pi h/n)}{\sin(\pi h/n)}\right]^2
 =\frac1{4\cos^2(\pi(s+1)h/n)}.
\]
Then \(\beta_h=\beta_{n-h}>0\). Multiplication by \(s+1\) permutes the nonzero residue classes modulo \(n\) up to sign. Hence \(\{\beta_h:1\le h\le s\}\) is exactly
\[
 \left\{\frac1{4\cos^2(\pi j/n)}:1\le j\le s\right\},
\]
with distinct nonzero elements. The polynomial with reciprocal roots \(4\cos^2(\pi j/n)\) is \(P_s(T)\) above: indeed the standard recurrence \(Q_{k+1}(T)=(T-2)Q_k(T)-Q_{k-1}(T)\), with \(Q_0=1\), \(Q_1=T-1\), yields the displayed binomial coefficients and these roots by \(T=4\cos^2\theta\). Alternatively direct substitution via the trigonometric identity \(\sin((2s+1)\theta)/\sin\theta\). Since \(P_s(0)=(-1)^s\), the monic polynomial with roots \(\beta_1,\ldots,\beta_s\) is \(R_s(T)=(-1)^sT^sP_s(T^{-1})\).

For \(r=2t\), the antipodal index is \(k_{2t}=ts+s\). Therefore
\[
 d_{2t}=-\sum_{h=1}^{n-1}\zeta^{-hs}\beta_h^t.
\]
For \(r=2t+1\), put \(k_* =\lfloor(3s+1)/2\rfloor\), so that \(k_{2t+1}=ts+k_*\), and similarly
\[
 d_{2t+1}=-\sum_{h=1}^{n-1}\zeta^{-hk_*}A(\zeta^h)\beta_h^t.
\]
Pairing the terms \(h\) and \(n-h\) gives a sum of precisely \(s\) distinct exponential modes for either parity. Their coefficients cannot vanish: in the even case they are \(-2\cos(2\pi hs/n)\), nonzero since \(n\) is odd; in the odd case the trigonometric expression above gives a nonzero sine-ratio times \(-2\cos(\pi h(s-2k_*)/n)\). If \(s\) is odd then \(s-2k_*=-n\), giving cosine \((-1)^h\); if \(s\) is even then \(s-2k_*=-2s\), whose cosine is nonzero for odd \(n\). Thus the minimal characteristic polynomial for **each** parity subsequence is \(R_s\), and substituting its coefficients gives the stated recurrence for all \(r\ge0\).

**4. Dynamical degree.** The largest of the distinct positive modes is \(\beta_1=1/[4\sin^2(\pi/(2n))]\). The nonzero coefficient of this mode in each parity expansion proves \(\lim_{r\to\infty}d_r^{1/r}=\sqrt{\beta_1}=1/[2\sin(\pi/(2n))]\). Positivity of degrees ensures there is no cancellation of the unique dominant mode within a parity.

## Verification
The standalone `verify_inverse.py` uses exact integer arithmetic. It independently constructs (i) the circular-convolution coefficient vectors and (ii) the exponent matrices of iterated monomials, checks the claimed antipodal minima, and tests the full reciprocal recurrence. On execution it reports `VERIFY_OK`: 50 odd dimensions (\(3\) through \(101\)), degrees through iteration \(90\) for \(n\le51\) and through iteration \(35\) otherwise, 1,584 exact recurrence instances, and 81 direct exponent-matrix comparisons. This finite check is corroboration, not the infinite proof.

## Relationship to prior work
Russo–Simis (2001) and Costa–Simis (2011) establish the quadratic odd-cycle Cremona map and the degree and monomial coordinates of its inverse. Hasselblatt–Propp (2008; available from their 2006 preprint) supplies general integer-matrix formulas for degrees and entropy of monomial maps, without the explicit all-iterate inverse cycle formula or a reciprocal finite-order recurrence. Sun (2004) gives circular-unimodality properties of **binomial** residue sums, closely related to the *forward* cycle powers; these do not directly cover the inverse's uniform-arc convolution and its parity-dependent antipodal residues. The new claim is the all-dimensional inverse iterate formula and its minimal parity recurrences, not the known inversion formula or the general spectral-radius principle. Published-record and primary-literature searches also considered the general degree-growth results of Favre–Wulcan (2012); no stronger implication covering the specific recurrence was identified.

## Limitations
The result applies to the standard consecutive-edge quadratic odd-cycle map, not arbitrary graph-monomial Cremona maps or arbitrary circulants. It describes **algebraic degrees of iterates**, not individual higher dynamical degrees. Root-of-unity expressions are auxiliary characteristic-zero identities for field-independent integer sequences. The linear recurrence is minimal separately on even and odd subsequences; no assertion is made about the minimal order of a recurrence with unit shifts in \(r\). Novelty comparisons cannot exclude every uncatalogued or inaccessible source; the result has received mathematical reconstruction and reproducibility checks but no independent audit.

## References
- F. Russo and A. Simis, *On Birational Maps and Jacobian Matrices*, Compositio Mathematica 126 (2001), 335–358, DOI:10.1023/A:1017572213947.
- B. Costa and A. Simis, *Cremona maps defined by monomials*, preprint arXiv:1101.2413 (2011).
- B. Hasselblatt and J. Propp, *Degree-growth of monomial maps*, arXiv:math/0604521 (2006), Ergodic Theory and Dynamical Systems 28 (2008), 1369–1375.
- Z.-W. Sun, *On sums of binomial coefficients and their applications*, arXiv:math/0404385 (2004).
- C. Favre and E. Wulcan, *Degree growth of monomial maps and McMullen's polytope algebra*, arXiv:1011.2854 (2010), Indiana University Mathematics Journal 61 (2012), 493–524.
