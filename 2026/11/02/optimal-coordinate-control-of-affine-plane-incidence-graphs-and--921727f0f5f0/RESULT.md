# Optimal coordinate control of affine-plane incidence graphs and a concurrent-pencil census

## Finding

Let \(\mathcal A\) be **any existing finite affine plane of order \(q\ge2\)**, without a Desarguesian assumption. Its incidence graph \(G\) has a vertex for every point and every line, with one unit-weight edge for each incidence. For the continuous-time network \(\dot z=-L_Gz+B_Su\), each column of \(B_S\) independently actuates a single selected graph vertex. The following statements form one exact actuator-placement classification.

**(a) Sharp count and obligatory line directions.** Exactly \(q^2-1\) independently actuated vertices are necessary and sufficient for full-state controllability. Every controlling set, of any size, includes line vertices from at least \(q\) distinct parallel classes. There is an optimal set with exactly \(q\) line inputs and \(q^2-q-1\) point inputs, so these two minima are attained together.

**(b) All minimum placements.** If \(S=R\sqcup C\), where \(R\) is a set of selected points, \(C\) a set of selected lines and \(|S|=q^2-1\), put \(T=\mathcal P\setminus R\), so \(|T|=|C|+1\). Then \(S\) controls the system **if and only if** \(C\) meets at least \(q\) distinct parallel classes and the following square real matrix is nonsingular:

\[
H(T,C)=\begin{pmatrix}
\mathbf1_T^{\mathsf T}\\
\bigl(\mathbf1_{\ell\cap T}^{\mathsf T}\bigr)_{\ell\in C}
\end{pmatrix}.
\]

The first row is all ones; the remaining rows mark point–line incidence. The condition gives a finite exact certificate for **every** proposed minimum placement, including placements with nonconcurrent selected lines.

**(c) Exact natural subfamily count.** Fix a point \(O\) and choose exactly \(q\) of its \(q+1\) incident lines as the line controllers. Among the \(\binom{q^2}{q+1}\) possibilities for the \(q+1\) unactuated points, **exactly**

\[
2q(q-1)^q
\]

produce optimal controllability. Consequently the number of distinct optimal sets in which the \(q\) selected line vertices form a concurrent pencil is exactly

\[
\boxed{2q^3(q+1)(q-1)^q}.
\]

These are counts of vertex subsets, not of isomorphism orbits. No numerical optimization, large-order existence assumption, or prime-power hypothesis is used.

## Assumptions and scope

A finite affine plane of order \(q\) has \(q^2\) points, \(q(q+1)\) lines, \(q+1\) parallel classes with \(q\) lines in each, and \(q+1\) lines through each point. Each line contains \(q\) points, each pair of distinct points lies on one line, and two lines in different parallel classes intersect at one point. The theorem is conditional on such a plane existing; it covers both coordinatizable and non-Desarguesian instances.

The graph Laplacian is the *combinatorial*, not normalized, Laplacian, with the displayed incidence edges all having weight one. Inputs are independent scalar signals, each placed at exactly one selected point or line vertex. Controllability means the ordinary finite-dimensional Kalman/PBH full-state property, not observability, approximate controllability, or controllability after varying edge weights.

Write \(P=q^2\), \(M=q(q+1)\) and let \(N\) be the \(P\times M\) point–line incidence matrix. Order graph vertices with points first. Then

\[
L_G=\begin{pmatrix}(q+1)I_P&-N\\-N^{\mathsf T}&qI_M\end{pmatrix},
\qquad NN^{\mathsf T}=qI_P+J_P.
\]

The last identity is exact: a point is on \(q+1\) lines and any two distinct points share exactly one line.

## Proof

**1. Exhaustive eigenspace decomposition.** Since \(NN^{\mathsf T}=qI+J\), the incidence matrix has full row rank \(P\). Its singular values are \(\sqrt{q(q+1)}\) once and \(\sqrt q\) with multiplicity \(P-1\); its right kernel has dimension \(M-P=q\). The radial constant-on-each-bipartition sector has Laplacian eigenvalues \(0\) and \(2q+1\), each simple, with respective eigenvectors \((\mathbf1_P,\mathbf1_M)\) and \(((q+1)\mathbf1_P,-q\mathbf1_M)\).

