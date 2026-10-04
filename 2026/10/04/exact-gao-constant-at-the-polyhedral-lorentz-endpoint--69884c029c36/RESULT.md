# Exact Gao constant at the polyhedral Lorentz endpoint
## Finding
For every real parameter \(0<\omega<1\), consider the two-dimensional Lorentz sequence space \(X_\omega=l^{(2)}(\omega,1)\) with norm
\[
N_\omega(s,t)=\max\{|s|,|t|\}+\omega\min\{|s|,|t|\}.
\]
Its Gao constant
\[
c'_{\mathrm{NJ}}(X_\omega)=\inf_{x,y\in S_{X_\omega}}\frac{N_\omega(x+y)^2+N_\omega(x-y)^2}{4}
\]
has the exact value
\[
c'_{\mathrm{NJ}}(X_\omega)=
\begin{cases}
\dfrac{(1+\omega)^2}{2(1+\omega^2)},&0<\omega\le\sqrt2-1,\\[5pt]
\dfrac{1}{1+\omega^2},&\sqrt2-1\le\omega<1.
\end{cases}
\]
The two branches agree at \(\omega=\sqrt2-1\).

## Assumptions and scope
The scalar field is real and \(0<\omega<1\). If \((u',v')\) is the decreasing rearrangement of \((|u|,|v|)\), then the Lorentz norm at exponent \(r=1\) is \(u'+\omega v'\), which is exactly the displayed norm \(N_\omega\). The invariant considered here is Gao's original quadratic constant, equivalently the Gao-type constant at exponent \(2\).

For an absolute normalized norm, write its convex representative as \(\phi(t)=N_\omega(1-t,t)\). By symmetry it suffices to use \(0\le t\le1/2\), where
\[
\phi(t)=1-(1-\omega)t=(1-t)+\omega t,
\qquad
\phi_2(t)=\sqrt{(1-t)^2+t^2}.
\]

## Proof
The comparison theorem for absolute normalized norms gives, at Gao exponent \(2\),
\[
c'_{\mathrm{NJ}}(X_\omega)\ge\frac{1}{(M_1M_2)^2},
\qquad
M_1=\max_{0\le t\le1}\frac{\phi(t)}{\phi_2(t)},
\qquad
M_2=\max_{0\le t\le1}\frac{\phi_2(t)}{\phi(t)}.
\]
Cauchy--Schwarz gives
\[
(1-t)+\omega t\le\sqrt{1+\omega^2}\sqrt{(1-t)^2+t^2},
\]
with equality at \(t=\omega/(1+\omega)\). Hence
\[
M_1=\sqrt{1+\omega^2}.
\]

To compute \(M_2\), set \(u=t/(1-t)\) on \(0\le t\le1/2\), so \(0\le u\le1\). Then
\[
R(u):=\frac{\phi_2(t)}{\phi(t)}=\frac{\sqrt{1+u^2}}{1+\omega u},
\]
and
\[
\frac{d}{du}\log R(u)^2
=\frac{2(u-\omega)}{(1+u^2)(1+\omega u)}.
\]
Thus \(R\) decreases on \([0,\omega]\) and increases on \([\omega,1]\), so its maximum is attained at an endpoint:
\[
M_2=\max\left\{1,\frac{\sqrt2}{1+\omega}\right\}.
\]
Consequently the comparison theorem yields exactly the two claimed lower bounds, with the changeover at \(1+\omega=\sqrt2\).

It remains to attain them. Put
\[
a=\frac{1}{1+\omega^2},
\qquad
b=\frac{\omega}{1+\omega^2}.
\]
Then \(a\ge b>0\) and \(N_\omega(a,b)=a+\omega b=1\).

If \(0<\omega\le\sqrt2-1\), take \(x=(a,b)\) and \(y=(b,a)\). Both are unit vectors, and direct substitution gives
\[
\frac{N_\omega(x+y)^2+N_\omega(x-y)^2}{4}
=\frac{(1+\omega)^2}{2(1+\omega^2)}.
\]

If \(\sqrt2-1\le\omega<1\), take \(x=(a,b)\) and \(y=(a,-b)\). Again both are unit vectors, while
\[
N_\omega(x+y)=2a,
\qquad
N_\omega(x-y)=2b,
\]
so
\[
\frac{N_\omega(x+y)^2+N_\omega(x-y)^2}{4}
=a^2+b^2
=\frac{1}{1+\omega^2}.
\]
Each witness reaches the corresponding lower bound, proving the formula.

## Verification
The proof is analytic and does not rely on finite enumeration. The two comparison maxima were recomputed independently from their one-variable ratios, including the endpoint change at \(\omega=\sqrt2-1\). The proposed extremizers were substituted directly into \(N_\omega\) to verify both unit-sphere constraints and the claimed objective values. As an additional non-proof stress test, numerical minimization over polygonal unit-sphere edges at representative parameters on both sides of the transition agreed with the formula.

## Relationship to prior work
Zuo, Huang, Huang, and Wang define the same Gao-type invariant for absolute normalized norms and prove the general comparison bound used above. Their Lorentz example treats \(l^{(2)}(\omega,r)\) only for \(2\le r<\infty\), while their conclusion explicitly lists the range \(1\le r<2\) as not yet known. The result here settles the natural polyhedral endpoint \(r=1\) for the quadratic Gao constant and reveals a phase transition in the extremizing geometry.

Cui and Wang's earlier Lorentz calculation is stated for two-dimensional Lorentz spaces with \(2\le q<\infty\), so it does not cover this endpoint. A later paper on the generalized Gao constant also treats the Lorentz family only for \(q\ge2\) and concerns the corresponding supremal generalized invariant rather than the infimal Gao constant computed here.

## Limitations
The theorem concerns only the real two-dimensional Lorentz family at exponent \(r=1\) and Gao exponent \(2\). It does not solve the remaining interval \(1<r<2\), nor does it determine the full Gao-type family at exponents different from \(2\). Literature searches cannot exclude an unindexed or differently phrased prior computation, although the defining 2022 paper explicitly identifies the containing Lorentz range as unresolved.

## References
1. Z. Zuo, Y. Huang, H. Huang, and J. Wang, “The Gao-Type Constant of Absolute Normalized Norms on \(\mathbb{R}^2\),” *Mathematics* 10 (2022), 4591. DOI: 10.3390/math10234591.
2. H. Cui and F. Wang, “Gao's constants of Lorentz sequence spaces,” *Soochow Journal of Mathematics* 33 (2007). The published abstract states the two-dimensional calculation for \(2\le q<\infty\).
3. Z.-F. Zuo, Y.-M. Huang, and J. Wang, “The generalized Gao's constant of absolute normalized norms in \(\mathbb{R}^2\),” *Mathematical Inequalities & Applications* 26 (2023), 109–129. DOI: 10.7153/mia-2023-26-09.
