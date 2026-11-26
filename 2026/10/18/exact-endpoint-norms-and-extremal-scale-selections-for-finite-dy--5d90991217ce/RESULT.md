# Equality cases for the finite dyadic Haar endpoint norm

## Finding

Let \(E_m\) be conditional expectation on the dyadic filtration of \([0,1]\), with \(E_0 f=\int_0^1f\). For integer \(d\ge1\), put \(D_m=E_m-E_{m-1}\) for \(1\le m\le d\) and \(P_S=\sum_{m\in S}D_m\), where \(S\subseteq\{1,\ldots,d\}\). Write \(b_m=\mathbf 1_{\{m\in S\}}\). The equality cases for the maximum \(L^1\)-operator norm are precisely:

- At \(d=1\) the selector is \((1)\); at \(d=2\) it is \((1,1)\).
- At \(d\ge3\) there are exactly two: \(b_1=b_d=1\), and \(b_2,\ldots,b_{d-1}\) alternate, starting with either zero or one. The last digit is set to one independently of that alternation.

Equivalently, for the Walsh–Paley Lebesgue constants \(L_N\), the only maximizing indices in \(0\le N<2^d\) for \(d\ge3\) are
\[
N=\frac{2^{d+1}+(-1)^d}{3}\qquad\text{and}\qquad
N=\frac{5\,2^{d-1}-(-1)^d}{3}.
\]
At \(d=1,2\) they are \(1,3\), respectively. The sharp value is
\[
\frac d3+\frac79+\frac{(-1)^d}{9\,2^{d-1}}.
\]
This value is already in the Walsh/discrepancy literature [1, 2]. The contribution here is the necessary-and-sufficient equality classification, in particular exclusion of all other selectors or Walsh indices, not a new calculation of the maximum or of its logarithmic growth.

## Assumptions and scope

Use Lebesgue probability measure and either real or complex scalars. The selectors are scale-homogeneous: a chosen level includes all its Haar functions. The theorem does not optimize arbitrary subsets of individual Haar functions or general martingale multipliers. The usual finite dyadic atoms may be represented as binary strings; endpoints of atoms have no effect on the operator norms.

## Relation to the known maximum

Let \(w_j\) denote the Walsh–Paley characters on the dyadic group, so \(w_iw_j=w_{i\,\mathrm{xor}\,j}\) and the frequency block of \(D_m\) is \([2^{m-1},2^m)\). Set \(N=\sum_{m=1}^{d}b_m2^{m-1}\). The highest nonzero bit of \(N\,\mathrm{xor}\,j\) for \(j<N\) must be a bit set in \(N\); conversely, xoring \(N\) with a number in any such block gives a smaller index. Consequently
\[
N\,\mathrm{xor}\,[0,N)=\bigcup_{b_m=1}[2^{m-1},2^m).
\]
Conjugation by multiplication with \(w_N\) is isometric on \(L^1\) and carries the \(N\)-term Walsh projection to \(P_S\). The \(L^1\)-norm of the Walsh projection is \(L_N\), by convolution and the identical absolute column sums on the finite dyadic group. Thus the two equality problems are identical.

Dick–Pillichshammer [1, Theorem 2] identify \(L_N\) with the non-normalized star discrepancy of the binary van der Corput sequence. On p. 4 they give the displayed exact maximum on a dyadic block and exhibit the first index above, citing Faure [2, Lemme 4.1]. For \(d\ge2\) the attaining index is in \([2^{d-1},2^d)\); the same formula for the overall range follows from the smaller values on earlier blocks, or from the proof below. The closed-block endpoint at \(d=1\) is not in the optimizing range here. Fine's pointwise formula, reproduced in [1, Theorem 1], is not claimed as new. The all-depth argument below is included to prove the exact equality criterion, and gives an independent computation of the known value in the same notation.

## Proof of the equality classification

