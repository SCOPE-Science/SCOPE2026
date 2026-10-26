# Sharp positivity horizon and transient norm of biharmonic heat on triangular graphs

## Finding
For every integer \(n\ge4\), consider the **triangular graph** \(T_n=J(n,2)\), whose vertices are the two-element subsets of \(\{1,\ldots,n\}\) and whose edges join intersecting distinct subsets. Let \(L_n\) be its unnormalized combinatorial Laplacian and let \(H_n(t)=\exp(-tL_n^2)\), \(t\ge0\). Write
\[
F_n(t)=(n-2)-2(n-1)e^{-n^2t}+ne^{-4(n-1)^2t}.
\]
Then the exact, sharp endpoint norms for counting-coordinate \(\ell^1\) and \(\ell^\infty\) are
\[
\boxed{\|H_n(t)\|_{1\to1}=\|H_n(t)\|_{\infty\to\infty}
=1+\frac{2(n-3)}{n(n-1)}[-F_n(t)]_+.}
\]
Here \([z]_+=\max\{z,0\}\). There is a unique \(\tau_n>0\) with \(F_n(\tau_n)=0\). **Entrywise positivity is exactly**
\[
\boxed{H_n(t)\ge0\text{ entrywise}\iff t=0\text{ or }t\ge\tau_n.}
\]
For \(0<t<\tau_n\) the only negative entries correspond to disjoint two-subsets; all intersecting entries and the diagonal are positive. At \(t=\tau_n\) exactly the disjoint entries vanish, and for \(t>\tau_n\) every entry is strictly positive.

The endpoint norm strictly increases from one to a unique maximum and then strictly decreases back to one. The unique maximizer is
\[
\boxed{\theta_n=\frac{\log(2(n-1)/n)}{(3n-2)(n-2)}},
\qquad 0<\theta_n<\tau_n,
\]
and its sharp value is the displayed norm formula evaluated at \(\theta_n\). A maximizing datum has value \(-1\) on vertices disjoint from a chosen vertex and \(+1\) on all other vertices.

Write \(r_*\in(0,1)\) for the unique root of \(r^3+r^2+r-1=0\). The complete large-graph scaling is
\[
\boxed{n^2\tau_n\longrightarrow-\log r_*,\qquad
n^2\theta_n\longrightarrow\frac{\log2}{3},\qquad
\max_{t\ge0}\|H_n(t)\|_{\infty\to\infty}\longrightarrow\frac{3}{2^{1/3}}-1.}
\]
A more sensitive distinction between this family and other three-spectrum graph families is the explicit first finite-size correction
\[
\boxed{\max_{t\ge0}\|H_n(t)\|_{\infty\to\infty}
=\frac3{2^{1/3}}-1
-\frac{\bigl(10+\tfrac83\log2\bigr)2^{-1/3}-8}{n}
+O(n^{-2}).}
\]
The positive coefficient in this defect is approximately \(1.4040753446\).

## Assumptions and scope
All graph edges have unit conductance. The Laplacian is \((L_nf)(S)=\sum_{T\sim S}(f(S)-f(T))\), not a normalized Laplacian. Operators act on real or complex functions on the \(N=\binom n2\) vertices with the usual coordinate \(\ell^1\), \(\ell^2\), or \(\ell^\infty\) norms. The proof includes \(n=4\) and all larger integers; time satisfies \(t\ge0\). Negative graph-heat entries do not contradict Hilbert-space contractivity \(\|H_n(t)\|_{2\to2}=1\).

## Proof
Let \(B\) be the \(N\)-by-\(n\) unoriented vertex/point incidence matrix: \(B_{S,i}=1\) when \(i\in S\). Thus \(BB^\top=A+2I\), where \(A\) is the adjacency matrix of \(T_n\), while \(B^\top B=(n-2)I+J\). The centered column space of \(B\) has orthogonal projector
\[
(E_1)_{S,T}=\frac{|S\cap T|-4/n}{n-2}.
\]
Let \(E_0=J/N\) and \(E_2=I-E_0-E_1\). From the preceding two incidence identities, these are pairwise orthogonal idempotents and
\[
L_n=nE_1+(2n-2)E_2.
\]
Consequently
\[
H_n(t)=E_0+uE_1+vE_2,\qquad
u=e^{-n^2t},\quad v=e^{-4(n-1)^2t}.
\]
For \(S\cap T=\varnothing\) its entry is
\[
h_0(t)=\frac{2F_n(t)}{n(n-1)(n-2)}.
\]
For distinct \(S,T\) with \(|S\cap T|=1\), it is
\[
h_1(t)=\frac{1-v}{N}+\frac{n-4}{n(n-2)}(u-v)>0
\quad(t>0),
\]
because \(n\ge4\) and \(0<v<u<1\). Every diagonal entry is also strictly positive as an exponential sum of nonnegative diagonal spectral-projector entries. Thus only disjoint entries can be negative. Each row contains exactly \(\binom{n-2}{2}\) such entries. Since every row sums to one and the matrix is symmetric,
\[
\|H_n(t)\|_{\infty\to\infty}=\|H_n(t)\|_{1\to1}
=1+2\binom{n-2}{2}[-h_0(t)]_+.
\]
This is the exact norm formula; the row sign pattern stated above attains it.

