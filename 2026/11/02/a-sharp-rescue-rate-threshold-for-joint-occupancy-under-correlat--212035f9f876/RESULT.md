# A sharp rescue-rate threshold for joint occupancy under correlated catastrophes

## Finding

Consider two habitat patches subject to local extinctions, recolonization, and sudden environmental catastrophes. Keep the marginal catastrophe hazard of each occupied patch fixed, but vary the fraction of catastrophic events shared by the two patches. A larger shared fraction always **lowers the stationary expected number of occupied patches** when there is positive rescue between patches. Yet it may **raise**, preserve, or lower the probability that **both** patches are occupied, with one sharp threshold at \(d=c+e+k\).

For \(c,d,e,k>0\) and \(\rho\in[0,1]\), put
\[
\Delta=(c+e+k)^2+cd,\qquad D_\rho=2\Delta-\rho k(c-d+e+k).
\]
The exact stationary quantities are
\[
J_\rho=\Pr\{X=Y=1\}=\frac{2c(c+d)}{D_\rho},
\qquad
M_\rho=\mathbb E[X+Y]=\frac{2c[2(c+d+e+k)-\rho k]}{D_\rho}.
\]
Consequently,
\[
\frac{dM_\rho}{d\rho}=-\frac{4cdk(c+d)}{D_\rho^2}<0,
\qquad
\frac{dJ_\rho}{d\rho}=\frac{2ck(c+d)(c-d+e+k)}{D_\rho^2}.
\]
Thus the sign of the joint-occupancy response is positive, zero, or negative according as \(d<c+e+k\), \(d=c+e+k\), or \(d>c+e+k\), uniformly in \(\rho\). The equality is an exact invariance along the entire interpolation, not just equality at the two endpoints.

## Assumptions and scope

The occupancy variables \(X,Y\) take values in \(\{0,1\}\). There are four independent Poisson mechanisms: (i) each empty habitat gains a population from outside at rate \(c>0\); (ii) an empty habitat gains a population from the other habitat at rate \(d>0\), but only when that other habitat is occupied; (iii) each occupied habitat becomes empty at independent local-extinction rate \(e>0\); (iv) each occupied habitat is cleared by an *individual* catastrophe clock of rate \((1-\rho)k\), while an additional *shared* catastrophe clock of rate \(\rho k\) clears every currently occupied habitat simultaneously, where \(k>0\) and \(0\le\rho\le1\). All clocks are independent, except for the common effect of the single shared clock. Each occupied patch has the same marginal instantaneous catastrophic loss hazard \((1-\rho)k+\rho k=k\), irrespective of \(\rho\). The shared clock has no observable state change when both patches are already empty.

These rules give a finite irreducible continuous-time Markov chain and therefore a unique stationary distribution. No claim is made for closed systems with \(c=0\), heterogeneous patch parameters, non-Poisson shocks, population abundances beyond binary occupancy, or a general network of patches.

## Proof

Let \(p_j\) denote the stationary probability that exactly \(j\in\{0,1,2\}\) patches are occupied. Exchangeability makes occupancy count a Markov chain. Its nonzero transition rates are
\[
0\to1:2c,\quad 1\to0:e+k,\quad 1\to2:c+d,
\quad 2\to1:2[e+(1-\rho)k],\quad 2\to0:\rho k.
\]
The last transition is a simultaneous loss of both occupied patches, not two independent single losses. Stationarity at counts \(2\) and \(0\) yields
\[
(c+d)p_1=[2e+(2-\rho)k]p_2,
\qquad 2cp_0=(e+k)p_1+\rho kp_2.
\]
Combining these equations with \(p_0+p_1+p_2=1\), one obtains
\[
p_2=\frac{2c(c+d)}{D_\rho},\qquad
p_1=\frac{2c[2e+(2-\rho)k]}{D_\rho},
\]
\[
p_0=\frac{2(e+k)^2+\rho k(c+d-e-k)}{D_\rho}.
\]
In particular, \(J_\rho=p_2\) and \(M_\rho=p_1+2p_2\), giving the asserted formulas.

