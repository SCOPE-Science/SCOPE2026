# Weak-trace spectral defect of power composition on Dirichlet-type Hilbert scales

## Finding
For each real \(s\) and integer \(d\ge 2\), consider the Hilbert space \(\mathcal H_s\) of analytic functions \(f(z)=\sum_{n\ge0}a_nz^n\) in the disk with
\[
\|f\|_s^2=\sum_{n\ge0}(n+1)^s|a_n|^2<\infty.
\]
Let \(C_df=f(z^d)\) and \(K_s=C_d^*C_d-C_dC_d^*\). Let \(Q_d\) be the orthogonal projection onto the span of monomials \(z^n\) with \(n\ge1\) not divisible by \(d\). Define
\[
a=d^s,\qquad b=-d^s s\left(1-\frac1d\right),\qquad R_s=K_s-aQ_d.
\]

**Theorem.** The self-adjoint operator \(R_s\) is compact, and \(\sigma_{\mathrm{ess}}(K_s)=\{0,a\}\). For \(s\ne0\), its singular values in nonincreasing order satisfy
\[
\lim_{j\to\infty}j\,\sigma_j(R_s)=2d^s|s|\left(1-\frac1d\right)^2=:A_{s,d}>0.
\]
Both its positive part \((R_s)_+\) and negative part \((R_s)_-\) have logarithmic spectral coefficient \(A_{s,d}/2\):
\[
\lim_{N\to\infty}\frac1{\log N}\sum_{j=1}^N\sigma_j((R_s)_\pm)=\frac{A_{s,d}}2.
\]
Consequently \(R_s\in\mathcal S_p\) exactly for \(p>1\), with \(R_s\in\mathcal S_{1,\infty}\setminus\mathcal S_1\) at the critical exponent. Here \(\mathcal S_{1,\infty}\) denotes compact operators with \(\sup_{j\ge1}j\sigma_j<\infty\). The signed diagonal trace along the natural degree filtration nevertheless converges:
\[
\boxed{\lim_{N\to\infty}\sum_{n=0}^{N}\langle R_s e_n,e_n\rangle=b\log d,}\qquad
 e_n=(n+1)^{-s/2}z^n.
\]
For \(s=0\), \(R_0=0\) exactly. The original self-commutator satisfies \(K_s\ge0\) for \(s\ge0\). When \(s<0\), it has infinitely many positive and infinitely many negative eigenvalues. For \(s>0\), it has strictly positive diagonal entries at every positive degree and one zero at degree zero.

The spectral coefficient above is a canonical singular-value limit; the signed degree-cutoff limit is a separate, basis-filtration-dependent quantity. Neither expression is asserted to be the ordinary trace of \(R_s\), which is not trace class for \(s\ne0\).

## Assumptions and scope
The scalar field is complex. The integer \(d\ge2\) and real parameter \(s\) are fixed as \(j,N\to\infty\). The inner product makes \(e_n=(n+1)^{-s/2}z^n\) an orthonormal basis. The operators act on all of \(\mathcal H_s\); no finite-dimensional cutoff is used in their definitions. Every power composition operator \(C_d\) is bounded because the monomial weights below are bounded above and below by positive constants depending only on \(d,s\). The singular-value claims for \(R_s\) concern its nonzero singular values, with zeros added if necessary.

## Proof
1. **Exact diagonalization.** On the orthonormal monomial basis,
\[
 C_de_n=\sqrt{w_n}\,e_{dn},\qquad
 w_n=\left(\frac{dn+1}{n+1}\right)^s,\quad n\ge0.
\]
Thus \(C_d^*C_de_n=w_ne_n\). Its range monomials have mutually distinct degrees, so \(C_dC_d^*e_n=w_{n/d}e_n\) when \(d\mid n\), and zero otherwise. For \(n=0\), both terms equal \(e_0\). Consequently,
\[
 K_se_n=\kappa_ne_n,\qquad
 \kappa_0=0,\quad
 \kappa_n=w_n-\mathbf1_{d\mid n}w_{n/d}\ (n\ge1).
\]
No off-diagonal terms remain. The sequence \(w_n\) is strictly increasing when \(s>0\), strictly decreasing when \(s<0\), and constant one when \(s=0\), since \((dn+1)/(n+1)\) increases strictly with \(n\) for \(d>1\). The sign and inertia assertions for \(K_s\) follow immediately: nonmultiples contribute positive \(w_n\), while positive multiples contribute \(w_n-w_{n/d}\) with sign \(s\).

2. **Compact normal form.** The elementary expansion
\[
 w_n=a+\frac bn+O_{s,d}(n^{-2})
 \qquad(n\to\infty)
\]
holds because \((dn+1)/(n+1)=d[1-(1-1/d)/(n+1)]\) and \((1+u)^s=1+su+O_s(u^2)\) uniformly for small \(u\). If \(r_n=\langle R_se_n,e_n\rangle\), then for positive degrees
\[
 r_n=\begin{cases}
 b/n+O_{s,d}(n^{-2}),&d\nmid n,\\
 b(1-d)/n+O_{s,d}(n^{-2}),&d\mid n.
 \end{cases}
\]
Also \(r_0=0\). Therefore \(r_n\to0\), so \(R_s\) is compact and \(K_s=aQ_d+R_s\). The range and kernel of \(Q_d\) are both infinite dimensional, giving precisely the Fredholm essential spectrum \(\{0,a\}\).

