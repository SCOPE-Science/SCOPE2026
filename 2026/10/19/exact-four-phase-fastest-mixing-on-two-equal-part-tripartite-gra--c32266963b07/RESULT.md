# Exact four-phase fastest mixing on two-equal-part tripartite graphs

## Finding
For every pair of integers \(p,q\ge2\), the globally fastest-mixing symmetric nonnegative stochastic Markov chain supported on the complete tripartite graph \(K_{p,p,q}\), with arbitrary nonnegative holding probabilities, has an explicitly determined second-largest eigenvalue modulus (SLEM). Put \(\kappa=2p/q\). Its minimum SLEM is
\[
\mu_*(\kappa)=
\begin{cases}
1-\kappa,&0<\kappa\le\frac12,\\
\frac{1}{1+2\kappa},&\frac12\le\kappa\le2,\\
\frac{\kappa}{4+3\kappa},&2\le\kappa\le4,\\
\frac{\kappa-1}{3\kappa},&\kappa\ge4.
\end{cases}
\]
The branch formulas agree at all three transition values. Every globally optimal value can be attained by a graph-automorphism-invariant transition matrix. **All such invariant optimizers** (not necessarily all unrestricted optimizers) are classified below. For \(\tfrac12<\kappa<2\) the invariant optimizer set is a nondegenerate closed line segment; outside that open regime it is a singleton. Thus this family exhibits three sharp parameter transitions and a substantial exact degeneracy in optimal allocations.

## Assumptions and scope
Write the vertex classes as \(A\), \(B\), \(C\), with cardinalities \(p,p,q\). Allowed transitions are between *distinct* classes and self-loops, not between different vertices in the same class. The stochastic matrix \(P\) must be real symmetric, entrywise nonnegative, and have every row sum equal to one; transition weights may be zero on allowed edges. The target is
\[
\min_P \left\|P-\frac{\mathbf1\mathbf1^{\mathsf T}}{2p+q}\right\|_2.
\]
For an invariant matrix, assign one transition probability \(x\) to each edge from \(A\) to \(B\), and one probability \(y\) to each edge joining \(C\) to either \(A\) or \(B\). Define \(X=px\), \(Y=qy\), and \(\kappa=2p/q\). Then its diagonal entries are \(1-X-Y\) in \(A\cup B\), and \(1-\kappa Y\) in \(C\). Hence the complete feasibility conditions are
\[
X\ge0,\quad Y\ge0,\quad X+Y\le1,\quad\kappa Y\le1.
\]
Set \(x=X/p\) and \(y=Y/q\) after selecting the parameters below.

The **complete family of invariant optima** is:

1. If \(0<\kappa\le\tfrac12\), \(Y=1\), \(X=0\), and \(\mu_*=1-\kappa\).
2. If \(\tfrac12\le\kappa\le2\), put \(Y=2/(1+2\kappa)\) and \(\mu_*=1/(1+2\kappa)\). Then \(X\) may be *any* number in
\[
\boxed{\max\left\{0,\frac{2(\kappa-1)}{1+2\kappa}\right\}\ \le X\le\ \min\left\{\frac{2\kappa-1}{1+2\kappa},\frac{\kappa}{1+2\kappa}\right\}.}
\]
At either endpoint of this \(\kappa\)-range the interval collapses to one point.
3. If \(2\le\kappa\le4\), put \(Y=4/(4+3\kappa)\), \(X=2\kappa/(4+3\kappa)\), and \(\mu_*=\kappa/(4+3\kappa)\).
4. If \(\kappa\ge4\), put \(Y=1/\kappa\), \(X=2(\kappa-1)/(3\kappa)\), and \(\mu_*=(\kappa-1)/(3\kappa)\).

At \(\kappa=\tfrac12,2,4\) the adjacent parameter descriptions coincide. In the first regime all \(A\)-to-\(B\) transitions vanish; in the fourth, holding probability in \(C\) vanishes. No uniqueness of the minimizing unrestricted stochastic matrix is asserted.

## Proof
**Step 1: symmetry reduction valid for unrestricted competitors.** The objective is the spectral norm of an affine function of \(P\), hence convex. Permutations within the three classes and interchange of \(A,B\) are graph automorphisms and preserve feasibility and the objective. Averaging any feasible matrix over these permutations produces a feasible invariant matrix without increasing its objective. Compactness ensures a minimizer. It therefore suffices to optimize over the two parameters \(X,Y\) to obtain the unrestricted **optimal value**; this argument does not imply all unrestricted optimizers are invariant.

**Step 2: exact spectrum.** The within-class zero-sum subspaces have eigenvalues \(1-X-Y\) (multiplicity \(2(p-1)\)) and \(1-\kappa Y\) (multiplicity \(q-1\)). The difference between the constant vectors on \(A\) and \(B\) has eigenvalue \(1-2X-Y\). The remaining class-constant zero-sum vector takes values \(q\) on both \(A,B\) and \(-2p\) on \(C\), and has eigenvalue \(1-(1+\kappa)Y\). The last eigenvalue is one. Their multiplicities sum to \(2p+q\), and therefore
\[
\mu(X,Y)=\max\{1-X-Y,\ 1-\kappa Y,\ |1-2X-Y|,\ |1-(1+\kappa)Y|\}.
\]
The first two terms are nonnegative on the feasible domain.