There is a \(q\)-dimensional eigenspace for eigenvalue \(q\), consisting exactly of \((0,y)\) with \(Ny=0\). Every such \(y\) is constant on each parallel class, with its \(q+1\) class constants \(\alpha_1,\ldots,\alpha_{q+1}\) satisfying \(\sum_c\alpha_c=0\): those vectors lie in \(\ker N\), and their dimension is already \(q\).

For each \(p\perp\mathbf1_P\), the remaining eigenpairs are

\[
\lambda_\pm=\frac{2q+1\pm\sqrt{4q+1}}2,
\qquad (p,\gamma_\pm N^{\mathsf T}p),
\qquad \gamma_\pm=\frac{q+1-\lambda_\pm}{q}\ne0.
\]

Indeed \(NN^{\mathsf T}p=qp\) and \((q+1-\lambda_\pm)(q-\lambda_\pm)=q\). Each of these two eigenspaces has dimension \(P-1\). Their eigenvalues are distinct from the three other eigenvalues for every \(q\ge2\), and all dimensions sum to \(P+M\). Hence the decomposition is exhaustive.

**2. Necessary lower bounds.** If \(S\) contains fewer than \(P-1\) vertices, its coordinate restrictions cannot be injective on either \((P-1)\)-dimensional eigenspace. The PBH criterion implies noncontrollability. Likewise, selected point coordinates vanish identically on the eigenvalue-\(q\) eigenspace. A selection of line vertices in fewer than \(q\) parallel classes leaves at least two class coefficients unobserved; assigning them opposite nonzero values produces a vanishing-on-\(S\) eigenvector. Therefore every controlling set meets at least \(q\) distinct line parallel classes and has at least \(P-1=q^2-1\) vertices.

**3. Necessary and sufficient test for minimum sets.** Fix \(|S|=P-1\). On either of the \(\lambda_\pm\) eigenspaces, being orthogonal to all selected point controls forces \(p\) to be supported in \(T\); being orthogonal to all selected line controls forces \(N_C^{\mathsf T}p=0\), because \(\gamma_\pm\ne0\). The already required condition \(p\perp\mathbf1_P\) becomes \(\mathbf1_T^{\mathsf T}p_T=0\). Thus no such nonzero eigenvector exists if and only if \(H(T,C)p_T=0\) has only the trivial solution. Since \(|T|=|C|+1\), the displayed matrix is square, so this is exactly \(\det H(T,C)\ne0\).

For eigenvalue \(q\), the parallel-class coefficient description from step 1 shows that the restriction to \(C\) is injective exactly when at least \(q\) classes occur. Both radial eigenvectors have no zero coordinate, so every nonempty \(S\) detects them. All PBH eigenspace tests are now accounted for, proving (b).

**4. Sharp construction.** Fix a point \(O\), choose \(q\) of its \(q+1\) incident lines \(\ell_1,\ldots,\ell_q\), and choose one point \(P_i\ne O\) on each \(\ell_i\). These \(q\) selected lines belong to distinct parallel classes and their noncentral points are mutually disjoint. Let \(T=\{O,P_1,\ldots,P_q\}\), actuate all other points and the \(q\) chosen lines. The number of controls is \((q^2-q-1)+q=q^2-1\). The equations \(H(T,C)p_T=0\) read \(p_O+p_{P_i}=0\) for every \(i\), together with \(p_O+\sum_i p_{P_i}=0\). Therefore \((1-q)p_O=0\), forcing all components to vanish because \(q\ge2\). Step 3 proves controllability, and step 2 proves sharpness. It also proves the simultaneous optimality of the number of line controls and total controls in (a).

**5. Exact concurrent-pencil census.** For the fixed \(q\) lines in step 4, the incidence signatures of all points relative to those lines are: the all-ones vector for \(O\) (one point), the \(q\) coordinate vectors \(e_i\) (each achieved by exactly \(q-1\) points), and the zero vector (achieved by exactly \(q-1\) points on the one unselected line through \(O\)). Appending a leading coordinate one, these \(q+2\) distinct signatures form an affine circuit in \(\mathbb R^q\):

\[
\mathbf1=\sum_{i=1}^{q}e_i,
\qquad
1-q+(q-1)=0.
\]

