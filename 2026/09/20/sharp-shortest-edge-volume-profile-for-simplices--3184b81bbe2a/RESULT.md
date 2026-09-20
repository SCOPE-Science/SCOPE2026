# Sharp shortest-edge volume profile for diameter-bounded simplices

**Same-model review: passed. Independent audit: not yet performed.**

## Result

Let
\[
T=\operatorname{conv}(p_0,\ldots,p_n)\subset\mathbb R^n,\qquad n\ge 2,
\]
be a nondegenerate Euclidean simplex of diameter at most \(D\). Suppose a distinguished edge has length
\[
|p_0p_1|=s,\qquad 0<s\le D.
\]
Then
\[
\boxed{
\operatorname{Vol}_n(T)\le
\frac{sD^{n-2}}{n!\,2^{n/2}}
\sqrt{2nD^2-(n-1)s^2}
}. \tag{1}
\]
Equality holds if and only if every edge other than \(p_0p_1\) has length \(D\). Such an equality simplex exists for every \(0<s\le D\) and is unique up to Euclidean isometry and relabeling of the remaining vertices.

Consequently, if \(D=\operatorname{diam}T\), \(\ell_{\min}(T)\) is the shortest edge, and
\[
\mu=\frac{\ell_{\min}(T)}D,
\]
then, with
\[
V_*(D)=\frac{\sqrt{n+1}}{n!\,2^{n/2}}D^n
\]
the volume of the regular \(n\)-simplex of diameter \(D\),
\[
\boxed{
\frac{\operatorname{Vol}_n(T)}{V_*(D)}
\le
F_n(\mu):=
\mu\sqrt{\frac{2n-(n-1)\mu^2}{n+1}}
}. \tag{2}
\]
The profile is sharp for every \(\mu\in(0,1]\). For \(0<\mu<1\), equality means that exactly one edge has length \(\mu D\) and all other edges have length \(D\); for \(\mu=1\), equality is the regular simplex.

Since \(F_n\) is strictly increasing on \((0,1]\), (2) has the sharp inverse form
\[
\boxed{
\frac{|e|}D\ge
\sqrt{
\frac{n-\sqrt{n^2-(n^2-1)r^2}}{n-1}
}
\quad\text{for every edge }e,
} \tag{3}
\]
where
\[
r=\frac{\operatorname{Vol}_n(T)}{V_*(D)}.
\]
Thus volume close to the largest-small-simplex value forces every edge to be quantitatively close to the diameter, with the best possible global profile. Near regularity,
\[
F_n(1-\delta)=1-\frac2{n+1}\delta+O(\delta^2),
\]
so the inverse stability is linear to first order, and that rate is sharp.

## Proof

Put the distinguished edge symmetrically on the first coordinate axis:
\[
p_0=(-s/2,0),\qquad p_1=(s/2,0)
\]
in \(\mathbb R\times\mathbb R^m\), where \(m=n-1\). Write the remaining vertices as
\[
p_{i+1}=(t_i,y_i),\qquad i=1,\ldots,m,
\]
with \(y_i\in\mathbb R^m\), and let \(Y\) be the \(m\times m\) matrix whose columns are the \(y_i\).

Expanding the simplex determinant along the distinguished-edge direction gives
\[
n!\operatorname{Vol}_n(T)=s|\det Y|. \tag{4}
\]

Because each \(p_{i+1}\) is within distance \(D\) of both \(p_0\) and \(p_1\),
\[
(t_i+s/2)^2+\|y_i\|^2\le D^2,\qquad
(t_i-s/2)^2+\|y_i\|^2\le D^2.
\]
Adding these inequalities yields
\[
t_i^2+\|y_i\|^2\le D^2-\frac{s^2}4,
\]
and therefore
\[
\|y_i\|^2\le R^2:=D^2-\frac{s^2}4. \tag{5}
\]
For \(i\ne j\), orthogonal projection cannot increase distance, so
\[
\|y_i-y_j\|\le |p_{i+1}p_{j+1}|\le D. \tag{6}
\]

Set
\[
\alpha=\frac{D^2}2,\qquad
\beta=R^2-\alpha=\frac{D^2}2-\frac{s^2}4>0,
\]
and consider the positive-semidefinite operator
\[
S=
\alpha\sum_{i=1}^m y_i y_i^\top+
\beta\sum_{1\le i<j\le m}(y_i-y_j)(y_i-y_j)^\top .
\]
Using (5) and (6),
\[
\begin{aligned}
\operatorname{tr}S
&\le \alpha mR^2+\beta\binom m2D^2\\
&=m\alpha(\alpha+m\beta).
\end{aligned} \tag{7}
\]
On the other hand,
\[
S=YQY^\top,\qquad
Q=\alpha I+\beta(mI-J),
\]
where \(J\) is the all-ones matrix. The complete-graph Laplacian \(mI-J\) has eigenvalue \(0\) on the all-ones direction and eigenvalue \(m\) on its orthogonal complement, hence
\[
\det Q=\alpha(\alpha+m\beta)^{m-1}. \tag{8}
\]
Applying arithmetic-geometric mean to the eigenvalues of \(S\), and then (7),
\[
\det S\le
\left(\frac{\operatorname{tr}S}m\right)^m
\le
[\alpha(\alpha+m\beta)]^m. \tag{9}
\]
Since \(\det S=(\det Y)^2\det Q\), (8)-(9) imply
\[
(\det Y)^2
\le
\alpha^{m-1}(\alpha+m\beta)
=
\left(\frac{D^2}2\right)^{n-2}
\frac{2nD^2-(n-1)s^2}4. \tag{10}
\]
Combining (4) and (10) proves (1).