The norm of \(P_S=P_SE_d\) equals its norm on functions constant on the depth-\(d\) atoms, since \(E_d\) is contractive and fixes that space. All columns of the matrix have the same absolute sum by dyadic symmetry, and this sum is its \(\ell^1\) norm for either scalar field. Fix an input atom and put \(A_\ell=\sum_{m=1}^{\ell}b_m2^{m-1}\), \(A_0=0\). The entry for an output atom sharing exactly the first \(\ell<d\) digits is \(2^{-d}(A_\ell-b_{\ell+1}2^\ell)\), and at the input atom it is \(2^{-d}A_d\). There are \(2^{d-\ell-1}\) entries in the former shell. With \(t_m=A_m/2^m\), this gives
\[
t_0=0,\qquad t_m=(t_{m-1}+b_m)/2,\qquad
\|P_S\|_{1\to1}=\tfrac12\sum_{m=1}^{d}|b_m-t_{m-1}|+t_d.
\]

Let \(V_k(t)\) be the maximum of this control objective with \(k\) choices remaining, given initial state \(t\in[0,1]\). The two actions give
\[
V_0(t)=t,\qquad V_k(t)=\max\{t/2+V_{k-1}(t/2),\ (1-t)/2+V_{k-1}((1+t)/2)\}.
\]
For one step, the alternatives are \(t\) and 1, so \(V_1(t)=1\) and the digit 1 is forced if \(t<1\). If \(V_{k-1}(t)=a+c|t-1/2|\) with \(0\le c<1\), the two alternatives for \(k\ge2\) are
\[
a+c/2+(1-c)t/2,\qquad a+1/2-(1-c)t/2.
\]
They cross only at \(1/2\). Their maximum again has the stated form, with new coefficients \(a+(1+c)/4\) and \((1-c)/2\), so the strict condition \(c<1\) persists for every step. Therefore whenever at least two choices remain, the only optimal digit is 1 when \(t<1/2\), the only optimal digit is 0 when \(t>1/2\), and both are optimal exactly at \(t=1/2\).

Starting at zero forces the first digit to be 1, and then \(t_1=1/2\). If there is just one step left its forced digit is 1. Otherwise the second digit gives the only tie: the two corresponding new states are \(1/4,3/4\). All states thereafter are in \((0,1)\); for an interior state the strict rule maps it to the opposite open half without reaching \(1/2\). It follows that digits after the second alternate as long as at least two choices remain, and the final digit is forced by the one-step rule. This proves both necessity and sufficiency and rules out any further equality cases. Summing the selector digits as powers of two gives the two stated indices. For the value, iterating the coefficients from \(a_1=1,c_1=0\) gives \(a_k=k/3+11/18+(-1/2)^{k-1}/18\), \(c_k=(1-(-1/2)^{k-1})/3\); hence \(V_d(0)=a_d+c_d/2\) is the known sharp value.

## Verification and limitations

The retained standard-library script `checker.py` compares the shell expression against the actual conditional-expectation matrix through depth 6, then exactly exhausts all selectors through depth 15, comparing the full sets of maximizers. Those finite checks are supplementary; the strict Bellman comparison proves that no equality case can be missed at any depth. The inspected Walsh/discrepancy maximum statement exhibits an attaining index without claiming to list all of them. The classification is asserted as distinct only to the extent supported by accessible comparisons; older equivalent equality treatments cannot be excluded. The result does not extend the equality analysis to irregular filtrations or unrestricted Haar selections.

## References

1. J. Dick and F. Pillichshammer, *Lebesgue constants for the Walsh system and the discrepancy of the van der Corput sequence*, [arXiv:2412.03164v1](https://arxiv.org/abs/2412.03164v1), Theorems 1–2 and p. 4.
2. H. Faure, *Discrépance quadratique de la suite de van der Corput et de sa symétrique*, Acta Arith. 55 (1990), 333–350, [DOI 10.4064/aa-55-4-333-350](https://doi.org/10.4064/aa-55-4-333-350), Lemme 4.1 as cited in [1].
3. A. Seeger and T. Ullrich, *Lower bounds for Haar projections: deterministic examples*, [arXiv:1511.01470v1](https://arxiv.org/abs/1511.01470v1). Its smoothness-space estimates are distinct from this endpoint equality problem.
