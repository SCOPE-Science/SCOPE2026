# Arithmetic degree obstruction and robust three-delay reconstruction for exact toral maps

## Finding
For each integer \(m\ge2\), let \(T_m:\mathbb T^3\to\mathbb T^3\) be the toral endomorphism with integer matrix
\[
 A_m=\begin{pmatrix}0&-2&0\\1&4&0\\0&0&m\end{pmatrix},\qquad \mathbb T^3=\mathbb R^3/\mathbb Z^3.
\]
For a continuous map \(F:\mathbb T^3\to\mathbb T^3\) homotopic to \(T_m\), and any continuous circle-valued observable \(\phi:\mathbb T^3\to S^1\), consider its three consecutive forward-delay map
\[
 \mathcal D_{F,\phi}(x)=\big(\phi(x),\phi(Fx),\phi(F^2x)\big)\in(S^1)^3.
\]
Then the **complete set of topological degrees** attained as \(\phi\) varies is exactly
\[
 \boxed{\{\deg\mathcal D_{F,\phi}:\phi\in C(\mathbb T^3,S^1)\}=(m^2-4m+2)\,\mathbb Z.}
\]
In particular, when \(m\ne3\), **no continuous circle-valued observable can yield an injective three-delay map**, for any such \(F\). In contrast, when \(m=3\), the smooth character
\[
 \phi_0(x)=\exp\big(2\pi i(x_2+x_3)\big)
\]
has a three-delay map that is a torus-group automorphism for \(F=T_3\); the same fixed observable gives a \(C^1\) diffeomorphic three-delay map for every \(C^1\) torus map sufficiently close to \(T_3\). Thus the exact three-delay reconstruction threshold is \(m=3\), and this threshold is stable under the stated perturbations.

For the unperturbed map \(T_m\), if the observable is restricted to a character \(\chi_{p,q,r}(x)=\exp(2\pi i(px_1+qx_2+rx_3))\) with integers \(p,q,r\), then the delay map either has infinite fibers or is a finite torus covering of degree
\[
 |r(m^2-4m+2)(-2p^2+4pq-q^2)|.
\]
Its **smallest possible nonzero covering degree** is \(|m^2-4m+2|\). The character \(\phi_0\) attains this minimum for every \(m\), with an explicit cyclic kernel of that order. A second circle character always suffices for reconstruction: the three scalar samples \(\chi_{0,1,0}(x)\), \(\chi_{0,1,0}(T_mx)\), and \(\chi_{0,0,1}(x)\) give a torus automorphism. Therefore the smallest number of circle-valued sensors whose three-delay data injectively reconstruct the state of \(T_m\) is one for \(m=3\) and two otherwise. This sensor count uses exactly three consecutive time samples per sensor and does not concern arbitrarily many delays.

## Assumptions and scope
The parameter \(m\) is an arbitrary integer at least two. All spaces, maps and observables in the degree and impossibility statements are continuous; \(F\) need only be homotopic to the stated integer torus endomorphism, with no injectivity, hyperbolicity or differentiability hypothesis. The positive perturbative statement takes \(F\) of class \(C^1\) in a sufficiently small neighborhood of \(T_3\), in the standard flat-torus \(C^1\) topology. The character-fiber and two-sensor formulas concern the unperturbed map \(T_m\). Degrees use the standard orientations of domain and codomain \(\mathbb T^3\).

This family is noninvertible and hyperbolic, with eigenvalues \(2-\sqrt2\), \(2+\sqrt2\) and \(m\); its characteristic polynomial has no nonconstant unimodular factor, so it is exact by the established toral-endomorphism criterion. The contracted direction makes the family nonexpanding. These contextual dynamics are not premises of the degree calculation.

