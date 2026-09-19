# Sharp convergence of the AESZ-28 Apéry approximants to \(\zeta(3)\)

## Result

Let \(A_n,C_n\) be the two solutions of
\[
4n^2(16n^2-1)u_{n-1}
-\bigl(65n^4+130n^3+105n^2+40n+6\bigr)u_n
+(n+1)^4u_{n+1}=0
\]
with
\[
(A_0,A_1)=(1,6),\qquad (C_0,C_1)=(0,1).
\]
Henrik Bachmann proved
\[
\lim_{n\to\infty}\frac{C_n}{A_n}=\frac{\zeta(3)}7.
\]
The dominant solution also has the positive double-binomial representation
\[
A_n=\sum_{i,j=0}^n
\binom ni^2\binom nj^2\binom{i+j}{n}^2,
\]
where \(\binom{i+j}{n}=0\) when \(i+j<n\).

The convergence admits the following sharp asymptotic expansion:
\[
\boxed{
\frac{\zeta(3)}7-\frac{C_n}{A_n}
=
\frac{\sqrt2\,\pi^3}{84}\,64^{-n}
\left(1-\frac{35}{48n}+O(n^{-2})\right).
}
\]
Equivalently,
\[
\boxed{
\zeta(3)-7\frac{C_n}{A_n}
=
\frac{\sqrt2\,\pi^3}{12}\,64^{-n}
\left(1-\frac{35}{48n}+O(n^{-2})\right).
}
\]

There is also a sharp asymptotic for the associated linear form:
\[
\boxed{
\zeta(3)A_n-7C_n
=
\frac{\sqrt3\,\pi}{9n^2}
\left(1-\frac{4}{3n}+O(n^{-2})\right).
}
\]

Finally, the recurrence and the known limit give the exact positive series
\[
\boxed{
\zeta(3)=
7\sum_{k=0}^{\infty}
\frac{(4k+1)\binom{4k}{2k}\binom{2k}{k}}
{(k+1)^4 A_kA_{k+1}}.
}
\]
Its \(n\)-term truncation is exactly \(7C_n/A_n\).

## Proof

### 1. Exact Casoratian

Set
\[
W_n=A_nC_{n+1}-A_{n+1}C_n.
\]
Writing
\[
a_n=4n^2(16n^2-1)
\]
and eliminating \(A_{n+1},C_{n+1}\) with the common recurrence gives
\[
W_n=\frac{a_n}{(n+1)^4}W_{n-1},\qquad W_0=1.
\]
Hence
\[
W_n
=
\prod_{j=1}^n\frac{4j^2(16j^2-1)}{(j+1)^4}
=
\frac{(4n+1)\binom{4n}{2n}\binom{2n}{n}}{(n+1)^4}.
\]
In particular \(W_n>0\), so \(C_n/A_n\) is strictly increasing. Since Bachmann proved its limit is \(\zeta(3)/7\),
\[
\frac{\zeta(3)}7-\frac{C_n}{A_n}
=
\sum_{k=n}^{\infty}
\frac{W_k}{A_kA_{k+1}}.
\]
Taking \(n=0\) yields the exact series above.

Stirling's formula gives
\[
W_n=
\frac{2\sqrt2}{\pi}\,64^n n^{-4}
\left(1-\frac{63}{16n}+O(n^{-2})\right).
\]

### 2. Asymptotics of \(A_n\)

Put \(i=nx,\ j=ny,\ s=x+y\). For \(0<x,y<1\) and \(s>1\), uniform Stirling expansion of the summand in the double-binomial formula gives
\[
\binom ni^2\binom nj^2\binom{i+j}{n}^2
=
\frac{s}{(2\pi n)^3x(1-x)y(1-y)(s-1)}
e^{nF(x,y)}
\left(1+O(n^{-1})\right),
\]
where
\[
F(x,y)
=
2\left(
h(x)+h(y)+s\log s-(s-1)\log(s-1)
\right)
\]
and
\[
h(t)=-t\log t-(1-t)\log(1-t).
\]

The Hessian of \(F\) is negative definite in the interior, so \(F\) is strictly concave there. Its unique critical point is
\[
(x_0,y_0)=\left(\frac34,\frac34\right),
\]
and
\[
F(x_0,y_0)=\log64.
\]
Moreover
\[
-D^2F(x_0,y_0)
=
\frac13
\begin{pmatrix}
40&8\\
8&40
\end{pmatrix},
\qquad
\det(-D^2F)=\frac{512}{3},
\]
while the non-exponential prefactor satisfies
\[
\frac{s_0}{x_0(1-x_0)y_0(1-y_0)(s_0-1)}
=\frac{256}{3}.
\]

A two-dimensional lattice Laplace expansion therefore gives
\[
A_n=
\frac{2\sqrt6}{3\pi^2}\,
\frac{64^n}{n^2}
\left(1+\frac{a_1}{n}+O(n^{-2})\right).
\]
The contribution outside a fixed neighborhood of \((3/4,3/4)\) is exponentially smaller, by strict concavity and the standard entropy bounds for binomial coefficients.

