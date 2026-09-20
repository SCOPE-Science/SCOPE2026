# Exact one-dimensional minimal fillings for regular hexagons in constant curvature

## Statement

Let \(M=\{0,1,\dots,5\}\) be a cyclic six-point metric for which the distance between two labels depends only on their cyclic separation:
\[
d(i,j)=
\begin{cases}
a,&\min(|i-j|,6-|i-j|)=1,\\
b,&\min(|i-j|,6-|i-j|)=2,\\
c,&\min(|i-j|,6-|i-j|)=3.
\end{cases}
\]
Assume that there is a nondecreasing concave function \(f:[0,\pi]\to[0,\infty)\) with \(f(0)=0\) such that
\[
a=f(\pi/3),\qquad b=f(2\pi/3),\qquad c=f(\pi).
\]

Then the one-dimensional Gromov minimal-filling weight of \(M\) is
\[
\boxed{\operatorname{mf}(M)
=\min\left\{a+2b,\frac32(a+c)\right\}.}
\]

Both branches have explicit nonnegative weighted-tree fillings.

### Constant-curvature regular hexagons

For six equally spaced vertices on a metric circle of radius \(R\), the chord-distance profile is concave in the central angle in each of the following cases.

- Euclidean plane:
  \[
  f_0(\theta)=2R\sin(\theta/2).
  \]
- Unit sphere, for a convex minor-arc configuration \(0<R<\pi/2\):
  \[
  f_S(\theta)=2\arcsin\!\bigl(\sin R\,\sin(\theta/2)\bigr).
  \]
- Hyperbolic plane of curvature \(-1\):
  \[
  f_H(\theta)=2\operatorname{arsinh}\!\bigl(\sinh R\,\sin(\theta/2)\bigr).
  \]

Consequently the displayed minimum gives the exact one-dimensional minimal-filling weight for regular hexagons in all three geometries.

For a Euclidean regular hexagon of side length \(s\),
\[
(a,b,c)=(s,\sqrt3\,s,2s),
\]
so
\[
\boxed{\operatorname{mf}(H_6)=(1+2\sqrt3)s.}
\]
This makes sharp, for \(n=6\), the earlier regular-polygon upper estimate
\[
\operatorname{mf}(H_n)\le
2\sin\frac{\pi}{n}+(n-2)\sin\frac{2\pi}{n}
\]
under unit-circumradius normalization.

For the spherical and hyperbolic cases,
\[
\begin{aligned}
a_S&=2\arcsin\!\left(\tfrac12\sin R\right),&
b_S&=2\arcsin\!\left(\tfrac{\sqrt3}{2}\sin R\right),&
c_S&=2R,\\
a_H&=2\operatorname{arsinh}\!\left(\tfrac12\sinh R\right),&
b_H&=2\operatorname{arsinh}\!\left(\tfrac{\sqrt3}{2}\sinh R\right),&
c_H&=2R,
\end{aligned}
\]
and these are substituted directly into the same two-branch formula.

## Proof

### 1. Consequences of concavity

Concavity and monotonicity give
\[
a\le b\le c,\qquad c\le a+b,\qquad 3b\ge2c,\qquad 2b\ge a+c.
\]
Indeed, the second inequality is subadditivity of a nonnegative concave function with \(f(0)=0\), the third follows from
\(f(2\pi/3)\ge \frac23 f(\pi)\), and the fourth from midpoint concavity at \(2\pi/3\).

These inequalities will guarantee nonnegative edge weights and verify the filling constraints below.

### 2. A filling of weight \(a+2b\)

Take an internal path
\[
p-q-r-s.
\]
Attach leaves \(1,2\) to \(p\), leaf \(0\) to \(q\), leaf \(5\) to \(r\), and leaves \(3,4\) to \(s\). Put
\[
\begin{aligned}
w(p1)=w(s4)&=\frac{a+b-c}{2},\\
w(p2)=w(s3)&=\frac{a-b+c}{2},\\
w(pq)=w(rs)&=\frac{c-a}{2},\\
w(q0)=w(r5)&=\frac{3b-2c}{2},\\
w(qr)&=c-b.
\end{aligned}
\]
All weights are nonnegative by the inequalities above.

The induced leaf-to-leaf distances are:
\[
\begin{array}{c|c}
\text{pairs} & \text{tree distance}\\ \hline
12,34 & a\\
02,04,15,35 & b\\
03,14,25 & c\\
01,05,45 & 2b-c\\
13,24 & 2c-b\\
23 & 3c-2b.
\end{array}
\]
The first three rows meet the boundary distance exactly. For the remaining rows,
\[
2b-c\ge a,\qquad 2c-b\ge b,\qquad 3c-2b\ge a.
\]
The first is \(2b\ge a+c\); the other two follow from \(c\ge b\ge a\).
Thus this is a filling, and its total weight is
\[
a+2b.
\]

### 3. A filling of weight \(\frac32(a+c)\)

Partition the boundary into three adjacent pairs, for instance
\[
\{0,5\},\qquad \{1,2\},\qquad \{3,4\}.
\]
Make each pair a cherry, and connect the three cherry vertices to one central vertex. Give each of the six leaf edges weight \(a/2\), and each of the three central spokes weight \((c-a)/2\).

Within a cherry the tree distance is \(a\); between distinct cherries it is \(c\), which dominates every boundary distance. Hence this is a filling of total weight
\[
6\frac a2+3\frac{c-a}{2}=\frac32(a+c).
\]

Therefore
\[
\operatorname{mf}(M)\le
\min\left\{a+2b,\frac32(a+c)\right\}.
\]

### 4. Universal tour lower bound

A standard theorem for one-dimensional minimal fillings permits a minimal filling of a finite metric space to be taken with binary-tree type. For a fixed tree, every cyclic tour around the tree gives the half-perimeter lower bound
\[
w(G)\ge\frac12\sum_{i=0}^{5} d(\pi_i,\pi_{i+1}),
\qquad \pi_6=\pi_0.
\]

For a cyclic order \(\pi\), let \((n_1,n_2,n_3)\) count how many of its six consecutive pairs have cyclic hexagon separation \(1,2,3\). A finite six-leaf tree lemma gives:

> Every labeled unrooted binary tree on \(\{0,\dots,5\}\) admits a compatible tour whose gap count belongs to
> \[
> \mathcal S=
> \{(2,4,0),(0,4,2),(1,4,1),(2,2,2),(3,0,3),(1,2,3)\}.
> \]

For these six possibilities, the tour half-perimeters are respectively
\[
\begin{array}{c|c}
(n_1,n_2,n_3)&\text{half-perimeter}\\ \hline
(2,4,0)&a+2b,\\
(0,4,2)&2b+c,\\
(1,4,1)&(a+4b+c)/2,\\
(2,2,2)&a+b+c,\\
(3,0,3)&3(a+c)/2,\\
(1,2,3)&(a+2b+3c)/2.
\end{array}
\]
Using \(a\le b\le c\), the first four are at least \(a+2b\), while the last two are at least \(3(a+c)/2\) in the precise sense needed here:
\[
\begin{aligned}
2b+c-(a+2b)&=c-a\ge0,\\
\frac{a+4b+c}{2}-(a+2b)&=\frac{c-a}{2}\ge0,\\
(a+b+c)-(a+2b)&=c-b\ge0,\\
\frac{a+2b+3c}{2}-\frac32(a+c)&=b-a\ge0.
\end{aligned}
\]
Thus every binary-tree filling has weight at least
\[
\min\left\{a+2b,\frac32(a+c)\right\}.
\]
Combined with the two constructions, this proves the theorem.

### 5. Verification of the six-leaf tree lemma

The finite lemma is independently reproducible from the included script `artifacts/verify_hexagon.py`. It generates all
\[
(2\cdot6-5)!!=105
\]
labeled unrooted binary trees by successive edge subdivision. For each tree it enumerates the \(60\) cyclic leaf orders up to rotation and reversal.

A cyclic order is a tree tour exactly when every split induced by an edge has one side occurring as a circular interval. The script checks this criterion, computes \((n_1,n_2,n_3)\), and verifies that every one of the \(105\) trees has a tour in \(\mathcal S\). As an additional compression check, the \(105\) labeled trees form \(17\) orbits under the dihedral group of the hexagon, and the script prints a witnessing tour for every orbit.

