# Quantitative dimension scale for Kusner counterexamples near p=4

## Statement

Let \(e(\ell_p^n)\) be the maximum cardinality of an equilateral subset of \(\ell_p^n\), and for \(p>4\) define the first failure dimension
\[
N(p):=\min\{n\ge 1:e(\ell_p^n)\ge n+2\}.
\]
Nathan Xiong proved that \(N(p)<\infty\) for every \(p>4\) by constructing \(8m\) equilateral points in \(\ell_p^{8m-2}\) with \(m\) a power of two.

The construction admits a Hadamard-order refinement. Define
\[
\Phi_p(a):=
\frac{2(a+1)^p+2(a-1)^p+4-2a^p-2^p}
{2^{p-1}(a^p+2)},
\qquad a\ge 1,
\]
and
\[
\Gamma(p):=\max_{a\ge1}\bigl(\Phi_p(a)-1\bigr).
\]
Then \(\Gamma(p)>0\) for every \(p>4\).

**Theorem 1 (Hadamard-order refinement).**
If a Hadamard matrix of order \(m\) exists and
\[
m\,\Gamma(p)\ge1,
\]
then there are \(8m\) equilateral points in \(\ell_p^{8m-2}\). In particular,
\[
N(p)\le 8m-2.
\]

**Theorem 2 (sharp near-\(4\) scale inside this template).**
As \(\varepsilon\downarrow0\),
\[
\Gamma(4+\varepsilon)
=
c\,\varepsilon+O(\varepsilon^2),
\]
where
\[
c=
\sqrt2\,\log(1+\sqrt2)-\frac74\log2
=
0.0334429143005567\ldots>0.
\]
Consequently Paley Hadamard matrices and the prime number theorem in arithmetic progressions give
\[
\boxed{
N(4+\varepsilon)
\le
\left(\frac8c+o(1)\right)\frac1{\varepsilon}
=
\frac{239.2136022627\ldots+o(1)}{\varepsilon}.
}
\]
Moreover, any member of the same one-parameter Hadamard construction must satisfy
\[
m\ge\frac1{\Gamma(4+\varepsilon)}
=
\left(\frac1c+O(\varepsilon)\right)\frac1\varepsilon.
\]
Thus the \(1/(p-4)\) order, and the continuous leading threshold \(1/c\) for the Hadamard order, are asymptotically optimal within this construction family.

Combining this with Swanepoel's quantitative stability theorem at \(p=4\) gives the global two-sided window
\[
\boxed{
\frac{8/\varepsilon}{W(8/\varepsilon)}-2
\le
N(4+\varepsilon)
\le
\left(\frac8c+o(1)\right)\frac1\varepsilon,
}
\]
where \(W\) is the principal Lambert \(W\)-function. Hence
\[
N(4+\varepsilon)
=
\Omega\!\left(\frac1{\varepsilon\log(1/\varepsilon)}\right)
\quad\text{and}\quad
N(4+\varepsilon)
=
O\!\left(\frac1\varepsilon\right).
\]

## Proof

### 1. Replacing the Sylvester matrix by an arbitrary Hadamard matrix

Let \(H\) be a normalized Hadamard matrix of order \(m\), so a distinguished column consists entirely of \(+1\)'s. Let \(H_4\) be the character table of \(\mathbb F_2^2\).

