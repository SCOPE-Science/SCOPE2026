# Rational robust witnesses for the Bézout simplex characterization

## Statement

Let \(\mathcal K_n^n\) be the full-dimensional convex bodies in \(\mathbb R^n\), \(n\ge2\). For
\[
0\ne x\in \operatorname{int}(K-K),
\qquad
C_K(x):=K\cap(K-x),
\]
define the special-test Bézout defect
\[
\mathfrak D(K,x)
:=
V_n(K)\,V_n\!\bigl(K[n-2],[0,x],C_K(x)\bigr)
-
V_n\!\bigl(K[n-1],[0,x]\bigr)\,
V_n\!\bigl(K[n-1],C_K(x)\bigr).
\tag{1}
\]
Thus the Bézout inequality for the special pair
\[
A=[0,x],\qquad B=K\cap(K-x)
\]
is exactly \(\mathfrak D(K,x)\le0\).

The following strengthening of the recent Langharst--Wang simplex characterization holds.

**Theorem.** The map
\[
(K,x)\longmapsto \mathfrak D(K,x)
\]
is jointly continuous on
\[
\mathcal E_n
=
\{(K,x):K\in\mathcal K_n^n,\ 0\ne x\in\operatorname{int}(K-K)\},
\]
where convex bodies carry the Hausdorff metric and \(x\) the Euclidean metric. Consequently:

1. If \(K\) is not a simplex, then its strict-witness set
   \[
   W_K
   =
   \{x\in\operatorname{int}(K-K)\setminus\{0\}:
   \mathfrak D(K,x)>0\}
   \tag{2}
   \]
   is a nonempty open subset of \(\mathbb R^n\). In particular \(W_K\) has positive Lebesgue measure.

2. Every non-simplex \(K\) has a **rational robust witness**: there is
   \[
   q\in\mathbb Q^n\setminus\{0\},\qquad
   q\in\operatorname{int}(K-K),
   \]
   and constants \(\eta,\varepsilon>0\) such that
   \[
   \mathfrak D(L,q)\ge\eta
   \tag{3}
   \]
   for every full-dimensional convex body \(L\) with
   \[
   d_H(L,K)<\varepsilon.
   \]
   For the same neighborhood, \(q\in\operatorname{int}(L-L)\).

3. Hence the uncountable family of tests in condition (iii) of Langharst--Wang's Theorem 1.2 can be replaced by one fixed countable test bank:
   \[
   \boxed{
   K\text{ is a simplex}
   \iff
   \mathfrak D(K,q)\le0
   \quad
   \text{for every }
   q\in\mathbb Q^n\setminus\{0\}
   \cap\operatorname{int}(K-K).
   }
   \tag{4}
   \]
   More generally, \(\mathbb Q^n\) can be replaced by any fixed dense subset \(D\subset\mathbb R^n\).

Equivalently, for each \(q\in\mathbb Q^n\setminus\{0\}\) set
\[
\mathcal U_q
=
\{K\in\mathcal K_n^n:
q\in\operatorname{int}(K-K),\ \mathfrak D(K,q)>0\}.
\]
Then every \(\mathcal U_q\) is Hausdorff-open and
\[
\boxed{
\{K\in\mathcal K_n^n:K\text{ is not a simplex}\}
=
\bigcup_{q\in\mathbb Q^n\setminus\{0\}}\mathcal U_q.
}
\tag{5}
\]
Thus every non-simplex belongs to an open neighborhood certified by one fixed rational displacement.

A probabilistic corollary is immediate. If \(K\) is not a simplex and a probability law on \(\operatorname{int}(K-K)\) assigns positive mass to every nonempty open set, then one special test detects failure with positive probability; independent repeated samples detect failure almost surely. No uniform lower bound on the one-sample detection probability is claimed.

## Context