### 6. Concavity of the constant-curvature chord profiles

For the spherical formula, with \(k=\sin R\in(0,1)\),
\[
f_S''(\theta)=
-\frac{k(1-k^2)\sin(\theta/2)}
{2\left(1-k^2\sin^2(\theta/2)\right)^{3/2}}
\le0.
\]
For the hyperbolic formula, with \(k=\sinh R>0\),
\[
f_H''(\theta)=
-\frac{k(1+k^2)\sin(\theta/2)}
{2\left(1+k^2\sin^2(\theta/2)\right)^{3/2}}
<0.
\]
The Euclidean profile has
\[
f_0''(\theta)=-\frac R2\sin(\theta/2)\le0.
\]
All three profiles are increasing on \([0,\pi]\), completing the constant-curvature specialization.

## Context and prior work

Ivanov and Tuzhilin developed the one-dimensional Gromov minimal-filling theory and proved the binary-tree reduction and tour lower bounds used above. In their treatment of convex polygons they obtained an exact formula for five vertices, but for regular \(n\)-gons stated only the upper estimate quoted above (Assertion 11.5, attributed to E. E. Zaval'nyuk).

Edelsbrunner, Ivanov and Karasev subsequently listed as an open problem the description of minimal fillings for vertex sets of regular polygons in the Euclidean plane, on the standard sphere, and in the Lobachevskii plane. The present result addresses the exact-weight subproblem for \(n=6\), rather than claiming a classification of all minimizing trees for every \(n\).

Eremin later gave a general minimax formula for the minimal-filling weight of an arbitrary finite metric space. The theorem here is a closed-form evaluation for this symmetric six-point family, obtained by combining two explicit optimal fillings with a complete six-leaf tour reduction.

A 2026 preprint by Ivanov and Tuzhilin develops a convex-polyhedral description for parametric generalized fillings. Its abstract was checked during the literature comparison; the full text was not inspected, so it remains the most important residual source that could contain an equivalent special-case computation.

## Limitations

- The six-point theorem assumes a nondecreasing concave cyclic chord profile. It does not claim the same two-branch formula for arbitrary triples \(a\le b\le c\).
- The spherical corollary is stated for convex minor-arc regular hexagons with \(0<R<\pi/2\).
- The result determines the minimum weight and gives explicit optimal fillings, but does not classify every minimizing tree and weight assignment.
- The finite lower-bound lemma is computer-verified by exhaustive enumeration; the verifier is included and uses only the Python standard library.
- Originality is to the best of our knowledge. In particular, the 2026 convex-polyhedra preprint was not available in full text in the sources inspected for this comparison.

## Reproducibility

Run
```text
python3 artifacts/verify_hexagon.py
```
with Python 3. The expected headline output is
```text
labeled_binary_trees=105
dihedral_orbits=17
all_trees_have_target_tour=true
```
followed by one witnessing tour for each dihedral orbit.

## References

1. H. Edelsbrunner, A. Ivanov, R. Karasev, *Current Open Problems in Discrete and Computational Geometry*, Modeling and Analysis of Information Systems **19** (2012), no. 5, 5–17. https://doi.org/10.18255/1818-1015-2012-5-5-17
2. A. O. Ivanov, A. A. Tuzhilin, *One-dimensional Gromov minimal filling problem*, Sbornik: Mathematics **203** (2012), no. 5, 677–726. https://doi.org/10.1070/SM2012v203n05ABEH004239 ; https://arxiv.org/abs/1101.0106
3. A. Yu. Eremin, *A formula for the weight of a minimal filling of a finite metric space*, Sbornik: Mathematics **204** (2013), no. 9, 1285–1306. https://doi.org/10.1070/SM2013v204n09ABEH004340
4. A. O. Ivanov, A. A. Tuzhilin, *Minimal fillings of finite metric spaces: The state of the art*, Contemporary Mathematics **625** (2014/2016), 9–35.
5. A. O. Ivanov, A. A. Tuzhilin, *Minimal Fillings of Finite Metric Spaces and Convex Polyhedra*, arXiv:2607.27211 (2026). https://arxiv.org/abs/2607.27211
