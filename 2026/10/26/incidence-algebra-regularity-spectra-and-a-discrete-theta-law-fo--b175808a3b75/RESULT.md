# Incidence-algebra regularity spectra and a discrete-theta law for triangular matrices

## Finding

**Theorem (regularity-spectrum invariance and theta fluctuations).** Fix a prime power \(q\ge2\). For every finite poset \(P\) with \(n\) vertices and \(e(P)\) strict comparable pairs, let \(I_q(P)\) be its finite-field incidence algebra. Let \(B_q(P)\) be the algebra on the same interval-basis vector space whose off-diagonal ideal has square zero, while its diagonal idempotents act on intervals by their endpoints. For an element \(a\) of either algebra, let \(Z(a)=\{v\in P:a(v,v)=0\}\), and write \(e_P(Z)\) for the number of strict comparable pairs entirely contained in \(Z\).

Call \(a\) *von Neumann regular* if \(axa=a\) for some \(x\) in the same algebra. In **both** algebras, for every prescribed \(Z\subseteq P\), the exact number of regular elements with \(Z(a)=Z\) is
\[
N_{P,q}(Z)=(q-1)^{n-|Z|}q^{e(P)-e_P(Z)}.
\]
In particular the complete zero-diagonal-support distributions agree in these algebras, although their off-diagonal multiplication can differ. Every regular element in either algebra is also *unit regular*: the witness in \(axa=a\) can be chosen invertible.

When \(P\) is the chain \(1<\cdots<n\), let \(K_n=|Z(a)|\) for uniformly sampled *regular* \(a\). Its law is exactly
\[
\Pr(K_n=k)=\frac{\binom nk(q-1)^{-k}q^{-\binom k2}}{\sum_{j=0}^n\binom nj(q-1)^{-j}q^{-\binom j2}},\qquad 0\le k\le n.
\]
For every sufficiently large \(n\), define the unique positive real \(\kappa_n\) by
\[
n=\kappa_n+(q-1)(\kappa_n+1)q^{\kappa_n},\qquad m_n=\lfloor\kappa_n\rfloor,\quad\theta_n=\kappa_n-m_n.
\]
Define the discrete-theta probability measure on \(\mathbb Z\)
\[
\nu_{q,\theta}(t)=\frac{q^{\theta t-t(t-1)/2}}{\Theta_q(\theta)},\qquad \Theta_q(\theta)=\sum_{j\in\mathbb Z}q^{\theta j-j(j-1)/2}.
\]
Then, uniformly in the centering phase \(0\le\theta_n<1\),
\[
\bigl\|\mathcal L(K_n-m_n)-\nu_{q,\theta_n}\bigr\|_{\rm TV}
=O_q(1/\log n).
\]
Moreover, with \(w_{n,q}(k)=\binom nk(q-1)^{-k}q^{-\binom k2}\), the regularity probability in either chain algebra has the sharp relative asymptotic
\[
\Pr(a\text{ regular})=\left(\frac{q-1}{q}\right)^n
w_{n,q}(m_n)\Theta_q(\theta_n)\left(1+O_q(1/\log n)\right).
\]
In particular, \(\kappa_n=\log_q n-\log_q\log_q n-\log_q(q-1)+o(1)\); the fluctuations remain of order one and retain a nonconstant lattice phase rather than becoming Gaussian.

## Assumptions and scope

All posets are finite; all scalar fields are \(\mathbb F_q\) with \(q\) any prime power. An interval-basis vector is written \(e_{uv}\) for \(u\le v\), with \(e_{uv}e_{vw}=e_{uw}\) in \(I_q(P)\) when the endpoints are comparable and zero for nonmatching indices. In \(B_q(P)\), the products of two **strict** interval vectors are set to zero, and diagonal idempotents retain their usual left and right endpoint action. Thus \(B_q(P)\) is *not generally* the quotient \(I_q(P)/J^2\); both algebras have dimension \(n+e(P)\). The regularity condition is the multiplicative-semigroup condition \(axa=a\), not regularity of a local ring or regularity of a matrix under conjugation.

When the poset is a chain, \(I_q(P)\) is the full upper-triangular matrix algebra, and \(B_q(P)\) is the complete acyclic quiver algebra with all paths of length at least two killed. For \(n\ge3\) these algebras have different radical nilpotency lengths. The asymptotic statements hold as \(n\to\infty\) with \(q\) fixed; there is no claim of a uniform estimate as \(q\to\infty\).

## Proof

