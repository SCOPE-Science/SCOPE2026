# The arithmetic zeta function of the characteristic-three Ballico–Hefez K3 resolution

## Finding
Let \(S\subset\mathbb P^3_{\mathbb F_3}\) have coordinates \([w:x_0:x_1:x_2]\) and equation
\[
 w^4=2(x_0^3x_1+x_0x_1^3)-x_2^4-(x_2^2-x_0x_1)^2.
\]
Let \(Y\to S\) be its minimal resolution over \(\mathbb F_3\). Then \(Y\) is a K3 surface, the Frobenius characteristic polynomial on \(H^2_{\mathrm{\acute et}}(Y_{\overline{\mathbb F}_3},\mathbb Q_\ell)\), for \(\ell\ne3\), is
\[
 \boxed{(X-3)^{14}(X+3)^8},
\]
and its Hasse–Weil zeta function is
\[
 \boxed{Z(Y,T)=\frac{1}{(1-T)(1-9T)(1-3T)^{14}(1+3T)^8}}.
\]
For every integer \(n\ge1\), this is equivalent to the exact formula
\[
 \boxed{\#Y(\mathbb F_{3^n})=1+3^{2n}+(14+8(-1)^n)3^n}.
\]
In particular, \(\#Y(\mathbb F_3)=28\), \(\#Y(\mathbb F_9)=280\), and the arithmetic Picard ranks are \(\rho(Y/\mathbb F_3)=14\) and \(\rho(Y/\mathbb F_9)=22\). All assertions refer to this specific prime-field model, not every \(\mathbb F_3\)-form of the geometric K3 surface.

## Assumptions and scope
The cited geometric theorem of Hoang–Shimada identifies the three \(\mathbb F_3\)-rational singularities of \(S\) as rational double points of type \(A_3\) and describes the minimal resolution. Its 40 explicitly parametrized lines and nine exceptional curves are all defined over \(\mathbb F_9\) and span the 22-dimensional second \(\ell\)-adic cohomology rationally. For each exceptional chain, the two end curves are conjugate under \(\mathbb F_9/\mathbb F_3\), while the middle curve is fixed. The statements below use these published geometric inputs; the arithmetic point counts and the resulting full Frobenius polynomial are calculated here.

## Proof
**Finite base-field counts.** The homogeneous equation is evaluated by enumerating unique normalized representatives, namely four-tuples whose first nonzero coordinate equals 1. There are exactly \(3^3+3^2+3+1=40\) such representatives over \(\mathbb F_3\). For the equation displayed above, the counts by first nonzero coordinate \(w,x_0,x_1,x_2\) are respectively \(12,6,1,0\). Thus \(\#S(\mathbb F_3)=19\). The accompanying checker verifies this by two exhaustive methods: evaluation on all 40 projective points and counting fourth roots over each of the 13 points of \(\mathbb P^2(\mathbb F_3)\). These are finite, exhaustive computations, not inferences from sampling.

At each of the three singularities, the geometric exceptional fiber is a chain of three projective lines. Over \(\mathbb F_3\), Frobenius exchanges the distinct end components and fixes the middle component. Every rational point of the exceptional fiber therefore lies on the middle component, which is \(\mathbb P^1_{\mathbb F_3}\), and there are four such points. Replacing each singular point by its exceptional fiber contributes three net rational points. Hence
\[
 \#Y(\mathbb F_3)=19+3(4-1)=28.
\]

**Two-valued Frobenius.** All the divisors in the cited cohomology-spanning set are defined over \(\mathbb F_9\). On untwisted \(H^2\), therefore, the square of geometric Frobenius acts as multiplication by 9. The second cohomology has dimension 22, so its Frobenius eigenvalues are among \(3\) and \(-3\). Write their multiplicities \(a\) and \(b\), so \(a+b=22\). The Lefschetz trace formula for K3 surfaces yields
\[
 28=1+9+3(a-b),
\]
whence \(a-b=6\), \(a=14\), \(b=8\). This gives the displayed characteristic polynomial, the zeta function, and every extension-field count.

**Independent quadratic-field check.** Over \(\mathbb F_9=\mathbb F_3[u]/(u^2+1)\), exhaustive enumeration of all 820 normalized points of \(\mathbb P^3(\mathbb F_9)\), independently checked by fourth-root fibers over all 91 points of \(\mathbb P^2(\mathbb F_9)\), gives \(\#S(\mathbb F_9)=199\). Over \(\mathbb F_9\), each three-component exceptional chain has \(3(9+1)-2=28\) points. Consequently
\[
 \#Y(\mathbb F_9)=199+3(28-1)=280
 =1+9^2+22\cdot9,
\]
as required by the Frobenius computation.

**Picard ranks.** The geometric Néron–Severi rank is 22. A divisor class descends to \(\mathbb F_{3^n}\) up to finite index precisely when the corresponding Frobenius eigenvalue is \(3^n\). There are 14 positive eigenvalues over \(\mathbb F_3\), while over \(\mathbb F_9\) all 22 classes descend, proving the stated arithmetic ranks.

## Verification
Run `python3 CHECK.py` with Python 3 and no third-party dependencies. It implements \(\mathbb F_3\) and \(\mathbb F_9\), verifies finite-field arithmetic and normalization, independently counts the quartic using projective points and fourth-root fibers, and checks both resolved counts and the eigenvalue multiplicities. Its expected final line is `VERIFY_OK`. The geometric basis and exceptional-fiber decomposition are established in the cited primary work, not by this finite-field program.

## Relationship to prior work
Hoang–Shimada construct the Ballico–Hefez cyclic quartic in characteristic three, prove its exceptional \(3A_3\) configuration, and exhibit the 49 rational curves spanning second cohomology (their Section 6). Their paper identifies the geometric supersingular K3 surface with Artin invariant one; it does not provide the prime-field Frobenius polynomial above or the associated zeta function. Schütt proves existence of a *different* \(\mathbb F_3\)-form of the same geometric supersingular K3 surface with arithmetic Picard rank 21, so the geometric isomorphism class alone does not determine this form's arithmetic Picard rank or zeta function. The present computation supplies those exact invariants for the explicit Hoang–Shimada model.

## Limitations
This result depends on the published generation of cohomology by the 49 divisors and their fields of definition. The included checker exhausts the relevant finite-field point sets but does not itself reprove that geometric theorem. The zeta function is for the *smooth minimal resolution*, not the singular quartic. The calculation does not classify all \(\mathbb F_3\)-twists, their automorphisms, or their integral Néron–Severi lattices. Independent mathematical validation has not yet been performed; less accessible historical calculations could conceivably contain the same exact arithmetic specialization.

## References
1. H. T. Hoang and I. Shimada, *On Ballico–Hefez curves and associated supersingular surfaces*, arXiv:1402.3372, first public version 2014-02-14, especially Proposition 1.9 and Section 6. https://arxiv.org/abs/1402.3372
2. M. Schütt, *A note on the supersingular K3 surface of Artin invariant 1*, arXiv:1105.4993, 2011, especially Theorem 1.1 and Section 2. https://arxiv.org/abs/1105.4993
