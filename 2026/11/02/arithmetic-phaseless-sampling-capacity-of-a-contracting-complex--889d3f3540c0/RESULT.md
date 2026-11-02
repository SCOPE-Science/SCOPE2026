# Arithmetic phaseless sampling capacity of a contracting complex spiral

## Finding

Fix \(0<\rho<1\), \(\theta\in\mathbb R\), and the sample nodes \(z_n=\rho^n e^{in\theta}\) for integers \(n\ge1\). If \(\theta/\pi=p/q\in\mathbb Q\) in lowest terms, take the positive denominator \(q\); for irrational \(\theta/\pi\), write \(q=\infty\).

**Theorem.** (1) Modulus data \(\{|f(z_n)|:n\ge n_0\}\) on every sufficiently late tail determine any two holomorphic functions on a connected neighborhood of the origin, up to a single unimodular factor, if and only if \(q=\infty\). Here a tail is chosen so that all its sample nodes lie in the domain.

(2) Fix an integer \(d\ge0\) and the space \(\mathcal P_d\) of complex polynomials of degree at most \(d\). All spiral moduli determine every \(P\in\mathcal P_d\) up to unimodular phase **if and only if** \(d<q\). When this holds, already the first \(M=(d+1)^2\) squared moduli suffice, and an explicit invertible Vandermonde system recovers the complete coefficient Gram matrix \((a_j\overline{a_k})_{0\le j,k\le d}\).

(3) These \(M\) measurements are the smallest number of real evaluations permitting a linear recovery of **every** Hermitian \((d+1)\times(d+1)\) lifted matrix on this prescribed spiral. This linear-lifting bound does **not** assert the minimum number of phaseless samples for rank-one polynomial signals.

For \(q\le d\), the explicit nonproportional degree-\(q\) polynomials \(1+iz^q\) and \(1-iz^q\) have identical moduli at **all** the spiral nodes.

## Assumptions and scope

The parameter \(\rho\) is strictly between zero and one, the angular increment \(\theta\) is fixed, and all claims concern exact complex arithmetic. The holomorphic statement requires an open connected domain containing \(0\) and the measured tail. No assumption of boundedness, Hardy/Bergman membership, or nonvanishing at the origin is imposed. The polynomial result holds for arbitrary complex coefficients, including zero polynomials.

The reconstruction in part (2) solves a complex Vandermonde linear system from real data and then extracts the rank-one Gram factor. This is an exact-information statement: it does not provide a uniform noise condition number as \(d\) grows.

## Proof

**1. Irrational angles imply local holomorphic phase uniqueness.** Suppose \(f,g\) have equal moduli on a sufficiently late tail. If either function is identically zero, the identity theorem makes both zero. Otherwise let \(k,\ell\) be their respective orders at the origin. Since \(|f(z_n)|\sim |a_k|\rho^{nk}\) and \(|g(z_n)|\sim |b_\ell|\rho^{n\ell}\), equality forces \(k=\ell\), and then \(|a_k|=|b_k|\). Divide each function by \(z^k\), and rotate one by a unimodular constant so their new constant terms agree and equal some \(c\ne0\).

If the resulting holomorphic functions \(F,G\) are unequal, let \(m\ge1\) be the first index at which their Taylor coefficients differ, by \(\delta\ne0\). Then, uniformly as \(z\to0\),
\[
|F(z)|^2-|G(z)|^2
 =2\operatorname{Re}(\overline c\,\delta z^m)+O(|z|^{m+1}).
\]
At \(z=z_n\) the left-hand side vanishes; division by \(\rho^{nm}\) yields
\[
\operatorname{Re}(\overline c\,\delta e^{inm\theta})=O(\rho^n).
\]
For irrational \(\theta/\pi\), the sequence \(nm\theta\pmod {2\pi}\) is dense on the circle. The continuous real function \(t\mapsto\operatorname{Re}(\overline c\,\delta e^{it})\) therefore must vanish everywhere, contradicting \(c\delta\ne0\). Hence \(F=G\) locally and, by the identity theorem, throughout the connected domain.

**2. Rational-angle counterexample and the sharp degree cutoff.** For coprime integers \(p,q\), with \(\theta=\pi p/q\), each \(z_n^q=\rho^{nq}(-1)^{np}\) is real. Thus \(|1+iz_n^q|=|1-iz_n^q|\) for all \(n\), although the two degree-\(q\) polynomials are not unimodular multiples. In particular full holomorphic recovery fails and polynomial recovery fails for \(d\ge q\).

For \(d<q\), repeat the leading-Taylor argument with two polynomials of degree at most \(d\). After factoring their common order \(k\) and matching leading phases, a nonzero difference begins at some \(1\le m\le d-k\le d\). The limit relation forces \(\operatorname{Re}(C e^{inm\pi p/q})\to0\), where \(C\ne0\). The finite periodic sequence must then vanish for every \(n\); in particular the terms at \(n=q\) and \(n=q+1\) require both \(\operatorname{Re}C=0\) and \(\operatorname{Re}(C e^{im\pi p/q})=0\). Since \(q\nmid m\), their determinant is \(\sin(m\pi p/q)\ne0\), contradiction. This proves the exact cutoff.

