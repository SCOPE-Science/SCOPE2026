# Maximum spectral radius in strongly connected digraphs with \(m+2\) arcs

## Result

Let \(\mathcal{SC}_{m+2}(m)\) be the class of finite strongly connected simple digraphs with \(m\) vertices and \(m+2\) arcs, where loops are allowed and parallel arcs are not.

For \(m\ge 3\), let \(r_m\in(0,1)\) be the unique solution of
\[
r+r^2+r^{m-1}=1.
\]
Then every \(G\in\mathcal{SC}_{m+2}(m)\) satisfies
\[
\boxed{\rho(G)\le r_m^{-1}}.
\]
Equality holds if and only if \(G\) is, up to isomorphism, the directed three-petal rose whose directed cycles have lengths
\[
\boxed{1,\;2,\;m-1}
\]
and share exactly one common vertex while otherwise being vertex-disjoint. Equivalently, the extremal topological polynomial is
\[
1-z-z^2-z^{m-1}.
\]

For the loopless subclass and \(m\ge4\), let \(s_m\in(0,1)\) be the unique solution of
\[
2s^2+s^{m-2}=1.
\]
Then
\[
\boxed{\rho(G)\le s_m^{-1}}
\]
for every loopless \(G\in\mathcal{SC}_{m+2}(m)\), with equality if and only if \(G\) is the directed three-petal rose with cycle lengths
\[
\boxed{2,\;2,\;m-2}.
\]
Equivalently, its extremal topological polynomial is
\[
1-2z^2-z^{m-2}.
\]

These statements prove both parts of Conjecture 5.15 of Klech (2026). The exceptional loopless case \(m=3\) is already identified in that paper: there is one isomorphism class and its spectral radius is \((1+\sqrt5)/2\).

## Proof

Write \(d^+(v)\) for the outdegree of \(v\). Strong connectivity gives \(d^+(v)\ge1\) for every vertex, and
\[
\sum_{v\in V(G)}(d^+(v)-1)=|E(G)|-|V(G)|=2.
\]
Consequently exactly one of the following two degree patterns occurs.

1. One vertex has outdegree \(3\), and every other vertex has outdegree \(1\).
2. Two vertices have outdegree \(2\), and every other vertex has outdegree \(1\).

We treat these cases by first-return excursions.

### 1. One branching vertex

Let \(v\) be the unique vertex of outdegree \(3\). Starting along each of its three outgoing arcs and then following the unique outgoing arc at every nonbranching vertex produces a first-return directed path to \(v\). It must return to \(v\): otherwise a repeated nonbranching vertex would create a closed directed cycle from which \(v\) is unreachable, contradicting strong connectivity.

Let the three return lengths be \(\ell_1,\ell_2,\ell_3\). Every vertex other than \(v\) occurs on at least one excursion, hence
\[
\sum_{i=1}^3(\ell_i-1)\ge m-1,
\qquad\text{so}\qquad
\ell_1+\ell_2+\ell_3\ge m+2. \tag{1}
\]
Because parallel arcs are forbidden, at most one \(\ell_i\) can equal \(1\). In the loopless case all three lengths are at least \(2\).

Let \(x\) be the positive Perron vector and put \(z=\rho(G)^{-1}\). Along a deterministic excursion of length \(\ell\), the first successor of \(v\) has Perron coordinate \(z^{\ell-1}x_v\). The eigenvalue equation at \(v\) therefore gives
\[
z^{\ell_1}+z^{\ell_2}+z^{\ell_3}=1. \tag{2}
\]

For fixed \(0<z<1\), moving one unit of exponent from a smaller exponent to a larger one increases the corresponding sum of powers:
\[
z^{a-1}+z^{b+1}-z^a-z^b
=(1-z)(z^{a-1}-z^b)>0
\qquad(1<a\le b).
\]
Thus, subject to (1), the sum in (2) is maximized by making the exponents as unequal as the lower bounds permit.

If loops are allowed, the maximum is
\[
z+z^2+z^{m-1}.
\]
Indeed, with one exponent equal to \(1\), the other two are extremized at \(2,m-1\); if there is no exponent \(1\), the maximum is at most
\[
2z^2+z^{m-2}\le z+z^2+z^{m-1}.
\]
Hence at \(z=r_m\) the left side of (2) is at most \(1\), and therefore \(\rho(G)\le r_m^{-1}\). Equality forces
\[
\{\ell_1,\ell_2,\ell_3\}=\{1,2,m-1\}
\]
and equality in the vertex count in (1), so the excursions are internally disjoint and cover all vertices. This is exactly the stated directed rose.

