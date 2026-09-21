# Near-extremal identifying open codes from twice-subdivided skeletons

## Statement

An **identifying open code** (IO-code) in a finite simple graph \(G\) is a set \(D\subseteq V(G)\) such that every open-neighborhood trace \(N_G(v)\cap D\) is nonempty and the traces are pairwise distinct. Its minimum size is denoted \(\gamma^{\mathrm{IOC}}(G)\).

Fix an integer \(\Delta\ge 3\). Let \(H\) be any connected simple graph with
\[
p=|V(H)|\ge2,\qquad m=|E(H)|,\qquad \Delta(H)\le\Delta.
\]
Construct \(L_\Delta(H)\) as follows.

1. Replace each edge \(uv\in E(H)\) by a length-three path
   \[
   u-x_{u,uv}-x_{v,uv}-v,
   \]
   so every original edge is subdivided exactly twice.
2. For every original vertex \(v\), attach \(\Delta-d_H(v)\) vertex-disjoint pendant paths \(v-s_{v,j}-\ell_{v,j}\) of length two.

Then \(L_\Delta(H)\) is connected, open-twin-free, has maximum degree exactly \(\Delta\), contains no \(4\)-cycle, and satisfies
\[
\boxed{
|V(L_\Delta(H))|=(2\Delta+1)p-2m
}
\]
and
\[
\boxed{
\gamma^{\mathrm{IOC}}(L_\Delta(H))
=|V(L_\Delta(H))|-p
=2\Delta p-2m.
}
\]

Thus an exact IO-code number is obtained for an arbitrary bounded-degree skeleton, not only for one special family.

## Proof

Write \(G=L_\Delta(H)\), and call the vertices inherited from \(H\) **centers**. Every center has degree exactly \(\Delta\); each subdivision vertex and each support \(s_{v,j}\) has degree two; each \(\ell_{v,j}\) is a leaf.

The order formula follows from
\[
|V(G)|
=p+2m+2\sum_{v\in V(H)}(\Delta-d_H(v))
=p+2m+2(\Delta p-2m)
=(2\Delta+1)p-2m.
\]

Every cycle of \(G\) lies in the twice-subdivided copy of \(H\), and projects to a cycle of \(H\). Hence every cycle of \(G\) has length divisible by three and at least nine, so \(G\) has no \(4\)-cycle. Open-twin-freeness is also immediate from the construction: leaves have distinct singleton neighborhoods, support vertices have distinct center-leaf neighborhoods, subdivision vertices have distinct center-subdivision neighborhoods, and centers have degree at least three while all other vertices have degree at most two.

Let \(D\) be any IO-code and put \(X=V(G)\setminus D\). Since every leaf \(\ell_{v,j}\) has the unique neighbor \(s_{v,j}\), total domination forces every support \(s_{v,j}\) into \(D\).

For each center \(v\), define
\[
B_v=\{v\}
\cup\{\ell_{v,j}:1\le j\le \Delta-d_H(v)\}
\cup\{x_{w,vw}:vw\in E(H)\}.
\]
The last set consists of the subdivision vertices at the *opposite* ends of the edges incident with \(v\). The sets \(B_v\) are pairwise disjoint, each has size \(\Delta+1\), and together they contain every vertex not already forced into \(D\).

We claim that \(|X\cap B_v|\le1\) for every \(v\). Indeed:

- \(v\) and a leaf \(\ell_{v,j}\) cannot both be omitted because \(N(s_{v,j})=\{v,\ell_{v,j}\}\) must meet \(D\).
- Two leaves \(\ell_{v,j},\ell_{v,k}\) cannot both be omitted because
  \[
  N(s_{v,j})\triangle N(s_{v,k})=\{\ell_{v,j},\ell_{v,k}\};
  \]
  otherwise the two supports have equal traces on \(D\).
