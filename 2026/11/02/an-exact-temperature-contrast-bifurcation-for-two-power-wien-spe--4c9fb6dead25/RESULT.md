# Sharp opening of the bimodality window in a two-power Wien spectrum

## Finding

Consider the exact model
\[
S(x)=A x^3e^{-x}+B x^4e^{-x/r},\qquad x>0,\quad A,B>0,\quad r>1.
\]
Let \(\lambda_{\rm lo}(r)<\lambda_{\rm hi}(r)\) be the endpoints of the interval of \(B/A\) with two strict local maxima, when that interval exists. The result concerns the **width of this interval on a logarithmic amplitude scale** as it first opens. Let \(r_*=2.156640808732223\ldots\) be the unique root greater than one of \(28r^4-120r^3+168r^2-92r+15=0\). Put
\[
R_r(x)=\frac{r(x-3)}{x(4r-x)}e^{-(r-1)x/r},\quad H_r(x)=\partial_x\log R_r(x),\qquad 3<x<4r.
\]
Let \(x_*=5.639594827458655\ldots\) be the simultaneous zero of \(H_{r_*}\) and \(\partial_x H_{r_*}\) in that domain. Define
\[
k=\frac1{r_*^2}+\frac4{(4r_*-x_*)^2},\qquad
h_2=\frac2{(x_*-3)^3}-\frac2{x_*^3}+\frac2{(4r_*-x_*)^3}.
\]
For \(\delta=r-r_*\downarrow0\) from above, the opening law is
\[
\boxed{\log\frac{\lambda_{\rm hi}(r)}{\lambda_{\rm lo}(r)}
=K\delta^{3/2}+O(\delta^{5/2}),\qquad
K=\frac{4k}{3}\sqrt{\frac{2k}{h_2}}=2.451745065918099\ldots.}
\]
This gives the leading fractional amplitude-ratio range that supports two modes at a specified small excess temperature contrast. The log width is unchanged if amplitudes are replaced by normalized Gamma-mixture odds, which differ from \(B/A\) by a common scale factor at fixed \(r\).

## Assumptions and scope

This is a two-component, frequency-domain Wien model with emissivity powers zero and one. The variables can be read as \(x=h\nu/(k_{\rm B}T_{\rm c})\) and \(r=T_{\rm h}/T_{\rm c}\). The peaks are mathematical strict local maxima on the full positive half-line. The result does not imply observable two-peak resolution, nor apply without modification to a finite detector band or to exact Planck spectra.

## Proof

**Set-up: locate the critical point of the mode window.** The derivative is positive through \(x=3\) and negative from \(x=4r\) onward. On \((3,4r)\) it is
\[
S'(x)=A x^3e^{-x/r}(4-x/r)\bigl(B/A-R_r(x)\bigr).
\]
Hence the relevant turning levels are the values of \(R_r\) at the two zeros of
\[
H_r(x)=\frac1{x-3}-\frac1x+\frac1{4r-x}-\frac{r-1}{r}.
\]
Here \(\partial_x^2 H_r>0\) since \(2/(x-3)^3>2/x^3\), and \(H_r\to+\infty\) at both ends. Its unique minimizer is interior and depends smoothly on \(r\) by the implicit function theorem. The minimum decreases strictly: \(\partial_r H_r=-r^{-2}-4/(4r-x)^2<0\), and the domain increases with \(r\). The minimum is positive at \(r=1\), and negative for large \(r\) since \(H_r(5)\to-7/10\). Consequently it vanishes exactly once. To identify that parameter, multiply \(H_r\) by \(r x(x-3)(4r-x)\); the numerator is
\[
N_r(x)=3r(4r-x)+r x(x-3)-(r-1)x(x-3)(4r-x).
\]
The cubic discriminant is \(12r^2(4r-3)^2(28r^4-120r^3+168r^2-92r+15)\). At the critical parameter there is a double root of \(N_r\) at its interior zero \(x_*\), forcing the quartic to vanish. The quartic shifted by \(r=1+t\) is \(28t^4-8t^3-24t^2-4t-1\), with exactly one positive root by Descartes' rule and its endpoint signs. For \(r>r_*\), \(H_r\) has two simple zeros \(x_-<x_+\) with signs \(+,-,+\). As \(R_r\) runs from zero to infinity, it has a local maximum at \(x_-\) and local minimum at \(x_+\); the derivative factorization gives precisely two strict maxima between the levels \(\lambda_{\rm lo}=R_r(x_+)\), \(\lambda_{\rm hi}=R_r(x_-)\).

**Opening asymptotic.** The log width is \(-\int_{x_-}^{x_+}H_r(x)\,dx\). Set \(s=\sqrt\delta\) and write \(x=x_*+s z\). The function
\[
G(s,z)=s^{-2}H_{r_*+s^2}(x_*+s z)
\]
extends real analytically through \(s=0\) for bounded \(z\), because \(H_{r_*}(x_*)=\partial_x H_{r_*}(x_*)=0\) and all denominators are nonzero in a neighborhood. Its value there is \(G(0,z)=-k+h_2 z^2/2\), where \(k,h_2>0\). Let \(a=\sqrt{2k/h_2}\). The simple zeros at \(z=\pm a\) give analytic branches \(z_-(s),z_+(s)\) by the implicit function theorem. For small \(s>0\) these parameterize exactly the two turning points of \(R_r\), by strict convexity of \(H_r\).

After the substitution the width equals \(s^3J(s)\), where \(J(s)=-\int_{z_-(s)}^{z_+(s)}G(s,z)\,dz\). This function is analytic near zero, for example by mapping the interval affinely to \([0,1]\) and integrating its locally uniformly converging power series. Since \(G(-s,-z)=G(s,z)\), uniqueness gives \(z_\pm(-s)=-z_\mp(s)\), so \(J(-s)=J(s)\). Thus \(J(s)=J(0)+O(s^2)\), with
\[
J(0)=\int_{-a}^a(k-h_2z^2/2)\,dz=\frac{4ka}{3}.
\]
This proves the leading coefficient and the stated remainder.

## Relationship to prior work and limitations

Normalizing \(S\) gives a mixture of Gamma densities of shapes \(4,5\) and rates \(1,1/r\), with second-to-first weight odds \(4r^5 B/A\). The mode-count criterion and the boundary levels are a specialization of general Gamma-mixture and two-density modality criteria, not separate novelty claims here. The critical quartic is useful for specifying the point about which the expansion is taken. The contribution is the local amplitude-window asymptotic, including its coefficient and the absence of a term of order \(\delta^2\). The mechanism is the standard coalescence of two turning points; no novel general bifurcation mechanism is claimed. The cited mode criteria supply the endpoints, but do not give the evaluated near-critical width in their inspected statements. First-publication priority for the asymptotic is not established.

## References

1. S. E. Ahmed, M. N. Goria and A. Hussein, “Gamma Mixture: Bimodality, Inflexions and L-Moments,” *Communications in Statistics — Theory and Methods* **37** (2008), 1147–1161, §2. https://doi.org/10.1080/03610920701713286
2. Š. Došlá, “Conditions for Bimodality and Multimodality of a Mixture of Two Unimodal Densities,” *Kybernetika* **45** (2009), 279–292, Theorems 1–2 and §3.5. https://www.kybernetika.cz/content/2009/2/279
3. G. M. Kennedy and M. C. Wyatt, “Do Two Temperature Debris Disks Have Multiple Belts?”, arXiv:1408.4116, §§3–5, for modified thermal spectra. https://arxiv.org/abs/1408.4116
