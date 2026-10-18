# Parity-split polynomial transfer spectrum and nonlinear correlation in an even-symmetric four-branch map

## Finding
For every \(0<d<1/2\), put \(a=1/2-d\) and let \(T_d:[0,1]\to[0,1]\) be the four-branch map in the next section. The Lebesgue Perron–Frobenius operator \(P_d\) preserves every polynomial space \(\mathcal V_m=\mathbb R[x]_{\le m}\), \(m\ge0\), and its restriction is diagonalizable with the following **complete eigenvalue multiset**:
\[
\{1\}\ \cup\ \{0\}^{\lceil m/2\rceil}\ \cup\ \bigl\{2[d^{2j+1}+a^{2j+1}]:1\le j\le\lfloor m/2\rfloor\bigr\}.
\]
In particular, centered odd polynomials are precisely the polynomial kernel of \(P_d\); all even-degree nonconstant eigenvalues are strictly positive and pairwise distinct.

Set \(u(x)=x-1/2\), \(g(x)=u(x)^2-1/12\), and \(\lambda(d)=2(d^3+a^3)=3(d-1/4)^2+1/16\). For Lebesgue-stationary initial state and every integer \(n\ge1\),
\[
\int_0^1u(x)u(T_d^n x)\,dx=0,
\qquad
\int_0^1g(x)g(T_d^n x)\,dx=\frac{\lambda(d)^n}{180}.
\]
The second identity also holds for \(n=0\). Consequently the nonlinear normalized autocorrelation is exactly \(\lambda(d)^n\), despite identically zero positive-lag coordinate autocorrelation. The rate \(\lambda(d)\) has a unique minimum \(1/16\) at \(d=1/4\) within the allowed parameter interval.

The same dichotomy lifts to the nonlinear even-symmetric map \(F_d=q^{-1}\circ T_d\circ q\), where \(q(x)=\tfrac12+\tfrac12(2x-1)^3\). Its stationary measure \(\mu\) has density \(3(2x-1)^2\). With \(v(x)=(2x-1)^3\) and \(h(x)=(2x-1)^6-1/3\), for all \(n\ge1\) one has
\[
\int v(x)v(F_d^n x)\,d\mu(x)=0,
\qquad
\int h(x)h(F_d^n x)\,d\mu(x)=\frac4{45}\lambda(d)^n.
\]
Again the second identity includes \(n=0\). These are *real-valued map-level correlations*, not assertions about independent output bits, finite-precision implementations, or an entire encryption system.

## Assumptions and scope
Fix \(d\in(0,1/2)\), \(a=1/2-d\), and define, up to choices at finitely many breakpoints,
\[
T_d(x)=\begin{cases}
 x/d,&0\le x<d,\\
 (x-d)/a,&d\le x<1/2,\\
 (1-d-x)/a,&1/2\le x<1-d,\\
 (1-x)/d,&1-d\le x\le1.
\end{cases}
\]
At endpoints common to adjacent branches the one-sided values may differ; statements about invariant measures and transfer operators are made modulo finite sets. Every branch covers the unit interval and has inverse-slope magnitude \(d\) or \(a\). Lebesgue measure is invariant because the four inverse-slope magnitudes sum to \(2d+2a=1\). The transfer operator is defined by the usual duality \(\int (P_df)\psi\,dx=\int f(\psi\circ T_d)\,dx\), for integrable \(f\) and bounded \(\psi\). The polynomial spectral statement is only for finite-dimensional \(\mathcal V_m\); it makes no claim about the whole spectrum on \(L^2\), bounded variation, or other Banach spaces.

The monotone homeomorphism \(q:[0,1]\to[0,1]\) obeys \(q(0)=0\), \(q(1)=1\), and \(q'(x)=3(2x-1)^2\). The probability \(\mu(dx)=q'(x)dx\) is \(F_d\)-invariant because \(q_*\mu\) is Lebesgue measure. No differentiability of \(q^{-1}\) at \(1/2\) is required.

## Proof
For any polynomial \(f\), the four inverse branches pair by reflection, giving exactly
\[
(P_df)(y)=d\,[f(dy)+f(1-dy)]
+a\,[f(d+ay)+f(1-d-ay)]. \tag{1}
\]
Reflection around \(1/2\) makes each centered odd monomial \(u^{2j+1}\) vanish under \(P_d\). For every integer \(j\ge1\),
\[
P_d(u^{2j})(y)=2d(1/2-dy)^{2j}+2a(1/2-d-ay)^{2j}.
\]
This is a polynomial of degree \(2j\) with leading coefficient \(\lambda_{2j}=2(d^{2j+1}+a^{2j+1})>0\). Also \(P_d1=1\). Thus the matrix in increasing-degree centered monomials is upper triangular (with degrees decreasing in the images) and has exactly the diagonal spectrum stated. Since \(0<d,a<1/2\), \(1>\lambda_2>\lambda_4>\cdots>0\). The only polynomials annihilated by \(P_d\) are odd about \(1/2\): if the even part of a polynomial were nonzero, the top even-degree coefficient could not disappear under \(P_d\). Therefore the zero eigenspace has dimension \(\lceil m/2\rceil\), equal to its algebraic multiplicity. The nonzero eigenvalues are simple, so the full polynomial restriction is diagonalizable.

