# Three distinct mobility optima and an exact replacement-matrix law for regular networks

## Finding

Consider one territorial-raider individual based at each vertex of a finite connected simple undirected \(d\)-regular graph \(G\), where \(d\ge 2\). At each interaction event, individuals move independently. An individual stays at its home vertex with probability \(h/(h+d)\) and visits any one of its \(d\) neighbors with probability \(1/(h+d)\), where \(h>0\). In a group of size \(k\ge 2\), an ordered pair of distinct group members has replacement weight \(1/(k-1)\); an individual alone has self-replacement weight one.

Write \(A\) for the adjacency matrix of \(G\), \(W\) for the expected replacement-weight matrix, \(p=1/(h+d)\), and \(q=h/(h+d)\). Define
\[
\begin{aligned}
a_d(h)&=\frac{2h}{d(h+d)}\left[1-(1-p)^d\right],\\
b_d(h)&=p^2\int_0^1(1-q+qt)(1-p+pt)^{d-2}\,dt,\\
s_d(h)&=q(1-p)^d+d^2p^2(1-p)^{d-1}.
\end{aligned}
\]
Then **the entire replacement network** admits the exact polynomial identity
\[
\boxed{W=s_d(h)I+a_d(h)A+b_d(h)(A^2-dI).}
\]
In particular, for distinct homes \(i,j\),
\[
W_{ij}=a_d(h)\mathbf{1}_{\{i,j\}\in E(G)}+b_d(h)|N(i)\cap N(j)|,
\]
so pair weights depend only on adjacency and the number of common neighbors. Even on graphs with triangles, the self-weight \(s_d(h)\) and the total nonsingular replacement temperature \(T_d(h)=1-s_d(h)\) depend on \(d,h\), not on the graph topology. Every row of \(W\) sums to one, and \(W\) is symmetric.

The common temperature has its **unique global maximum at \(h=1\)**, with
\[
T_d(1)=1-\left(\frac{d}{d+1}\right)^d.
\]
If \(G\) is triangle-free and \(i,j\) are adjacent, their replacement weight is exactly \(a_d(h)\). This weight has a **unique global maximizer** \(h_d^*\) satisfying \(h_d^*>d\). More precisely, put \(x_d=1/(h_d^*+d)\). It is the unique solution in \((0,1/d)\) of
\[
\boxed{(1-x_d)^{d-1}[2-(d+1)x_d]=1.}
\]
The unweighted meeting probability for such a pair is \(2h/(h+d)^2\), whose unique maximizer is \(h=d\). Thus three intrinsically different optimal fidelities are **strictly ordered** for every \(d\ge2\):
\[
\boxed{h_{\rm temperature}=1< h_{\rm encounter}=d <h_{\rm replacement}=h_d^*.}
\]
For \(d=2\), \(h_2^*=(1+\sqrt{13})/2=2.302775637\ldots\). Furthermore,
\[
\lim_{d\to\infty}\frac{h_d^*}{d}
=\frac{1}{2-\operatorname{W}_0(e^2)}-1
=1.2580784965\ldots,
\]
where \(\operatorname{W}_0\) is the principal real Lambert inverse of \(w\mapsto we^w\).

## Assumptions and scope

The graph is finite, simple, connected and undirected; every vertex has the same degree \(d\ge2\), and hosts exactly one individual. A simultaneous group is the set of individuals at one vertex after **independent**, memoryless movement. The weight assigned to a distinct pair in a group of size \(k\) is \(1/(k-1)\); the expected weight \(W_{ij}\) sums this quantity over possible encounter sites and other attendees. The diagonal weight \(W_{ii}\) is the probability that individual \(i\) is alone. These are the standard normalized replacement weights of the territorial-raider framework, not bare co-location probabilities and not fixation probabilities. The matrix identity and temperature classification hold with or without triangles. The sharp edge-optimum statement requires triangle-freeness. The parameter \(h\) is strictly positive. These conclusions are exact for every admissible graph, integer degree and fidelity.

## Proof

