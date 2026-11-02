# Odd posterior moments exactly classify information-mixing reversal for conjugate binary-input channels

## Finding

Let \(E\) be a finite alphabet, and let \(P,Q\) be arbitrary probability laws on \(E\). Set \(M=(P+Q)/2\) and define the posterior contrast \(z(x)=(P(x)-Q(x))/(P(x)+Q(x))\) at every \(x\) with \(M(x)>0\). Under \(X\sim M\), write \(Z=z(X)\). Thus \(Z\in[-1,1]\) and \(\mathbb E Z=0\).

Make two disjoint labeled copies \(E_A,E_B\) of \(E\). On the union, define experiment pairs \((P_1,Q_1)\) and \((P_2,Q_2)\) by placing \((P,Q)\) on \(E_A\) and \((Q,P)\) on \(E_B\), respectively, with zero mass on the other copy. Let \(\overline P=(P_1+P_2)/2\) and \(\overline Q=(Q_1+Q_2)/2\). With natural-log Jensen–Shannon divergence \(\operatorname{JS}\), the exact two-coordinate homogenization gap is

\[
\Delta(P,Q):=\operatorname{JS}(\overline P^{\otimes2},\overline Q^{\otimes2})-\operatorname{JS}(P_1\otimes P_2,Q_1\otimes Q_2)
=\sum_{j=1}^{\infty}\frac{\bigl(\mathbb E Z^{2j+1}\bigr)^2}{(2j)(2j+1)}\ge0.
\]

The series converges absolutely, including for singular \(P,Q\). Equality occurs **if and only if** the law of \(Z\) under \(M\) is symmetric under sign reversal. For a two-symbol alphabet, the gap is strictly positive exactly when \(P\ne Q\) and \(P(0)+Q(0)\ne1\), taking \(0\) as either one of the symbols.

Equivalently, for a fair binary input \(H\), let \(A\) observe \(P\) under \(H=0\) and \(Q\) under \(H=1\), while \(B\) uses the reversed conditional distributions. Let \(A'\) and \(B'\) denote conditionally independent copies. Then

