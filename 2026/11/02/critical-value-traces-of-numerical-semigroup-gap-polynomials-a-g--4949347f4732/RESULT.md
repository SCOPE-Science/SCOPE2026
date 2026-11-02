# Critical-value traces of numerical-semigroup gap polynomials: a genus-rank law

## Finding

Let \(S\neq\mathbb N_0\) be any numerical semigroup, with finite set of gaps \(G=\mathbb N_0\setminus S\), Frobenius number \(F=\max G\ge1\), and genus \(\gamma=|G|\). Consider the full monic gap-polynomial family
\[
P_{\mathbf c}(z)=z^F+\sum_{\substack{g\in G\\g<F}}c_g z^g,
\qquad c_g\in\mathbb C.
\]
Write \(r_1,\ldots,r_{F-1}\) for the critical points, counted with algebraic multiplicity, and let \(\mathcal T_S(\mathbf c)=\sum_{j=1}^{F-1}P_{\mathbf c}(r_j)\). For \(F=1\) the critical-point multiset and sum are empty. Define the truncated formal series
\[
U(t)=\sum_{\substack{g\in G\\g<F}}\frac{g}{F}c_g t^{F-g}.
\]
Then, with \([t^F]\) denoting coefficient extraction,
\[
\boxed{\mathcal T_S(\mathbf c)=-F[t^F](1+U(t))\log(1+U(t))
=-F\sum_{k=2}^{F}\frac{(-1)^k}{k(k-1)}[t^F]U(t)^k.}
\]
The logarithm is interpreted formally at constant term one. Every monomial \(\prod_{g<F}c_g^{m_g}\) with \(m_g\ge0\) appears with a nonzero coefficient if and only if
\[
\sum_{g<F}m_g(F-g)=F.
\]
Writing \(k=\sum_{g<F}m_g\ge2\), its coefficient is exactly
\[
(-1)^{k+1}F\frac{(k-2)!}{\prod_g m_g!}
\prod_{g<F}\left(\frac{g}{F}\right)^{m_g}.
\]

The real Hessian \(H_S\) of \(\mathcal T_S\) at the zero coefficient vector, indexed by \(g,h\in G\setminus\{F\}\), has entries
\[
\boxed{(H_S)_{g,h}=-\frac{gh}{F}\,\mathbf 1_{\{g+h=F\}},
\qquad \operatorname{rank}H_S=2\gamma-F-1.}
\]
Its inertia (positive, negative, zero eigenvalues) is
\[
\left(\frac{\delta-e}{2},\frac{\delta+e}{2},
\gamma-1-\delta\right),\qquad
\delta=2\gamma-F-1,\quad e=\mathbf1_{\{2\mid F\}}.
\]
In particular, \(\mathcal T_S\equiv0\) exactly when \(S\) is symmetric, \(\operatorname{rank}H_S=1\) exactly when \(S\) is pseudo-symmetric, and \(H_S\) is nondegenerate exactly when \(S=\{0,F+1,F+2,\ldots\}\) is ordinary. If \(S\) is pseudo-symmetric (so \(F\) is even), the full, *unrestricted* gap family obeys the exact identity
\[
\boxed{\mathcal T_S(\mathbf c)=-\frac F8\,c_{F/2}^{\,2},}
\]
independently of every other allowed coefficient.

## Assumptions and scope

A numerical semigroup is an additive submonoid of \(\mathbb N_0\) with finite complement; exclude \(\mathbb N_0\), which has no Frobenius number. All claims hold for each such \(S\), all complex coefficients \(c_g\), and all \(F\ge1\). Hessian inertia refers to its real symmetric matrix on the real coefficient space; its rank is the same over \(\mathbb R\) and \(\mathbb C\). A semigroup is symmetric if each gap \(g\) has \(F-g\in S\); it is pseudo-symmetric if \(F\) is even and this holds except for the necessary gap \(F/2\). The identity for pseudo-symmetry uses the **full** polynomial including the central coefficient, unlike the central-term-deleted pseudo-gap family.

## Proof

