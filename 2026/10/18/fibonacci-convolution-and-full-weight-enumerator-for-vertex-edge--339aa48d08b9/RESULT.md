# Fibonacci convolution and full weight enumerator for vertex–edge perfect Roman functions on paths

## Finding

For each integer \(n\geq0\), let \(P_n\) be the path on \(n\) named vertices (including the empty path \(P_0\)). A vertex–edge perfect Roman function is a labeling \(f:V(P_n)\to\{0,1,2\}\) for which each edge \(uv\) has either a positive endpoint or an endpoint adjacent to **exactly one** vertex labeled \(2\). Let \(\Phi_n(z)=\sum_f z^{\sum_v f(v)}\), summed over all such functions, with \(\Phi_0(z)=1\). Then the complete bivariate generating function is

\[
\boxed{\sum_{n\geq0}\Phi_n(z)x^n
=\frac{1+x+x^3z^2}{1-xz-xz^2-x^2z-x^2z^2-x^3z^2-x^4z^2-x^4z^3}.}
\]

For every \(n\geq1\), the minimum weight is \(\lfloor n/2\rfloor\). Write \(m_n=[z^{\lfloor n/2\rfloor}]\Phi_n(z)\), and set \(m_0=1\). If \(\mathrm{Fib}_0=0\), \(\mathrm{Fib}_1=1\), and \(\mathrm{Fib}_{j+2}=\mathrm{Fib}_{j+1}+\mathrm{Fib}_j\), then for every integer \(k\geq0\),

\[
\boxed{m_{2k+1}=\mathrm{Fib}_{k+1},\qquad
m_{2k}=\sum_{j=0}^{k}\mathrm{Fib}_{j+1}\mathrm{Fib}_{k-j+1}.}
\]

Equivalently, the odd and even optimal-multiplicity series are \(\sum_{k\geq0}m_{2k+1}q^k=(1-q-q^2)^{-1}\) and \(\sum_{k\geq0}m_{2k}q^k=(1-q-q^2)^{-2}\). These are counts of distinct **labeled-vertex** functions; reversal is not identified.

## Assumptions and scope

Graphs are finite and simple, vertex labels have weights \(0\), \(1\), and \(2\), and adjacency is within the path. No additional requirement is imposed on positive vertices. All identities are identities of formal power series in the stated variables. The empty path is included only to make the generating function convenient; the original parameter is ordinarily discussed for nonempty graphs.

## Proof

**1. Local criterion.** Consider an edge between consecutive vertices whose two labels are \(0\). Each endpoint has at most one other path neighbor. Thus its vertex–edge perfect Roman condition is equivalent to: the label immediately preceding that pair is \(2\), or the label immediately following it is \(2\). A missing boundary neighbor never contributes a label \(2\). Every edge with a positive endpoint already satisfies the definition.

**2. Zero-run decomposition.** For a nonempty word containing a positive label, distinguish its positive letters (each \(1\) or \(2\)) and the maximal zero runs between and outside them. An internal zero run has length at most three. A run of length two is allowed precisely when at least one adjacent positive letter is \(2\); a run of length three precisely when both are \(2\). Runs of length zero or one are unrestricted. A boundary zero run has length at most two, with length two possible precisely when its single adjacent positive letter is \(2\). These statements follow directly by checking the leftmost and rightmost adjacent-zero pairs; a run of four contains a pair protected on neither side. If a word has no positive letters, only lengths zero or one are feasible.

**3. Two-letter transfer.** Let \(a,b\in\{1,2\}\) denote successive positive labels. A boundary run contributes \(L_1(x)=1+x\) or \(L_2(x)=1+x+x^2\). The internal gap contributes \(H_{11}(x)=1+x\), \(H_{12}(x)=H_{21}(x)=1+x+x^2\), or \(H_{22}(x)=1+x+x^2+x^3\). The following matrices/vectors therefore count all possible sequences of positive labels and their uniquely determined zero runs:

\[
\begin{aligned}
U&=\begin{pmatrix}xz(1+x)&xz^2(1+x+x^2)\end{pmatrix},\\
M&=\begin{pmatrix}
xz(1+x)&xz^2(1+x+x^2)\\
xz(1+x+x^2)&xz^2(1+x+x^2+x^3)
\end{pmatrix},\\
V&=\begin{pmatrix}1+x\\1+x+x^2\end{pmatrix}.
\end{aligned}
\]

