# Sharp growing-bandwidth fourth moments of central \(SU(2)\) Fourier polynomials

## Finding
For \(N\ge1\), let
\[
K_N=\sup_{\sum_{j=0}^{N-1}|a_j|^2=1}
\int_{SU(2)}\left|\sum_{j=0}^{N-1}a_j\chi_j(g)\right|^4\,dg,
\]
where \(\chi_j\) is the **unnormalized** irreducible character of highest weight \(j\), and \(dg\) is Haar probability measure. Define for \(f\in L^2(0,1;\mathbb C)\)
\[
B_t(f)=\int_0^1\int_0^1 f(x)f(y)
\mathbf1_{\{|x-y|\le t\le x+y\}}\,dx\,dy,
\qquad \mathcal F(f)=\int_0^2|B_t(f)|^2\,dt.
\]
Then the following **sharp full limit** holds:
\[
\boxed{\displaystyle
\lim_{N\to\infty}\frac{K_N}{N^3}
=\frac14\max_{\|f\|_{L^2(0,1)}=1}\mathcal F(f).}
\]
The continuum maximum exists and admits a nonnegative real maximizer; in particular the limit is at least \(34/315\). Moreover, for *any* sequence of arrays with squared coefficient norm one and fourth moments \(K_N-o(N^3)\), the step functions equal to \(\sqrt N|a_j|\) on \([j/N,(j+1)/N)\) are relatively compact in \(L^2(0,1)\), and every cluster point is a nonnegative maximizer of \(\mathcal F\).

## Assumptions and scope
The group is the compact group \(SU(2)\); the Fourier packet is the full initial segment \(\chi_0,\ldots,\chi_{N-1}\), with \(N\) tending through positive integers. Coefficients are unrestricted complex numbers, but an optimizer may be chosen nonnegative using the positivity of Clebsch–Gordan multiplicities. The character normalization is fixed by \(\chi_j(e)=j+1\) and
\[
\chi_j(\theta)=\frac{\sin((j+1)\theta)}{\sin\theta},\quad
\int_{SU(2)}h(g)\,dg=\frac2\pi\int_0^\pi h(\theta)\sin^2\theta\,d\theta
\]
for central functions. Consequently \(\int\chi_j\overline{\chi_k}\,dg=\mathbf1_{j=k}\). The theorem makes no assertion about uniqueness or smoothness of continuum extremizers.

## Proof
**1. An exact positive tensor.** The \(SU(2)\) Clebsch–Gordan rule is
\[
\chi_i\chi_j=\sum_{r=|i-j|,\,|i-j|+2,\ldots,\,i+j}\chi_r.
\]
Writing \(F_N(a)=\int|\sum_{j<N}a_j\chi_j|^4dg\), orthogonality gives
\[
F_N(a)=\sum_{i,j,k,l<N}a_i a_j\overline{a_k a_l}T_{ijkl},
\]
where \(T_{ijkl}\) counts the common integers in the two Clebsch–Gordan intervals of the indicated parity. Put
\[
\Delta(x,y,z,w)
=\big[\min(x+y,z+w)-\max(|x-y|,|z-w|)\big]_+.
\]
If \(i+j\) and \(k+l\) have opposite parity, then \(T_{ijkl}=0\). Otherwise, all endpoints have the same integer parity and counting by twos shows
\[
\bigg|T_{ijkl}-\frac N2\Delta(i/N,j/N,k/N,l/N)\bigg|\le1.
\]
In particular, uniformly for \(\sum|a_j|^2=1\), replacing the tensor incurs an error at most \(N^2\), since \(\sum|a_j|\le\sqrt N\).

