# Exact strong-rotundity profiles and singular endpoint laws for scalar \(\ell_p\)-summands
## Finding
Let \(Y\ne\{0\}\) be a real Banach space. For \(1\le p\le\infty\), put
\[
X_p=\mathbb R\oplus_pY,
\qquad
x=(1,0),
\qquad
f(t,y)=t.
\]
For every \(\epsilon\in[0,2]\), García-Pacheco's **local** index of strong rotundity at the support pair \((x,f)\) is
\[
\boxed{\eta_{X_p}(\epsilon,(x,f))=
\begin{cases}
\epsilon/2,&p=1,\\[2pt]
G_p^{-1}(\epsilon^p),&1<p<\infty,\\[2pt]
0,&p=\infty,\quad0\le\epsilon\le1,\\[2pt]
\epsilon,&p=\infty,\quad1<\epsilon\le2,
\end{cases}}
\tag{1}
\]
where for finite \(p\)
\[
G_p(d)=d^p+1-|1-d|^p,
\qquad 0\le d\le2.
\tag{2}
\]
For \(1<p<\infty\), the function \(G_p\) is strictly increasing from \(0\) to \(2^p\), so its inverse in (1) is uniquely defined for the entire stated range.

The stronger, sharp **exposed-slice radius identity** is
\[
\boxed{
\sup_{\substack{z\in B_{X_p}\\ f(z)\ge1-d}}
\|z-x\|_p=
\begin{cases}
G_p(d)^{1/p},&1\le p<\infty,\\[2pt]
\max\{1,d\},&p=\infty,
\end{cases}
}
\qquad0\le d\le2.
\tag{3}
\]
All suprema are attained, regardless of the dimension, norm or reflexivity of the nonzero space \(Y\).

The formulas reveal two singular endpoint phenomena:
\[
\eta_{X_p}(1,(x,f))=\tfrac12\quad(1\le p<\infty),
\qquad
\eta_{X_\infty}(1,(x,f))=0,
\tag{4}
\]
whereas
\[
\eta_{X_1}(2,(x,f))=1,
\qquad
\eta_{X_p}(2,(x,f))=2\quad(1<p\le\infty).
\tag{5}
\]
For every fixed \(1<p<\infty\), the precise strong-exposure asymptotic is
\[
\eta_{X_p}(\epsilon,(x,f))
=\frac{\epsilon^p}{p}\bigl(1+o(1)\bigr)
\qquad(\epsilon\downarrow0).
\tag{6}
\]
At \(p=2\), (1) reduces to the previously published Hilbert/square-summand law \(\epsilon^2/2\); the non-Hilbert exponents and both endpoint discontinuities are the additional quantitative content.

## Assumptions and scope
All spaces and duals are over the reals. For \(p<\infty\), the norm on \(X_p\) is
\[
\|(t,y)\|_p=(|t|^p+\|y\|_Y^p)^{1/p},
\]
and for \(p=\infty\) it is \(\|(t,y)\|_\infty=\max\{|t|,\|y\|_Y\}\).

In the notation of García-Pacheco, a **local** strong-rotundity index is attached to a norm-one support pair \((x,f)\) with \(f(x)=1\). Let
\[
H=f^{-1}(\{1\}),
\qquad B=B_{X_p},
\]
and let \(U(x,\epsilon)\) denote the open norm ball of radius \(\epsilon\) about \(x\). By definition,
\[
\eta_{X_p}(\epsilon,(x,f))
=\operatorname{dist}\bigl(H,B\setminus U(x,\epsilon)\bigr).
\tag{7}
\]
In particular, the complement uses the **closed** distance constraint \(\|z-x\|_p\ge\epsilon\). Formula (1) is pointwise at the specified pair and does **not** claim the global infimum over all norm-one support pairs in \(X_p\).

## Proof
Fix a unit vector \(u\in Y\), which exists since \(Y\ne\{0\}\).

**Step 1: exact reduction to a one-variable problem.** For each \(z=(t,y)\in X_p\) with \(t\le1\), one has
\[
\operatorname{dist}(z,H)=1-t.
\tag{8}
\]
Indeed, every \(w\in H\) has \(\|w-z\|_p\ge |f(w-z)|=1-t\). Equality is attained at \(w=(1,y)\). Thus (7) becomes
\[
\eta_{X_p}(\epsilon,(x,f))
=\inf\{1-t: \|(t,y)\|_p\le1,\ \|(1-t,-y)\|_p\ge\epsilon\}.
\tag{9}
\]
All feasible points have \(-1\le t\le1\), hence \(0\le1-t\le2\).

**Step 2: the sharp slice radius for finite exponents.** Let \(1\le p<\infty\). For \(z=(t,y)\in B\),
\[
\|y\|_Y^p\le1-|t|^p,
\]
and consequently
\[
\|z-x\|_p^p
=(1-t)^p+\|y\|_Y^p
\le(1-t)^p+1-|t|^p.
\tag{10}
\]
The scalar function
\[
h_p(t)=(1-t)^p+1-|t|^p,
\qquad -1\le t\le1,
\]
is nonincreasing. For \(0\le t\le1\), each of \((1-t)^p\) and \(-t^p\) is nonincreasing. For \(-1\le t\le0\), its derivative when \(p>1\) is
\[
h_p'(t)=-p(1-t)^{p-1}+p(-t)^{p-1}<0.
\]
When \(p=1\), \(h_1(t)=2\) on \([-1,0]\). Therefore, imposing \(f(z)=t\ge1-d\) in (10) gives
\[
\|z-x\|_p^p\le h_p(1-d)
=d^p+1-|1-d|^p=G_p(d).
\tag{11}
\]
Equality is realized at
\[
z_d=
\left(1-d,\ (1-|1-d|^p)^{1/p}u\right),
\tag{12}
\]
which belongs to \(S_{X_p}\) and satisfies \(f(z_d)=1-d\). This proves (3) for every finite \(p\), including \(d=0,2\).

