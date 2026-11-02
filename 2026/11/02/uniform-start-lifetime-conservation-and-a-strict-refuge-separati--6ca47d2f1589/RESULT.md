# Uniform-start lifetime conservation and a strict refuge-separation risk order on a cyclic habitat

## Finding
Consider a single mobile individual on a cycle with \(n\ge4\) habitat sites. It migrates independently to each nearest neighbor at rate \(\gamma>0\). Exactly two distinct sites are protected from mortality; at every other site death occurs at rate \(\mu>0\). Let \(d\in\{1,\ldots,\lfloor n/2\rfloor\}\) be the cyclic distance between the protected sites. Let \(T_d\) be the death time when the initial site is selected **uniformly from the \(n-2\) unprotected sites**, and put \(L_d(s)=\mathbb E[e^{-sT_d}]\).

**Theorem.** For all choices of \(n,\gamma,\mu\) above, the expected lifetime has the position-independent value
\[
\mathbb E[T_d]=\frac{n}{\mu(n-2)}.
\]
Nevertheless, for every \(s>0\), the **entire Laplace transform** is strictly ordered by separation:
\[
L_1(s)>L_2(s)>\cdots>L_{\lfloor n/2\rfloor}(s).
\]
In particular, the variances obey
\[
\operatorname{Var}(T_1)>\operatorname{Var}(T_2)>\cdots>\operatorname{Var}(T_{\lfloor n/2\rfloor}).
\]
If instead the individual starts uniformly among **all** \(n\) sites, its expected lifetime is strictly largest for adjacent protected sites and strictly smallest when the two protected sites are maximally separated. Thus the choice of initial population changes which quantities depend on spatial placement.

The strict orders compare geometrically distinct separations, up to rotations and reflections. They hold for arbitrary positive migration and mortality rates; neither a large-population approximation nor a particular cycle size is used.

## Assumptions and scope
Let the cycle vertices be \(\mathbb Z/n\mathbb Z\), with protected sites \(0\) and \(d\). The continuous-time migration generator \(Q\) has \(Q_{i,i\pm1}=\gamma\), \(Q_{ii}=-2\gamma\), and all other entries zero. Define the diagonal matrix \(D_d\) whose entry is zero at the two protected sites and one at every unprotected site; put \(K_d=\mu D_d-Q\). Death is an absorbing transition at rate \(\mu\) from each unprotected site. Protection blocks local killing but **does not** absorb the individual, suppress migration, or cause reproduction. Since the finite migration chain is irreducible and unprotected sites exist, death occurs almost surely and every lifetime moment is finite.

The result concerns one moving particle with constant, symmetric nearest-neighbor migration. It is not an assertion about patch occupancy, colonization, density dependence, correlated environmental catastrophes, or unequal dispersal directions.

## Proof
**1. Killed-chain resolvent and lifetime moments.** Write \(\mathbf1\) for the all-ones vector and \(v_d=D_d\mathbf1\) for the unprotected-site indicator. The survival probability from each initial site at time \(t\) is \(e^{-tK_d}\mathbf1\). Consequently the mean vector and second-moment vector are \(K_d^{-1}\mathbf1\) and \(2K_d^{-2}\mathbf1\), respectively. The transform under a uniformly unprotected start is
\[
L_d(s)=1-\frac{s}{n-2}v_d^{\mathsf T}(K_d+sI)^{-1}\mathbf1\qquad(s>0).
\]
The migration generator has zero column sums, so
\[
\mathbf1^{\mathsf T}(K_d+sI)=\mu v_d^{\mathsf T}+s\mathbf1^{\mathsf T}.
\]
At \(s=0\), multiplying on the right by \(K_d^{-1}\mathbf1\) gives \(\mu v_d^{\mathsf T}K_d^{-1}\mathbf1=n\). Dividing by \(n-2\) proves the exact, separation-independent mean. At positive \(s\), setting \(Z_d(s)=\mathbf1^{\mathsf T}(K_d+sI)^{-1}\mathbf1\) yields
\[
L_d(s)=1-\frac{ns}{\mu(n-2)}+\frac{s^2 Z_d(s)}{\mu(n-2)}. \tag{1}
\]
For the second moment, the zero-shift identity similarly gives
\[
\operatorname{Var}(T_d)=\frac{2Z_d(0)}{\mu(n-2)}-\frac{n^2}{\mu^2(n-2)^2}. \tag{2}
\]
For an all-site uniform start, the mean equals \(Z_d(0)/n\).

**2. Exact two-site resolvent.** Fix \(s\ge0\), set \(a=\mu+s\), and let \(B_s=aI-Q\) with Green matrix \(G_s=B_s^{-1}\). If \(U\) has columns the two standard basis vectors at sites \(0\) and \(d\), then \(K_d+sI=B_s-\mu UU^{\mathsf T}\). Because \(B_s\mathbf1=a\mathbf1\) and the Green matrix is symmetric and circulant, the rank-two inverse identity (or direct multiplication of the displayed matrices) gives
\[
Z_d(s)=\frac n a+\frac{2\mu}{a^2[1-\mu(G_s(0)+G_s(d))]}, \tag{3}
\]
where \(G_s(k)=(G_s)_{0k}\). The denominator is strictly positive: \(K_d+sI\) is positive definite, and its restriction to the two-site perturbation subspace forces \(I-\mu U^{\mathsf T}G_sU\) to be positive definite; the common-row-sum eigenvalue is \(1-\mu[G_s(0)+G_s(d)]\). This also holds at \(s=0\).

