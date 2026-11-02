# Sharp three-level actuator thresholds and nodal resonances on weighted friendship networks

## Finding

Consider a weighted friendship graph with integer \(m\ge 2\): the vertices are one hub \(o\) and \(m\) disjoint peripheral pairs \((x_j,y_j)\), for \(1\le j\le m\). The undirected edges \(ox_j\), \(oy_j\), and \(x_jy_j\) have respective conductances \(a>0\), \(c>0\), and \(b>0\), independently of \(j\). Let \(L\) be the unnormalized weighted graph Laplacian. For a vertex set \(S\), let \(E_S\) contain the corresponding standard coordinate columns. Controllability means full Kalman rank for \((-L,E_S)\), not a grounded follower-only dynamical model.

**Theorem (every positive weight and every vertex set).** Write \(k(S)\) for the number of pairs containing at least one controlled peripheral vertex.

* If \(a\ne c\), then \((-L,E_S)\) is controllable precisely when \(k(S)\ge m-1\) and neither of the following obstructions holds: \(o\notin S\), every controlled peripheral vertex is of type \(x\), and \(b=ma\); or \(o\notin S\), every controlled peripheral vertex is of type \(y\), and \(b=mc\).
* If \(a=c=u\) and \(b\ne mu\), controllability holds precisely when every peripheral pair contains a controlled vertex.
* If \(a=c=u\) and \(b=mu\), controllability holds precisely when every peripheral pair contains a controlled vertex **and**, additionally, either the hub is controlled or both peripherals of at least one pair are controlled.

Consequently, the minimum number of independent vertex actuators is

\[
\nu_m(a,c,b)=
\begin{cases}
m-1,&a\ne c,\\
m,&a=c,\ b\ne ma,\\
m+1,&a=c,\ b=ma.
\end{cases}
\]

All minimum placements are characterized by the preceding criterion. More explicitly, when \(a\ne c\), choose exactly one peripheral vertex in each of any \(m-1\) pairs; the all-\(x\) choices are excluded at \(b=ma\), and the all-\(y\) choices are excluded at \(b=mc\). There are \(m2^{m-1}\) such choices in the generic case and \(m(2^{m-1}-1)\) on either exceptional weight surface. When \(a=c\) and \(b\ne ma\), choose one peripheral from each pair, giving \(2^m\) minimum sets. When \(a=c\) and \(b=ma\), choose one peripheral from each pair and then either add the hub or add the other peripheral of exactly one pair, giving \((m+2)2^{m-1}\) minimum sets.

For comparison, the underlying unweighted friendship graph has zero-forcing number \(m+1\). Therefore the \(m-1\) fixed-weight minimum for unequal spoke types saves exactly two vertex inputs compared with its strong-structural zero-forcing guarantee.

## Assumptions and scope

All parameters are quantified: \(m\in\{2,3,\ldots\}\), \((a,c,b)\in(0,\infty)^3\), and \(S\subseteq\{o,x_1,y_1,\ldots,x_m,y_m\}\). Edge weights are shared by every pair but are allowed to differ between the two hub ports. Every selected vertex has its **own** scalar input. Rank is over \(\mathbb R\); exact equality of conductances is intended. The graph is connected because all weights are positive.

The statement is about control of all \(2m+1\) state variables, \(\dot z=-Lz+E_Su\). It does not assert robustness of controllability Gramians near exceptional weights, and it does not treat arbitrary independent edge weights or arbitrary choices of which vertex is the hub.

## Proof

**1. Invariant splitting and the global spectrum.** Use vector coordinates \((z;w_1,\ldots,w_m)\), with \(w_j=(z_{x_j},z_{y_j})^{\mathsf T}\). Set

\[
A=\begin{pmatrix}a+b&-b\\-b&c+b\end{pmatrix},
\qquad q=\binom ac,
\qquad D=ac+b(a+c)>0.
\]

The Laplacian acts by

\[
(Lz)_o=m(a+c)z_o-q^{\mathsf T}\sum_{j=1}^m w_j,
\qquad (Lz)_j=Aw_j-qz_o.
\]

There is an orthogonal invariant decomposition into the difference space \(U=\{z_o=0,\ \sum_j w_j=0\}\), of dimension \(2(m-1)\), and the common-pair space \(W=\{w_1=\cdots=w_m\}\), of dimension three. The restriction to \(U\) consists of \(m-1\) copies of \(A\). Because \(b>0\), the two eigenvalues

