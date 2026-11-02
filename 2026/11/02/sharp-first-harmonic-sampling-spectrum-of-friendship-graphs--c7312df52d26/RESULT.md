# Sharp first-harmonic sampling spectrum of friendship graphs

## Finding
Let \(q\ge3\) and \(m\ge2\) be integers. Let \(F_m\) be the graph consisting of \(m\) triangles sharing exactly one vertex, and let \(\Omega\) be its set of proper colorings using the cyclic color palette \(\mathbb Z/q\mathbb Z\), with uniform probability. Use the normalized counting inner product on \(L^2(\Omega)\). Form the family comprising the constant function and, for every graph vertex \(v\) and nonzero frequency \(a\in\{1,\ldots,q-1\}\), the character \(\chi_{v,a}(c)=\exp(2\pi i a c(v)/q)\).

Write \(r=1/(q-1)\), \(S=1-r-2r^2\), \(A=1+r\), \(L=1-r+2(m-1)r^2\), and
\[
\mu_{\pm}=\frac{1+L\pm\sqrt{(1-L)^2+8mr^2}}{2}.
\]
Then the complete probability-normalized Gram spectrum consists exactly of \(1\) (multiplicity one) and, for each of the \(q-1\) nonzero frequencies, \(A\) (multiplicity \(m\)), \(S\) (multiplicity \(m-1\)), and \(\mu_-,\mu_+\) (one each). Coincident values add multiplicities.

At the minimal color palette \(q=3\), the Gram matrix has nullity exactly \(2m\), with one independent relation per triangle and nontrivial frequency. For every \(q\ge4\), the character family is linearly independent. In fact, for \(q\ge4\), \(\mu_-\) and \(\mu_+\) are the unique lowest and highest Gram levels, and the sharp squared singular-value condition number is
\[
\kappa_{m,q}^2=\frac{\mu_+}{\mu_-}=\frac{\mu_+^2}{S}=\frac{4m^2r^4}{S}+O_q(m).
\]
At \(q=3\), the sharp condition number **on the nonzero singular subspace, including the constant coordinate**, is \(\kappa_{m,3}^2=1+m/2\). Thus a minimal-color rank defect coexists with linear nonzero conditioning, whereas every fixed larger palette has quadratic squared conditioning.

## Assumptions and scope
All assertions apply to every integer \(m\ge2\) and \(q\ge3\), not only prime powers. The character frequencies use the additive cyclic group of the color names; no field structure is needed. The Gram matrix is that of the functions on **all** proper colorings, not the adjacency or Laplacian matrix of the graph. The quoted condition numbers are ratios of extreme positive Gram eigenvalues, equivalently squared singular-value condition numbers of the restriction/sampling operator with normalized column basis. The ordinary condition number is their square root.

## Proof
There are exactly \(q((q-1)(q-2))^m\) proper colorings: choose the common hub color, then independently choose an ordered pair of distinct colors from the \(q-1\) others for each triangle. Global translation of all colors shows that the constant is orthogonal to every nontrivial character and that different frequency bands \(a\ne b\) are mutually orthogonal.

Fix one nonzero frequency and let the center be \(h\), with outer vertices \((u_j,v_j)\), \(1\le j\le m\). Conditional on \(h\), the two outer colors in any triangle form a uniformly chosen ordered distinct pair from the remaining \(q-1\) colors, independently for different triangles. Character orthogonality implies
\[
\mathbb E[\chi_{u_j,a}\mid h]=-r\chi_{h,a}.
\]
For two different vertices in the same triangle the expectation of \(\chi_{u_j,a}\overline{\chi_{v_j,a}}\) is \(-r\): indeed the numerator from the sum over distinct remaining colors is \(1-(q-1)=-(q-2)\), divided by \((q-1)(q-2)\). For outer vertices in different triangles their correlation is \(r^2\) by conditional independence. Therefore the spatial block has diagonal \(1\), hub–outer and within-triangle entries \(-r\), and across-triangle outer entries \(r^2\).

