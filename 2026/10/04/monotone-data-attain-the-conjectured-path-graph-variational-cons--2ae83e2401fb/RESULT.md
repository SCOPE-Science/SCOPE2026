# Monotone data attain the conjectured path-graph variational constant
## Finding
Let \(n\ge 3\). Write \(P_n\) for the path with vertices \(1,\dots,n\), with edges joining consecutive vertices, and let \(M_{P_n}\) be the centered Hardy--Littlewood maximal operator
\[
(M_{P_n}f)(i)=\max_{r\ge 0}\frac{1}{|B(i,r)|}\sum_{j\in B(i,r)}|f(j)|.
\]
For nonnegative monotone data, the conjectured sharp path constant is already exact.

If
\[
0\le f(1)\le f(2)\le\cdots\le f(n),
\]
then
\[
\operatorname{Var}(M_{P_n}f)
=
f(n)-\frac1n\sum_{j=1}^n f(j)
\le
\left(1-\frac1n\right)\bigl(f(n)-f(1)\bigr)
=
\left(1-\frac1n\right)\operatorname{Var}(f).
\]
If \(f\) is nonincreasing, then
\[
\operatorname{Var}(M_{P_n}f)
=
f(1)-\frac1n\sum_{j=1}^n f(j)
\le
\left(1-\frac1n\right)\operatorname{Var}(f).
\]
Hence the optimal constant restricted to nonnegative monotone functions is exactly
\[
1-\frac1n.
\]

For a nonconstant nondecreasing function, equality holds exactly when
\[
f(1)=f(2)=\cdots=f(n-1)<f(n).
\]
For a nonconstant nonincreasing function, equality holds exactly when
\[
f(1)>f(2)=\cdots=f(n).
\]
Constant functions give the trivial equality \(0=0\).

The recent path-graph conjecture asks for the same constant for every function on \(P_n\). Since \(M_{P_n}f=M_{P_n}|f|\) and \(\operatorname{Var}(|f|)\le \operatorname{Var}(f)\), any counterexample to the full conjecture could be chosen nonnegative. The result above therefore shows that a counterexample, if one exists, must have at least one change of monotonic direction.

## Assumptions and scope
The graph is the finite path \(P_n\) with the graph metric and counting measure. The maximal operator is centered and uses graph balls. Only the \(1\)-variation is considered. The theorem applies to nonnegative monotone data; it does not prove the full conjecture for arbitrary data.

The recent source formulates the path conjecture
\[
\mathbf C_{P_n}=1-\frac1n
\]
for every \(n\ge3\), reports numerical evidence through \(n\le10\), and explains that even the weaker uniform estimate \(\mathbf C_{P_n}\le1\) would imply the corresponding sharp bound on \(\mathbb Z\) and then on \(\mathbb R\).

## Proof
Assume first that \(f\) is nondecreasing. For an integer radius \(k\ge0\), set
\[
I_i^k=\{\max(1,i-k),\dots,\min(n,i+k)\}
\]
and
\[
A_k f(i)=\frac1{|I_i^k|}\sum_{j\in I_i^k}f(j).
\]
Only integer radii matter, because graph balls are unchanged between consecutive integer radii.

We claim that, for each fixed \(k\), the sequence \(i\mapsto A_k f(i)\) is nondecreasing. Passing from \(I_i^k\) to \(I_{i+1}^k\), exactly one of four things happens.

1. Both endpoints move one step to the right. The intervals have the same size and the outgoing value is no larger than the incoming value, so the average cannot decrease.
2. The left endpoint stays fixed and the right endpoint moves right. A new value at least as large as every previous value is appended, so the average cannot decrease.
3. The right endpoint stays fixed and the left endpoint moves right. A value no larger than the previous average is removed, so the average cannot decrease.
4. Both endpoints stay fixed, in which case the averages are equal.

Thus every \(A_k f\) is nondecreasing, and therefore their pointwise maximum \(M_{P_n}f\) is nondecreasing.