Fix two distinct individuals based at \(i,j\). They can meet at \(i\) and \(j\) exactly when their homes are adjacent. At each of those two sites, the probability that both attend is \(qp\). The number of additional individuals present has distribution \(X\sim\operatorname{Bin}(d-1,p)\), independent of their attendance: the other \(d-1\) neighbors of the site visit with probability \(p\). The contribution from both home sites is therefore
\[
2qp\,\mathbb E\frac1{1+X}
=2qp\frac{1-(1-p)^d}{dp}=a_d(h).
\]
Here the binomial identity follows directly from the integral \(1/(k+1)=\int_0^1 t^k\,dt\).

Any other common encounter site must be a common neighbor of the two home vertices. At such a site, both focal individuals visit with probability \(p\), while the site's own resident attends independently with probability \(q\), and each of its other \(d-2\) neighbors attends with probability \(p\). Consequently the number of additional attendees is \(Y=U+Z\), where \(U\sim\operatorname{Bernoulli}(q)\) and \(Z\sim\operatorname{Bin}(d-2,p)\) are independent. Each common-neighbor site contributes
\[
p^2\mathbb E\frac1{1+Y}
=p^2\int_0^1(1-q+qt)(1-p+pt)^{d-2}\,dt=b_d(h).
\]
Distinct possible meeting sites may be summed because the two focal individuals occupy exactly one site each. Counting such sites yields the off-diagonal formula. For the diagonal, an individual can be alone either at home, with probability \(q(1-p)^d\), or at one of \(d\) neighboring sites, with total probability \(d\,p(1-q)(1-p)^{d-1}=d^2p^2(1-p)^{d-1}\). This proves the asserted \(s_d(h)\), the matrix identity, and symmetry. For each realized movement configuration, the outgoing replacement weights of an individual sum to one: either it is alone and assigns weight one to itself, or it assigns \(1/(k-1)\) to each of its \(k-1\) groupmates. Taking expectations proves row stochasticity; since \(W\) is symmetric, column stochasticity follows.

Direct differentiation, with \(d\) fixed, gives
\[
\frac{d}{dh}s_d(h)
=\frac{d(h-1)(h+d-1)^{d-2}(2h+d-1)}{(h+d)^{d+2}}.
\]
All factors except \(h-1\) are positive for \(h>0\), hence \(s_d\) has exactly one global minimum, at \(h=1\). This proves the temperature maximum and its stated value.

For a triangle-free graph, adjacent vertices have no common neighbor, so \(W_{ij}=a_d(h)\). Set \(x=1/(h+d)\); then \(0<x<1/d\) and
\[
a_d(h)=\frac2d(1-dx)[1-(1-x)^d],\qquad
\frac{da_d}{dx}=2\big[(1-x)^{d-1}(2-(d+1)x)-1\big].
\]
Let \(g_d(x)=(1-x)^{d-1}(2-(d+1)x)\). On \((0,1/d)\),
\[
g_d'(x)=-(1-x)^{d-2}\,[3d-1-d(d+1)x]<0,
\]
with \(g_d(0)=2>1\) and \(g_d(1/d)=(1-1/d)^d<1\). Hence precisely one critical point occurs; reversing the monotone change \(x=1/(h+d)\) shows it is the unique global maximum of \(a_d(h)\).

Moreover, strict Bernoulli's inequality gives \((1-x)^{-(d-1)}>1+(d-1)x\) for \(x>0\). At \(x=1/(2d)\), the positive factor \(2-(d+1)x\) equals \(1+(d-1)x\); thus \(g_d(1/(2d))<1\). The unique root satisfies \(x_d<1/(2d)\), whence \(h_d^*=1/x_d-d>d\). Direct differentiation of the meeting probability \(2h/(h+d)^2\) shows its unique maximum is \(h=d\). Since \(d\ge2\), the three peaks have the announced strict order.

For \(d=2\), \(a_2(h)=h(2h+3)/(h+2)^3\). Its derivative has numerator \(-2h^2+2h+6\), yielding the exact root \((1+\sqrt{13})/2\). Finally, write \(y_d=dx_d\). The defining equation becomes \((1-y_d/d)^{d-1}[2-(1+1/d)y_d]=1\). Strict monotonicity and uniform convergence on \([0,1/2]\) give \(y_d\to y\), the unique root of \(e^{-y}(2-y)=1\). Its exact value is \(y=2-\operatorname{W}_0(e^2)\), proving the limit.