**Step 3: inversion.** By (9)--(12), the exact local index is
\[
\eta_{X_p}(\epsilon,(x,f))
=\inf\{d\in[0,2]:G_p(d)\ge\epsilon^p\}.
\tag{13}
\]
For \(p=1\),
\[
G_1(d)=2\min\{d,1\},
\]
so (13) gives \(\eta_{X_1}(\epsilon,(x,f))=\epsilon/2\) throughout \([0,2]\), including \(\epsilon=2\).

If \(1<p<\infty\), then on \(0<d<1\),
\[
G_p'(d)=p d^{p-1}+p(1-d)^{p-1}>0,
\]
whereas on \(1<d<2\),
\[
G_p'(d)=p\bigl(d^{p-1}-(d-1)^{p-1}\bigr)>0.
\]
Moreover \(G_p(0)=0\), \(G_p(2)=2^p\). Hence (13) is uniquely inverted to give the middle case of (1).

**Step 4: the sup-sum endpoint.** For \(p=\infty\), the unit-ball condition reads \(|t|\le1\), \(\|y\|_Y\le1\), and
\[
\|z-x\|_\infty=\max\{1-t,\|y\|_Y\}.
\]
For \(t\ge1-d\), the largest possible distance is \(\max\{d,1\}\), attained at \(z=(1-d,u)\) when \(0\le d\le2\). The exact index is therefore
\[
\inf\{d\in[0,2]:\max\{d,1\}\ge\epsilon\},
\]
which equals \(0\) for \(0\le\epsilon\le1\) and \(\epsilon\) for \(1<\epsilon\le2\). This completes (1)--(3).

**Step 5: sharp phase values and asymptotics.** For every finite \(p\),
\[
G_p(1/2)=(1/2)^p+1-(1/2)^p=1.
\]
For finite \(p=1\) the minimum solution is \(d=1/2\), and for \(p>1\) it is the unique solution. This proves (4). Formula (5) follows from \(G_1(1)=2\), the strict increase \(G_p(2)=2^p\) for \(p>1\), and the endpoint formula.

Finally, when \(p>1\) and \(d\downarrow0\),
\[
G_p(d)=d^p+1-(1-d)^p=p d+o(d).
\]
Since \(\epsilon^p=G_p(d)\) and \(d\downarrow0\) with \(\epsilon\downarrow0\), this proves (6). More generally, the maximizing slice contact in (12) crosses the sign of its first coordinate precisely when
\[
\epsilon=2^{1/p},
\]
corresponding to \(d=1\), and is nonnegative below this threshold and negative above it for finite \(p>1\).

## Verification
The accompanying self-contained Python file `verify.py` evaluates the defining distance optimization in exact rational arithmetic for integer exponents and verifies the extremizing slice boundary points. It also checks random feasible points in two-dimensional scalar--fiber models, tests the inverse formulas at representative exponents, and confirms the special cases and endpoint pivots.

The numerical and finite tests are supplementary. The result for every real exponent and every nonzero real Banach space is proved by the exact norm identity, monotonicity of \(G_p\), and explicit attainment vectors in (8)--(13), not by a discretized search.

## Relationship to prior work
García-Pacheco introduced the local strong-rotundity index in 2023. Definition 2.1 is exactly (7), and Theorem 2.3 computes \(\epsilon^2/2\) for \(L^2\)-summand vectors; that known value is the case \(p=2\) of (1). Theorem 2.6 treats general \(L^p\)-summand vectors, but for a different question, namely sufficient conditions for stereographic projection pairs, and does not state (1) or (3) for \(p\ne2\). Proposition 2.2 of that paper also evaluates two particular \(\ell_\infty\) support pairs: it shows the endpoint value \(\eta(2)=2\) at the first coordinate vector and vanishing values at the all-ones vector. That known endpoint special case is not claimed as novel. It does not provide the intermediate-separation profile or its transition at \(\epsilon=1\).

Campos-Jiménez and García-Pacheco (2024) relate the index to the core of a unit sphere and give endpoint qualitative information. Their Theorems 3.4--3.5 address zero values at some pairs and characterizations at \(\epsilon=2\); they do not provide the complete local \(p\)-dependent profiles at a specified scalar-summand support pair.

Known estimates for moduli of local convexity and their relationship to strong rotundity are not an exact evaluation of the functional-distance quantity (7). The contribution here is the sharp exposed-slice profile, its inversion for every \(p\), the infinite-dimensional independence of the transverse norm, and two distinct noncommuting exponent endpoints.

## Limitations
The theorem is **local** at the canonical \(\ell_p\)-summand support pair, not the global infimum over every support pair. It is valid in every (possibly nonreflexive) nonzero real transverse Banach space but does not assert corresponding formulas for arbitrary vectors away from the scalar summand.

The \(p=2\) formula is already published, and the novelty claim is limited to the full \(p\)-range, the exact exposed-slice law and the endpoint transitions. Bibliographic and semantic searches do not exclude every equivalent unpublished or differently named derivation.

## References
1. F. J. García-Pacheco, “The index of strong rotundity,” *AIMS Mathematics* 8 (2023), 20477--20486, doi:10.3934/math.20231043. First public date printed in the original open-access PDF: 25 June 2023. Primary MSC 46B20.
2. A. Campos-Jiménez and F. J. García-Pacheco, “The core of the unit sphere of a Banach space,” *AIMS Mathematics* 9 (2024), 3440--3452, doi:10.3934/math.2024169. First public date 8 January 2024, primary MSC 46B20.
