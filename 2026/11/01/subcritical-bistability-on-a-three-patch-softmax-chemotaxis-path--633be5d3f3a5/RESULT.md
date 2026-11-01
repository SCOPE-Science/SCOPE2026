# Subcritical bistability on a three-patch softmax chemotaxis path

## Finding
For the logistic metapopulation chemotaxis system of Kim, Zhang, Zhao, and Cooney on the unweighted three-vertex path, there is a *strictly stable* spatially homogeneous equilibrium and a *distinct strictly stable* spatially heterogeneous equilibrium at the same parameters, even though the homogeneous equilibrium is strictly stable against every graph eigenmode. An exact rational equilibrium and exact Routh–Hurwitz inequalities certify both attractors without numerical continuation. The two basins contain open subsets of the positive orthant. This coexistence persists under sufficiently small perturbations of the parameters.

## Assumptions and scope
Vertices are labelled \(0,1,2\), with undirected edges \(0\!\sim\!1\) and \(0\!\sim\!2\), and no leaf–leaf edge. For each vertex define positive population \(n_i\) and chemical \(c_i\), satisfying
\[
\dot n_i=n_i(1-n_i)+10\sum_{j\sim i}\frac{e^{\chi c_i}n_j-e^{\chi c_j}n_i}{e^{\chi c_i}+e^{\chi c_j}},\qquad
\dot c_i=n_i-c_i+\frac1{60}\sum_{j\sim i}(c_j-c_i).
\]
These equations are precisely the three-patch specialization of the cited graph model with logistic rate and capacity one, chemical production and decay one, population migration parameter \(\eta_n=30\), chemical migration parameter \(\eta_c=1/10\), and graph normalization by the number of vertices. Fix
\[
\chi=\chi_*:=\frac{51}{20}\log\frac{258}{167}.
\]
Then both equilibria
\[
E_{\rm hom}:(n_0,n_1,n_2;c_0,c_1,c_2)=(1,1,1;1,1,1)
\]
and
\[
E_{\rm pat}:\left(\frac{21}{17},\frac{14}{17},\frac{14}{17};\frac{187}{153},\frac{127}{153},\frac{127}{153}\right)
\]
are linearly asymptotically stable (all six eigenvalues of each Jacobian have strictly negative real part). Each is therefore a locally exponentially attracting equilibrium with an open positive basin. No assertion about all initial conditions, the global number of equilibria, or traveling patterns is made.

## Proof
**Exact patterned balance.** Let \(u=n_0\), \(v=n_1=n_2\), \(C=c_0\), and \(D=c_1=c_2\). The proposed values satisfy \(C-D=20/51\). Thus \(\chi_*(C-D)=\log(258/167)\), and the softmax weight toward the hub is exactly
\[
s=\frac{e^{\chi_* C}}{e^{\chi_* C}+e^{\chi_* D}}=\frac{258}{425}.
\]
The flux into the hub *per edge* is \(J=10[(u+v)s-u]=42/289\). Direct arithmetic gives \(u(1-u)=-84/289\), \(v(1-v)=42/289\), so the hub equation has residual \(-84/289+2J=0\) and each leaf residual \(42/289-J=0\). Chemical balances hold exactly:
\[
u-C+\frac{D-C}{30}=0,\qquad v-D+\frac{C-D}{60}=0.
\]
All six coordinates are strictly positive.

**Homogeneous stability below the entire modal threshold.** For the three-path normalized negative graph Laplacian, use the positive Laplacian eigenvalues \(\kappa=0,1/3,1\). The population–chemical linearization at \(E_{\rm hom}\) reduces for each \(\kappa\) to
\[
H_\kappa=\begin{pmatrix}-1-15\kappa&15\chi_*\kappa\\1&-1-\kappa/20\end{pmatrix}.
\]
Its trace is negative. The determinant \((1+15\kappa)(1+\kappa/20)-15\chi_*\kappa\) is positive at \(\kappa=1\) for \(\chi_*<28/25\), and at \(\kappa=1/3\) for \(\chi_*<61/50\); the zero mode has two eigenvalues \(-1\). The strict bound \(\chi_*<28/25\) follows without floating-point approximations: put \(z=91/425\), use \(\log(258/167)=2\operatorname{artanh}z<2[z+z^3/(3(1-z^2))]\), and obtain
\[
\chi_*<\frac{47803483}{43086000}<\frac{28}{25}.
\]
Therefore every homogeneous eigenmode is exponentially damped.