**1. Formal critical-point trace.** Put \(n=F-1\) and \(D(t)=t^nP'_{\mathbf c}(1/t)/F=1+U(t)\). The monic polynomial \(P'_{\mathbf c}/F\) has roots \(r_1,\ldots,r_n\) with multiplicity, whence \(D(t)=\prod_{j=1}^n(1-r_jt)\). This remains valid for coincident roots, including all roots zero. Therefore in the formal series ring,
\[
-\log D(t)=\sum_{m\ge1}\frac{s_m}{m}t^m,
\qquad s_m=\sum_{j=1}^n r_j^m.
\]
Set \(c_F=1\). Expanding the polynomial at each critical point yields \(\mathcal T_S=\sum_{g\in G}c_gs_g\). Hence
\[
\begin{aligned}
\mathcal T_S
&=-[t^F]\log D(t)
\left(F+\sum_{\substack{g\in G\\g<F}}g c_g t^{F-g}\right)\\
&=-F[t^F]D(t)\log D(t),
\end{aligned}
\]
since the parenthesized factor is \(FD(t)\). The identity follows from
\((1+u)\log(1+u)=u+\sum_{k\ge2}(-1)^k u^k/(k(k-1))\).
As \(U(t)\) has no \(t^F\) coefficient, only \(k\ge2\) contribute. Its \(k\)-th power has exactly the monomials with \(\sum_gm_g=k\) and \(\sum_gm_g(F-g)=F\), and the multinomial theorem supplies the displayed coefficient. In particular none cancels: the factor is nonzero in characteristic zero, and each monomial has a unique total degree \(k\).

**2. Hessian and genus.** Only the \(k=2\) term contributes to the Hessian at zero. Differentiating gives the explicit weighted anti-diagonal matrix
\((H_S)_{g,h}=-gh/F\) for \(g+h=F\), and zero otherwise. Each nonzero row has exactly one nonzero entry in a unique column, so its rank is the number of gaps \(g<F\) for which \(F-g\) is also a gap.

To evaluate this count, for \(0\le j\le F\) put \(\varepsilon_j=\mathbf1_{\{j\in G\}}\). Since \(F\notin S\), no pair \(j,F-j\) can both lie in \(S\). Thus
\(\varepsilon_j+\varepsilon_{F-j}=1+\varepsilon_j\varepsilon_{F-j}\).
Summing over \(j=0,\ldots,F\) gives
\[
2\gamma=(F+1)+\sum_{j=0}^F\varepsilon_j\varepsilon_{F-j}.
\]
The last sum is exactly the Hessian rank, because \(0\in S\) and \(F\in G\). Each pair of distinct reflected gaps forms a real \(2\times2\) block with eigenvalues \(\pm gh/F\); when \(F\) is even, the unavoidable central gap gives one negative eigenvalue \(-F/4\). This yields the inertia formula.

The rank vanishes if and only if no two gaps are complementary, which is precisely symmetry. Rank one can occur only for even \(F\), with the central gap as the sole complementary pair, which is precisely pseudo-symmetry. Nondegeneracy means \(2\gamma-F-1=\gamma-1\), equivalently \(\gamma=F\), i.e. all \(1,\ldots,F\) are gaps and \(S\) is ordinary. Because a nonsymmetric semigroup has a nonzero Hessian, \(\mathcal T_S\) cannot be the zero polynomial; symmetric semigroups are handled by the next argument.

**3. Symmetric and pseudo-symmetric exact traces.** If \(S\) is symmetric, every exponent \(F-g\) occurring in \(U\) belongs to \(S\); additive closure and \(F\notin S\) imply \([t^F]U^k=0\) for all \(k\), so \(\mathcal T_S\equiv0\).

If \(S\) is pseudo-symmetric, write \(h=F/2\). Every exponent in \(U\) other than \(h\) lies in \(S\). A sum of these latter exponents cannot equal the gap \(F\), and cannot equal \(h\) either. Therefore the only multiset of exponents from \(U\) summing to \(F\) is exactly \(h+h\). The coefficient formula now gives
\(-F\cdot\tfrac12\cdot(h/F)^2c_h^2=-Fc_h^2/8\), as asserted. No higher-degree contributions exist.

