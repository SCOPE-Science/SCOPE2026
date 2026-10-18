# Exact polynomial phase-retrieval fibers on two rational-angle lines

## Finding

Let \(d\ge 0\), let \(P\in\mathbb C[z]\setminus\{0\}\) have degree at most \(d\), and let two lines through the origin make angle \(\theta=\pi p/q\), where \(q\ge2\), \(1\le p<q\), and \(\gcd(p,q)=1\). Consider the polynomials \(Q\) of degree at most \(d\) for which \(|Q(z)|=|P(z)|\) on any nonempty open segment of each line, modulo the equivalence \(Q\sim e^{i\gamma}Q\).

For every \(\lambda\) in the open upper half-plane set
\[
 a_\lambda=\min_{\zeta^q=\lambda}\operatorname{ord}_\zeta(P),\qquad
 b_\lambda=\min_{\zeta^q=\overline\lambda}\operatorname{ord}_\zeta(P).
\]
Here the order of \(P\) at a point that is not a zero is zero. Only finitely many of these numbers are positive. Every solution, and no other, is
\[
 Q(z)=e^{i\gamma}P(z)\prod_{\operatorname{Im}\lambda>0}
 \left(\frac{z^q-\overline\lambda}{z^q-\lambda}\right)^{t_\lambda},
 \qquad t_\lambda\in\mathbb Z,\quad -b_\lambda\le t_\lambda\le a_\lambda.
\]
The product includes only those \(\lambda\) with \(a_\lambda+b_\lambda>0\). The exact number of classes in the phase-retrieval fiber is
\[
 \boxed{\#\mathcal F_\theta(P)=\prod_{\operatorname{Im}\lambda>0}(a_\lambda+b_\lambda+1).}
\]
In particular, the observations determine \(P\) up to phase precisely when \(P\) has no factor \(z^q-\lambda\) with nonreal \(\lambda\). This is a polynomial-dependent criterion, not a genericity assumption. Over all nonzero polynomials of degree at most \(d\), the **sharp** maximum number of classes is
\[
 \boxed{\max_{0\ne P,\ \deg P\le d}\#\mathcal F_\theta(P)=2^{\lfloor d/q\rfloor}.}
\]
Thus all degree-at-most-\(d\) polynomials are uniquely recoverable whenever \(q>d\), although the angle is rational. Conversely, for each \(q\le d\) there are polynomials admitting more than one phase class. If \(\theta/\pi\) is irrational, every polynomial is uniquely recovered up to phase, as previously known for general holomorphic functions [1,2].

Moreover, equality at \(2d+1\) distinct sample parameters on each line is sufficient to force the same **complete fiber** (and hence the same classification) as exact modulus knowledge on the segments. This is a sufficiency statement only, with no assertion of minimal sample count.

## Assumptions and scope

The lines are \(L_0=\mathbb R\) and \(L_\theta=e^{i\theta}\mathbb R\), after a harmless common rigid coordinate change. The segments can have arbitrary positive length and need not contain the origin: equality on an open interval extends to the entire supporting line by polynomial identity. The same degree cap \(d\) applies to \(P\) and competing \(Q\). An empty product equals one. The phases \(e^{i\gamma}\) are arbitrary complex scalars of modulus one. The finite sampling statement assumes \(2d+1\) distinct **real parameters per line**, with no restriction requiring the two sets to be disjoint. Cases with a zero at the origin or other real-orbit factors are included.

## Proof

**1. Two modulus identities.** Define \(\widetilde R(z)=\overline{R(\overline z)}\) for a rational function \(R\). A polynomial identity on the first real segment gives
\[
 P(z)\overline{P(\overline z)}=Q(z)\overline{Q(\overline z)}.
\]
Thus \(P\) and \(Q\) have equal order at the origin and equal degrees and leading-coefficient moduli. In particular, their quotient \(R=Q/P\) extends meromorphically across all points of the Riemann sphere and is finite and nonzero both at zero and at infinity. On the first line \(R(z)\widetilde R(z)=1\). Polynomial identity on the second line gives \(R(z)\widetilde R(e^{-2i\theta}z)=1\). Hence \(\widetilde R(z)=\widetilde R(e^{-2i\theta}z)\), equivalently \(R(e^{2i\theta}z)=R(z)\).

**2. Cyclic invariant rational functions.** Because \(e^{2i\theta}\) is a primitive \(q\)-th root of unity, every nonzero finite zero or pole of \(R\) appears with the same multiplicity on its full \(q\)-point rotation orbit. Factoring its divisor, and using regularity at zero and infinity, yields \(R(z)=S(z^q)\) for a rational function \(S\) finite and nonzero at zero and infinity. (Equivalently, \(\mathbb C(z)^{\langle z\mapsto e^{2i\theta}z\rangle}=\mathbb C(z^q)\).) The first-line identity reduces to \(S(w)\overline{S(\overline w)}=1\). A nonreal root or pole of \(S\) at \(\lambda\) therefore has the opposite valuation at \(\overline\lambda\), while no real value can be a root or pole. Thus
\[
 S(w)=c\prod_{\operatorname{Im}\lambda>0}
 \left(\frac{w-\overline\lambda}{w-\lambda}\right)^{t_\lambda},\qquad |c|=1.
\]
The restriction \(|c|=1\) follows from the first-line identity at infinity. The integer exponents are uniquely determined by the rational-function divisor, and only finitely many are nonzero.

**3. Exact polynomiality and converse.** The denominator \((z^q-\lambda)^{t_\lambda}\) for a positive exponent \(t_\lambda\) divides \(P\) precisely when \(t_\lambda\le a_\lambda\); for a negative exponent, polynomiality is equivalent to \(-t_\lambda\le b_\lambda\). Factors with distinct \(\lambda\) in the upper half-plane are relatively prime, so these conditions are independent. Conversely, every allowed product is a polynomial of degree \(\deg P\); for \(z\in L_0\cup L_\theta\) the quantity \(z^q\) is real, hence each factor has absolute value one where defined and the equality extends through removable zeros. Two different exponent tuples have different rational divisors and cannot differ only by global phase. This proves the exact list and product count.

**4. Sharp global count.** Set \(s_\lambda=a_\lambda+b_\lambda\). Each positive \(s_\lambda\) accounts for at least \(q s_\lambda\) zeros of \(P\), counted with multiplicity, and the affected orbit sets are disjoint. Thus \(\sum s_\lambda\le \lfloor d/q\rfloor\). For every nonnegative integer \(s\), \(s+1\le 2^s\); multiplying gives the bound. For \(r=\lfloor d/q\rfloor\), equality is attained by
\[
 P(z)=z^{d-qr}\prod_{j=1}^{r}\big(z^q-(j+i)\big),
\]
whose \(r\) conjugation-paired orbits each contribute exactly two choices. The case \(r=0\) gives uniqueness for every \(P\).

**5. Irrational-angle and finite-sample boundaries.** If \(\theta/\pi\) is irrational, invariance of rational \(R\) under an infinite-order rotation is impossible for a nonzero finite divisor point. Hence \(R\) has no finite nonzero root or pole; regularity at zero and infinity forces it constant. On any line, \(|P(te^{i\phi})|^2\) is a real polynomial in \(t\) of degree at most \(2d\). Equality at \(2d+1\) distinct values of \(t\) implies that polynomial identity on that line, proving finite-sample sufficiency.

## Verification

Run `python verify.py` with Python 3.10+ and NumPy. The included `verification_output.txt` records exhaustive enumeration of individual reflected-zero choices for 16 finite examples, including \(q=2,3,4,5\), multiple nonreal orbit pairs, unequal positive orbit multiplicities, conjugate orbit pairs, and a generic orbit-free example. Counts match \(\prod(a_\lambda+b_\lambda+1)\) in every test. Finite testing is not a proof of the uniform statement; Steps 1–5 are the complete algebraic argument.

## Relationship to prior work

Perez [1, Theorem 2.1] proves uniqueness for arbitrary holomorphic functions when the crossing angle is irrational; the irrational case here is not new. Jaming [3, Section 3.1.2 and Remark 3.6] establishes the reflection-orbit mechanism and identifies finite regular-polygon orbits at rational angles; that qualitative orbit observation is likewise not new. Chalendar and Partington [2, Section 2.1 and Example 2.2] give another irrational-angle proof and rational-angle counterexamples (for rational functions). The present contribution is the **exact multiplicity-sensitive polynomial fiber, uniqueness criterion, and sharp maximum over each fixed degree**, including repeated zeros and the full rational-angle denominator dependence. None of those inspected passages supplies this fiber cardinality formula or its sharp degree-constrained extremizers. Related general phase-retrieval reviews [4] do not specialize to these exact two-line polynomial fibers.

## Limitations

The finding classifies exact noiseless data and does not provide Lipschitz stability under measurement error. The sample bound \(2d+1\) per line is sufficient but not proved minimal. This is a finite-degree polynomial theorem, not a classification for unrestricted meromorphic or holomorphic functions at rational angles; those classes can have infinitely many possibilities. The sharp fiber maximum does not imply that typical polynomials have many ambiguities: generically the fiber is a singleton. Priority is assessed against the inspected sources, not independently certified; an older equivalent count hidden in factorization or Pauli-partner literature remains possible. No independent mathematical audit has been performed.

## References

[1] Rolando Perez III, *A Note on the Phase Retrieval of Holomorphic Functions*, arXiv:2009.02061v1 (first posted 2020-09-04), Theorem 2.1, https://arxiv.org/abs/2009.02061.

[2] Isabelle Chalendar and Jonathan R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255v1 (first posted 2024-03-24), Section 2.1, https://arxiv.org/abs/2403.16255.

[3] Philippe Jaming, *Uniqueness results in an extension of Pauli's phase retrieval problem*, arXiv:1009.3418 (2010), Section 3.1.2 and Remark 3.6, https://arxiv.org/abs/1009.3418.

[4] Philipp Grohs, Sarah Koppensteiner and Martin Rathmair, *Phase Retrieval: Uniqueness and Stability*, arXiv:1901.07911 (2019), https://arxiv.org/abs/1901.07911.