**3. The cycle Green kernel is strictly decreasing in distance.** There is a unique \(\theta_s>0\) satisfying
\[
\cosh\theta_s=1+\frac{\mu+s}{2\gamma}.
\]
Solving \((a+2\gamma)G_s(k)-\gamma G_s(k-1)-\gamma G_s(k+1)=\mathbf1_{\{k=0\}}\) on the periodic cycle gives the standard, directly verifiable expression
\[
G_s(d)=\frac{\cosh((n/2-d)\theta_s)}{2\gamma\sinh\theta_s\sinh(n\theta_s/2)},
\quad 0\le d\le\lfloor n/2\rfloor. \tag{4}
\]
For integer \(0\le d<\lfloor n/2\rfloor\), the numerator decreases strictly with \(d\); its argument remains nonnegative. Therefore \(G_s(0)>G_s(1)>\cdots>G_s(\lfloor n/2\rfloor)>0\). Formula (3) is strictly increasing in \(G_s(d)\). Hence
\[
Z_1(s)>Z_2(s)>\cdots>Z_{\lfloor n/2\rfloor}(s)
\quad\text{for every }s\ge0.
\]
Substituting in (1), with its strictly positive factor \(s^2\), proves strict Laplace-transform ordering for \(s>0\). Substituting at \(s=0\) in (2) proves strict variance ordering, and dividing by \(n\) proves the opposite-starting-ensemble mean comparison. This completes the proof.

## Verification
The standalone file `verify_refuges.py` uses exact rational Gaussian elimination, not Monte Carlo simulations. It recomputes the killed-chain first and second moments, the Laplace transform, the rank-two Green identity (3), and the analytical cycle kernel (4). It checked \(n=4,\ldots,10\), every admissible separation, two independent positive rational rate pairs, and three positive rational transform parameters: **138 exact rational resolvent comparisons**. All checks passed. These finite checks are corroboration; the quantifiers in the theorem are discharged by the symbolic proof above.

For \(n=6\) and \(\mu=\gamma=1\), the unprotected-start mean is exactly \(3/2\) at every separation. At separations \(d=1,2,3\) the variances are respectively \(41/12\), \(217/76\), and \(11/4\), while the all-site-start means are \(17/9\), \(97/57\), and \(5/3\). At \(s=1\), the three Laplace transforms are \(17/38\), \(107/248\), and \(3/7\). All are exact rational results verified directly from the six-state generator.

Run `python verify_refuges.py` using Python 3; only standard-library modules are required.

## Relationship to prior work
Finite-lattice random walks with traps, their fundamental matrices, and mean first-passage times are established topics; see Hatlee and Kozak (1980), Soler (1982), and Evans and Nord (1985). Those sources study absorbing traps or general exact techniques, and the last two could not be inspected in complete full text. The present theorem does **not** claim to invent resolvent methods or the finite-cycle Green kernel.

Elkin and Possingham (2008) investigated protection, disturbance and dispersal in spatial metapopulations through a one-hundred-patch occupancy process. Ben Zion, Yaari and Shnerb (2010) studied persistence and checkerboard patterns in nonlinear population models with demographic noise. These are biologically relevant but mathematically different stochastic dynamics. Mavroforakis, Mathioudakis and Gionis (2015) studied optimal placement of *absorbing* nodes to shorten random-walk hitting times and proved general supermodularity; their protected-node meaning and objective differ from mortal hazards on the complement, and their published theorems do not state the conditional-mean conservation or strict entire-transform separation law established here.

The new contribution assessed is the combined, exact **all-cycle-size/all-positive-rate conditional-mean identity and full Laplace-transform separation order** for two death-free refuges, with the induced strict variance and all-site-start comparisons. Its general ingredients are classical, so uninspected historical work on partially absorbing cyclic walks remains a real priority risk.

## Limitations
The Laplace-transform order is **not** an assertion of pointwise survival-curve order or full convex stochastic order. Equal mean and strict Laplace-transform differences can coexist; neither distribution strictly stochastically dominates the other. A smaller lifetime variance is not by itself a general conservation-management objective; the preference depends on risk and the population used to choose the initial site. The model includes no births, finite population interactions, local extinction/recolonization, demographic feedback, or variable migration geometry. Zero migration and zero mortality are excluded; in those degenerate limits lifetimes or strict comparisons may fail. Because every exact matrix calculation is elementary once the model is specified, originality is restricted to the explicit universal separation theorem, not to general Markov-chain inversion.

## References
1. M. D. Hatlee and J. J. Kozak, “Random walks on finite lattices with traps,” *Physical Review B* **21** (1980), 1400. DOI: 10.1103/PhysRevB.21.1400. Earliest verified public date 1980-02-15.
2. J. M. Soler, “Alternative exact method for random walks on finite and periodic lattices with traps,” *Physical Review B* **26** (1982), 1067. DOI: 10.1103/PhysRevB.26.1067.
3. J. W. Evans and R. S. Nord, “Random walks on finite lattices with multiple traps: Application to particle-cluster aggregation,” *Physical Review A* **32** (1985), 2926–2943. DOI: 10.1103/PhysRevA.32.2926.
4. C. M. Elkin and H. P. Possingham, “The Role of Landscape-Dependent Disturbance and Dispersal in Metapopulation Persistence,” *American Naturalist* **172** (2008), 563–575. DOI: 10.1086/590962. Electronically published 2008-08-29.
5. Y. Ben Zion, G. Yaari and N. M. Shnerb, “Optimizing Metapopulation Sustainability through a Checkerboard Strategy,” *PLoS Computational Biology* **6** (2010), e1000643. DOI: 10.1371/journal.pcbi.1000643.
6. C. Mavroforakis, M. Mathioudakis and A. Gionis, “Absorbing random-walk centrality: Theory and algorithms,” preprint arXiv:1509.02533, first posted 2015-09-08.
