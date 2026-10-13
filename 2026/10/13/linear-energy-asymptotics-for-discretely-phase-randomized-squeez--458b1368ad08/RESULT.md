# Linear-energy asymptotics for discretely phase-randomized squeezed sensing
## Finding
Consider the phase-estimation channel with a uniformly random discrete phase \(2\pi k/M\) and a small target phase, as in Conlon et al., arXiv:2610.03657v1. Fix \(c\in(0,1)\), let \(M\to\infty\) through even integers, and impose the per-use mean photon budget
\[
\bar n=cM.
\]
For the squeezed vacuum, let \(p_j^{\mathrm{{SV}}}\) be its photon-number law and let the source's sector-pair visibility be
\[
B_{{M,\bar n}}=4\sum_{{\substack{{0\le j<M\\j\;\mathrm{{even}}}}}}
\frac{{p_j^{{\mathrm{{SV}}}}p_{{j+M}}^{{\mathrm{{SV}}}}}}{{p_j^{{\mathrm{{SV}}}}+p_{{j+M}}^{{\mathrm{{SV}}}}}}.
\]
Then
\[
B_{{M,cM}}\longrightarrow B(c)
=2\sqrt{{\frac{{2}}{{\pi c}}}}
\int_0^1
\frac{{dx}}{{\sqrt{{x}}e^{{x/(2c)}}+\sqrt{{x+1}}e^{{(x+1)/(2c)}}}}>0.
\]

Fix task constants \(0<a<\pi/2\), \(0<b<a/2\), and \(0<\zeta<1/2\) in the finite-sample estimation problem of the source. Its squeezed-vacuum protocol therefore satisfies
\[
\nu^*_{{\mathrm{{SV}}}}(M,cM;a,b,\zeta)=O_{{a,b,\zeta,c}}(1).
\]
For the source's specified classical optical family, including adaptive classical measure-and-prepare protocols under the same per-round energy constraint,
\[
\nu^*_{{\mathrm{{cl}}}}(M,cM;a,b,\zeta)
\ge C_{{b,\zeta,c}}\sqrt{{M}}e^{{M I(c)}}(1+o(1)),
\]
where
\[
I(c)=c-1-\ln c>0,
\qquad
C_{{b,\zeta,c}}=
\frac{{(1-2\zeta)^2}}{{16b^2}}(1-c)\sqrt{{2\pi}}.
\]
Thus every fixed \(c\in(0,1)\) gives a constant-versus-exponential sample-complexity separation at linear photon budget.

## Assumptions and scope
The result uses the exact model and task of arXiv:2610.03657v1. The integer \(M\) is even and tends to infinity. The mean photon number is fixed to \(\bar n=cM\) with a constant \(c\in(0,1)\). The accuracy window and confidence parameters \(a,b,\zeta\) are fixed independently of \(M\) and satisfy the source's conditions. The classical conclusion applies to the source's classical family and its adaptive measure-and-prepare extension, not to unrestricted nonclassical probes.

The statement does not assert that \(c=1\) is a sharp physical threshold. The source's coherent-state certificate used for the lower bound requires \(\bar n<M^2/(M+1)\), which holds eventually for fixed \(c<1\).

## Proof
For even photon number \(j=2k\), the squeezed-vacuum law can be written
\[
p_j^{{\mathrm{{SV}}}}
=\frac{{1}}{{\sqrt{{1+\bar n}}}}
\frac{{\binom{{2k}}{{k}}}}{{4^k}}
q^k,
\qquad
q=\frac{{\bar n}}{{1+\bar n}},
\]
and it vanishes for odd \(j\). Put \(\bar n=cM\), \(j=xM\), and keep \(x\) in a compact subinterval of \((0,\infty)\). The central-binomial asymptotic and
\[
\log q=-\frac{{1}}{{cM}}+O(M^{{-2}})
\]
give, uniformly on such compact sets,
\[
Mp_{{xM}}^{{\mathrm{{SV}}}}
\longrightarrow
g_c(x)
=\sqrt{{\frac{{2}}{{\pi c x}}}}e^{{-x/(2c)}}.
\]
Hence, uniformly for \(x\in[\varepsilon,1]\),
\[
M\frac{{p_j^{{\mathrm{{SV}}}}p_{{j+M}}^{{\mathrm{{SV}}}}}}{{p_j^{{\mathrm{{SV}}}}+p_{{j+M}}^{{\mathrm{{SV}}}}}}
\longrightarrow
h_c(x)=\frac{{g_c(x)g_c(x+1)}}{{g_c(x)+g_c(x+1)}}.
\]
The even lattice has spacing \(2/M\), so the Riemann sum on \([\varepsilon,1]\) tends to
\[
2\int_\varepsilon^1 h_c(x)\,dx.
\]
For the omitted endpoint \(0\le j<\varepsilon M\), each harmonic-mean term is at most \(p_{{j+M}}^{{\mathrm{{SV}}}}\). The same local asymptotic on the interval \([1,1+\varepsilon]\) makes the total endpoint contribution \(O_c(\varepsilon)\). Sending \(\varepsilon\downarrow0\) proves
\[
B_{{M,cM}}\to 2\int_0^1 h_c(x)\,dx.
\]
Since
\[
h_c(x)=
\sqrt{{\frac{{2}}{{\pi c}}}}
\left(\sqrt{{x}}e^{{x/(2c)}}+\sqrt{{x+1}}e^{{(x+1)/(2c)}}\right)^{{-1}},
\]
this is the displayed positive integral \(B(c)\).