All coefficients in this unique affine dependence are nonzero when \(q\ge2\). Hence any \(q+1\) distinct signatures are affinely independent, while repeated signatures yield dependent columns of \(H(T,C)\). There are \((q-1)^{q+1}\) valid choices omitting the center signature, \((q-1)^q\) choices omitting the zero signature, and \(q(q-1)^q\) choices omitting one of the \(e_i\) signatures. Their sum is \(2q(q-1)^q\). Finally, the concurrent set of \(q\) selected lines is specified uniquely by its intersection point (\(q^2\) choices) and the one omitted direction (\(q+1\) choices); uniqueness holds because \(q\ge2\). Multiplication proves the claimed total census.

## Verification

The standalone file `verify.py` uses Python standard-library arithmetic. For the coordinate affine planes over prime fields of orders \(2,3,5,7\), it checks every entry of \(NN^{\mathsf T}=qI+J\) and the explicit minimum construction. It enumerates **all 120** three-actuator sets at order \(2\), checks their PBH ranks using exact rational Gaussian elimination for all five distinct eigenvalues, and compares them with the placement certificate: **56** sets pass both tests. For a fixed concurrent line set, it exhausts unactuated-point subsets and gets **4** choices at order \(2\) and **48** at order \(3\), matching \(2q(q-1)^q\). It also checks 128 pseudorandom order-three placements against direct modular Kalman ranks, and checks the order-five construction with a direct full Kalman rank over a prime field. The packaged run prints `VERIFY_OK 3514`.

The proof above, not those finite checks, handles every existing affine plane and every admissible order. Arithmetic modulo a prime is used only for finite test cases; it is not used to establish infinite-order nonsingularity.

## Relationship to prior work

The PBH eigenspace test is classical. Zhang, Camlibel and Cao (2011) develop graph-partition controllability bounds and leader choices for distance-regular graphs, notably cycles and complete graphs. A point–line affine incidence graph has different point and line degrees, so it is **not** distance regular, and their explicit distance-regular leader constructions do not imply the present incidence-placement criterion.

Yuan and collaborators (2013) give the general maximum-eigenvalue-multiplicity principle and an algorithmic driver-node framework for symmetric networks. The conclusion that at least \(q^2-1\) independent inputs are needed follows from that known principle **once the incidence spectrum is supplied**; it is not claimed as a stand-alone novelty. The new content assessed here is the geometry-specific line-parallel-class obstruction, the if-and-only-if certificate for *all* minimal coordinate placements, the simultaneous optimal placement construction, and the exact concurrent-pencil count \(2q^3(q+1)(q-1)^q\). These do not appear in the inspected source text and cannot be read off from eigenvalue multiplicity alone.

## Limitations

The statement covers unit-weight combinatorial Laplacians, affine *point–line* incidence graphs and independent single-vertex inputs. It does not cover arbitrary edge weights, projective-plane graphs, arbitrary block designs, constrained feedback gains, actuator noise, or robustness. The general result is conditional on existence of a finite affine plane of the specified order. The certificate can be checked exactly using finite real/integer linear algebra, but the theorem does not give a closed scalar count of **all** minimum placement sets across every possible nonconcurrent line configuration. The concurrent-pencil family has an exact count. This is a mathematical proof with supplementary computational checks, not an independent external audit; a residual publication-priority risk remains for narrowly indexed incidence-network literature.

## References

1. S. Zhang, M. K. Camlibel and M. Cao, “Controllability of Diffusively-Coupled Multi-Agent Systems with General and Distance Regular Coupling Topologies,” *Proceedings of the IEEE CDC/ECC* (December 12–15, 2011), pp. 759–764, DOI: [10.1109/CDC.2011.6160658](https://doi.org/10.1109/CDC.2011.6160658). Accessible paper: https://skoge.folk.ntnu.no/prost/proceedings/cdc-ecc-2011/data/papers/0872.pdf.
2. Z. Yuan, C. Zhao, Z. Di, W.-X. Wang and Y.-C. Lai, “Exact controllability of complex networks,” *Nature Communications* **4**, 2447 (September 12, 2013), DOI: [10.1038/ncomms3447](https://doi.org/10.1038/ncomms3447). Open text: https://pmc.ncbi.nlm.nih.gov/articles/PMC3945876/.