For the quadratic observable, direct expansion of (1) gives
\[
P_du=0,\qquad
P_dg=\lambda(d)g+\beta(d)u,
\quad \beta(d)=2(-d^2+d^3-a^3).
\]
Hence for every \(n\ge1\), \(P_d^n g=\lambda(d)^n g+\lambda(d)^{n-1}\beta(d)u\). The centered moments are \(\int_0^1u\,dx=\int_0^1g\,dx=\int_0^1ug\,dx=0\) and \(\int_0^1g^2\,dx=1/180\). Transfer duality proves both correlation identities. Completing the square in \(\lambda(d)=3d^2-3d/2+1/4\) proves the sharp minimizer; for instance \(\lambda(27/100)=637/10000\) and \(\lambda(13/100)=1057/10000\).

Finally, \(v=2u\circ q\), \(h=4g\circ q\), and \(q\circ F_d=T_d\circ q\). Changing variables under \(q_*\mu=dx\) multiplies the first correlation by four and the second by sixteen. The first is zero, and the second is \(16\lambda(d)^n/180=4\lambda(d)^n/45\). Its zero-lag value is \(4/45\), as claimed.

## Verification
The accompanying standalone `verify.py` computes (1) symbolically, checks the quadratic transfer identity and variance exactly, and verifies odd-degree annihilation and even-degree leading coefficients through degree fourteen. It checks all lags zero through thirteen at seven rational parameters, and independently confirms the invariant density, transformed observables, the sharp quadratic rate, and two illustrative source parameters. Execute with Python 3 and SymPy: `python verify.py`. Exact finite checks support the analytical calculation; the all-degree and all-parameter assertions follow from the displayed proof, not from finite sampling.

## Relationship to prior work
El-den, Raslan and Abdullah's 2022 preprint / 2023 article explicitly uses this four-branch even-symmetric map and its skewed conjugate in video encryption; its Section 3.1 gives the branches, transformation and stationary density. It does not state the polynomial transfer-spectrum theorem or the exact analog autocorrelation law above. Sang, Wang and Yan's 2001 work establishes Bernoulli properties of quantized even-symmetric maps, which are distinct from the *real-valued nonlinear* correlations calculated here. Their earlier 2000 paper develops a general framework for covariance of chaotic sequences; its abstract, available without the full text in this examination, makes it a material potential antecedent. General finite-dimensional transfer-operator techniques explain the proof strategy; no novelty is claimed for the operator formalism itself. The specific parameterized all-polynomial spectral census and conjugated cubic/sextic observable correlation laws are the contribution under examination.

## Limitations
The theorem treats exact real-arithmetic dynamics, stationary input, and polynomial observables. It does not certify pseudorandom bitstream behavior, practical cryptographic resistance, finite-precision cycle lengths, or the full function-space spectrum. The source's nonlinear map is used solely through the mathematically defined monotone conjugacy, without relying on typography in its displayed primitive. A plausible historical general covariance source (Sang–Wang–Yan 2000) was not fully accessible; a prior equivalent derivation remains a priority risk. Independent expert validation is not claimed.

## References
1. B. M. El-den, W. A. Raslan, and A. A. Abdullah, *Even symmetric chaotic and skewed maps as a technique in video encryption*, publicly posted 2022-10-31, DOI: `10.21203/rs.3.rs-2123196/v1`; open-access journal version, *EURASIP Journal on Advances in Signal Processing* 2023, article 40, DOI: `10.1186/s13634-023-01003-4` (especially Section 3.1).
2. T. Sang, R. Wang, and Y. Yan, *Generating binary Bernoulli sequences based on a class of even-symmetric chaotic maps*, *IEEE Transactions on Communications* **49** (2001), 620–623, DOI: `10.1109/26.917768`. Abstract accessible; full text not examined.
3. T. Sang, R. Wang, and Y. Yan, *Constructing chaotic discrete sequences for digital communications based on correlation analysis*, *IEEE Transactions on Signal Processing* **48** (2000), 2557–2565, DOI: `10.1109/78.863058`. Abstract accessible; full text not examined.