If \(G\) is loopless, the same transfer argument gives
\[
z^{\ell_1}+z^{\ell_2}+z^{\ell_3}
\le 2z^2+z^{m-2}.
\]
Thus \(\rho(G)\le s_m^{-1}\), with equality exactly for the rose with cycle lengths \(2,2,m-2\).

It remains to show that the second degree pattern is always strictly below these bounds.

### 2. Two branching vertices

Let the two outdegree-\(2\) vertices be \(p,q\). Starting from each of their four outgoing arcs and stopping at the first return to \(\{p,q\}\) gives four first-return excursions. Every nonbranching vertex lies on at least one of them, so if their lengths are \(a,b,c,d\), then
\[
a+b+c+d\ge m+2. \tag{3}
\]

For \(0<z<1\), form the \(2\times2\) first-return matrix \(M(z)\): its \((u,w)\)-entry is the sum of \(z^\ell\) over excursions beginning at \(u\in\{p,q\}\) and first returning to \(w\in\{p,q\}\). Strong connectivity makes this reduced two-vertex digraph irreducible. Restricting the Perron eigenvector equation to \(p,q\) gives
\[
M(\rho(G)^{-1})
\binom{x_p}{x_q}
=
\binom{x_p}{x_q},
\]
hence
\[
\rho\!\left(M(\rho(G)^{-1})\right)=1. \tag{4}
\]
Moreover \(\rho(M(z))\) is strictly increasing in \(z\in(0,1)\).

Up to interchanging \(p,q\), there are only three endpoint patterns.

#### Pattern I: one self-return and one cross-return from each branch vertex

Here
\[
M(z)=
\begin{pmatrix}
z^a&z^b\\
z^c&z^d
\end{pmatrix}.
\]
For the general class, all lengths are at least \(1\). It is enough to prove
\[
(1-r_m^a)(1-r_m^d)>r_m^{b+c}, \tag{5}
\]
because then \(\rho(M(r_m))<1\).

Increasing any length only improves (5), so by (3) we may take \(a+b+c+d=m+2\). Put \(t=a+d\) and \(k=t-1\), so \(1\le k\le m-1\). Since
\[
x\longmapsto \log(1-r_m^x)
\]
is concave, for fixed \(t\) the product on the left of (5) is minimized when \(\{a,d\}=\{1,k\}\). Thus it suffices to show
\[
(1-r_m)(1-r_m^k)>r_m^{m+1-k}. \tag{6}
\]
After multiplying by \(r_m^k\), the only variable factor is
\[
r_m^k(1-r_m^k).
\]
Writing \(u=r_m^k\), the function \(u(1-u)\) is concave, so its minimum over
\(r_m^{m-1}\le u\le r_m\) occurs at an endpoint. For \(k=1\), (6) follows from
\[
(1-r_m)^2>r_m^m:
\]
for \(m\ge4\), \(1-r_m=r_m^2+r_m^{m-1}>r_m^2\), while \(m=3\) gives \(r_m=1/2\) directly. For \(k=m-1\),
\[
(1-r_m)(1-r_m^{m-1})-r_m^2=r_m^m>0.
\]
Therefore (5) is strict.

For the loopless class, the self-return lengths satisfy \(a,d\ge2\), while \(b,c\ge1\). Set \(z=s_m\). As above, reduce to equality in (3), put \(k=a+d-2\), and minimize the product at \(\{a,d\}=\{2,k\}\). Then \(2\le k\le m-2\), and it suffices to prove
\[
(1-s_m^2)(1-s_m^k)>s_m^{m-k}. \tag{7}
\]
After multiplication by \(s_m^k\), the variable factor is again \(s_m^k(1-s_m^k)\), so the minimum occurs at \(k=2\) or \(k=m-2\). The endpoint differences are
\[
(1-s_m^2)^2-s_m^{m-2}=s_m^4>0
\]
and
\[
(1-s_m^2)(1-s_m^{m-2})-s_m^2
=s_m^2(1-2s_m^2)>0,
\]
using \(2s_m^2+s_m^{m-2}=1\). Hence \(\rho(M(s_m))<1\).

#### Pattern II: one branch has a self-return, the other has two cross-returns

Write
\[
M(z)=
\begin{pmatrix}
z^a&z^b\\
z^c+z^d&0
\end{pmatrix}.
\]
The condition \(\rho(M(z))<1\) is
\[
z^a+z^{b+c}+z^{b+d}<1. \tag{8}
\]

In the general class, the three exponents in (8) have lower bounds \(1,2,2\), and their sum is
\[
a+(b+c)+(b+d)=(a+b+c+d)+b\ge m+3.
\]
By the same exponent-transfer argument, the largest possible value of the left side is
\[
r_m+r_m^2+r_m^m
<
r_m+r_m^2+r_m^{m-1}=1.
\]
Thus \(\rho(M(r_m))<1\).

