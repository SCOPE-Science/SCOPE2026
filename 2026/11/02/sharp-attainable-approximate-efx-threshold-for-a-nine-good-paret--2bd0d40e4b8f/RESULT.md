# Sharp attainable approximate-EFX threshold for a nine-good Pareto obstruction

## Finding

For the four-agent, nine-good positive additive valuation family of Mahabadi, Ramakrishnan, and Tarnawski (arXiv:2610.29201v1, Theorem 2), the maximum approximate-EFX factor among complete Pareto-optimal allocations is **exactly**
\[
\alpha_K^*=\frac{2K+3}{3K}=\frac23+\frac1K\qquad (K\in\mathbb Z,\ K\ge6).
\]
Thus the strict upper bound proved in the cited paper is attained at its boundary, for **every** parameter of the family. A boundary-attaining allocation has utilitarian welfare precisely one unit below the maximum, while nonetheless being Pareto optimal.

## Assumptions and scope

There are four agents indexed \(1,2,3,4\) and nine indivisible goods \(x,y,a,b,c,d,e,p,q\). Each good is assigned to exactly one agent. The valuations are additive, strictly positive, and specified by the matrix, with rows in agent order and columns in good order,
\[
V_K=\begin{pmatrix}
3K&2K+2&K&K&1&1&K&2&1\\
2K+2&3K&1&K&K&1&K&1&2\\
3K&2K+2&1&1&K&K&K&2&1\\
2K+2&3K&K&1&1&K&K&1&2
\end{pmatrix},\quad K\in\mathbb Z,\ K\ge6.
\]
A complete allocation \(A=(A_1,A_2,A_3,A_4)\) is \(\alpha\)-EFX when
\[
v_i(A_i)\ge\alpha\,v_i(A_j\setminus\{g\})
\quad\text{for all }i\ne j\text{ and all }g\in A_j.
\]
An allocation is Pareto optimal if no complete allocation weakly improves all four agents and strictly improves at least one. Define its EFX factor as the largest \(\alpha\) satisfying the displayed comparisons (zero comparison values do not constrain the factor).

## Proof

**Upper bound from prior work.** Theorem 2 of Mahabadi--Ramakrishnan--Tarnawski proves that, for this exact valuation matrix and each integer \(K\ge6\), no Pareto-optimal complete allocation is \(\alpha\)-EFX for \(\alpha>2/3+1/K\). That published upper bound is used without claiming to reprove it.

**Boundary witness.** Let
\[
A_1=\{x,b\},\quad A_2=\{y\},\quad
A_3=\{c,d,p,q\},\quad A_4=\{a,e\}.
\]
The utility vector is \((4K,3K,2K+3,2K)\). For each \(i\ne j\), write \(D_{ij}=\max_{g\in A_j}v_i(A_j\setminus\{g\})\). The exact off-diagonal values are
\[
(D_{ij})=\begin{pmatrix}
-&0&4&K\\
2K+2&-&K+3&K\\
3K&0&-&K\\
2K+2&0&K+3&-
\end{pmatrix}.
\]
For \(K\ge6\), all twelve inequalities \(v_i(A_i)\ge [(2K+3)/(3K)]D_{ij}\) follow by multiplying positive denominators. In particular the potentially smallest competing ratio is \(2K/(2K+2)\), and its comparison with the proposed factor reduces to \(2K^2-10K-6\ge0\), true for \(K\ge6\). The other ratios dominate by direct inspection: for agent \(2\), \(3K/(2K+2)\), \(3K/(K+3)\), \(3K/K\); for agent \(1\), \(4K/4\), \(4K/K\); for agent \(3\), \((2K+3)/(3K)\), \((2K+3)/K\); and for agent \(4\), \(2K/(K+3)\), \(2K/(2K+2)\). The inequality for \(2K/(K+3)\) follows from \(6K^2\ge (K+3)(2K+3)\) at \(K\ge6\). Agent \(3\) against agent \(1\), after deleting good \(b\), attains equality. Hence the witness EFX factor is exactly \((2K+3)/(3K)\).

**Pareto optimality.** Each good's largest possible utility is, in column order, \((3K,3K,K,K,K,K,K,2,2)\). Therefore the maximum total welfare is \(11K+4\). The witness has total welfare \(11K+3\). If any allocation Pareto dominated the witness, integrality of all valuations would force the dominating allocation to have welfare at least \(11K+4\), hence precisely the welfare maximum. Every good must then go to an agent valuing it maximally.

In any such welfare-maximizing allocation that weakly dominates the witness, agent \(1\) must receive \(x\): without \(x\), the most agent \(1\) could receive from goods for which she is a maximizing agent is \(a,b,e,p\), totaling \(3K+2<4K\). Consequently agent \(3\) cannot receive \(x\). To reach her required \(2K+3\), she must receive each of \(c,d,e\), since any two of those plus \(p\) total at most \(2K+2\). Now agent \(2\) must receive \(y\), since without it, the remaining maximally valued goods available to her total at most \(K+2<3K\) (from \(b,q\)). This leaves agent \(4\) at most \(a,q\), worth \(K+2<2K\) to her. This contradicts weak domination. Thus the witness is Pareto optimal.

Combining the attained boundary with the paper's upper bound proves equality for every integer \(K\ge6\).

## Verification

Run `python3 verify.py` with Python 3. The script checks the symbolic witness factors with exact `Fraction` arithmetic for an explicit finite sample of parameter values, and exhaustively checks the absence of Pareto domination for several parameters by enumerating all \(4^9=262144\) complete allocations each. These computations corroborate, but do not replace, the proof for every \(K\ge6\).

## Relationship to prior work

The cited paper's Theorem 2 establishes the nonattainability of every factor strictly greater than \(2/3+1/K\). That **does not alone** imply the boundary factor is achievable while maintaining Pareto optimality. The present result supplies a single explicit allocation attaining the boundary for the whole family, plus an independent Pareto-optimality proof. The general existence question for a positive absolute approximate-EFX factor simultaneously with Pareto optimality remains open. Alkassar--Fouz--Mehlhorn's nine-good EFX existence theorem does not require Pareto optimality and therefore does not imply this boundary claim.

## Limitations

This is a sharp characterization of a particular published family, **not** a universal approximation factor for all additive instances. The published strict upper bound is an essential input. The all-parameter Pareto-optimality proof uses integrality and the valuation structure of this family; the finite verification alone would not establish the infinite theorem. Related unindexed treatments might contain an equivalent boundary construction.

## References

Mahabadi, S., Ramakrishnan, P., and Tarnawski, J. *Pareto Inefficiency of EFX*, arXiv:2610.29201v1 (first submitted October 21, 2026), Theorem 2 and Section 4. https://arxiv.org/html/2610.29201v1

Alkassar, E., Fouz, M., and Mehlhorn, K. *Complete EFX Allocations Exist for Four Additive Agents and Up to Nine Goods*, arXiv:2608.08590 (first submitted August 9, 2026). https://arxiv.org/abs/2608.08590