For each triangle, its outer antisymmetric vector is an eigenvector of value \(A=1+r\), yielding \(m\) independent vectors. The outer vectors constant on each triangle, with total outer sum zero and hub coordinate zero, have eigenvalue \(S=1-r-2r^2\), yielding \(m-1\) dimensions. The remaining orthonormal span consists of the hub vector and the normalized sum of the \(2m\) outer coordinate vectors; the restriction is
\[
B=\begin{pmatrix}1&-\sqrt{2m}\,r\\-\sqrt{2m}\,r&1-r+2(m-1)r^2\end{pmatrix}.
\]
Its eigenvalues are \(\mu_\pm\) as stated and \(\det B=L-2mr^2=S\). These subspaces are orthogonal and account for all \(2m+1\) dimensions in each frequency.

The identity \(S=(q-3)q/(q-1)^2\) shows \(S=0\) exactly at \(q=3\), while \(A>0\). Since \(B\) has positive trace, its smaller eigenvalue vanishes exactly when \(S=0\), and otherwise both eigenvalues are positive. At \(q=3\), the relations \(\chi_{u_j,a}+\chi_{v_j,a}+\chi_{h,a}=0\) hold pointwise for all triangles because the three vertex colors are all distinct. They supply the \(m\) independent null vectors in each nonzero frequency band, matching the spectral nullity \(m\) there and \(2m\) overall. For \(q\ge4\), all eigenvalues are positive.

For \(m\ge2\), the characteristic polynomial of \(B\) at \(A\) equals \(-2(m-1)r^2(1+r)<0\), so \(\mu_-<A<\mu_+\). Also \(S<A\) and \(\mu_+>1\), hence, for \(S>0\), \(\mu_-=S/\mu_+<S\). Thus \(\mu_-\) and \(\mu_+\) are the strict extreme eigenvalues of every nontrivial frequency band; adding the constant eigenvalue \(1\) does not change this conclusion. For \(q=3\), the remaining positive levels are \(A=3/2\), \(\mu_+=1+m/2\), and the constant level \(1\), yielding the asserted nonzero condition number.

Finally, with \(q\) fixed, \(L=2mr^2+S\), so \(\mu_+=2mr^2+O_q(1)\); use \(\mu_+\mu_-=S\) to obtain the quadratic asymptotic when \(q\ge4\). All steps hold for arbitrary integers \(q,m\) in the specified ranges.

## Verification
The companion `verify.py` independently enumerates all proper colorings for nine nontrivial parameter pairs and reconstructs the character correlations by exact integer counts of color differences, then performs numerical Fourier evaluation and diagonalization. It tests \(28\) separate nonzero-frequency blocks with tolerance \(3\cdot10^{-12}\) and verifies the predicted rank boundary and multiplicities. These tests are finite corroboration; the proof above supplies the universal statements and the conditioning asymptotics.

## Relationship to prior work
The underlying friendship/windmill graphs and their structural classification are classical; Mertzios–Unger (2008) give a combinatorial account of the friendship theorem. Loh–Pikhurko–Sudakov (2008) study the chromatic polynomial and the enumeration of proper colorings, not the spectrum of restricted one-site Fourier characters. Their chromatic-counting setting motivates examining harmonic information carried by the uniform coloring measure. The present result uses the elementary conditional distribution within windmill triangles to resolve the complete first-harmonic Gram spectrum and exact conditioning. Other finite Fourier sampling results for cycle graphs, complete multipartite graphs, and colored trees do not imply this graph's spectrum directly: its common hub creates cross-triangle correlation \(r^2\) and a distinct low-rank spectral sector.

## Limitations
The theorem treats only the constant and single-vertex nontrivial additive characters, not higher-degree interactions. It concerns uniformly random proper colorings of friendship graphs; it does not classify all cactus graphs or all Potts temperatures. Originality is assessed by bounded literature and database comparison, not guaranteed against every older specialized formulation. Independent review and external validation have not been performed.

## References
1. George B. Mertzios and Walter Unger, *The Friendship Problem on Graphs*, ROGICS (May 12–17, 2008), pp. 152–158, https://mertzios.net/papers/Conf/Conf_Windmills.pdf .
2. Po-Shen Loh, Oleg Pikhurko, and Benny Sudakov, *Maximizing the number of q-colorings*, arXiv:0811.2625, initially posted November 17, 2008, https://arxiv.org/abs/0811.2625 .
3. Paul Fendley and Vyacheslav Krushkal, *Link invariants, the chromatic polynomial and the Potts model*, arXiv:0806.3484, initially posted June 20, 2008, https://arxiv.org/abs/0806.3484 .
