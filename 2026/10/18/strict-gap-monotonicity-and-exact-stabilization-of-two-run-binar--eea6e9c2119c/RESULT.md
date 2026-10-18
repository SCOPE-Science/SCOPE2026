# Strict gap monotonicity and exact stabilization of two-run binary digit-sum biases

## Finding

For integers \(r,s,g\ge1\), define the binary Hamming weight \(s_2(n)\), the two-run shift
\[
t_g=(2^r-1)+2^{r+g}(2^s-1),\qquad w=r+s,
\]
and its digit-sum bias
\[
c_g=\lim_{X\to\infty}\frac1X\#\{0\le n<X:s_2(n+t_g)\ge s_2(n)\}.
\]
The limit exists. For every integer \(h\), define
\[
N_h=\#\{(i,j):0\le i<r,\ 0\le j<s,\ i+j=h\},
\]
with \(N_h=0\) for negative indices.

**Theorem.** Whenever \(1\le g<w\), with \(h=w-g-1\),
\[
\boxed{c_{g+1}-c_g=4^{-(g+1)}\left(N_h-\sum_{k=1}^h\frac{N_{h-k}}{4^k}\right)>0.}
\]
For every \(g\ge w\), one has \(c_{g+1}=c_g\). Consequently the smallest separating gap where the sequence becomes permanently constant is **exactly** \(r+s\), for every pair \((r,s)\).

For example, when \(r=s=1\), \(c_1=5/8\) and \(c_g=11/16\) for all \(g\ge2\). When \(r=s=2\), the values for gaps \(1,2,3,4\) are \(73/128,153/256,5/8,161/256\), with the last value thereafter constant.

## Assumptions and scope

All parameters \(r,s,g\) are arbitrary positive integers and \(w=r+s\). The digit blocks are consecutive ones of lengths \(r\) and \(s\), with exactly \(g\) zeros between them; the least-significant digit is one. The theorem concerns the ordinary natural density, not just dyadic subsequences. It does **not** assert monotonicity under arbitrary changes to shifts with three or more one-blocks.

## Proof

**1. Carry interpretation and existence.** Binary addition of \(n\) and \(t_g\) has a number \(C(n,t_g)\) of carries, counted once at each position producing an outgoing carry. The elementary digit-sum identity
\[
s_2(n+t_g)-s_2(n)=s_2(t_g)-C(n,t_g)=w-C(n,t_g)
\]
reduces the event to \(C(n,t_g)\le w\). Each fixed finite initial block of binary digits of \(n\) has natural frequency \(2^{-m}\). After all nonzero digits of the shift, an ongoing carry survives each further random binary digit with probability \(1/2\), so truncation after \(m\) additional positions incurs probability at most \(2^{-m}\). This gives natural density by finite-residue approximations, including arbitrary cutoffs \(X\).

**2. Exact probability-generating matrices.** Let \(z\) mark one newly produced carry. In ascending digit order, with row/column indexed by incoming/outgoing carry \(0,1\), the two matrices are
\[
M_0(z)=\begin{pmatrix}1&0\\1/2&z/2\end{pmatrix},\qquad
M_1(z)=\begin{pmatrix}1/2&z/2\\0&z\end{pmatrix}.
\]
The eventual tail, after all shift digits have been read, is encoded by \(v(z)=(1,1/(2-z))^{\mathsf T}\). Indeed, once a carry is present, the number of *further* carries has geometric probability \(2^{-(j+1)}\) for \(j\ge0\). Thus the full carry probability-generating function is
\[
G_g(z)=(1,0)M_1(z)^r M_0(z)^g M_1(z)^s v(z),
\qquad c_g=\sum_{k=0}^w[z^k]G_g(z).
\]
All displayed series are absolutely convergent for \(|z|<2\), sufficient for coefficient extraction.

