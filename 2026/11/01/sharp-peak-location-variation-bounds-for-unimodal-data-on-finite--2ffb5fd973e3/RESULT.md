# Sharp peak-location variation bounds for unimodal data on finite paths

## Finding
For an integer \(n\ge 3\), let \(P_n\) be the path with vertices \(1,\ldots,n\), with its graph metric and counting measure. Define its centered maximal operator by
\[
(Mf)(i)=\max_{0\le r\le n-1}\frac{\sum_{j=\max(1,i-r)}^{\min(n,i+r)}|f(j)|}{\min(n,i+r)-\max(1,i-r)+1},
\]
and let \(\operatorname{Var}(f)=\sum_{i=1}^{n-1}|f(i+1)-f(i)|\).

**Theorem (unimodal preservation and peak-sensitive deficit).** For every nonnegative \(f\colon [n]\to\mathbb R\) and every \(k\in[n]\) for which
\[
f(1)\le\cdots\le f(k)\ge\cdots\ge f(n),
\]
the maximal function \(Mf\) has the same weak unimodality pattern, with \((Mf)(k)=p:=f(k)\). Moreover,
\[
\begin{aligned}
\operatorname{Var}(Mf)
&=2p-(Mf)(1)-(Mf)(n)\\
&\le2p-\frac1k\sum_{j=1}^k f(j)-\frac1{n-k+1}\sum_{j=k}^n f(j)\\
&\le\operatorname{Var}(f)-\frac{p-f(1)}k-\frac{p-f(n)}{n-k+1}.
\end{aligned}
\]
In particular, every nonnegative unimodal input obeys the full path-graph conjectured inequality
\[
\operatorname{Var}(Mf)\le\left(1-\frac1n\right)\operatorname{Var}(f).
\]
For a nonconstant nonnegative unimodal input, equality in this global bound holds precisely when \(f\) is a nonnegative constant baseline plus a positive point mass at one of the two *endpoint* vertices. Endpoint masses attain equality.

**Sharp interior-peak classification.** If \(2\le k\le n-1\), restrict to nonzero nonnegative unimodal inputs with \(f(1)=f(n)=0\) and peak at \(k\). Then the exact optimal variation constant is
\[
\boxed{\quad C_{n,k}^{\mathrm{peak},0}=1-\frac1{2k}-\frac1{2(n-k+1)}.\quad}
\]
Equality holds precisely for positive scalar multiples of the point mass at vertex \(k\). More quantitatively, writing \(p=f(k)>0\), every such input satisfies the sharp remainder
\[
C_{n,k}^{\mathrm{peak},0}\operatorname{Var}(f)-\operatorname{Var}(Mf)
\ge\frac1k\sum_{j=2}^{k-1}f(j)+\frac1{n-k+1}\sum_{j=k+1}^{n-1}f(j),
\]
where an empty sum equals zero. The right side vanishes for the unique extremizing ray.

## Assumptions and scope
All statements hold for real nonnegative sequences, for graph balls including the center, and for \(1\)-variation along consecutive edges. An interior peak \(k\) need not be the unique index attaining the maximum; the theorem includes plateaus. The final sharp constant is relative to inputs vanishing at both endpoints and *admitting* a peak at the designated interior index. No assumption of strict increases or decreases is used. Absolute values in the maximal-operator definition make nonnegativity a natural reduction, but replacing signed data by their absolute values may destroy unimodality.

## Proof
First prove preservation of unimodality. Fix \(1\le i<j\le k\) and a real threshold \(t\). We show that \((Mf)(i)>t\) implies \((Mf)(j)>t\). If \(f(j)>t\), this follows from the radius-zero ball. Otherwise, because \(f\) is nondecreasing on \([1,k]\), all values \(f(m)\) with \(m\le j\) are at most \(t\). If \((Mf)(i)>t\), some integer-radius ball \(I=B(i,r)\) has positive summed excess \(\sum_{m\in I}(f(m)-t)>0\); hence its right endpoint exceeds \(j\), and \(r>j-i\). Put \(s=r-(j-i)\ge0\). The ball \(J=B(j,s)\) has the same right endpoint as \(I\), and its left endpoint is no smaller. Consequently \(J\subseteq I\), and every point of \(I\setminus J\) lies to the left of \(j\), where \(f(m)-t\le0\). Removing such terms cannot decrease the summed excess. Thus \(\sum_{m\in J}(f(m)-t)>0\), whence \((Mf)(j)>t\). The implication holds for every \(t\), proving \((Mf)(i)\le(Mf)(j)\). Reflecting the path gives the corresponding nonincreasing conclusion for \(k\le i<j\le n\). Since every value of \(f\) is at most \(p\) and the singleton ball at \(k\) has average \(p\), we have \((Mf)(k)=p\).

