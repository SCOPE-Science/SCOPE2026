# The first-repeat law identifies the atomic mass spectrum

## Statement

Let \(X_1,X_2,\ldots\) be iid with common probability law \(\mu\) on a standard Borel space, and let

\[
T=\inf\{n\ge 2:X_n\in\{X_1,\ldots,X_{n-1}\}\}
\]

be the first repeated-observation time. Write the positive atomic masses of \(\mu\), with multiplicity, as

\[
p_1,p_2,\ldots>0,\qquad \sum_i p_i\le 1,
\]

and put

\[
q=1-\sum_i p_i
\]

for the total nonatomic mass.

Then the distribution of the single stopping time \(T\) uniquely determines the multiset \(\{p_i\}\) and \(q\). Conversely, two probability laws have the same distribution of \(T\) if and only if they have the same multiset of positive atomic masses and the same nonatomic mass.

Thus first-repeat data identify the complete ranked atomic mass spectrum but do not identify atom locations or the shape of the nonatomic component.

More precisely, with

\[
a_n=\Pr(T>n),\qquad n\ge 0,
\]

the exponential generating function

\[
B(z)=\sum_{n\ge0}\frac{a_n}{n!}z^n
\]

has the exact factorization

\[
\boxed{B(z)=e^{qz}\prod_i(1+p_i z).}
\]

The product converges uniformly on compact subsets of \(\mathbb C\). Hence the nonzero atomic masses are recovered from the zeros of \(B\):

\[
\boxed{\{-1/p_i\}_i=\{\text{zeros of }B\}}
\]

with multiplicity.

## Collision-power equivalence

For \(r\ge2\), define the order-\(r\) collision probability

\[
C_r=\Pr(X_1=\cdots=X_r)=\sum_i p_i^r.
\]

Near the origin,

\[
\boxed{
\log B(z)
=
z+\sum_{r\ge2}(-1)^{r-1}\frac{C_r}{r}z^r.
}
\]

Therefore

\[
\boxed{
C_r=(-1)^{r-1}r[z^r]\log B(z),\qquad r\ge2.
}
\]

Consequently the full first-repeat law and the complete sequence of integer-order collision probabilities \(C_2,C_3,\ldots\) contain exactly the same information about the atomic mass partition.

## Finite-horizon corollary for finitely many atoms

Suppose only that \(\mu\) has at most \(m\) positive atoms; an arbitrary nonatomic component is still allowed. Then

\[
\boxed{a_0,a_1,\ldots,a_{2m+1}}
\]

already determine all atomic masses and \(q\).

Indeed, these survival probabilities determine \(C_2,\ldots,C_{2m+1}\). Introduce the finite positive measure

\[
\rho=\sum_i p_i^2\,\delta_{p_i},
\]

where equal atom masses combine. Its moments are

\[
\int x^k\,d\rho(x)=C_{k+2},\qquad k=0,\ldots,2m-1.
\]

If two models with at most \(m\) atoms have the same listed moments, the signed difference of their \(\rho\)-measures is supported on at most \(2m\) distinct points and has its first \(2m\) moments equal to zero. Restricting to the actual union support gives a square Vandermonde system, so every signed weight is zero. Thus \(\rho\) is unique. At each distinct mass \(x>0\), the multiplicity is recovered as

\[
\frac{\rho(\{x\})}{x^2},
\]

and \(q=1-\sum_i p_i\).

This is a sufficient finite horizon, not a claim of a minimal horizon.

For the purely discrete finite-support case \(q=0\), the familiar simplification is

\[
B(z)=\prod_{i=1}^m(1+p_i z),\qquad
a_n=n!\,e_n(p_1,\ldots,p_m),
\]

so the finite polynomial directly recovers the probabilities up to label permutation.

## Proof of the factorization

The event \(T>n\) is exactly the event that \(X_1,\ldots,X_n\) are all distinct. Suppose exactly \(k\) of the \(n\) observations fall on atoms. The \(k\) atomic observations must hit distinct atoms, which contributes

\[
k!\,e_k(p_1,p_2,\ldots).
\]

There are \(\binom nk\) choices of their positions. The other \(n-k\) observations fall in the nonatomic component with probability \(q^{n-k}\), and conditional on doing so are pairwise distinct almost surely. Therefore

\[
a_n
=
\sum_{k=0}^n
\binom nk k!\,e_k(p)\,q^{n-k}
=
\sum_{k=0}^n
\frac{n!}{(n-k)!}e_k(p)q^{n-k}.
\]

Taking the exponential generating function gives

\[
\begin{aligned}
B(z)
&=
\sum_{n\ge0}\sum_{k=0}^n
e_k(p)\frac{q^{n-k}z^n}{(n-k)!}\\
&=
e^{qz}\sum_{k\ge0}e_k(p)z^k\\
&=
e^{qz}\prod_i(1+p_i z).
\end{aligned}
\]

