# A sharp positivity frontier for sixth-order Gauss diffusion on strongly regular graphs

## Finding

For every finite connected, noncomplete, unweighted strongly regular graph \(G\) with parameters \((v,k,\lambda,\mu)\), the completed three-stage, sixth-order Gauss–Legendre method for the diffusion equation \(u'=-Lu\) has a **unique sharp entrywise-positivity horizon**. Every off-diagonal entry of the completed step is strictly positive for every \(h>0\); every diagonal entry is the same strictly decreasing function of \(h\), crossing zero exactly once. Thus the sole obstruction to positivity is simultaneous sign loss of all return coefficients.

Write
\[
P(z)=120-60z+12z^2-z^3,\quad Q(z)=120+60z+12z^2+z^3,
\quad R(z)=P(z)/Q(z).
\]
Let \(r>s\) be the two nontrivial adjacency eigenvalues, with multiplicities \(f,g\), and set \(a=k-r\), \(b=k-s\). There is exactly one positive solution \(H_G\) of
\[
Q(aH_G)Q(bH_G)+fP(aH_G)Q(bH_G)+gP(bH_G)Q(aH_G)=0.
\]
For the completed step \(T(h)=P(hL)Q(hL)^{-1}\),
\[
\boxed{T(h)\text{ is entrywise nonnegative}\quad\Longleftrightarrow\quad 0\le h\le H_G.}
\]
The step is symmetric, has every row sum one, and satisfies \(\|T(h)\|_{2\to2}=1\) for all \(h\ge0\), including steps after positivity fails.

For the Petersen graph, \((v,k,\lambda,\mu)=(10,3,0,1)\), and \(H_G\) is the unique positive root of
\[
20h^6-30h^5-12h^4-147h^3-324h^2-180h-360=0,
\]
namely \(H_G\approx3.12731503346\). Every diagonal is \(163/22231>0\) at \(h=3\), and \(-4057/82955<0\) at \(h=4\), although every off-diagonal remains positive.

## Assumptions and scope

A strongly regular graph has \(v\) vertices, constant degree \(k\), exactly \(\lambda\) common neighbors for adjacent distinct vertices, and exactly \(\mu\) common neighbors for nonadjacent distinct vertices. Assume \(G\) is finite, simple, connected, undirected, noncomplete, and unweighted; then \(\mu>0\), \(v\ge4\). Put \(A\) for its adjacency matrix, \(J\) for the all-ones matrix, and \(L=kI-A\) for its combinatorial Laplacian. The diffusion time step \(h\) is real and nonnegative. All assertions concern the **completed** exact-arithmetic Runge–Kutta step, not the internal stages.

The nontrivial adjacency eigenvalues are the roots \(r>s\) of
\[
t^2-(\lambda-\mu)t-(k-\mu)=0.
\]
Their positive integer multiplicities \(f,g\) satisfy \(f+g=v-1\) and \(fr+gs=-k\); \(a=k-r\) and \(b=k-s\) are strictly positive with \(a<b\). The matrices \(Q(hL)\) are invertible for all \(h\ge0\) because \(Q(z)>0\) for \(z\ge0\). This class includes both primitive and imprimitive strongly regular graphs, with no vertex-transitivity assumption.

## Proof

**1. Scalar rational-function certificates.** For nonnegative real \(z\), \(Q(z)>0\), and differentiation gives the exact identities
\[
R'(z)=-\frac{24\bigl((z^2-15)^2+375\bigr)}{Q(z)^2}<0,
\qquad
\frac{d}{dz}\left(\frac{R(z)-1}{z}\right)
=\frac{2(z^4+120z^2+1200z+3600)}{Q(z)^2}>0.
\]
The quotient has its continuous value \(-1\) at \(z=0\). Also
\[
Q(z)-P(z)=120z+2z^3>0,\qquad P(z)+Q(z)=240+24z^2>0
\]
for \(z>0\), so \(-1<R(z)<1\) at every positive argument, with \(R(0)=1\) and \(\lim_{z\to\infty}R(z)=-1\).

**2. Three-dimensional adjacency algebra.** Counting length-two walks gives
\[
A^2=(\lambda-\mu)A+(k-\mu)I+\mu J,
\qquad L^2=(2k-\lambda+\mu)L-v\mu I+\mu J.
\]
The Laplacian eigenvalues are \(0,a,b\), and \(a+b=2k-\lambda+\mu\), \(ab=v\mu\). Consequently there exist real coefficients \(\beta(h),\gamma(h)\) satisfying
\[
T(h)=I+\beta(h)L+\gamma(h)L^2,
\]
with the interpolation conditions \(R(ah)=1+a\beta+a^2\gamma\) and \(R(bh)=1+b\beta+b^2\gamma\). Set
\[
d(h)=\frac{R(bh)-R(ah)}{b-a}<0,
\qquad
\gamma(h)=\frac{(R(bh)-1)/b-(R(ah)-1)/a}{b-a}>0.
\]
The signs follow from the scalar certificates of step 1, using \(0<a<b\). In addition \(\beta+(a+b)\gamma=d\).

**3. Every off-diagonal entry is strictly positive.** For distinct nonadjacent vertices \(i,j\), \(L_{ij}=0\) and \((L^2)_{ij}=\mu\); hence
\[
T(h)_{ij}=\mu\gamma(h)>0\quad(h>0).
\]
For distinct adjacent vertices, \(L_{ij}=-1\) and \((L^2)_{ij}=\lambda-2k\); thus
\[
T(h)_{ij}=-\beta+(\lambda-2k)\gamma
=-d+\mu\gamma>0\quad(h>0).
\]
These are all off-diagonal entry types on a strongly regular graph. In particular, no secondary off-diagonal threshold or positivity reentry is possible.

**4. All diagonal entries coincide and cross exactly once.** Spectral projectors onto the \(0,a,b\) eigenspaces lie in the adjacency algebra \(\operatorname{span}\{I,A,J\}\), so each has a constant diagonal. Its trace equals its rank; therefore the three respective projector diagonals are \(1/v,f/v,g/v\). Every diagonal of the step is hence
\[
F_G(h)=\frac{1+fR(ah)+gR(bh)}{v}.
\]
For \(h\ge0\), differentiation yields
\[
F'_G(h)=\frac{faR'(ah)+gbR'(bh)}{v}<0.
\]
Since \(F_G(0)=1\) and \(\lim_{h\to\infty}F_G(h)=(2-v)/v<0\), continuity and strict monotonicity supply a **unique** positive zero \(H_G\). Multiplication by \(Q(ah)Q(bh)>0\) gives the degree-six equation in the finding. The off-diagonal sign result proves that the full matrix is entrywise nonnegative exactly until this diagonal zero, inclusive, and never afterward.

**5. Mass and spectral norm.** From \(L\mathbf1=0\) and \(R(0)=1\), \(T(h)\mathbf1=\mathbf1\). The graph is undirected, so \(L\) and \(T\) are real symmetric. Step 1 implies \(|R(ah)|,|R(bh)|<1\) for \(h>0\), while the constant eigenvalue equals one. Hence \(\|T(h)\|_{2\to2}=1\) for all \(h\ge0\).

**6. Petersen exact example.** The nonzero Laplacian eigenvalues are \(a=2\) of multiplicity \(f=5\) and \(b=5\) of multiplicity \(g=4\). Substituting these numbers and cancelling positive factors gives
\[
F_G(h)=\frac{-20h^6+30h^5+12h^4+147h^3+324h^2+180h+360}
{(h^3+6h^2+15h+15)(25h^3+60h^2+60h+24)}.
\]
The stated exact signs at \(h=3,4\) follow by rational substitution, and the general strict-monotonicity argument proves uniqueness of its positive root.

## Verification

The standalone script `verify.py` uses symbolic differentiation and exact rational matrices. It checks both scalar derivative certificates and the Petersen numerator and exact endpoint signs. On six independent strongly regular graph examples (the 5-cycle, Petersen, triangular graphs on 5 and 6 symbols, and 3-by-3 and 4-by-4 rook graphs) at three positive rational time steps each, it reconstructs the graph parameters, confirms the strongly regular identity, evaluates the original rational matrix via exact inversion, computes its reduction modulo the Laplacian minimal polynomial, verifies the two off-diagonal entry types, checks 2,361 matrix entries, and checks row sums. The run reports:

`VERIFY_OK: scalar derivative identities; 6 strongly regular graphs; 2361 exact matrix-entry comparisons; off-diagonal positivity; stochasticity; Petersen sign crossing`

Run from the directory containing the script with `python verify.py` using Python 3 and SymPy. These finite examples are checks, not a substitute for the preceding all-graphs proof.

## Relationship to prior work

Strong-stability-preserving Runge–Kutta theory distinguishes spectral stability from positivity/monotonicity, and the diagonal Padé literature demonstrates positivity obstructions for general positive systems. Neither the general barriers nor the existing sharp [2/2] Markov-chain examples directly give the completed [3/3] Gauss step on strongly regular graphs. Strongly regular graph spectral theory supplies the adjacency algebra and three-eigenvalue structure, but it does not determine the sign of the rational step for all time parameters. Here the two scalar derivative certificates and the graph adjacency identity yield a **global sharp** classification. A complete multipartite graph is strongly regular only in particular balanced cases; classifications confined to complete multipartite graphs leave primitive strongly regular graphs such as the Petersen graph unresolved.

## Limitations

The result concerns finite unweighted strongly regular graph Laplacians, exact real arithmetic, and completed steps of the three-stage Gauss method. It does not imply positivity of Runge–Kutta internal stages, positivity for arbitrary weighted or directed graphs, nonlinear positivity, or improved accuracy. The defining positive root is unique but is not asserted to admit a radical expression for arbitrary parameters. Highly specialized or incompletely indexed literature could contain equivalent statements; no claim of independent audit or exhaustive originality certification is made.

## References

1. S. Gottlieb, C.-W. Shu, E. Tadmor, “Strong stability-preserving high-order time discretization methods,” *SIAM Review* 43 (2001), 89–112. DOI: https://doi.org/10.1137/S003614450036757X . Earliest openly documented publication: 2001-02-02 (original article first-page evidence).
2. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, “Essentially negative news about positive systems,” *Linear Algebra and its Applications* 436 (2012), 3425–3442. DOI: https://doi.org/10.1016/j.laa.2011.12.021 .
3. A. E. Brouwer, W. H. Haemers, *Spectra of Graphs*, Springer (2012), Chapter 9 on strongly regular graphs. Open preprint: https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf .
4. S. Blanes, A. Iserles, S. Macnamara, “Positivity-preserving methods for ordinary differential equations,” *ESAIM: Mathematical Modelling and Numerical Analysis* 56 (2022), 1843–1870. DOI: https://doi.org/10.1051/m2an/2022042 .
5. “Eight-state barrier for Markov positivity of the [2/2] Padé map” (2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab .
