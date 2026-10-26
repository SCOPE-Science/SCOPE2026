# A closed four-parameter canonical tensor-generation test for the Fujino–Sato toric threefolds

## Finding
For every quadruple of integers \(a,b,c,d\), let \(X(a,b,c,d)=Z''_{13}(a,b,c,d)\) denote the smooth complete toric threefold defined below. Define the integer predicate
\[
\mathcal E(u,v,w,z):\quad v+|u|>0,\qquad z+|w|>0,\qquad
\big(uw\ge 0\ \text{or}\ v|w|+z|u|>0\big).
\]
Then the canonical bundle \(K_X\) is tensor-generating **if and only if** all four conditions
\[
\begin{aligned}
&\mathcal E(d,a+2,d+1,c+2),\\
&\mathcal E(a,d+2,a+1,b+d+2),\\
&\mathcal E(b+d,1-a,b+d+1,1-c),\\
&\mathcal E(c,1-d,c+1,1-b-d)
\end{aligned}
\]
and all six wall conditions
\[
\boxed{\quad |b|\ne1,\quad a+d+2\ne0,\quad |c-a|\ne1,\quad
c-d+1\ne0,\quad b+d-a+1\ne0,\quad b+c+d\ne0\quad}
\]
hold. Thus the canonical tensor-generation problem for the entire unrestricted four-integer family reduces to ten explicit integer tests, without quantifiers or fan computations.

In particular, for each fixed triple \((a,b,c)\), an admissible integer \(d\) necessarily belongs to the finite interval
\[ -|a|-1\le d\le |c|. \]
There is nevertheless an unbounded, pairwise torically nonisomorphic **nonprojective** tensor-generating family
\[ X(0,m,m,0),\qquad m\in\mathbb Z,\quad m\ge2. \]
The maximum absolute anticanonical intersection with an invariant curve in this family is \(2m\), which distinguishes its toric isomorphism classes.

## Assumptions and scope
Everything is over an algebraically closed field of characteristic zero, as in the cited tensor-generation criterion. The eight rays of the smooth complete fan in the lattice \(N=\mathbb Z^3\) are, in order,
\[
\begin{array}{llll}
v_1=(1,1,b),&v_2=(1,0,0),&v_3=(0,-1,0),&v_4=(0,0,-1),\\
v_5=(-1,a,d),&v_6=(0,1,0),&v_7=(0,0,1),&v_8=(-1,c,d+1).
\end{array}
\]
The twelve maximal cones, denoted by their ray labels, are
\[
124,\ 234,\ 345,\ 456,\ 146,\ 167,\ 127,\ 237,\ 358,\ 568,\ 378,\ 678.
\]
These are precisely the all-integer Fujino–Sato family. Smoothness and completeness of these fans are established in the source; the statement is **not** about arbitrary three-dimensional fans. Tensor-generation is the canonical-bundle property of Ito–Zeng–Zeng, and we use their equivalence between canonical tensor-generation, the strict ray-vertex test, and nonzero anticanonical intersections on all invariant curves.

## Proof
**Step 1 (eliminating one-dimensional strict feasibility).** For four real numbers \(u,v,w,z\), there exists \(t\in(-1,1)\) such that
\[ ut<v\quad\text{and}\quad wt<z \]
if and only if \(\mathcal E(u,v,w,z)\). Indeed, each half-interval intersects \((-1,1)\) exactly when its threshold exceeds its minimum over the closed endpoints: \(v+|u|>0\) and \(z+|w|>0\). When \(uw\ge0\), both strict half-intervals point in the same direction, or one has zero coefficient; the two separate nonemptiness conditions imply a common witness. When \(uw<0\), the inequalities impose opposite bounds. Their strict compatibility is exactly \(v|w|+z|u|>0\). This argument also covers zero coefficients by the first two conditions. All inequalities are strict, so equality boundaries correctly fail.

**Step 2 (the ray-vertex criterion).** Write \(\ell\) for a linear functional strictly maximized, among a ray's fan-neighbors, at that ray. A ray is a vertex of the neighbor convex hull if and only if such an \(\ell\) exists. The four rays \(v_1,v_2,v_5,v_8\) are automatically strict vertices: the functional given by the first coordinate exposes the two positive and the two negative first-coordinate pairs, and a small perturbation distinguishes either member of each pair (the members are distinct for every integer choice).

For the remaining four rays, normalize the exposing functionals respectively to \(\ell_3=(p,-1,t)\), \(\ell_4=(p,t,-1)\), \(\ell_6=(p,1,t)\), and \(\ell_7=(p,t,1)\). Substitution of their incident neighbors from the displayed twelve cones gives, in each case, \(-1<t<1\); the two strict bounds on \(p\) have a feasible intersection exactly when the following simultaneous conditions hold:
\[
\begin{array}{c|c}
\text{ray}&\text{two inequalities in }t\\ \hline
v_3&dt<a+2,\quad (d+1)t<c+2\\
v_4&at<d+2,\quad(a+1)t<b+d+2\\
v_6&(b+d)t<1-a,\quad(b+d+1)t<1-c\\
v_7&ct<1-d,\quad(c+1)t<1-b-d.
\end{array}
\]
For example, at \(v_3\), the neighbor rays \(v_4,v_7\) force \(-1<t<1\), the ray \(v_2\) forces \(p<1\), and rays \(v_5,v_8\) force \(p>dt-a-1\) and \(p>(d+1)t-c-1\). The other three rows follow by exactly the same substitution with their listed functionals. Applying Step 1 gives **precisely** the four predicates in the statement.