There is exactly one decomposition per feasible word, hence
\[
\sum_{n\geq0}\Phi_n(z)x^n=1+x+U(I-M)^{-1}V.
\]

The determinant of \(I-M\) is
\[
1-xz-xz^2-x^2z-x^2z^2-x^3z^2-x^4z^2-x^4z^3,
\]
using \((1+x)(1+x+x^2+x^3)-(1+x+x^2)^2=-x^2\). Expanding the two-by-two inverse and combining the \(1+x\) term gives the claimed numerator \(1+x+x^3z^2\). Because \(M\) has no constant term in \(x\), inversion is valid in formal power series.

**4. Minimum-weight boundary.** Substitute \(x=y/t\) and \(z=t^2\) into the exact generating function. A monomial corresponding to length \(n\) and weight \(w\) acquires \(t^{2w-n}y^n\). Put \(D(y)=1-y^2-y^4\). Direct substitution gives
\[
\mathcal G(y,t)=\frac{y/t+1+y^3t}{D(y)-t(y+y^3)-t^2(y^2+y^4)-t^3y}.
\]

As \(D(y)\) has constant term one, the expression has no power of \(t\) below \(-1\) when expanded coefficientwise in \(y\). Thus \(2w-n\geq-1\) for all feasible words, proving \(w\geq\lfloor n/2\rfloor\). The coefficients of \(t^{-1}\) and \(t^0\) are exactly
\[
[t^{-1}]\mathcal G=\frac{y}{D(y)},\qquad
[t^0]\mathcal G=\frac1{D(y)}+\frac{y^2+y^4}{D(y)^2}=\frac1{D(y)^2}.
\]

For odd lengths only exponent \(-1\) reaches the lower bound, and for even lengths only exponent \(0\) reaches it. The coefficients of \(D(y)^{-1}\) are positive Fibonacci numbers, as are those of its square; therefore the lower bound is achieved for every length. Replacing \(y^2\) by \(q\) gives the two exact minimum-multiplicity identities.

## Verification

The standalone file `verify_paths.py` exhaustively tests the original edge condition on all \(797{,}161\) ternary words of lengths zero through twelve, independently of the zero-run decomposition. It compares each full weight histogram with coefficients generated from the displayed rational denominator. It then checks the minimum weights and Fibonacci/convolution coefficients for all lengths one through \(160\). Execution output is supplied in `verification_output.txt`. These are finite reproducibility checks, not substitutes for the unrestricted proof above.

## Relationship to prior work

Al Subaiei, AlMulhim and Akwu introduced vertex–edge perfect Roman domination, proved general complexity results and bounds, and in Proposition 1 obtained the scalar minimum \(\lfloor n/2\rfloor\) for paths. That minimum is **not** new here. The result above gives the complete weight enumerator and exact multiplicities at the known minimum. Broader logic-based bounded-treewidth techniques supply abstract counting algorithms but do not themselves state this particular two-letter transfer, closed rational series, or Fibonacci convolution. General Roman and other perfect-Roman labeling variants impose different edge conditions.

## Limitations

The rational series and Fibonacci formulas are proved for simple paths, not cycles or arbitrary trees. Complexity or optimized implementation for broader graph classes is not claimed. Originality comparisons are based on the inspected primary source and focused literature searches; complete bibliographic priority cannot be guaranteed. No independent scientific validation has been performed.

## References

1. B. Al Subaiei, A. AlMulhim, and A. D. Akwu, “Vertex-edge perfect Roman domination number,” *AIMS Mathematics* **8** (2023), 21472–21483; DOI: 10.3934/math.20231094. Public PDF: https://www.aimspress.com/aimspress-data/math/2023/9/PDF/math-08-09-1094.pdf (5 July 2023).
2. H. Naresh Kumar and Y. Venkatakrishnan, “Vertex-edge Roman domination,” *Kragujevac Journal of Mathematics* **45** (2021), 685–698 (earlier, nonperfect vertex–edge variant).
3. S. Arnborg, J. Lagergren, and D. Seese, “Easy problems for tree-decomposable graphs,” *Journal of Algorithms* **12** (1991), 308–340 (general bounded-treewidth evaluation context; not asserted to be a prior path-enumerator formula).
