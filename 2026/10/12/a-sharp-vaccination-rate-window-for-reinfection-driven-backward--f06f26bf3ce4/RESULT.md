# A sharp vaccination-rate window for reinfection-driven backward bifurcation
## Finding
For the SEIRV model of Khan, Wang, Liu and Xiong, keep \(\Lambda,\mu,\gamma,\delta,\theta\) positive and fix an imperfect vaccine with \(0<\sigma<1\). Their Theorem 5.2 uses an exact reinfection threshold \(\beta_2^*\) to determine the local bifurcation direction at \(R_0=1\): the branch is backward when \(\beta_2>\beta_2^*\) and forward when \(\beta_2<\beta_2^*\).

Define
\[
B_0=\frac{\mu(\gamma+\mu)^2(\delta+\mu+\theta)^2}{\gamma^2\delta\Lambda},\qquad x=\frac{\alpha\sigma}{\mu}.
\]
The source threshold has the exact form
\[
\beta_2^*(\alpha)=B_0\left(1-\frac{(1-\sigma)x}{(1+x)^2}\right).
\]
It follows that \(\beta_2^*(\alpha)\) has a unique minimum at \(\alpha=\mu/\sigma\):
\[
\min_{\alpha>0}\beta_2^*(\alpha)=B_0\frac{3+\sigma}{4}.
\]
It is strictly decreasing before that point, strictly increasing after it, and tends to \(B_0\) at both rate extremes \(\alpha\downarrow0\) and \(\alpha\to\infty\).

This gives a complete sharp classification at fixed reinfection strength. Put \(r=\beta_2/B_0\), \(c=1-\sigma\), and, when \(r<1\), \(q=1-r\). Then:

1. If \(r\le(3+\sigma)/4\), no \(\alpha>0\) satisfies the strict backward-bifurcation inequality.
2. If \((3+\sigma)/4<r<1\), the backward regime is exactly the open interval \(\alpha_-<\alpha<\alpha_+\), with
\[
x_\pm=\frac{c-2q\pm\sqrt{c(c-4q)}}{2q},\qquad \alpha_\pm=\frac{\mu}{\sigma}x_\pm,
\]
and the endpoints obey
\[
x_-x_+=1,\qquad \alpha_-\alpha_+=\left(\frac{\mu}{\sigma}\right)^2.
\]
3. If \(r\ge1\), the backward inequality holds for every \(\alpha>0\). At \(r=1\) this is strict for every finite positive \(\alpha\), because \(0<\sigma<1\) makes the bracketed threshold factor strictly less than one.

Thus the model has an exact bounded vaccination-rate window in the intermediate case. The window is reciprocal around the distinguished rate \(\mu/\sigma\) in the dimensionless coordinate \(x\).

## Assumptions and scope
The statement concerns the exact local bifurcation threshold printed for the source SEIRV model. All demographic and progression parameters appearing in \(B_0\) are fixed and positive, \(\alpha>0\), and \(0<\sigma<1\). The source interprets \(\sigma\) as residual susceptibility after vaccination, so smaller \(\sigma\) means a more effective vaccine. The source's criterion \(\beta_2>\beta_2^*\) is used exactly as proved there; the present result classifies how that criterion changes when only the vaccination rate \(\alpha\) varies.

The statement is about the direction of the local bifurcation at \(R_0=1\), not about the global size of the bistable region or the value of the lower critical threshold \(R_0^C\). It does not claim that increasing \(\alpha\) worsens disease burden: in the same source model, \(R_0\) decreases monotonically with \(\alpha\) for \(0<\sigma<1\). The result instead separates that familiar effect from the nonmonotone dependence of the reinfection strength required to create a backward branch.

## Proof
The source gives
\[
\beta_2^*=\frac{\mu(\gamma+\mu)^2(\delta+\mu+\theta)^2\bigl(\mu^2+\alpha^2\sigma^2+\alpha\mu\sigma(1+\sigma)\bigr)}{\gamma^2\delta\Lambda(\mu+\alpha\sigma)^2}.
\]
Factor out \(B_0\) and set \(x=\alpha\sigma/\mu\). The remaining dimensionless ratio is
\[
\frac{1+x^2+x(1+\sigma)}{(1+x)^2}
=1-\frac{(1-\sigma)x}{(1+x)^2}.
\]
Hence
\[
\frac{1}{B_0}\frac{d\beta_2^*}{dx}
=\frac{(1-\sigma)(x-1)}{(1+x)^3}.
\]
Because \(0<\sigma<1\), this derivative is negative for \(0<x<1\), zero only at \(x=1\), and positive for \(x>1\). The unique minimum therefore occurs at \(x=1\), equivalently \(\alpha=\mu/\sigma\), and substitution gives
\[
\frac{\beta_2^*}{B_0}=1-\frac{1-\sigma}{4}=\frac{3+\sigma}{4}.
\]
The limits at \(x\downarrow0\) and \(x\to\infty\) are both one.

