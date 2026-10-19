# A prime-order arithmetic controllability transition for anisotropic tori

## Finding
Let \(p\ge5\) be an odd prime. On the periodic grid \(\mathbb Z_p\times\mathbb Z_p\), place conductance \(a>0\) on each horizontal cycle edge and \(b>0\) on each vertical cycle edge. If \(a/b\in\mathbb Q_{>0}\), the least number of independent vertex inputs required for full-state controllability of the continuous-time Laplacian system is exactly
\[
\nu_p(a,b)=\begin{cases}4,&a\ne b,\\8,&a=b.\end{cases}
\]
For \(a\ne b\), four inputs at \(\{0,1\}\times\{0,1\}\) suffice; for \(a=b\), eight at \(\{0,1\}\times\{0,1,2,3\}\) suffice. Both lower bounds are unconditional over all vertex-input placements of the stated sizes.

A general real-parameter consequence is that four inputs are optimal whenever \(a/b\notin E_p\), where \(E_p\) is the explicit finite set of positive ratios of nonzero differences of distinct cycle-Laplacian eigenvalues defined below. Rational ratios enter this finite set only at one, but the claim does not classify optimal input counts at the other exceptional algebraic ratios.

## Assumptions and scope
Write \(L_p\) for the standard Laplacian of the undirected simple cycle \(C_p\), with every cycle edge of unit weight, and
\[
L_{p;a,b}=aL_p\otimes I_p+bI_p\otimes L_p.
\]
The vertex set is indexed by \((x,y)\in\mathbb Z_p^2\). For any vertex subset \(S\), \(B_S\) denotes the matrix whose columns are the standard coordinate vectors at those vertices; each selected vertex receives its own independent scalar control. We study the real time-invariant system \(\dot z=-L_{p;a,b}z+B_Su\). Controllability means the ordinary Kalman full-state rank condition, or equivalently the Popov–Belevitch–Hautus (PBH) rank condition. The graph need not be pinned and the constant consensus mode is included among the states. No assertion is made for arbitrary non-coordinate input matrices, time-dependent gains, irrational exceptional ratios, or cycles of composite length.

For \(h=(p-1)/2\), define \(\lambda_0=0\) and \(\lambda_k=2-2\cos(2\pi k/p)\) for \(1\le k\le h\). These are the distinct cycle-Laplacian eigenvalues. Put
\[
E_p=\left\{\frac{\lambda_i-\lambda_k}{\lambda_\ell-\lambda_j}>0:\ i,k,j,\ell\in\{0,\ldots,h\},\ i\ne k,\ j\ne\ell\right\}.
\]
This set is finite and consists of positive real algebraic numbers.

## Proof
**1. Cyclotomic independence.** Let \(\zeta=e^{2\pi i/p}\). Suppose rational \(q_1,\ldots,q_h\) obey \(\sum_{k=1}^hq_k\lambda_k=0\). Define
\[
P(X)=\sum_{k=1}^h q_k(2-X^k-X^{p-k})\in\mathbb Q[X].
\]
Then \(P(\zeta)=0\) and \(\deg P\le p-1\). Since the minimal polynomial of \(\zeta\) over \(\mathbb Q\) is \(\Phi_p(X)=1+X+\cdots+X^{p-1}\), we have \(P=c\Phi_p\) for some \(c\in\mathbb Q\). But \(P(1)=0\), while \(\Phi_p(1)=p\), hence \(c=0\). For every \(1\le k\le h\), the coefficient of \(X^k\) in \(P\) is \(-q_k\), because the exponent pairs \(\{k,p-k\}\) are disjoint. Therefore every \(q_k=0\). The \(\lambda_1,\ldots,\lambda_h\) are rationally linearly independent, in particular distinct and nonzero.

**2. Resonance classification.** The Fourier vectors \(\varphi_{s,t}(x,y)=\zeta^{sx+ty}\) diagonalize \(L_{p;a,b}\), with eigenvalue \(a\lambda_{\bar s}+b\lambda_{\bar t}\), where \(\bar s\in\{0,\ldots,h\}\) labels the class \(\{s,-s\}\). For \(a/b\in\mathbb Q\), any equality
\[
a\lambda_i+b\lambda_j=a\lambda_k+b\lambda_\ell
\]
becomes, by independence, \((a/b)(e_i-e_k)=e_\ell-e_j\), where \(e_0=0\) and \(e_i\) are the standard vectors for \(i\ge1\). If distinct pairs occur, both difference vectors are nonzero, and any nonzero coordinates have modulus one. Hence their positive ratio must be one. Thus for \(a\ne b\) with rational ratio there are no cross-pair collisions. For arbitrary positive real ratio, a cross-pair collision implies \(a/b\in E_p\), proving the nonexceptional real-ratio corollary. Rational independence also gives \(E_p\cap\mathbb Q_{>0}=\{1\}\).

**3. Sharp lower bounds.** For \(a\ne b\) in the rational-ratio scope, a spectral label pair \((i,j)\) has multiplicity \(d_id_j\), where \(d_0=1\) and \(d_i=2\) for \(i>0\). As \(h\ge2\), the maximum multiplicity is four. If \(a=b\), the unordered pairs \(\{i,j\}\) label distinct eigenvalues by rational independence. The multiplicity is \(d_i^2\) for \(i=j\) and \(2d_id_j\) for \(i\ne j\); a pair of distinct positive indices attains eight, and no label has greater multiplicity. For a symmetric state matrix, PBH requires every eigenspace of dimension \(d\) to inject under restriction to the input coordinates, so at least \(d\) independent vertex inputs are required. This proves the lower bounds four and eight.

