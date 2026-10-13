# Four genotypes are the sharp threshold for reentrant mutation–selection abundance rankings

## Finding
Consider a connected simple undirected mutation graph, positive genotype replication rates, and a common symmetric mutation rate \(\mu>0\) on every edge. A normalized equilibrium is the positive unit-sum principal eigenvector \(p(\mu)\) of the mutation–selection matrix \(\operatorname{diag}(f)-\mu L\), where \(L\) is the graph Laplacian.

**Sharp-minimum theorem.** On every connected graph with at most three genotypes, no pair of equilibrium frequencies can reverse its strict ordering twice as \(\mu\) increases. On the four-genotype path \(1-2-3-4\), take the replication-rate vector \(f=(1,8,2,3)\). The ordering between genotypes \(1\) and \(3\) reverses exactly twice, at the two roots greater than \(1\) of
\[
F(\mu)=2\mu^3-13\mu^2+22\mu-10.
\]
Writing these roots as \(r_-\in(8/5,5/3)\) and \(r_+\in(4,5)\), with respective approximations \(1.62588594620450\) and \(4.12939283654537\), the exact ordering is
\[
p_1(\mu)<p_3(\mu)\quad(0<\mu<r_-\ \text{or}\ \mu>r_+),
\qquad p_1(\mu)>p_3(\mu)\quad(r_-<\mu<r_+),
\]
and equality holds exactly at \(r_-\) and \(r_+\). Thus genotype \(1\), although intrinsically less fit than genotype \(3\), has greater stationary abundance over a bounded intermediate mutation-rate interval. Both low- and high-mutation regimes restore the opposite ordering.

## Assumptions and scope
The genotype network is any connected simple undirected graph when proving the at-most-three-genotype lower bound. Every genotype has a fixed positive, time-independent replication rate \(f_i\); mutations act along each undirected edge in both directions at rate \(\mu>0\), independently of replication. The deterministic unnormalized abundance equation is \(\dot y=(\operatorname{diag}(f)-\mu L)y\), and its positive normalized equilibrium is the principal eigenvector with entries summing to one. Equivalently normalized frequencies satisfy \(\dot p=(\operatorname{diag}(f)-\mu L)p-(f^{\mathsf T}p)p\). This is an additive continuous-time mutation–selection model, not the multiplicative reproduction-error matrix of the discrete-time Eigen model. A ranking reversal means a change of the strict sign of a fixed pairwise frequency difference as \(\mu\) varies; an identically tied pair is not a reversal.

For the four-genotype example, the matrix is
\[
M(\mu)=\begin{pmatrix}
1-\mu&\mu&0&0\\
\mu&8-2\mu&\mu&0\\
0&\mu&2-2\mu&\mu\\
0&0&\mu&3-\mu
\end{pmatrix}.
\]
All four replication rates are strictly positive. The nonconstant fitness vector makes the principal eigenvalue simple for every positive mutation rate, by irreducibility of the symmetric Metzler matrix.

## Proof
**The lower bound.** Connected graphs on at most three vertices are one vertex, one edge, the three-vertex path, or the triangle. For two adjacent vertices, the higher-replication-rate endpoint has the larger principal eigenvector coordinate for every \(\mu>0\), by the endpoint eigenvector equations. On the triangle, \(L=3I-\mathbf1\mathbf1^{\mathsf T}\), so for the principal eigenpair \((\lambda,p)\),
\[
p_i=\frac{\mu\sum_j p_j}{\lambda+3\mu-f_i}.
\]
All denominators are positive; therefore the ordering of coordinates agrees with the ordering of replication rates and cannot change. On the three-vertex path, the two leaves have a fixed relative order since each satisfies \(p_{\mathrm{leaf}}=\mu p_{\mathrm{center}}/(\lambda+\mu-f_{\mathrm{leaf}})\). Center-versus-leaf equality holds exactly when \(\lambda(\mu)=f_{\mathrm{leaf}}\). Differentiating the simple principal eigenvalue gives
\[
\lambda'(\mu)=-\frac{p^{\mathsf T}Lp}{p^{\mathsf T}p}<0
\]
whenever the replication rates are not all equal: equality would make \(p\) constant and hence all replication rates equal. Hence each center–leaf pair can cross at most once. If every fitness is equal, all coordinates remain tied. This establishes the claimed impossibility of two strict reversals for at most three genotypes.

**Algebraic four-vertex construction.** Let \(z\) be an eigenvalue parameter and set
\[
P(z,\mu)=\det(zI-M(\mu)),\qquad
Q(z,\mu)=(z-8+2\mu)(z-1+\mu)-2\mu^2.
\]
The first two eigenvector equations give
\[
\frac{p_3}{p_1}=1+\frac{Q(\lambda(\mu),\mu)}{\mu^2}.
\]
Thus \(p_1=p_3\) if and only if \(Q(\lambda(\mu),\mu)=0\). Exact polynomial division and elimination yield
\[
P(z,\mu)\bmod Q(z,\mu)
=\mu^2((\mu-1)z-4\mu+3),
\qquad
\operatorname{Res}_z(P,Q)=\mu^4F(\mu).
\]
For \(\mu>0\), a common root must have \(\mu\ne1\) and
\[
z=4+\frac1{\mu-1}.
\]
Substitution gives the exact identity \(Q(4+1/(\mu-1),\mu)=F(\mu)/(\mu-1)^2\); conversely every root of \(F\) other than \(1\) supplies a common eigenvalue of \(P\) and \(Q\).

