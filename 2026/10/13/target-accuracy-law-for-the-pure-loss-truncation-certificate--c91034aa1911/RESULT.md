# Target-accuracy law for the pure-loss truncation certificate
## Finding
Fix \(\bar n>0\), put \(r=\bar n/(\bar n+1)\), and set
\[
\lambda=\frac12\ln\frac{\bar n+1}{\bar n}.
\]
The finite-dimensional pure-loss construction of Mandal, Piveteau, Pfister, and Renes controls its coherent-information loss by
\[
B_{\bar n}(d)=4r^{{d/2}}g(\bar n r^{{-d/2}})+2h_2(r^{{d/2}}),
\]
where \(g(x)=(x+1)\log_2(x+1)-x\log_2x\) and \(h_2\) is binary entropy. This certificate has the sharp large-cutoff expansion
\[
B_{\bar n}(d)=\frac{e^{{-\lambda d}}}{\ln2}
\left(6\lambda d+4\ln\bar n+6+O(e^{{-\lambda d}})\right).
\]
Thus the continuous solution of \(B_{\bar n}(d)=\delta\) satisfies
\[
d=\frac1\lambda\left[
\ln\frac1\delta+\ln\ln\frac1\delta+\ln\frac6{{\ln2}}+o(1)
\right]
\qquad(\delta\downarrow0).
\]
The least unrestricted integer cutoff differs by \(O(1)\). If the cutoff must be prime, as in the source's finite-field polar construction, the prime number theorem yields an admissible prime
\[
d=\left(\frac1\lambda+o(1)\right)\ln\frac1\delta.
\]
Because the source's complete decoder uses \(O(d^2m\log m)\) arithmetic operations for blocklength \(m\), this gives the sufficient target-gap scaling
\[
O\!\left(m\log m\,\log^2\frac1\delta\right)
\]
for fixed \(\bar n\).

## Assumptions and scope
The statement concerns the explicit truncation penalty in Lemma 3 of arXiv:2610.03674v1. The mean photon number \(\bar n\) is fixed and positive, \(d\) tends to infinity, and \(\delta\) is a target upper bound on that continuity certificate. The asymptotic does not assert that the certificate is tight for the actual coherent-information loss. The prime-cutoff statement uses only the classical fact that a prime exists at \(x(1+o(1))\) above a large real threshold \(x\).

## Proof
Write \(\varepsilon=r^{{d/2}}=e^{{-\lambda d}}\). For fixed \(\bar n>0\) and \(\varepsilon\downarrow0\), direct expansion gives
\[
g(\bar n/\varepsilon)
=\frac{\ln(\bar n/\varepsilon)+1+O(\varepsilon)}{\ln2}
\]
and
\[
h_2(\varepsilon)
=\frac{\varepsilon\ln(1/\varepsilon)+\varepsilon+O(\varepsilon^2)}{\ln2}.
\]
Substitution into the definition of \(B_{\bar n}(d)\) yields
\[
B_{\bar n}(d)
=\frac{\varepsilon}{\ln2}
\left(6\ln(1/\varepsilon)+4\ln\bar n+6+O(\varepsilon)\right).
\]
Since \(\ln(1/\varepsilon)=\lambda d\), this is the displayed expansion.

For the inverse law, write \(y=\lambda d\) and \(L=\ln(1/\delta)\). The expansion implies
\[
\delta=\frac{6}{\ln2}y e^{{-y}}(1+O(1/y)).
\]
Taking logarithms gives
\[
y=L+\ln y+\ln\frac6{{\ln2}}+o(1).
\]
Because \(y/L\to1\), one may replace \(\ln y\) by \(\ln L+o(1)\), proving the continuous formula. Integer rounding changes \(d\) by at most a bounded amount once the certificate is in its eventually decreasing regime. The prime number theorem then supplies an allowed prime cutoff with the same leading \(\lambda^{{-1}}L\) scale. Substituting \(d=O(\log(1/\delta))\) into the source's \(O(d^2m\log m)\) decoder bound proves the final complexity statement.

## Verification
The algebra above reconstructs the certificate from the exact expression in Lemma 3 and uses standard asymptotic expansions of bosonic and binary entropy. The accompanying checker evaluates the exact certificate with high-precision arithmetic for several fixed energies and confirms convergence to the derived coefficient; those finite calculations are corroborative and are not used as proof. The source's complexity bound was checked in its decoder-implementation section.

## Relationship to prior work
Mandal, Piveteau, Pfister, and Renes prove that their truncated pure-loss input loses at most \(B_{\bar n}(d)\) in coherent information and state that this loss decays exponentially with the cutoff. They also prove total decoding complexity \(O(d^2m\log m)\), but do not state the target-accuracy inversion, the logarithmic correction, or the resulting accuracy dependence of the decoder bound.

Winter's energy-constrained continuity theorem supplies the entropy inequality used by that paper; it is a general continuity result and does not specialize the geometric thermal tail of this truncated two-mode squeezed state into the displayed cutoff law. Shirokov's finite-dimensional approximation work gives broad capacity-approximation theorems under energy constraints, but its general statement does not identify this channel-specific certificate or its coupling to the new polar/BPQM decoder complexity.

## Limitations
The cutoff law is sufficient for the published continuity certificate and is not a converse for finite-dimensional approximation. The full additive \(\ln\ln(1/\delta)\) correction is stated for the continuous or unrestricted-integer inversion; requiring prime dimension preserves the leading asymptotic but no equally sharp additive prime-gap term is claimed. The hidden constant in the decoder operation count remains the one hidden by the source's \(O(d^2m\log m)\) estimate. No claim is made about finite-precision implementation of the source's real-valued eigen-list registers.

## References
1. A. Mandal, C. Piveteau, H. D. Pfister, and J. M. Renes, “Efficient capacity-achieving entanglement generation with application to pure-loss Bosonic channels,” arXiv:2610.03674v1, 2026.
2. A. Winter, “Tight uniform continuity bounds for quantum entropies: conditional entropy, relative entropy distance and energy constraints,” arXiv:1507.07775v6, 2016.
3. M. E. Shirokov, “Uniform finite-dimensional approximation of basic capacities of energy-constrained channels,” arXiv:1707.05641v2, 2017.
