# A mesoscopic Gaussian law for residue obstructions in binary polynomial rings

## Finding
Let \(\mathbb A=\mathbb F_2[T]\), let \(d\ge 2^{16}\), and choose a monic polynomial \(f\in\mathbb A\) of degree \(d\) uniformly from its \(2^d\) possibilities. Put
\[
L=\log_2 d,\qquad E=\lceil L\rceil,\qquad
B=\big\lfloor L-\log_2 L-3\big\rfloor.
\]
For every monic irreducible \(P\) of degree at least two, write \(\psi_P(f)\in\mathbb F_2\) for the residue-field trace of the residue at \(P\) of
\[
\omega_f=\frac{dT}{T(T+1)f(T)},
\]
and define \(J_P(f)=1\) if \(P\mid f\) and \(\psi_P(f)=1\), and \(J_P(f)=0\) otherwise. Define the degree-truncated obstruction count
\[
W_d(f)=\sum_{\substack{P\ \text{monic irreducible}\\2\le\deg P\le B}}J_P(f).
\]
For \(Q_P=2^{\deg P}\), let \(\beta_P=(Q_P^{-1}+Q_P^{-2})/2\). Then the **joint distribution** of the entire vector \((J_P(f))_{2\le\deg P\le B}\) is within total variation distance \(7d^{-2}\) of a family of independent Bernoulli variables with respective parameters \(\beta_P\). In particular, for every \(d\ge2^{16}\),
\[
\left|\Pr(W_d=0)-\prod_{2\le\deg P\le B}(1-\beta_P)\right|\le\frac7{d^2}.
\]

Put \(I_j=j^{-1}\sum_{a\mid j}\mu(a)2^{j/a}\), the number of monic irreducibles of degree \(j\) over \(\mathbb F_2\), and \(\beta_j=(2^{-j}+2^{-2j})/2\). Define
\[
\mu_B=\sum_{j=2}^B I_j\beta_j,\qquad
v_B=\sum_{j=2}^B I_j\beta_j(1-\beta_j).
\]
As \(d\to\infty\), \(B\to\infty\), and
\[
\mu_B=\tfrac12\log B+O(1),\qquad
v_B=\tfrac12\log B+O(1),
\]
with natural logarithms in these expressions. Moreover, for an absolute constant \(C_0\),
\[
\sup_{t\in\mathbb R}\left|
\Pr\!\left(\frac{W_d-\mu_B}{\sqrt{v_B}}\le t\right)-\Phi(t)
\right|\le\frac{C_0}{\sqrt{\log B}}+\frac7{d^2}
\]
for all sufficiently large \(d\), where \(\Phi\) is the standard normal distribution function. The zero-obstruction probability has the explicit asymptotic
\[
\Pr(W_d=0)=\frac{\mathfrak C}{\sqrt B}\left(1+O(B^{-1})\right)+O(d^{-2}),
\]
where the positive convergent Euler-type constant is
\[
\mathfrak C=e^{(1-\gamma)/2}
\prod_{j=2}^{\infty}\left(e^{1/(2j)}(1-\beta_j)^{I_j}\right)
=1.4303595418685\ldots .
\]
Here \(\gamma\) is the Euler–Mascheroni constant. Equivalently, the zero-obstruction probability is asymptotic to \(\mathfrak C/\sqrt{\log_2 d}\). These assertions concern the *residue obstruction statistic*, not the occurrence of positive orthogonal multiplicity.

## Assumptions and scope
All polynomials are over \(\mathbb F_2\), and all irreducibles are monic. The trace of a local residue is well-defined for every \(P\mid f\); set \(J_P(f)=0\) when \(P\nmid f\). Prime factors \(T\) and \(T+1\) are excluded from the counted family, but they are not forbidden as factors of \(f\). The law is unconditional and finite-degree, with a growing set of primes up to the explicitly specified bound \(B\). It uses the established single-prime residue distribution of Niedbala Giraudin (2026), whose proof is also summarized below. There is no assumption of independence for *all* prime divisors, nor any unproved orthogonal-multiplicity criterion.

