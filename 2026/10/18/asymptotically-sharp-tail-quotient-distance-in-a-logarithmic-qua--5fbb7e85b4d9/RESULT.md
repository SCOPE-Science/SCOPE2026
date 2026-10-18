# Asymptotically sharp tail-quotient distance in a logarithmic quasi-Banach space

## Finding
Fix \(\theta>0\). In Berná's logarithmic quasi-Banach space \(X_\theta\), let \(\mathbf 1_A=\sum_{j\in A}e_j\) for a finite set \(A\subset\mathbb N\), and let
\[
T_N=\overline{\operatorname{span}\{e_j:j>N\}}^{\|\cdot\|_\theta},\qquad
q_\theta(u)=\sup_{N\ge1}\inf_{v\in T_N}\|u-v\|_\theta.
\]
For every fixed \(\theta>0\), uniformly over all finite \(A\) with \(|A|=m\),
\[
\boxed{\lim_{m\to\infty}\frac{q_\theta(\mathbf 1_A)}m=2.}
\]
More quantitatively, if \(L=\log m\ge e\) and
\[
\delta_m=\frac{3\log\log m+10+2/\theta}{\log m}\le\frac12,
\]
then
\[
\boxed{2-\delta_m\le\frac{q_\theta(\mathbf 1_A)}m\le2.}
\]
Consequently, because \(\|\mathbf 1_A\|_\theta=m(1+\theta\log m)\),
\[
\frac{\|\mathbf 1_A\|_\theta}{q_\theta(\mathbf 1_A)}
\sim\frac\theta2\log m.
\]
The same limit gives \(q_\theta(\mathbf1_A)/\|J\mathbf1_A\|_{X_\theta^{**}}\to2\), where \(J\) is the canonical map into the bidual. These are statements about the explicitly specified constant-coefficient blocks; no assertion is made for arbitrary vectors.

## Assumptions and scope
Work over either \(\mathbb R\) or \(\mathbb C\), with natural logarithms and \(\theta>0\) fixed independently of \(m\). On \(\ell_1\), define
\[
h_t(z)=z\log\max\{|z|,t\},\quad
S(x)=\sum_jx_j,\quad
F_t(x)=\sum_jh_t(x_j)-h_t(S(x)),\quad
H(x)=\sup_{t>0}|F_t(x)|.
\]
Define \(\|x\|_\theta=\|x\|_1+\theta H(x)\), and let \(X_\theta\) be the closure of finitely supported sequences under this quasi-norm, as in the cited source. Each coordinate functional is continuous. Thus a vector in \(T_N\) has zero coordinates through \(N\). Both the tail distance and the claimed limit are invariant under coordinate permutations, and the quantitative estimate holds for every choice of \(A\) with \(|A|=m\).

## Proof
**Upper bound.** Given \(N\ge1\), choose \(B\subset\{j>N\}\setminus A\) of cardinality \(m\), and let \(v=\mathbf1_B\in T_N\). By cancellation of equal positive and negative entries, \(S(\mathbf1_A-\mathbf1_B)=0\) and \(F_t(\mathbf1_A-\mathbf1_B)=0\) for every \(t>0\). Hence \(\|\mathbf1_A-v\|_\theta=2m\), so \(q_\theta(\mathbf1_A)\le2m\).

**Scale-one entropy obstruction.** Fix \(0<\delta\le1/2\), assume \(m\ge1/\delta\), and take \(N\ge\max A\). For \(v\in T_N\), write \(w=-v\), \(b=\|w\|_1\), and \(x=\mathbf1_A+w\). The supports of \(w\) and \(A\) are disjoint, so \(\|x\|_1=m+b\). If \(b\ge(1-\delta)m\), this alone gives \(\|x\|_\theta\ge(2-\delta)m\).

