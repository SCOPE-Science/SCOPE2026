# A sharp one-moment rescue limit for residual-screened Gaussian orthogonalization

## Finding

Consider one exact step of Gaussian-sketched Gram–Schmidt with \(k\ge 1\) previously orthonormal ambient columns, one new orthogonal unit input, and \(m\ge k+1\) Gaussian sketch rows. Write \(d=m-k\). Generate \(L\ge1\) independent sketches and select the candidate having the largest *sketched least-squares residual norm*. For the resulting sketch-normalized ambient vector \(q_*\), every positive real moment has the **exact integrability boundary**

\[
\mathbb E\|q_*\|_2^p<\infty\quad\Longleftrightarrow\quad 0<p<\min\{d+1,Ld\}.
\]

In particular, two sketches raise the moment cutoff from \(d\) to \(d+1\), but no number of independent candidates can improve it further using only the residual norms to choose a candidate. The largest-residual rule minimizes every positive moment of \(\|q\|_2\), among all rules based solely on those norms, in the extended-real sense.

**The angular defect cannot be screened this way.** Regardless of \(L\), for any residual-only selection rule, the squared fraction of the ambient norm lying in the previously spanned subspace has law

\[
\frac{\|U^\top q\|_2^2}{\|q\|_2^2}
\sim \operatorname{Beta}\!\left(\frac{k}{2},\frac{d+1}{2}\right),
\qquad
\mathbb E\frac{\|U^\top q\|_2^2}{\|q\|_2^2}=\frac{k}{m+1}.
\]

At the first nontrivial finite-variance boundary \(d=2\), exactly two candidates have the explicit expectation

\[
\mathbb E\|q_*\|_2^2=m(k+1)\log 2,
\]

whereas one candidate has infinite squared norm in expectation. For instance, \(k=1,m=3\) gives \(6\log2\) for two candidates but infinite expectation for one.

## Assumptions and scope

Let \(n\ge k+1\). Fix \(U\in\mathbb R^{n\times k}\) with \(U^\top U=I_k\), and a unit vector \(z\in\mathbb R^n\) with \(U^\top z=0\). For each \(j=1,\ldots,L\), independently draw \(S_j\in\mathbb R^{m\times n}\) with i.i.d. \(N(0,1/m)\) entries. Define the unique least-squares coefficient, residual length, and ambient candidate almost surely by

\[
 c_j=\arg\min_{c\in\mathbb R^k}\|S_j(z-Uc)\|_2,\qquad
 \rho_j=\|S_j(z-Uc_j)\|_2,\qquad
 q_j=\frac{z-Uc_j}{\rho_j}.
\]

Thus \(\|S_jq_j\|_2=1\) and \((S_jU)^\top S_jq_j=0\), but \(q_j\) need not be Euclidean-orthogonal to \(U\) or have unit Euclidean norm. Let \(J=\arg\max_j\rho_j\); ties have probability zero. A **residual-only rule** may instead select any random index measurable from \((\rho_1,\ldots,\rho_L)\) and independent supplementary randomization, but not from the coefficient vectors or the original ambient candidates. All statements concern one step, exact arithmetic, and fixed input \((U,z)\).

## Proof

**1. Gaussian regression and independence.** Put \(G_j=\sqrt m S_jU\) and \(h_j=\sqrt m S_jz\). Each \(G_j\) is an \(m\times k\) standard Gaussian matrix independent of standard Gaussian \(h_j\). For one candidate, suppress the subscript and write \(P_G=G(G^\top G)^{-1}G^\top\). Then

\[
 c=(G^\top G)^{-1}G^\top h,\qquad
 Z= m\rho^2=\|(I-P_G)h\|_2^2\sim\chi^2_d.
\]

Conditionally on \(G\), the projected components \(P_Gh\) and \((I-P_G)h\) are independent, and the conditional law of \(Z\) is always \(\chi^2_d\). Hence \(c\) and \(Z\) are independent; this also holds jointly across all independently drawn candidates.

**2. Exact coefficient distribution.** The coefficient vector has the multivariate Student representation

\[
 c\ \overset{\mathrm d}=\ \frac{v}{\sqrt Y},\qquad
 v\sim N(0,I_k),\quad Y\sim\chi^2_{d+1},\quad v\perp Y.
\]

To verify rather than assume the distribution, fix any nonzero deterministic \(t\in\mathbb R^k\). Conditionally on \(G\), \(t^\top c\) is centered normal with variance \(t^\top(G^\top G)^{-1}t\). Right orthogonal invariance of \(G\) reduces the latter quadratic form to \(\|t\|_2^2((G^\top G)^{-1})_{11}\). A Schur complement expresses its reciprocal as the squared length of the first Gaussian column after projection off the other \(k-1\) columns, namely \(\chi^2_{m-k+1}=\chi^2_{d+1}\). The stated Student representation therefore holds for every \(t^\top c\), and the Cramér–Wold theorem identifies the full vector distribution. Consequently

\[
 \|c\|_2^2\ \overset{\mathrm d}=\ X/Y,
 \qquad X\sim\chi^2_k,\quad Y\sim\chi^2_{d+1},\quad X\perp Y.
\]

**3. Selected norm factorization.** Set \(Z_{(L)}=\max_j Z_j\). Selection by the residuals leaves the chosen coefficient distributed like an independent copy of \(c\), independent of the entire residual vector, because every coefficient is independent of every residual and the coefficient copies are identically distributed. Orthogonality of \(z\) and columns of \(U\) gives

