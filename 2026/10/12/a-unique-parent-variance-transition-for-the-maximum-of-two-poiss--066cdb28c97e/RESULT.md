# A unique parent-variance transition for the maximum of two Poisson counts

## Finding

For each \(\lambda>0\), let \(X_1,X_2\) be independent \(\operatorname{Pois}(\lambda)\) variables, and set \(M_\lambda=\max\{X_1,X_2\}\). Write \(I_j\) for the modified Bessel function of the first kind of integer order \(j\). Define
\[
 k_\lambda=e^{-2\lambda}I_0(2\lambda),\qquad
 h_\lambda=\lambda e^{-2\lambda}\bigl(I_0(2\lambda)+I_1(2\lambda)\bigr).
\]
There is exactly one \(\lambda_*\in(0,\infty)\) such that \(\operatorname{Var}(M_{\lambda_*})=\lambda_*\). It is the unique positive solution of
\[
 \lambda e^{-2\lambda}\frac{\bigl(I_0(2\lambda)+I_1(2\lambda)\bigr)^2}{I_0(2\lambda)}=1,
\]
and \(\lambda_*\approx1.16679740191840365086656\). The full, strict variance comparison with the **parent** Poisson law is
\[
\begin{aligned}
  \operatorname{Var}(M_\lambda)&>\lambda&&\text{if }0<\lambda<\lambda_*,\\
  \operatorname{Var}(M_\lambda)&=\lambda&&\text{if }\lambda=\lambda_*,\\
  \operatorname{Var}(M_\lambda)&<\lambda&&\text{if }\lambda>\lambda_*.
\end{aligned}
\]
At every positive intensity, however, the maximum is strictly underdispersed relative to its **own** mean:
\[\operatorname{Var}(M_\lambda)<\mathbb E M_\lambda.\]
In particular, the two dispersion comparisons should not be conflated.

## Assumptions and scope

Both counts have the same strictly positive Poisson intensity and are independent. Every inequality holds for all real \(\lambda>0\), not merely for integer intensities or a finite numerical grid. The observation is the maximum of exactly two counts; no assertion is made about maxima of larger samples or heterogeneous intensities. The variance benchmark \(\lambda\) is the variance (and mean) of an *individual parent count*, not the mean of the maximum.

## Proof

