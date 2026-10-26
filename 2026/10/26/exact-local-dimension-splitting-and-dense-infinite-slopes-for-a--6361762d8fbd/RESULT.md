# Exact local-dimension splitting and dense infinite slopes for a critical-cusp tent conjugacy

## Finding
For every \(1<\theta<2\), consider the symmetric expanding full-branch map defined below and its unique measure of maximal entropy \(\mu_\theta\). Put \(\Lambda_\theta=1+\theta/2\), \(d_0=\log 2/\log\Lambda_\theta\), and \(d_c=d_0/2\). There exist positive finite constants, depending on the fixed parameter, such that as \(r\downarrow0\),
\[
\mu_\theta([0,r])\asymp r^{d_0},\qquad
\mu_\theta([1-r,1])\asymp r^{d_0},\qquad
\mu_\theta([\tfrac12-r,\tfrac12+r])\asymp r^{d_c}.
\]
Here \(\asymp\) denotes two-sided bounds by constants independent of sufficiently small \(r\). In particular, the corresponding pointwise dimensions exist and equal \(d_0\) at each endpoint and \(d_c\) at the critical point and every one of its finite preimages. The precritical set is countable and dense.

The increasing distribution function \(H_\theta(x)=\mu_\theta([0,x])\) is a homeomorphism satisfying \(H_\theta\circ f_\theta=T\circ H_\theta\), where \(T(u)=2\min\{u,1-u\}\). It has extended derivative \(+\infty\) at every precritical point, one-sided derivative zero at both endpoints, and ordinary derivative zero for Lebesgue-almost every interior point. Thus \(\mu_\theta\) is singular with respect to Lebesgue measure, even though the same map has a unique absolutely continuous invariant probability with \(W^{2,1}\) density [1]. The precise exponents satisfy \(1<d_0<\log2/\log(3/2)\) and \(1/2<d_c<\log2/(2\log(3/2))<1\).

## Assumptions and scope
Fix \(1<\theta<2\) and write \(c=1/2\), \(K_\theta=(1-\theta/2)/\sqrt2\). For \(0\le t\le1/2\) put
\[
f_\theta(c\pm t)=1-\theta t-2K_\theta\sqrt t.
\]
Each half interval maps monotonically onto \([0,1]\). Away from \(c\), its derivative has absolute value \(\theta+K_\theta/\sqrt{|x-c|}\ge\Lambda_\theta>1\). We use the two inverse branches \(g_0:[0,1]\to[0,c]\) and \(g_1:[0,1]\to[c,1]\), with the branch endpoints interpreted in the usual measure-zero manner. Let \(\mu_\theta\) be the Bernoulli measure assigning mass \(2^{-n}\) to each \(n\)-cylinder; the uniformly contracting inverse branches make it uniquely defined. The measure is nonatomic, fully supported, ergodic, and of entropy \(\log2\), so it is the unique measure of maximal entropy. Pointwise dimension at an endpoint is defined using the intersection of centered balls with \([0,1]\). The result is not a claim about the almost-everywhere dimension of \(\mu_\theta\).

## Proof
**1. Bernoulli cylinders and tent conjugacy.** Each inverse branch is Lipschitz with constant at most \(\Lambda_\theta^{-1}\). Its cylinders have exponentially shrinking diameters and full symbolic incidence. Pushing the fair two-symbol Bernoulli law to the unique points in the nested cylinders gives an ergodic nonatomic invariant probability \(\mu_\theta\) satisfying
\[
\mu_\theta(g_i(B))=\tfrac12\mu_\theta(B)
\]
for Borel sets \(B\), up to overlaps at the common inverse-branch endpoint of zero mass. This gives full support. The itinerary is one-to-one except for at most countably many boundary codings, so the system is measurably isomorphic to the full fair two-shift. The full-branch symbolic coding also gives entropy at most \(\log2\), with equality only for the fair Bernoulli law, proving uniqueness of the maximal-entropy measure. From the branch identities for its distribution function,
\[
H_\theta(f_\theta(x))=2H_\theta(x)\quad(0\le x\le c),\qquad
H_\theta(f_\theta(x))=2(1-H_\theta(x))\quad(c\le x\le1).
\]
Consequently \(H_\theta\) is an increasing homeomorphism conjugating \(f_\theta\) to the full tent map.

**2. Sharp left-endpoint scaling.** Since \(f_\theta(0)=0\) and its right derivative equals \(\Lambda_\theta\), its left inverse branch satisfies
\[
g_0(u)=\Lambda_\theta^{-1}u+O_\theta(u^2),\qquad u\downarrow0.
\]
Choose a sufficiently small \(\delta>0\), and set \(u_n=g_0^n(\delta)\). Uniform contraction implies \(\sum_n u_n<\infty\). Therefore, since \(\log(u_{n+1}/u_n)=-\log\Lambda_\theta+O_\theta(u_n)\), the product telescopes to a finite positive limit \(\lim_{n\to\infty}\Lambda_\theta^n u_n=L_\delta\in(0,\infty)\). The exact Bernoulli cylinder identity gives
\[
\mu_\theta([0,u_n])=2^{-n}\mu_\theta([0,\delta]).
\]
Because \(u_n\asymp\Lambda_\theta^{-n}\) and successive scales have uniformly bounded ratios, monotonicity sandwiches any sufficiently small \(r\) between adjacent \(u_n\), yielding \(\mu_\theta([0,r])\asymp r^{d_0}\). Taking logarithms proves the claimed left-endpoint pointwise dimension.

