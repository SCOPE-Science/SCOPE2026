# The logarithmic second moment of the two-variable gcd map

## Finding
For positive integers \(a,b\), define
\[
f(a,b)=\frac{\gcd(ab,a+b)}{\gcd(a,b)}.
\]
As real \(x\to\infty\), the exact endpoint second moment obeys
\[
\boxed{\sum_{1\le a,b\le x}f(a,b)^2
=\frac{x^2\log x}{2\zeta(2)}+O\!\left(x^2\log\log x\right)
=\frac{3}{\pi^2}x^2\log x+O\!\left(x^2\log\log x\right).}
\]
The sums are over **ordered** pairs. This settles the first boundary exponent \(t=2\) identified as an open asymptotic problem in Fan--Tóth [1, Section 4, item 4].

## Assumptions and scope
All variables \(a,b,d,k,i,j\) are positive integers. The variable \(x\) is real and sufficiently large, and \(a,b\le x\) means \(a,b\le\lfloor x\rfloor\). The symbols \(\mu,\varphi,\zeta\) denote the Möbius function, Euler totient and Riemann zeta function. Define the second Jordan totient
\[
J_2(d)=d^2\prod_{p\mid d}(1-p^{-2})=\sum_{e\mid d}\mu(e)(d/e)^2.
\]
All implied constants are absolute. The claim concerns the squared moment only; no estimate for higher exponents is asserted.

## Proof
**Step 1: Exact decomposition.** Put \(\delta=\gcd(a,b)\), \(a=\delta i\) and \(b=\delta j\) with \(\gcd(i,j)=1\). Since \(\gcd(ij,i+j)=1\),
\[
f(a,b)=\gcd(\delta,i+j).
\]
By \(m^2=\sum_{d\mid m}J_2(d)\), the exact identity is
\[
S(x):=\sum_{a,b\le x}f(a,b)^2
=\sum_{d^2k\le2x} J_2(d)\,V_d\!\left(\frac{x}{dk}\right),\qquad
V_d(y):=\#\{1\le i,j\le y:\ \gcd(i,j)=1,\ d\mid i+j\}.
\tag{1}
\]
Indeed write \(\delta=dk\), and observe that if \(d\mid i+j\) then \(d\le i+j\le2x/(dk)\), hence \(d^2k\le2x\). This is an exact finite rearrangement, without discarded terms.

**Step 2: Uniform congruence count.** For every integer \(d\ge1\) and real \(y\ge1\),
\[
V_d(y)=\frac{y^2}{d\zeta(2)}\prod_{p\mid d}\frac{p}{p+1}
+O\bigl(y\log(2y)\bigr).\tag{2}
\]
For any \(m\ge1\) and real \(z\ge1\), the number \(Q_m(z)\) of ordered pairs up to \(z\) with \(m\mid u+v\) is \(z^2/m+O(z)\), with absolute constant: for each \(u\), counting \(v\) in one residue class costs at most one rounding error. Möbius inversion gives
\[
V_d(y)=\sum_{e\le y}\mu(e)\,Q_{d/\gcd(d,e)}(y/e).
\]
After replacing \(Q_m\) with its main term, the aggregate error is \(O(y\sum_{e\le y}1/e)=O(y\log(2y))\). Extending the resulting Dirichlet series beyond \(e>y\) adds at most
\(\frac{y^2}{d}\sum_{e>y}\gcd(d,e)e^{-2}\le y^2\sum_{e>y}e^{-2}=O(y)\).
Finally
\[
\sum_{e\ge1}\frac{\mu(e)\gcd(d,e)}{e^2}
=\frac1{\zeta(2)}\prod_{p\mid d}\frac{p}{p+1},
\]
which proves (2), uniformly in \(d\). A separate bound applies when \(d\le2y\): since at most \(2y/d\) multiples of \(d\) can occur as \(i+j\), and at most \(y\) pairs realize a fixed sum,
\[
0\le V_d(y)\le\frac{2y^2}{d}.\tag{3}
\]
For \(d>2y\) the count is zero.