For the fixed-\(\beta_2\) classification, write \(f(x)=\beta_2^*(\alpha)/B_0\). The strict backward-bifurcation condition is \(r>f(x)\). Since \(f\) has range \([(3+\sigma)/4,1)\) on \(x>0\), the first and third cases follow immediately.

For \((3+\sigma)/4<r<1\), set \(q=1-r>0\) and \(c=1-\sigma>0\). The boundary equation \(r=f(x)\) is
\[
q(1+x)^2=cx,
\]
or
\[
qx^2+(2q-c)x+q=0.
\]
Its discriminant is \(c(c-4q)>0\) exactly because \(r>(3+\sigma)/4\). Thus its two positive roots are
\[
x_\pm=\frac{c-2q\pm\sqrt{c(c-4q)}}{2q}.
\]
Their product is one by Vieta's formula. Since \(f(1)=(3+\sigma)/4<r\) and \(f(x)\to1>r\) at both extremes, the strict inequality \(r>f(x)\) holds exactly between the roots. Multiplying the roots by \(\mu/\sigma\) proves the stated interval and endpoint product.

## Verification
The proof is symbolic and exact. The accompanying `verify.py` checks the algebraic normalization with rational arithmetic and checks the nontrivial interval formula on the exact example \(\sigma=1/2\), \(r=8/9\), for which \(x_-=1/2\), \(x_+=2\), and \(x_-x_+=1\). These finite checks are reproducibility aids, not substitutes for the general derivative and quadratic proof above.

The source equation was independently reconstructed from its Appendix B notation \(P,Q,\beta_1^*,\xi\) and from the displayed closed form for \(\beta_2^*\). Both routes give the same threshold used here.

## Relationship to prior work
Khan et al. derive \(\beta_2^*\) and prove that it determines the local bifurcation direction. They also explicitly show that the vaccinated-population reproduction number decreases with \(\alpha\) for a partially effective vaccine. In the inspected full text, however, the dependence of \(\beta_2^*\) on \(\alpha\) is not classified: no unique minimizer, exact minimum, bounded rate window, or reciprocal endpoint law is stated.

Safan and Rihan study backward bifurcation in a different imperfect-vaccination SIS model and derive a critical vaccination rate for eradication. Gomes, White and Medley develop reinfection-threshold ideas for partial immunity and vaccination, while Song formalizes a basic reinfection number as a bifurcation diagnostic. These works motivate the interaction between vaccination and reinfection but do not imply the exact rate dependence above for this SEIRV threshold. Gutierrez and Gog's 2026 SIRI analysis treats vaccination as a pre-epidemic vaccinated fraction and studies final-size/reinfection-threshold structure, rather than a continuous vaccination-flow rate controlling the local backward-bifurcation threshold.

## Limitations
The result is conditional on the source model and on holding \(\Lambda,\mu,\gamma,\delta,\theta,\sigma\) fixed while varying \(\alpha\). It does not assert that the actual endemic prevalence, basin size, or lower critical threshold \(R_0^C\) is nonmonotone in \(\alpha\). It also does not extend automatically to waning-vaccine models, age structure, time-dependent vaccination controls, or models in which reinfection and breakthrough susceptibility share different functional forms.

At the excluded endpoint \(\sigma=1\), the threshold becomes constant in \(\alpha\); the limiting case \(\sigma=0\) also requires separate interpretation because \(x=\alpha\sigma/\mu\) ceases to parametrize the rate. The strict boundaries \(\beta_2=\beta_2^*\) are degenerate bifurcation thresholds and are deliberately not counted as backward.

## References
1. Khan A, Wang L, Liu J, Xiong M. Dynamics of an SEIRV endemic model: effects of reinfection. *Journal of Biological Dynamics*. 2026;20(1):2713881. doi:10.1080/17513758.2026.2713881.
2. Song B. Basic reinfection number and backward bifurcation. *Mathematical Biosciences and Engineering*. 2021;18(6):8064-8083. doi:10.3934/mbe.2021400.
3. Safan M, Rihan FA. Mathematical analysis of an SIS model with imperfect vaccination and backward bifurcation. *Mathematics and Computers in Simulation*. 2014;96:195-206. doi:10.1016/j.matcom.2011.07.007.
4. Gomes MGM, White LJ, Medley GF. Infection, reinfection, and vaccination under suboptimal immune protection: epidemiological perspectives. *Journal of Theoretical Biology*. 2004;228(4):539-549. doi:10.1016/j.jtbi.2004.02.015.
5. Gutierrez MA, Gog JR. Final-Size Solutions for SIRI Models with Vaccination. *Bulletin of Mathematical Biology*. 2026;88:64. doi:10.1007/s11538-026-01610-w.
