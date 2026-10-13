# Liouville signs and a sharp affine prime test for a generalized Möbius recurrence

## Finding
For each integer \(c\ge1\), choose the affine input \(f_c(m)=1+c(m-1)\) in the generalized Möbius recurrence of Andrews, Kauffman, and Sahoo [1]. The resulting integer-valued function \(s_c\) admits an exact polynomial expansion in \(c-1\) whose coefficients enumerate ordered squarefree factorizations. The expansion gives both a Liouville-sign rule and a sharp fixed-function prime test: for all integers \(c\ge3\) and \(n\ge2\),
\[
s_c(n)=-1\quad\Longleftrightarrow\quad n\text{ is prime}.
\]
The positive integral slopes \(c=1\) and \(c=2\) fail this equivalence, so the integral threshold is sharp.

## Assumptions and scope
For an integer \(c\ge1\), define \(f_c(m)=1+c(m-1)\) for each positive integer \(m\). In particular \(f_c(1)=1\), so it is an admissible arithmetic input for [1]. Set \(s_c(1)=1\) and, for every integer \(n\ge2\),
\[
s_c(n)=1-n-\sum_{d=2}^{n-1}s_c(d)f_c\!\left(\left\lfloor\frac nd\right\rfloor\right).
\]
These values may be negative, so \(s_c\) is understood as integer-valued, as the displayed recurrence requires. Let \(\Omega(n)=\sum_{p\mid n}\nu_p(n)\), counting multiplicity. For \(r\ge1\), define \(N_r(n)\) as the number of ordered \(r\)-tuples \((d_1,\ldots,d_r)\) satisfying \(d_i>1\), \(d_i\) squarefree, and \(d_1\cdots d_r=n\). We study each \(n\ge2\) and every positive integer slope \(c\).

**Complete expansion.** For every such pair,
\[
\boxed{s_c(n)=(-1)^{\Omega(n)}\sum_{r=1}^{\Omega(n)}N_r(n)(c-1)^{r-1}.}
\]
In particular, if \(n=\prod_{i=1}^h p_i^{e_i}\), \(E=\max_i e_i\), and \(K=\sum_i e_i\), then
\[
N_r(n)=\sum_{j=0}^{r}(-1)^{r-j}\binom rj\prod_{i=1}^h\binom j{e_i},
\qquad N_E(n)=\prod_i\binom E{e_i},\qquad
N_K(n)=\frac{K!}{\prod_i e_i!}.
\]
Here a binomial coefficient with upper index smaller than the lower index is zero. Thus the polynomial \(s_c(n)\) has exact vanishing order \(E-1\) at \(c=1\). For every \(c\ge2\), its sign is \((-1)^{\Omega(n)}\). For every \(c\ge3\), it equals \(-1\) exactly at prime inputs.

## Proof
Write \(u(n)=1\) for the constant arithmetic function, \(\varepsilon(1)=1\) and \(\varepsilon(n)=0\) for \(n>1\), and let \(\mu\) be the classical Möbius function. Use \(*\) for Dirichlet convolution, so \(u*\mu=\varepsilon\).

**1. From floors to divisors.** Put
\[
A_c(n)=\sum_{d=1}^{n}s_c(d)f_c\!\left(\left\lfloor\frac nd\right\rfloor\right).
\]
The defining recurrence, including \(n=1\), gives \(A_c(n)=1-n+f_c(n)\). Thus \(A_c(n)-A_c(n-1)=c-1\) for \(n\ge2\). In this difference, for every \(d<n\), the floor changes only when \(d\mid n\), and then the affine input changes by exactly \(c\); the new \(d=n\) term contributes \(s_c(n)\). Consequently
\[
s_c(n)+c\sum_{d\mid n,\ d<n}s_c(d)=c-1,
\]
and, because \(s_c(1)=1\),
\[
\boxed{s_c(n)=-1-c\sum_{d\mid n,\ 1<d<n}s_c(d).}\tag{1}
\]
This derivation independently establishes the divisor recurrence and requires no primality assumption.

**2. Formal convolution identity.** Write \(t=c-1\) and \(L=\varepsilon-\mu\). Equation (1), together with the value at \(1\), is equivalent to
\[
s_c*\bigl(cu-(c-1)\varepsilon\bigr)
=(c-1)u+(2-c)\varepsilon.
\]
Convolving with \(\mu\), using \(u*\mu=\varepsilon\), gives
\[
s_c*(\varepsilon+tL)=\varepsilon+(t-1)L.
\]
As \(L(1)=0\), the convolution inverse of \(\varepsilon+tL\) has the coefficientwise finite geometric expansion \(\sum_{j\ge0}(-t)^jL^{*j}\), with \(L^{*0}=\varepsilon\). Therefore
\[
\boxed{s_c=\varepsilon-\sum_{r\ge1}(-t)^{r-1}L^{*r}.}\tag{2}
\]
For a fixed argument \(n\), no term with \(r>\Omega(n)\) can contribute, because \(L(1)=0\).