**2. Uniform two-channel approximation.** Define \(A_N(x)=\sqrt N a_j\) and \(E_N(x)=(-1)^j\sqrt N a_j\) on the \(j\)-th cell. Then both have squared \(L^2\)-norm one. The parity indicator is
\[
\mathbf1_{i+j\equiv k+l\; (2)}
=\tfrac12\bigl(1+(-1)^{i+j+k+l}\bigr).
\]
The function \(\Delta\) is globally Lipschitz in its four arguments, so its replacement by its cellwise average costs at most a universal constant divided by \(N\). Fubini's theorem yields
\[
\boxed{\displaystyle
\left|\frac{F_N(a)}{N^3}-
\frac{\mathcal F(A_N)+\mathcal F(E_N)}4\right|\le\frac C N,}
\]
with a numerical constant \(C\) independent of \(N\) and of every normalized complex coefficient array. Here the identity
\[
\mathcal F(f)=\int_{[0,1]^4}
 f(x)f(y)\overline{f(z)f(w)}\Delta(x,y,z,w)
\,dx\,dy\,dz\,dw
\]
follows by integrating in \(t\) the common triangular support. The factor \(1/4\) is essential: one half counts parity-compatible quadruples, and another half counts allowed representation weights within an interval.

**3. Weak continuity of the continuum functional.** For fixed \(t\in[0,2]\), let \(H_t\) be the Hilbert–Schmidt integral operator with kernel \(\mathbf1_{\{|x-y|\le t\le x+y\}}\). If \(f_n\rightharpoonup f\) in \(L^2(0,1)\), compactness of \(H_t\) proves \(B_t(f_n)\to B_t(f)\): pair the strongly convergent \(H_tf_n\) with the weakly convergent second factor (with conjugations fixed appropriately for the bilinear form). Also
\[
\|H_t-H_s\|_{\mathrm{HS}}^2\le C|t-s|,
\]
because the symmetric difference of the defining planar regions is contained in strips of total area \(O(|t-s|)\). For a bounded \(L^2\) sequence, these bounds make \(B_t(f_n)\) equicontinuous in \(t\). A finite-net argument gives uniform convergence in \(t\), hence \(\mathcal F(f_n)\to\mathcal F(f)\). The functional is homogeneous of degree four, nonnegative and weakly sequentially continuous. It therefore attains a positive maximum on the \(L^2\)-unit sphere: maximize on the weakly compact closed ball, observe \(\mathcal F(1)>0\), and use homogeneity to force norm one. Positivity of its kernel implies \(\mathcal F(f)\le\mathcal F(|f|)\).

**4. Upper bound and the parity-channel obstruction.** Extract weakly convergent subsequences \(A_N\rightharpoonup f\) and \(E_N\rightharpoonup h\) along any sequence of normalized arrays. Alternating cell signs converge weak-* to zero against \(L^1\) test functions. For arbitrary \(p,q\in L^2(0,1)\),
\[
\|p+(-1)^{\lfloor Nx\rfloor}q\|_2^2\to
\|p\|_2^2+\|q\|_2^2.
\]
Duality and Cauchy–Schwarz, tested against the weak limits, therefore give
\[
\|f\|_2^2+\|h\|_2^2\le1.
\]
The preceding uniform approximation and weak continuity imply
\[
\limsup\frac{F_N(a)}{N^3}
=\frac{\mathcal F(f)+\mathcal F(h)}4
\le\frac M4(\|f\|_2^4+\|h\|_2^4)
\le\frac M4,
\]
along every subsequence realizing a limsup; here \(M=\max_{\|u\|_2=1}\mathcal F(u)\). (The displayed equality is understood on the extracted subsequence.)

**5. Recovery sequence.** Choose any normalized \(g\in L^2(0,1)\) with \(g\ge0\). Let \(A_N\) be the normalized averages of \(g\) on the \(N\) equal cells. Then \(A_N\to g\) strongly, while its alternating version tends weakly to zero. The two-channel approximation gives
\[
\lim_{N\to\infty}\frac{F_N(a)}{N^3}
=\frac{\mathcal F(g)}4.
\]
Taking \(g\) to maximize \(\mathcal F\) proves the full sharp limit.