The source's finite-sample theorem bounds its explicit squeezed-vacuum protocol by a constant multiple of \(B_{{M,\bar n}}^{{-1}}\), with all other factors depending only on \(a,b,\zeta\). Since \(B_{{M,cM}}\to B(c)>0\), the squeezed sample complexity is bounded independently of \(M\).

For the classical family, the same theorem gives
\[
\nu^*_{{\mathrm{{cl}}}}
\ge
\frac{{(1-2\zeta)^2}}{{16b^2}}
(1-\kappa_{{M,\bar n}})
\frac{{e^{{\bar n}}M!}}{{\bar n^M}},
\qquad
\kappa_{{M,\bar n}}=\frac{{\bar n(M+1)}}{{M^2}}.
\]
With \(\bar n=cM\),
\[
1-\kappa_{{M,cM}}=1-c-\frac{{c}}{{M}},
\]
and Stirling's formula yields
\[
\frac{{e^{{cM}}M!}}{{(cM)^M}}
=\sqrt{{2\pi M}}
\exp\left(M(c-1-\ln c)\right)(1+o(1)).
\]
The strict inequality \(I(c)=c-1-\ln c>0\) for \(0<c<1\) follows from \(\ln c<c-1\). Combining these formulas gives the claimed classical lower bound.

## Verification
A standalone checker evaluates the exact squeezed-vacuum sector sum using log-gamma arithmetic for several fixed values of \(c\) and increasing even \(M\), compares it with the integral \(B(c)\), and checks the normalized classical exponent against \(I(c)\). These finite calculations corroborate the formulas but are not used to prove the limiting statements.

## Relationship to prior work
Conlon et al., arXiv:2610.03657v1, derive the exact sector visibility, the general finite-sample bounds, and then specialize their principal asymptotic sample-complexity corollary to the sublinear budget \(\bar n=M/\log M\). They also show that sublinear coherent-state energy cannot maintain nonvanishing QFI and hence that at least linear energy is necessary on the classical side. The present result resolves a different regime left between those statements: every fixed subcritical linear coefficient \(0<c<1\). It evaluates the sector visibility asymptotically in that regime and obtains a constant squeezed sample cost together with an explicit classical large-deviation exponent \(I(c)\).

Earlier discrete-phase-randomization work by Cao, Zhang, Lo, and Ma, arXiv:1410.3217, studies coherent-state sources for quantum-key-distribution security and convergence toward continuous phase randomization. It does not study the phase-estimation task, squeezed-vacuum sector visibility, or the sample-complexity separation above.

## Limitations
The conclusion concerns the noiseless discrete-twirl model and the probe families of the source. It does not establish optimality of the squeezed-vacuum constant sample count among all quantum probes. It does not establish a converse for squeezed probes. It does not determine what happens at \(c=1\) or for \(c>1\), and it must not be read as proving a sharp energy phase transition there. The classical exponential lower bound is a consequence of the source's certificate in its stated validity range.

## References
1. L. O. Conlon et al., “Super-Exponential Advantage of Squeezed Light in Phase Estimation under Discrete Phase Randomisation,” arXiv:2610.03657v1 (2026).
2. Z. Cao, Z. Zhang, H.-K. Lo, and X. Ma, “Discrete-phase-randomized coherent state source and its application in quantum key distribution,” New Journal of Physics 17, 053014 (2015), arXiv:1410.3217.
