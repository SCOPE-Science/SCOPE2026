# Finite-component obstruction law for global pair-correlation normalization
## Finding
Let \((X,d,T)\) be a metric dynamical system. Let \(X_1,\ldots,X_m\) be nonempty \(T\)-invariant subsets with \(m\ge 2\) and
\[
\Delta:=\min_{i\ne j}\operatorname{dist}(X_i,X_j)>0.
\]
For each \(i\), let \(\mu_i\) be a \(T\)-invariant probability measure supported on \(X_i\), let \(p_i>0\) with \(\sum_i p_i=1\), and define \(\mu:=\sum_i p_i\mu_i\). For any positive sequence \(r_n\to0\), write
\[
C_i(n):=\int \mu_i(B(x,r_n))\,d\mu_i(x),\qquad C_\mu(n):=\int \mu(B(x,r_n))\,d\mu(x).
\]
Assume \(C_i(n)/C_1(n)\to a_i\in(0,\infty)\) for every \(i\), and set
\[
A:=\sum_{j=1}^m p_j^2a_j.
\]

Define the single-orbit count
\[
S_n(x):=\#\{(u,v):0\le u\ne v<n,\ d(T^ux,T^vx)\le r_n\}.
\]
If, for every \(i\),
\[
\frac{S_n(x)}{n^2C_i(n)}\longrightarrow 1
\]
for \(\mu_i\)-almost every \(x\in X_i\), then
\[
\frac{S_n(x)}{n^2C_\mu(n)}\longrightarrow \frac{a_i}{A}
\]
for \(\mu_i\)-almost every \(x\in X_i\). In particular, this global-normalized limit cannot equal \(1\) for \(\mu\)-almost every \(x\).

For two orbits define
\[
Q_n(x,y):=\#\{(u,v):0\le u,v<n,\ d(T^ux,T^vy)\le r_n\}.
\]
If, for every \(i\),
\[
\frac{Q_n(x,y)}{n^2C_i(n)}\longrightarrow 1
\]
for \(\mu_i\otimes\mu_i\)-almost every \((x,y)\in X_i\times X_i\), then the global-normalized limit is
\[
\frac{Q_n(x,y)}{n^2C_\mu(n)}\longrightarrow
\begin{cases}
\frac{a_i}{A},& (x,y)\in X_i\times X_i,\\
0,&(x,y)\in X_i\times X_j,\ i\ne j,
\end{cases}
\]
for the corresponding product-almost-everywhere statements. Hence the global two-orbit i.i.d. normalization also cannot converge to \(1\) for \(\mu\otimes\mu\)-almost every pair when \(m\ge2\).

When the component correlation integrals have the same asymptotic scale, so that \(a_i=1\) for all \(i\), the same-component inflation factor is exactly
\[
\frac{1}{\sum_{j=1}^m p_j^2}.
\]
For equal weights this factor is \(m\).

## Assumptions and scope
The separation hypothesis is geometric and exact: the component supports must have a positive pairwise distance. The componentwise pair-correlation laws are assumptions, not conclusions of this result. No mixing hypothesis is needed beyond whatever is used separately to establish those local laws. The ratios \(C_i(n)/C_1(n)\) are assumed to converge to finite positive constants; no claim is made here when the component correlation integrals have incompatible orders.

The statement applies to any shrinking-radius sequence \(r_n\to0\), including the power scales \(r_n=s/n^\beta\) used in recent dynamical pair-correlation work, whenever the displayed componentwise hypotheses hold.

## Proof
Because \(r_n\to0\), for all sufficiently large \(n\) one has \(r_n<\Delta\). If \(x\in X_i\), then \(B(x,r_n)\) meets no \(X_j\) with \(j\ne i\). Since \(\mu_j\) is supported on \(X_j\),
\[
\mu(B(x,r_n))=p_i\mu_i(B(x,r_n)).
\]
Integrating this identity component by component gives the exact formula
\[
C_\mu(n)=\sum_{i=1}^m p_i^2C_i(n)
\]
for all sufficiently large \(n\). Dividing by \(C_1(n)\) yields
\[
\frac{C_\mu(n)}{C_1(n)}\longrightarrow A.
\]

If \(x\in X_i\), invariance of \(X_i\) gives \(T^ux\in X_i\) for every \(u\ge0\). Therefore the single-orbit count is exactly the count internal to component \(i\), so the assumed local law and the previous correlation-integral identity imply
\[
\frac{S_n(x)}{n^2C_\mu(n)}
=
\frac{S_n(x)}{n^2C_i(n)}\,
\frac{C_i(n)}{C_1(n)}\,
\frac{C_1(n)}{C_\mu(n)}
\longrightarrow \frac{a_i}{A}.
\]
If this limit were \(1\) for \(\mu\)-almost every \(x\), then positivity of every \(p_i\) would force \(a_i=A\) for every \(i\). Substituting into the definition of \(A\) would give
\[
A=A\sum_{i=1}^m p_i^2.
\]
Since \(A>0\) and \(m\ge2\) with every \(p_i>0\), one has \(\sum_i p_i^2<1\), a contradiction.

For two orbits, if \(x\in X_i\) and \(y\in X_j\) with \(i\ne j\), positive separation gives \(d(T^ux,T^vy)\ge\Delta>r_n\) for all sufficiently large \(n\) and all \(u,v\), hence \(Q_n(x,y)=0\). If \(x,y\in X_i\), the assumed local two-orbit law and the same three-factor calculation yield the limit \(a_i/A\). This proves all assertions.

## Verification
The proof was checked directly from the definitions. The only geometric step is that balls of radius below \(\Delta\) cannot cross between supports. The exact identity \(C_\mu(n)=\sum_i p_i^2C_i(n)\) was then substituted into both orbit normalizations. The impossibility of a global single-orbit limit \(1\) reduces to \(\sum_i p_i^2<1\) for a nontrivial positive probability vector. No numerical experiment or unproved asymptotic estimate is used.

## Relationship to prior work
Baker and Todd define the i.i.d.-matched single-orbit normalization using \(n^2\int\mu(B(z,r_n))\,d\mu(z)\), and analogously for two orbits, in arXiv:2606.17880v3. Their principal theorems impose quantitative mixing hypotheses. The present statement instead isolates what the same global normalization does after a finite positively separated invariant decomposition, assuming the required local pair-correlation laws component by component.

A public archived audit of version 2 of that manuscript exhibited a two-component piecewise-linear example in which same-component pair counts have an inflated limit and cross-component two-orbit counts vanish. The formula above recovers that mechanism and gives its exact finite-component and unequal-weight form. Aistleitner, Lachmann, and Pausinger proved that classical Poissonian pair correlation forces equidistribution and gave an \(L^2\)-density lower bound for non-equidistributed sequences; that result is conceptually related but does not provide the finite-component global-normalization identity or the componentwise limit formula above.

## Limitations
The theorem does not address components whose supports touch, countably infinite ergodic decompositions, rates of convergence, or cases in which the ratios \(C_i(n)/C_1(n)\) fail to converge. It also does not prove the componentwise local pair-correlation laws; those must come from separate dynamical hypotheses. The originality comparison found no matching statement in the checked sources and database searches, but an elementary decomposition identity of this kind may exist elsewhere as folklore.

## References
1. Simon Baker and Mike Todd, *Pair correlation statistics for dynamical systems*, arXiv:2606.17880v3 (2026).
2. Christoph Aistleitner, Thomas Lachmann, and Florian Pausinger, *Pair correlations and equidistribution*, Journal of Number Theory 182 (2018), 206–220, DOI 10.1016/j.jnt.2017.06.009.