**6. Compactness of near-extremal moduli.** Replacing each coefficient by its absolute value cannot decrease \(F_N\). A near-extremizing normalized complex array thus yields a near-extremizing nonnegative array. Let \(A_N\rightharpoonup f\ge0\) and \(E_N\rightharpoonup h\). Equality in the upper bound forces one weak limit to have norm one and the other zero. The alternative \(f=0\), \(\|h\|_2=1\) is impossible: for any \(q\in L^2\),
\[
|\langle E_N,q\rangle|\le\langle A_N,|q|\rangle\to0
\]
when \(A_N\ge0\) tends weakly to zero. Therefore \(\|f\|_2=1\), \(h=0\), and \(\mathcal F(f)=M\). Weak convergence plus convergence of norms implies \(A_N\to f\) strongly. This works along every extracted subsequence and proves the asserted relative compactness.

**7. A concrete lower bound.** For the normalized test function \(g(x)=\sqrt3 x\), direct integration gives \(\mathcal F(g)=136/315\) (the unnormalized triangular integral is \(2t/3-t^2/2+t^4/24\) on \(0\le t\le1\), and \((2-t)^2/2-(2-t)^3/3+(2-t)^4/24\) on \(1\le t\le2\)). Hence the sharp limiting constant is at least \(34/315\). In comparison, \(g=1\) gives exactly \(1/12\) after the factor \(1/4\).

## Verification
The standalone `checks.py` computes the fourth moment two ways (Clebsch–Gordan fusion and direct Weyl-angular quadrature) for four complex test arrays and checks both continuum normalizations against large finite packets. These are numerical consistency tests; the uniform approximation, compactness lemma and full asymptotic are proved above, not inferred from samples.

## Relationship to prior work
Kumar and Ruzhansky (2020, arXiv:2005.08464v1, Sections 1 and 5.1) study Fourier coefficient inequalities on the conjugacy-class hypergroup of \(SU(2)\), including the \(L^p\) Hardy–Littlewood inequality; this does not specify the sharp growing-degree \(L^2\to L^4\) synthesis constant or its extremizers. Dai, Gorbachev and Tikhonov (2017, arXiv:1708.09837v1, introduction and Theorem 1.1) give a full asymptotic norm relation for the \(L^p\to L^\infty\) spherical Nikolskii problem but, for finite target exponent, state a lower-limit inequality; their statement does not yield the upper limit and strong-modulus compactness here. Their 2019 follow-up (arXiv:1907.03832v1, Theorem A and Section 1) focuses on endpoint constants. The current result concerns the **zonal, central** full low-frequency packet and resolves this more specialized \(L^2\to L^4\) limit via positive fusion coefficients and two parity channels. Results about a *fixed number* of high-weight characters and endpoint norms of Peter–Weyl projections concern different asymptotic parameters or different operators. These distinctions do not prove historical priority; see limitations.

## Limitations
The continuum sharp value is determined by a genuine infinite-dimensional maximization rather than a closed elementary constant. No uniqueness, explicit formula or differential regularity of continuum maximizers is established. Modulus profiles are controlled, not arbitrary complex coefficient phases. The published-priority comparison is limited to the identified accessible sources and indexed research records; additional specialized Jacobi asymptotics could affect priority. All statements use the stated normalization and the full initial character packet, not arbitrary gaps or general compact groups.

## References
1. Vishvesh Kumar and Michael Ruzhansky, *Hardy–Littlewood inequality and \(L^p\)–\(L^q\) Fourier multipliers on compact hypergroups*, arXiv:2005.08464v1 (public 2020-05-18), especially Sections 1 and 5.1. https://arxiv.org/abs/2005.08464
2. Feng Dai, Dmitry Gorbachev and Sergey Tikhonov, *Nikolskii constants for polynomials on the unit sphere*, arXiv:1708.09837v1 (public 2017-08-31), especially Theorem 1.1 and the upper-limit section. https://arxiv.org/abs/1708.09837
3. Feng Dai, Dmitry Gorbachev and Sergey Tikhonov, *Estimates of the asymptotic Nikolskii constants for spherical polynomials*, arXiv:1907.03832v1 (public 2019-07-08), especially Theorem A and Section 1. https://arxiv.org/abs/1907.03832
