# Universal Cesàro averages of multinomial modal log coefficients — provenance-corrected presentation

## Status and provenance

The theorem below is correct, but it was already present in earlier SCOPE records.

`2026/09/18/multinomial-mode-cesaro-universality--a66b1067c370`,
first committed at 2026-09-18T20:07:58Z, proves the polynomial transfer law at the multinomial mode and the universal Cesàro mean of every logarithmic coefficient; it also goes further by computing a nonuniversal second multiplicative coefficient.

`2026/09/19/multinomial-mode-cesaro-log-coefficients--69879bbdb548`,
first committed at 2026-09-19T08:07:59Z, already gives the same Bernoulli--Stirling closed form displayed below.

This record was first committed later, at 2026-09-19T20:31:49Z. It is therefore retained as an alternate derivation and verification package, with no separate originality claim.

## Theorem

Let
\[
X\sim\operatorname{Mult}(N;p_1,\ldots,p_n),\qquad p_i>0,\quad \sum_i p_i=1,
\]
and assume \(p_1,\ldots,p_n\) are linearly independent over \(\mathbb Q\). Let \(m(N)\) be the unique multinomial mode and
\[
\Delta_i(N)=m_i(N)-Np_i.
\]
For Elezović's logarithmic local-expansion coefficients
\[
c_k(t;p)=\frac{(-1)^{k+1}}{k(k+1)}
\left[B_{k+1}-\sum_{i=1}^n p_i^{-k}B_{k+1}(t_i+1)\right],
\]
one has, for every fixed \(k\ge1\),
\[
\boxed{
\lim_{M\to\infty}\frac1M\sum_{N=1}^M c_k(\Delta(N);p)
=
\frac{(-1)^{k+1}}{k(k+1)}
\left[
B_{k+1}
-
\frac{(k+1)!(n-2)!}{(k+n-1)!}
\left\{\!\!\begin{matrix}k+n\\ n-1\end{matrix}\!\!\right\}
\right].
}
\]
The limit depends only on \(n\). In particular,
\[
\overline c_1=-\frac{(n-1)(3n+4)}{24},
\qquad
\overline c_2=\frac{n(n-1)(n+2)}{48}.
\]

More generally, every polynomial \(F\) in the modal displacement vector has a Cesàro limit equal to its expectation under Janson's Jefferson seat-excess limit law.

## Proof

Elezović identifies the multinomial mode with Jefferson--D'Hondt apportionment. Under rational independence there are no persistent divisor ties. Janson's fixed-\(p\) Jefferson theorem, with the house size uniform on \(\{1,\ldots,M\}\), is therefore exactly a Cesàro limit theorem for \(\Delta(N)\). The displacement vectors are uniformly bounded, so weak convergence upgrades to convergence of every polynomial moment.

For one coordinate, Janson's Jefferson limit can be written
\[
\Xi_i\overset d=\frac{np_i-1}{2}+U_0+p_i\sum_{r=1}^{n-2}U_r,
\]
where the \(U_r\) are independent uniform variables on \((-1/2,1/2)\). Combining this moment generating function with
\[
\sum_{m\ge0}B_m(x)\frac{z^m}{m!}=\frac{ze^{xz}}{e^z-1}
\]
gives
\[
\sum_{m\ge0}\mathbb E B_m(\Xi_i+1)\frac{z^m}{m!}
=
e^w\left(\frac{e^w-1}{w}\right)^{n-2},
\qquad w=p_i z.
\]
Hence
\[
\mathbb E B_m(\Xi_i+1)
=
p_i^m\,m!\,[w^m]\,
e^w\left(\frac{e^w-1}{w}\right)^{n-2}.
\]
The standard Stirling-number generating function yields
\[
[w^{k+1}]e^w\left(\frac{e^w-1}{w}\right)^{n-2}
=
\frac{(n-2)!}{(k+n-1)!}
\left\{\!\!\begin{matrix}k+n\\n-1\end{matrix}\!\!\right\}.
\]
After multiplication by \(p_i^{-k}\) and summation over \(i\), the remaining factor is \(\sum_i p_i=1\), proving the formula.

## Scientific role of this record

The bundled computation remains useful as an independent numerical/reproducibility check of the formula. Scientifically, however, this record is a later restatement of the earlier SCOPE results cited above rather than a new finding.

## References

1. N. Elezović, *Multinomial probabilities near the mode: integer modes and the complete local expansion*, arXiv:2609.20229 (2026).
2. S. Janson, *Asymptotic bias of some election methods*, Annals of Operations Research 215 (2014), 89--136; arXiv:1110.6369.
3. SCOPE record `2026/09/18/multinomial-mode-cesaro-universality--a66b1067c370`, first committed 2026-09-18T20:07:58Z.
4. SCOPE record `2026/09/19/multinomial-mode-cesaro-log-coefficients--69879bbdb548`, first committed 2026-09-19T08:07:59Z.
