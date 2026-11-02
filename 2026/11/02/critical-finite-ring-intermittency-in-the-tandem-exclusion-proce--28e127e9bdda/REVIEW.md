# Scientific review

## Correctness — PASS

For the periodic tandem process with directed local moves \(110\to101\) and \(101\to011\), and \(K_N/N\to\rho\in(0,1)\), \(\beta_N/(\alpha N^2)\to\lambda\in(0,\infty)\), the asserted observable is the **configuration-dependent instantaneous jump intensity per bond**. Its stationary Gibbs law is independently derived by a telescoping incoming/outgoing global-balance calculation and is also an established input from the originating paper. Exact positive cyclic-composition counts and the exact conditional occurrence probabilities of one-site vacant runs give uniform factorial-moment bounds. Dominated convergence and moment expansion prove convergence in probability to zero, the finite nonzero mean limit, the linear growth of variance, fixed higher moments, and the rare-event frequency. The proof covers all fixed positive integer moments and all fixed thresholds away from the critical burst height. There is no claim about the temporal integrated current. The reproducible finite-state verifier performs 2,239 exact/approximate checks and is not used as a substitute for the analytic proof.

## Originality — PASS, qualified best-knowledge

Ngoc, Nhung and Thi, *Tandem Exclusion Process* (arXiv:2606.01568, first submitted 2026-06-01), establish this model, its active stationary Gibbs law, its thermodynamic stationary current, and its strong-recovery mean. None of these is claimed as new. Antal, Droz and Rácz (arXiv:cond-mat/0308442) provide low-temperature finite-size Ising domain-wall counting, which encompasses the basic static block-count combinatorics after a fixed-magnetization reduction; the block-count Bessel limit is not offered as an independent novel theorem. Gabel, Krapivsky and Redner (arXiv:1007.3217) analyze a related facilitated exclusion dynamics lacking the follower recovery move. The assessed difference is the joint finite-ring high-rate regime, under which snapshot transition intensity converges to zero in probability despite retaining a strictly positive expected value and a variance proportional to ring length. Broader rare-event fluctuation theorems could cover this particular scalar observable implicitly; independent priority investigation remains necessary.

## Value — PASS

The originating current calculation concerns the stationary average. The new rate-size crossover shows that this average can be supported entirely by rare instantaneous bursts rather than by typical snapshots. It gives a full hierarchy of diverging intensity moments, the sharp rate of rare snapshots, and a concrete warning against identifying one-time intensity fluctuations with temporal integrated-current fluctuations. The scaling \(q_N\asymp N^2\) is selected intrinsically by the probability of a unit vacant gap between surviving macroscopic particle blocks, rather than by an arbitrary small-system parameter choice. This is a natural physical interpretation of the fast follower-recovery regime.

## Residual risks and limitations

Broad large-deviation and rare-event studies of exclusion processes may imply parts of the statement. The static Bessel law itself follows classical Ising/domain-wall counting. The full temporal event-count process, finite-rate corrections, and trajectories are unproved. Further independent assessment of both proof and priority is appropriate.

Self-review: passed. Independent audit: not yet performed.