**3. Positive factorization coefficients.** For \(d>1\), the value \(L(d)=-\mu(d)\) vanishes unless \(d\) is squarefree, in which case \(L(d)=(-1)^{\Omega(d)+1}\). Thus every ordered factorization counted in \(L^{*r}(n)\) contributes the same sign \((-1)^{\Omega(n)+r}\). Substituting into (2) yields the complete expansion as stated. To count \(N_r(n)\), assign each of the \(e_i\) copies of prime \(p_i\) to distinct positions among \(r\) labelled factors. There are \(\prod_i\binom r{e_i}\) choices when empty factors are allowed. Inclusion-exclusion over empty positions gives the displayed formula for \(N_r(n)\).

A prime with exponent \(E\) cannot occupy fewer than \(E\) squarefree factors, so \(N_r(n)=0\) for \(r<E\). At \(r=E\), every factor contains every prime of exponent \(E\), so no factor is empty; assigning the other primes yields exactly \(\prod_i\binom E{e_i}\). At \(r=K\), every factor must be prime and the ordered number of assignments is \(K!/\prod_i e_i!\). Both numbers are positive. Hence the order at \(c=1\) is exactly \(E-1\), and the polynomial has sign \((-1)^{\Omega(n)}\) for \(c\ge2\).

**4. Sharp fixed-function prime detection.** If \(n\) is prime, the sole factorization has length one, so \(s_c(n)=-1\). Conversely let \(n\) be composite and \(c\ge3\). If \(K=\Omega(n)\) is even, \(s_c(n)>0\). If \(K\) is odd, then \(K\ge3\), and positivity of all coefficients together with \(N_K(n)\ge1\) gives
\[
|s_c(n)|\ge (c-1)^{K-1}\ge4.
\]
Thus no composite has value \(-1\). Finally, for a prime \(p\) and \(a\ge1\), the only nonzero factorization count is \(N_a(p^a)=1\), so \(s_c(p^a)=(-1)^a(c-1)^{a-1}\). In particular \(s_2(8)=-1\). For \(c=1\), the expansion reduces to \(s_1(n)=\mu(n)\); thus \(s_1(30)=-1\). Neither smaller positive integer slope is a prime test.

## Verification
Run the included standalone standard-library program `python3 verify.py`. It checks the original floor recurrence, the independently evaluated divisor recurrence (1), and the ordered-squarefree-factorization formula for \(1\le n\le300\) and five slopes \(c\in\{1,2,3,4,7\}\) (1,500 three-way comparisons). It also checks nonnegativity, minimal factor length, first nonzero coefficient, and top coefficient for \(2\le n\le2000\) (1,999 inputs). Finally it verifies both sharp boundary counterexamples. Exact integer arithmetic is used throughout. The recorded output is in `verify_output.txt`. These finite calculations are consistency checks; the infinite statements follow from the formal convolution proof.

## Relationship to prior work
Andrews, Kauffman, and Sahoo [1] introduce this arbitrary-input recurrence and prove its divisor reformulation; they do not specialize to affine inputs, exhibit the positive ordered-squarefree factorization polynomial, determine the vanishing order in slope, or prove a fixed admissible nonconstant function detects primes. The reverse-direction argument in [1] changes quantification from a fixed input to a statement about all admissible inputs, so that argument alone does not imply the fixed-function theorem above.

The published note [2] identifies the constant-one input as a counterexample to an unrestricted fixed-function interpretation; it explicitly leaves nonconstant-function prime criteria untreated. Our result instead proves a complete positive family and a sharp threshold inside the canonical affine family. The Dirichlet-convolution identities used in the proof are classical [3]. Searches for affine, convolutional, factorization-polynomial, and equivalent fixed-function formulations found no statement covering the combined theorem. Such negative search evidence is not a uniqueness certificate.

## Limitations
The proven fixed-function prime test is for the stated affine integer slopes \(c\ge3\), not every admissible arithmetic input. The polynomial factorization identity holds for every positive integer slope \(c\), and the formal argument extends algebraically to other scalar slopes, but no classification of all admissible nonlinear inputs is claimed. Direct evaluation of \(s_c(n)\) is not asserted to outperform standard primality algorithms. Unindexed equivalent derivations remain possible.

## References
1. G. E. Andrews, L. H. Kauffman, D. Sahoo, *A surprising generalization of the Möbius function*, arXiv:2609.25628v1, first submitted 2026-09-22; especially the defining recurrence, Proposition 1, and proof of Theorem 1. Full text: https://arxiv.org/html/2609.25628v1.
2. *A constant-function obstruction to a generalized Möbius primality criterion*, publicly accessible research note: https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-constant-function-obstruction-to-a-generalized-m-bius-primalit--e1be936699e5. Its result treats the constant-one input, not the affine positive-slope classification.
3. Standard Möbius inversion and Dirichlet convolution, \(u*\mu=\varepsilon\), e.g. https://en.wikipedia.org/wiki/Dirichlet_convolution.