- If \(e=vw\), then \(v\) and the opposite subdivision vertex \(x_{w,e}\) cannot both be omitted because
  \[
  N(x_{v,e})=\{v,x_{w,e}\}
  \]
  must meet \(D\).
- A leaf \(\ell_{v,j}\) and an opposite subdivision vertex \(x_{w,e}\) cannot both be omitted because
  \[
  N(s_{v,j})\triangle N(x_{v,e})
  =\{\ell_{v,j},x_{w,e}\}.
  \]
- Two distinct opposite subdivision vertices \(x_{w,e}\) and \(x_{z,f}\) cannot both be omitted because
  \[
  N(x_{v,e})\triangle N(x_{v,f})
  =\{x_{w,e},x_{z,f}\}.
  \]

Thus at most one vertex is omitted from each \(B_v\), so \(|X|\le p\) and therefore
\[
|D|\ge |V(G)|-p.
\]

For the reverse inequality, take
\[
D_0=V(G)\setminus V(H),
\]
that is, omit exactly the \(p\) centers. In \(G[D_0]\), every support is paired with its leaf and the two subdivision vertices replacing each edge of \(H\) are paired with one another. Hence every noncenter has a nonempty singleton trace on \(D_0\), and these singleton traces are all distinct. Every center has as its trace all its \(\Delta\) neighbors, so center traces have size \(\Delta\ge3\) and are pairwise distinct. Therefore \(D_0\) is an IO-code of size \(|V(G)|-p\), proving the formula.

## Consequences for the bounded-degree extremal problem

Take \(H=C_p\), where \(p\ge3\). Then
\[
|V(L_\Delta(C_p))|=(2\Delta-1)p,
\qquad
\gamma^{\mathrm{IOC}}(L_\Delta(C_p))=(2\Delta-2)p,
\]
so
\[
\boxed{
\frac{\gamma^{\mathrm{IOC}}(L_\Delta(C_p))}{|V(L_\Delta(C_p))|}
=\frac{2\Delta-2}{2\Delta-1}.
}
\]
This gives arbitrarily large connected, open-twin-free, \(C_4\)-free examples of maximum degree \(\Delta\) with that exact density.

Taking \(H=P_p\) instead yields trees with
\[
|V(L_\Delta(P_p))|=(2\Delta-1)p+2,
\qquad
\gamma^{\mathrm{IOC}}(L_\Delta(P_p))=(2\Delta-2)p+2,
\]
and hence densities strictly larger than \((2\Delta-2)/(2\Delta-1)\) for every finite \(p\), converging to that value as \(p\to\infty\).

Chakraborty, Foucaud and Henning proved in 2026 that every connected open-twin-free \(C_4\)-free graph of order \(n\ge5\), maximum degree at most \(\Delta\), and not equal to the subdivided star \(T_\Delta\), satisfies
\[
\gamma^{\mathrm{IOC}}(G)\le \frac{2\Delta-1}{2\Delta}n.
\]
For \(\Delta\ge4\), they gave an infinite construction of density \((2\Delta-4)/(2\Delta-3)\), described a more complicated slight improvement, and explicitly suggested constructing examples with density \((2\Delta-3)/(2\Delta-2)\) as an open direction.

The cycle-skeleton family above strictly exceeds that suggested target:
\[
\frac{2\Delta-2}{2\Delta-1}
-
\frac{2\Delta-3}{2\Delta-2}
=
\frac{1}{(2\Delta-2)(2\Delta-1)}>0.
\]
It also strictly exceeds the paper's stated refined construction density
\[
\frac{2\Delta-4}{2\Delta-3}
+
\frac{2}{3(\Delta-1)^2(2\Delta-3)}
\]
by
\[
\frac{2(\Delta-2)(3\Delta-2)}
{3(\Delta-1)^2(2\Delta-3)(2\Delta-1)}>0.
\]
Consequently, if \(a_\Delta\) denotes the asymptotic limsup of \(\gamma^{\mathrm{IOC}}(G)/|V(G)|\) over connected open-twin-free \(C_4\)-free graphs with maximum degree at most \(\Delta\), then for every \(\Delta\ge4\),
\[
\boxed{
\frac{2\Delta-2}{2\Delta-1}
\le a_\Delta
\le
\frac{2\Delta-1}{2\Delta}.
}
\]
The remaining gap between these two constants is only
\[
\frac{1}{2\Delta(2\Delta-1)}.
\]

