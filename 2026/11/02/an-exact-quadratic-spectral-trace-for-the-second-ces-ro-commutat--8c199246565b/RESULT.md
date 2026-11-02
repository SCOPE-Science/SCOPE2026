# An exact quadratic spectral trace for the second Cesàro commutator

## Finding
Let \(M\) be the unshifted generalized order-two Cesàro matrix on complex \(\ell^2(\mathbb N_0)\). Its positive self-commutator \(K=M^*M-MM^*\) has the exact quadratic trace
\[
\operatorname{Tr}(K^2)=\|K\|_{\mathcal S_2}^2=\frac{448}{3}\zeta(3)-\frac{40\pi^2}{27}-\frac{13066}{81}=3.576886080095425209\ldots.
\]
This is a second spectral moment, not the trace of \(K\), which is already known to be \(22/9\).

## Assumptions and scope
Indices start at zero. Precisely, \(M_{nj}=2(n-j+1)/((n+1)(n+2))\) for \(0\le j\le n\), and \(M_{nj}=0\) otherwise. The space is the complex Hilbert space \(\ell^2(\mathbb N_0)\), and the operator order is exactly two, with unshifted parameter zero. We write \(H_N=\sum_{j=1}^N 1/j\), \(\zeta(s)=\sum_{j\ge1}j^{-s}\) for \(s>1\).

## Proof
**Step 1: positive factorization and trace-class convergence.** The diagonal-interrupter identity for the unshifted second Cesàro matrix [1,2] reads
\[
MM^*=M^*PM,\qquad P_{nn}=\frac{(n+1)(n+2)}{(n+3)(n+4)}.
\]
Put \(r_n=1-P_{nn}=(4n+10)/((n+3)(n+4))>0\) and \(R=\operatorname{diag}(r_n)\). Then \(K=M^*RM=B^*B\), where \(B=R^{1/2}M\). Since
\[
\sum_{j=0}^n |M_{nj}|^2=\frac{2(2n+3)}{3(n+1)(n+2)}=O((n+1)^{-1}),
\]
we have \(\|B\|_{\mathcal S_2}^2=\sum_n r_n\sum_j |M_{nj}|^2<\infty\). Thus \(K\ge0\) is trace class and \(\operatorname{Tr}(K^2)=\operatorname{Tr}((BB^*)^2)\); all rearrangements below are absolutely valid.

**Step 2: exact Gram entries.** For \(n\ge l\), summing \(M_{nj}M_{lj}\) over \(0\le j\le l\) gives
\[
(MM^*)_{nl}=\frac{2(3n-l+3)}{3(n+1)(n+2)}.
\]
Indeed, after setting \(k=l-j+1\), the finite numerator sum is \(\sum_{k=1}^{l+1}k(k+n-l)=(l+1)(l+2)(3n-l+3)/6\). Since \((BB^*)_{nl}=\sqrt{r_n r_l}(MM^*)_{nl}\), grouping diagonal and symmetric off-diagonal entries yields
\[
\operatorname{Tr}(K^2)=\sum_{n=0}^\infty T_n,\qquad
T_n=\frac{4r_n}{9(n+1)^2(n+2)^2}\left[r_n(2n+3)^2+2\sum_{l=0}^{n-1}r_l(3n-l+3)^2\right].
\]

**Step 3: finite sums and partial fractions.** Set \(h=H_{n+2}\) and \(S_j=\sum_{l<n}l^jr_l\). Partial fractioning \(r_l=-2/(l+3)+6/(l+4)\) gives exactly
\[
\begin{aligned}
S_0&=4h+6/(n+3)-8,\\
S_1&=4n-18h-24/(n+3)+35,\\
S_2&=2n^2-20n+78h+96/(n+3)-149.
\end{aligned}
\]
Insert \(\sum_{l<n}r_l(3n-l+3)^2=(3n+3)^2S_0-2(3n+3)S_1+S_2\). Exact rational simplification gives \(T_n=A_nH_{n+2}+D_n\), with
\[
\begin{aligned}
A_n={}&\frac{104}{9(n+4)}-\frac{8}{3(n+3)}+\frac{136}{3(n+2)}+\frac{16}{3(n+2)^2}-\frac{488}{9(n+1)}+\frac{208}{3(n+1)^2},\\
D_n={}&-\frac{56}{n+4}+\frac{100}{9(n+4)^2}+\frac{464}{9(n+3)}-\frac{20}{3(n+3)^2}-\frac{40}{9(n+2)}-\frac{4}{(n+2)^2}+\frac{80}{9(n+1)}-\frac{628}{9(n+1)^2}.
\end{aligned}
\]
Each entire sum converges despite the individually separated harmonic first-order poles; in evaluating them, group the terms with reciprocal first powers before taking limits.

