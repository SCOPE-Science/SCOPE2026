# Sharp asymmetric bispectral identifiability and minimal phase sampling

## Finding

Let \(n,r,s\) be integers with \(r>s\geq1\), \(r\geq3\), and \(n>r+s\). On the cyclic group \(G=\mathbb Z/n\mathbb Z\), put
\[
S_{r,s}=\{-s,\ldots,-1\}\cup\{1,\ldots,r\}\pmod n,
\qquad d=r+s.
\]
For every complex signal whose Fourier transform is nonzero **exactly** on \(S_{r,s}\), the complete fiber of the joint power spectrum and bispectrum is
\[
\boxed{\quad\widehat g(k)=t^k\widehat f(k)\ (k\in S_{r,s}),\qquad
 t\in\begin{cases}\mathbb T,&2r+s<n,\\
\{z\in\mathbb T:z^n=1\},&2r+s\ge n.
\end{cases}\quad}
\]
Outside \(S_{r,s}\), both transforms vanish. Here \(k\) in the exponent is the indicated signed integer representative. Hence bispectral recovery up to a cyclic translation holds for every such signal **if and only if** \(2r+s\ge n\). The below-threshold fiber is a circle, not merely finitely ambiguous; above threshold it is precisely the \(n\) cyclic translates.

There are explicitly specified, sharp-size bispectral measurement packets: \(d-1\) entries suffice to determine the full circle-valued fiber in the first regime, while \(d\) entries suffice for translation-level uniqueness in the second. No smaller collection of individual bispectral entries can have these respective identifying properties, given the power spectrum.

The number of active Fourier modes by itself does not determine identifiability. At \(n=11\), \((r,s)=(4,2)\) has a continuous fiber although \((r,s)=(5,1)\), with the same six active modes, has only eleven cyclic shifts.

## Assumptions and scope

Define the unnormalized Fourier transform by \(\widehat f(k)=\sum_{x\in G}f(x)e^{-2\pi ikx/n}\). We observe the power spectrum \(P_f(k)=|\widehat f(k)|^2\) and the bispectrum
\[
B_f(j,k)=\widehat f(j)\widehat f(k)\overline{\widehat f(j+k)},
\]
with all indices reduced modulo \(n\). A bispectral *sample* means one ordered pair \((j,k)\) and its complex value, under the standing assumption that the power spectrum is already known. The arbitrary nonzero complex Fourier magnitudes and phases on the prescribed support are allowed; no reality or conjugate symmetry is assumed. Equality of data is exact and noiseless. No claim is made concerning missing nonzero coefficients, unknown Fourier support, or stability in noise.

## Proof

**1. Phase relations.** Suppose \(P_g=P_f\) and \(B_g=B_f\). Their common nonzero Fourier support is \(S_{r,s}\). For each supported signed frequency define \(u_k=\widehat g(k)/\widehat f(k)\in\mathbb T\). Any pair \(j,k\in S_{r,s}\) with \(j+k\pmod n\in S_{r,s}\) imposes precisely
\[
u_ju_k=u_{j+k\pmod n}.
\]
All other bispectral entries vanish for both signals and impose no relation. Conversely, these equalities plus \(P_g=P_f\) are sufficient.

**2. The connected phase chain.** For \(2\le k\le r\), the pairs \((1,k-1)\) give \(u_k=u_1u_{k-1}\), whence \(u_k=u_1^k\) on the positive block. For \(2\le j\le s\), the pairs \((-1,-(j-1))\) give \(u_{-j}=u_{-1}^{j}\); when \(s=1\), this is vacuous. Crucially \((2,-1)\) has sum \(1\) (the hypothesis \(r\ge3\) ensures all needed frequencies occur), so
\[
u_2u_{-1}=u_1 \quad\Longrightarrow\quad u_{-1}=u_1^{-1}.
\]
Thus all ratios have the unique form \(u_k=t^k\) with \(t=u_1\in\mathbb T\), using the signed integer exponents on both blocks. The \((r-1)+(s-1)+1=d-1\) named pairs already force this form.

**3. Exact transition.** Every remaining permitted bispectral triple has signed indices \(j,k,\ell\in[-s,r]\setminus\{0\}\), with \(\ell\equiv j+k\pmod n\). Consequently \(j+k-\ell\) is a multiple of \(n\), and lies between \(-(2s+r)\) and \(2r+s\). Because \(r>s\), the condition \(2r+s<n\) excludes all nonzero multiples of \(n\). In that regime every \(t\in\mathbb T\) satisfies every relation.

If \(2r+s\ge n\), take
\[
a=r,\qquad b=n-s-r.
\]
The constraints \(n>r+s\) and \(2r+s\ge n\) guarantee \(1\le b\le r\). Thus \(a,b\) lie in the positive block and \(a+b=n-s\equiv-s\pmod n\). The corresponding relation is \(t^{n-s}=t^{-s}\), forcing \(t^n=1\). Conversely, whenever \(t^n=1\), **every** modular addition relation is satisfied. This proves both exhaustive fibers. Multiplication of \(\widehat f(k)\) by \(e^{-2\pi ikh/n}\) is the transform of a cyclic translation by \(h\in G\); since frequency \(1\) belongs to the support, these \(n\) translates are distinct.