**3. Finite constructive phase lifting and its sharp linear sample count.** Write \(P(z)=\sum_{j=0}^d a_jz^j\) and set
\[
\lambda_{jk}=\rho^{j+k}e^{i(j-k)\theta},\qquad 0\le j,k\le d.
\]
For every \(n\ge1\),
\[
|P(z_n)|^2=\sum_{j,k=0}^d H_{jk}\lambda_{jk}^{n},
\qquad H_{jk}=a_j\overline{a_k}.
\]
The \(\lambda_{jk}\) are pairwise distinct exactly when \(\theta/\pi\) is irrational or has reduced denominator \(q>d\): equality of their absolute values forces \(j+k=j'+k'\), and equality of their arguments then forces \((j-j')\theta\in\pi\mathbb Z\), impossible for distinct \(j,j'\in\{0,\ldots,d\}\) in the stated cases. There are \(M=(d+1)^2\) distinct nonzero bases. Thus the \(M\times M\) matrix \((\lambda_{jk}^{n})_{1\le n\le M}\) is a Vandermonde matrix times an invertible diagonal, with determinant
\[
\left(\prod_{j,k}\lambda_{jk}\right)
\prod_{(j,k)<(r,s)}(\lambda_{rs}-\lambda_{jk})\ne0
\]
for any fixed ordering of the pairs. The data therefore determine the entire Hermitian Gram matrix \(H\), and, when it is nonzero, determine a vector \(a\) up to one common unimodular factor. Choose any \(k\) with \(H_{kk}>0\), take \(a_k=\sqrt{H_{kk}}>0\), and set \(a_j=H_{jk}/a_k\). The zero matrix corresponds only to the zero polynomial.

Finally, the real vector space of Hermitian \((d+1)\times(d+1)\) matrices has real dimension \(M\). Any fewer than \(M\) real intensity functionals have nontrivial kernel there; thus \(M\) is the exact minimum for **linear** recovery of the unconstrained lift. No claim is made of minimality for nonlinear rank-one recovery.

## Verification

The standalone `verify_spiral.py` checks the exact rational-angle collision criterion over a range of degrees and denominators, verifies explicit rational-resonance modulus collisions, computes a fully rational \(4\times4\) lifted-recovery determinant for degree one at \(\rho=1/2\), \(\theta=\pi/2\), and checks distinctness of several nonresonant complex Vandermonde bases. The rational determinant is \(-75/2048\). These finite tests support the formulas; the proof above establishes all quantifiers and infinitely many samples.

## Relationship to prior work

Perez (arXiv:2009.02061, 2020) proves holomorphic phase retrieval from *two full intersecting line segments* at an irrational angle and develops the local harmonic-series rigidity argument. Liehr (arXiv:2308.05722, 2023) gives an exact arithmetic criterion for *families of complete parallel lines*. Grohs–Liehr–Rathmair (arXiv:2308.00385, 2023) study *discrete, finite-density* phaseless uniqueness sets for Fock spaces, with no interior accumulation. Przybylek–Siedlecki (arXiv:1907.09371, 2019) give general polynomial-time procedures for phaseless polynomial interpolation.

The present result instead treats a **single contracting complex geometric progression**, has the exact rational denominator cutoff for **every finite degree**, and proves an explicit **consecutive-sample linear phase lift**. Full segment/line/circle measurements cannot be inferred from one point per shrinking radius. Conversely, a sequence accumulating at an interior point is very different from the separated Fock sampling sets treated in the cited work. The proof technique is elementary but the specified arithmetic sampling classification and finite lift are not stated by the inspected sources. Historical priority is not independently established.

## Limitations

The theorem is exact but gives no robust noise bound or optimal nonlinear sampling count. Because nodes accumulate exponentially at zero, Vandermonde conditioning can be severe. The holomorphic infinite-tail uniqueness theorem assumes the accumulation point lies *inside* the domain, and must not be transferred to boundary-accumulating Hardy, Bergman, or Fock sampling problems without further argument. The finite reconstruction is polynomial-specific and is not a general reconstruction algorithm for arbitrary holomorphic functions. No claim of independent audit or priority certification is made.

## References

- R. Perez III, *A Note on the Phase Retrieval of Holomorphic Functions*, arXiv:2009.02061, first posted 2020-09-04.
- P. Grohs, L. Liehr, M. Rathmair, *Phase Retrieval in Fock Space and Perturbation of Liouville Sets*, arXiv:2308.00385, first posted 2023-08-01.
- L. Liehr, *Arithmetic Progressions and Holomorphic Phase Retrieval*, arXiv:2308.05722, first posted 2023-08-10.
- M. R. Przybylek, P. Siedlecki, *A Note on the Complexity of a Phaseless Polynomial Interpolation*, arXiv:1907.09371, first posted 2019-07-22.