At the left endpoint, every centered ball is a prefix. Prefix averages of a nondecreasing sequence are nondecreasing as the prefix grows, so
\[
(M_{P_n}f)(1)=\frac1n\sum_{j=1}^n f(j).
\]
At the right endpoint, every ball average is at most \(f(n)\), while the singleton ball gives \(f(n)\). Hence
\[
(M_{P_n}f)(n)=f(n).
\]
Because \(M_{P_n}f\) is nondecreasing, its total variation telescopes:
\[
\operatorname{Var}(M_{P_n}f)
=
(M_{P_n}f)(n)-(M_{P_n}f)(1)
=
f(n)-\frac1n\sum_{j=1}^n f(j).
\]

Since \(f(j)\ge f(1)\) for \(1\le j\le n-1\),
\[
\frac1n\sum_{j=1}^n f(j)
\ge
\frac{(n-1)f(1)+f(n)}n.
\]
Therefore
\[
f(n)-\frac1n\sum_{j=1}^n f(j)
\le
\frac{n-1}n\bigl(f(n)-f(1)\bigr).
\]
For a monotone sequence,
\[
\operatorname{Var}(f)=f(n)-f(1),
\]
which proves the desired inequality.

If \(f\) is nonconstant, equality in the mean estimate occurs exactly when every intermediate value equals \(f(1)\), namely
\[
f(1)=\cdots=f(n-1)<f(n).
\]
This also shows sharpness, for example with \(f=(0,\dots,0,1)\).

The nonincreasing case follows either by the same argument or by reflecting the path. Then \(M_{P_n}f\) is nonincreasing, its left endpoint equals \(f(1)\), its right endpoint equals the global average, and the stated identity and equality characterization follow.

Finally, for arbitrary real \(g\),
\[
M_{P_n}g=M_{P_n}|g|
\]
by definition, while
\[
\operatorname{Var}(|g|)\le \operatorname{Var}(g)
\]
edge by edge. Thus any violation of the full conjectured inequality would yield a nonnegative violation after replacing \(g\) by \(|g|\). The monotone theorem excludes all nonnegative monotone candidates.

## Verification
The analytic proof is complete and does not rely on finite computation. A separate exact-rational checker enumerates every nondecreasing sequence of length \(3\) through \(8\) with values in \(\{0,1,2,3\}\). It verifies the exact endpoint formula, the sharp inequality, the equality classification, and the reflected nonincreasing case. The finite check is only a consistency test; it is not used as an infinite proof.

## Relationship to prior work
González-Riquelme, Kovač, and Madrid formulate the conjecture
\[
\mathbf C_{P_n}=1-\frac1n
\]
for every \(n\ge3\), report numerical evidence through \(n\le10\), and state that the full conjecture is expected to be difficult. Their paper does not state a monotone-data theorem; searches of the full text for “monotone” and “nondecreasing” return no occurrence.

Earlier finite-graph work establishes sharp constants for complete and star graphs and studies related discrete maximal inequalities, but the inspected sources do not imply the exact identity
\[
\operatorname{Var}(M_{P_n}f)
=
f(n)-\frac1n\sum_{j=1}^n f(j)
\]
for nondecreasing path data, nor its equality classification. The present result is a structured all-\(n\) slice of the open path problem and isolates oscillation as necessary for any counterexample.

## Limitations
The full path-graph conjecture remains open. The argument is specific to monotone data and \(1\)-variation. It does not control data with one or more changes of monotonic direction, and it does not address \(p\)-variation for \(p\ne1\). Targeted literature and database searches cannot exclude an unindexed folklore observation stated in different terminology.

## References
1. C. González-Riquelme, V. Kovač, J. Madrid, “Sharp variational inequalities for the Hardy--Littlewood maximal operator on finite undirected graphs,” arXiv:2603.12462, first posted 12 March 2026.
2. F. Liu, Q. Xue, “On the variation of the Hardy--Littlewood maximal functions on finite graphs,” Collectanea Mathematica 72 (2021), 333--349, DOI:10.1007/s13348-020-00290-6.
3. C. González-Riquelme, J. Madrid, “Sharp inequalities for maximal operators on finite graphs,” Journal of Geometric Analysis 31 (2021), 9708--9744, arXiv:2005.03146.