**3. Right endpoint and cusp scaling.** As \(r\downarrow0\),
\[
f_\theta(1-r)=\Lambda_\theta r+O_\theta(r^2).
\]
The right-branch Bernoulli identity, valid for all small \(r\), gives the exact relation
\[
\mu_\theta([1-r,1])=\tfrac12\mu_\theta([0,f_\theta(1-r)]),
\]
so the right-endpoint exponent is also \(d_0\). Near the cusp define \(s(r)=\theta r+2K_\theta\sqrt r\). Each half of \([c-r,c+r]\) maps bijectively to \([1-s(r),1]\), and each has half the image mass. Thus the **exact identity**
\[
\mu_\theta([c-r,c+r])=\mu_\theta([1-s(r),1])
\]
holds; similarly each one-sided cusp interval has half that mass. As \(s(r)\asymp\sqrt r\), the two-sided cusp bounds are precisely \(r^{d_0/2}\). This also establishes positive lower bounds individually on the left and right cusp increments.

**4. Dense precritical transfer.** Every cylinder \(g_w([0,1])\) contains the point \(g_w(c)\), which is an \(n\)-step preimage of \(c\) when \(w\) has length \(n\). Their diameters tend uniformly to zero, proving density of \(\mathcal P=\bigcup_{n\ge0}f_\theta^{-n}(\{c\})\). For \(x\in f_\theta^{-n}(\{c\})\) choose a small neighborhood within its \(n\)-cylinder. There are no earlier encounters with \(c\) since the critical orbit is \(c\mapsto1\mapsto0\mapsto0\). The iterate \(f_\theta^n\) is therefore a smooth local diffeomorphism with finite nonzero derivative at \(x\), and the exact cylinder mass-scaling identity transports the one-sided cusp bounds back to \(x\). Hence \(\mu_\theta([x-r,x+r])\asymp_x r^{d_c}\), and the same exponent holds from either side. As \(d_c<1\), both difference quotients of \(H_\theta\) diverge to \(+\infty\). Since \(d_0>1\), the one-sided endpoint difference quotients tend to zero.

**5. Singularity despite smooth invariant density.** Proposition 4.2 of [1] proves that this map has a unique absolutely continuous invariant probability \(\nu_\theta\) with density in \(W^{2,1}([0,1])\subset L^\infty\). If \(\mu_\theta\) were absolutely continuous, uniqueness would force \(\mu_\theta=\nu_\theta\), contradicting the mass bound \(\mu_\theta([c-r,c+r])\gtrsim r^{d_c}\) with \(d_c<1\). To exclude a nonzero absolutely continuous component, note that both \(f_\theta\) and its inverse branches map Lebesgue-null sets to null sets: away from the single cusp \(f_\theta\) is locally Lipschitz on a countable cover, while both inverse branches are globally Lipschitz. Accordingly the Lebesgue-decomposition components of an invariant measure are themselves invariant. Ergodicity of \(\mu_\theta\) forces one component to vanish. The absolutely continuous component is impossible, so \(\mu_\theta\perp\mathrm{Leb}\). By the differentiation theorem for distribution functions, \(H_\theta'=0\) for Lebesgue-almost every \(x\).

## Verification
The independent finite arithmetic diagnostics in `verify.py` evaluate the original maps and both explicit inverse branches on \(1001\) test ordinates for each of three parameters, verify branch identities and cusp envelopes, and check the convergence of scaled inverse iterates. The resulting output, in `verification_output.txt`, reports `FINITE_IDENTITY_DIAGNOSTICS_PASS 6030`. These are finite checks only. The infinite-scale estimates follow from the contraction, summability, and exact Bernoulli identities proved above, not the computation.

## Relationship to prior work
Oltiboev and Vafoyev [1] define precisely this square-root-cusp family and prove the existence and uniqueness of its smooth absolutely continuous invariant density, but do not analyze its maximal-entropy measure or local dimensions. Dobbs [2, Section 11] establishes the general tent-conjugacy interpretation of maximal-entropy measures for cusp maps, constructs other examples with different Lyapunov behavior, and explains why such measures need not share the density regularity of a physical measure. The present result uses this established entropy framework, and adds a sharp **three-site pointwise-dimension law**, its transfer to **every** precritical point, and the resulting explicit coexistence of dense infinite slopes with almost-everywhere zero slope for the particular critical family whose invariant density is highly regular. No priority claim is made for the general Bernoulli/tent-conjugacy principle.

## Limitations
The inequalities are two-sided power laws, not asserted asymptotic constants. The theorem does not calculate the Hausdorff dimension of the entire maximal-entropy measure, the multifractal spectrum of all generic points, or differentiability at arbitrary exceptional points. The derivative \(+\infty\) is in the extended monotone sense; finite derivative assertions do not follow from that description. Existing general results on local dimensions of conformal measures might imply some of these exponents upon specialization, and complete bibliographic exhaustiveness is not asserted.

## References
[1] D. Oltiboev and F. Vafoyev, *Critical cusp cancellation and analytic response for a Bernoulli random interval map*, arXiv:2610.23180v1 (2026), especially Section 3 and Proposition 4.2. https://arxiv.org/abs/2610.23180

[2] N. Dobbs, *On cusps and flat tops*, Annales de l'Institut Fourier 64 (2014), Section 11, DOI:10.5802/aif.2858. https://doi.org/10.5802/aif.2858

[3] N. Dobbs, *Visible measures of maximal entropy in dimension one*, Bulletin of the London Mathematical Society 39 (2007), 366–376, DOI:10.1112/blms/bdm005. https://doi.org/10.1112/blms/bdm005
