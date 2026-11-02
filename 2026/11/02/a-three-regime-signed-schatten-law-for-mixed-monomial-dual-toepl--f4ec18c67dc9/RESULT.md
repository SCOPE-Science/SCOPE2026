# A three-regime signed Schatten law for mixed-monomial dual Toeplitz self-commutators

## Finding
Let \(p,q\) be distinct positive integers and \(\eta\ne0\). For the dual Toeplitz operator \(S_{z^p+\eta\overline z^{\,q}}\) on the orthogonal complement of the analytic Bergman space in normalized disk \(L^2\), its self-commutator \(D=S^*S-SS^*\) is trace class, has infinitely many positive and infinitely many negative eigenvalues, has infinite-dimensional kernel, and satisfies
\[
\operatorname{Tr}D=|\eta|^2q-p.
\]
Its complete nonzero spectrum is given below by explicit quadratic equations, one for each angular Fourier sector. The positive and negative spectral parts undergo three distinct sharp Schatten transitions. Put
\[
s=|\eta|^2q^2-p^2,\qquad g=|\eta|^2p^2q^2(p-q)^2.
\]
If \(s>0\), the ordered nonzero positive and absolute negative eigenvalues respectively decay as \(s j^{-2}\) and \((g/s)j^{-4}\). If \(s<0\), their respective asymptotics are \((g/|s|)j^{-4}\) and \(|s|j^{-2}\). On the balanced surface \(|\eta|=p/q\), both decay cubically:
\[
\lambda_j(D_+)\sim c_+j^{-3},\qquad
\lambda_j(D_-)\sim c_-j^{-3},\qquad
c_\pm=\frac{p^2}{2}\big(\sqrt{13}|p-q|\pm3(p-q)\big)>0.
\]
Here \(D_+=\max(D,0)\), \(D_-=\max(-D,0)\), and all nonzero eigenvalues are arranged in nonincreasing order with multiplicity. Therefore, for every \(t>0\), the optimal Schatten membership thresholds for \((D_+,D_-)\) are \((t>1/2,t>1/4)\) if \(s>0\), \((t>1/4,t>1/2)\) if \(s<0\), and \((t>1/3,t>1/3)\) if \(s=0\). The equality endpoints are excluded.

## Assumptions and scope
Let \(\mathbb D\) be the unit disk with normalized area measure \(dA=dx\,dy/\pi\), let \(A^2=A^2(\mathbb D,dA)\) be its complex analytic Bergman space, and let \(P:L^2\to A^2\) be the orthogonal projection. Set \(Q=I-P\), \(\mathcal K=QL^2\). The dual Toeplitz operator with bounded symbol \(\phi\) is \(S_\phi=QM_\phi|_{\mathcal K}\). The Bergman Hankel operator is \(H_f=QM_f|_{A^2}\). Only distinct positive integer exponents and nonzero complex \(\eta\) are claimed; no equivalence with other classes of Toeplitz compression is assumed.

**Exact spectrum.** For every \(\ell\ge0\), put \(L=\ell+1\) and define
\[
 A_m(L)=\frac{m^2}{(L+m)(L+2m)},\qquad
 G_{pq}(L)=\frac{pq}{(L+p+q)\sqrt{(L+p)(L+q)}},
\]
\[
 \Delta(L)=A_p(L)A_q(L)-G_{pq}(L)^2
 =\frac{p^2q^2(p-q)^2}{(L+p)(L+q)(L+2p)(L+2q)(L+p+q)^2}>0,
\]
\[
 \tau(L)=|\eta|^2A_q(L)-A_p(L),\qquad
 \lambda_{\pm,\ell}=
 \frac{\tau(L)\pm\sqrt{\tau(L)^2+4|\eta|^2\Delta(L)}}2.
\]
These two simple eigenvalues have strictly opposite signs for every \(\ell\ge0\). The remaining possible nonzero eigenvalues occur in finitely many sectors \(\ell=-r\), where \(1\le r\le\max(p,q)\). For those sectors replace \(A_m(L)\) by
\[
 A_m^{(-r)}=\begin{cases}\frac{m-r+1}{2m-r+1},&r\le m,\\0,&r>m,\end{cases}
\]
and replace \(G_{pq}(L)\) by
\[
 G_{pq}^{(-r)}=\begin{cases}
 \frac{\sqrt{(p-r+1)(q-r+1)}}{p+q-r+1},&r\le\min(p,q),\\0,&r>\min(p,q).
 \end{cases}
\]
Use the same quadratic roots with \(\tau=|\eta|^2A_q^{(-r)}-A_p^{(-r)}\) and \(\Delta=A_p^{(-r)}A_q^{(-r)}-(G_{pq}^{(-r)})^2\), omitting zero roots. There are no further nonzero eigenvalues, and \(0\) has infinite multiplicity.