\[
 \|q_*\|_2^2=\frac{1+\|c_J\|_2^2}{\rho_J^2}
 \ \overset{\mathrm d}=\ m\frac{1+X/Y}{Z_{(L)}},
\]

where \(X,Y,Z_{(L)}\) are mutually independent. Hence for all \(p>0\), the extended positive expectation factors exactly:

\[
 \mathbb E\|q_*\|_2^p
 =m^{p/2}\,\mathbb E(1+X/Y)^{p/2}\,\mathbb EZ_{(L)}^{-p/2}.
\]

Near zero, the \(\chi^2_{d+1}\) density is comparable to \(y^{(d+1)/2-1}\), so the coefficient factor is integrable exactly for \(p<d+1\). The \(\chi^2_d\) cumulative distribution satisfies \(\Pr(Z\le t)\asymp t^{d/2}\) as \(t\downarrow0\), giving \(\Pr(Z_{(L)}\le t)\asymp t^{Ld/2}\); thus its inverse moment is integrable exactly for \(p<Ld\). At equality on either boundary, the relevant density integral diverges logarithmically. This proves the sharp if-and-only-if statement, including both endpoints.

**4. Optimality and saturation.** Every residual-only selection has the same independent coefficient factor in Step 3, and its selected squared residual satisfies \(Z_J\le Z_{(L)}\) pointwise. This proves simultaneous optimality of the maximum-residual choice, even when the moment expectations are infinite. For \(L\ge2\) and integer \(d\ge1\), \(Ld\ge d+1\), establishing exact saturation of the moment rescue at one extra power. No bound based solely on screening residuals removes the independent coefficient singularity.

**5. Angular invariance and explicit case.** Since \(U^\top q_J=-c_J/\rho_J\),

\[
 \frac{\|U^\top q_J\|_2^2}{\|q_J\|_2^2}
 =\frac{\|c_J\|_2^2}{1+\|c_J\|_2^2}
 \ \overset{\mathrm d}=\ \frac{X}{X+Y}
 \sim\operatorname{Beta}(k/2,(d+1)/2).
\]

For \(d=2,L=2,p=2\), \(\mathbb E(1+X/Y)=1+k\), while \(Z_j\sim\chi^2_2\), so the density of \(Z_{(2)}\) yields, by Frullani's integral,

\[
 \mathbb E\frac1{Z_{(2)}}
 =\int_0^\infty\frac{e^{-t/2}-e^{-t}}t\,dt=\log2.
\]

Multiplying the independent factors proves \(m(k+1)\log2\), as stated. For \(L=1\), the inverse moment of \(\chi^2_2\) diverges.

## Verification

The self-contained `verify.py` checks the predicted moment cutoff over 288 parameter tuples, 162 direct Gaussian least-squares instances with four identities each, the two-dimensional second-moment and angular benchmarks, coefficient–residual independence diagnostics, and the Frullani integral. It reports **948 checks passed** using NumPy, including batch-median diagnostics to reduce unstable empirical means of heavy-tailed finite-moment quantities. One can reproduce using `python -m pip install -r requirements.txt` followed by `python verify.py`. No simulation or truncated numerical integration is used to prove an infinite-moment claim; all such claims are derived in the proof.

## Relationship to prior work

Balabanov and Grigori's randomized Gram–Schmidt (arXiv:2011.05090v1, Algorithm 2) introduces the sketched least-squares and sketched-residual normalization motivating this one-step model. Its embedding, accuracy and numerical-stability analysis is different from residual-only selection among independently resketched candidates. Jang and Grigori's later RGS-L2 work (DOI:10.1002/nla.70029) repairs Euclidean orthogonality by reorthogonalization, not by the residual-only screening studied here. Classical Gaussian regression and inverse-Wishart distributions underlie Step 2 and are not claimed as new. A previously available result on Gaussian low-rank sketch failure gives the coefficient's Student moment cutoff; the new statement concerns the joint independent residual factor, optimal residual-only selection, and the sharp saturation of moment rescue while angular error remains invariant.

## Limitations

This is a one-step exact-distribution statement for real independent Gaussian sketches and fixed Euclidean-orthonormal prior columns. It does not give an end-to-end floating-point backward-error bound, an Arnoldi/GMRES convergence theorem, or an optimal choice of candidates under computational cost constraints. Selecting candidates using coefficient information falls outside the proved optimality class. A residual-only filter cannot reduce the mean angular defect in this model. The nonexistence of a high-order moment does not imply that any particular realized sketch fails or that its errors have an infinite mean at every order. A mathematically equivalent specialized result may exist outside the inspected literature.

## References

1. O. Balabanov and L. Grigori, *Randomized Gram-Schmidt process with application to GMRES*, arXiv:2011.05090v1 (publicly submitted 2020-11-10), https://arxiv.org/abs/2011.05090.
2. Y. Jang and L. Grigori, *Randomized Orthogonalization Process With Reorthogonalization*, Numerical Linear Algebra with Applications 32 (2025), e70029, DOI:10.1002/nla.70029.
3. R. J. Muirhead, *Aspects of Multivariate Statistical Theory*, Wiley (1982), for classical Gaussian regression, Wishart and multivariate Student calculations.