**Step 1: exact moments.** Put \(S=X_1+X_2\) and \(D=X_1-X_2\). Then \(M_\lambda=(S+|D|)/2\), \(\operatorname{Var}(S)=2\lambda\), and \(\mathbb E D^2=2\lambda\). The symmetric Skellam mass function gives
\[
 \Pr(D=j)=e^{-2\lambda}I_{|j|}(2\lambda)\quad(j\in\mathbb Z).
\]
The standard modified-Bessel recurrence
\[jI_j(2\lambda)=\lambda\bigl(I_{j-1}(2\lambda)-I_{j+1}(2\lambda)\bigr)\]
telescopes, by absolute convergence, to
\[\mathbb E|D|=2\lambda e^{-2\lambda}\bigl(I_0(2\lambda)+I_1(2\lambda)\bigr)=2h_\lambda.\]
Thus \(\mathbb E M_\lambda=\lambda+h_\lambda\). For any integrable count statistic \(G(X_1,X_2)\), differentiating the two-Poisson exponential-family weights yields
\[
 \frac{d}{d\lambda}\mathbb EG=\frac1\lambda\operatorname{Cov}\bigl(S,G\bigr).
\]
Since \(I_0'(z)=I_1(z)\) and \(I_1'(z)=I_0(z)-I_1(z)/z\), where prime denotes differentiation in the Bessel argument, direct differentiation shows \(h_\lambda'=k_\lambda\). Hence
\[
 \operatorname{Cov}(S,|D|)=\lambda\frac{d}{d\lambda}\mathbb E|D|=2\lambda k_\lambda.
\]
Combining this with \(\operatorname{Var}(|D|)=2\lambda-4h_\lambda^2\) gives the exact identities
\[
 \boxed{\mathbb EM_\lambda=\lambda+h_\lambda,\qquad
 \operatorname{Var}(M_\lambda)=\lambda+\lambda k_\lambda-h_\lambda^2.}
\]

**Step 2: a strictly monotone sign ratio.** Define
\[
 r_\lambda=\frac{I_1(2\lambda)}{I_0(2\lambda)},\qquad
 R_\lambda=\frac{h_\lambda^2}{\lambda k_\lambda}
 =\lambda k_\lambda(1+r_\lambda)^2.
\]
The integral representation of modified Bessel functions implies \(0<r_\lambda<1\): explicitly, \(I_0(2\lambda)-I_1(2\lambda)=\pi^{-1}\int_0^\pi e^{2\lambda\cos\theta}(1-\cos\theta)\,d\theta>0\), and the defining power series gives \(I_1>0\). The displayed derivative identities give
\[
 \frac{k_\lambda'}{k_\lambda}=2(r_\lambda-1),\qquad
 r_\lambda'=2(1-r_\lambda^2)-\frac{r_\lambda}{\lambda}.
\]
Therefore, without any numerical monotonicity assumption,
\[
 \boxed{\frac{d}{d\lambda}\log R_\lambda
  =(1-r_\lambda)\left(2+\frac1{\lambda(1+r_\lambda)}\right)>0.}
\]
The power series \(I_0(2\lambda)=1+O(\lambda^2)\) and \(I_1(2\lambda)=\lambda+O(\lambda^3)\) imply \(R_\lambda\sim\lambda\) as \(\lambda\downarrow0\). Standard fixed-order Bessel asymptotics \(I_j(2\lambda)\sim e^{2\lambda}/\sqrt{4\pi\lambda}\) show \(R_\lambda\sim2\sqrt{\lambda/\pi}\) as \(\lambda\to\infty\). Hence \(R_\lambda\) crosses \(1\) exactly once, at \(\lambda_*\). Finally,
\[
 \operatorname{Var}(M_\lambda)-\lambda
 =\lambda k_\lambda(1-R_\lambda)
\]
proves all three sign regimes.

**Step 3: distinguish the two benchmarks.** The difference between the maximum's own mean and its variance is
\[
 \mathbb EM_\lambda-\operatorname{Var}(M_\lambda)
 =h_\lambda^2+\lambda e^{-2\lambda}I_1(2\lambda)>0.
\]
Thus the parent-variance transition is compatible with underdispersion relative to the maximum's mean. Moreover the same Bessel asymptotics yield
\[
 \lim_{\lambda\to\infty}\frac{\operatorname{Var}(M_\lambda)}{\lambda}=1-\frac1\pi.
\]
This completes the proof.

## Verification

Run `python verify.py` with a Python interpreter supporting the standard-library `decimal` module. The script independently obtains the maximum's first two moments from the nonnegative mass identity
\[
 \Pr(M_\lambda=j)=F_\lambda(j)^2-F_\lambda(j-1)^2\qquad(j\ge0),
\]
where \(F_\lambda(-1)=0\) and \(F_\lambda\) is the Poisson CDF; it compares these moments with the two Bessel-series formulas at 16 positive intensities. With 72-digit Decimal arithmetic, it checks discrepancies less than \(10^{-42}\) and brackets the unique root by bisection. These finite checks do not establish the universal result; the preceding analytic argument does.

## Relationship to prior work

Badiella, del Castillo, and Puig prove that discrete order statistics preserve ultra-log-concavity and deduce that Poisson order statistics have variance strictly smaller than **their own mean**. This establishes neither a comparison with the *parent intensity* \(\lambda\) nor the existence and uniqueness of the sign-change point. The standard Skellam law and its Bessel recurrence give the ingredients for the exact moment expressions. Such expressions by themselves do not settle the global number of crossings: the additional strict derivative identity for \(R_\lambda\) is the determining step here. Existing exact moment formulas, including those available independently from the Skellam identities, are treated as known mathematical inputs rather than claimed as novel. The new assertion is the complete unique-crossing classification relative to the parent variance.

## Limitations

The location \(\lambda_*\) is defined exactly by a transcendental equation, not claimed to admit elementary closed form. Its decimal approximation is numerical only. The statement concerns two *independent identically distributed* Poisson observations and no larger sample. An equivalent parameter-transition theorem could exist in less directly indexed order-statistic or modified-Bessel literature. The literature comparison is not an independent publication audit.

## References

1. L. Badiella, J. del Castillo, P. Puig, “Ultra log-concavity of discrete order statistics,” *Statistics & Probability Letters* **201** (2023), 109900, DOI: 10.1016/j.spl.2023.109900; open-access full text: https://ddd.uab.cat/pub/artpub/2023/283158/StaProLet_a2023v201n109900.pdf. Article first listed available online 26 June 2023.
2. H. L. Gan, E. D. Kolaczyk, “Approximation of the difference of two Poisson-like counts with Skellam,” arXiv:1708.04018 (2017), https://arxiv.org/abs/1708.04018.
3. NIST Digital Library of Mathematical Functions, §§10.29 and 10.40 (modified Bessel recurrence, differentiation, and large-argument asymptotics): https://dlmf.nist.gov/10.29 and https://dlmf.nist.gov/10.40.
4. P. Puig and collaborators, “Some mechanisms leading to underdispersion: Old and new proposals,” *Scandinavian Journal of Statistics* (2024), DOI: 10.1111/sjos.12677, https://onlinelibrary.wiley.com/doi/10.1111/sjos.12677.