Differentiate the scalar function:
\[
F_n'(t)=2n(n-1)\bigl(ne^{-n^2t}-2(n-1)e^{-4(n-1)^2t}\bigr).
\]
Its parenthesis starts at \(2-n<0\) and has exactly one zero because the ratio of its two exponentials grows strictly with \(t\). Solving gives \(\theta_n\) above. Hence \(F_n\) first strictly decreases and then strictly increases. It starts at zero, has negative derivative, and tends to \(n-2>0\). There is therefore exactly one positive zero \(\tau_n>\theta_n\), proving every time-positivity and uniqueness claim.

For asymptotics put \(s=n^2t\). Uniformly on compact \(s\)-intervals,
\[
\frac{F_n(s/n^2)}n\longrightarrow f(s)=1-2e^{-s}+e^{-4s}.
\]
Writing \(r=e^{-s}\), the factorization \(f(s)=(1-r)(1-r-r^2-r^3)\) shows that the positive root is unique and simple, giving \(n^2\tau_n\to-\log r_*\). Direct expansion of the explicit \(\theta_n\) yields \(n^2\theta_n=\log2/3+O(1/n)\). At its minimum \(v/u=n/[2(n-1)]\). Substitute this into the exact peak norm to obtain
\[
\max_{t\ge0}\|H_n(t)\|_{\infty\to\infty}
=1+\frac{2(n-3)(n-2)}{n(n-1)}
\left[\frac{3n-2}{2(n-1)}e^{-n^2\theta_n}-1\right].
\]
Taylor-expanding \(n^2\theta_n=\log2/3+\bigl(8\log2/9-1/3\bigr)/n+O(n^{-2})\) in this exact expression proves both the limit and the displayed first-order correction.

## Verification
The accompanying `check.py` reconstructs the Johnson graph Laplacian independently from its adjacency relation for \(4\le n\le11\), checks the proposed projectors and their orthogonality using exact rational arithmetic, compares the time-dependent formulas with direct numerical matrix exponentials in smaller dimensions, and checks the stated asymptotic scales at several large values. It reports `CHECK_OK exact_and_numeric_assertions=65720` in a completed local run. Its finite checks are corroboration, not proof of the infinite-dimensional-parameter statements. Run `python check.py` with Python, NumPy and SciPy installed.

## Relationship to prior work
Daners, Glück and Kennedy developed general theories of eventual positivity for Banach-lattice semigroups, including finite-dimensional semigroups and fourth-order operators [1]. Their qualitative framework does not give this exact triangular-graph kernel, sharp endpoint modulus, unique peak, or the first finite-size correction. Standard triangular-graph incidence/spectral structure is described in [2] and is rederived here rather than used as a black box. Related three-spectral-value positivity results govern qualitative time-set structure, but do not by themselves determine these graph-specific sharp norm values. A previous exact treatment for rectangular rook graphs concerns different adjacency matrices; their results do not imply the finite-time formula here.

## Limitations
The theorem applies only to the specific complete-graph line-graph family \(J(n,2)\), the unnormalized squared Laplacian, and counting-coordinate endpoint norms. It does not classify arbitrary strongly regular graphs, time-dependent perturbations, other powers of the Laplacian, or eigenfunction localization. Novelty is assessed relative to inspected material and does not establish historical priority against every older source. No independent mathematical audit is claimed.

## References
[1] D. Daners, J. Glück, and J. B. Kennedy, *Eventually and asymptotically positive semigroups on Banach lattices*, arXiv:1511.05294, first posted 17 November 2015, https://arxiv.org/abs/1511.05294.

[2] E. W. Weisstein, *Triangular Graph*, MathWorld, https://mathworld.wolfram.com/TriangularGraph.html (graph definition and parameter reference).