**1. Incidence-algebra Schur complement.** Fix diagonal values \(\alpha_v\), with nonzero set \(T=P\setminus Z\). Reorder rows and columns by \(T,Z\), writing the incidence matrix as
\[
A=\begin{pmatrix}B&C\\D&E\end{pmatrix}.
\]
The \(T\times T\) incidence block \(B\) is invertible because its diagonal is nonzero. Its inverse is again supported only on comparable pairs of \(T\). The matrices
\[
U=\begin{pmatrix}I&0\\-DB^{-1}&I\end{pmatrix},\qquad
V=\begin{pmatrix}I&-B^{-1}C\\0&I\end{pmatrix}
\]
are both incidence-algebra units: every nonzero entry of each product follows an increasing comparable chain. They give
\[
UAV=\operatorname{diag}(B,S),\qquad S=E-DB^{-1}C.
\]
The \(Z\times Z\) block \(S\) belongs to the strictly upper-triangular radical of \(I_q(Z)\). If \(A\) is regular, so is \(UAV\); its \(Z\times Z\) block satisfies \(S=SYS\) for some \(Y\in I_q(Z)\). Consequently \(S=S(YS)^h\) for every positive integer \(h\). Since \(YS\) belongs to a nilpotent ideal, \(S=0\). Conversely if \(S=0\), then \(\operatorname{diag}(B^{-1},I_Z)\) is an invertible generalized inverse of \(\operatorname{diag}(B,0)\); transporting it through \(U,V\) gives an invertible witness for \(A\). Thus regularity is *equivalent* to \(S=0\), with all field characteristics and the empty-block boundary included.

For each fixed choice of the diagonal entries and all strict entries outside \(Z\times Z\), the equations \(S=0\) prescribe the strict entries of \(E\) uniquely as \(DB^{-1}C\). There are exactly \(e(P)-e_P(Z)\) independent unrestricted strict entries. The number of nonzero diagonal choices is \((q-1)^{n-|Z|}\), proving the formula for \(I_q(P)\).

**2. Square-zero comparison.** In \(B_q(P)\), let \(a=d+r\), where \(d=\sum_v\alpha_v e_{vv}\) and \(r\) is off-diagonal. If \(a=axa\), the \((u,v)\) entry for \(u<v\) with \(u,v\in Z\) is necessarily zero: the off-diagonal product is \(\alpha_u\alpha_v x_{uv}+(\alpha_u x_{uu}+\alpha_v x_{vv})a_{uv}=0\). Conversely, when all such entries vanish, choose \(x_{vv}=\alpha_v^{-1}\) for \(v\in T\), choose \(x_{vv}=1\) for \(v\in Z\), and for each \(u<v\) set \(x_{uv}=-a_{uv}/(\alpha_u\alpha_v)\) when both diagonal entries are nonzero and \(x_{uv}=0\) otherwise. The defining products verify \(axa=a\); the diagonal entries of \(x\) are all nonzero, hence \(x\) is a unit. Counting free strict entries gives the identical formula. Indeed the map that replaces \(A_{ZZ}\) by \(S(A)\) and keeps all other coordinates fixed is a diagonal-stratum-wise polynomial bijection (with nonzero diagonal inverses allowed as field scalars), transporting the regularity indicator to the square-zero indicator.

**3. Exact chain spectrum.** For a chain, every \(k\)-element zero set has \(\binom k2\) strict comparable pairs. Sum the first formula over its \(\binom nk\) possible zero sets and divide by the total \(q^{n+\binom n2}\) to obtain the displayed exact probability law and regularity probability.

