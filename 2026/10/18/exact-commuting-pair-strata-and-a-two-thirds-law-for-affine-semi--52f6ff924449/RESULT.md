# Exact commuting-pair strata and a two-thirds law for affine semisymmetric quasigroups

## Finding

Fix a prime power \(q\) and an integer \(n\ge1\), and put \(V=\mathbb F_q^n\). Consider **all distinct operations on this fixed labelled vector space** of the form
\[
u*v=A u+B v+c,\qquad A,B\in\operatorname{GL}_n(\mathbb F_q),\quad c\in V,
\]
that satisfy semisymmetry \((u*v)*u=v\) for every \(u,v\in V\). Let \(H_{n,q}(r)\) count these operations for which the proportion \(\operatorname{cp}(*)\) of commuting ordered pairs is \(q^{-r}\). The following formulas determine the **entire finite-dimensional probability distribution**.

Write \(G_m(Q)=|\operatorname{GL}_m(\mathbb F_Q)|=\prod_{j=0}^{m-1}(Q^m-Q^j)\), with \(G_0(Q)=1\), and write \(\gamma_m(q)=\prod_{j=1}^m(1-q^{-j})\), with \(\gamma_0(q)=1\).

* If \(3\nmid q\) and \(q\equiv1\pmod3\), for every \(0\le r\le n\),
\[
H_{n,q}(r)=q^{n-r}G_n(q)\sum_{b=0}^r
  \frac{1}{G_{n-r}(q)G_b(q)G_{r-b}(q)}.
\]
* If \(3\nmid q\) and \(q\equiv2\pmod3\), then \(H_{n,q}(r)=0\) for odd \(r\), while for even \(0\le r\le n\),
\[
H_{n,q}(r)=\frac{q^{n-r}G_n(q)}{G_{n-r}(q)G_{r/2}(q^2)}.
\]
* If \(q\) has characteristic three, put \(s(a,b,c)=(a+b+c)^2+(a+b)^2+a^2\). Then
\[
H_{n,q}(r)=q^{n-r}G_n(q)
\sum_{\substack{a,b,c\ge0\\3a+2b+c=n\\2a+b=r}}
\frac{q^{-s(a,b,c)}}{\gamma_a(q)\gamma_b(q)\gamma_c(q)}.
\]

The nonzero strata occur at every \(r\in\{0,\ldots,n\}\) in the split case, at the even \(r\le n\) in the nonsplit case, and at every \(r\le\lfloor2n/3\rfloor\) in characteristic three. Every formula counts operations, **not isomorphism classes**.

In addition, for each fixed prime power \(q\), uniformly choose one of these affine semisymmetric operations and denote its commuting fraction by \(X_{n,q}\). There are constants \(0<c_q<C_q<\infty\), depending only on \(q\), such that for every \(n\ge1\),
\[
c_q q^{-2n/3}\le \mathbb E[X_{n,q}]\le C_q q^{-2n/3}.
\]
Writing \(R_{n,q}=-\log_qX_{n,q}\) and \(r_n=(2n-1)/3\), there is also a constant \(D_q\) such that for all \(t\ge0\),
\[
\Pr\bigl(|R_{n,q}-r_n|\ge t\bigr)\le D_q q^{-t^2}.
\]
Thus the same two-thirds exponent and a dimension-independent discrete-Gaussian concentration law hold in the split, nonsplit, and characteristic-three cases, even though their finite-dimensional allowable ranks differ.

## Assumptions and scope

All \(q\) are prime powers, and all linear maps and vector spaces are defined over \(\mathbb F_q\). The zero-dimensional case is excluded. Two displayed affine formulas define the same operation precisely when their coefficients \((A,B,c)\) agree. Every sampled object is one of these operations on the fixed vector space, sampled uniformly without identifying isomorphic quasigroups. The statistic counts **ordered** pairs \((u,v)\) satisfying \(u*v=v*u\). The limit is in dimension \(n\to\infty\) at **fixed** \(q\); no uniformity in \(q\) is claimed.

## Proof

### Semisymmetry and commuting pairs