## Proof
**1. The known dual Toeplitz–Hankel identity.** The product identity of Stroethoff–Zheng gives
\[
 S_fS_g=S_{fg}-H_fH_{\overline g}^*.
\]
For \(\phi=z^p+\eta\overline z^{\,q}\), this implies
\[
 D=H_\phi H_\phi^*-H_{\overline\phi}H_{\overline\phi}^*
 =|\eta|^2H_{\overline z^{\,q}}H_{\overline z^{\,q}}^*
 -H_{\overline z^{\,p}}H_{\overline z^{\,p}}^*.
\]
The first equality is an established algebraic identity, not an asserted novelty of this result.

**2. Angular-mode Gram decomposition.** The normalized Bergman monomials are \(e_n=\sqrt{n+1}z^n\), \(n\ge0\). For \(m\ge1\) and each integer \(\ell\ge-m\), define
\[
 u_{m,\ell}=H_{\overline z^{\,m}}e_{\ell+m}.
\]
If \(\ell\ge0\), the Bergman projection formula gives
\[
 u_{m,\ell}=\sqrt{\ell+m+1}
 \left(z^{\ell+m}\overline z^{\,m}-\frac{\ell+1}{\ell+m+1}z^\ell\right).
\]
If \(-m\le\ell<0\), the projection term is absent, leaving \(u_{m,\ell}=\sqrt{\ell+m+1}z^{\ell+m}\overline z^{\,m}\). The operators are orthogonal across angular degrees \(\ell\), and
\[
 H_{\overline z^{\,m}}H_{\overline z^{\,m}}^*
 =\bigoplus_{\ell\ge-m}|u_{m,\ell}\rangle\langle u_{m,\ell}|.
\]
Normalized disk moments \(\int_{\mathbb D}|z|^{2k}dA=(k+1)^{-1}\) give, for \(\ell\ge0\),
\[
 \|u_{m,\ell}\|^2=A_m(L),\qquad
 \langle u_{p,\ell},u_{q,\ell}\rangle=G_{pq}(L).
\]
For \(\ell=-r<0\), the corresponding Gram entries are exactly \(A_m^{(-r)}\) and \(G_{pq}^{(-r)}\). Thus every angular block of \(D\) is a signed difference of two rank-one positive operators, of rank at most two. On a rank-two block its trace is \(\tau\) and determinant is \(-|\eta|^2\Delta\); the displayed quadratic equation follows. Its discriminant is positive for all nonnegative \(\ell\), since the exact rational determinant \(\Delta(L)>0\) whenever \(p\ne q\). Hence one simple eigenvalue of each sign occurs in every such block. For \(\ell<0\), the formula with zero roots discarded is still correct, even for rank-one blocks. Angular blocks outside the specified range vanish. Each angular sector contains an infinite-dimensional radial orthogonal complement to the span of these at most two vectors, proving the infinite-dimensional zero eigenspace.

**3. Trace-class summability and trace.** For all \(n\ge0\), the exact Hankel-vector norms are
\[
 \|H_{\overline z^{\,m}}e_n\|^2=\begin{cases}
 \dfrac{n+1}{n+m+1},&0\le n<m,\\
 \dfrac{m^2}{(n+1)(n+m+1)},&n\ge m.
 \end{cases}
\]
A telescoping sum gives \(\|H_{\overline z^{\,m}}\|_{\mathcal S_2}^2=m\). Therefore \(D\) is a difference of two positive trace-class operators and \(\operatorname{Tr}D=|\eta|^2q-p\).