**4. Theta local limit and error.** Write \(w_k=w_{n,q}(k)\). The exact successive ratio is
\[
\frac{w_{k+1}}{w_k}=\frac{n-k}{(q-1)(k+1)}q^{-k},
\]
which strictly decreases in \(k\). The defining equation for \(\kappa=\kappa_n\) ensures this ratio equals one for real \(k=\kappa\). Put \(m=\lfloor\kappa\rfloor\) and \(\theta=\kappa-m\). For any integer \(t\) with \(-m\le t\le n-m\), telescoping successive ratios yields
\[
\frac{w_{m+t}}{w_m}=q^{\theta t-t(t-1)/2}R_{n,m,\theta}(t),
\]
where, for \(t>0\),
\[
R_{n,m,\theta}(t)=\prod_{j=0}^{t-1}\frac{n-m-j}{n-\kappa}\frac{\kappa+1}{m+j+1},
\]
and for \(t<0\) the reciprocal of the corresponding product over \(j=t,\ldots,-1\). The denominator \(n-\kappa=(q-1)(\kappa+1)q^\kappa\) is positive. For \(|t|\le m/2\), elementary logarithmic estimates give
\[
|\log R_{n,m,\theta}(t)|\le C_q\frac{t^2+|t|}{m},
\]
with a constant independent of \(n\) and \(\theta\). The decreasing-ratio property bounds both the exact and theta weights by \(C_q q^{-c_qt^2}\) outside a fixed central interval. Applying \(|e^u-1|\le |u|e^{|u|}\) on \(|t|\le m/2\), then summing the resulting \(O_q((t^2+|t|)q^{-c_qt^2}/m)\), and bounding the remaining tails by \(O_q(q^{-c_qm^2})\), yields
\[
\sum_t\left|\frac{w_{m+t}}{w_m}-q^{\theta t-t(t-1)/2}\right|=O_q(m^{-1}).
\]
Both normalizing sums are uniformly bounded above and below by positive \(q\)-dependent constants. Normalizing proves total-variation distance \(O_q(m^{-1})\); summing before normalizing yields the stated relative regularity-probability asymptotic. Finally, taking base-\(q\) logarithms in the equation defining \(\kappa\) gives \(\kappa=\log_q n-\log_q\log_q n-\log_q(q-1)+o(1)\), so \(m\asymp_q\log n\). This completes the proof.

## Verification

The standalone scripts `check_incidence.py` and `check.py` use standard-library arithmetic, with an explicit \(\mathbb F_4\) implementation in the latter. Running `python3 check_incidence.py` exhaustively solves \(axa=a\) as linear equations in each witness coordinate on seven incidence-algebra configurations (chains, diamond, a non-chain branching poset, and an antichain) over \(\mathbb F_2\) and \(\mathbb F_3\), testing \(22{,}156\) algebra elements. It checks their exact diagonal-zero spectra and an independent Schur-complement criterion. Running `python3 check.py` checks nine square-zero configurations, totaling \(97{,}829\) elements over \(\mathbb F_2,\mathbb F_3,\mathbb F_4\); for 99 cases it independently enumerates all potential witnesses. It also compares twelve finite-\(n\) defect laws with their phase-dependent theta approximations. The two text outputs contain the exact configurations and checks. The infinite statements are proved above rather than inferred from these experiments.

## Relationship to prior work

Khripchenko and Novikov (2008, Theorem 4) already prove that every regular element of a finitary incidence algebra is a product of invertible elements and a diagonal idempotent. Thus diagonalizability up to two-sided multiplication is **prior coverage** and is not claimed new. Gould, Johnson, and Naz (arXiv 2019) study regularity-related semigroup structure of upper-triangular matrices, especially over semirings, but do not provide the stated full finite-field poset-wise zero-set probabilities and theta fluctuation law. For \(q=2\), the unrefined chain total is the **known OEIS A079491 sequence**; Wilf's *Algorithms and Complexity*, §5.6, supplies the underlying binomial sum as an expected independent-set count and already bounds its largest-term index between logarithmic scales. None of those elementary formulas, existing classifications, or their quoted numerical values is asserted original here. The contribution assessed here is their synthesis into an exact *paired-algebra support law for every finite poset*, together with the quantitative *phase-dependent full distribution and sharp relative normalization* for the growing chain. Existing specialization of the stated local limit in earlier asymptotic/combinatorial literature remains a plausible priority risk.

## Limitations

The result concerns only von Neumann regular *elements*, not regularity of the entire upper-triangular monoid. The asymptotic error constants depend on fixed \(q\); the definition of \(\kappa_n\) applies to all sufficiently large \(n\), and small \(n\) are covered only by the exact formulas. The equivalence of regularity spectra is a counting/stratum bijection, not an algebra isomorphism. The complete chain local limit is unproved for field sizes growing with \(n\), and no claim of complete novelty relative to unindexed literature is made. The calculation has not received independent external validation.

## References

1. N. S. Khripchenko and B. V. Novikov, *Finitary incidence algebras*, arXiv:0803.0069v1 (2008), especially Theorems 2–4. https://arxiv.org/pdf/0803.0069
2. V. Gould, M. Johnson, and M. Naz, *Matrix semigroups over semirings*, arXiv:1907.12518v1 (first posted 2019-07-29), especially the introduction and discussion of upper triangular semigroups. https://arxiv.org/abs/1907.12518
3. N. J. A. Sloane et al., OEIS A079491, exact binary chain totals and an independent-set interpretation. https://oeis.org/A079491
4. H. S. Wilf, *Algorithms and Complexity*, §5.6 (1994 internet edition), expected independent-set sum and modal bounds.
