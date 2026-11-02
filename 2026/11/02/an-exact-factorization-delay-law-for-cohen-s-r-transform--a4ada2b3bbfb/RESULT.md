# An exact factorization-delay law for Cohen's R-transform

## Finding

Let \(q\) be an odd prime power and \(n\ge 2\). Choose uniformly a monic irreducible degree-\(n\) polynomial over \(\mathbb F_q\), and iterate Cohen's \(R\)-transform. Whenever the transform splits into two distinct irreducible degree-\(n\) factors, choose one of them by an independent fair coin; stop at the **first** irreducible transform of degree \(2n\). Let \(J\) be the number of reducible transforms before stopping. An exact finite divisor-sum probability generating function for \(J\) is given below. In particular, for every odd \(n\ge3\), \(\mathbb E[J]=1\) **exactly**, whereas for every even \(n\ge2\), \(\mathbb E[J]<1\).

Put \(e=\nu_2(q^n-1)\) and, for every divisor \(d\mid n\), put \(e_d=\nu_2(q^d-1)\) and \(o_d=(q^d-1)/2^{e_d}\). Define

\[
w_v(d)=\begin{cases}
o_d,&v=0,\\
2^{v-1}o_d,&1\le v\le e_d,\\
0,&v>e_d,
\end{cases}\quad
C_v=\frac1n\sum_{d\mid n}\mu(n/d)w_v(d),\quad
N=\frac1n\sum_{d\mid n}\mu(n/d)q^d.
\]

Here \(\mu\) is the Möbius function, and every \(C_v\) is a nonnegative integer. The full probability generating function, for \(|z|<2\), is

\[
\boxed{\mathbb E[z^J]=\frac1N\left(\sum_{v=1}^{e}C_vz^{e-v}+C_0\frac{z^e}{2-z}\right).}
\]

In particular, the geometric tail is exact:

\[
\Pr(J\ge e+t)=\frac{C_0}{N\,2^t}\qquad(t=0,1,2,\ldots).
\]

The mean also has the finite arithmetic formula

\[
\boxed{\mathbb E[J]=\frac{\displaystyle\sum_{d\mid n}\mu(n/d)(q^d-1)(e-e_d+1)}{\displaystyle\sum_{d\mid n}\mu(n/d)q^d}.}
\]

