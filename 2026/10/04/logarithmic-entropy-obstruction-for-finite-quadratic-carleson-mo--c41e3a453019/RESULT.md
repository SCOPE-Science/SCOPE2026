# Logarithmic entropy obstruction for finite quadratic Carleson modulation sets

## Finding

For a finite set
\[
\Theta\subset 2^{\mathbb Z},
\]
define
\[
\mathcal C_{2,\Theta}f(x)
=
\max_{\lambda\in\Theta}
\left|
\operatorname{p.v.}\int_{\mathbb R}
f(x-t)e^{2\pi i\lambda t^2}\frac{dt}{t}
\right|.
\]

There is an absolute constant \(c>0\) such that, for every sufficiently large integer \(M\), one can choose \(\Theta_M\) to be a block of exactly \(M\) consecutive dyadic modulation parameters and choose a nonnegative function
\[
f_M\in C_c^\infty(\mathbb R),
\qquad
\|f_M\|_{L^1}=1,
\]
for which
\[
\left|
\left\{
x:
\mathcal C_{2,\Theta_M}f_M(x)
\ge
c\frac{\log M}{\sqrt M}
\right\}
\right|
\ge
c\sqrt M.
\]

In particular,
\[
\|\mathcal C_{2,\Theta_M}\|_{L^1\to L^{1,\infty}}
\ge
c\log M.
\]
Hence
\[
\sup_{\substack{\Theta\subset 2^{\mathbb Z}\\|\Theta|=M}}
\|\mathcal C_{2,\Theta}\|_{L^1\to L^{1,\infty}}
\gtrsim
\log M.
\]

Thus the endpoint obstruction for the lacunary quadratic Carleson operator is already finite-dimensional in its modulation parameter: weak-\(L^1\) constants for \(M\)-point dyadic modulation sets cannot be uniformly bounded and must grow at least logarithmically.

## Assumptions and scope

For a fixed modulation parameter,
\[
\mathcal C_2^\lambda f(x)
=
\operatorname{p.v.}\int_{\mathbb R}
f(x-t)e^{2\pi i\lambda t^2}\frac{dt}{t}.
\]
The finite maximal operator is
\[
\mathcal C_{2,\Theta}f
=
\max_{\lambda\in\Theta}|\mathcal C_2^\lambda f|.
\]

The weak norm is
\[
\|F\|_{L^{1,\infty}}
=
\sup_{\alpha>0}
\alpha
\left|
\{x:|F(x)|>\alpha\}
\right|.
\]

The result is a lower bound only. It does not claim that the optimal \(M\)-parameter weak-\(L^1\) growth is exactly logarithmic. In particular, it does not close the gap with the square-logarithmic finite-maximal estimate that appears for the oscillatory truncations in the motivating paper.

## Proof

Fix the positive smooth function \(\varphi\) used in the lower-bound construction of Fragkos, Krause, and Lacey, normalized by
\[
\int_{\mathbb R}\varphi=1
\]
and supported in a fixed compact interval about the origin.

For a large integer \(N\), their construction uses the intervals
\[
Q_j
=
j+
2^{-Nj}
\left[-\frac12,\frac12\right],
\qquad
1\le j\le N,
\]
and the nonnegative test function
\[
\chi_N
=
\frac1N
\sum_{j=1}^N
\varphi_{Q_j}.
\]
Every packet has integral one, so
\[
\|\chi_N\|_{L^1}=1.
\]

The proof of the source lower theorem does not need all dyadic modulation parameters. It explicitly restricts to the finite block
\[
\Theta_N^0
=
\left[
A_1^{-1}2^{N^2/2},
A_1 2^{3N^2/4}
\right]
\cap
2^{\mathbb N},
\]
where \(A_1>1\) is an absolute constant fixed in that proof.

For these parameters the source decomposes the action of
\[
\mathcal C_2^\lambda\chi_N
\]
into a stationary harmonic-sum main term and uniformly controlled errors. It then constructs a set \(E_N\), obtained from translated unions of Bohr sets, with
\[
|E_N|\gtrsim N.
\]
For every \(x\in E_N\), a parameter
\[
\lambda_0\in\Theta_N^0
\]
is chosen so that the phases in the long harmonic sum are nearly constant. The resulting estimate is
\[
\left|
\frac1N
\sum_{j=k+1}^N
\frac{e(2\lambda_0jx)}{x-j}
\right|
\gtrsim
\frac{\log N}{N}.
\]
The source's stationary and oscillatory error estimates are chosen smaller than a fixed fraction of this quantity. Therefore the same proof gives the finite-parameter statement
\[
\inf_{x\in E_N}
\max_{\lambda\in\Theta_N^0}
|\mathcal C_2^\lambda\chi_N(x)|
\gtrsim
\frac{\log N}{N}.
\]

