# An interval-supported but non-BV stationary density for a Cantor-driven random affine iteration

## Finding
Let \(C_0,C_1,\ldots\) be independent random variables with the standard symmetric middle-third Cantor distribution, and consider the random iteration
\[
X_{n+1}=\frac{X_n+2C_n}{3},\qquad X_0\in[0,1].
\]
It has exactly one stationary law \(\mu\), with support \([0,1]\). Although the driving law is singular, \(\mu\) has a density \(f\in L^2(\mathbb R)\), and indeed \(f\in H^s(\mathbb R)\) whenever
\[
0\le s<\log_3(16/9)-\frac12.
\]
Nevertheless, **no representative of \(f\) has bounded variation on \((0,1)\)**. In particular, there is no Lipschitz representative.

The exact arithmetic obstruction is the following Fourier resonance. Define
\[
A=\prod_{j=1}^{\infty}\cos\left(\frac\pi{3^j}\right),\quad
B=\prod_{j=1}^{\infty}\cos^j\left(\frac\pi{3^j}\right),\quad
t_N=\frac\pi2\,3^{N+1}.
\]
Both constants are strictly positive, \(3A>1\), and, for every integer \(N\ge1\),
\[
\left|\widehat\mu(t_N)\right|=B A^N,
\qquad
\left|t_N\widehat\mu(t_N)\right|=\frac{3\pi B}{2}(3A)^N\longrightarrow\infty.
\]
There is also a quantitative high-regularity obstruction: setting \(s_*= -\log A/\log3\), the density does not belong to \(H^s(\mathbb R)\) for any \(s\ge s_*\). Numerically \(A\simeq0.466274579\) and \(s_*\simeq0.694495\); these approximations are not used in the proof.

## Assumptions and scope
The Cantor variable has the explicitly normalized ternary expansion
\[
C_n=\sum_{k=1}^{\infty}\frac{2B_{n,k}}{3^k},
\]
where the \(B_{n,k}\) are independent fair \(\{0,1\}\)-valued variables over all pairs \((n,k)\). The Fourier convention is \(\widehat\mu(t)=\int e^{itx}\,d\mu(x)\). The assertion is for the **fixed matching contraction ratio** \(1/3\); it is not a classification of other ratios. Sobolev spaces are the standard \(L^2\)-based spaces on \(\mathbb R\), with the density extended by zero off \([0,1]\).

## Proof
**1. Stationarity, normalization and support.** The affine update is a contraction by \(1/3\) in the state variable. Iterating with independent innovations gives, in distribution, the unique stationary series
\[
X_*=\frac23\sum_{n=0}^{\infty}3^{-n}C_n.
\]
This series lies in \([0,1]\). Its support is the unique compact fixed point of \(K\mapsto (K/3)+(2/3)\mathcal C\), with \(\mathcal C\) the ternary Cantor set. The largest complementary gap of \((2/3)\mathcal C\) inside \([0,2/3]\) has length \(2/9\), smaller than \(1/3\). Consequently
\[
[0,1/3]+(2/3)\mathcal C=[0,1],
\]
so this entire interval is the stationary support.