By unimodality, variation telescopes on each side of the peak:
\[
\operatorname{Var}(Mf)=\bigl(p-(Mf)(1)\bigr)+\bigl(p-(Mf)(n)\bigr).
\]
The ball about vertex \(1\) of radius \(k-1\) is exactly \([1,k]\); the ball about \(n\) of radius \(n-k\) is \([k,n]\). Their averages give the two lower estimates used for the first inequality in the theorem. By monotonicity toward \(p\),
\[
\sum_{j=1}^k f(j)\ge(k-1)f(1)+p,
\qquad
\sum_{j=k}^n f(j)\ge p+(n-k)f(n).
\]
Substituting these into the preceding upper bound proves the peak-sensitive deficit. Since \(k\le n\) and \(n-k+1\le n\), and since \(\operatorname{Var}(f)=(p-f(1))+(p-f(n))\), the bound \(\operatorname{Var}(Mf)\le(1-1/n)\operatorname{Var}(f)\) follows.

For the equality statement in the global bound, if \(1<k<n\) and \(f\) is nonconstant then at least one of \(p-f(1),p-f(n)\) is positive, and both denominators are strictly below \(n\). Therefore equality is impossible. If \(k=n\), the sequence is nondecreasing; its right endpoint is \(p\), and its left maximal value equals the *whole-sequence average* (prefix averages increase with prefix length). Equality in \(\operatorname{Var}(Mf)\le(1-1/n)\operatorname{Var}(f)\) requires \(f(1)=\cdots=f(n-1)<p\), which is a nonnegative constant baseline plus a positive endpoint mass. For such a positive baseline \(b\), \(M(b\mathbf1+c\mathbf1_{\{n\}})=b+M(c\mathbf1_{\{n\}})\), so equality indeed holds for any \(b\ge0\) and \(c>0\). The case \(k=1\) is the reflection. Thus the full nonconstant equality class is precisely an endpoint point mass added to a nonnegative constant baseline.

Now fix \(2\le k\le n-1\) and \(f(1)=f(n)=0\). Then \(\operatorname{Var}(f)=2p\), and the first inequality above specializes to
\[
\operatorname{Var}(Mf)\le2p-\frac{p}{k}-\frac{p}{n-k+1}
-\frac1k\sum_{j=2}^{k-1}f(j)-\frac1{n-k+1}\sum_{j=k+1}^{n-1}f(j).
\]
This is the stated remainder. For the singleton \(f=p\mathbf1_{\{k\}}\), one has \((Mf)(1)=p/k\) and \((Mf)(n)=p/(n-k+1)\), so the upper bound is attained and the constant is sharp. Conversely, equality requires each nonnegative term in the remainder to vanish. The two sums then force \(f(j)=0\) for every \(j\ne k\). This completes the classification. \(\square\)

## Verification
The proof is analytical for every \(n\ge3\), every admissible peak index and arbitrary real nonnegative input. The standalone `check_unimodal.py` independently evaluates the finite radius maxima with exact rational arithmetic, verifies preservation of weak unimodality and all displayed inequalities, and checks sharpness and uniqueness for small integer samples. Invoke with `python check_unimodal.py`. Finite testing is a supplementary diagnostic, not an infinite-dimensional proof or a certificate of literature priority.

## Relationship to prior work
González-Riquelme, Kovač, and Madrid (arXiv:2603.12462, first submitted 12 March 2026) conjectured that the sharp full-path \(1\)-variation constant is \(1-1/n\). Their manuscript treats complete graphs exactly and reports path computations for small sizes but does not give an all-size theorem for unimodal inputs or a peak-dependent sharp constant. Earlier exact results for nonnegative *monotone* path data provide the same global factor and endpoint-mass equality classification in the boundary-peak case; they do not determine the nonmonotone, interior-peak extremal profile or the rigidity remainder.

Bilz and Weigt's work on variation of centered maximal functions treats indicator functions on the whole line and integer lattice, with a broader special function class. That result does not directly provide the finite-path, boundary-truncated, peak-location-dependent exact ratio or the all-n classification here. The new contribution is an exact peak-dependent subproblem and a preservation principle, not a proof of the unrestricted conjecture.

## Limitations
This result does not settle the sharp \(1\)-variation inequality for path inputs with two or more changes of monotonic direction. The explicitly sharp position-dependent constant assumes a nonnegative input with zero values at both endpoints. No result is asserted for arbitrary graphs, higher-dimensional lattices, or other variation exponents. The originality comparison is limited to identifiable and inspected literature; earlier equivalent folklore under different terminology cannot be categorically excluded. The proof and checker have not undergone independent external validation.

## References
1. C. González-Riquelme, V. Kovač, J. Madrid, *Sharp variational inequalities for the Hardy–Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462, first submitted 2026-03-12, https://arxiv.org/abs/2603.12462.
2. C. Bilz, J. Weigt, *The One-Dimensional Centred Maximal Function Diminishes the Variation of Indicator Functions*, Journal of Geometric Analysis 35 (2025), article 256, DOI:10.1007/s12220-025-01965-x, https://doi.org/10.1007/s12220-025-01965-x.
3. F. Liu, Q. Xue, *On the variation of the Hardy–Littlewood maximal functions on finite graphs*, Collectanea Mathematica 72 (2021), 333–349, DOI:10.1007/s13348-020-00290-6.
