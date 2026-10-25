# The sharp support-diameter disk for zeros of squared Stieltjes transforms

## Finding
Let \(0\le a<b<\infty\), and let \(\mu\) be a nonzero finite positive Borel measure supported on \([a,b]\). Define
\[
F_\mu(z)=\int_{[a,b]}\frac{d\mu(t)}{(z+t)^2},\qquad z\in\Omega:=\mathbb C\setminus[-b,-a].
\]
Let
\[
D_{a,b}=\left\{z\in\mathbb C:\left|z+\frac{a+b}{2}\right|\le\frac{b-a}{2}\right\}.
\]
Every zero of \(F_\mu\) in \(\Omega\) lies in \(D_{a,b}\). Conversely, every nonreal point of \(D_{a,b}\) is a zero of \(F_\nu\) for some nonzero positive measure \(\nu\) supported on at most two points of \([a,b]\). Thus \(D_{a,b}\), with its real diameter excluded from \(\Omega\), is the exact universal region of possible zeros as the positive measure varies.

## Assumptions and scope
The measure is finite, nonzero, positive, and supported in a fixed compact interval \([a,b]\) with \(0\le a<b\). The kernel has order two. The transform is considered only on \(\Omega=\mathbb C\setminus[-b,-a]\), where it is holomorphic. No assertion is made about transforms of infinite-support measures or kernels of noninteger order.

## Proof
Take \(z=x+iy\) with \(y>0\), and put \(\theta(t)=\arg(z+t)\in(0,\pi)\). Then \(\theta(t)\) is continuous and strictly decreasing on \([a,b]\). The arguments of \((z+t)^{-2}\) therefore range over an interval of width \(2(\theta(a)-\theta(b))\).

The elementary identity
\[
(x+a)(x+b)+y^2=\left|z+\frac{a+b}{2}\right|^2-\frac{(b-a)^2}{4}
\]
shows that \(z\) is outside \(D_{a,b}\) exactly when \(\theta(a)-\theta(b)<\pi/2\). In that case the kernel values lie in an open semicircle: after a fixed rotation, every \((z+t)^{-2}\) has strictly positive real part. Since \(\mu\) is nonzero and positive, \(F_\mu(z)\ne0\). For real \(z\notin[-b,-a]\), the integrand is positive; the lower half-plane follows by conjugation. This proves the disk bound.

For sharpness, suppose first that \(z\) is in the upper half-plane and in the interior of \(D_{a,b}\). Then \(\theta(a)-\theta(b)>\pi/2\), so continuity gives \(t_*\in(a,b)\) with \(\theta(a)-\theta(t_*)=\pi/2\). For a nonreal boundary point choose \(t_*=b\). Set
\[
\nu=|z+a|^2\,\delta_a+|z+t_*|^2\,\delta_{t_*}.
\]
Then
\[
F_\nu(z)=e^{-2i\theta(a)}+e^{-2i\theta(t_*)}=0,
\]
because the two unit phases are opposite. Complex conjugation gives the same construction in the lower half-plane. Hence every nonreal point of the disk is attained by a positive measure with at most two atoms.

## Verification
For \(a=0\), \(b=1\), and \(\nu=\delta_0+\delta_1\),
\[
F_\nu(z)=z^{-2}+(z+1)^{-2}
\]
has zeros \(z=(-1\pm i)/2\), which lie on the boundary circle \(|z+1/2|=1/2\). An interior check is \(z=-1/2+i/4\): the measure \(4\delta_0+\delta_{5/8}\) gives \(4z^{-2}+(z+5/8)^{-2}=0\). These exact examples check the sharpness construction; the universal assertion follows from the argument-width proof above, not from finite experimentation.

## Relationship to prior work
Karp and Prilepkina develop the classes of generalized Stieltjes transforms and give complex-variable conditions for them, including sectorial mapping properties and a general estimate. Those statements do not specify the support-dependent disk above or show that every nonreal point of that disk can be attained by a positive measure with at most two atoms. The result here is a sharp support-interval localization theorem for order two, together with its converse extremal construction.

## Limitations
The disk is a universal region over all positive measures supported on \([a,b]\), not a claim that a fixed measure has zeros throughout the disk. The theorem does not classify the number or multiplicity of zeros for a given measure. It does not extend here to other kernel powers, unbounded support, signed measures, or measures with a non-real support set.

## References
1. D. Karp and E. Prilepkina, “Generalized Stieltjes transforms: basic aspects,” arXiv:1111.4271v1 (first posted 18 November 2011); published in *Journal of Classical Analysis* 1 (2012), 53–74, DOI: 10.7153/jca-01-07.
2. E. R. Love and A. Byrne, “Real Inversion Theorems for Generalized Stieltjes Transforms,” *Journal of the London Mathematical Society* s2-22 (1980), 285–306, DOI: 10.1112/jlms/s2-22.2.285.