In the loopless class the three exponents are all at least \(2\), so their sum constraint gives
\[
s_m^a+s_m^{b+c}+s_m^{b+d}
\le 2s_m^2+s_m^{m-1}
<
2s_m^2+s_m^{m-2}=1.
\]
Again the inequality is strict.

#### Pattern III: both branch vertices have two cross-returns

Now
\[
M(z)=
\begin{pmatrix}
0&z^a+z^b\\
z^c+z^d&0
\end{pmatrix}.
\]
In each pair of excursions with the same initial and terminal branch vertices, at most one can have length \(1\), since parallel arcs are forbidden.

For the general class this immediately gives
\[
z^a+z^b\le z+z^2,\qquad
z^c+z^d\le z+z^2.
\]
At \(z=r_m\),
\[
\rho(M(r_m))
\le r_m+r_m^2
<1.
\]

For the loopless class, let \(A=a+b\) and \(C=c+d\). Each is at least \(3\), and by decreasing lengths if necessary it suffices to take \(A+C=m+2\). For fixed \(A\), the first row sum is at most \(s_m+s_m^{A-1}\), and similarly for the second row. Writing \(k=A-1\), where \(2\le k\le m-2\),
\[
\rho(M(s_m))^2
\le
(s_m+s_m^k)(s_m+s_m^{m-k}).
\]
The right side is maximized at \(k=2\) or \(k=m-2\), because after expansion the only variable terms are
\(s_m^{k+1}+s_m^{m-k+1}\), whose sum is maximized at an endpoint by exponent transfer. Hence
\[
\rho(M(s_m))^2
\le
(s_m+s_m^2)(s_m+s_m^{m-2}).
\]
Using \(s_m^{m-2}=1-2s_m^2\),
\[
1-(s_m+s_m^2)(s_m+s_m^{m-2})
=
(1-s_m-s_m^2)^2+s_m(1-s_m)^2(1+s_m)>0.
\]
So \(\rho(M(s_m))<1\).

In every two-branch pattern, (4) and strict monotonicity imply that the actual value \(z=\rho(G)^{-1}\) is strictly larger than the corresponding candidate root \(r_m\), or \(s_m\) in the loopless case. Thus no graph with two branching vertices attains either maximum.

The one-branch roses described above attain the bounds, completing the proof.

## Context and prior work

Klech, *Generating Functions and the Minimum Spectral Radius in Strongly Connected Digraphs with \(m+2\) Edges* (arXiv:2609.18367, submitted 16 September 2026), gives a complete structural classification of \(\mathcal{SC}_{m+2}(m)\), proves the minimum-spectral-radius problem, and states the two maximum-spectral-radius formulas above as Conjecture 5.15.

Earlier work establishes related but different extremal results. Lin and Shu (2012) determine maximum and minimum spectral radius for strongly connected bicyclic digraphs, i.e. the \(n+1\)-arc class. Shan, Wang and He (2022) determine \(\alpha\)-spectral extrema inside several specified families such as rose, generalized-theta and tri-ring digraphs. Those subclass results are compatible with the extremizers above but do not establish the maximum over the entire \(m+2\)-arc strongly connected class.

The proof here does not require the eighteen-family ear classification used for the minimum problem. The excess-outdegree identity reduces the whole class to one or two branching vertices, and first-return Perron equations then permit direct comparison.

## Limitations

The result is specific to the excess-two class \(|E|-|V|=2\). Although the first-return reduction suggests a possible route for larger fixed excess, the number and endpoint patterns of branching excursions grow quickly and no general \(m+k\)-arc theorem is claimed.

The motivating conjecture is extremely recent. Searches of exact and synonymous formulations, the polynomial formulas, “strongly connected tricyclic digraph” spectral-radius literature, and the principal earlier spectral papers located no prior proof of Conjecture 5.15. A not-yet-indexed parallel result remains a residual originality risk.

## References

1. R. Klech, *Generating Functions and the Minimum Spectral Radius in Strongly Connected Digraphs with \(m+2\) Edges*, arXiv:2609.18367 (2026). https://arxiv.org/abs/2609.18367
2. H. Lin and J. Shu, *A note on the spectral characterization of strongly connected bicyclic digraphs*, Linear Algebra and its Applications 436 (2012), 2524–2530. https://doi.org/10.1016/j.laa.2011.09.018
3. H. Shan, F. Wang and C. He, *Some \(\alpha\)-spectral extremal results for some digraphs*, Linear and Multilinear Algebra 70 (2022), 7493–7513. https://doi.org/10.1080/03081087.2021.1996523