\[
\lambda_\pm=\frac{a+c+2b\pm\sqrt{(a-c)^2+4b^2}}2
\]

are distinct, and each associated eigenvector of \(A\) has **both** coordinates nonzero.

In an orthonormal basis of \(W\), the restricted Laplacian is

\[
H=\begin{pmatrix}
m(a+c)&-\sqrt m\,a&-\sqrt m\,c\\
-\sqrt m\,a&a+b&-b\\
-\sqrt m\,c&-b&c+b
\end{pmatrix}.
\]

Its eigenvalues are \(0\) and the two positive roots of

\[
\mu^2-\big((m+1)(a+c)+2b\big)\mu+(2m+1)D=0.
\]

**2. The asymmetric case has no hidden spectral overlap.** Assume \(a\ne c\). A vector perpendicular to \(q\) in the pair space is a multiple of \((c,-a)\), but

\[
A\binom c{-a}=D\binom1{-1},
\]

which is not proportional to \((c,-a)\) unless \(a=c\). Thus \(q\) has a nonzero inner product with both eigenvectors of \(A\). Standard symmetric arrowhead elimination now shows that the three eigenvalues of \(H\) are simple and disjoint from \(\lambda_\pm\). Indeed, a common eigenvalue of \(A\) and \(H\) would force the hub coordinate of an \(H\)-eigenvector to vanish by projection on the corresponding \(A\)-eigenvector; the remaining hub equation would then require the same eigenvector to be perpendicular to \(q\), a contradiction. A repeated eigenvalue of \(H\) would likewise give a nonzero eigenvector at zero hub coordinate by dimensionality, again impossible. Hence each nonzero global mode has a nonzero hub coordinate.

For a global eigenvector with common coordinates \((z_o,x,y)\), the condition \(x=0\) forces \(-by-az_o=0\). Eliminating its eigenvalue from the hub and \(y\) equations gives

\[
(b-ma)\big((a+c)b+ac\big)=0.
\]

Since the second factor is strictly positive, a global mode vanishing at every \(x_j\) exists **only** when \(b=ma\). Conversely, at this equality the vector with \(z_o=-m\), all \(x_j=0\), and all \(y_j=1\) is a global eigenvector, with eigenvalue \(ma+(m+1)c\). Interchanging \(a,x\) with \(c,y\) proves that a global mode vanishes on all \(y_j\) precisely when \(b=mc\), witnessed by \(z_o=-m\), all \(x_j=1\), all \(y_j=0\). These two positive parameter surfaces are distinct when \(a\ne c\).

**3. PBH conditions for asymmetric spokes.** For a fixed \(\lambda_\pm\), every difference-mode eigenvector has \(w_j=t_jv_\pm\) with \(\sum_jt_j=0\), where both coordinates of \(v_\pm\) are nonzero. Observing at least one leaf in a pair is therefore exactly the condition \(t_j=0\) for that pair. There is no nonzero invisible difference mode if and only if \(k(S)\ge m-1\); if at least two pairs are missed, choose opposite nonzero amplitudes on them. By step 2, the remaining nonconstant global modes can be invisible only for an all-\(x\) leaf-only set at \(b=ma\) or an all-\(y\) leaf-only set at \(b=mc\). The zero mode is the all-ones vector, visible whenever \(S\ne\varnothing\). The PBH criterion therefore proves the first case of the theorem.

**4. Coincident spoke weights.** Now put \(a=c=u\). The pair-symmetric difference eigenvectors have eigenvalue \(u\) with multiplicity \(m-1\). Independent pair-antisymmetric vectors \((t_j,-t_j)\), for arbitrary \(t_j\), have eigenvalue \(u+2b\) with multiplicity \(m\). In the common-pair space the remaining eigenvalues are \(0\) and \((2m+1)u\). The only collision involving these positive eigenspaces occurs at \(b=mu\), where the pair-antisymmetric and hub-versus-pairs eigenspaces merge to dimension \(m+1\).

Observing the pair-antisymmetric modes requires at least one observed peripheral in **every** pair. Off the collision this also observes all other modes: any one-per-pair set sees the pair-symmetric differences, the nonconstant common mode, and the constant mode. At the collision, one-per-pair measurements have rank only \(m\) on an \((m+1)\)-dimensional merged eigenspace. One extra measurement at the hub or at the opposite peripheral of any pair raises this restriction to rank \(m+1\); any other choice leaves a nonzero invisible merged eigenvector. This proves the remaining cases and all minimum set descriptions.