**2. Exact characteristic product.** Write \(\varepsilon_{n,k}=2B_{n,k}-1\). Since \(\mathbb EC_n=1/2\), regrouping the absolutely summable centered series by \(m=n+k\) gives
\[
X_*-\frac12=\sum_{m=1}^{\infty}\frac{2}{3^{m+1}}
\sum_{i=1}^{m}\varepsilon_{m,i}',
\]
with all \(\varepsilon_{m,i}'\) independent fair signs. Therefore
\[
\left|\widehat\mu(t)\right|
=\prod_{m=1}^{\infty}\left|\cos\left(\frac{2t}{3^{m+1}}\right)\right|^m.
\tag{1}
\]
The products converge at each real \(t\) because the tail deficits are summable, even after multiplication by \(m\).

**3. An explicit \(L^2\) and positive-Sobolev bound.** For \(|t|\ge 3\pi/2\), select \(m\ge1\) with
\[
\frac\pi3\le u:=\frac{2|t|}{3^{m+1}}\le\pi.
\]
Dropping all other factors from (1), and using the \(m\)-th and \((m+1)\)-st factors,
\[
|\widehat\mu(t)|\le|\cos u\cos(u/3)|^m.
\]
If \(\pi/3\le u\le\pi/2\), this product has modulus at most \(1/2\). If \(\pi/2\le u\le\pi\), put \(z=\cos^2(u/3)\in[1/4,3/4]\). The triple-angle identity yields
\[
\cos u\cos(u/3)=4z^2-3z,
\]
whose absolute value on that interval is at most \(9/16\), with equality at \(z=3/8\). Thus, with \(\kappa=\log_3(16/9)\),
\[
|\widehat\mu(t)|\le C(1+|t|)^{-\kappa}.
\tag{2}
\]
The exact integer inequality \(16^2>3\cdot9^2\) implies \(\kappa>1/2\). Plancherel and the Fourier characterization of Sobolev spaces prove the stated \(L^2\) density and membership for every \(0\le s<\kappa-1/2\).

**4. The resonant subsequence.** At \(t_N=(\pi/2)3^{N+1}\), each factor in (1) with \(m\le N\) has modulus one. Writing \(m=N+j\) in the remaining factors yields
\[
|\widehat\mu(t_N)|
=\prod_{j=1}^{\infty}\cos^{N+j}(\pi/3^j)=A^NB.
\]
The products are positive because \(\sum_{j\ge1}j(1-\cos(\pi/3^j))<\infty\). The elementary product inequality \(\prod_j(1-a_j)\ge1-\sum_j a_j\), together with \(1-\cos x\le x^2/2\), gives
\[
A\ge\frac12\left(1-\frac{\pi^2}{144}\right)>
\frac12\left(1-\frac{16}{144}\right)=\frac49>\frac13.
\]
Hence \(|t_N\widehat\mu(t_N)|\to\infty\). If \(f\) had a bounded-variation representative on \((0,1)\), its zero extension would be BV on \(\mathbb R\). Its distributional derivative would then be a finite signed measure, forcing \(|t\widehat f(t)|\le\|Df\|_{\mathrm{TV}}\) for every \(t\), a contradiction.

**5. A non-Sobolev range, without asserting sharpness.** Fix \(|v|\le1/10\). For \(m\le N\), the factors of (1) at \(t_N+v\) become \(|\cos(2v/3^{m+1})|^m\), whose product is bounded below uniformly in \(N,v\) by a positive constant because \(\sum_{m\ge1}m(2v/3^{m+1})^2\le1/1600\). For the factors \(m=N+j\), compare their logarithms with those at \(t_N\). The mean-value theorem, boundedness of \(\tan\) on the relevant angles, and
\[
\sum_{j\ge1}(N+j)\frac{2|v|}{3^{N+j+1}}=O((N+1)3^{-N})
\]
show that this ratio is also bounded below by a positive constant independent of \(N,v\). Thus for one fixed \(c>0\),
\[
|\widehat\mu(t_N+v)|\ge c A^N\quad(|v|\le1/10,\ N\ge1).
\]
The corresponding frequency intervals are disjoint. Their contributions to the squared \(H^s\) norm dominate a positive multiple of
\[
\sum_{N\ge1}(3^{2s}A^2)^N.
\]
This diverges for \(s\ge-\log A/\log3\), proving the claimed upper obstruction.

## Verification
The accompanying `verify.py` computes the product parameters, tests finite grouped-product identities and the exact resonance formula, and checks the strict inequalities used in the proof. It uses only the Python standard library. It prints `VERIFY_OK` when all its checks pass. These finite tests corroborate the identities; the uniform analytic estimates, Plancherel application, and BV contradiction above establish the infinite claims.

## Relationship to prior work
Mantica's 2010 work introduced and analyzed precisely these homogeneous uncountable random affine systems. Its equation (22) already expresses the invariant characteristic function as a product, while Theorem 3 gives a general sufficient \(L^2\) criterion and Theorem 4 establishes absolute continuity for different contraction values. The present calculation is therefore **not** a claim to have discovered the invariant-product representation or the general \(L^2\) method. The model-specific statement proved here is the simultaneous \(L^2\)-but-not-BV regularity at the matching Cantor contraction, together with the explicit lattice-resonance constants and a Sobolev obstruction. Those conclusions are not supplied by that sufficient criterion.

Mantica (2011) develops Jacobi-matrix methods for the same infinite affine systems, including singular Cantor driving measures in Section 4.4, Example 2. Its analysis of stationary-measure continuity in Section 5 does not assert a Fourier-resonance BV classification at matching ternary scale. Mantica and Peirone (2015), Theorem 1.1, concerns the topological attractor (a finite union of intervals) of second-generation uncountable affine systems; it does not classify BV regularity of stationary densities. In this specialization the topological interval assertion has the elementary proof given above.

## Limitations
No exact optimal Sobolev exponent is claimed: the positive interval of membership and the excluded range leave a gap. Failure of BV does not exclude continuity, so continuity itself is not decided here. The argument applies to the specified fair Cantor law and the exact contraction ratio \(1/3\), not arbitrary asymmetric weights or independent ratios. The novelty comparison is based on inspected accessible literature and mathematical-result searches; absolute historical priority requires independent review.

## References
1. G. Mantica, *Dynamical Systems and Numerical Analysis: the Study of Measures generated by Uncountable I.F.S.*, arXiv:1005.3395v1 (first public 2010-05-19), especially Sections 2, 6–8 and Theorems 3–4. https://arxiv.org/abs/1005.3395
2. G. Mantica, *Direct and Inverse Computation of Jacobi Matrices of Infinite Homogeneous Affine I.F.S.*, arXiv:1106.4945v1 (first public 2011-06-24), especially Example 2 and Section 5. https://arxiv.org/abs/1106.4945
3. G. Mantica and R. Peirone, *Attractors of Iterated Function Systems with uncountably many maps*, arXiv:1506.08033v1 (first public 2015-06-26), especially Theorem 1.1 and Section 8. https://arxiv.org/abs/1506.08033