**Step 3: Central rectangle.** Write \(L=\log x\), \(T=\lfloor\sqrt x/L^3\rfloor\), and \(K=\lfloor L^3\rfloor\). For large \(x\), all \(d\le T,k\le K\) satisfy \(d^2k\le x/L^3<2x\), so apply (2) inside this rectangle. The total error from (2), using \(J_2(d)\le d^2\), is
\[
\ll xL\sum_{d\le T}d\sum_{k\le K}k^{-1}
\ll xLT^2\log(2K)\ll\frac{x^2\log L}{L^5}.\tag{4}
\]
The main term is
\[
\frac{x^2}{\zeta(2)}\left(\sum_{k\le K}\frac1{k^2}\right)
\sum_{d\le T}\frac{J_2(d)}{d^3}\prod_{p\mid d}\frac{p}{p+1}.
\]
The exact Euler-factor identity
\[
J_2(d)\prod_{p\mid d}\frac{p}{p+1}=d\varphi(d)
\]
turns this into
\[
\frac{x^2}{\zeta(2)}\left(\zeta(2)+O(K^{-1})\right)
\sum_{d\le T}\frac{\varphi(d)}{d^2}.
\]
Since \(\varphi(n)/n=\sum_{e\mid n}\mu(e)/e\), elementary harmonic summation proves
\[
\sum_{d\le T}\frac{\varphi(d)}{d^2}
=\sum_{e\le T}\frac{\mu(e)}{e^2}\sum_{m\le T/e}\frac1m
=\frac{\log T}{\zeta(2)}+O(1).\tag{5}
\]
Indeed \(\sum_e|\mu(e)|\log(2e)/e^2<\infty\), which controls the constants and truncation. Because \(\log T=\tfrac12L-3\log L+O(1)\), the central rectangle contributes
\[
\frac{x^2L}{2\zeta(2)}+O(x^2\log L).\tag{6}
\]

**Step 4: Tails.** For each term present in (1), the condition \(d^2k\le2x\) ensures \(d\le2x/(dk)\), so (3) and \(J_2(d)\le d^2\) give the uniform majorant
\[
J_2(d)\,V_d(x/(dk))\le\frac{2x^2}{d k^2}.\tag{7}
\]
All omitted terms either have \(d>T\) or have \(d\le T,k>K\). Their combined contribution is at most
\[
2x^2\sum_{T<d\le\sqrt{2x}}\frac1d\sum_{k\ge1}\frac1{k^2}
+2x^2\sum_{d\le T}\frac1d\sum_{k>K}\frac1{k^2}
\ll x^2\log L+x^2\frac{L}{K}
\ll x^2\log L.\tag{8}
\]
Combining (6) and (8) completes the claimed asymptotic, because \(\log L=\log\log x\). Every approximation above is uniform in the summation variables, and no finite computation is used to establish the infinite asymptotic.

## Verification
The standalone `verify.py` reconstructs \(J_2\) via Möbius convolution, checks the Jordan identity and the Euler-factor cancellation for all integers through 300, and agrees on two exact finite computations of the squared moment: direct ordered-pair enumeration versus (1) with exact coprimality/congruence counts. It verifies complete equality at five bounds and performs a larger direct check at three further bounds. The captured command output is in `verify_output.txt`. These are finite identity checks, not validation of the limiting estimate; the proof of (2)--(8) is analytical.

## Relationship to prior work
Fan and Tóth [1] obtain average values for exponents below two (Corollary 3) and **explicitly leave \(t\ge2\) as a further research problem** in Section 4, item 4. The exact exponent-two asymptotic and leading constant established here are not consequences of those subcritical estimates: their constants diverge as \(t\uparrow2\), and the endpoint requires a separate divisor cutoff. Thang Pang Ern and Malcolm Tan Jun Xi [2] study the same map's values, symmetries and density-one fiber, not its squared moment. Related exact-density results for more variables concern the level set \(f=1\), not endpoint power averages.

## Limitations
Only the first endpoint moment \(t=2\) is determined. The error term is not claimed optimal, and no asymptotic is asserted for \(t>2\). Reproducibility code tests only finite inputs. Although the most directly relevant original papers and published comparisons were examined, undiscovered equivalent work remains a novelty risk. Independent review of the argument has not been performed.

## References
[1] Steve Fan and László Tóth, *On the asymptotic density of the ordered pairs \((a,b)\) of positive integers such that \(\gcd(ab,a+b)=\gcd(a,b)\)*, arXiv:2606.20057 (first posted 2026-06-18; Section 4, item 4), https://arxiv.org/abs/2606.20057. Full-text version inspected: https://pdfs.assets.alphaxiv.org/2606.20057v3.pdf.

[2] Thang Pang Ern and Malcolm Tan Jun Xi, *On the Asymptotic Density of a GCD-based Map*, arXiv:2506.19812 (2025-06-24), https://arxiv.org/abs/2506.19812. Full text: https://pdfs.assets.alphaxiv.org/2506.19812v1.pdf.