**5. Counts and zero forcing.** The counts follow by choosing the unobserved pair and the peripheral types, excluding just the forbidden all-one-type pattern on a nodal surface; or, at the symmetric collision, by distinguishing the added hub from a second leaf. To show \(Z(F_m)=m+1\), note that any initially entirely white peripheral pair stays entirely white under the color-change rule: only its two pair vertices and the hub can reach it, and the hub sees two white vertices. Thus every zero-forcing set contains a peripheral from each pair. If exactly one peripheral in every pair is initially black and the hub is white, no black vertex has a unique white neighbor. At least \(m+1\) initial black vertices are needed. The hub together with one peripheral from each pair forces every remaining peripheral, attaining \(m+1\).

## Verification

The standalone, standard-library script `verify.py` constructs the weighted Laplacian directly, forms the full Kalman matrix \([E_S,LE_S,\ldots,L^{2m}E_S]\), and computes rank over exact rational numbers using `fractions.Fraction` elimination. It compares the rank with the closed PBH criterion for **9,126** test instances. Exhaustive vertex sets are covered for \(m=2,3\) across 45 triples of small positive integer weights for each \(m\); all sets of sizes \(m-1,m,m+1\) are checked for six separate \(m=4\) parameter choices, including both nodal surfaces and the symmetric collision. Invoke `python3 verify.py` from the extracted files. Successful output is `PASS: 9126 exact rational controllability comparisons`.

This finite verification tests implementation, placements, eigenvalue collisions, and boundary examples. It does not establish the theorem for infinitely many \(m\) or real parameters; that conclusion is supplied by steps 1–5 of the proof.

## Relationship to prior work

Monshizadeh, Zhang and Camlibel (2014) relate zero-forcing sets to controllability **uniformly over qualitative matrix classes**, not to minimum inputs for this fixed weighted Laplacian. The zero-forcing baseline \(m+1\) is consistent with that theory. Xiang, Zhu, Chen and Chen (2013) provide weighted-network algebraic/graph-theoretic controllability tests and note possible controllability improvements from changing edge weights, but do not provide this motif's complete positive-weight classification or the two nodal equalities. Mousavi, Haeri and Mesbahi (2018) treat ordinary (unweighted) cograph Laplacians; the unweighted friendship graph is a covered special case, where the theorem here reduces to \(m\) inputs. The extra claims assessed here are the exact asymmetric-spoke \(m-1\) law, sharp codimension-one placement failures at \(b=ma\) and \(b=mc\), and the symmetric collision at \(b=ma\) for all \(m\).

A related earlier calculation of grounded leader-selection **trace of inverse** on symmetric friendship graphs addresses a different objective, rather than the full-state Kalman controllability predicate. Published zero-forcing and general PBH criteria do not by themselves supply these explicit all-parameter formulas without the invariant-space and nodal calculation above.

## Limitations

The edge conductances are pairwise repeated across all petals, and inputs are independent coordinate channels. No claim is made for arbitrary perturbations from that three-parameter weight structure, follower-only grounding, robustness, minimal control energy, numerical conditioning, or fixed-amplitude inputs. In exact arithmetic, arbitrarily small \(a-c\ne0\) changes the minimum count; this can be badly conditioned in practice. The overlap assessment is based on inspected literature and targeted searches, not a proof of unique priority; a specialized equivalent historical result may remain undiscovered. Independent mathematical verification has not been performed.

## References

1. N. Monshizadeh, S. Zhang and M. K. Camlibel, *Zero forcing sets and controllability of dynamical systems defined on graphs*, arXiv:1403.4868, first publicly posted 2014-03-19, https://arxiv.org/abs/1403.4868 .
2. L. Xiang, J. J. H. Zhu, F. Chen and G. Chen, *Controllability of Weighted and Directed Networks with Nonidentical Node Dynamics*, Mathematical Problems in Engineering (2013), doi:10.1155/2013/405034, https://doi.org/10.1155/2013/405034 .
3. S. S. Mousavi, M. Haeri and M. Mesbahi, *Laplacian Dynamics on Cographs: Controllability Analysis through Joins and Unions*, arXiv:1802.03599, first publicly posted 2018-02-10, https://arxiv.org/abs/1802.03599 .
4. A. Rahmani, M. Ji, M. Mesbahi and M. Egerstedt, *Controllability of Multi-Agent Systems from a Graph-Theoretic Perspective*, SIAM Journal on Control and Optimization 48 (2009), 162–186, doi:10.1137/060674909, https://doi.org/10.1137/060674909 .