**4. Exact sample minimum.** Record the phase of \(B_f(1,k-1)\) for all \(2\le k\le r\), of \(B_f(-1,-(j-1))\) for \(2\le j\le s\), and of \(B_f(2,-1)\). These are \(d-1\) individual entries. Their phase equalities impose exactly the recursions in step 2 and leave a one-dimensional torus of possible phase multipliers. If \(2r+s\ge n\), record one further entry \(B_f(r,n-s-r)\). Step 3 shows that its phase equality imposes precisely \(t^n=1\), so these \(d\) entries give exactly the finite shift fiber.

For minimality, the unknown phases with nonzero Fourier magnitudes fixed comprise a real \(d\)-torus. Each individual nonzero bispectral sample, after dividing by its known modulus, is a single circle-valued character of this torus, hence can lower the identity component of its kernel in dimension by at most one. Therefore fewer than \(d-1\) such samples cannot leave exactly the one-dimensional fiber below threshold; fewer than \(d\) cannot leave a finite fiber above threshold. Zero bispectral entries impose no restriction because the support is known. The constructions attain both lower bounds.

## Verification

The standalone checker `bispectrum_asym_check.py` enumerates all supported modular addition relations and computes exact integer Smith normal forms for both the complete relation matrix and the displayed minimal packet. It tests every triple \((n,r,s)\) with \(5\le n\le28\), \(3\le r<n\), \(1\le s<r\), and \(r+s<n\). There are 1,522 parameter cases (435 continuous and 1,087 discrete), totaling 310,585 allowed ordered bispectral relations. Their nonzero Smith invariants are respectively \((1,\ldots,1)\) of length \(d-1\), and \((1,\ldots,1,n)\) of length \(d\). The proof above is independent of this finite computation and covers all admitted integers.

Run with Python 3 and SymPy: `python3 bispectrum_asym_check.py`.

## Relationship to prior work

Bispectral phase recursion, translation invariance, and possible phase ambiguities are classical. Giannakis (1989), Yellott–Iverson (1992), and Kakarala (2009) provide foundational approaches. Kakarala's group theorem for fully nonvanishing Fourier transforms and its spectral-subgroup variant do not determine fibers for a zero-mean set consisting of two unequal frequency blocks: the support here omits the trivial character and is not subgroup-closed. Bendory, Boumal, Ma, Zhao, and Singer (2017), Proposition II.1, prove a related sufficiency threshold for **real signals with equal positive/negative bandwidth**, assuming the associated conjugate symmetry. Their result is not asserted as new here and does not imply the present **complex unequal-block, sharp necessary-and-sufficient** statement or the minimum packet count. Pinilla, Mishra, and Sadler (2021) study a bandlimited sample bound under a different nonzero-central-frequency setup, rather than this exact zero-mean fiber classification.

The new contribution assessed here is the imbalance-sensitive sharp transition, exact continuous-versus-finite fiber classification, and information-theoretically minimal phase-only bispectral packet. A broad spectral-gap reconstruction method from earlier signal-processing literature could admit an equivalent formulation; priority beyond the sources compared is not certified.

## Limitations

Only exact power plus bispectrum, fully known support, and nonzero coefficients throughout the prescribed support are addressed. The sampling-optimality statement counts individual bispectral complex values **conditional on already knowing the power spectrum**, not raw time-domain observations, noise samples, or total power-plus-bispectrum data. The result does not provide stability or a noise-robust algorithm, and does not classify supports with multiple internal gaps. Exhaustive historical priority verification is not established.

## References

1. G. B. Giannakis, *Signal reconstruction from multiple correlations: frequency- and time-domain approaches*, J. Opt. Soc. Am. A **6** (1989), 682–697, doi:10.1364/JOSAA.6.000682.
2. J. I. Yellott, Jr. and G. J. Iverson, *Uniqueness properties of higher-order autocorrelation functions*, J. Opt. Soc. Am. A **9** (1992), 388–404, doi:10.1364/JOSAA.9.000388.
3. R. Kakarala, *The bispectrum as a source of phase-sensitive invariants for Fourier descriptors: a group-theoretic approach*, arXiv:0902.0196, first public version 2009-02-02.
4. T. Bendory, N. Boumal, C. Ma, Z. Zhao, and A. Singer, *Bispectrum inversion with application to multireference alignment*, arXiv:1705.00641, Proposition II.1.
5. S. Pinilla, K. V. Mishra, and B. M. Sadler, *Unique bispectrum inversion for signals with finite spectral/temporal support*, arXiv:2111.06479, Proposition 1.
