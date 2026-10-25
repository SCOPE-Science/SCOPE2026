# Sharp four-term progression correlations and dyadic rigidity in the Rudin–Shapiro subshift

## Finding
Let \(r_n=(-1)^{\sum_{j\geq0}\varepsilon_j(n)\varepsilon_{j+1}(n)}\), where \(\varepsilon_j(n)\in\{0,1\}\) are the binary digits of a nonnegative integer. For each positive integer \(h\), let
\[
C(h)=\lim_{N\to\infty}\frac1N\sum_{n=0}^{N-1}r_nr_{n+h}r_{n+2h}r_{n+3h}.
\]
Then this limit exists, and the unrestricted sharp inequality and complete equality classification are
\[
|C(h)|\leq\frac12,\qquad |C(h)|=\frac12\ \Longleftrightarrow\ h=2^k\ (k\in\mathbb Z_{\geq0}),
\]
with \(C(2^k)=-\frac12\) at every equality case. This detects rigid higher-order dependence in a sequence with vanishing nontrivial two-point autocorrelations.

## Assumptions and scope
The sequence is the standard one-sided Rudin–Shapiro sign sequence, normalized by \(r_0=1\). The correlation averages are Cesàro averages over nonnegative integers; equivalently, they are cylinder correlations under the unique invariant probability measure of the two-sided Rudin–Shapiro subshift. The four sites are **equally spaced** \(0,h,2h,3h\). No analogous bound is asserted for general four-site shapes. All integers \(h\geq1\) are included; no finite spacing cutoff is used.

## Proof
**Dyadic invariance.** The exact binary recursions are \(r_{2m}=r_m\) and \(r_{2m+1}=(-1)^m r_m\). Splitting a four-site progression over even and odd starting positions gives \(C(2h)=C(h)\): the product of the four odd-position signs is \((-1)^{4m+6h}=1\). It is therefore enough to prove the assertion for odd \(h\).

**Exact carry transducer.** Read the bits of \(h\) from least significant to most significant. A state consists of three carries \((c_1,c_2,c_3)\) for the additions \(n+jh\), together with the previously emitted four binary digits \((u_0,u_1,u_2,u_3)\), initially zero. Given a spacing bit \(b\in\{0,1\}\) and a free bit \(a\in\{0,1\}\) of \(n\), emit \(v_0=a\) and, for \(j=1,2,3\),
\[
v_j\equiv a+jb+c_j\pmod2,\qquad c'_j=\left\lfloor\frac{a+jb+c_j}{2}\right\rfloor.
\]
The transition weight is \((-1)^{\sum_{j=0}^{3}u_jv_j}\), and the next previous-digit tuple is \((v_0,v_1,v_2,v_3)\). All 30 reachable states are exhaustively enumerated in `verify.py`, along with their closure under both spacing bits and both free input bits. Let \(T_b\) be the unnormalized signed transfer on integer state vectors obtained by summing over the two choices of \(a\). Since every starting coordinate contributes two signed unit masses, the \(\ell^1\) norm satisfies \(\|T_bd\|_1\leq2\|d\|_1\).

After the final nonzero spacing bit, all remaining bits of \(h\) are zero. Let \(f_0\equiv1\) on the 30 states, and let \(f_3\) be the threefold dual zero-bit transfer of \(f_0\). Exact enumeration certifies the **identity on every reachable state** \(T_0^*f_3=2f_3\), so the eventual tail expectation is exactly \(f_3/8\); there is no truncation approximation. For the signed state vector \(d(h)\) after the \(L\) binary digits of \(h\),
\[
C(h)=2^{-L-3}\langle d(h),f_3\rangle.
\]
This also proves existence of the correlation limit. The identity can be verified by literal rational cylinder expectations, and all transfers are integer-exact.

**Five-bit exhaustion.** Consider every five-bit low prefix \(p\) of an odd spacing, including zero padding when its actual length is shorter. Of the 16 possible prefixes, precisely \(p=1\) and \(p=31\) have \(\|d(p)\|_1/32>1/2\), with value \(5/8\). Precisely \(p=15\) and \(p=17\) have value \(1/2\); after either next bit their normalized norm is \(3/8\). The remaining 12 have value strictly below \(1/2\), permanently by norm nonexpansion. These are exhaustive finite-state checks, not a sample of spacings.

