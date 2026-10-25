# A resonance law for age-limited seed banks under periodic forcing

## Finding
Consider a discrete annual seed-bank model with a maximum of \(L\) viable seed age classes, a constant germination fraction \(0<g<1\), dormant-seed survival \(0<s<1\), and positive seasonal seed productivity \(r_t\) of period \(m\ge2\). Put \(a=g\), \(b=s(1-g)\), and let \(M_L(r)\) be the \(L\)-by-\(L\) matrix with every entry of its first row equal to \(ar\), with \(b\) on its first subdiagonal, and with all other entries zero. The population at time \(t+1\) equals \(M_L(r_t)\) times its vector of seeds aged \(0,\ldots,L-1\) seasons.

**Permutation-isospectrality theorem.** For every positive list \((r_0,\ldots,r_{m-1})\) and every positive integer \(k\), if \(L=km\) or \(L=km-1\), every reordering of the \(m\) seasons has **the same entire characteristic polynomial** for its \(m\)-year product, not merely the same dominant growth multiplier. This is an infinite family of exact order-blind longevity/season-length resonances, without assuming equal seasonal productivities.

**Sharp four-season contrast.** For a four-season cycle with two high-productivity years \(H\) and two low-productivity years \(J\), \(H>J>0\): at \(L=1\), the ordering is irrelevant; at \(L=2\), alternating \(HJHJ\) always has strictly greater long-run multiplier than clustered \(HHJJ\); at \(L=3,4\), the two multipliers are equal for every parameter choice. At \(L=5\), clustering can instead grow while alternation declines. Thus five viable age classes are the smallest maximum-age limit for which clustering can **strictly beat** alternation in this model.

An exact witness uses \(g=1/5\), \(s=9/10\), \(H=4\), and \(J=1/6\):
\[
\rho\!\left(M_5(H)^2M_5(J)^2\right)>1>
\rho\!\left(M_5(H)M_5(J)M_5(H)M_5(J)\right).
\]

## Assumptions and scope
All stages are seeds, classified by the number \(0\) through \(L-1\) of completed dormant seasons. Each season the same fraction \(g\) of every age class germinates and produces \(r_t\) fresh seeds per germinated seed; dormant seeds survive into the next age class with probability \(s\), and seeds exceeding the maximum age leave the system. Germinated seeds do not remain in the seed bank. This is a deterministic linear low-density expectation model; no stochastic extinction probability or nonlinear ecological persistence is asserted. The spectral radius measures asymptotic per-cycle growth (decline below one, growth above one). Temporal multiplication order is irrelevant to the theorem's universal claim because all reorderings are included.

## Proof
Write \(S_t\) for the total of all viable age classes just before season \(t\), and let \(N_t\) be the age-zero count. From the matrix recurrence, \(N_{t+1}=ar_tS_t\), and age-\(j\) seeds have mass \(b^jN_{t-j}\). Therefore
\[
 S_{t+1}=(b+ar_t)S_t-ab^Lr_{t-L}S_{t-L}. \tag{1}
\]
For any nonzero Floquet multiplier \(\mu\) of the \(m\)-step product, a corresponding solution satisfies \(S_{t+m}=\mu S_t\). Conversely, for \(\mu\ne b^m\), a Floquet sequence satisfying (1) reconstructs an original age-structured solution: set \(N_{t+1}=ar_tS_t\), reconstruct its \(L\) age cohorts, and subtract their total from \(S_t\). The difference obeys \(D_{t+1}=bD_t\); periodic Floquet scaling forces \((\mu-b^m)D_t=0\).

**Case \(L=km\).** Periodicity gives \(r_{t-L}=r_t\) and \(S_{t-L}=\mu^{-k}S_t\). Equation (1) becomes the scalar first-order recurrence
\[
 S_{t+1}=\left[b+ar_t\left(1-b^L\mu^{-k}\right)\right]S_t.
\]
Its full-period compatibility equation, after removing the spurious root \(\mu=b^m\) introduced by the reduction, gives the following *polynomial identity* for the monic characteristic polynomial of the period product \(P\):
\[
\boxed{\displaystyle
\det(\mu I-P)=\frac{\mu^L}{\mu-b^m}
\left[\mu-\prod_{j=0}^{m-1}
\left(b+ar_j(1-b^L\mu^{-k})\right)\right].}
\tag{2}
\]
The right side is interpreted after algebraic cancellation of the removable factor; it is a polynomial of degree \(L\). To justify the polynomial identity, first take generic positive parameters with simple nonzero monodromy eigenvalues distinct from \(b^m\); the Floquet reconstruction gives equality of the roots, and both sides are monic of degree \(L\). The identity extends to all parameter choices by polynomial continuity.

**Case \(L=km-1\).** Now \(r_{t-L}=r_{t+1}\) and \(S_{t-L}=\mu^{-k}S_{t+1}\), yielding
\[
 \left(1+ab^Lr_{t+1}\mu^{-k}\right)S_{t+1}=(b+ar_t)S_t.
\]
The corresponding characteristic polynomial identity is
\[
\boxed{\displaystyle
\det(\mu I-P)=\frac{
\prod_{j=0}^{m-1}(\mu^k+ab^Lr_j)
-\mu^L\prod_{j=0}^{m-1}(b+ar_j)}{\mu-b^m}.}
\tag{3}
\]
The same reconstruction and removable-factor argument applies. Formulas (2) and (3) are symmetric in the seasonal productivities, proving all-order **full isospectrality**.

For \(m=4\), the cases \(L=3,4\) are covered by (3) and (2), respectively, while \(L=1\) is a scalar product. For \(L=2\), writing \(P_c=M_2(H)^2M_2(J)^2\) and \(P_a=M_2(H)M_2(J)M_2(H)M_2(J)\), direct multiplication gives
\[
 \operatorname{tr}(P_a)-\operatorname{tr}(P_c)
 =a^2b^2(H-J)^2>0,
 \qquad \det(P_a)=\det(P_c)=a^4b^4H^2J^2.
\]
For strictly positive two-by-two products at fixed determinant, the positive Perron root increases strictly with the trace; hence \(\rho(P_a)>\rho(P_c)\) for all \(H\ne J\).

Finally, for the rational five-age witness, put \(a=1/5\), \(b=18/25\), \(H=4\), \(J=1/6\). The strictly positive vectors
\[
 v=(104,50,2,2,27)^{\mathsf T},\qquad
 w=(40,2,22,1,11)^{\mathsf T}
\]
satisfy \(P_cv-v>0\) and \(w-P_aw>0\) in every coordinate, where \(P_c=M_5(H)^2M_5(J)^2\) and \(P_a=M_5(H)M_5(J)M_5(H)M_5(J)\). Explicit exact rational margins are reproduced in the verification certificate. The Collatz–Wielandt bounds thus imply \(\rho(P_c)>1>\rho(P_a)\). This also establishes the asserted minimum \(L=5\) after the \(L=1,2,3,4\) cases.

## Verification
The accompanying standalone script `checker.py` uses rational arithmetic only. It verifies the \(L=2\) trace and determinant comparison, both coordinatewise \(L=5\) Perron inequalities, and characteristic-polynomial invariance for all reorderings in the eight tested cases \(m\in\{3,4\}\) with \(L\in\{m-1,m,2m-1,2m\}\). The emitted `certificate.json` records every exact margin. Finite checks supplement, rather than prove, the all-\(m\), all-\(k\) algebraic identities (2)–(3).

## Relationship to prior work
Mertens, van den Bosch and Heesterbeek (2002) modeled crop-rotation order in a structured weed population and reported different growth rates for clustered versus alternating rotations; their model tracks soil depth and uses changing crop-dependent matrix entries. The present result does **not** claim that seasonal order effects or periodic projection matrices are new. It isolates a distinct finite-age homogeneous-survival subfamily with complete order-invariant spectra at specific longevity congruences and an exact reversal of the four-season ranking as longevity changes. Mertens et al. (2006) studied transient responses to cyclic permutations, which do not imply invariance under every permutation. Cushing and Ackleh (2011/2012) developed reproductive thresholds for periodic matrix models including period-two Leslie models; their stated general framework does not immediately imply formulas (2)–(3). Meyer and Li (2013) give a more general age-structured seed-bank framework directed to spreading speeds, rather than this permutation classification. Accessible sources did not substantiate a previously published equivalent; a stronger spectral rearrangement theorem could conceivably cover this special case.

## Limitations
Identical monodromy spectra do not imply identical transient trajectories, stage distributions, or finite-time seed counts. The result depends on equal germination fraction across seed ages, constant dormant survival, uniform fecundity across germinated ages, a strict finite maximum age, and deterministic periodic forcing. Arbitrary age-specific rates, survival correlations, density dependence, stochastic environments, and competing species are outside scope. The five-age comparison is existential, not a claim that clustering always dominates at age five. Independent bibliographic assessment has not occurred, and relevant historical full texts were not all accessible.

## References
- Mertens, S. K., van den Bosch, F., and Heesterbeek, J. A. P. (2002). *Weed populations and crop rotations: Exploring dynamics of a structured periodic system*. Ecological Applications 12, 1125–1141. DOI: 10.1890/1051-0761(2002)012[1125:WPACRE]2.0.CO;2. First publicly dated version checked: 2002-08-01.
- Mertens, S. K., Yearsley, J. M., van den Bosch, F., and Gilligan, C. A. (2006). *Transient population dynamics in periodic matrix models: Methodology and effects of cyclic permutations*. Ecology 87, 2338–2348. DOI: 10.1890/0012-9658(2006)87[2338:TPDIPM]2.0.CO;2.
- Cushing, J. M., and Ackleh, A. S. (2011/2012). *A net reproductive number for periodic matrix models*. Journal of Biological Dynamics 6, 166–188. DOI: 10.1080/17513758.2010.544410.
- Meyer, K. I., and Li, B. (2013). *A spatial model of plants with an age-structured seed bank and juvenile stage*. SIAM Journal on Applied Mathematics 73, 1676–1702. DOI: 10.1137/120880501. Primary MSC: 92D40.
