# Sharp conductance-budget plateau for a pendant complete bipartite network

## Finding
Let integers \(p\ge4\), \(q\ge2\), and a total conductance budget \(B>0\) be given. Form \(G_{p,q}^{+}\) from the complete bipartite graph \(K_{p,q}\) by attaching one new leaf \(\ell\) to a distinguished vertex \(a\) in the part of size \(p\). Give every allowed edge an arbitrary nonnegative conductance, with conductances summing to \(B\). For the weighted combinatorial Laplacian \(L\), let
\[
\Lambda_{p,q}(B)=\max_{\substack{w_e\ge0\\\sum_e w_e=B}}\lambda_2(L(w)).
\]
Then
\[
\boxed{\Lambda_{p,q}(B)\le\frac{B}{p+4},\qquad
\Lambda_{p,q}(B)=\frac{B}{p+4}\ \Longleftrightarrow\ 2\le q\le p+2.}
\]
For \(q\le p+2\), one globally optimal allocation, with \(\lambda=B/(p+4)\), assigns \(2\lambda\) to the leaf edge \(\{\ell,a\}\), assigns \(3\lambda/q\) to each edge from \(a\) to the part of size \(q\), and assigns \(\lambda/q\) to each edge from the other \(p-1\) vertices of its part to the opposite part. This allocation is the **unique optimum invariant under independent permutations of the \(p-1\) nondistinguished vertices and the \(q\) opposite-part vertices**; uniqueness among all nonsymmetric allocations is not asserted. For \(q>p+2\), the bound is strictly unattainable by *any* allocation, symmetric or not. The proposed allocation has exact spectral gap \(\lambda\min\{1,(p+2)/q\}\) for every \(q\ge2\), but it is not claimed to remain globally optimal above the transition.

The restriction \(p\ge4\) is substantive. At \((p,q)=(3,2)\), setting the leaf weight to \(11/41\), each distinguished-to-opposite weight to \(8/41\), and each other-to-opposite weight to \(7/82\) yields total budget \(1\) and gap \(6/41>1/7\); hence the same universal bound cannot be extended to all \(p=3\).

## Assumptions and scope
The base graph has disjoint parts \(A\) and \(D\), with \(|A|=p\), \(|D|=q\), one chosen \(a\in A\), and \(A_0=A\setminus\{a\}\) of cardinality \(m=p-1\). The only edges are all \(A\)-to-\(D\) edges and the new leaf edge \(\{a,\ell\}\). Vertex masses are equal; the Laplacian is unnormalized and has off-diagonal entries minus the edge conductance. Budget counts each unoriented edge exactly once. The objective is the second-smallest eigenvalue, including disconnected allocations (then \(\lambda_2=0\)). All quantifiers above concern every \(p\ge4\), \(q\ge2\), and real \(B>0\).

## Proof
**1. A geometry certificate valid against every nonsymmetric allocation.** Let \(m=p-1\ge3\), and index coordinates in the order \(a,A_0,D,\ell\). Define the mean-zero vector
\[
v=(1,\underbrace{-3/m,\ldots,-3/m}_{m},\underbrace{0,\ldots,0}_{q},2)^{\mathsf T}.
\]
Let \(E\) be zero outside its \(A_0\times A_0\) block, where it equals \(I_m-J_m/m\). Put
\[
\sigma^2=\frac{m^2-9}{m(m-1)}\ge0,\qquad X=vv^{\mathsf T}+\sigma^2E.
\]
Both terms are positive semidefinite and annihilate the all-ones vector, so \(X\succeq0\) and \(X\mathbf1=0\). Every admissible edge \(\{i,j\}\) has the **same squared dual distance**
\[
X_{ii}+X_{jj}-2X_{ij}=1.
\]
Indeed the leaf edge changes the \(v\) coordinate by \(1\), each \(a\)-to-\(D\) edge by \(1\), and each \(A_0\)-to-\(D\) edge has squared distance
\[
\frac9{m^2}+\sigma^2(1-1/m)=1.
\]
Furthermore,
\[
\operatorname{tr}X=5+\frac9m+\sigma^2(m-1)=m+5=p+4.
\]
For arbitrary nonnegative allowed weights summing to \(B\), one has \(\operatorname{tr}(LX)=B\). Since \(L\succeq\lambda_2(L)(I-J_{p+q+1}/(p+q+1))\), tracing against \(X\) gives
\[
 B=\operatorname{tr}(LX)\ge\lambda_2(L)\operatorname{tr}X=(p+4)\lambda_2(L).
\]
This proves the unrestricted upper bound without assuming that the optimizer shares the graph's symmetries.