3. **Two tails and the sharp weak-trace coefficient.** Suppose \(s\ne0\), hence \(b\ne0\). Integers not divisible by \(d\) have density \(1-1/d\), whereas positive multiples have density \(1/d\). The preceding asymptotic expansions imply, as \(t\downarrow0\),
\[
 \#\{n\ge1: |r_n|>t\}
 \sim \frac{|b|}{t}\left[\left(1-\frac1d\right)+\frac{d-1}{d}\right]
 =\frac{2|b|(1-1/d)}t.
\]
To justify the asymptotic, sandwich \(|r_n|\), for all sufficiently large \(n\) in each residue class, between \((|c|-\varepsilon)/n\) and \((|c|+\varepsilon)/n\), with \(c=b\) or \(c=b(1-d)\), count integers in the arithmetic progressions, and then let \(\varepsilon\downarrow0\). The finitely many excluded indices have no effect. Inverting the counting asymptotic for decreasing rearrangements gives \(j\sigma_j(R_s)\to A_{s,d}=2|b|(1-1/d)\). For the positive and negative parts, precisely one residue group contributes at leading order to each sign, and each contributes \(|b|(1-1/d)\). This yields separately \(j\sigma_j((R_s)_\pm)\to A_{s,d}/2\); summing the harmonic asymptotics gives the stated logarithmic coefficients. The same estimates give \(\sum_n|r_n|^p<\infty\) exactly for \(p>1\). For \(s=0\), all \(w_n=1\) and the formulas give \(K_0=Q_d\) and \(R_0=0\).

4. **Exact shell identity and the conditional trace limit.** The degree cutoff is \(E_N=\operatorname{span}\{e_0,\dots,e_N\}\), with \(e_0\) contributing zero. For every \(N\ge1\), the exact diagonal formula telescopes:
\[
 \sum_{n=1}^N\kappa_n
 =\sum_{n=1}^N w_n-\sum_{k=1}^{\lfloor N/d\rfloor}w_k
 =\sum_{n=\lfloor N/d\rfloor+1}^{N}w_n.
\]
Since \(\operatorname{Tr}(Q_d|_{E_N})=N-\lfloor N/d\rfloor\), one obtains the exact finite identity
\[
 \sum_{n=0}^N\langle R_se_n,e_n\rangle
 =\sum_{n=\lfloor N/d\rfloor+1}^N(w_n-a).
\]
Insert \(w_n-a=b/n+O(n^{-2})\). The error tends to zero because its sum over \(\lfloor N/d\rfloor<n\le N\) is \(O(N^{-1})\). The harmonic sum tends to \(\log d\), giving the claimed signed limit. It is a natural cutoff prescription rather than a conventional trace.

## Verification
The accompanying `check.py` uses only the Python standard library. It performs exact-rational checks of the diagonal identities and finite shell telescoping for integral parameters, plus numerical large-degree checks for nonintegral parameters and sorted singular values. Execute `python3 check.py` from the directory containing the files. The proof above, not finite testing, establishes statements for all integers \(d\ge2\), real \(s\), and all dimensions. The checker is deterministic and prints its completed check count.

## Relationship to prior work
Abdollahi–Mehrangiz (2011) treated the exact spectra and self-commutator of monomial composition on the classical Dirichlet space, where the classical coefficient weight is degree \(n\), not the present \((n+1)^s\). Their Theorem 4.1 gives a scalar times a projection, so the critical \(1/j\) defect for the present analytic Hilbert scale is not stated there. Abdollahi–Mehrangiz–Roientan (2015) treated the ordinary Bergman case, corresponding exactly to the present \(s=-1\) coefficient weight; thus the underlying unweighted Bergman spectral diagonalization and its obvious specializations are *not* claimed new. The contribution here is the whole real-parameter Hilbert scale, together with the exact two-sided weak-trace coefficients and finite signed degree-cutoff anomaly. MacCluer–Weir (2004) investigated essentially normal Bergman composition operators with linear-fractional symbols, rather than these monomial symbols or their critical residual ideal.

The known endpoint spectral formulas alone do not state or imply a parameter-uniform theorem by logical specialization: the weights for the other real values of \(s\) are different operators. The present proof explicitly supplies those weighted diagonal entries and the residue-class asymptotics. The passage from a known diagonal entry formula at \(s=-1\) to any corollary for that particular point is not claimed as new.

## Limitations
This is a theorem for the coefficient-defined Dirichlet-type Hilbert scales and monomial symbols \(z^d\), not arbitrary weighted Bergman radial measures, nonmonomial self-maps, or multi-variable composition. The critical coefficient depends on the chosen Hilbert norm: equivalence of norms alone does not preserve adjoints, singular values, or self-commutators. The degree-cutoff signed trace depends on the canonical monomial grading and is not a basis-independent trace. A 2015 article on exactly the unweighted Bergman specialization was available only in bibliographic description, not in complete text; an unindexed generalization to arbitrary coefficient weights remains a historical-priority risk. The included finite calculations do not certify asymptotic assertions without the proof.

## References
- A. Abdollahi and S. Mehrangiz, *Self-Commutators of Composition Operators with Monomial Symbols on the Dirichlet Space*, Abstract and Applied Analysis (2011), article 618968. DOI: 10.1155/2011/618968. First verified day-resolved publication: 2011-10-27.
- A. Abdollahi, S. Mehrangiz and T. Roientan, *Self-commutators of composition operators with monomial symbols on the Bergman space*, Bulletin of the Iranian Mathematical Society 41 (2015), issue 7, 65–76. Bibliographic description: https://eurekamag.com/research/109/906/109906911.php.
- B. D. MacCluer and R. J. Weir, *Essentially normal composition operators on Bergman spaces*, Acta Sci. Math. (Szeged) 70 (2004), 799–817. Full text: https://www.acta.hu/download.phtml?id=2815.