The cubic has one root in \((7/10,4/5)\), one in \((8/5,5/3)\), and one in \((4,5)\), by alternating exact endpoint signs. These are all its roots, since the intervals are disjoint and \(F\) has degree three. At the first root the common eigenvalue \(4+1/(\mu-1)\) is less than \(1\). But the principal eigenvalue is at least the Rayleigh quotient of the all-ones vector, which is the mean fitness \(7/2\), so this first root does **not** produce a frequency tie. At each of the two roots larger than \(1\), the common eigenvalue exceeds \(4\). Since \(M(\mu)\preceq\operatorname{diag}(1,8,2,3)\) in the Loewner order, its second-largest eigenvalue is at most the second-largest fitness, \(3\). Hence any eigenvalue above \(4\) must be the principal eigenvalue, and both roots greater than \(1\) are genuine pairwise ties.

The two ties are transverse. Indeed, for every positive mutation rate the matrix is an irreducible symmetric tridiagonal matrix and its four eigenvalues are simple. At any common root with \(\mu>1\), the polynomial remainder above fixes the shared eigenvalue uniquely. Thus in the product \(\operatorname{Res}_z(P,Q)=\prod_jQ(\lambda_j(\mu),\mu)\) exactly one continuous factor vanishes. Both admissible cubic roots are simple, so that factor changes sign at each root. Since the first two eigenvector equations express the sign of \(p_3-p_1\) as the sign of \(Q\), each tie reverses the strict ranking. Finally, as \(\mu\downarrow0\), fitness \(8\) at vertex \(2\) is uniquely maximal and first-order perturbation gives \(p_1/p_3\to(8-2)/(8-1)=6/7<1\). Consequently the signs are precisely those in the finding.

A separate high-mutation check gives the same final sign: the positive normalized eigenvector has expansion \(p=(\mathbf1+w/\mu+O(\mu^{-2}))/4\), where \(Lw=f-(7/2)\mathbf1\) and \(\sum_iw_i=0\). Solving yields \(w_1-w_3=-1/2\), hence \(p_1-p_3=-1/(8\mu)+O(\mu^{-2})<0\) for large \(\mu\).

## Verification
Run `python verify_reentrant.py` in an environment with SymPy installed; NumPy is optional for supplementary approximate eigenvector checks. The script reconstructs the matrix directly, recomputes the characteristic polynomial, verifies the polynomial remainder and resultant, checks three disjoint exact rational root brackets, verifies the common-eigenvalue identity, and checks the low- and high-mutation coefficients. A sample successful run prints `VERIFY_OK charpoly=1 quotient_remainder=1 resultant=1` and `VERIFY_OK cubic_positive_root_brackets=3 crossing_eigenvalue_identity=1`. The universal at-most-three-vertex assertion follows from the displayed eigenvector identities and monotonicity proof, not finite numerical enumeration.

## Relationship to prior work
Diffusion-like mutation plus genotype-dependent replication, with localization of the leading eigenvector, is a classical mutation–selection setup (Epstein, arXiv:q-bio/0602027, 2006). Saakian and Hu (2006) examine other analytically solvable quasispecies fitness landscapes. Kostova, Zhou, and Zemla (2011) analyze genotype dominance under replication and degradation in an Eigen-type model. Barbosa, Donangelo, and Souza (2012; first preprint 2011) use graph-constrained mutation and analyze fitness-dependent steady abundance with a random graph and Hamming-based fitness. Seifert and colleagues (2014) explicitly note that equilibrium genotype frequency need not track intrinsic fitness and study inference from the distributions. These motivate the present question but do not, in the primary material inspected, state the sharp four-genotype reentrant ordering theorem or its exact two-switch cubic for a fixed additive path mutation generator. The models' distinctions matter: an existing general eigenvector relation does not by itself establish the sharp minimality and complete crossing count claimed here.

## Limitations
The result is an exact deterministic finite-genotype theorem, not an empirical prediction about a particular viral population. Mutation rates are equal and symmetric on a prescribed restricted path; genotype replication rates do not depend on the mutation parameter. For larger networks, weighted mutation, heterogeneous error processes, nonlinear frequency-dependent selection, and stochastic finite populations, no bound on the number of rank reversals is proved. The numerical root approximations are supplementary: the proof rests on polynomial identities, rational root intervals, and spectral inequalities. Historical sources discuss closely related mutation–selection dynamics; specialized unpublished or inaccessible results could imply the classification, so independent originality validation remains necessary.

## References
1. C. L. Epstein, “Anderson Localization, Non-linearity and Stable Genetic Diversity,” arXiv:q-bio/0602027 (first posted 2006-02-28); *Journal of Statistical Physics* 124, 25–46 (2006), doi:10.1007/s10955-006-9149-0.
2. D. B. Saakian and C.-K. Hu, “Exact solution of the Eigen model with general fitness functions and degradation rates,” *PNAS* 103, 4935–4939 (first publicly available 2006-03-20), doi:10.1073/pnas.0504924103.
3. T. Kostova, C. Zhou, and A. Zemla, “On the role of the degradation rates for the dominance of the fittest in Eigen’s quasispecies model,” *Journal of Biological Dynamics* 5, 531–548 (first published online 2011-04-20), doi:10.1080/17513758.2010.544766.
4. V. C. Barbosa, R. Donangelo, and S. R. Souza, “Quasispecies dynamics with network constraints,” arXiv:1112.3322 (posted 2011-12-14); *Journal of Theoretical Biology* 312, 114–119 (2012), doi:10.1016/j.jtbi.2012.07.032.
5. D. Seifert, F. Di Giallonardo, K. J. Metzner, H. F. Günthard, and N. Beerenwinkel, “A Framework for Inferring Fitness Landscapes of Patient-Derived Viruses Using Quasispecies Theory,” *Genetics* 199, 191–203 (first published online 2014-11-17), doi:10.1534/genetics.114.172312.