## Proof
**Cohomological degree formula.** Every continuous \(\phi:\mathbb T^3\to S^1\) has an integral cohomology class \((p,q,r)\in H^1(\mathbb T^3;\mathbb Z)\cong\mathbb Z^3\). Equivalently, \(\phi\) is homotopic to the Fourier character \(\chi_{p,q,r}\). Since \(F\) is homotopic to \(T_m\), its pullback on first integral cohomology has matrix \(A_m^\mathsf T\). Hence the three coordinate cohomology classes of \(\mathcal D_{F,\phi}\) are represented by the rows of the integral observability matrix
\[
 M_{p,q,r}(m)=\begin{pmatrix} k\\kA_m\\kA_m^2\end{pmatrix},\qquad k=(p,q,r).
\]
The top-degree cohomology generator of \(\mathbb T^3\) is the cup product of the three degree-one generators. Pulling it back multiplies it by the determinant of the three first-cohomology rows, proving \(\deg\mathcal D_{F,\phi}=\det M_{p,q,r}(m)\). This is valid for nonlinear \(F\) and nonlinear \(\phi\), without a regular-value assumption.

**Exact determinant and complete degree spectrum.** Direct multiplication gives the first two rows
\[
 (p,q,r),\qquad (q,-2p+4q,mr).
\]
Replacing the third row by \((\text{third})-4(\text{second})+2(\text{first})\) produces \((0,0,r f(m))\), where \(f(m)=m^2-4m+2\). Thus
\[
 \det M_{p,q,r}(m)=r f(m)Q(p,q),\quad Q(p,q)=-2p^2+4pq-q^2.
\]
Every degree is divisible by \(f(m)\). Conversely, \(Q(0,1)=-1\) and \(r\) may be any integer, so the choices \((p,q,r)=(0,1,r)\) realize **every** integer multiple of \(f(m)\). This proves the exact spectrum even when \(F\) is nonlinear, because the cohomological action has not changed.

**Sharp impossibility and the exceptional embedding.** If a continuous map \(G:\mathbb T^3\to\mathbb T^3\) is injective, invariance of domain makes its image open. Compactness makes its image closed; connectedness forces it to be the whole codomain. Thus \(G\) is a homeomorphism and \(|\deg G|=1\). The integer \(f(m)=(m-2)^2-2\) has absolute value one for an integer \(m\ge2\) precisely when \(m=3\): the equation \(f(m)=-1\) gives \((m-2)^2=1\), and \(f(m)=1\) gives \((m-2)^2=3\). Therefore the degree spectrum prevents injective three-delay maps for \(m\ne3\).

At \(m=3\), take \(k=(0,1,1)\). Then \(\det M_{0,1,1}(3)=-f(3)=1\). The character delay map for \(T_3\) is exactly the integer linear torus map induced by \(M_{0,1,1}(3)\in\operatorname{GL}(3,\mathbb Z)\), so it is a smooth group automorphism. For \(C^1\) maps \(F\) sufficiently close to \(T_3\), the fixed-character delay map remains \(C^1\)-close to this automorphism; its differential stays invertible on compact \(\mathbb T^3\). It is therefore a local diffeomorphism, hence a covering, and its homotopy-invariant degree stays \(+1\). A covering of degree one with consistent orientation is one-sheeted, hence a global \(C^1\) diffeomorphism.

**Exact character ambiguity.** When the determinant vanishes, the integer linear torus map induced by \(M\) has positive-dimensional kernel, so each nonempty fiber is infinite. Otherwise it is a surjective covering, and Smith normal form or a fundamental-lattice index calculation gives exactly \(|\det M|\) points per fiber. Since any nonzero integer product \(|rQ(p,q)|\) is at least one, the smallest possible nonzero covering degree is \(|f(m)|\); it is attained by \(k=(0,1,1)\). For this character, a generator for its entire finite kernel is
\[
 v_m=\frac1{f(m)}(4-m,-1,1)\pmod{\mathbb Z^3}.
\]
Indeed \(M_{0,1,1}(m)v_m=(0,0,1)^\mathsf T\) and the third coordinate of \(v_m\) has exact additive order \(|f(m)|\). The determinant gives the same order for the full kernel, so this cyclic subgroup exhausts it.