**3. Effect of one separating zero.** Set \(S_m(z)=\sum_{j=0}^{m-1}(2z)^j\). Direct multiplication gives
\[
(M_1^r)_{0,1}=\frac{zS_r(z)}{2^r},\qquad
M_0^g=\begin{pmatrix}1&0\\\frac{1-(z/2)^g}{2-z}&(z/2)^g\end{pmatrix}.
\]
For \(u=M_1^s v\), the needed difference simplifies exactly to
\[
u_1-\frac{u_0}{2-z}=-\frac{(1-z)^2S_s(z)}{2^{s-1}(2-z)^2}.
\]
Consequently
\[
G_{g+1}(z)-G_g(z)
=\frac{z^{g+1}(1-z)^2 S_r(z)S_s(z)}{2^{w+g}(2-z)}.
\]
Summing coefficients through degree \(w\) amounts to dividing by \(1-z\) and extracting degree \(w\). Therefore, with \(h=w-g-1\),
\[
c_{g+1}-c_g=2^{-(w+g)}[z^h]\frac{1-z}{2-z}S_r(z)S_s(z).
\]
As \([z^m]S_rS_s=2^mN_m\) and
\[
\frac{1-z}{2-z}=\frac12-\sum_{k\ge1}\frac{z^k}{2^{k+1}},
\]
we obtain precisely the displayed increment. When \(g\ge w\), the index \(h\) is negative, giving zero.

**4. Strict positivity and sharpness.** For \(0\le h\le w-2\), \(N_h\ge1\). The convolution sequence \(N_h\) of two interval indicators changes by at most one between adjacent indices; hence \(N_{h-k}\le N_h+k\) for \(k\ge1\). It follows that
\[
N_h-\sum_{k=1}^h\frac{N_{h-k}}{4^k}
\ge N_h-\sum_{k\ge1}\frac{N_h+k}{4^k}
=\frac23N_h-\frac49\ge\frac29>0.
\]
For every \(1\le g<w\), \(h\) lies between \(0\) and \(w-2\); thus the increment is strictly positive. In particular the last increase occurs from \(g=w-1\) to \(g=w\), so the stabilization gap cannot be lowered. \(\square\)

## Verification

The standalone Python 3 program `verify.py` evaluates both the two-state exact carry process and an independent enumeration of initial residue classes with a geometric carry tail. It checks the exact increment and eventual stabilization for all \(1\le r,s\le9\) and relevant gaps (972 comparisons), plus 45 independent residue-class comparisons with \(1\le r,s\le3\). It also confirms the displayed examples. Run `python3 verify.py`; the expected output begins with `VERIFY_OK`. These finite checks supplement, but do not substitute for, the general proof above.

## Relationship to prior work

Cusick's digit-sum conjecture motivated the archived 2015 paper of Drmota–Kauers–Spiegelhofer, which supplies the classical correlation setting and related transfer recurrences. The 2020 work of Spiegelhofer–Wallner studies dependence on one-block structure and normal approximation as the number of blocks grows. Sobolewski–Spiegelhofer (initial preprint 2024) derives a general exact correlation decomposition and, in Section 5.3, explicit two-block estimates proving \(c_t>5/9\); Section 6.1 proposes extremal inequalities under changes in block lengths. Its general expressions can calculate individual biases but the inspected arguments do **not** state or establish the strictly increasing separation law and exact optimal finite saturation threshold proved here. The 2026 first-exit proof establishes the global inequality \(c_t>1/2\), a different conclusion which does not imply monotonic separation. The underlying two-state matrix method and existence of the correlation densities are known: the asserted contribution is solely the explicit signed gap-difference identity, its strict positivity, and exact stabilization cutoff.

## Limitations

The result is restricted to exactly two nonempty runs of ones. It does not solve a general block-length monotonicity conjecture or classify correlations of three or more runs. Priority remains subject to scrutiny of unindexed equivalent reductions of the general exact decompositions, especially Sobolewski–Spiegelhofer's two-block formula; a general formula that can evaluate these values is not itself the asserted new inequality. No independent audit has been performed.

## References

1. M. Drmota, M. Kauers and L. Spiegelhofer, *On a Conjecture of Cusick Concerning the Sum of Digits of n and n + t*, arXiv:1509.08623, first posted 2015-09-29; SIAM J. Discrete Math. 30 (2016), 621–649. https://arxiv.org/abs/1509.08623
2. L. Spiegelhofer and M. Wallner, *The binary digits of n+t*, arXiv:2005.07167 (2020). https://arxiv.org/abs/2005.07167
3. B. Sobolewski and L. Spiegelhofer, *Decomposing the sum-of-digits correlation measure*, arXiv:2411.07779, first posted 2024-11-12; see Sections 2, 5.3 and 6.1. https://arxiv.org/abs/2411.07779
4. K. Cheng, *A first-exit proof of Cusick's sum-of-digits conjecture*, arXiv:2606.23398 (2026). https://arxiv.org/abs/2606.23398