The denominator is strictly positive everywhere: it is affine in \(\rho\), with \(D_0=2[(c+e+k)^2+cd]>0\) and
\[
D_1=2c^2+2cd+4ce+3ck+dk+2e^2+3ek+k^2>0.
\]
Direct differentiation gives both displayed derivative identities. All their non-sign factors are strictly positive. Thus \(M_\rho\) is strictly decreasing for every \(d>0\), whereas \(J_\rho\) is strictly increasing, constant, or strictly decreasing precisely according as \(d\) lies below, at, or above \(c+e+k\). The formulas hold at both endpoints by continuity, completing the proof.

## Verification

The included `verify.py` independently constructs the full four-state generator rather than using the occupancy-count chain. It solves 144 exact-rational stationary systems over different positive rates and four correlation fractions, verifies the stated stationary formulas, reconstructs both symbolic derivatives, and checks three exact cases with \(c=e=k=1\):

* At \(d=1\), increasing \(\rho\) from zero to one changes joint occupancy from \(1/5\) to \(2/9\), but lowers mean occupancy from \(4/5\) to \(7/9\).
* At the threshold \(d=3\), joint occupancy is \(1/3\) at both endpoints (indeed at every \(\rho\)), while mean occupancy drops from \(1\) to \(11/12\).
* At \(d=4\), joint occupancy falls from \(5/13\) to \(10/27\), and mean occupancy falls from \(14/13\) to \(26/27\).

Run `python verify.py` with SymPy available. These finite checks support reproduction; the exact stationarity argument and derivative factorization prove the all-parameter theorem.

## Relationship to prior work

Johst and Drechsler (2003) studied the effect of spatially correlated landscape disturbance on *mean extinction time*, reporting that correlation reduced persistence in their spatially explicit dynamic-habitat models. Hiebeler (2005) examined synchronized block disturbances in a continuous-time spatial contact process, including mean-density predictions from pair approximations. Keeling (2000) developed approximate moment equations for coupled metapopulations and distinguished mean density, correlation, and extinction risks. Sutherland, Elston and Lambin (2012) empirically quantified correlated extinction and rescue effects. These contributions motivate the question and are not claimed as new.

The finding here concerns an **exact, finite, irreducible stationary law** with fixed marginal catastrophe hazard, a continuous interpolation between independent and common shock clocks, two different occupancy objectives, and an exact rescue-rate transition. Unlike extinction-time or single-density results, the joint-occupancy transition follows from its own exact formula. An exhaustive priority claim is not made: complete texts of the closest Johst–Drechsler and Hiebeler articles could not be inspected, and a mathematical equivalent may exist in broader common-shock Markov-chain literature.

## Limitations

The equality threshold refers to the binary, two-patch, exchangeable Poisson model only. The mean is a stationary expected *count*, not a population size or mean lifetime. Common catastrophes here reset occupied patches simultaneously; the construction does not model temporally correlated non-Poisson environments. A local loss hazard held fixed does not imply fixed unconditional patch extinction rates or independent final occupancies. The result is a structural model comparison and does not demonstrate field-scale management benefits or identify the best real-world disturbance regime.

## References

1. K. Johst and M. Drechsler (2003), *Are spatially correlated or uncorrelated disturbance regimes better for the survival of species?*, Oikos 103, 449–456. DOI: 10.1034/j.1600-0706.2003.12770.x; verified first public date 2003-10-21.
2. D. E. Hiebeler (2005), *Spatially correlated disturbances in a locally dispersing population model*, Journal of Theoretical Biology 232, 143–149. DOI: 10.1016/j.jtbi.2004.08.007.
3. M. J. Keeling (2000), *Metapopulation moments: coupling, stochasticity and persistence*, Journal of Animal Ecology 69, 725–736. DOI: 10.1046/j.1365-2656.2000.00430.x.
4. C. Sutherland, D. A. Elston, and X. Lambin (2012), *Multi-scale processes in metapopulations: contributions of stage structure, rescue effect, and correlated extinctions*, Ecology 93, 2465–2473. DOI: 10.1890/12-0172.1.
