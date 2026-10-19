# Four is the sharp minimum for order-dependent extinction in a two-stage population

## Finding

Consider a positive two-stage linear population subject to evenly spaced, instantaneous, stage-specific mortality pulses. Let the ecological generator be an irreducible real Metzler matrix \(A\in\mathbb R^{2\times2}\), with both off-diagonal entries strictly positive, and let the common interval be \(\tau>0\). Each pulse class \(j\) has a positive diagonal survival matrix \(D_j\), with all entries in \((0,1]\). A block of \(k\) pulse classes is repeated indefinitely, in any chosen order, with the same multiset of classes and the same interval \(\tau\).

**Order immunity for at most three pulses.** For \(k\in\{1,2,3\}\), all permutations of those \(k\) classes have the *same complete Floquet-multiplier multiset* and thus exactly the same asymptotic extinction/growth threshold. This statement holds for all permitted \(A,\tau,D_j\); the transient trajectories need not agree.

**Sharpness at four pulses.** There are positive ecological rates and four distinct pulse classes, all with strict survival probabilities between zero and one, such that one repeating order makes every positive population tend to zero and another repeating order makes every positive population grow without bound. Their common pulse multiset, spacing, and length-four period are identical. Thus four is the *minimum number of pulses* for genuinely order-dependent Floquet growth in this two-stage equal-spacing model.

## Assumptions and scope

Between pulses the stage population \(u(t)\in\mathbb R_{>0}^{2}\) obeys \(\dot u=A u\). At a pulse of class \(j\), \(u^+=D_j u^-\). Set \(E=e^{\tau A}\). With chronological pulse indices \(\sigma=(\sigma_1,\ldots,\sigma_k)\), the one-block map from just after the preceding pulse is

\[
P_\sigma=D_{\sigma_k}E\cdots D_{\sigma_2}E D_{\sigma_1}E.
\]

Repeated blocks use the same \(\sigma\). The positive Perron spectral radius \(\rho(P_\sigma)\) is less than one exactly in the exponentially decaying regime, and greater than one exactly in the growing regime; the equality regime is not classified here. The theorem does not require the pulse classes to be biologically named compounds or the coefficients to represent a specific measured population.

The life-cycle generator includes the two-stage specialization of the age/stage model of D'Ovidio Long, Adjei, and Patel:
\[
A=\begin{pmatrix}-(\mu_1+\alpha_{12})&\lambda\\\alpha_{12}&-\mu_2\end{pmatrix},\quad \mu_1,\mu_2,\alpha_{12},\lambda>0.
\]
On its invariant fully resistant genotype face, stage-specific resistant survival probabilities provide the diagonal entries of \(D_j\). The present finding concerns a **specified new extension** in which distinct pulse classes repeat in a block, rather than a single fixed pulse matrix repeating each interval. It asserts nothing about arbitrary evolving allele frequencies.

## Proof

**1. A reversible similarity.** For a general \(A\) as assumed, set \(R=\operatorname{diag}(\sqrt{A_{21}},\sqrt{A_{12}})\). Then \(RAR^{-1}\) is a real symmetric matrix, with off-diagonal entries \(\sqrt{A_{12}A_{21}}\). Therefore \(E_s=RER^{-1}=e^{\tau RAR^{-1}}\) is symmetric positive definite. Each diagonal \(D_j\) commutes with \(R\). Let \(Q=E_s^{1/2}\), the symmetric positive-definite square root, and set \(S_j=QD_jQ\). Every \(S_j\) is real symmetric positive definite. Similarity first by \(R\), then by \(Q\), gives

\[
P_\sigma\sim S_{\sigma_k}S_{\sigma_{k-1}}\cdots S_{\sigma_1}.
\]

**2. Three factors cannot encode the order in the spectrum.** A cyclic rotation of a product of invertible matrices preserves its characteristic polynomial, by similarity. Reversing any product of real symmetric matrices transposes it and likewise preserves its characteristic polynomial. For one, two, or three labeled factors, *every permutation* is a composition of cyclic rotations and reversal. Hence all such products are isospectral. This is a direct application of standard matrix algebra; the novelty claimed here is its sharp stage-structured control consequence together with the four-pulse threshold counterexample.

**3. An exact four-pulse ecological realization.** Choose

\[
\mu_1=\tfrac14,\quad\alpha_{12}=\tfrac14,\quad\lambda=4,\quad\mu_2=\tfrac12,\quad\tau=\log 2.
\]

Then \(A=\left(\begin{smallmatrix}-1/2&4\\1/4&-1/2\end{smallmatrix}\right)\). Since \((A+I/2)^2=I\), the between-pulse map is exactly

\[
E=\frac1{\sqrt2}E_0,\qquad E_0=\begin{pmatrix}5/4&3\\3/16&5/4\end{pmatrix}.
\]