**4. Four adjacent inputs in the anisotropic case.** The Fourier modes in one distinct label pair form the tensor product of two frequency sets \(T_i=\{0\}\) if \(i=0\), or \(T_i=\{i,-i\}\) if \(i>0\). Restricting them to \(\{0,1\}\times\{0,1\}\) produces the Kronecker product of the one-dimensional evaluation matrices with columns \((1,\zeta^s)^\top\), \(s\in T_i\), and similarly in the other coordinate. For nonzero \(i\), the relevant two-column determinant is \(\zeta^{-i}-\zeta^i\ne0\), as \(p\) is odd. Each factor has full column rank and so does the tensor product. Therefore the four-input patch passes PBH for every eigenspace.

**5. Eight adjacent inputs in the isotropic case.** Fix an unordered pair \(\{i,j\}\). Its modes are the union of \(T_i\times T_j\) and \(T_j\times T_i\), taking the union only once if \(i=j\). At most four distinct vertical frequencies \(t\) appear. On the four consecutive vertical sites \(y=0,1,2,3\), their evaluation columns form a full-column-rank Vandermonde matrix, because the roots \(\zeta^t\) are distinct. For each fixed vertical frequency, there are at most two horizontal frequencies (and when there are two they are the distinct residues \(\pm i\) or \(\pm j\)). Their restrictions to \(x=0,1\) form a full-column-rank Vandermonde matrix. Taking linear combinations of the modes that vanish at all eight patch sites, vertical Vandermonde independence first separates the groups of constant vertical frequency, then horizontal independence forces every coefficient to zero. Thus each eigenspace restricts injectively, proving PBH controllability with eight inputs.

The lower and upper bounds agree in both regimes, so the classification is exact. A scalar shift of the state matrix does not alter its eigenspaces, and hence does not alter these input counts.

**6. Prime restriction matters.** On \(C_6\), the positive distinct Laplacian eigenvalues include \(\lambda_1=1\) with multiplicity two and \(\lambda_2=3\) with multiplicity two. At weights \(a=1,b=2\), the distinct label pairs \((1,1)\) and \((2,0)\) both give eigenvalue three; their independent subspaces have dimensions four and two, respectively. Thus the product eigenspace has dimension at least six and no four vertex controls can work. This is an explicit composite-order obstruction, not a proof about all composite orders.

## Verification
Run `python verify_prime_tori.py` with NumPy installed. The executable performs 85 checks of Fourier-mode PBH restrictions, independently assembled full weighted Laplacians and orthogonal eigenbases, exact-multiplicity predictions in the tested cases, and invariance under scalar shifts. Cases include primes \(5,7,11\) and unequal ratios \(1/2,2,2/3,4/7,1001/1000,1/1001\). Full-matrix eigenspace checks are run for primes \(5\) and \(7\), while Fourier checks also cover \(11\). These finite floating-point checks support but cannot establish the quantified theorem; the proof above provides the infinite-family argument. No formal proof assistant or independent audit was used.

## Relationship to prior work
Notarstefano and Parlangeli (arXiv:1203.0129v1, first public 1 March 2012) develop controllability criteria for grid graphs defined using Cartesian products of paths, not periodic weighted prime tori. Chapman, Nabi-Abdolyousefi and Mesbahi (2014) prove general PBH and Cartesian-product principles, notably their `p-simple` condition that distinct factor-eigenvalue sums do not collide; this general principle explains the tensor-product part of the present proof. It does **not** itself establish cyclotomic independence or show that all unequal positive rational direction ratios meet the condition. The present claim is the explicit arithmetic no-resonance result together with exact minimal coordinate-input constructions and the sharp isotropy transition.

Li, Li, Liu and Hu (2026, DOI 10.1109/TAC.2026.3698015) explicitly announce exact minimal control sets for torus grid graphs. We do not claim their isotropic/unweighted torus result as novel. Available abstract material does not identify a rationally anisotropic weighted classification; however the full text could not be inspected, so equivalent coverage remains a serious novelty risk. Independent evaluation should compare the full result, especially any weighted-torus extensions.

## Limitations
The equality-case result is included to quantify the anisotropic transition and is not claimed as newly discovered. The prime-order and rational-ratio conditions are mathematical hypotheses, not numerical approximations. At other algebraic exceptional ratios in \(E_p\), the optimal input count is not classified; no claim of robust numerical conditioning is made as \(a/b\) approaches one. The 2026 torus-grid paper's full text was unavailable and may contain a stronger applicable theorem. The result establishes mathematical controllability, not energy bounds or practical controller placement cost.

## References
1. G. Notarstefano and G. Parlangeli, *Controllability and observability of grid graphs via reduction and symmetries*, arXiv:1203.0129v1 (1 March 2012), https://arxiv.org/abs/1203.0129 ; DOI: 10.1109/TAC.2013.2241493.
2. A. Chapman, M. Nabi-Abdolyousefi and M. Mesbahi, *Controllability and Observability of Network-of-Networks via Cartesian Products*, IEEE Transactions on Automatic Control (2014), DOI: 10.1109/TAC.2014.2328757.
3. T. Li, Y. Li, Z.-X. Liu and X. Hu, *Minimal Controllability of Sphere and Torus Grid Graphs*, IEEE Transactions on Automatic Control (2026), DOI: 10.1109/TAC.2026.3698015 (abstract examined, full paper inaccessible).
