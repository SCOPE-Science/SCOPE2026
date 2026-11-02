# Sharp dyadic vanishing boundary for the quadratic generalized Möbius recurrence

## Finding
Let \(s(1)=1\), and for every integer \(n\ge2\) define the quadratic generalized Möbius sequence by
\[
s(n)=1-n-\sum_{d=2}^{n-1}s(d)\left\lfloor\frac nd\right\rfloor^{2}.
\]
For every odd integer \(m\ge1\), write its prime factorization as \(m=\prod_{i=1}^{r}p_i^{e_i}\), with distinct odd primes \(p_i\), positive \(e_i\), and \(k=\Omega(m)=\sum_i e_i\). For \(m=1\), use the empty product and \(k=0\). Then, for every integer \(a\ge k+3\),
\[
\boxed{s(2^a m)=0,}
\]
and the immediately preceding dyadic layer is exactly
\[
\boxed{s(2^{k+2}m)=2^{k+1}\frac{k!}{\prod_i e_i!}\prod_i(p_i-1)^{e_i}>0.}
\]
In particular, the stated eventual-zero threshold is sharp for every fixed odd part \(m\).

## Assumptions and scope
The sequence uses the admissible input \(f(t)=t^2\) in the generalized Möbius recurrence of Andrews, Kauffman and Sahoo. All integers and arithmetic functions are over \(\mathbb Z\). The theorem applies to every odd \(m\ge1\), including \(m=1\), and to the specified powers of two without a size restriction. The theorem does **not** classify earlier nonzero/zero values or all zeros of \(s\).

## Proof
Let \(*\) denote Dirichlet convolution, \(\varepsilon\) the identity arithmetic function supported at \(1\), \(\mathbf 1(n)=1\) for every positive integer, and \(g(n)=2n-1\). The defining floor recurrence, written at \(n\) and at \(n-1\) and subtracted, gives the equivalent divisor recurrence
\[
s(n)=-1-\sum_{\substack{d\mid n\\1<d<n}}s(d)(2n/d-1)\qquad(n\ge2).
\]
Indeed, for \(d\ge2\), the floors at \(n/d\) and \((n-1)/d\) differ exactly when \(d\mid n\), in which case their squares differ by \(2n/d-1\). Thus
\[
s*g=g+\varepsilon-\mathbf 1,
\qquad s=\varepsilon+(\varepsilon-\mathbf 1)*g^{*-1}.
\]
The inverse exists over the integers since \(g(1)=1\).

Regard an arithmetic function on positive integers as a formal power series in \(t\), whose coefficient at \(t^a\) is its restriction to odd integers after substituting the argument \(2^a m\). Coefficients lie in the Dirichlet-convolution ring of integer-valued functions on odd positive integers. In that ring write \(E\) for the convolution identity, \(U(m)=1\), and \(I(m)=m\). The series corresponding to \(g\) is
\[
G(t)=\sum_{a\ge0}(2^{a+1}I-U)t^a
=\frac{2I}{1-2t}-\frac U{1-t}
=\frac{H+tJ}{(1-2t)(1-t)},
\]
where \(H=2I-U\) and \(J=2(U-I)\). Crucially \(H(1)=1\), whereas \(J(1)=0\). Dirichlet inversion gives
\[
(H+tJ)^{*-1}=\sum_{j\ge0}(-t)^j J^{*j}*H^{*-(j+1)}.
\]
This is a purely formal identity; all coefficients at a fixed positive integer are finite divisor sums.

The series corresponding to \(s\), with the all-ones function represented by \(U/(1-t)\), is
\[
S(t)=E+\big[(E-U)+(2U-3E)t+2Et^2\big](H+tJ)^{*-1}.
\]
Here products of coefficient arithmetic functions are Dirichlet convolutions. Since \(J(1)=0\), a nonzero term in \(J^{*j}(m)\) requires a factorization of \(m\) into \(j\) integers greater than one. Hence \(J^{*j}(m)=0\) for \(j>\Omega(m)=k\). The coefficient of \(t^a\) at odd part \(m\) in \(S(t)\) consequently vanishes whenever \(a>k+2\), proving the first formula.

For \(a=k+2\), only the highest-degree term \(2Et^2\) contributes. Its value is \(2(-1)^k J^{*k}*H^{*-(k+1)}(m)\). Because \(\Omega(m)=k\), every one of the \(k\) factors supplied by \(J\) must be prime, and every factor supplied by the inverses of \(H\) must be \(1\). Thus
\[
J^{*k}(m)=\frac{k!}{\prod_i e_i!}\prod_i\bigl(2(1-p_i)\bigr)^{e_i}.
\]
Multiplying by \(2(-1)^k\) yields exactly the positive boundary formula. For \(m=1\), \(k=0\), the same calculation reads \(s(4)=2\) and \(s(2^a)=0\) for all \(a\ge3\). This proves the claim in every case.

## Verification
The standalone `verify.py` uses exact integer arithmetic. It evaluates the independent divisor recurrence through \(n=16384\), cross-checks the original floor recurrence through \(n=512\), and tests the asserted positive boundary for every odd part whose boundary is at most \(16384\). It also tests every zero-tail entry within that bound. Run `python3 verify.py` in a directory containing this file. Representative values are \(s(4)=2\), \(s(24)=8\), \(s(144)=32\), and \(s(240)=128\), with all corresponding next dyadic layers zero. The code is finite corroboration; the formal-convolution argument proves the infinite theorem.

## Relationship to prior work
Andrews, Kauffman and Sahoo introduced the generalized floor recurrence and proved a universal prime-value statement; their Proposition 1 yields the divisor reformulation used here. They displayed formulas at prime squares and products of two primes. Their inspected six-page original preprint does not state the sharp dyadic vanishing region, its dependence on \(\Omega(m)\), or the positive factorial boundary value. The contribution here is the all-odd-part dyadic classification of the eventual-zero threshold and its exact final nonzero layer, rather than the definition of the sequence, prime values, or the divisor-recurrence identity.

## Limitations
No classification is claimed for values at earlier dyadic exponents; sporadic zeros before the sharp boundary are possible and are not excluded. The conclusion concerns only the quadratic input \(f(t)=t^2\), not arbitrary generalized Möbius inputs. Targeted primary-literature, indexed-research and sequence-table searches did not locate a prior equivalent result, but unindexed or unpublished derivations may exist; such search results are not a proof of priority. No external or independent audit has been performed.

## References
1. G. E. Andrews, L. H. Kauffman, D. Sahoo, *A surprising generalization of the Möbius function*, arXiv:2609.25628v1 (first publicly posted 2026-09-22), especially (1), Proposition 1, and Theorem 1. https://arxiv.org/abs/2609.25628v1
2. OEIS A349358, *Dirichlet inverse of A064216* (a distinct sequence included in a targeted inverse-sequence search). https://oeis.org/A349358
