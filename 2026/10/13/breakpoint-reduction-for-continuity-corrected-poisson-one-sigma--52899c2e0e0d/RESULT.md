# Breakpoint reduction for continuity-corrected Poisson one-sigma concentration
## Finding
Let \(X_\lambda\sim\operatorname{Pois}(\lambda)\) for \(\lambda>0\), and define the continuity-corrected one-standard-deviation mass
\[
J(\lambda)=\Pr\!\left\{\left\lfloor\lambda-\sqrt\lambda\right\rfloor\le X_\lambda\le\left\lceil\lambda+\sqrt\lambda\right\rceil\right\}.
\]
For integers \(m\ge0\) and \(n\ge1\), set
\[
A_m=\left(\frac{1+\sqrt{4m+1}}2\right)^2,
\qquad
B_n=\left(\frac{\sqrt{4n+1}-1}2\right)^2.
\]
These are exactly the positive parameters at which the lower or upper rounded endpoint changes. On every connected component of
\[
(0,\infty)\setminus\bigl(\{A_m:m\ge0\}\cup\{B_n:n\ge1\}\bigr),
\]
the function \(J\) has no local minimum. Hence, writing \(\Phi\) for the standard-normal distribution function,
\[
\inf_{\lambda>0}J(\lambda)
=
\min\!\left\{2\Phi(1)-1,
\inf_{m\ge0}J(A_m),
\inf_{n\ge1}J(B_n)\right\}.
\]
In addition, every integer square \(s^2\), \(s\ge2\), is a strict local minimum of \(J\), and
\[
J(s^2)\longrightarrow 2\Phi(1)-1.
\]
Thus the continuum comparison reduces exactly to two explicit discrete breakpoint sequences. In particular, no uniform lower constant strictly larger than \(2\Phi(1)-1\) is possible.

## Assumptions and scope
The result concerns the Poisson family with parameter \(\lambda>0\) and the specific continuity correction using a floor at the lower one-standard-deviation endpoint and a ceiling at the upper endpoint. No assertion is made here that every breakpoint value exceeds \(2\Phi(1)-1\); rather, the result gives an exact reduction of that remaining inequality to discrete parameters.

For a fixed parameter, put
\[
\ell(\lambda)=\max\!\left\{0,\left\lfloor\lambda-\sqrt\lambda\right\rfloor\right\},
\qquad
u(\lambda)=\left\lceil\lambda+\sqrt\lambda\right\rceil.
\]
The maximum with zero only removes impossible negative Poisson indices.