Langharst and Wang proved in September 2026 that the Bézout inequality
\[
V_n(K)\,V_n(K[n-2],A,B)
\le
V_n(K[n-1],A)V_n(K[n-1],B)
\tag{6}
\]
characterizes simplices among all full-dimensional convex bodies. Their Theorem 1.2 is stronger than the original formulation: it suffices that (6) hold for every nonzero
\[
x\in\operatorname{int}(K-K)
\]
with the special pair
\[
A=[0,x],
\qquad
B=K\cap(K-x).
\tag{7}
\]
Their proof uses the whole continuum of special shifts to derive a longest-chord identity and then the simplex characterization.

The theorem above shows that this continuum requirement has a robust countable certification form. If \(K\) is not a simplex, failure cannot be confined to an isolated or exceptional displacement: it occupies an open, hence positive-measure, set of shifts. Moreover one can choose a rational shift whose strict violation survives all sufficiently small Hausdorff perturbations of the body.

## Proof

### 1. A continuity lemma for convex intersections

We use the following elementary lemma.

**Lemma.** Suppose \(A_j\to A\) and \(B_j\to B\) in Hausdorff distance and
\[
\operatorname{int}A\cap\operatorname{int}B\ne\varnothing.
\]
Then
\[
A_j\cap B_j\longrightarrow A\cap B
\]
in Hausdorff distance.

**Proof.**
Choose \(z\) and \(r>0\) such that
\[
z+rB_2^n\subset A\cap B.
\tag{8}
\]
Write \(C=A\cap B\). Outer convergence is immediate: if \(y_j\in A_j\cap B_j\) and a subsequence converges to \(y\), then Hausdorff convergence gives \(y\in A\cap B\).

For the reverse inclusion, fix \(0<t<1\). For every \(y\in C\), put
\[
y_t=(1-t)y+t z.
\]
Convexity and (8) give
\[
y_t+t r B_2^n\subset A\cap B.
\tag{9}
\]
Let
\[
e_j=\max\{d_H(A_j,A),d_H(B_j,B)\}.
\]
Hausdorff convergence of convex bodies is equivalent to uniform convergence of support functions, so when \(e_j<tr\), (9) implies \(y_t\in A_j\cap B_j\). Indeed, for every \(u\in S^{n-1}\),
\[
\langle y_t,u\rangle+tr\le h_A(u),
\qquad
h_{A_j}(u)\ge h_A(u)-e_j,
\]
and therefore \(\langle y_t,u\rangle<h_{A_j}(u)\); the same argument applies to \(B_j\).

If
\[
R=\max_{y\in C}|y-z|,
\]
then
\[
|y-y_t|\le tR
\]
uniformly in \(y\in C\). First choose \(t\) small and then \(j\) large. This proves the inner Hausdorff approximation and hence the lemma. \(\square\)

### 2. Joint continuity of the special-test body

Take
\[
(K_j,x_j)\to(K,x)\in\mathcal E_n.
\]
Since
\[
K_j-x_j\to K-x
\]
in Hausdorff distance, it remains only to verify the interior-overlap hypothesis. For a full-dimensional convex body,
\[
x\in\operatorname{int}(K-K)
\iff
\operatorname{int}K\cap\operatorname{int}(K-x)\ne\varnothing.
\tag{10}
\]
Indeed, \(x=a-b\) with \(a,b\in\operatorname{int}K\) exactly when
\(b\in\operatorname{int}K\) and \(b+x=a\in\operatorname{int}K\).

Applying the lemma with
\[
A_j=K_j,\qquad B_j=K_j-x_j
\]
gives
\[
C_{K_j}(x_j)\to C_K(x).
\tag{11}
\]
The segment map \(x\mapsto[0,x]\) is Hausdorff-continuous, and volume and mixed volume are Hausdorff-continuous in all arguments. Equation (1) therefore proves the joint continuity of \(\mathfrak D\).

The incidence condition in \(\mathcal E_n\) is itself open. One way to see this is that
\[
K_j-K_j\to K-K
\]
in Hausdorff distance, while any point of \(\operatorname{int}(K-K)\) has a positive interior ball. The same support-function argument used above shows that such a point remains interior after sufficiently small Hausdorff perturbations.