For \(F=1\), \(U=0\) and the empty Hessian has rank zero, as required.

## Verification

The accompanying pure-Python script `verification/critical_trace_verify.py` enumerates every numerical semigroup with Frobenius number \(1\le F\le13\). At three independently chosen integer coefficient vectors per semigroup, it computes the trace in two ways: (i) as a matrix trace of \(P(C)\) for the exact-rational companion matrix \(C\) of the normalized derivative; and (ii) by the independent truncated \(U\)-power coefficient formula. It separately checks the genus-rank count and the full pseudo-symmetric identity. For \(F\le7\), it reconstructs Hessian entries from exact univariate interpolation of matrix-trace evaluations, rather than inserting the claimed Hessian formula into the trace calculation.

Run `python3 verification/critical_trace_verify.py` with the Python standard library. The expected full result is:

```text
VERIFY_OK semigroups=276 trace_companion_vs_log=828 Hessian_entry_checks=207 symmetric=24 pseudosymmetric=10 other=242 exact_rational=yes
CASE F=2 genus=2 rank=1 trace=-1/4
CASE F=5 genus=4 rank=2 trace=-6/5
CASE F=6 genus=4 rank=1 trace=-3/4
CASE F=11 genus=6 rank=0 trace=0
```

The proof applies for all Frobenius numbers; finite tests are only cross-checks. The companion computation is an algebraic exact-arithmetic trace, not a floating-point root finder.

## Relationship to prior work

P. Grinfeld, *Power sums of critical points of gap polynomials for symmetric and pseudo-symmetric numerical semigroups* (arXiv:2609.03049; first submitted 2026-09-02), proves vanishing of critical-point power sums on gaps for symmetric semigroups and, after deleting the central term, for pseudo-symmetric semigroups. Its Corollary 5 gives vanishing of the sum of critical values in those restricted cases. The general critical-value trace polynomial, its coefficient support, the Hessian rank \(2\gamma-F-1\), and the exact nonzero pseudo-symmetric central-square value are not stated there. The present calculation uses the same classical Newton/Vieta machinery to answer a distinct, unrestricted coefficient-evaluation question.

L. G. Fel's papers on symmetric polynomials associated with numerical semigroups (arXiv:2010.03363, and arXiv:2012.13357) study different polynomials built from semigroup generators and syzygy degrees; their accessible abstracts do not present the critical-value trace of sparse gap polynomials. An earlier unpublished project description by M. Becht and P. Grinfeld mentions critical values of polynomials associated with irreducible numerical semigroups but does not specify these evaluated identities; the historical-priority risk remains.

## Limitations

The theorem concerns sums of critical values counted with multiplicity, not the individual critical values, their distribution, or critical points of higher-dimensional polynomials. The classification of symmetric and pseudo-symmetric semigroups is classical; the new content is an explicit analytic encoding and exact evaluation of its coefficient-space trace and Hessian. The coefficient-extraction identity is derived from classical formal logarithms, so historical equivalence to an earlier general polynomial identity remains possible. The 2019 project description was available only as an abstract.

## References

1. P. Grinfeld, *Power sums of critical points of gap polynomials for symmetric and pseudo-symmetric numerical semigroups*, arXiv:2609.03049 (first submitted 2026-09-02). https://arxiv.org/abs/2609.03049
2. L. G. Fel, *Symmetric polynomials associated with numerical semigroups*, arXiv:2010.03363 (2020); *Discrete Mathematics Letters* **5** (2021), 56–62. https://arxiv.org/abs/2010.03363
3. L. G. Fel, *Genera of numerical semigroups and polynomial identities for degrees of syzygies*, arXiv:2012.13357 (2020). https://arxiv.org/abs/2012.13357
4. M. Becht and P. Grinfeld, *Numerical semigroups in polynomials*, Drexel University STAR Research Abstract Booklet (2019), abstract only. https://drexel.edu/pennoni/~/media/Drexel/Pennoni-Group/Pennoni/Documents/UREP/STAR-Abstracts/2019-Abstract-Booklet.pdf