## Verification

The companion `verify.py` checks the formula against the *original group-sum definition*, not against a rearrangement of the claimed matrix identity. Using exact rational arithmetic, it constructs every nonempty occupancy subset at each possible meeting site and compares all entries of \(W\) for cycles on five and six vertices, complete bipartite graphs of degrees three and four, the cube, and the triangular prism. Four positive rational fidelity values are checked; the test covers 1,044 individual matrix-entry comparisons, including graphs with and without triangles, and verifies every row sum exactly.

At \(h=2\) on the three-regular triangular prism, the checker obtains exactly
\[
a_3=244/1875,\quad b_3=109/3750,\quad s_3=272/625,\quad T_3=353/625.
\]
Edges within one triangular face have weight \(a_3+b_3=199/1250\), whereas vertical edges have weight \(a_3=244/1875\), despite the **same temperature for every vertex**. The infinite-degree maximization and all-graph matrix formula are proved analytically; finite replay is only an independent consistency check.

## Relationship to prior work

Pires and Broom (2026) develop the independent territorial-raider movement model, completely mixed population benchmarks, and numerical home-fidelity comparisons for multiplayer dilemmas. Broom, Erovenko and Rychtář (2020/2021) give the general replacement-weight group-sum formula; Schimit, Pattni and Broom (2019) numerically compare many network topologies using temperature and group size. Pires and Broom (2024) investigate networks of communities, especially at large fidelity. Haq, Schimit and Broom (2025) analyze predictors for complete networks and note large interaction temperature near \(h=1\).

These foundational definitions, known complete-mixing formulas, and the general role of temperature are **not** new claims here. The contribution is the *all-regular-graph closed matrix polynomial in adjacency and common-neighbor counts*, together with its exact all-degree separation of temperature, encounter, and replacement-weight maximizers. The result is a structural property of replacement weights; it is **not** a theorem that the maximizing fidelity also maximizes evolutionary cooperation or fixation probabilities.

## Limitations

The result assumes one individual per vertex, a single common fidelity parameter, regular undirected networks, independent memoryless movement, and the specified group-size normalization. For heterogeneous degree, multiple residents per site, coordinated travel or different updating rules, the formulas may change. Triangle-free adjacency is essential for the sharp edge-optimum formula: edges belonging to triangles receive an extra positive common-neighbor term and can have a different maximizing fidelity. The theorem quantifies the static replacement network only; it asserts nothing about selected mutant-fixation probabilities, Nash equilibria, or nonlinear cooperation outcomes. Although primary literature was inspected, equivalent regular-network formulas in older specialist papers remain a possibility.

## References

1. D. L. Pires and M. Broom, “Multiplayer social dilemmas in completely mixed populations and networks of mixing communities,” *Journal of Mathematical Biology* 93, 51 (2026), published 1 October 2026. https://doi.org/10.1007/s00285-026-02464-5.
2. M. Broom, I. V. Erovenko and J. Rychtář, “Modelling Evolution in Structured Populations Involving Multiplayer Interactions,” *Dynamic Games and Applications* 11, 270–293 (2021), first published 27 June 2020. https://doi.org/10.1007/s13235-020-00358-9.
3. P. H. T. Schimit, K. Pattni and M. Broom, “Dynamics of multiplayer games on complex networks using territorial interactions,” *Physical Review E* 99, 032306 (2019). https://doi.org/10.1103/PhysRevE.99.032306.
4. D. L. Pires and M. Broom, “The rules of multiplayer cooperation in networks of communities,” *PLOS Computational Biology* 20, e1012388 (2024). https://doi.org/10.1371/journal.pcbi.1012388.
5. H. Haq, P. H. Schimit and M. Broom, “Predictors of Fixation Probability on Complete Networks Involving Multiplayer Interactions Under Coordinated Movement Systems,” *Dynamic Games and Applications* (2025). https://doi.org/10.1007/s13235-025-00635-5.