**Exceptional-prefix induction.** For each \(b\in\{0,1\}\), let \(D_k^{(b)}\) be the signed vector after the spacing-digit string \((1,b,b,\ldots,b)\) of length \(k\geq5\). The exact two-phase affine description is
\[
D_k^{(b)}=-(2^{k-2}-1)B_b+v_{b,k\bmod2},
\]
where \(B_b\) consists of two positive unit coordinate masses and each phase vector is an integer combination of six unit coordinate masses. Their finite, explicit defining vectors are computed directly from \(D_5^{(b)},D_6^{(b)},D_7^{(b)},D_8^{(b)}\) in `verify.py`; the identities \(T_bB_b=2B_b\) and \(T_bv_{b,\mathrm{odd/even}}=v_{b,\mathrm{even/odd}}-B_b\) certify the formula for **all** \(k\geq5\). For \(t=2^{k-2}-1\geq7\), integer coefficient and stable-sign verification on the entire half-line \(t\geq7\) yields
\[
\|D_k^{(b)}\|_1=2t+6,\quad
\|T_{1-b}D_k^{(b)}\|_1=4t+4,\quad
\|T_aT_{1-b}D_k^{(b)}\|_1=8t\quad(a=0,1).
\]
After the first nonrepeating spacing bit and any subsequent bit, the normalized norm is exactly \(\tfrac12-2^{1-k}<\tfrac12\). Any finite odd \(h>1\) either has a nonexceptional low-five-bit prefix or eventually departs from one of the two exceptional paths; if the spacing ends on the all-ones path, mandatory infinite zero-padding supplies that departure and a subsequent bit. Therefore its four-site correlation is strictly smaller in magnitude than \(1/2\). Odd spacings of fewer than five bits are handled directly by the exact terminal functional; their values are strictly below \(1/2\) except for \(h=1\).

Finally direct exact evaluation of the terminal functional gives \(C(1)=-1/2\). Dyadic invariance transfers this equality to every \(h=2^k\), completing both directions of the classification. The induction for exceptional prefixes is checked using symbolic affine coefficients rather than a cutoff in \(k\).

## Verification
Run `python3 verify.py` with Python 3 (standard library only). The checker reconstructs all 30 reachable carry states, verifies closure and the exact terminal fixed-point identity, enumerates all 16 low-five-bit odd prefixes, and proves both exceptional affine induction branches and their strict-exit inequalities on the entire half-line \(t\geq7\). It independently compares 14 exact finite binary-prefix averages with the derived rational correlation formula as a supplementary test. The infinite theorem rests on finite closure, exact state identities and unbounded induction, **not** finite numerical experiments.

## Relationship to prior work
Ravy (arXiv:1303.3792) discusses hidden higher-order Rudin–Shapiro correlations in coherent diffraction and gives other four-site geometries. Mazáč (arXiv:2211.01090), especially Sections 4 and 6, rigorously derives Rudin–Shapiro higher-order correlations and striking families of four-point shapes. Some non-arithmetic-progression four-site correlations can approach magnitude one, so the present sharp bound is **special to equal spacing**, not a contradiction. Konieczny's work on Gowers uniformity addresses averaged additive configurations, not this pointwise extremal classification. The contribution here is the exact supremum and complete equality family for the one-parameter arithmetic-progression shape, certified by the finite carry transducer and affine exceptional-path induction.

## Limitations
The theorem covers only the classical balanced Rudin–Shapiro signs and four equally spaced sites. It gives no exact closed formula for each arbitrary \(C(h)\) beyond the explicit transfer algorithm, no analogous result for five or more sites, and no bound for arbitrary four-site configurations. The priority comparison is based on inspected accessible literature and semantic search, not an assertion of universal uniqueness; a historically implicit equivalent may exist. No independent scientific audit has been performed.

## References
- S. Ravy, “Homometry in the light of coherent beams,” arXiv:1303.3792 (first public version 2013-03-15).
- J. Mazáč, “Correlation functions of the Rudin–Shapiro sequence,” arXiv:2211.01090 (first public version 2022-11-02), Sections 4 and 6.
- J. Konieczny, “Gowers norms for the Thue–Morse and Rudin–Shapiro sequences,” Annales de l'Institut Fourier, DOI:10.5802/aif.3285.