**Two-sensor realization.** Let \(\psi_1=\chi_{0,1,0}\), \(\psi_2=\chi_{0,0,1}\). The joint three-measurement map \(x\mapsto(\psi_1(x),\psi_1(T_mx),\psi_2(x))\) is induced by
\[
 \begin{pmatrix}0&1&0\\1&4&0\\0&0&1\end{pmatrix},
\]
whose determinant is \(-1\), independently of \(m\). It is a smooth torus-group automorphism. When \(m\ne3\), the preceding degree obstruction proves no single continuous circle-valued sensor with three delays can replace these two. When \(m=3\), one suffices. (One or two circle samples cannot embed a three-torus, by covering dimension.)

## Verification
A standalone symbolic checker, `checks/check_delay_degree.py`, verifies the characteristic-polynomial recurrence, the exact symbolic determinant identity, the cyclic-kernel Smith invariants for \(2\le m\le19\), and bounded integer tests in \((p,q,r)\). It was executed successfully. The unbounded quantifiers, degree obstruction, and perturbation stability follow from the analytic and topological proof above, not finite testing.

## Relationship to prior work
Leuridan, *Linear toral endomorphisms, exactness, Bernoulliness and generators* (arXiv:2610.01642v1, first public 1 October 2026, primary MSC 37A05) establishes structural properties of exact nonexpanding toral endomorphisms and rules out smooth **finite-partition** generators under a boundary-regularity condition. A circle-valued continuous observable has infinitely many possible outputs, so its three-delay injectivity is a different property and does not contradict finite-partition obstructions. The present classification concerns a concrete hyperbolic exact family and a topological degree invariant not supplied in that work.

Botvinick-Greenhouse, Martin and Yang, *Invariant Measures in Time-Delay Coordinates for Unique Dynamical System Identification* (arXiv:2412.00589v2), formulate delayed-observable embeddings and identification results with dimension and genericity conditions, but not this integral-homotopy obstruction or exceptional three-delay family. Hughes, *Behavioral Realizations using Companion Matrices and the Smith Form* (SIAM J. Control Optim. 2016, DOI 10.1137/140991911), develops observability via companion matrices in real continuous-time linear systems; it does not state the mod-one degree spectrum for nonlinear toral delay maps. The determinant method uses standard cohomological degree, integral observability, and Smith normal form; their general availability is acknowledged rather than claimed novel.

## Limitations
The exact classification is only for **three consecutive** forward circle-valued delays of the stated toral homotopy classes. It does not exclude reconstruction with four or more delays, other observation codomains, or nonconsecutive time choices. The perturbative positive result is local in the \(C^1\) topology near the indicated linear map; no global positive theorem for all nonlinear maps in the same homotopy class is claimed. The optimal covering-degree formula is exact for Fourier characters at the unperturbed maps; arbitrary continuous observables need not be coverings, and degree zero alone gives no universal fiber-cardinality bound. General observability and integer-lattice tools could give equivalent formulations not found in the literature searched.

## References
1. C. Leuridan, *Linear toral endomorphisms, exactness, Bernoulliness and generators*, arXiv:2610.01642v1 (2026), https://arxiv.org/abs/2610.01642 .
2. J. Botvinick-Greenhouse, R. Martin, Y. Yang, *Invariant Measures in Time-Delay Coordinates for Unique Dynamical System Identification*, arXiv:2412.00589v2, https://arxiv.org/abs/2412.00589 .
3. T. H. Hughes, *Behavioral Realizations using Companion Matrices and the Smith Form*, SIAM J. Control Optim. 54 (2016), 845–865, DOI 10.1137/140991911, https://www.repository.cam.ac.uk/items/21fcdf02-4927-46cd-bc18-23f23d51e477 .
