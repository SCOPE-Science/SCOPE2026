# Strict finite-population polarization ordering in four-person majority gain–loss dynamics

## Finding
Fix an integer \(N\ge6\), a noise parameter \(0<p<1\), and either of the **one-step gain–loss chains** defined below. Let \(K_p\) be the stationary number of agents holding opinion \(+1\), and put \(D_p=|2K_p-N|\). For either independence noise or unanimous-group anticonformity noise, whenever \(0<p_1<p_2<1\), the distribution of \(D_{p_2}\) is strictly smaller than that of \(D_{p_1}\) in monotone likelihood-ratio order, on its ordered finite support. Consequently,

\[
\Pr(D_{p_2}\ge d)<\Pr(D_{p_1}\ge d)
\]

for every attainable threshold \(d\) strictly above the minimum polarization, and every nonconstant nondecreasing function of polarization has strictly smaller stationary expectation at \(p_2\). Thus **every finite-population polarization tail**, not only the locations of stationary modes, is strictly reduced by increasing either type of noise. For the anticonformist chain, \(N\ge6\) is also the sharp population-size condition for irreducibility: at \(N=4\) and \(N=5\) its one-step state space decomposes into multiple closed classes.

These statements apply to the exact continuous-time birth–death chains obtained by using the four-agent *gain–loss coefficients* in Muslim–Wella–Nugraha (2023) as single-step transition **rates**. They are not statements about a microscopic chain that changes all four selected spins simultaneously.

## Assumptions and scope
Let \((z)_j=z(z-1)\cdots(z-j+1)\) for integers \(z\ge j\ge1\), with \((z)_j=0\) when \(0\le z<j\), and \((z)_0=1\). All populations \(N\ge6\) have states \(k\in\{0,\ldots,N\}\). Write

\[
U_k=\frac{4(N-k)(k)_3}{(N)_4},\qquad V_k=\frac{4k(N-k)_3}{(N)_4}.
\]

The chain has only jumps \(k\to k+1\) of rate \(\lambda_k\), and \(k\to k-1\) of rate \(\mu_k\). A nonexistent boundary jump has rate zero. The two models are:

**Independence gain–loss chain** (\(I\)):

\[
\lambda_k^{I}=(1-p)U_k+\frac{2p(N-k)}{N},\qquad
\mu_k^{I}=(1-p)V_k+\frac{2pk}{N}.
\]

**Unanimity-triggered anticonformity gain–loss chain** (\(A\)):

\[
\lambda_k^{A}=(1-p)U_k+p\frac{(N-k)_4}{(N)_4},\qquad
\mu_k^{A}=(1-p)V_k+p\frac{(k)_4}{(N)_4}.
\]

These are precisely the algebraic one-step coefficients appearing in equations (10) and (14), respectively, of the motivating paper. Their continuous-time rate interpretation is explicit: it is always a valid finite-state Markov model even where the coefficients would not be admissible as probabilities of a single discrete-time update. In particular, replacing simultaneous multispin moves with single-unit jumps is an **assumption**, not a proven equivalence to the full four-spin simulation.

## Proof
**1. Irreducibility and symmetry.** In model \(I\), \(p>0\) gives strictly positive interior birth and death rates. In model \(A\), \(\lambda_k>0\) whenever \(k\ge3\) (a three-plus-one conformist update) or \(N-k\ge4\) (a unanimous minus-group update). For \(N\ge6\) these conditions cover every \(k<N\). Analogously \(\mu_k>0\) whenever \(N-k\ge3\) or \(k\ge4\), covering every \(k>0\). Both chains therefore have a unique strictly positive stationary law \(\pi_p\). The exact identity \(\lambda_k=\mu_{N-k}\) gives \(\pi_p(k)=\pi_p(N-k)\) by uniqueness.

**2. Exact stationary ratios.** Detailed balance for every birth–death chain gives

\[
\pi_p(k)=\frac1Z\prod_{i=0}^{k-1}\frac{\lambda_i(p)}{\mu_{i+1}(p)},
\qquad 0\le k\le N,
\]

with an empty product equal to one and \(Z\) its finite normalizing sum. Consider \(k\ge\lceil N/2\rceil\) and \(k<N\). Set \(a=(k)_3\), \(b=(N-k-1)_3\), and \(C=(N)_4\). Since \(N\ge6\), \(a>b\ge0\). In model \(I\),

\[
R_k^{I}(p):=\frac{\pi_p(k+1)}{\pi_p(k)}
=\frac{N-k}{k+1}
\frac{4(1-p)a/C+2p/N}{4(1-p)b/C+2p/N}.
\]

The sign of its derivative in \(p\) is the sign of \(b-a\), which is strictly negative. In model \(A\), the product identities \((N-k)_4=(N-k)b\) and \((k+1)_4=(k+1)a\) give the simpler formula