## Proof
Fix a connected component on which \(\ell(\lambda)=\ell\) and \(\nu(\lambda)=u\) are constant. With
\[
p_k(\lambda)=e^{-\lambda}\frac{\lambda^k}{k!},\qquad k\ge0,
\]
we have
\[
J(\lambda)=\sum_{k=\ell}^{u}p_k(\lambda).
\]
Termwise differentiation and the identity
\[
p_k'(\lambda)=p_{k-1}(\lambda)-p_k(\lambda)
\]
with the convention \(p_{-1}(\lambda)=0\) give the telescoping formula
\[
J'(\lambda)=p_{\ell-1}(\lambda)-p_u(\lambda).
\]
If \(\ell=0\), then \(J'(\lambda)=-p_u(\lambda)<0\), so the branch is strictly decreasing. If \(\ell\ge1\), then
\[
\frac{p_{\ell-1}(\lambda)}{p_u(\lambda)}
=
\frac{u!}{(\ell-1)!}\,\lambda^{-(u-\ell+1)},
\]
which is strictly decreasing in \(\lambda\). Therefore \(J'\) changes sign at most once, and any sign change is from positive to negative. Equivalently, the only possible stationary parameter is
\[
\lambda_*=\left(\frac{u!}{(\ell-1)!}\right)^{1/(u-\ell+1)},
\]
and if it lies in the branch it is a strict maximum. Thus no open rounding cell contains a local minimum.

The lower endpoint changes exactly when \(\lambda-\sqrt\lambda=m\) for an integer \(m\ge0\). Writing \(y=\sqrt\lambda\), the equation \(y^2-y=m\) gives \(\lambda=A_m\). Likewise the upper endpoint changes exactly when \(\lambda+\sqrt\lambda=n\), giving \(\lambda=B_n\). Since every branch has its infimum at a boundary, the infimum over all finite parameters is the infimum over these breakpoint values together with the two limiting ends. As \(\lambda\downarrow0\), \(J(\lambda)\to1\). As \(\lambda\to\infty\), the standardized Poisson central limit theorem gives
\[
J(\lambda)\to 2\Phi(1)-1
\]
along any sequence for which the normalized rounded endpoints converge to \(-1\) and \(1\); in particular this holds along integer squares. This yields the displayed infimum reduction.

For an integer \(s\ge2\), the point \(\lambda=s^2\) is simultaneously
\[
A_{s(s-1)}=B_{s(s+1)}=s^2.
\]
At the point itself, the event is
\[
s^2-s\le X_{s^2}\le s^2+s.
\]
Approaching from the left keeps the upper endpoint \(s^2+s\) but includes the additional lower atom \(s^2-s-1\), while approaching from the right keeps the lower endpoint \(s^2-s\) but includes the additional upper atom \(s^2+s+1\). Hence
\[
\lim_{\lambda\uparrow s^2}J(\lambda)
=J(s^2)+p_{s^2-s-1}(s^2)>J(s^2),
\]
and
\[
\lim_{\lambda\downarrow s^2,\,\lambda>s^2}J(\lambda)
=J(s^2)+p_{s^2+s+1}(s^2)>J(s^2).
\]
Thus \(s^2\) is a strict local minimum. Finally,
\[
J(s^2)=\Pr\!\left\{-1\le\frac{X_{s^2}-s^2}{s}\le1\right\}
\longrightarrow 2\Phi(1)-1
\]
by the Poisson central limit theorem.

## Verification
The proof is analytic and covers every \(\lambda>0\). The accompanying checker verifies the telescoping derivative formula by finite differences away from rounding breakpoints and confirms the strict-square-minimum behavior for \(2\le s\le100\). Those computations are regression checks only; they are not used to infer the universal statements.

The breakpoint equations were also solved symbolically and substituted back into \(\lambda\mp\sqrt\lambda\). The square coincidence identities \(A_{s(s-1)}=B_{s(s+1)}=s^2\) follow directly.

## Relationship to prior work
Sun, Hu, and Sun introduced this continuity-corrected Poisson one-standard-deviation quantity in their study of variation comparison and reported numerical evidence for the discrete comparison; the paper states that its discrete conclusions are numerical rather than a proof of the full corrected inequality. The present result supplies an exact structural reduction of the continuum parameter problem and identifies all possible locations at which a minimum can occur.

Zhang, Hu, and Sun later determined exact infima for the uncorrected Poisson one-standard-deviation probabilities. Their Poisson section uses piecewise analysis as rounded uncorrected endpoints change, but it studies a different event and does not state the continuity-corrected breakpoint reduction above. In particular, the uncorrected exact infimum does not imply the behavior of \(J\), because the added boundary atoms change at different one-sided breakpoints.

The normal benchmark should be understood as the exact value \(2\Phi(1)-1\), not a rounded decimal. Since \(J(s^2)\) converges to that value, any strictly larger fixed decimal threshold eventually fails regardless of the unresolved sign of the exact-normal comparison at finite breakpoints.

## Limitations
This result does not prove that \(J(\lambda)>2\Phi(1)-1\) for every finite \(\lambda\). It proves that this question is exactly equivalent to checking the two explicit breakpoint sequences, with the normal mass as the only limiting competitor. No monotonicity of the full breakpoint sequences is claimed.

The originality search did not identify an earlier statement of this exact reduction, but elementary Poisson interval derivatives are classical, so an equivalent lemma could exist under different terminology. The result should therefore be read as a precise structural reduction tied to this continuity-corrected problem, not as a claim that the differentiation identity itself is new.

## References
1. P. Sun, Z.-C. Hu, and W. Sun, “Variation comparison between infinitely divisible distributions and the normal distribution,” arXiv:2304.11459v1, 2023; later published in *Statistical Papers*.
2. J. Zhang, Z.-C. Hu, and W. Sun, “On the measure concentration of infinitely divisible distributions,” arXiv:2310.03471v1, 2023; later published in *Acta Mathematica Scientia*.