Otherwise \(b<(1-\delta)m\). Put \(V=\sum_jw_j\) and \(S=m+V\). Then \(\delta m<|S|<2m\), and in particular \(|S|\ge1\). Also \(|w_j|\le b<m\). At the single scale \(t=1\), define the absolutely convergent sum
\[
D=\sum_j w_j\log\frac{m}{\max\{|w_j|,1\}}.
\]
Each logarithm lies in \([0,\log m]\); consequently \(|D|\le b\log m\). Since \(h_1(1)=0\), direct substitution into the definition of \(F_1\) gives the exact identity
\[
F_1(x)=-m\log m-D-S\log\frac{|S|}{m}.
\]
The bounds \(\delta<|S|/m<2\) and \(|S|<2m\) imply
\[
\left|S\log\frac{|S|}{m}\right|\le2m\log(2/\delta).
\]
Thus the reverse triangle inequality yields
\[
H(x)\ge|F_1(x)|
\ge(m-b)\log m-2m\log(2/\delta)
\ge m\bigl(\delta\log m-2\log(2/\delta)\bigr).
\]
In particular, whenever
\[
\theta\bigl(\delta\log m-2\log(2/\delta)\bigr)\ge1,
\]
we have \(\|x\|_\theta\ge m+b+m\ge2m\). Combining the two cases shows that **every** \(v\in T_N\) satisfies \(\|\mathbf1_A-v\|_\theta\ge(2-\delta)m\). Taking the infimum over \(T_N\), then the supremum over \(N\), proves the same lower bound for \(q_\theta\).

**Effective choice and limit.** Take \(L=\log m\ge e\) and \(\delta=\delta_m\le1/2\) as stated. Because \(\delta_m\ge1/L\),
\[
\delta_m L-2\log(2/\delta_m)
\ge3\log L+10+2/\theta-2\log(2L)
=\log L+10+2/\theta-2\log2>1/\theta.
\]
Also \(\delta_m m\ge1\). The previous bound applies. As \(m\to\infty\), \(\delta_m\to0\), proving the sharp limit. Finally, the source's exact block quasi-norm is \(m(1+\theta\log m)\), and its bidual-image norm is \(m\); dividing by the tail-distance asymptotic gives both asserted corollaries. \(\square\)

## Verification
The proof is valid for arbitrary real or complex tail vectors, not only for finite or constant-coefficient competitors. The crucial identity is obtained by evaluating \(F_t\) at \(t=1\), with no optimization over \(t\) required. All sums are absolutely convergent because \(w\in\ell_1\) and \(|w_j|\le b<m\), so every coefficient of \(D\) is bounded by \(\log m\). Boundary assumptions \(\delta m\ge1\), \(0<\delta\le1/2\), and \(\theta>0\) are explicit. The companion `check_tail.py` evaluates the finite-support defect at every breakpoint and verifies defining cancellations and finite examples; these tests are diagnostic, not an infinite proof.

## Relationship to prior work
Berná, *A semi-greedy Markushevich basis which is not quasi-greedy* (arXiv:2610.05052v1, Sections 3, 5, 6), establishes \(m\le q_\theta(\mathbf1_A)\le2m\) and \(\|\mathbf1_A\|_\theta=m(1+\theta\log m)\). The present result identifies the sharp limiting endpoint \(2\) and a quantitative convergence bound; neither follows from those two-sided estimates alone.

*Logarithmic suppression conditionality in a semi-greedy non-quasi-greedy Markushevich basis* establishes the different invariant \(k_m(\theta)\asymp_\theta\log(m+1)\), with coefficient bounds, by studying norms of finite coordinate projections. Its full published result concerns \(k_m\), not the infimum over infinite-dimensional tail subspaces \(T_N\). Although both employ positive coordinate blocks, a bound for the supremum of projection ratios does not determine these tail-quotient distances. Earlier counterexamples by Albiac, Ansorena, Berasategui and Berná use other quasi-Banach constructions and do not supply the stated tail limit.

## Limitations
The result concerns the explicit quasi-norm \(\|\cdot\|_\theta\), not arbitrary equivalent renormings or general vectors. \(\theta\) must be fixed and positive; the proof does not give a uniform limit when \(\theta=\theta_m\to0\). The displayed convergence estimate need not give the optimal lower-order correction. No claim is made about the exact finite-\(m\) tail distance or the exact leading coefficient of general suppression conditionality constants. Independent priority review is not included.

## References
1. P. M. Berná, *A semi-greedy Markushevich basis which is not quasi-greedy*, arXiv:2610.05052v1, first posted 2026-10-04, https://arxiv.org/html/2610.05052v1.
2. *Logarithmic suppression conditionality in a semi-greedy non-quasi-greedy Markushevich basis*, published 2026-10-11, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-logarithmic-suppression-conditionality-in-a-semi-greedy-non-quas--d622ec85fec3/RESULT.md.
3. F. Albiac, J. L. Ansorena, M. Berasategui and P. M. Berná, *When Greedy Approximation Breaks: Counterexamples in Quasi-Banach Spaces*, arXiv:2510.13693v2, https://arxiv.org/html/2510.13693v2.