Take four **strict** stage-survival pairs \((d_{j,1},d_{j,2})\), writing \(D_j=\operatorname{diag}(d_{j,1},d_{j,2})\):

\[
D_0:(1/2,4/5),\quad D_1:(9/10,1/2),\quad
D_2:(19/20,1/2),\quad D_3:(3/5,99/100).
\]

Compare chronological blocks \(\sigma^-=(0,2,3,1)\) and \(\sigma^+=(2,1,3,0)\). The four copies of \(1/\sqrt2\) contribute exactly \(1/4\), so both monodromy matrices are rational. Direct rational multiplication yields

\[
\begin{aligned}
\operatorname{tr}(P_{\sigma^-})&=\frac{101759121}{102400000},\\
\operatorname{tr}(P_{\sigma^+})&=\frac{4243977}{4096000},\\
\det(P_{\sigma^-})&=\det(P_{\sigma^+})=\frac{50787}{16000000}<1,\\
\det(I-P_{\sigma^-})&=\frac{4829579}{512000000}>0,\\
\det(I-P_{\sigma^+})&=-\frac{16871941}{512000000}<0.
\end{aligned}
\]

Each \(P\) is an entrywise positive real \(2\times2\) matrix with positive determinant. Its two real eigenvalues are positive. Since their product is below one, the sign of \(\det(I-P)\) decides whether its Perron eigenvalue is smaller or greater than one. Hence \(\rho(P_{\sigma^-})<1<\rho(P_{\sigma^+})\), rigorously separating extinction and growth for the two orders. Perron–Frobenius theory applied to repeated positive block maps proves the claimed fate of every strictly positive initial stage population. This completes the sharpness argument.

## Verification

Run `python3 verify.py` using only the Python standard library. It derives and checks the exact rational monodromy traces, determinants, the signs at unit eigenvalue, admissibility of all survival probabilities and growth/decay threshold, and enumerates illustrative finite permutations with one through four classes. The universal three-pulse conclusion comes from the preceding similarity and transpose proof, not from enumeration. The approximate Perron radii are \(0.9905369039\) and \(1.0330545740\), respectively; exact signs are the certificates.

## Relationship to prior work

D'Ovidio Long, Adjei, and Patel (2026) formulate the coupled stage–genotype impulsive model and analyze ecological growth under a *single fixed diagonal pulse* each interval; their general model provides the two-stage generator and full-resistance invariant face used here. Patel and De Leenheer (2023 preprint; 2024 journal) establish spectral-radius threshold theory and convexity in the pulse interval for a *fixed* pulse matrix. The current result instead changes the chronological order of distinct pulse matrices within an equal-spacing repeating block.

Mermer and coauthors (2020 online; 2021 volume) demonstrate finite-season effects of the **order** of several insecticide applications in a temperature-driven, multi-stage pest model; they do not address the all-permutation isospectral invariant for at most three evenly spaced pulse types or the four-pulse extinction reversal in an indefinitely repeated two-stage constant-generator system. Their finite-horizon order effects do not conflict with asymptotic growth invariance under the narrower hypotheses here. A 2023 follow-up studies two-application empirical schedules, likewise different from the present statement.

Cyclic invariance of matrix-product spectra, invariance under transpose, symmetrization, and Perron–Frobenius theory are standard prior mathematics and are **not** asserted to be new.

## Limitations

Equal spacing, time-homogeneous two-stage linear flow, positive diagonal pulse survival, and repeated identical blocks are essential hypotheses. The proof gives no all-order invariance for unequal intervals or for an arbitrary nonsymmetrizable higher-stage generator. The example proves unbounded linear population growth, not convergence to a bounded nonzero equilibrium. The ecological threshold is conditional on fully resistant genotype frequencies and does not classify transient or long-term allele-frequency trajectories in the complete eco-evolutionary model. The four survival pairs are an exact model witness, not empirical estimates. Equivalent formulations in unindexed literature remain an originality risk; no independent audit has been performed.

## References

1. A. D'Ovidio Long, A. Adjei, S. Patel, *On the formulation and analysis of a stage-structured eco-evolutionary model with pulsed disturbances*, arXiv:2609.10581v1 (publicly posted 2026-09-05), https://arxiv.org/abs/2609.10581.
2. S. Patel and P. De Leenheer, *On the spectral radius properties of a key matrix in periodic impulse control*, arXiv:2310.07616 (2023); *Systems & Control Letters* 187 (2024), 105781, https://arxiv.org/abs/2310.07616.
3. S. Mermer et al., *Timing and order of different insecticide classes drive control of Drosophila suzukii; a modeling approach*, *Journal of Pest Science* 94 (2021), 743–755, DOI:10.1007/s10340-020-01292-w.
4. S. Mermer et al., *Comparing the effectiveness of different insecticide application orders for suppressing Drosophila suzukii ...*, *Journal of Economic Entomology* 116 (2023), 899–908, DOI:10.1093/jee/toad057.