\[
R_k^{A}(p)=\frac{N-k}{k+1}
\frac{4(1-p)a+pb}{4(1-p)b+pa}.
\]

The numerator of the derivative of the final fraction is \(4(b^2-a^2)\), also strictly negative. Both denominators are positive in the stated open parameter range.

**3. Whole-distribution ordering.** By stationary symmetry, the law of \(D_p\) has ordered support \(\{N\bmod2,\,N\bmod2+2,\ldots,N\}\). The ratio between consecutive radial masses is a corresponding upper-half ratio \(R_k(p)\), except for the first even-\(N\) ratio, which is \(2R_{N/2}(p)\). Thus every consecutive radial-mass ratio is strictly decreasing in \(p\). For \(p_1<p_2\), the likelihood ratio \(\Pr(D_{p_2}=d)/\Pr(D_{p_1}=d)\) therefore strictly decreases along the support. Its total mass is one under either law, so the single-crossing argument gives strict inequalities for every nontrivial upper tail and for every nonconstant nondecreasing function of \(D\).

**4. Small-population boundary.** For \(N=4\) in model \(A\), state \(k=2\) has \(\lambda_2=\mu_2=0\). For \(N=5\), \(\lambda_2=\mu_3=0\), separating the state space into closed lower and upper portions. Hence \(N=6\) is the first population size for which all single-step anticonformist rates are positive in the necessary directions for irreducibility.

## Verification
The attached standalone `verify.py` uses only Python's standard library and exact rational arithmetic. It reconstructed the two chains, normalized the detailed-balance stationary measures for every \(6\le N\le30\) and eight rational parameter values in \((0,1)\), and checked symmetry, detailed balance, every tested upper radial ratio, all nontrivial polarization-tail inequalities, and the special small-\(N\) boundaries. It passed **24,477 exact identities and strict comparisons** across **400 stationary distributions**. An independent exact linear-system solution of the seven-state generator at \(N=6\), \(p=1/4\) matched the product formula for both dynamics.

At \(N=6\), increasing noise from \(p=1/4\) to \(p=1/2\) changes the exact probability of \(D\ge4\) from \(52/77\) to \(243/593\) under independence, and from \(1296/1391\) to \(16/23\) under anticonformity. Numerical or finite exact tests are not the proof of the quantified all-populations theorem; its proof is the symbolic stationary-ratio argument above.

To reproduce: run `python3 verify.py` with Python 3. The program prints PASS and these rational examples or raises an assertion.

## Relationship to prior work
Muslim, Wella and Nugraha (arXiv:2305.06554, 2023), section 3, derive the four-person gain–loss coefficients, a large-\(N\) Fokker–Planck stationary approximation and order/disorder critical points. Their figures compare the *locations and shapes* of stationary peaks at selected noise values. The result here is an **exact, finite-\(N\), all-noise ordering of every stationary polarization tail for the explicitly identified one-step chain**, and the sharp small-population irreducibility cutoff. It does not claim the coefficients, approximate stationary density, phase-transition exponents or monotonic qualitative physical narrative as new.

Crokidakis and de Oliveira (arXiv:1505.05163, 2015) analyze a related majority model with three-person group moves and independence, not these four-person birth–death coefficients. Nowak, Stoń and Sznajd-Weron (arXiv:2012.11725, 2020) analyze a noisy \(q\)-voter model governed by unanimity rather than a four-person three-to-one majority rate. General birth–death detailed balance and likelihood-ratio comparison are standard; the model-specific uniform strict inequalities are the mathematical content of this finding.

## Limitations
The theorem concerns the **continuous-time single-step chain**, not exact simultaneous four-person flips, other network topologies, quenched rather than per-update nonconformity, or unequal opinion biases. Its common domain is \(N\ge6\), \(0<p<1\). It does not establish a dynamical coupling or order at fixed transient times; the ordering holds for stationary laws. It does not identify the complete literature priority of this distribution-wide comparison, and generic stochastic comparison results may supply alternative proofs. No independent scientific audit is asserted.

## References
1. R. Muslim, S. A. Wella, A. R. T. Nugraha, *Phase transition in the majority rule model with the nonconformist agents*, arXiv:2305.06554 (first public arXiv submission 2023-05-11). https://arxiv.org/abs/2305.06554
2. N. Crokidakis, P. M. C. de Oliveira, *Inflexibility and independence: Phase transitions in the majority-rule model*, arXiv:1505.05163 (2015). https://arxiv.org/abs/1505.05163
3. B. Nowak, B. Stoń, K. Sznajd-Weron, *Discontinuous phase transitions in the multi-state noisy q-voter model: quenched vs. annealed disorder*, arXiv:2012.11725 (2020). https://arxiv.org/abs/2012.11725