For even \(n=2^rm\), \(r\ge1\), \(m\) odd, and \(e'=\nu_2(q^{n/2}-1)\), this becomes

\[
\boxed{\mathbb E[J]=1-
\frac{(e-e')\displaystyle\sum_{u\mid m}\mu(u)(q^{n/(2u)}-1)}
{\displaystyle\sum_{d\mid n}\mu(n/d)q^d}<1.}
\]

## Assumptions and scope

The field has odd cardinality \(q\), possibly a nonprime prime power, and the input degree is \(n\ge2\). The initial polynomial is uniform among all \(N\) monic irreducibles of that degree. A failure means a reducible transform and entails one factorization; the fair-coin choice applies at **every** such failure. The process stops at the first doubling and makes no claim that subsequent transforms remain irreducible. This is a distribution over both the initial polynomial and the independent factor choices, not a worst-case bound or a deterministic branch-selection algorithm.

For a monic irreducible polynomial \(f\) of degree \(n\), Cohen's transform is

\[
f^R(X)=(2X)^n f\left(\frac{X+X^{-1}}2\right)\in\mathbb F_q[X].
\]

It is monic of degree \(2n\), and for \(n\ge2\), each reducible transform has exactly two *distinct* monic irreducible factors of degree \(n\).

## Proof

**1. Conjugacy and factor degrees.** Define the involution \(\psi(y)=(y+1)/(y-1)\) on the projective line, and \(\theta(x)=(x+x^{-1})/2\). Direct algebra gives \(\theta(\psi(y))=\psi(y^2)\). Let \(\beta\) be a root of the degree-\(n\) input polynomial and \(y=\psi(\beta)\). Since \(n\ge2\), \(\beta\notin\{1,-1\}\), so \(y\in\mathbb F_{q^n}^{\times}\) and has exact Frobenius degree \(n\). Roots \(\alpha\) of \(f^R\) satisfy \(\theta(\alpha)=\beta\), equivalently \(\psi(\alpha)^2=y\).

If \(y\) is not a square in \(\mathbb F_{q^n}\), every preimage has degree \(2n\) and \(f^R\) is irreducible. If \(y\) has square roots in \(\mathbb F_{q^n}\), each preimage has exact degree \(n\), because its image \(\beta\) has degree \(n\). The two preimages are reciprocal and cannot be conjugate over \(\mathbb F_q\): if a Frobenius power interchanged them, it would fix \(\beta\), and hence be a multiple of \(n\), in which case it could not interchange two distinct elements of \(\mathbb F_{q^n}\). Thus the two degree-\(n\) factors are distinct. These standard factor-degree facts are also established by Ugolini (2012), Theorem 2.8.

**2. Random-branch dynamics.** The cyclic group \(\mathbb F_{q^n}^{\times}\) has order \(2^e o_n\), with \(o_n\) odd. Let \(v\in\{0,\ldots,e\}\) be the two-adic valuation of the multiplicative order of \(y\). When \(v=e\), \(y\) is a nonsquare, so \(J=0\). When \(1\le v<e\), either of the two square roots has order with two-adic valuation \(v+1\): squaring lowers the nonzero valuation by one, and multiplication by \(-1\) does not alter valuation \(v+1\ge2\). Consequently the process has exactly \(e-v\) reducible stages, independent of coin choices.

When \(v=0\), the odd-order subgroup contains a unique square root of \(y\); the other square root has order with two-adic valuation one. Thus at each visit to \(v=0\), the next branch stays at \(v=0\) with probability \(1/2\) or escapes to \(v=1\) with probability \(1/2\). Once it escapes, it takes exactly \(e-1\) further reducible stages to reach \(v=e\). Therefore \(J=e+Z\), where \(\Pr(Z=j)=2^{-j-1}\), \(j\ge0\). In particular, termination is almost sure, even for initial periodic points.

**3. Exact-degree counts.** In \(\mathbb F_{q^d}^{\times}\), exactly \(o_d\) elements have odd multiplicative order, and exactly \(2^{v-1}o_d\) have order with two-adic valuation \(v\) when \(1\le v\le e_d\). All other level counts vanish. Möbius inversion over the subfields of \(\mathbb F_{q^n}\) counts elements of exact Frobenius degree \(n\) at valuation \(v\) as \(\sum_{d\mid n}\mu(n/d)w_v(d)\). Frobenius orbits have size \(n\), and the valuation is constant along each orbit, giving the integer \(C_v\). The total number of orbits is \(N\). Weight the conditional laws from step 2 by \(C_v/N\); the geometric generating function is \(\sum_{j\ge0}2^{-j-1}z^j=(2-z)^{-1}\). This proves the displayed probability generating function and its tail identity.

**4. Exact mean and parity distinction.** For a field \(\mathbb F_{q^d}\) with exponent \(e_d\), summing the conditional mean \(e-v+\mathbf1_{v=0}\) over all nonzero elements gives

\[
(q^d-1)(e-e_d+1).
\]

Indeed, in a cyclic group of order \(2^{e_d}o_d\), the average of \(v\) is \(e_d-1+2^{-e_d}\), and the probability of \(v=0\) is \(2^{-e_d}\). Möbius inversion restricted to exact Frobenius degree \(n\), then division by \(nN\), proves the finite mean formula.

If \(n\) is odd, each \(n/d\) is odd, hence \(e_d=e\), because \((q^n-1)/(q^d-1)\) is a sum of an odd number of odd terms. Since \(n>1\), \(\sum_{d\mid n}\mu(n/d)=0\). The numerator of the mean formula equals its denominator, proving \(\mathbb E[J]=1\).

If \(n=2^rm\) with \(m\) odd and \(r\ge1\), only terms with \(n/d=u\) or \(n/d=2u\), for squarefree odd \(u\mid m\), survive the Möbius sum. The corresponding valuations are \(e\) and \(e'=\nu_2(q^{n/2}-1)\), respectively. The displayed even-degree formula follows. The difference \(e-e'=\nu_2(q^{n/2}+1)>0\). Also, \(\sum_{u\mid m}\mu(u)(q^{n/(2u)}-1)>0\): when \(m=1\) it is \(q^{n/2}-1\), and otherwise it counts elements of exact degree \(m\) over \(\mathbb F_{q^{2^{r-1}}}\). The denominator counts all elements of exact degree \(n\) and is positive. Hence \(\mathbb E[J]<1\), as claimed.

## Verification

The accompanying `verify.py` uses SymPy over small prime fields to enumerate all monic irreducible polynomials at nine parameter pairs, independently factor each Cohen transform, check all two-factor branch transitions, and compare the exact valuation-level histogram and expected cost to the divisor formulas. It exhausts \(315\) initial irreducibles in these tested fields and additionally tests \(144\) parameter pairs with proper prime-power \(q\) by exact integer arithmetic. Run `python verify.py` with Python 3 and SymPy installed. These are finite checks; the infinite theorem follows from the proof above.

## Relationship to prior work

Ugolini (2012) proves the known Cohen-transform factorization dichotomy and deterministic finite-time escape using the graph of \(\theta\); these facts are not asserted to be new. Ugolini (2013) derives the complete field-level conjugacy and reversed-binary-tree structure, including the \(2^{v-1}\) counts at tree depth \(v\). Bassa and Menares (2019) generalize the conjugacy-to-power-maps construction. The present statement concerns **a new probability model and exact-degree ensemble**: the Möbius-inverted count of degree-\(n\) irreducible seeds, fair random branch choices, the resulting *entire* probability generating function, and the sharp odd-versus-even expectation law. The cited graph theorems provide ingredients; the claim is not that those graph or irreducibility theorems are new.

## Limitations

The law applies only to odd characteristic and input degree at least two. It measures the number of **reducible transforms** before the first successful degree doubling, not runtime in bit operations, total factorization time, a deterministic branch strategy, or indefinite persistence of irreducibility thereafter. The fair-coin rule is a specified probabilistic model, not a claim about typical software selection. The formula is an exact consequence of established finite-field dynamics plus new ensemble counting; older specialized probability calculations might still imply an equivalent formula, and independent mathematical validation is not available.

## References

1. S. Ugolini, *Sequences of irreducible polynomials without prescribed coefficients over odd prime fields*, arXiv:1207.6959v1 (2012-07-30), especially Theorems 2.8 and 3.1. https://arxiv.org/abs/1207.6959
2. S. Ugolini, *On the iterations of certain maps \(x\mapsto k(x+x^{-1})\) over finite fields of odd characteristic*, arXiv:1304.3283v1 (2013-04-11), especially Section 2 and Theorem 2.6. https://arxiv.org/abs/1304.3283
3. A. Bassa and R. Menares, *The R-transform as a power map and its generalisations to higher degree*, arXiv:1909.02608v1 (2019-09-05). https://arxiv.org/abs/1909.02608