## Reproducible finite check

The artifact `artifacts/verify_small.py` independently formulates the minimum IO-code problem as a binary covering/separation formulation. It checks every connected Graph Atlas skeleton on two through five vertices for \(\Delta\in\{3,4,5\}\) whenever \(\Delta(H)\le\Delta\). Across 79 instances it verifies the order formula, maximum degree, open-twin-freeness, absence of a 4-cycle, the explicit code, and the exact optimum. The output is recorded in `artifacts/expected_output.txt`. This computation is corroborative; the theorem is proved above without computation.

## Relation to prior literature and limitations

The terminology is equivalent to the older **open neighborhood locating-dominating** (OLD) terminology. Seo and Slater established foundational tree bounds, and Chellali--Jafari Rad--Seo--Slater developed general OLD bounds and extremal characterizations. The latter, for example, gives \(OLD(G)\le n-\rho(G)\) for connected \(C_4\)-free graphs of minimum degree at least three, which does not cover the leaf-rich graphs constructed here.

The closest prior result is the 2026 bounded-maximum-degree paper above. Its published concluding section still states the \(\Delta\ge4\) construction gap and proposes a lower density than the one achieved here. Searches under identifying-open-code, OLD/open-neighborhood-locating-dominating, subdivision, double subdivision, maximum-degree, and equivalent terminology did not locate the skeleton-lift formula or the density \((2\Delta-2)/(2\Delta-1)\). Originality is therefore claimed only **to the best of our knowledge**.

Residual uncertainty remains because two older tree-focused sources were not inspected in complete theorem-by-theorem detail: Seo--Slater, *Open neighborhood locating-dominating in trees* (2011, DOI 10.1016/j.dam.2010.12.010), and Seo--Slater, *Open Locating-Dominating Interpolation for Trees* (Congressus Numerantium 215, 2014). Their available descriptions concern general tree bounds, extremal trees, and interpolation rather than bounded-maximum-degree asymptotic constructions; moreover, the 2026 paper cites this older literature while still leaving the relevant construction direction open. A differently indexed tree construction equivalent to the one above nevertheless remains the principal originality risk.

The result does **not** determine the exact asymptotic extremal constant \(a_\Delta\), prove the 2026 upper bound asymptotically sharp for \(\Delta\ge4\), or characterize all extremal graphs. For \(\Delta=3\), the known \(5n/6\) construction is stronger than the present \(4n/5\) limiting density; the improvement here is specifically relevant for \(\Delta\ge4\).

## References

1. D. Chakraborty, F. Foucaud, M. A. Henning, *Identifying open codes in trees and 4-cycle-free graphs of given maximum degree*, Discrete Applied Mathematics 386 (2026), 319--333. DOI: 10.1016/j.dam.2026.02.032. Preprint: arXiv:2407.09692.
2. M. Chellali, N. Jafari Rad, S. J. Seo, P. J. Slater, *On open neighborhood locating-dominating in graphs*, Electronic Journal of Graph Theory and Applications 2 (2014), 87--98. DOI: 10.5614/ejgta.2014.2.2.1.
3. S. J. Seo, P. J. Slater, *Open neighborhood locating-dominating in trees*, Discrete Applied Mathematics 159 (2011), 484--489. DOI: 10.1016/j.dam.2010.12.010.
4. M. A. Henning, A. Yeo, *Distinguishing-transversal in hypergraphs and identifying open codes in cubic graphs*, Graphs and Combinatorics 30 (2014), 1139--1149. DOI: 10.1007/s00373-013-1311-2.