**Step 3 (every invariant curve).** There are exactly eighteen two-dimensional cones in the twelve-triangle fan. For such a cone \(\langle v_i,v_j\rangle\), let \(v_k,v_l\) be the opposite generators of its two incident maximal cones. Smoothness gives a unique integer wall relation \(v_k+v_l=\alpha v_i+\beta v_j\), and the anticanonical degree on the invariant curve is \(2-\alpha-\beta\). Substitution of the eight rays yields the **complete** degree table:
\[
\begin{array}{c|rrrrrrrrr}
\text{wall}&12&14&16&17&23&24&27&34&35\\ \hline
(-K_X)\cdot C&2&1-b&2&b+1&2&b+1&1-b&a+d+2&c-a+1
\end{array}
\]
\[
\begin{array}{c|rrrrrrrrr}
\text{wall}&37&38&45&46&56&58&67&68&78\\ \hline
(-K_X)\cdot C&c-d+1&a-c+1&2&b+d-a+1&a-c+1&2&-b-c-d&c-a+1&2.
\end{array}
\]
Requiring all eighteen degrees to be nonzero reduces exactly to the six displayed wall tests. The cited canonical tensor-generation criterion now proves the equivalence: **all** ray-vertex conditions and **all** wall degrees are necessary and jointly sufficient. There are no other ray or wall cases.

**Step 4 (finite band).** The second ray predicate contains \(d+2+|a|>0\), hence for integer parameters \(d\ge-|a|-1\). The fourth contains \(1-d+|c|>0\), hence \(d\le |c|\). This proves the asserted finite search band without assuming projectivity.

**Step 5 (infinite nonprojective family and separation).** Put \((a,b,c,d)=(0,m,m,0)\). For \(m\ge2\), the first two ray predicates hold immediately. The third and fourth coincide with \(\mathcal E(m,1,m+1,1-m)\): both inequalities in the scalar formulation hold for \(t\) sufficiently close to \(-1\) from above (their values at \(t=-1\) are strictly below the displayed thresholds for \(m\ge2\)). The six wall tests hold, so \(K_X\) is tensor-generating. The Fujino–Sato projectivity condition for these fans is \(b=0\) or \(a=c\); neither holds for this family. On evaluating the eighteen degrees above, their largest absolute value is \(2m\), arising at wall \(67\), and all others have absolute value at most \(m+1<2m\) for \(m\ge2\). Toric isomorphisms permute invariant curves and preserve anticanonical degrees; hence different \(m\) yield nonisomorphic toric varieties.

## Verification
The standalone standard-library program `CHECK.py` reconstructs every wall relation using exact rational arithmetic and independently checks the ray-vertex property by searching Carathéodory convex combinations among fan-neighbors. Its exhaustive parameter sample is \(-2\le a,b,c,d\le2\), consisting of \(625\) quadruples; it also checks the family for \(2\le m\le24\). The recorded output is `VERIFY_OK: 625 exact four-parameter ray/edge tests; 23 family cases`. These **finite checks are supplementary**, not the proof of the universal quantified theorem; Steps 1–5 are the proof.

## Relationship to prior work
Ito, M. Zeng, and X. Zeng, *Tensor-generating line bundles on toric varieties* (arXiv:2610.22279v1, first public October 15, 2026), prove the general canonical ray-and-curve criterion and explicitly pose the unrestricted \(Z''_{13}(a,b,c,d)\) parameter classification as Question 6.6. The present work evaluates that criterion for **all four independent integers**, eliminates all auxiliary inequalities, and supplies an unbounded nonprojective family distinguished by an intrinsic toric invariant. Their explicit one-parameter examples are covered by the test but do not give the unrestricted classification.

Fujino and Sato, *On non-projective complete toric varieties* (arXiv:2412.02392v2), provide the fan and its projectivity characterization, not the tensor-generation classification. A previous computation for the subfamily \(Z''_{13}(a,2,a+2,d)\) is a special case; it does **not** cover arbitrary \((a,b,c,d)\). The general theorem of Ito–Zeng–Zeng is stronger as a criterion for all fans, but does not state the explicit arithmetic specialization or the family above. The novelty is the exact evaluation and parameter geometry, not a new general criterion.

## Limitations
The conclusions concern the stated smooth complete toric fans and the canonical bundle, not general line bundles or abstract varieties up to unrestricted isomorphism. The pairwise distinction is proved for **toric** isomorphisms only. The finite band is necessary, not sufficient in isolation. Originality is relative to literature and published records actually compared; undiscovered equivalent parameter tables remain a residual risk. Independent audit or validation has not been performed.

## References
1. Daigo Ito, Michael R. Zeng, and Xiangru Zeng, *Tensor-generating line bundles on toric varieties*, arXiv:2610.22279v1, October 15, 2026. Theorem 1.1, its canonical specialization, Section 6 and Question 6.6. https://arxiv.org/abs/2610.22279
2. Osamu Fujino and Hiroshi Sato, *On non-projective complete toric varieties*, arXiv:2412.02392v2, December 2024, especially the family \(Z''_{13}\), fan description and projectivity criterion. https://arxiv.org/abs/2412.02392