Comparison of coefficients in \((u*v)*u=v\) yields
\[
AB=I,\quad A^2+B=0,\quad (A+I)c=0.
\]
These are equivalent to \(B=A^{-1}\), \(A^3=-I\), and \(c\in\ker(A+I)\). Since \(A^3=-I\), invertibility is automatic. Every such choice has bijective left and right translations and is therefore a quasigroup. Put \(r=\operatorname{rank}(A+I)\). The number of allowed translation vectors is \(q^{n-r}\). Moreover,
\[
u*v=v*u\iff(A-A^{-1})(u-v)=0
\iff A(A+I)(u-v)=0.
\]
There are \(q^n q^{n-r}\) commuting ordered pairs out of \(q^{2n}\); hence \(\operatorname{cp}(*)=q^{-r}\).

### Exact matrix enumerations

For characteristic other than three, \(t^3+1=(t+1)(t^2-t+1)\) is squarefree. When \(q\equiv1\pmod3\), all three eigenvalues belong to \(\mathbb F_q\). Matrices with \(n-r\) copies of eigenvalue \(-1\), and \(b,r-b\) copies of the other eigenvalues, comprise one conjugacy class of size \(G_n(q)/[G_{n-r}(q)G_b(q)G_{r-b}(q)]\). Multiplying by \(q^{n-r}\) gives the first formula. When \(q\equiv2\pmod3\), the second factor is irreducible and the residual invariant summand has even dimension \(r\), with centralizer \(\operatorname{GL}_{r/2}(\mathbb F_{q^2})\); this gives the second formula.

In characteristic three, the polynomial is \((t+1)^3\) and \(A=-I+N\), where \(N^3=0\). Let \(a,b,c\) denote the numbers of Jordan blocks of respective sizes three, two, one. Then \(n=3a+2b+c\), and \(\operatorname{rank}N=2a+b\). The column lengths of the conjugate Jordan partition are \((a+b+c,a+b,a)\). The standard invertible centralizer count is
\[
q^{(a+b+c)^2+(a+b)^2+a^2}
\gamma_a(q)\gamma_b(q)\gamma_c(q).
\]
Dividing \(G_n(q)\) by this count and multiplying by \(q^{n-r}\) proves the third formula. Each asserted range of ranks follows by selecting the listed blocks (or simple/irreducible summands); for the characteristic-three upper bound, each nilpotent Jordan block has rank at most two-thirds of its dimension.

### Dimension asymptotics

The infinite product \(\gamma_\infty(q)=\prod_{j\ge1}(1-q^{-j})\) is strictly positive. Thus every factor \(G_m(q)\) lies between \(\gamma_\infty(q)q^{m^2}\) and \(q^{m^2}\); the same fixed-\(q\) bounds apply to each \(\gamma_m(q)\).

For all **admissible** ranks \(r\), the exact expressions above imply uniform two-sided estimates, with constants depending only on \(q\):
\[
H_{n,q}(r)\asymp_q
q^{\,n^2-(n-r)^2-r^2/2+n-r}
=q^{\,S_n-\frac32(r-r_n)^2},
\quad
S_n=\frac{2n^2}{3}+\frac n3+\frac16,
\quad r_n=\frac{2n-1}{3}.
\]
Here \(F\asymp_q G\) means both their ratio and its reciprocal are bounded above independently of \(n,r\). To justify the uniformity, in the split case set \(b=r/2+d\); the additional sum over \(b\) is bounded above by a constant times \(\sum_{d\in\frac12\mathbb Z}q^{-2d^2}\), while a nearest-to-balanced term gives the lower bound. In the nonsplit case the centralizer exponent is exactly \((n-r)^2+r^2/2\). In characteristic three write the remaining two column lengths as \((r/2+d,r/2-d)\); the same Gaussian sum bounds the block-type sum. The balanced choice is feasible for each \(r\le\lfloor2n/3\rfloor\): its larger column length is at most \(n-r\). Since the centralizer factors \(\gamma_a,\gamma_b,\gamma_c\) are uniformly bounded above and below, all constants are independent of the dimension.