Consequently,
\[
\left|
\left\{
x:
\mathcal C_{2,\Theta_N^0}\chi_N(x)
\gtrsim
\frac{\log N}{N}
\right\}
\right|
\gtrsim
N,
\]
and, since
\[
\|\chi_N\|_1=1,
\]
one gets
\[
\|\mathcal C_{2,\Theta_N^0}\|_{L^1\to L^{1,\infty}}
\gtrsim
\log N.
\]

The cardinality of the finite source block satisfies
\[
|\Theta_N^0|\asymp N^2,
\]
because it contains all dyadic powers in an exponent interval of length
\[
\frac14N^2+O(1).
\]

Now fix a sufficiently large integer \(M\). Choose
\[
N=\lfloor\sqrt M\rfloor.
\]
For large \(M\),
\[
|\Theta_N^0|\le M.
\]
Enlarge \(\Theta_N^0\), if necessary, to a block \(\Theta_M\) of exactly \(M\) consecutive dyadic powers. Enlarging the modulation set can only increase the pointwise maximum. Since
\[
N\asymp\sqrt M
\]
and
\[
\log N\asymp\log M,
\]
the preceding level-set estimate becomes
\[
\left|
\left\{
x:
\mathcal C_{2,\Theta_M}\chi_N(x)
\gtrsim
\frac{\log M}{\sqrt M}
\right\}
\right|
\gtrsim
\sqrt M.
\]
Taking
\[
f_M=\chi_N
\]
proves the finding.

## Verification

The proof is a quantitative extraction from the finite block already used inside the primary lower-bound argument.

Three points were checked independently.

First,
\[
\|\chi_N\|_1=1
\]
is exact because every packet is nonnegative and has integral one.

Second, the modulation set used in the source proof is finite before the final supremum is compared with the full lacunary operator. Its logarithmic exponents range from
\[
N^2/2+O(1)
\]
to
\[
3N^2/4+O(1),
\]
so its cardinality is
\[
N^2/4+O(1).
\]

Third, the Bohr-set union has measure comparable from below to \(N\), while the selected harmonic sum has size comparable from below to
\[
(\log N)/N.
\]
Multiplication of level and measure therefore gives the weak-\(L^1\) lower scale
\[
\log N.
\]

No infinite limiting argument is used to obtain the finite-family bound, and no numerical experiment is used as evidence.

## Relationship to prior work

Fragkos, Krause, and Lacey prove that the lacunary quadratic Carleson operator fails every modular estimate below the scale
\[
t\log_2 t,
\]
and in particular is not of weak type \((1,1)\). Their proof uses a finite interval of dyadic modulations at each construction scale, but the paper states the conclusion for the infinite lacunary supremum rather than as a cardinality-dependent weak-\(L^1\) lower bound.

The same paper also proves a square-logarithmic weak-\(L^1\) estimate for a finite maximal operator built from uniformly sparse-controlled oscillatory truncations. That estimate makes modulation cardinality an explicit parameter on the positive side. The finding here supplies the complementary lower entropy obstruction for the actual quadratic modulation family: at least one logarithm in the number of parameters is unavoidable.

Earlier quadratic and polynomial Carleson results establish boundedness in reflexive \(L^p\) ranges and do not provide this finite-cardinality endpoint lower law. Searches using finite modulation, modulation entropy, consecutive dyadic blocks, weak-\(L^1\) growth, and the source identifier did not locate a published statement of the logarithmic finite-family lower bound.

## Limitations

The result does not determine the exact optimal finite-family growth. It proves
\[
\gtrsim\log M
\]
and nothing stronger.

The lower-bound family consists of consecutive dyadic modulation parameters. The result therefore gives a worst-case finite-family obstruction, not a lower bound for every \(M\)-point modulation set.

The proof is tied to the explicit Bohr-set wave-packet construction for the purely quadratic phase. No analogous finite-entropy law is claimed here for general polynomial phases.

## References

1. A. Fragkos, B. Krause, and M. Lacey, *Endpoint Estimates for Stein's Purely Quadratic Carleson Operator*, arXiv:2609.04101v2, 2026.
2. V. Lie, *The weak-\(L^2\) boundedness of the quadratic Carleson operator*, Geometric and Functional Analysis 19 (2009), 457--497.
3. J. P. G. Ramos, *The Hilbert transform along the parabola, the polynomial Carleson theorem and oscillatory singular integrals*, Mathematische Annalen 379 (2021), 159--185.
