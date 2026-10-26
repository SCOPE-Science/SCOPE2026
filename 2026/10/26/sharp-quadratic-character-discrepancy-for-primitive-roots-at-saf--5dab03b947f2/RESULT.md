# Sharp quadratic-character discrepancy for primitive roots at safe primes

## Finding

Let \(p=2q+1\ge7\) be a safe prime, with \(q\) an odd prime; write \(\chi\) for the Legendre character on \(\mathbb F_p\), extended by \(\chi(0)=0\). Let \(Q(X)=aX^2+bX+c\) over \(\mathbb F_p\), with \(b^2-4ac\ne0\) and \((a,c)\ne(0,0)\). Let \(G_p\) denote the primitive roots modulo \(p\), and set
\[
S_p(Q)=\sum_{g\in G_p}\chi(Q(g)),\quad
R_p(Q)=\#\{g\in G_p:Q(g)=0\},\quad
T_p(Q)=\sum_{x\in\mathbb F_p}\chi(xQ(x)).
\]
Then the **exact identities**
\[
S_p(Q)=-\frac{\chi(a)+\chi(c)+T_p(Q)}2-\chi(Q(-1))
\]
and, for \(\varepsilon\in\{-1,1\}\),
\[
N_{\varepsilon}(Q)=\#\{g\in G_p:\chi(Q(g))=\varepsilon\}
=\frac{p-3-2R_p(Q)+\varepsilon[-\chi(a)-\chi(c)-T_p(Q)-2\chi(Q(-1))]}4
\]
hold. Uniformly,
\[
\boxed{|S_p(Q)|\le\lfloor\sqrt p\rfloor+2.}
\]
For every safe prime \(p\ge23\), both \(N_{1}(Q)\) and \(N_{-1}(Q)\) are positive, with the explicit bound
\[
N_{\varepsilon}(Q)\ge \frac{p-11-2\lfloor\sqrt p\rfloor}{4}>0.
\]
The existence threshold is exact among safe primes: for \(p=5,7,11\), the admissible polynomial \(Q(X)=X^2+X+1\) lacks at least one sign on the primitive roots. Moreover the uniform discrepancy constant \(\lfloor\sqrt p\rfloor+2\) is attained at \(p=23\) by \(Q(X)=X^2+X+4\), and at \(p=47\) by \(Q(X)=X^2+X+36\). In particular the safe-prime subfamily satisfies Sun's character-sum conjecture 4.8 and simultaneous-sign conjecture 4.9.

## Assumptions and scope

All congruences and characters refer to the finite field \(\mathbb F_p\). A *safe prime* is a prime of the form \(p=2q+1\) with \(q\) prime. The formulas above require \(q\) odd, thus \(p\ge7\). The two allowed polynomial types are separable quadratics (\(a\ne0\)) and nonconstant linear polynomials (\(a=0\), \(b\ne0\), \(c\ne0\)); allowing \(c=0\) is also covered when \(a\ne0\) and \(b\ne0\). Coefficient triples are understood modulo \(p\); multiplication of all coefficients by a nonzero scalar preserves the two-sign existence property but may exchange the signs. An element called a quadratic residue or nonresidue is always nonzero.

## Proof

**Step 1: primitive-root filter.** Since \(p-1=2q\) with \(q\) odd prime, the multiplicative group has \(q-1=(p-3)/2\) generators. Its nonzero quadratic nonresidues are precisely its elements of orders \(2\) and \(2q\); the unique element of order \(2\) is \(-1\). Therefore
\[
\mathbf1_{G_p}(x)=\frac{1-\chi(x)}2-\mathbf1_{x=-1}\qquad(x\in\mathbb F_p^\times).
\]
Writing \(T=\sum_x\chi(xQ(x))\), one obtains
\[
2S_p(Q)=\sum_{x\ne0}\chi(Q(x))-T-2\chi(Q(-1)).
\]

**Step 2: total quadratic sum.** The elementary discriminant-nonzero quadratic-character identity gives \(\sum_x\chi(Q(x))=-\chi(a)\) for \(a\ne0\). For \(a=0\), the hypothesis forces \(b\ne0\), and the sum is zero, which is also \(-\chi(a)\). Subtract the \(x=0\) term \(\chi(c)\). This proves the displayed identity for \(S_p(Q)\). Among \((p-3)/2\) primitive roots, exactly \(R_p(Q)\le2\) are zeros; since \(N_{1}+N_{-1}=(p-3)/2-R_p(Q)\) and \(N_{1}-N_{-1}=S_p(Q)\), the formula for \(N_{\varepsilon}\) follows.