**4. Noncritical asymptotics.** Direct denominator expansion gives
\[
 A_m(L)=m^2L^{-2}-3m^3L^{-3}+O(L^{-4}),\qquad
 \Delta(L)=p^2q^2(p-q)^2L^{-6}\big(1+O(L^{-1})\big).
\]
Consequently \(\tau(L)=sL^{-2}+O(L^{-3})\), while the product of block eigenvalues is \(-gL^{-6}(1+O(L^{-1}))\). For \(s>0\) the positive eigenvalue is \(sL^{-2}(1+o(1))\), forcing its negative partner to be \(-(g/s)L^{-4}(1+o(1))\); for \(s<0\) their roles reverse. Finitely many exceptional sectors do not change ordered-eigenvalue asymptotics.

**5. Critical asymptotics.** If \(|\eta|=p/q\), direct subtraction yields the exact formula
\[
 \tau(L)=\frac{p^2(p-q)(3L+2p+2q)}{(L+p)(L+2p)(L+q)(L+2q)}
 =3p^2(p-q)L^{-3}+O(L^{-4}),
\]
and \(|\eta|^2\Delta(L)=p^4(p-q)^2L^{-6}(1+O(L^{-1}))\). Substitution in the quadratic roots yields the two stated positive constants involving \(\sqrt{13}\), with cubic decay on both sides. Because \(\sum_{j\ge1}j^{-a t}\) converges exactly when \(a t>1\), the three Schatten thresholds follow for all positive \(t\), including quasi-Banach Schatten ideals.

## Verification
The accompanying standalone \(\texttt{checker.py}\) uses exact rational disk moments and exact rational Gram-determinant identities, tests the finite angular-block inertia, reproduces trace telescoping, and checks high-index asymptotic values. Run with \(\texttt{python3 checker.py}\) from the extracted package. The observed run passed 83,450 finite assertions. These checks are supplementary; the infinite spectral classification and asymptotic statements are established by the preceding proof.

## Relationship to prior work
Kong, Li, Sun, and Zheng (2026) establish qualitative hyponormality and subnormality criteria for dual Toeplitz operators, including harmonic polynomial symbols. Those criteria do not state the full signed eigenvalue sequence of the compact self-commutator or the balanced cubic decay regime. The dual Toeplitz–Hankel product identity used here comes from Stroethoff and Zheng (2002). Existing general Bergman Hankel operator-ideal results may determine coarse membership, but the exact two-eigenvalue angular spectrum, opposite-sign decay exponents and critical \(\sqrt{13}\) coefficients require the signed Gram calculation presented above. No assertion is made that the foundational product identity, radial moment formula or rank-two linear algebra are new.

## Limitations
Only monomial harmonic symbols with distinct positive exponents are treated. No statement is made for general polynomial symbols, arbitrary radial weights or Toeplitz compressions onto different Hilbert spaces. No independent mathematical validation or exhaustive publication-priority certification has been performed. A 2020 paper on dual Toeplitz spectra could only be compared through accessible abstract and partial text, leaving a residual risk of a differently formulated earlier result.

## References
1. L. Kong, Y. Li, D. Sun, D. Zheng, *Hyponormal and subnormal dual Toeplitz operators*, arXiv:2610.34017v1 (first posted 2026-10-25), https://arxiv.org/html/2610.34017v1.
2. K. Stroethoff, D. Zheng, *Algebraic and spectral properties of dual Toeplitz operators*, Transactions of the American Mathematical Society 354 (2002), 2495–2520, https://math.vanderbilt.edu/zhengd/DT.pdf.
3. C. Ding, et al., *Invertibility and spectral properties of dual Toeplitz operators*, Journal of Mathematical Analysis and Applications 484 (2020), 123762, https://doi.org/10.1016/j.jmaa.2019.123762 (full text not inspected).