Since \(\sum_i p_i<\infty\), the product converges uniformly on compact sets. Also \(0\le a_n\le1\), so \(B\) is entire independently of the product representation.

The exponential factor has no zeros, while every factor \(1+p_i z\) contributes the zero \(-1/p_i\). Equality of first-repeat laws therefore implies equality of the entire functions \(B\), hence equality of their zero multisets and of the positive atom-mass multisets. The nonatomic mass then follows from normalization. The converse follows immediately from the displayed formula for \(a_n\).

Finally, expanding the logarithm for sufficiently small \(|z|\),

\[
\log B(z)
=
qz+\sum_i\log(1+p_i z)
=
\left(q+\sum_i p_i\right)z
+
\sum_{r\ge2}(-1)^{r-1}\frac{\sum_i p_i^r}{r}z^r,
\]

and \(q+\sum_i p_i=1\), proving the collision-power identity.

## Why the result is useful

A first-repeat experiment is a very severe data reduction: one keeps only one stopping time from an iid sequence and discards the repeated value, all labels, and all observations before it. Nevertheless, at the population-law level the complete distribution of that stopping time retains the entire discrete mass spectrum of an otherwise arbitrary mixed distribution.

The result also separates what repeat data can and cannot identify. Atomic probabilities and total dust mass are identifiable; atom locations and all structure internal to the nonatomic component are not. The logarithmic transform shows that first-repeat probabilities are an alternative encoding of all integer-order Rényi collision probabilities.

## Relation to prior work and originality boundary

The forward generalized-birthday problem is classical. Stein's 1990 technical report explicitly applies Newton identities to a generalized birthday problem, and Camarri and Pitman derive exact and asymptotic repeat-time formulas for unequal discrete probabilities. Newton identities and the fact that sufficiently many power sums determine a finite probability vector are not claimed here as new. Recent work on collision statistics also explicitly uses \(C_r=\sum_i p_i^r\) and notes finite-alphabet recovery from sufficiently many power sums.

The claim here is narrower: to the best of our knowledge, the complete inverse statement for an arbitrary probability law with both atoms and nonatomic mass was not found in the checked literature—namely that the one-dimensional law of the first-repeat time is a complete invariant for the atomic mass multiset plus dust, with the entire-function factorization above—and neither was the stated finite-horizon recovery bound for at most \(m\) atoms with arbitrary dust.

The strongest residual priority risk is Stein (1990): its title makes it especially plausible that part of the finite-discrete inversion is already explicit there. The report's bibliographic record was verified, but its full text was not available for theorem-level inspection. Camarri–Pitman (2000) was verified to study exactly the first-repeat problem for arbitrary countable discrete laws and to derive exact formulas; the accessible article record did not establish whether an inverse-identifiability corollary is stated. Accordingly, no novelty is claimed for the purely discrete Newton-identity algebra itself.

## Limitations

- This is structural identification from the full population distribution of \(T\), not a finite-sample statistical-rate result.
- Recovering distant zeros of an estimated entire generating function can be severely ill-conditioned, especially for very small or nearly equal atom masses.
- The nonatomic component is identified only through its total mass \(q\); its support, geometry and density are invisible to repeat events.
- The finite-horizon \(2m+1\) bound is sufficient and is not asserted to be optimal.
- The strongest older source likely to affect priority, Stein (1990), was not available for full theorem-level inspection.

## Reproducibility

`artifacts/verify_exact.py` uses only the Python standard library and exact rational arithmetic. It verifies the survival-factorization coefficients and the logarithmic recovery of \(C_2,\ldots,C_7\) for a mixed three-atom example, together with the finite purely discrete endpoint check. `artifacts/VERIFICATION.txt` records the verified output.

## References

1. C. Stein, *Application of Newton's Identities to a Generalized Birthday Problem and to the Poisson Binomial Distribution*, Stanford Department of Statistics Technical Report 354, 1990. https://statistics.stanford.edu/technical-reports/application-newtons-identities-generalized-birthday-problem-and-poisson-binomial
2. M. Camarri and J. Pitman, *Limit distributions and random trees derived from the birthday problem with unequal probabilities*, Electronic Journal of Probability 5 (2000), DOI: https://doi.org/10.1214/EJP.v5-58
3. M. Camarri, *Asymptotics for k-fold repeats in the birthday problem with unequal probabilities*, 1998 technical report / later Random Structures & Algorithms. https://statistics.berkeley.edu/tech-reports/524
4. M. Skorski, *Towards More Efficient Rényi Entropy Estimation*, Entropy 25 (2023), 185. https://doi.org/10.3390/e25020185
5. A. J. Gates, *Finite-Resolution Information from Collision Statistics*, Entropy 28 (2026), 882. https://doi.org/10.3390/e28080882