**Step 3: the sharp square-root envelope.** If \(ac\ne0\), the cubic polynomial \(xQ(x)\) is squarefree, because \(Q(0)=c\ne0\) and the discriminant of \(Q\) is nonzero. Thus \(E:y^2=xQ(x)\) is a nonsingular elliptic curve over \(\mathbb F_p\), and \(T=\#E(\mathbb F_p)-(p+1)\). Hasse's theorem gives \(|T|\le2\sqrt p\). The rational point \((0,0)\) has order two, so \(\#E(\mathbb F_p)\) is even. As \(p+1\) is even, \(T\) is even and therefore \(|T|\le2\lfloor\sqrt p\rfloor\). As \(|\chi(a)|=|\chi(c)|=1\) and \(|\chi(Q(-1))|\le1\), the asserted bound follows.

If \(ac=0\), the hypotheses imply \(b\ne0\). For \(a=0\), \(xQ(x)=bx^2+cx\), whose complete character sum is \(-\chi(b)\). For \(c=0\), \(xQ(x)=x^2(ax+b)\), and summing over \(x\ne0\) again gives \(-\chi(b)\). In either case \(T=-\chi(b)\), hence the same bound follows (in fact \(|S_p(Q)|\le2\)).

**Step 4: existence and thresholds.** The number of nonzero values is \(H=(p-3)/2-R_p(Q)\ge(p-7)/2\); thus
\[
N_{\varepsilon}=\frac{H+\varepsilon S_p(Q)}2
\ge\frac{p-11-2\lfloor\sqrt p\rfloor}{4}.
\]
For \(p\ge23\) this lower bound is strictly positive and increases as \(p\) increases (for instance use \(\lfloor\sqrt p\rfloor\le\sqrt p\) and \(p-11-2\sqrt p>0\) for \(p\ge23\)). The three smaller safe primes \(5,7,11\) have the stated explicit counterexamples, verified by the elementary residue test. The examples at \(23\) and \(47\) have \(S_p(Q)=-6\) and \(-8\), respectively, meeting the envelope exactly.

For Sun's conjecture 4.8, for \(p\ge23\) the sharper derived bound implies \(|S_p(Q)|<\tfrac12\sqrt p\log p\), since \(\log p>2+4/\sqrt p\) at \(p=23\) and the difference is increasing thereafter. Sun's conjecture 4.9 on this safe-prime family follows from positivity of both counts.

## Verification

The standalone script `verify.py` uses exact integer arithmetic and independently tests primitive-root membership by multiplicative order. It checks all normalized separable quadratic and eligible linear coefficient triples over the ten safe primes at most \(179\), totaling \(84672\) triples. It checks the exact signed-count and sum identities for every eligible polynomial when \(p\ge7\), tests the discrepancy envelope and sign existence when \(p\ge23\), verifies the small-prime obstructions, and checks attainment at \(23\) and \(47\). The exhaustive finite check corroborates but does not replace Steps 1–4, especially the elliptic-curve bound.

To replay from the same directory, run `python3 verify.py`.

## Relationship to prior work

Zhi-Wei Sun introduced the polynomial character sum and formulated conjectures 4.8 and 4.9 in *New observations on primitive roots modulo primes* (arXiv:1405.0290, §4). Sun also established special linear-shift character-sum results, so the present linear specializations are not claimed independently novel. Booker, Cohen, Sutherland, and Trudgian's *Primitive values of quadratic polynomials in a finite field* (arXiv:1803.01435, Theorem 1) shows existence of a primitive input giving a primitive quadratic output outside an explicit exceptional list. For safe primes at least \(47\), applying their theorem to \(Q\) and \(-Q\) already implies the **two-sign existence conclusion for genuine quadratic polynomials**, because \(p\equiv3\pmod4\). The present contribution is instead the exact signed counting identity, the explicit uniform \(\lfloor\sqrt p\rfloor+2\) discrepancy bound and attainment, and the full safe-prime threshold including \(p=23\) and degenerate linear leading coefficient. The earlier existence theorem does not state those quantitative results. The character-sum mechanism uses standard Hasse/Weil theory; the originality claim is the precise specialized combined statement, not those general tools.

## Limitations

No claim is made about primes whose multiplicative groups have more than two distinct prime-order factors, about conjectures 4.8–4.9 for arbitrary primes, or about infinitely many safe primes. The value of \(T_p(Q)\) may still require a finite-field character sum or elliptic-curve point count. Related exact formulas may exist in unlocated literature. Independent mathematical audit has not been performed.

## References

1. Zhi-Wei Sun, *New observations on primitive roots modulo primes*, arXiv:1405.0290, especially §4, Conjectures 4.8–4.9. First public arXiv submission: 2014-04-21. https://arxiv.org/abs/1405.0290
2. Andrew R. Booker, Stephen D. Cohen, Nicole Sutherland, and Tim Trudgian, *Primitive values of quadratic polynomials in a finite field*, arXiv:1803.01435, Theorem 1 and §2. https://arxiv.org/abs/1803.01435
3. Hasse's bound for elliptic curves over finite fields (standard theorem, used in Step 3).
