# Exact local-time covariance hierarchy for Brownian-bridge power energies

## Finding

Let \(B=(B_t)_{0\le t\le1}\) be a standard Brownian bridge from \(0\) to \(0\). Let \(L=L_1^0\) be its local time at zero, normalized by the occupation-density formula
\[
\int_0^1 f(B_s)\,ds=\int_{\mathbb R}f(x)L_1^x\,dx,
\]
for nonnegative Borel functions \(f\). Set \(I_0=1\) and, for each integer \(q\ge1\), set
\[
I_q=\int_0^1 B_t^{2q}\,dt.
\]
Then for every integer \(q\ge0\),
\[
\operatorname{Cov}(L,I_q)=\sqrt{\frac{\pi}{2}}\,\frac{q!}{2^q(2q+1)}\left(\frac{\binom{2q+2}{q+1}}{2^{2q+1}}-1\right).
\]
The covariance is zero for \(q=0\) and strictly negative for every \(q\ge1\). In particular,
\[
\operatorname{Cov}\!\left(L,\int_0^1 B_t^2\,dt\right)=-\frac{1}{24}\sqrt{\frac{\pi}{2}}.
\]

## Assumptions and scope

The bridge is the centered Gaussian process with covariance \(K(s,t)=\min(s,t)-st\). Local time has the occupation-density normalization above; changing local-time convention changes the covariance by the same multiplicative factor. The theorem concerns integer even powers on the unit time interval. It does not assert a full joint law, independence, or a general covariance sign for arbitrary path functionals.

## Proof

For \(0<s<1\), the marginal density of \(B_s\) at zero is
\[
p_s(0)=\frac{1}{\sqrt{2\pi s(1-s)}}.
\]
Conditioning the Gaussian bridge on \(B_s=0\) gives a centered Gaussian bridge on each side of \(s\). Its conditional variance at time \(t\) is
\[
v(s,t)=\begin{cases}
\dfrac{t(s-t)}{s},&0<t\le s,\[4pt]
\dfrac{(t-s)(1-t)}{1-s},&s\le t<1.
\end{cases}
\]
Therefore \(\mathbb E[B_t^{2q}\mid B_s=0]=(2q-1)!!\,v(s,t)^q\) for integer \(q\ge1\). Integrating separately on \((0,s)\) and \((s,1)\), with the substitutions \(t=su\) and \(t=s+(1-s)u\), yields
\[
\int_0^1 v(s,t)^q\,dt=\operatorname{B}(q+1,q+1)\bigl(s^{q+1}+(1-s)^{q+1}\bigr),
\]
where \(\operatorname{B}\) is the beta function.

The occupation-density formula, the joint Gaussian density, and Tonelli's theorem then give
\[
\mathbb E[L I_q]=\frac{2(2q-1)!!\,\operatorname{B}(q+1,q+1)\operatorname{B}(q+\tfrac32,\tfrac12)}{\sqrt{2\pi}}.
\]
Also,
\[
\mathbb E[L]=\int_0^1p_s(0)\,ds=\sqrt{\frac{\pi}{2}},\qquad
\mathbb E[I_q]=(2q-1)!!\operatorname{B}(q+1,q+1)=\frac{q!}{2^q(2q+1)}.
\]
Subtracting \(\mathbb E[L]\mathbb E[I_q]\) gives
\[
\operatorname{Cov}(L,I_q)=\sqrt{\frac{\pi}{2}}\,\mathbb E[I_q]\left(\frac{2}{\pi}\operatorname{B}(q+\tfrac32,\tfrac12)-1\right).
\]
The beta–gamma identity gives
\[
\frac{2}{\pi}\operatorname{B}(q+\tfrac32,\tfrac12)=\frac{\binom{2q+2}{q+1}}{2^{2q+1}},
\]
which proves the stated formula for \(q\ge1\). For \(q=0\), \(I_0=1\), so the covariance is zero and the same displayed formula evaluates to zero.

For \(n=q+1\ge2\), \(2^{2n}=\sum_{k=0}^{2n}\binom{2n}{k}\ge\binom{2n}{n}+2\binom{2n}{n-1}=\binom{2n}{n}\left(1+\frac{2n}{n+1}\right)>2\binom{2n}{n}\). Hence \(\binom{2q+2}{q+1}<2^{2q+1}\), so the bracket is strictly negative. At \(q=1\), the factor is \(\binom42/2^3-1=-1/4\), giving the stated quadratic-energy covariance.

## Verification

The proof is analytic and uses only the Gaussian conditional-variance formula, the occupation-density normalization, and beta integrals. Substitution checks give zero at \(q=0\), \(-\sqrt{\pi/2}/24\) at \(q=1\), and \(-3\sqrt{\pi/2}/80\) at \(q=2\). No finite simulation is used as proof of the all-\(q\) statement.

## Relationship to prior work

Pitman's study of Brownian-bridge local times establishes the occupation-density framework and distributional identities for local time. Knight studies conditional moments of the area under the absolute value of a Brownian bridge given its local time at zero. Those are closely related objects, but the functional here is the integrated even-power energy \(I_q=\int_0^1B_t^{2q}\,dt\), and the claim is its explicit mixed covariance with local time. The proof above supplies that covariance directly from the bridge's conditional Gaussian variance.

## Limitations

The result is a covariance identity, not a joint distribution or a correlation coefficient. It does not establish negative association for all functionals of the bridge, nor does it cover noninteger powers, nonzero endpoint bridges, or other local-time normalizations without rescaling. The broader literature may contain indirect implications not identified in the inspected sources.

## References

1. Jim Pitman, “The distribution of local times of a Brownian bridge,” UC Berkeley Department of Statistics, Technical Report No. 539. The report landing page is dated November 1, 1998; the PDF title page is dated November 3, 1998. Landing page: https://statistics.berkeley.edu/tech-reports/539 ; full report: https://statistics.berkeley.edu/sites/default/files/tech-reports/539.pdf.
2. Frank B. Knight, “The moments of the area under reflected Brownian bridge conditional on its local time at zero,” *Journal of Applied Mathematics and Stochastic Analysis* 13 (2000), 99–124. DOI: https://doi.org/10.1155/S1048953300000137.