**Step 3: exact elimination of \(X\).** Fix feasible \(Y\) and put \(T=1-Y\ge0\). For \(0\le X\le T\), direct inspection of two intersecting affine functions gives
\[
\min_{0\le X\le T}\max\{T-X,\ |T-2X|\}=\frac{T}{3},
\quad\text{uniquely at }X=\frac{2T}{3}.
\]
Thus the minimum over all invariant matrices is the minimum on \(0\le Y\le\min\{1,1/\kappa\}\) of
\[
g_\kappa(Y)=\max\left\{1-\kappa Y,\ (1+\kappa)Y-1,\frac{1-Y}{3}\right\}.
\]
The negative half of \(|1-(1+\kappa)Y|\) is dominated by \((1-Y)/3\) or \(1-\kappa Y\) until the increasing half becomes active; equivalently it can be retained throughout with no change to the minimizing value. Indeed \(1-(1+\kappa)Y\le1-\kappa Y\) for \(Y\ge0\).

**Step 4: minimization of the one-dimensional envelope.** The first affine function is decreasing, the second increasing, and the third decreasing. At \(\kappa\le\tfrac12\), the endpoint \(Y=1\) attains the bound \(1-\kappa Y\ge1-\kappa\), and it uniquely determines \(Y\). For \(\tfrac12\le\kappa\le2\), the first two meet at \(Y=2/(1+2\kappa)\), with common value \(1/(1+2\kappa)\); at that point the third is no greater because \(\kappa\le2\). The intersection is the unique minimizing \(Y\). For \(2\le\kappa\le4\), the second and third meet at \(Y=4/(4+3\kappa)\), with common value \(\kappa/(4+3\kappa)\); the first is no greater because \(\kappa\ge2\), and feasibility follows from \(\kappa\le4\). This again fixes \(Y\). For \(\kappa\ge4\), the bound \((1-Y)/3\ge(1-1/\kappa)/3\) is attained at the feasible endpoint \(Y=1/\kappa\), where the other affine functions lie below it. This endpoint uniquely fixes \(Y\). These calculations prove the four stated optimal values.

**Step 5: classify every invariant minimizer.** In the first and last two regimes the first/third affine terms force \(X=2(1-Y)/3\), except in the first where \(Y=1\) forces \(X=0\). In the middle regime \(Y\) is fixed and the inequalities \(1-X-Y\le\mu_*\) and \(|1-2X-Y|\le\mu_*\), together with \(0\le X\le1-Y\), yield precisely
\[
\max\{0,1-Y-\mu_*\}\le X\le\min\{1-Y,(1-Y+\mu_*)/2\}.
\]
Substitution gives the interval in the theorem; its length is strictly positive exactly when \(\tfrac12<\kappa<2\). All claimed allocations obey feasibility. No other invariant allocations can be optimal.

## Verification
Run the embedded `verify.py` using Python 3, with only the standard library. It constructs exact-rational stochastic matrices, checks every row and spectral eigen-equation, and independently enumerates vertices of the three-variable linear-program formulation. The completed check reports `VERIFY_OK 453 exact matrix designs, 311949 eigen-equation coordinates, 151 independent LP vertex enumerations`. The test sizes and outputs are not a proof for all \(p,q\); Steps 1–5 give the infinite-family proof.

For example \(p=2,q=4\), so \(\kappa=1\), gives optimum \(\mu_*=1/3\), \(Y=2/3\), and any \(X\in[0,1/3]\). Hence distinct invariant optimal chains can omit or retain edges between \(A,B\). For \(p=3,q=2\), \(\kappa=3\), one instead gets the unique invariant optimum \((X,Y)=(6/13,4/13)\) and \(\mu_*=3/13\).

## Relationship to prior work
The foundational formulation of fastest mixing as a semidefinite program and the exact bipartite case appear in Boyd, Diaconis and Xiao (2004). Their subsequent work with Parrilo (2007), especially Section 5.3.2, writes the *general complete multipartite* spectral decomposition and the reduced semidefinite program, but stops short of the four-phase solved \(K_{p,p,q}\) frontier or the optimizer segment given here. Jafarizadeh (2010) treats particular symmetric multipartite interconnection patterns; its analyzed interconnection model is different from the fully connected, unequal-size three-class case here. The graph-theoretic spectral reduction itself is not claimed new. The contribution assessed here is the exact all-ratio minimax solution and the full invariant optimal face.

## Limitations
The Markov chains are symmetric, hence have uniform stationary distribution; arbitrary nonreversible chains or prescribed nonuniform stationary distributions are outside scope. Zero probabilities on allowed edges and diagonal self-loops are permitted. The characterization is complete **among automorphism-invariant** minimizers; only the optimum value and existence of an invariant optimizer are established for unrestricted feasible matrices. This result is not an independent audit of the prior literature. Possible equivalent specialized results that are not indexed in the inspected sources remain a literature-completeness risk.

## References
1. S. Boyd, P. Diaconis and L. Xiao, *Fastest mixing Markov chain on a graph*, SIAM Review 46 (2004), 667–689, DOI: 10.1137/S0036144503423264; first electronically published 2004-10-29. https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf
2. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest mixing Markov chain on graphs with symmetries*, SIAM Journal on Optimization 20 (2009), 792–819, arXiv:0709.0955, especially Section 5.3.2. https://arxiv.org/pdf/0709.0955
3. S. Jafarizadeh, *Fastest mixing Markov chain on symmetric K-partite network*, 2010 preprint, arXiv:1008.2588. https://arxiv.org/pdf/1008.2588