### Equality

All coefficients in the trace estimate are positive. Equality in (7) therefore forces
\[
\|y_i\|^2=R^2
\quad\text{and}\quad
\|y_i-y_j\|^2=D^2
\]
for all \(i\ne j\). Equality in (5) then forces \(t_i=0\), and the two endpoint inequalities both become equalities. Thus every edge other than the distinguished edge has length \(D\).

Conversely, assume all those edges have length \(D\). Then \(t_i=0\), and the Gram matrix of the \(y_i\) is
\[
G_0=Y^\top Y=\alpha I+\beta J. \tag{11}
\]
Its eigenvalues are \(\alpha>0\) with multiplicity \(m-1\) and \(\alpha+m\beta>0\) once, so this configuration exists and is nondegenerate. Moreover
\[
Q=(\alpha+m\beta)I-\beta J
\]
and \(QG_0=\alpha(\alpha+m\beta)I\), which makes \(S\) scalar; hence equality also holds in (9). Equation (11) determines the configuration up to an orthogonal transformation, proving uniqueness up to Euclidean isometry.

### Shortest-edge profile and inverse

Apply (1) to a shortest edge \(s=\mu D\) and divide by \(V_*(D)\) to obtain (2). Direct differentiation gives
\[
F_n'(\mu)>0\qquad(0<\mu<1),
\]
so the profile is invertible. Squaring \(r\le F_n(\mu)\) gives
\[
(n-1)\mu^4-2n\mu^2+(n+1)r^2\le0.
\]
Selecting the root in \([0,1]\) gives (3). The equality family from (1) shows sharpness for every admissible value of \(r\).

## Context and originality check

The classical "largest small polytope" problem asks for maximum volume under a diameter bound. Graham's 1975 work on the planar largest-small problem explicitly motivated the higher-dimensional version; the \(d+1\)-vertex case is the regular simplex, and Kind--Kleinschmidt treated the \(d+2\)-vertex case. Fejes Toth's survey records this history.

Recent frame-based work gives aggregate inequalities relating simplex volume to sums of squared edge lengths, while recent work on Cech-complex extremizers studies special simplices with short and long edges and computes circumradii. The located statements do not give the sharp volume envelope at a prescribed distinguished or shortest edge, the unique one-short-edge equality family, or the inverse law (3).

Searches were made under the formulations "largest small simplex", "maximum volume simplex with prescribed edge", "shortest edge simplex volume", "edge ratio simplex volume", and related diameter/mesh-quality terminology. No equivalent theorem or stronger statement implying (1)-(3) was located. Originality is therefore claimed only **to the best of our knowledge**. Because the proof is elementary linear algebra and distance geometry, an equivalent older formulation or folklore result remains a plausible residual risk.

## Checks and limiting cases

- For \(n=2\), (1) becomes the familiar maximal area of a triangle with base \(s\) and both other sides bounded by \(D\):
  \[
  A\le \frac{s}{4}\sqrt{4D^2-s^2}.
  \]
- For \(s=D\), (1) becomes exactly the regular-simplex volume \(V_*(D)\).
- As \(s\downarrow0\), the sharp volume tends to zero linearly in \(s\), as expected from collapse along the distinguished edge.

## Scientific limitations

The result is Euclidean and simplex-specific. It controls edge-length regularity, not Hausdorff distance, Banach-Mazur distance, altitude ratios, or circumradius/inradius directly. It treats one prescribed edge (and, through minimization, the shortest edge), not simultaneous prescriptions on several short edges. Originality is to the best of our knowledge and retains a residual folklore/distance-geometry risk.

## References

1. R. L. Graham, *The Largest Small Hexagon*, Journal of Combinatorial Theory, Series A 18 (1975), 165-170. https://doi.org/10.1016/0097-3165(75)90004-7
2. B. Kind and P. Kleinschmidt, *On the Maximal Volume of Convex Bodies with Few Vertices*, Journal of Combinatorial Theory, Series A 21 (1976), 124-128. https://doi.org/10.1016/0097-3165(76)90056-X
3. G. Fejes Toth, *Finite variations on the isoperimetric problem*, arXiv:2202.09920; later in *Lagerungen* (2023). https://arxiv.org/abs/2202.09920
4. J. Ledford, K. Rivera-Ayala, E. Schroeder, *A note concerning frames and geometric inequalities*, arXiv:2509.05611 (2025). https://arxiv.org/abs/2509.05611
5. H. Edelsbrunner and J. Pach, *Maximum Betti Numbers of Cech Complexes*, Discrete & Computational Geometry (published 2025). https://doi.org/10.1007/s00454-025-00796-5