**2. The equality candidate and its entire spectrum.** Scale \(\lambda=B/(p+4)\) to \(1\) temporarily. Give the leaf edge rate \(2\), the \(a\)-to-\(D\) edges rate \(3/q\), and all \(A_0\)-to-\(D\) edges rate \(1/q\). The budget is \(2+3+m=m+5\). The spaces of coordinate vectors summing to zero within \(A_0\), respectively within \(D\), are Laplacian eigenspaces with eigenvalues \(1\) (multiplicity \(m-1\)), respectively \((m+3)/q=(p+2)/q\) (multiplicity \(q-1\)). On the four-dimensional space of vectors constant on each of \(\{\ell\},\{a\},A_0,D\), the Laplacian has the equitable quotient
\[
Q=\begin{pmatrix}
2&-2&0&0\\
-2&5&0&-3\\
0&0&1&-1\\
0&-3/q&-m/q&(m+3)/q
\end{pmatrix},
\]
with characteristic polynomial
\[
\det(tI-Q)=\frac{t(t-1)}q
\bigl(qt^2-(7q+m+3)t+6q+6m+12\bigr).
\]
The two other quotient roots are real because \(Q\) is similar to a real symmetric compression of \(L\). Their sum is \(7+(m+3)/q>7\), their product is \(6+(6m+12)/q>6\), and their polynomial at \(t=1\) equals \(5m+9>0\). Consequently both roots exceed \(1\): their sum excludes both being below \(1\), and the positive value at \(1\) excludes straddling \(1\). Thus
\[
\lambda_2(L_{\mathrm{candidate}})=\frac{B}{p+4}\min\left\{1,\frac{p+2}{q}\right\}.
\]
When \(q\le p+2\), this attains the universal upper bound and is globally optimal.

**3. Sharp necessity, including nonsymmetric competitors.** Any optimum exists because the fixed-budget nonnegative conductance simplex is compact. Suppose an allocation attains \(\lambda=B/(p+4)\). Average its weights over the automorphisms permuting \(A_0\) and \(D\) independently. Concavity of \(\lambda_2\) in \(L\) shows that the averaged allocation also attains \(\lambda\), and has three edge rates: \(z\) for the leaf edge, \(x\) for each \(a\)-to-\(D\) edge, and \(y\) for each \(A_0\)-to-\(D\) edge. Equality in the trace bound of step 1 means the positive-semidefinite matrices \(L-\lambda(I-J/N)\) and \(X\) have zero trace product. As \(v\) belongs to the range of \(X\), this forces \(Lv=\lambda v\). Its leaf, \(A_0\), and \(D\) coordinates give, respectively,
\[
 z=2\lambda,\qquad qy=\lambda,\qquad x=3y.
\]
Hence the averaged optimum is precisely the candidate in step 2. If \(q>p+2\), its eigenvalue \(\lambda(p+2)/q\) is smaller than \(\lambda\), a contradiction. Therefore the upper bound is strictly unattainable above the threshold. The same equations prove uniqueness among invariant optimizers in the equality regime.

**4. Failure of the \(p=3\) extension.** For the explicit budget-one conductances stated in the finding, the exact Laplacian spectrum is
\[
\left\{0,\frac6{41},\frac7{41},\frac{15}{41},\frac{27-\sqrt{113}}{41},\frac{27+\sqrt{113}}{41}\right\}.
\]
Since \(6/41>1/7\), the universal \(B/(p+4)\) assertion would be false at \((p,q)=(3,2)\).

## Verification
Run `python checks/verify.py` from the extracted package directory with Python 3, SymPy, and NumPy installed. The checker symbolically verifies the four-dimensional quotient characteristic polynomial and the dual-geometry identities; checks 57 rational assembled-matrix/Gram identities; compares independently assembled numerical spectra in 189 configurations; and checks the exact six-vertex boundary counterexample. These are supplementary checks of algebra and implementation, not a replacement for the quantified proof in steps 1–3. The proof's certificate \(X\) is given explicitly and needs no numerical eigenvalue claims to establish the all-parameter bound.

## Relationship to prior work
Sun, Boyd, Xiao and Diaconis (2006) formulate the continuous-time fastest-mixing conductance problem and its maximum-variance dual; the present bound uses that dual viewpoint, but adds an explicit feasible Gram certificate and a sharp size-imbalance criterion for a pendant biclique. Göring, Helmberg and Wappler (first available preprint September 2, 2005) develop the analogous absolute-algebraic-connectivity embedding duality and separator structure; the present result is a particular graph-family optimum rather than a new general duality principle. Boyd, Diaconis, Parrilo and Xiao (2007) discuss symmetry reduction for **discrete-time** fastest-mixing chains and treat the intact complete bipartite graph; the pendant-edge continuous-time budget problem and threshold above are not implied by that intact-graph calculation. The proofs here are self-contained and do not rely on a claim of novelty for semidefinite or automorphism averaging methods.

## Limitations
No formula is asserted for the true optimum when \(q>p+2\); only its strict separation below \(B/(p+4)\) is proved. Nonsymmetric optimal weights need not be unique. The all-parameter universal upper bound is asserted only for \(p\ge4\); an explicit example disproves its unrestricted extension to \(p=3\). The present literature comparison cannot exclude every specialized previous treatment of pendant bipartite networks; the 2002 work of Kirkland and Pati on vertex connectivity was only accessible in abstract form. This result has not undergone independent verification.

## References
1. F. Göring, C. Helmberg, M. Wappler, *Embedded in the Shadow of the Separator*, preprint dated September 2, 2005, https://optimization-online.org/2005/09/1202/ (full preprint https://optimization-online.org/wp-content/uploads/2005/09/1202.pdf).
2. J. Sun, S. Boyd, L. Xiao, P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review **48** (2006), 681–699, DOI:10.1137/S0036144504443821, full text https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf.
3. S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955 (first posted September 6, 2007), https://arxiv.org/pdf/0709.0955.
4. S. Kirkland, S. Pati, *On Vertex Connectivity and Absolute Algebraic Connectivity for Graphs*, Linear and Multilinear Algebra **50** (2002), 253–284, DOI:10.1080/03081080290025453 (abstract accessible; full text not inspected).