Every field regime has an admissible integer rank within distance one of \(r_n\) (an even rank in the nonsplit case). Summing these Gaussian weights over the permitted integer lattice yields
\[
\sum_rH_{n,q}(r)\asymp_q q^{S_n}.
\]
The same comparison, restricted to \(|r-r_n|\ge t\), gives the stated tail estimate because the discrete Gaussian tails are bounded by a fixed \(q\)-dependent multiple of \(q^{-t^2}\). Finally, the weighted sum \(\sum_rH_{n,q}(r)q^{-r}\) is comparable to \(q^{S_n-r_n}\): the upper bound follows by completing the square, and the lower bound from an admissible rank within distance one of \(r_n\). Dividing by \(\sum_rH_{n,q}(r)\) gives \(\mathbb E[X_{n,q}]\asymp_qq^{-r_n}\asymp_q q^{-2n/3}\). This proves both assertions, including the characteristic-three truncation.

## Verification

The standalone script `verify.py` reconstructs finite-field arithmetic (including \(\mathbb F_4\) and \(\mathbb F_9\)), enumerates all candidate matrices of size up to three, tests \(A^3=-I\), calculates the rank, and independently compares every rank-stratum count to the displayed formulas in fourteen field/dimension configurations. In seven small configurations it also enumerates the admissible translation vectors and directly checks semisymmetry and the exact number of commuting pairs of **each** resulting operation. All checks returned `VERIFY_OK`. The script uses only Python's standard library; run `python verify.py`.

## Relationship to prior work

Allsop and Wanless determine the possible numbers of commuting ordered pairs among quasigroups of any specified finite order; their conclusion explicitly invites study within more structured families. That general existence spectrum does **not** determine how many labelled **affine semisymmetric** operations realize each count or their conditioned large-dimensional distribution. Smith and Wang give the linear semisymmetry criterion \(\rho^3=-I\), which is used here as background; our contribution is the finite-field commuting-pair census and the two-thirds concentration law. Fulman's exposition of the general finite-field matrix cycle index includes centralizer formulas from which the matrix-class terms above can be specialized; hence those centralizer identities are **not** claimed new. The novelty asserted here is the quasigroup-specific translation weighting, complete conditional distribution, and uniform dimension asymptotics across all characteristics. Kozlik investigates nuclei of semisymmetric quasigroups, a different invariant, and the current result does not assert anything about their nuclei. Related quadratic-quasigroup classifications concern a smaller, differently parametrized class and do not provide these conditional distributions.

## Limitations

The distribution counts distinct affine operations on a fixed coordinate vector space, not isomorphism classes and not non-affine semisymmetric quasigroups. Constants in the mean and Gaussian-tail estimates depend on the field size; no explicit sharp constants or convergence of the rescaled expected commuting fraction is asserted. The exact finite formulas are based on established matrix conjugacy and centralizer counts; they are supplied to make the conditional distribution reproducible, not as independent discoveries of new finite-field matrix identities. The paper on semisymmetric quasigroup nuclei was accessible in abstract form only, so additional overlap in its full text cannot be completely excluded; independent expert validation has not been performed.

## References

1. J. Allsop and I. M. Wanless, *Commuting Pairs in Quasigroups*, arXiv:2412.08107 (first version 2024-12-11); Journal of Combinatorial Designs (2025), DOI:10.1002/jcd.21994. https://arxiv.org/abs/2412.08107 ; https://doi.org/10.1002/jcd.21994
2. J. D. H. Smith and S. G. Wang, *Quasigroup Words and Reversible Automata*, arXiv:1911.08393 (2019), especially Section 6.3.1. https://arxiv.org/abs/1911.08393
3. J. Fulman, *Random Matrix Theory over Finite Fields*, survey notes (2004), Section 2.1, including the Kung–Stong cycle-index and centralizer formulas. https://ocw.mit.edu/courses/18-996-random-matrix-theory-and-its-applications-spring-2004/8b95d016309930598ececb496e983f2c_s_0273.pdf
4. A. R. Kozlik, *The Nucleus of a Semisymmetric Quasigroup*, arXiv:2607.27872 (2026-07-30). https://arxiv.org/abs/2607.27872
5. *Isomorphisms of Quadratic Quasigroups*, Proceedings of the Edinburgh Mathematical Society, Section 2, especially Lemma 2.6. https://www.cambridge.org/core/journals/proceedings-of-the-edinburgh-mathematical-society/article/isomorphisms-of-quadratic-quasigroups/669ED39409230BA3A8C9672DFAE5B14C