To identify the first correction, substitute
\[
A_n=c\,64^nn^{-2}
\left(1+\frac{a_1}{n}+O(n^{-2})\right)
\]
into the recurrence. The first nontrivial coefficient gives
\[
-1008a_1-609=0,
\]
hence
\[
a_1=-\frac{29}{48}.
\]
Thus
\[
\boxed{
A_n=
\frac{2\sqrt6}{3\pi^2}\,
\frac{64^n}{n^2}
\left(1-\frac{29}{48n}+O(n^{-2})\right).
}
\]

### 3. Quotient increment and tail

Combining the two expansions,
\[
\frac{W_n}{A_nA_{n+1}}
=
\frac{3\sqrt2\,\pi^3}{256}\,
64^{-n}
\left(1-\frac{35}{48n}+O(n^{-2})\right).
\]
Because
\[
\frac{C_{n+1}}{A_{n+1}}-\frac{C_n}{A_n}
=
\frac{W_n}{A_nA_{n+1}},
\]
the error is a geometrically weighted tail. For any fixed \(q\in(0,1)\),
\[
\sum_{j=0}^{\infty}q^j
\left(1+\frac{\alpha}{n+j}+O((n+j)^{-2})\right)
=
\frac{1}{1-q}
\left(1+\frac{\alpha}{n}+O(n^{-2})\right).
\]
Taking \(q=1/64\) gives
\[
\frac{\zeta(3)}7-\frac{C_n}{A_n}
=
\frac{\sqrt2\,\pi^3}{84}\,
64^{-n}
\left(1-\frac{35}{48n}+O(n^{-2})\right).
\]
Multiplying by \(7A_n\) yields
\[
\zeta(3)A_n-7C_n
=
\frac{\sqrt3\,\pi}{9n^2}
\left(1-\frac{4}{3n}+O(n^{-2})\right).
\]

## Context and significance

The recurrence is AESZ no. 28. Panzer exhibited the positive double-binomial formula for \(A_n\) and numerically observed the Apéry limit; Bachmann's 2026 preprint proves the limit and monotonicity in a construction connected with finite multiple zeta values. The Calabi--Yau differential-operator database records the same holomorphic solution and the singularity at \(1/64\).

The new statement quantifies the Apéry limit all the way to its leading constant and first correction. It also gives a positive \(64\)-geometric exact series for \(\zeta(3)\) and identifies the unexpectedly small linear form \(\zeta(3)A_n-7C_n\) to two asymptotic orders.

## Verification

`artifacts/verify.py` computes the two recurrence solutions exactly as rational numbers, checks the closed Casoratian identity for \(0\le n<80\), and numerically compares the three asymptotic formulas with their first corrections. `artifacts/verify_output.txt` contains the resulting normalized ratios. These computations support the formulas but are not used in the proof.

## Originality and limitations

Originality is asserted only to the best of our knowledge. The inspected version of Bachmann's preprint proves the limit \(C_n/A_n\to\zeta(3)/7\) but does not state a sharp asymptotic for the quotient error or the linear form. Searches using the recurrence, AESZ-28 terminology, Martin-sequence terminology, the constants above, and equivalent Apéry-limit formulations did not locate the displayed asymptotic formulas or exact positive series.

A significant residual risk is that Bachmann cites Sato--Tasaka, *Multivariate Apéry-like numbers, interpolations, and modular L-values*, as a manuscript in preparation proving the same limiting value. Its full contents were not available for inspection, so it could contain unindexed information about convergence rates. Panzer's 2025 slides give the recurrence, binomial formula, and limiting constant but not the sharp error asymptotics found here.

The asymptotic evaluation of the positive double-binomial sum uses standard multivariate Laplace analysis; no novelty is claimed for the method itself. The result does not improve known irrationality measures for \(\zeta(3)\), does not analyze denominator growth of \(C_n\), and does not address the finite or \(q\)-analogue developed by Bachmann.

## References

1. H. Bachmann, *A q-recurrence for a finite Apéry limit*, arXiv:2609.18271v1 (2026). https://arxiv.org/abs/2609.18271
2. E. Panzer, *Combinatorial Feynman rules*, MAMP 2025 lecture slides. https://indico.mitp.uni-mainz.de/event/413/contributions/5723/attachments/4051/5363/MAMP2025_Panzer.pdf
3. E. Panzer and K. Yeats, *Feynman symmetries of the Martin and \(c_2\) invariants of regular graphs*, Combinatorial Theory 5 (2025), no. 1, 10. https://doi.org/10.5070/C65165021
4. M. Chamberland and A. Straub, *Apéry Limits: Experiments and Proofs*, American Mathematical Monthly 128 (2021), 811--824. https://arxiv.org/abs/2011.03400
5. Calabi--Yau differential operator database, AESZ no. 28. https://cydb.mathematik.uni-mainz.de/?m=lookup&search=true&sol=3948