**Patterned symmetric modes.** The graph and the patterned equilibrium are invariant under swapping leaves. Set \(m=(u+2v)/3\), \(z=u-v\), \(e=C-D\), and let \(s=(1+e^{-\chi e})^{-1}\). On the leaf-symmetric subspace,
\[
\dot m=m(1-m)-\tfrac29z^2,\quad
\dot z=z(1-2m-z/3)+30[m(2s-1)+(z/3)(s-2)],\quad
\dot e=z-\tfrac{21}{20}e.
\]
The mean chemical \(h=(C+2D)/3\) satisfies \(\dot h=m-h\); it adds one stable eigenvalue \(-1\) and does not feed back into the other equations. At the patterned equilibrium \((m,z,e)=(49/51,7/17,20/51)\), differentiation gives
\[
J_{\rm sym}=\begin{pmatrix}
-47/51&-28/153&0\\
28/5&-3857/255&(1809612/122825)\chi_*\\
0&1&-21/20
\end{pmatrix}.
\]
Writing its characteristic polynomial as \(\lambda^3+a_1\lambda^2+a_2\lambda+a_3\), exact arithmetic yields
\[
a_1=5813/340,\quad
a_2=\frac{28(139553-64629\chi_*)}{122825},\quad
a_3=\frac{21(6249047-5400112\chi_*)}{8352100},
\]
\[
a_1a_2-a_3=\frac{7(3151150651-1421751828\chi_*)}{41760500}.
\]
All four displayed quantities are strictly positive throughout \(0<\chi_*<28/25\): the last three are decreasing affine functions of \(\chi_*\) and remain positive at \(28/25\). The cubic Routh–Hurwitz criterion gives strict stability.

**Patterned antisymmetric modes.** A leaf-difference population perturbation and leaf-difference chemical perturbation evolve under
\[
J_{\rm anti}=\begin{pmatrix}-571/85&(603204/122825)\chi_*\\1&-61/60\end{pmatrix}.
\]
Its trace is negative and its determinant decreases with \(\chi_*\) but remains strictly positive even at \(28/25\). Both remaining eigenvalues therefore have negative real parts. The combined invariant subspaces exhaust all six state dimensions, proving hyperbolic attraction. Hyperbolic equilibria persist with their stability under sufficiently small smooth changes of parameters by the implicit-function theorem and eigenvalue continuity.

## Verification
The standalone `check.py` uses exact rational and symbolic computations to reproduce all six equilibrium residuals, the coefficient identities in both symmetry blocks, the strict rational upper bound on \(\chi_*\), and the Routh–Hurwitz and two-dimensional determinant inequalities. It also independently differentiates the unreduced six-dimensional system and numerically checks its spectrum, as a supplementary diagnostic. Run `python check.py` with Python, SymPy, and NumPy installed. The analytical proof above, rather than finite numerical tests, establishes the infinite-dimensional parameter-neighborhood assertion.

## Relationship to prior work
Kim, Zhang, Zhao, and Cooney introduced the softmax finite-graph chemotaxis equations, their homogeneous linear stability criteria, and weakly nonlinear spatial bifurcation analysis, with a two-patch graph worked out explicitly. Their graphon analysis discusses possible subcritical regimes but does not provide an exact strictly bistable three-vertex finite-graph parameter witness below every linear instability threshold. Continuum chemotaxis with logistic growth has a substantial theory of spatial patterns, including work of Jin, Wang, and Zhang; continuum results do not directly imply the stated nonlinear finite-graph witness. The present claim is the explicit hyperbolic coexistence on the sparse three-path, rather than the general existence of chemotaxis patterns or the general possibility of bistability.

## Limitations
This is an existence-and-robustness result for a fixed finite graph and a particular parameter point. It does not classify all steady states, all stability regions, or the global dynamics. It does not prove independence from every historical nonlinear chemotaxis theorem; related broad results could subsume some conclusions. Independent review and historical priority certification have not been performed.

## References
1. D. Kim, Y. Zhang, Y. Zhao, and D. B. Cooney, *The Keller–Segel Model for Chemotaxis on Metapopulation Graphs and Graphons*, arXiv:2610.31049v1 (first public 2026-10-22), https://arxiv.org/abs/2610.31049 .
2. H. Jin, W. Wang, and Z.-A. Zhang, *Pattern formation in a Keller–Segel chemotaxis model with logistic growth*, https://arxiv.org/abs/1407.5246 .
3. T. Ma and S. Wang, *Dynamic Transition and Pattern Formation for Chemotactic Systems*, https://arxiv.org/abs/1206.5084 .