### 3. Open strict witnesses

Langharst--Wang's Theorem 1.2 states that \(K\) is a simplex if and only if
\[
\mathfrak D(K,x)\le0
\]
for every nonzero \(x\in\operatorname{int}(K-K)\). Therefore, if \(K\) is not a simplex, there exists \(x_0\) in that domain with
\[
\mathfrak D(K,x_0)>0.
\tag{12}
\]
Continuity in \(x\) makes \(W_K\) open, and (12) makes it nonempty. Every nonempty open subset of \(\mathbb R^n\) has positive Lebesgue measure.

### 4. Rational and Hausdorff-stable witnesses

Because \(\mathbb Q^n\) is dense, the nonempty open set \(W_K\) contains a nonzero rational vector \(q\). Thus
\[
\mathfrak D(K,q)>0.
\]
Joint continuity of \(\mathfrak D\), together with openness of the incidence condition
\(q\in\operatorname{int}(L-L)\), gives \(\varepsilon>0\) such that for
\(d_H(L,K)<\varepsilon\),
\[
q\in\operatorname{int}(L-L),
\qquad
\mathfrak D(L,q)>
\frac12\mathfrak D(K,q).
\]
Taking
\[
\eta=\frac12\mathfrak D(K,q)>0
\]
proves (3).

If all rational admissible tests pass, \(K\) cannot be a non-simplex, since a non-simplex has the rational strict witness just constructed. Conversely, a simplex satisfies the Bézout inequality for all convex \(A,B\), hence certainly for all rational special tests. This proves (4). The same argument works for any fixed dense set \(D\).

Finally, joint continuity makes every \(\mathcal U_q\) open, and the rational-witness theorem gives the union identity (5).

## Sanity check: the unit square

Let
\[
K=[0,1]^2,\qquad x=(s,0),\qquad 0<s<1.
\]
Then
\[
C_K(x)=[0,1-s]\times[0,1].
\]
Using
\[
\operatorname{Area}(A+tB)
=
\operatorname{Area}(A)+2tV_2(A,B)+t^2\operatorname{Area}(B),
\]
one obtains
\[
V_2(K,[0,x])=\frac s2,\qquad
V_2([0,x],C_K(x))=\frac s2,\qquad
V_2(K,C_K(x))=\frac{2-s}{2}.
\]
Hence
\[
\boxed{
\mathfrak D(K,(s,0))=\frac{s^2}{4}>0.
}
\]
Thus every rational \(s\in(0,1)\) gives an explicit strict rational witness for this non-simplex.

## What is and is not resolved

The result is a robustness and certification refinement of the Langharst--Wang characterization, not a new proof of their simplex theorem. It supplies no dimension-only lower bound on the size of \(W_K\), on the violation margin, or on the probability of detecting a non-simplex by random sampling. Such uniform bounds cannot follow from continuity alone when bodies approach the simplex locus.

The interior condition is essential for the continuity lemma in this form: at boundary shifts, the intersection can lose dimension or disappear under arbitrarily small perturbations. No claim is made about a continuous extension of the defect through all of \(\partial(K-K)\).

## References

1. D. Langharst and S. Wang, *The Bézout inequality for mixed volumes characterizes simplices*, arXiv:2609.20380v1 (2026). https://arxiv.org/abs/2609.20380
2. I. Soprunov and A. Zvavitch, *Bezout Inequality for Mixed Volumes*, International Mathematics Research Notices 2016, no. 23, 7230--7252. https://doi.org/10.1093/imrn/rnv390
3. C. Saroglou, I. Soprunov and A. Zvavitch, *Wulff Shapes and a Characterization of Simplices via a Bezout Type Inequality*, Advances in Mathematics 357 (2019), 106820. https://arxiv.org/abs/1801.02675