\[
I(H;A,A')-I(H;A,B)=2\Delta(P,Q),
\]

so the repeated-channel strategy is never less informative than the conjugate-channel strategy and is strictly more informative under the same exact condition. This answers the conjugate-channel comparison for every finite output alphabet, including boundary probabilities.

For a weak-contrast family with \(P_\varepsilon(x)=M(x)(1+\varepsilon u(x))\), \(Q_\varepsilon(x)=M(x)(1-\varepsilon u(x))\), \(\mathbb E_M u=0\) and \(|\varepsilon|\|u\|_\infty\le1\), the gap has the expansion

\[
\Delta(P_\varepsilon,Q_\varepsilon)=\frac{\varepsilon^6}{6}\bigl(\mathbb E_Mu^3\bigr)^2+O_{M,u}(\varepsilon^{10}).
\]

In particular, if the cubic moment vanishes, later odd moments control the first possible nonzero order; exact symmetry makes every order vanish.

For the explicit pair \(P=(1,0)\), \(Q=(1/2,1/2)\), the gap is

\[
\Delta(P,Q)=\frac{12\log2-5\log5}{16}=\frac1{16}\log\left(\frac{4096}{3125}\right)>0.
\]

## Assumptions and scope

The alphabet is **finite and nonempty**. There are no full-support assumptions. Terms involving a zero probability are understood by the continuous convention \(0\log0=0\); \(z\) need only be defined on the support of \(M\). In the weak-contrast statement the reference law \(M\) is fixed, \(u\) is a fixed bounded function with mean zero, and \(\varepsilon\) tends to zero through values making both perturbed laws nonnegative. All logarithms are natural. Jensen–Shannon divergence uses equal mixing weights:

\[
\operatorname{JS}(R,S)=\tfrac12D\bigl(R\Vert(R+S)/2\bigr)+\tfrac12D\bigl(S\Vert(R+S)/2\bigr).
\]

No statement is asserted for unequal hypothesis priors, unequal pooling weights, arbitrary pairs of nonconjugate channels, or more than two pooled observations.

## Proof

**Step 1: information representation and the two correlation kernels.** Let \(H\) be uniform on \(\{0,1\}\), and let \(A,A',B,B'\) be conditionally independent given \(H\). Conditional on \(H=0\), the observations \(A,A'\) have law \(P\) and \(B,B'\) have law \(Q\); for \(H=1\), reverse those laws. The equal-prior identity \(\operatorname{JS}(R,S)=I(H;Y)\) holds when \(Y\mid H=0\sim R\) and \(Y\mid H=1\sim S\).

Write \(m(x)=M(x)\). The unconditional joint law of \((A,A')\) has density \(m(x)m(y)[1+z(x)z(y)]\) with respect to counting measure, whereas \((A,B)\) has density \(m(x)m(y)[1-z(x)z(y)]\). Both coordinate marginals are \(M\). For \(h(t)=(1+t)\log(1+t)\) on \([-1,1]\), with \(h(-1)=0\), set \(T=ZZ'\) for independent \(Z,Z'\) with the contrast law. Directly from the definition of mutual information,

\[
I(A;A')=\mathbb E h(T),\qquad I(A;B)=\mathbb E h(-T).
\]

**Step 2: a precise pooling identity.** Conditional independence and the entropy chain rule give, for any two observations \(X,Y\) conditionally independent given \(H\),

\[
I(H;X,Y)=I(H;X)+I(H;Y)-I(X;Y).
\]

In the conjugate setting \(I(H;A)=I(H;B)\). Consequently,

\[
I(H;A,A')-I(H;A,B)=I(A;B)-I(A;A').
\]

The tagged mixture experiment outputs \((J,Y)\), where \(J\) is an independent fair label choosing the \(A\) or \(B\) channel and \(Y\) is its observation. Conditional on the two labels in two independent repetitions, the mutual information equals \(I(H;A,A')\) for the two equal labels and \(I(H;A,B)\) for the two unequal labels. The labels themselves contain no information about \(H\). It follows that

\[
\operatorname{JS}(\overline P^{\otimes2},\overline Q^{\otimes2})=\tfrac12 I(H;A,A')+\tfrac12 I(H;A,B),
\]

while \(\operatorname{JS}(P_1\otimes P_2,Q_1\otimes Q_2)=I(H;A,B)\). Therefore

\[
\Delta(P,Q)=\tfrac12\mathbb E\bigl[h(-T)-h(T)\bigr].
\]

**Step 3: nonnegative odd-moment series.** The Taylor expansion, with a uniform and absolutely convergent tail on \([-1,1]\), is

\[
h(t)=t+\sum_{n=2}^{\infty}\frac{(-1)^n t^n}{n(n-1)}.
\]

Uniform convergence follows from \(\sum_{n\ge2}1/[n(n-1)]<\infty\). Since \(\mathbb EZ=0\), independence gives \(\mathbb ET=0\). Subtracting the expansions and taking expectations yields

\[
\tfrac12\mathbb E[h(-T)-h(T)]
=\sum_{j=1}^{\infty}\frac{\mathbb E T^{2j+1}}{(2j)(2j+1)}
=\sum_{j=1}^{\infty}\frac{(\mathbb E Z^{2j+1})^2}{(2j)(2j+1)}.
\]

Every coefficient and every square is nonnegative. This proves the exact identity and the claimed sign, including endpoint probabilities by uniform convergence.

**Step 4: all equality cases.** Equality forces every odd moment of \(Z\) of degree at least three to vanish; its degree-one odd moment already vanishes. Thus for every polynomial \(g\), \(\mathbb E g(Z)=\mathbb E g(-Z)\). By uniform polynomial approximation of continuous functions on \([-1,1]\), the laws of \(Z\) and \(-Z\) agree. Conversely a sign-symmetric law has zero odd moments and gives equality.

For a two-symbol alphabet, let \(m=M(0)\in(0,1)\) and let its two nonzero contrast values be \(a\) and \(b\). Centering requires \(ma+(1-m)b=0\). If the contrast is not identically zero, its two-point law is sign-symmetric precisely when \(m=1/2\) and \(b=-a\), equivalent to \(P(0)+Q(0)=1\). If the contrast is identically zero, \(P=Q\). If \(M\) is supported on one symbol, \(P=Q\) automatically. This completes the binary characterization.

**Step 5: weak contrasts and one exact example.** For \(P_\varepsilon=M(1+\varepsilon u)\), \(Q_\varepsilon=M(1-\varepsilon u)\), the mixture stays \(M\) and the contrast is \(Z=\varepsilon u(X)\). The series starts at order six, with next possible term of order ten. The absolute remainder is bounded by \(|\varepsilon|^{10}\|u\|_\infty^{10}\sum_{j\ge2}1/[(2j)(2j+1)]\) for \(|\varepsilon|\|u\|_\infty\le1\).

For \(P=(1,0)\) and \(Q=(1/2,1/2)\), direct enumeration of the two tagged product experiments gives \(\operatorname{JS}(P_1\otimes P_2,Q_1\otimes Q_2)=\tfrac12\log2\) and \(\operatorname{JS}(\overline P^{\otimes2},\overline Q^{\otimes2})=\tfrac54\log2-\tfrac5{16}\log5\). The difference simplifies to the displayed strictly positive logarithm because \(4096>3125\).

## Verification

The accompanying standalone `VERIFY.py` uses only the Python standard library, exact rational input probabilities and 75-digit decimal logarithms. It independently computes both Jensen–Shannon divergences by direct product enumeration, compares them with the mutual-information correlation-kernel identity for 164 rational law pairs, checks the binary equality and strictness regimes, verifies the exact illustrative logarithm, and tests the sixth-order limiting coefficient. The committed `VERIFICATION.log` reports 1321 passing assertions. Those calculations serve as finite checks and are **not** a proof of the all-alphabet identity, absolute convergence or equality classification; those follow from Steps 1–5.

To reproduce from the package directory, execute `python3 VERIFY.py` with Python 3.11 or newer. No online services, random external datasets or third-party dependencies are required; the random finite examples use a fixed pseudorandom seed.

## Relationship to prior work

Kontorovich's 2026 local-to-global framework addresses the existence of bounded homogenization constants for general \(f\)-divergences and identifies subclasses where constant one is optimal; it does not state this exact Jensen–Shannon parity series or the equality classification for conjugate channels. Kireeva and Mourrat's earlier mutual-information comparison supplies the conditional-independence identity used in Step 2 and gives concrete non-Gaussian failures, a low-signal expansion and numerical indications for reversed Bernoulli channels. Their inspected Section 2 does not establish the all-parameter binary classification or the arbitrary-alphabet odd-moment formula. In particular, the locus \(P(0)+Q(0)=1\) is a nonidentical equality family, so the strict comparison is not universal for every unequal binary channel.

The identified contribution is **the exact nonnegative series and complete equality boundary**, not the chain rule, the existence of non-Gaussian counterexamples or the sixth-power phenomenon by itself. Earlier unrelated disjoint-support Jensen–Shannon counterexamples also establish failure of constant-one homogenization but not the present conjugate-channel classification. Further unindexed information-theory identities remain a historical-priority risk.

## Limitations

The result neither determines the sharp *universal* Jensen–Shannon homogenization constant nor settles comparisons for arbitrary, nonconjugate channels. No independent proof review has been performed. Numerical checks do not certify the general identity. The self-contained argument applies to finite alphabets; extensions to arbitrary measurable channels are not asserted here. The earliest primary paper motivating the present homogenization comparison was posted 2026-10-22; the older information-mixing results are relevant prior work and are not claimed as new.

## References

- Aryeh Kontorovich, *A local-to-global principle for \(f\)-divergence homogenization*, arXiv:2610.31164v1, first public 2026-10-22, https://arxiv.org/html/2610.31164v1. Sections 1–2 and 6–7.
- Anastasia Kireeva and Jean-Christophe Mourrat, *Breakdown of a concavity property of mutual information for non-Gaussian channels*, arXiv:2304.05129v1, first public 2023-04-11, https://arxiv.org/pdf/2304.05129. Section 2, Lemma 2.2, the Bernoulli examples and Proposition 2.3; published in *Information and Inference* 13(2), 2024.