## Proof
**1. Prime-local probabilities.** Fix a monic irreducible \(P\) of degree \(j\ge2\), and write \(Q=2^j\). In the uniform \(P\)-adic residue model, \(\Pr(\nu_P(f)=e)=(1-Q^{-1})Q^{-e}\) for every integer \(e\ge0\). For \(e=1\), write \(f=Ph\). Reduction of the simple-pole formula gives
\[
\psi_P(Ph)=\operatorname{Tr}_{\mathbb F_Q/\mathbb F_2}
\left(\frac{1}{T(T+1)hP'}\bmod P\right).
\]
For uniformly distributed units \(h\bmod P\), inversion and multiplication by the fixed unit permute \(\mathbb F_Q^\times\). The trace-one subset has \(Q/2\) elements, so \(\Pr(\psi_P=1\mid\nu_P=1)=Q/[2(Q-1)]\). For every \(e\ge2\), the local residue depends only on \(h\bmod P^e\). Multiplication of \(h\) by \(1+P^{e-1}s\), with \(s\bmod P\), changes the residue trace by a nonzero \(\mathbb F_2\)-linear trace form in \(s\). Hence its values are exactly balanced in every such coset, and \(\Pr(\psi_P=1\mid\nu_P=e)=1/2\). This rederives the two ingredients of the 2026 single-prime theorem.

It follows by summing the disjoint valuation events that
\[
\Pr(J_P=1)=\frac{(1-Q^{-1})Q^{-1}Q}{2(Q-1)}
+\frac12\sum_{e=2}^{\infty}(1-Q^{-1})Q^{-e}
=\frac1{2Q}+\frac1{2Q^2}=\beta_P.
\]
The infinite expression is a local \(P\)-adic probability; finite-degree samples will be compared to it by truncation.

**2. Uniformity and simultaneous truncation.** Fix \(E\ge2\). Let \(J_{P,E}(f)=J_P(f)\) if \(\nu_P(f)<E\), and zero otherwise. If \(\nu_P(f)=e<E\), then \(f=P^eh\) and the residue depends only on \(h\bmod P^e\), hence on \(f\bmod P^{2e}\). Therefore \(J_{P,E}\) depends only on \(f\bmod P^{2E}\). Under the uniform distribution modulo \(P^{2E}\) its success probability is
\[
\beta_{P,E}=\frac1{2Q}+\frac1{2Q^2}-\frac1{2Q^E}.
\]
Indeed, the omitted valuation tail \(e\ge E\) has probability \(Q^{-E}\), and its conditional trace-one probability is \(1/2\).

For any monic modulus \(R\) with \(\deg R\le d\), uniform monic degree-\(d\) polynomials are exactly uniform modulo \(R\): their \(d\) freely chosen lower coefficients cover every class the same number of times. Let
\[
S_B=\sum_{2\le\deg P\le B}\deg P.
\]
The finite-field identity \(jI_j\le2^j\) implies \(S_B<2^{B+1}\). Since \(2^B\le d/(8L)\) and \(E\le L+1\),
\[
2ES_B<4E2^B\le\frac{L+1}{2L}d<d.
\]
The Chinese remainder theorem consequently makes \((f\bmod P^{2E})_{2\le\deg P\le B}\) exactly independent and uniform. Hence the full truncated vector \((J_{P,E})_P\) is **exactly** a product of Bernoulli laws with parameters \(\beta_{P,E}\).

**3. Quantitative approximation.** Couple each actual variable to its truncation using the same polynomial. By a union bound, the probability that any two differ is at most \(\sum_P Q_P^{-E}\). Coupling Bernoulli variables of parameters \(\beta_{P,E}\) and \(\beta_P\) costs a further \(\frac12\sum_P Q_P^{-E}\). Thus
\[
d_{\mathrm{TV}}\left(\mathcal L((J_P)_P),\bigotimes_P\mathrm{Bern}(\beta_P)\right)
\le\frac32\sum_{2\le\deg P\le B}2^{-E\deg P}.
\]
Since \(I_j\le2^j/j\le2^j\), the sum is at most
\[
\sum_{j=2}^{\infty}2^{-j(E-1)}
=\frac{2^{-2(E-1)}}{1-2^{1-E}}
\le\frac{4d^{-2}}{1-2^{1-E}}.
\]
For \(E\ge16\), multiplying by \(3/2\) gives strictly less than \(7d^{-2}\). Total-variation contraction under summation proves the corresponding statement for \(W_d\).

**4. Normal and zero laws.** The irreducible counting formula gives \(I_j=2^j/j+O(2^{j/2})\) for \(j\ge2\). Consequently \(I_j\beta_j=1/(2j)+O(2^{-j/2})\), and \(I_j\beta_j^2=O(2^{-j}/j)\). Harmonic summation yields the claimed estimates for \(\mu_B,v_B\). The sum of the third centered absolute moments of the independent Bernoulli variables is bounded by their total variance, so the classical Berry–Esseen inequality gives an error \(O(v_B^{-1/2})=O((\log B)^{-1/2})\). Total variation adds at most \(7d^{-2}\).

Finally let \(H_B=\prod_{j=2}^B(1-\beta_j)^{I_j}\). The series
\[
\sum_{j=2}^{\infty}\left(I_j\log(1-\beta_j)+\frac1{2j}\right)
\]
converges absolutely, with exponentially small tails. Since \(\sum_{j=2}^B j^{-1}=\log B+\gamma-1+O(B^{-1})\), exponentiating proves \(H_B=\mathfrak C B^{-1/2}(1+O(B^{-1}))\). The total-variation bound finishes the zero-probability assertion.

## Verification
The standalone `VERIFY.py` implements polynomial arithmetic in \(\mathbb F_2[T]\) independently of the asymptotic argument. It exhausts all \(1024\) monic polynomials of degree \(10\) for the irreducibles \(T^2+T+1\) and \(T^3+T+1\), obtaining the joint simple-pole obstruction frequencies \((0,0):840\), \((1,0):120\), \((0,1):56\), and \((1,1):8\), exactly as independent Bernoulli variables of probabilities \(1/8\) and \(1/16\) predict. It separately checks the double-pole trace formula on all \(12\) and \(56\) admissible completions for those two primes, with exactly half trace-one in each case. Finally, it independently evaluates the polynomial-prime product and \(\mathfrak C\). Run using `python3 VERIFY.py` with the standard Python library. These are finite checks, not proofs of the infinite limit.

## Relationship to prior work
Niedbala Giraudin (2026), Theorems 2–3, proves prime-local residue formulas and a reciprocity law, and conjectures a much broader global model for orthogonal multiplicity. The single-prime local conditional distributions used here are **not new**. The present result combines them with a degree-budgeted, growing Chinese-remainder window, a uniform total-variation estimate for higher prime powers, and a quantitative Gaussian and zero-obstruction law. It does not assert global independence: the original paper's reciprocity identity supplies a genuine relation among **all** prime-local residues when \(f\) is coprime to \(T(T+1)\). The 2020 survey on perfect linear complexity profiles and the relevant sections of Malagoli's 2017 thesis concern continued fractions, orthogonal multiplicity, and related existence results; neither inspected discussion states this mesoscopic local-obstruction distribution.

## Limitations
This theorem is about a **local differential-residue statistic**, not the proportion of polynomials with positive orthogonal multiplicity. In particular, the equivalence between vanishing of all local residues and positive orthogonal multiplicity is not assumed or proved; the 2026 paper identifies it as an unproved input. The Gaussian law covers irreducibles of degree at most \(B=\log_2d-O(\log\log d)\), not all prime divisors of \(f\). The available literature does not prove historical uniqueness; a general local-statistic theorem may imply the mesoscopic result. The complete original 1998 Blackburn paper was not available for direct full-text comparison, although its relevant statements are discussed in accessible later literature.

## References
1. D. Niedbala Giraudin, *The proportion of polynomials over F2 with positive orthogonal multiplicity*, arXiv:2610.02352, first posted 1 October 2026. https://arxiv.org/abs/2610.02352 .
2. J.-P. Allouche, G.-N. Han and H. Niederreiter, *Perfect linear complexity profile and Apwenian sequences*, Finite Fields Appl. 68 (2020), 101761; arXiv:2008.12160. https://arxiv.org/html/2008.12160v1 .
3. F. Malagoli, *Continued fractions in function fields: polynomial analogues of McMullen's and Zaremba's conjectures*, thesis (2017), especially sections 4.1 and 4.2.2; arXiv:1704.02640. https://arxiv.org/html/1704.02640v2 .
4. S. R. Blackburn, *Orthogonal sequences of polynomials over arbitrary fields*, J. Number Theory 68 (1998), 99–111, DOI:10.1006/jnth.1997.2201 (original full text not directly inspected).