**Step 4: exact infinite summation.** The elementary Euler identity \(\sum_{j\ge1}H_j/j^2=2\zeta(3)\) implies
\[
\sum_{n\ge0}\frac{H_{n+2}}{(n+1)^2}=2\zeta(3)+\zeta(2)-1,\qquad
\sum_{n\ge0}\frac{H_{n+2}}{(n+2)^2}=2\zeta(3)-1.
\]
The simple-pole coefficients of \(A_n\), in increasing order of their shifts, are \((-488/9,136/3,-8/3,104/9)\). Their generating polynomial factors as \((x-1)8(13x^2+10x+61)/9\). Use
\[
\sum_{n\ge0}H_{n+2}x^n=\frac{-\log(1-x)/(1-x)-x}{x^2},\qquad 0<x<1.
\]
In the resulting integral set \(g(x)=\log(1-x)+x-x^2\). Direct integrations give \(\int_0^1g(x)x^{-2}\,dx=-2\), \(\int_0^1g(x)x^{-1}\,dx=1/2-\zeta(2)\), and \(\int_0^1g(x)\,dx=-5/6\). Combining simple and double poles therefore yields
\[
\sum_{n\ge0}A_nH_{n+2}=\frac{448}{3}\zeta(3)+\frac{544}{9}\zeta(2)-\frac{5084}{27}.
\]
For \(D_n\), cancel the four simple poles together and use \(\sum_{n\ge0}((n+a)^{-2})=\zeta(2)-H_{a-1}^{(2)}\). The result is
\[
\sum_{n\ge0}D_n=\frac{2186}{81}-\frac{208}{3}\zeta(2).
\]
Adding these absolutely convergent grouped series gives
\[
\operatorname{Tr}(K^2)=\frac{448}{3}\zeta(3)-\frac{80}{9}\zeta(2)-\frac{13066}{81}
=\frac{448}{3}\zeta(3)-\frac{40\pi^2}{27}-\frac{13066}{81},
\]
as asserted. The Euler identity may, for example, be proved by integrating the generating series for \(H_n\) twice, so no unproved operator-theoretic lemma is hidden in the summation.

## Verification
A standalone Python-standard-library checker, `check_exact.py`, verifies 567 independent exact-rational identities covering the Gram sums, three finite harmonic reduction formulas, the partial fraction decomposition, and the expression for each grouped contribution at indices \(0\le n\le20\). The infinitely many terms and their sum are justified analytically above; the finite tests are consistency checks, not an infinite proof. The exact final expression evaluates to \(3.576886080095425209\ldots\).

## Relationship to prior work
Ma [1] proves hyponormality for the whole generalized Cesàro family and gives the defect decomposition underlying the factorization; the paper does not report this order-two quadratic spectral trace. Rhaly [2] established the order-two diagonal-interrupter identity and qualitative hyponormality, but not the quadratic moment in the inspected sections. Existing published mathematical-record results give the linear trace for generalized Cesàro self-commutators and a cubic spectral decay for the classical order-one case; neither fixes the order-two sum of squares of eigenvalues. The new invariant is not inferred from the known linear trace alone.

## Limitations
The result is an exact second moment for one canonical infinite-dimensional positive trace-class operator. It does not recover individual eigenvalues, higher moments, asymptotic singular-value constants, or a uniform statement for nonzero shifts or other orders. Broader literature might encode the value in an unexamined closed trace formula; independent priority assessment remains outstanding.

## References
[1] Yicen Ma, *Hyponormality of Generalized Cesàro Matrices of Every Positive Integer Order*, arXiv:2610.00193v1 (first submitted 18 September 2026), https://arxiv.org/html/2610.00193v1 .

[2] H. C. Rhaly Jr., *Supraposinormality and Hyponormality for the Generalized Cesàro Matrices of Order Two*, arXiv:1602.01408v1 (2016), https://arxiv.org/pdf/1602.01408 .

[3] published-finding corpus mathematical record, *A shift-invariant harmonic trace for generalized Cesàro self-commutators*, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-a-shift-invariant-harmonic-trace-for-generalized-ces-ro-self-com--b9745d36b9d7 .