Xiong's four front vectors are
\[
q_{00}=(a,1,1,0),\quad
q_{10}=(-1,a,0,1),\quad
q_{01}=(-1,0,a,-1),\quad
q_{11}=(0,-1,1,a).
\]
Set
\[
R=a^p+2,\qquad
A=(a+1)^p+(a-1)^p+2,\qquad
B=2a^p+2^p.
\]
For distinct indices \(i,i'\in\mathbb F_2^2\), the quantities
\(\|q_i-q_{i'}\|_p^p\) and \(\|q_i+q_{i'}\|_p^p\) are both \(A\) when
\(i+i'\in\{10,01\}\), and both \(B\) when \(i+i'=11\).

Index the rows of \(H\) by \(s\). Replace Xiong's Walsh row in the front coordinates by the \(s\)-th row of \(H\):
\[
U_{i,s}=H_{s,:}\otimes q_i.
\]
For the back coordinates use the rows of \(H_4\otimes H\). In the distinguished column of \(H\), delete the \(00\) and \(11\) columns, scale the \(10\) and \(01\) columns by \(\beta\), and scale all remaining columns by \(\alpha\), where
\[
\alpha^p=\frac R4,\qquad
\beta^p=\frac{m(A-B)}{2^p}.
\]

Only the Hadamard orthogonality counts are needed in Xiong's distance calculation. Distinct rows of \(H\) agree in \(m/2\) positions and disagree in \(m/2\) positions. Distinct rows of \(H_4\otimes H\) disagree in \(2m\) positions. Because the distinguished column of \(H\) is constant, when the \(H_4\)-indices differ exactly two of the four distinguished-column entries disagree. For differences \(10\) or \(01\), one of those two entries is deleted and one is a \(\beta\)-entry; for difference \(11\), both are \(\beta\)-entries. Therefore the four pair types have the same counts as in Xiong's proof.

With
\[
2A-B=2^{p-1}R\left(1+\frac1m\right),
\tag{1}
\]
all pairwise \(p\)-th power distances are \(2^p mR\). Indeed, the two nontrivial cross-index cases both reduce to
\[
m(2A-B)+2^{p-1}(m-1)R
=
2^pmR
\]
by (1), while the equal-index cases give the same value directly.

Equation (1) is exactly
\[
\Phi_p(a)=1+\frac1m.
\]
For \(p>4\),
\[
\Phi_p(1)=\frac{2^p+2}{3\cdot2^{p-1}}<1,
\]
whereas Xiong's Lemma 4.1, evaluated at \(a_0=4^{1/p}\), gives \(\Phi_p(a_0)>1\). Thus \(\Gamma(p)>0\). If \(m\Gamma(p)\ge1\), continuity gives an \(a>1\) satisfying (1). This proves Theorem 1.

### 2. The optimized excess above \(1\)

At \(p=4\), direct simplification gives
\[
\Phi_4(a)
=
\frac{a^4+12a^2-4}{4(a^4+2)}
=
1-\frac{3(a^2-2)^2}{4(a^4+2)}.
\]
Hence \(a=\sqrt2\) is the unique global maximizer, with
\[
\Phi_4(\sqrt2)=1,\qquad
\partial_a\Phi_4(\sqrt2)=0,\qquad
\partial_a^2\Phi_4(\sqrt2)=-2.
\]
The limit as \(a\to\infty\) is \(2^{2-p}\), so for \(p\) near \(4\) the global maximizing point remains in a fixed compact interval. The nondegenerate maximum and the implicit-function theorem therefore give a unique nearby maximizer
\[
a_*(p)=\sqrt2+O(p-4),
\]
and the envelope expansion
\[
\Gamma(4+\varepsilon)
=
\partial_p\Phi_p(a)\big|_{(p,a)=(4,\sqrt2)}\,\varepsilon
+O(\varepsilon^2).
\]

Let \(t=1+\sqrt2\). At \((p,a)=(4,\sqrt2)\), the numerator and denominator of \(\Phi_p(a)\) both equal \(48\), while
\[
t^4-t^{-4}=24\sqrt2.
\]
Differentiating with respect to \(p\) at fixed \(a\) gives
\[
\partial_p\Phi_p(a)\big|_{(4,\sqrt2)}
=
\sqrt2\log(1+\sqrt2)-\frac74\log2
=:c.
\]
The constant is positive. For example, with \(u=\sqrt2-1\),
\[
\log(1+\sqrt2)
=
2\sum_{j\ge0}\frac{u^{2j+1}}{2j+1}
>
2\left(u+\frac{u^3}3+\frac{u^5}5\right),
\]
while
\[
\log2
=
2\sum_{j\ge0}\frac{3^{-(2j+1)}}{2j+1}
<
\frac{25}{36}.
\]
The resulting lower bound for
\(\sqrt2\log(1+\sqrt2)\) is \(>31/25\), whereas
\((7/4)\log2<175/144<31/25\).

This proves the expansion in Theorem 2.

### 3. Removing the dyadic rounding asymptotically

Paley's construction gives a Hadamard matrix of order \(q+1\) whenever
\(q\) is a prime congruent to \(3\pmod4\). The prime number theorem in arithmetic progressions implies that, for \(x\to\infty\), one can choose such a prime with
\[
q\ge x,\qquad q=(1+o(1))x.
\]
Take \(x=1/\Gamma(4+\varepsilon)\). Then there is a Hadamard order
\[
m=q+1
=
\frac{1+o(1)}{\Gamma(4+\varepsilon)}
=
\left(\frac1c+o(1)\right)\frac1\varepsilon.
\]
Theorem 1 gives
\[
N(4+\varepsilon)\le8m-2
=
\left(\frac8c+o(1)\right)\frac1\varepsilon.
\]

Conversely, equation (1) requires
\[
\frac1m=\Phi_p(a)-1\le\Gamma(p),
\]
so \(m\ge1/\Gamma(p)\) for every choice of \(a\) in this template. This proves the asserted template-optimal scale.

### 4. A global lower bound from stability at \(p=4\)

Swanepoel proved that
\[
|p-4|
<
\frac{4\log(1+2/n)}{\log(n+2)}
\quad\Longrightarrow\quad
e(\ell_p^n)=n+1.
\]
If \(n=N(4+\varepsilon)\), this forces
\[
\varepsilon
\ge
\frac{4\log(1+2/n)}{\log(n+2)}.
\]
Using \(\log(1+x)\ge x/(1+x)\) for \(x\ge0\),
\[
\varepsilon
\ge
\frac8{(n+2)\log(n+2)}.
\]
Writing \(y=n+2\) and inverting \(y\log y\) yields
\[
n\ge\frac{8/\varepsilon}{W(8/\varepsilon)}-2.
\]

## Context and originality

Xiong's September 2026 construction uses \(m=2^k\) and proves existence by taking \(m\) sufficiently large; its proof is stated with Sylvester/Walsh Hadamard matrices. Swanepoel's earlier theorem gives the explicit \(p=4\) stability interval in a fixed dimension. Chalmers gives a much smaller counterexample at \(p=5\), together with persistence on an unspecified open interval around \(5\), but it does not control the regime \(p\downarrow4\).

To the best of our knowledge, the arbitrary-Hadamard extension above, the optimized expansion of \(\Gamma(p)\), the asymptotic constant \(8/c\), and the resulting two-sided dimension window near \(p=4\) have not previously been recorded. Targeted searches for combinations of Kusner/Xiong, Hadamard/Paley, dimension bounds, and \(p-4\) did not locate an equivalent statement.

## Limitations

The upper bound concerns existence of a counterexample and is not claimed to determine the true first failure dimension \(N(p)\). The lower and upper bounds still differ by a logarithmic factor. The constant \(8/c\) is sharp only for the Hadamard version of Xiong's one-parameter construction, not among all possible equilateral configurations. The motivating all-\(p>4\) preprint is very recent, so unindexed parallel work remains a residual originality risk.

## References

1. N. Xiong, *Kusner's conjecture is false for \(p>4\)*, arXiv:2609.14794 (2026). https://arxiv.org/abs/2609.14794
2. K. J. Swanepoel, *Equilateral sets and a Schütte Theorem for the 4-norm*, Canadian Math. Bull. 57 (2014), 640--647; arXiv:1304.7033. https://arxiv.org/abs/1304.7033
3. L. R. Chalmers, *A counterexample to Kusner's conjecture on equilateral sets*, arXiv:2608.14013 (2026). https://arxiv.org/abs/2608.14013
4. R. E. A. C. Paley, *On Orthogonal Matrices*, J. Math. Phys. 12 (1933), 311--320. https://doi.org/10.1002/sapm1933121311
5. A. Selberg, *An elementary proof of the prime-number theorem for arithmetic progressions*, Canadian J. Math. 2 (1950), 66--78. https://doi.org/10.4153/CJM-1950-007-5
