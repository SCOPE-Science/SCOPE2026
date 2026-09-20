# A 2-adic trace criterion for parity cancellation in diagonal rational partitions

## Statement

Let
\[
C_N=\{a/b:1\le a\le N,\ 2\le b\le N,\ (a,b)=1\}
\]
and let \(A_N(z)\) be the residue numerator in the fixed-alphabet generating function of diagonal rational partitions,
\[
A_N(z)=\sum_{\substack{0\le r_{a/b}<b\\
\sum_{a/b\in C_N}(a/b)r_{a/b}\in\mathbb Z}}
z^{\sum_{a/b\in C_N}(a/b)r_{a/b}}.
\]
Put
\[
L_N=\operatorname{lcm}(1,\ldots,N)=2^v O,\qquad v=\lfloor\log_2N\rfloor,
\]
where \(O\) is odd, and set \(D=2^v\). Work in the negacyclic ring
\[
\mathcal R_D=\mathbb Z[x]/(x^D+1).
\]
For each even denominator \(b=2^t c\le N\), with \(c\) odd, and each \(1\le a\le N\) coprime to \(b\), define
\[
G_{a,b}(x)=\sum_{r=0}^{2^t-1}
 x^{\,2^{v-t}(O/c)ar}\in\mathcal R_D,
\]
and let
\[
P_N(x)=\prod_{\substack{2\le b\le N\\2\mid b}}
\prod_{\substack{1\le a\le N\\(a,b)=1}}G_{a,b}(x)
\equiv\sum_{j=0}^{D-1}c_j(N)x^j\pmod{x^D+1}.
\]
Finally put
\[
B_N=\prod_{\substack{3\le b\le N\\b\text{ odd}}}
 b^{\#\{2\le a\le N:a\text{ even},\ (a,b)=1\}}.
\]
Then
\[
\boxed{A_N(-1)=\frac{B_N}{O}\,c_0(N).}
\]
In particular,
\[
\boxed{A_N(-1)=0\iff c_0(N)=0.}
\]
Thus cancellation of the raw maximal parity pole can be decided inside a cyclotomic ring of degree only \(2^{\lfloor\log_2N\rfloor}\), without expanding the full residue numerator or summing over all \(L_N\) characters.

For \(N\ge5\), Raghava proved that \(M_N(2)\) is the unique maximum of the raw root-of-unity pole orders. Hence the criterion also gives
\[
A_N(-1)\ne0\Longleftrightarrow s_N=M_N(2),
\]
while a zero forces
\[
s_N\le M_N(2)-1.
\]

## The first case beyond the published table

For \(N=8\), \(D=8\) and \(O=105\). Grouping the factors of \(P_8\) by \(t=\nu_2(b)\) gives the exact reductions
\[
P_{8,1}(x)=8(1-x^4),\qquad
P_{8,2}(x)=8,
\]
\[
P_{8,3}(x)=8(-x^2+x^6)
\qquad\text{in }\mathbb Z[x]/(x^8+1).
\]
Therefore
\[
\boxed{P_8(x)=1024x^6},
\]
so \(c_0(8)=0\) and hence
\[
\boxed{A_8(-1)=0.}
\]
This is a new parity cancellation immediately after the published table \(3\le N\le7\), in which \(N=4\) was the only cancellation.

An independent exact bounded-residue computation gives
\[
\boxed{A_8'(-1)=-592704000\ne0,}
\]
so the zero at \(-1\) is simple. The denominator multiplicities are
\[
(c_8(1),\ldots,c_8(8))=(7,3,5,3,6,2,6,3),
\]
and
\[
(M_8(2),M_8(3),\ldots,M_8(8))=(11,7,6,6,2,6,3).
\]
Consequently the \(-1\) pole has order \(10\), all other nontrivial roots have pole order at most \(7\), and
\[
\boxed{s_8=10.}
\]
Thus for \(R_8(m)\), all coefficients of \(m^j\) with \(10\le j\le34\) are constant, while the coefficient of \(m^9\) is nonconstant.

The leading principal coefficient of \(H_8(z)\) at \(-1\) is
\[
\frac{A_8'(-1)}{
2^{\sum_{a\text{ odd}}c_8(a)}
\prod_{a\text{ even}}a^{c_8(a)}}
=-\frac{128625}{34359738368}.
\]
Since \([z^m](1+z)^{-10}=(-1)^m\binom{m+9}{9}\), the parity-dependent part of the coefficient of \(m^9\) in the quasipolynomial is exactly
\[
\boxed{-\frac{1225}{118747255799808}(-1)^m.}
\]

## Exact finite census

Applying the trace criterion with exact integer negacyclic arithmetic gives, for \(3\le N\le100\),
\[
\boxed{A_N(-1)=0\iff
N\in\{4,8,11,12,14,17,27,28,31,61,62,64\}.}
\]
The value \(N=4\) is the previously published cancellation. The remaining eleven values are additional exact cancellations. This finite census is not claimed to classify all \(N\), nor to imply that infinitely many cancellations occur.

## Proof of the trace criterion

For an assignment \(r=(r_{a/b})\), put
\[
S(r)=\sum_{a/b\in C_N}(a/b)r_{a/b}.
\]
Orthogonality of characters of \((L_N^{-1}\mathbb Z)/\mathbb Z\) gives
\[
A_N(-1)=\frac1{L_N}\sum_{j=0}^{L_N-1}
\prod_{a/b\in C_N}
\sum_{r=0}^{b-1}
\exp\!\left(2\pi i(j+\tfrac12)\frac{ar}{b}\right).
\]

Suppose first that \(a\) is even. Then \(b\) is odd, and the inner geometric sum is nonzero exactly when \(b\mid 2j+1\); in that case it equals \(b\). Because the coordinate \(2/b\) occurs for every odd \(b\le N\), all even-numerator coordinates together force
\[
O\mid 2j+1.
\]
The surviving characters are therefore exactly
\[
2j+1=Ok,
\]
where \(k\) runs over the odd residues modulo \(2D\).

For such a surviving character, an odd numerator with odd denominator contributes \(1\). If \(a\) is odd and \(b=2^tc\) is even, put
\[
\zeta=e^{\pi i/D}.
\]
The geometric ratio is
\[
q=\zeta^{2^{v-t}(O/c)ka},
\]
and \(q^{2^t}=-1\). Hence
\[
\sum_{r=0}^{b-1}q^r
=\frac2{1-q}
=\sum_{r=0}^{2^t-1}q^r.
\]
It follows that the product for the character indexed by \(k\) is
\[
B_NP_N(\zeta^k).
\]
The odd residues \(k\bmod 2D\) are precisely the Galois automorphisms of \(\mathbb Q(\zeta)\). Therefore
\[
A_N(-1)=\frac{B_N}{L_N}
\operatorname{Tr}_{\mathbb Q(\zeta)/\mathbb Q}(P_N(\zeta)).
\]
Reduce \(P_N\) modulo \(x^D+1\) as \(\sum_{j=0}^{D-1}c_j(N)x^j\). For a primitive \(2D\)-th root, the trace of \(1\) is \(D\), whereas
\[
\operatorname{Tr}(\zeta^j)=0\qquad(1\le j<D).
\]
Thus
\[
\operatorname{Tr}(P_N(\zeta))=Dc_0(N).
\]
Since \(L_N=DO\), the stated formula follows.

## Relation to prior work and originality scope

Raghava's September 2026 preprint introduces \(A_N(z)\), proves the root-of-unity pole criterion, shows that \(M_N(2)\) uniquely maximizes the raw pole order for \(N\ge5\), and explicitly tabulates \(A_N(-1)\) only for \(3\le N\le7\). In that table, \(N=4\) is the only cancellation. The accessible main text does not give a general criterion for \(A_N(-1)\), the \(N=8\) cancellation, the exact value \(s_8=10\), or a larger cancellation census.

The trace reduction uses standard finite Fourier projection and cyclotomic trace ideas. General Fourier--Dedekind and Ehrhart period-collapse literature supplies the surrounding language, but searches for the specific diagonal-rational-partition numerator, parity cancellation, the \(N=8\) evaluation, and equivalent root-of-unity formulations did not locate the result above. Originality is therefore claimed only to the best of our knowledge.

A relevant residual risk is the ancillary numerical material distributed with the motivating preprint. The accessible HTML states that an `anc/` directory contains a finite arithmetic certificate for its displayed small-\(N\) computations, but that source-archive material was not inspected here. It could contain broader computational machinery or additional unpublished evaluations. This does not affect the proof of the trace criterion or the exact verification above, but it limits the strength of the originality claim for the finite census.

## Limitations

The result isolates only the primitive second-root cancellation \(A_N(-1)\). It does not classify cancellations at other roots of unity, determine \(s_N\) for every cancellation index in the finite census, determine the least quasipolynomial period, or prove any infinite family of parity cancellations. The census is exact only for \(N\le100\). The exact computation is corroborative for the general trace formula and is part of the proof of the finite claims; it is not evidence for behavior beyond the checked range.

## Reproducibility

`artifacts/verify_parity_cancellation.py` uses only the Python standard library. It performs exact integer arithmetic in \(\mathbb Z[x]/(x^D+1)\), verifies the published values for \(3\le N\le7\), proves the displayed \(P_8\) reduction, independently computes \(A_8(-1)\) and \(A_8'(-1)\) from bounded residues, checks the \(N=8\) pole data and parity coefficient, and enumerates the exact cancellation set through \(N=100\). Its deterministic output is in `artifacts/verification.txt`.

## References

1. K. Srinivasa Raghava, *Arithmetic Constraints and Limit Laws for Diagonal Rational Partitions*, arXiv:2609.18945 (2026), https://arxiv.org/abs/2609.18945.
2. M. Beck and S. Robins, *Computing the Continuous Discretely*, 2nd ed., Springer (2015), https://doi.org/10.1007/978-1-4939-2969-6.
3. M. Beck, S. V. Sam and K. M. Woods, *Maximal periods of (Ehrhart) quasi-polynomials*, J. Combin. Theory Ser. A 115 (2008), 517--525, https://doi.org/10.1016/j.jcta.2007.05.009.
