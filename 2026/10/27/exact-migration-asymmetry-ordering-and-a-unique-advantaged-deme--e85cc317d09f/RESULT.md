# Exact migration-asymmetry ordering and a unique advantaged-deme optimum in a two-deme branching model

## Finding

Consider a supercritical, two-type Galton–Watson process in which a parent of type \(i\) produces independent Poisson numbers of children of types \(j=1,2\), with means \(\lambda M_{ij}\). Fix \(\lambda>1\) and \(0<s<2\). Define the column-stochastic matrix
\[
M=M_s(d)=\begin{pmatrix}
1-\frac{s-d}{2}&\frac{s+d}{2}\\
\frac{s-d}{2}&1-\frac{s+d}{2}
\end{pmatrix},\qquad |d|<\min\{s,2-s\}.
\]
Let \(q_i(d)\) denote the probability that a process initiated by one type-\(i\) individual survives forever, and let \(\bar q(d)=(q_1(d)+q_2(d))/2\) be the survival probability with uniformly randomly chosen initial type.

**Theorem (strict asymmetry ordering, optimal advantaged origin).** For all the parameters above, \(q_i(d)>0\), and \(\bar q(d)\) is an even, continuously differentiable function that is **strictly decreasing in \(|d|\)** for positive \(|d|\). Writing \(D(d)=\operatorname{diag}(1-q_1(d),1-q_2(d))\) and \(A(d)=I-\lambda D(d)M_s(d)\), its exact derivative is
\[
\boxed{\quad \bar q'(d)=\frac{\lambda(q_1+q_2)(q_2-q_1)}{4\det A(d)},\quad \det A(d)>0.\quad}
\]
For \(d>0\), the advantaged origin is type 1: \(q_1(d)>q_2(d)\).

In the **complete redistribution family** \(s=1\), a second, distinct phenomenon occurs for every \(\lambda>1\): \(q_1(d)\) has exactly one maximizer \(d_\ast\in(0,1)\), increasing strictly on \((0,d_\ast)\) and decreasing strictly on \((d_\ast,1)\), even though \(\bar q\) decreases throughout. The maximizing imbalance is explicit through a unique scalar root:
\[
\boxed{\quad x_\ast+\lambda e^{-x_\ast}=2\lambda-1-\log\lambda,\qquad x_\ast>\log\lambda,\qquad d_\ast=\frac{x_\ast-\log\lambda}{x_\ast+\log\lambda}.\quad}
\]
At that point \(q_2(d_\ast)=1-1/\lambda\) and \(q_1(d_\ast)=1-e^{-x_\ast}\).

There is also an exact local suppression curvature. If \(q_\circ\in(0,1)\) is the positive solution of \(q_\circ=1-e^{-\lambda q_\circ}\), \(p_\circ=1-q_\circ\), and \(z=\lambda p_\circ\in(0,1)\), then for fixed \(\lambda>1\) and \(s\in(0,2)\),
\[
\boxed{\quad\bar q(d)=q_\circ-\frac{\lambda^2q_\circ^2p_\circ}{2(1-z)[1-z(1-s)]^2}d^2+O_{\lambda,s}(d^4),\qquad d\to0.\quad}
\]
The strictly positive coefficient quantifies how rapidly equal initial-type establishment probability is lost near balanced migration.

## Assumptions and scope

There are exactly two reproductive types/demes. Conditional on a parent's type, offspring counts by destination type are independent Poisson variables and reproduction events of distinct individuals are independent. The matrix \(M_s(d)\) is strictly positive in its off-diagonal entries and nonnegative on the diagonal, with each column summing to one. Thus its Perron root is one. Both initial types have probability \(1/2\) when computing \(\bar q\). The parameter \(s\) is the sum of off-diagonal migration probabilities; \(d\) is their difference. The case \(s=1\) means both columns of \(M_s(d)\) are the same, so offspring destination choice is independent of parental type.

This is an **exact theorem for the infinite-population Poisson branching process**. Its use as an approximation to beneficial-mutant establishment in serial dilution requires additional biological regime assumptions. It does not assert an exact finite-population fixation probability.

## Proof

**1. Survival fixed point and its uniqueness.** Let \(F(q)=\mathbf1-\exp(-\lambda Mq)\), with the exponential componentwise. The vector of ultimate nonextinction probabilities is the unique strictly positive fixed point of
\[
q=F(q),\qquad q\in[0,1]^2.
\]
Since \(M\) is irreducible, nonnegative, and column stochastic, it has a strictly positive Perron vector \(v\) with \(Mv=v\). For sufficiently small \(\epsilon>0\), strict supercriticality gives \(F(\epsilon v)>\epsilon v\). Since \(F(\mathbf1)<\mathbf1\), monotone iteration between these bounds supplies a fixed point \(q\in(0,1)^2\). A positive fixed point is unique: if \(q,r>0\) were different fixed points, after interchanging them if needed choose \(t=\min_i q_i/r_i<1\). Then \(q\ge tr\), with equality in at least one coordinate, but strict concavity along positive rays gives \(F(q)\ge F(tr)>tF(r)=tr\), a contradiction at that coordinate. Standard multitype Galton–Watson extinction iteration yields this fixed point as the survival vector.

**2. The linearized fixed point is strictly stable.** Put \(D=\operatorname{diag}(1-q_1,1-q_2)\). The equation \(q=F(q)\) implies \(\lambda(Mq)_i=-\log(1-q_i)\), hence
\[
(\lambda DMq)_i=-(1-q_i)\log(1-q_i)<q_i
\]
for \(0<q_i<1\). Perron–Frobenius comparison therefore yields \(\rho(\lambda DM)<1\). In particular \(A=I-\lambda DM\) is invertible, \(A^{-1}\ge0\), and \(\det A>0\). The implicit-function theorem makes \(q\) smooth in the interior parameter \(d\).

**3. Exact sensitivity and strict total suppression.** Write \(u=(q_1+q_2)/2\), and note
\[
\frac{dM}{dd}=\frac12\begin{pmatrix}1&1\\-1&-1\end{pmatrix}.
\]
Differentiating the fixed-point equation gives
\[
A\begin{pmatrix}q_1'\\q_2'\end{pmatrix}
=\lambda u\begin{pmatrix}1-q_1\\-(1-q_2)\end{pmatrix}.
\]
A direct inversion of this \(2\times2\) system gives
\[
\begin{aligned}
\bar q'&=\frac{\lambda(q_1+q_2)(q_2-q_1)}{4\det A},\\
q_1'&=\frac{\lambda(q_1+q_2)(1-q_1)[1-\lambda(1-q_2)]}{2\det A},\\
q_2'&=-\frac{\lambda(q_1+q_2)(1-q_2)[1-\lambda(1-q_1)]}{2\det A}.
\end{aligned}
\]
Exchange of type labels takes \(d\) to \(-d\), so \(q_1(-d)=q_2(d)\). At \(d=0\), \(q_1=q_2=q_\circ\). The antisymmetric derivative at zero is strictly positive:
\[
q_1'(0)=-q_2'(0)=\frac{\lambda q_\circ p_\circ}{1-\lambda p_\circ(1-s)}>0.
\]
For nonzero \(d\), equality \(q_1=q_2>0\) would contradict the fixed-point equations because the row sums of \(M\) are \(1+d\) and \(1-d\). Continuity therefore implies \(q_1(d)>q_2(d)\) for every \(d>0\) in the admissible interval. The first sensitivity formula and \(\det A>0\) then yield \(\bar q'(d)<0\), and type symmetry proves the statement for \(|d|\).

**4. Sharp quadratic response.** Differentiate \(\bar q'\) at \(d=0\). There \(\det A=(1-z)[1-z(1-s)]\), and \(q_2-q_1=-2\lambda q_\circ p_\circ d/[1-z(1-s)]+O(d^3)\). Since \(\bar q\) is even and smooth, integration gives precisely the displayed \(d^2\) coefficient and an \(O(d^4)\) remainder.

**5. The uniquely optimal advantaged origin at complete redistribution.** Set \(s=1\), \(d\in(0,1)\). The columns of \(M\) coincide, and the equations simplify to
\[
q_1=1-e^{-\lambda(1+d)u},\qquad q_2=1-e^{-\lambda(1-d)u}.
\]
Because \(u>0\) and \(u'<0\), the product \((1-d)u\) is strictly decreasing; hence \(q_2\) decreases strictly from \(q_\circ\) to zero as \(d\uparrow1\). Put \(q_{\mathrm c}=1-1/\lambda\). The scalar relation for \(q_\circ\) and the inequality \(\lambda-1>\log\lambda\) show \(q_\circ>q_{\mathrm c}>0\). Thus \(q_2\) crosses \(q_{\mathrm c}\) exactly once. The formula for \(q_1'\) from Step 3 is positive above this crossing and negative below it; consequently the crossing is the unique global maximum of \(q_1\).

At the crossing, let \(x=\lambda(1+d)u\). The other exponent is \(\lambda(1-d)u=\log\lambda\), so \(2\lambda u=x+\log\lambda\). Also \(2u=q_1+q_2=2-e^{-x}-1/\lambda\). Equating yields \(x+\lambda e^{-x}=2\lambda-1-\log\lambda\), while \(x>\log\lambda\). On this interval the left-hand side is strictly increasing from \(1+\log\lambda\), whereas the right side exceeds that value by \(2(\lambda-1-\log\lambda)>0\); thus \(x_\ast\) exists and is unique. Finally, dividing the two exponents gives \(d_\ast=(x_\ast-\log\lambda)/(x_\ast+\log\lambda)\), as claimed. \(\square\)

## Verification

The accompanying `verify.py` implements fixed-point iteration for the survival vector, independently evaluates the implicit sensitivity formula against centered finite differences, checks type-exchange symmetry, and checks the scalar optimality equation. On the recorded test suite it returned `CHECK_OK 148`, covering 144 asymmetric parameter tests and four independent optimality tests. A separate symbolic calculation simplified the differentiated mean formula to \(\lambda(q_1+q_2)(q_2-q_1)/(4\det A)\). Neither finite precision nor a finite test grid replaces the proof.

As a concrete illustration, take \(\lambda=2\), \(s=1\). The scalar root is \(x_\ast\approx2.049168954104122\), so \(d_\ast\approx0.494480470870398\), with \(q_1(d_\ast)\approx0.871158067332034\), \(q_2(d_\ast)=0.5\). At symmetric migration the two survival probabilities both equal \(q_\circ\approx0.796812130020039\). The advantaged initial deme therefore has an interior optimum even as the uniformly averaged establishment probability falls below the balanced value.

## Relationship to prior work

Abbara and Bitbol's 2023 study derives the exact Poisson multitype generating function (their Eq. S25) for serial dilution in structured microbial populations. It proves circulation invariance and a **first-order-in-selection** suppression result for noncirculation graphs; Eqs. S59–S61 provide the star's leading weak-selection establishment probabilities. With two demes, their leading averaged formula is proportional to \(s^2/(s^2+d^2)\), consistent with the present strict-asymmetry theorem at weak selection. That formula does **not itself imply** the exact monotonicity for arbitrary \(\lambda>1\), the exact quadratic coefficient at fixed \(\lambda\), or the unique advantaged-origin optimum in the rank-one \(s=1\) family.

Czuppon, Blanquart, Uecker, and Débarre (2021) studied two habitat classes and nonmonotone mutant establishment under habitat-dependent selective growth and dispersal. Their nonmonotonic patterns concern differing habitat fitnesses and emigration intensity; they do not entail the present homogeneous-fecundity, fixed-total-migration, two-type Poisson theorem. These comparisons establish distinct mathematical statements, not absolute publication priority.

## Limitations

The theorem is restricted to two types, a shared reproduction multiplier, independently Poisson offspring, column-stochastic migration, and uniformly sampled initial type for the averaged result. The unique type-specific maximizer is proved for \(s=1\), not for every possible value of \(s\). The branching approximation can fail for finite demes, non-Poisson offspring, mutation during establishment, or the rare-migration regime. The theorem does not claim finite-population fixation, fixation times, or an all-deme version for more than two demes. Publication priority and independent validation are unresolved.

## References

1. A. Abbara and A.-F. Bitbol, *Frequent asymmetric migrations suppress natural selection in spatially structured populations*, arXiv:2306.10879, initial public submission June 19, 2023. Full text: https://arxiv.org/abs/2306.10879 (notably Eqs. S25, S59–S61 and Supplement §§3.4–3.5).
2. P. Czuppon, F. Blanquart, H. Uecker, and F. Débarre, *The Effect of Habitat Choice on Evolutionary Rescue in Subdivided Populations*, *The American Naturalist* 197 (2021), DOI:10.1086/714034, https://www.journals.uchicago.edu/doi/full/10.1086/714034.
3. American Mathematical Society, *MSC2020 Classification*, classification 92D15 (problems related to evolution), https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=92D15.
