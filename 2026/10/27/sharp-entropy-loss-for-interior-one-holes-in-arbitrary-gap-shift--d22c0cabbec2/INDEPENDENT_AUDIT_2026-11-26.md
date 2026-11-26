# Independent mathematical audit

## correctness

PASS

Reconstructed the claim under the stated closure definition and reassessed the corrected RESULT.md. The original finite-word admissibility sentence cannot stand as a sufficiency criterion: S={0,1} allows no 00, even though 00 contains no pair of consecutive ones. The repaired scope states the boundary extension requirement. Independently identify the full survivor as the closure of alternating positive zero runs in S and one runs of any positive length except k: for each finite survivor word its complete runs obey the constraints, its partial zero runs can be extended using its occurrence in X_S, and its partial one runs extend to allowed lengths; this works also for one-symbol words or words within one run. The two run generating functions then multiply to C_k(t)=P(t)((1−t)⁻¹−t^(k−1)); the background graph entropy theorem gives its unique root. Both C_k and G=P/(1−t) have nonnegative coefficients and increase strictly from 0 to infinity; C_k(q)=1−(1−q)q^(k−1) proves q_k>q, including k=2. Choose q<r<1 to bound q_k≤r eventually. The mean value theorem on [q,r] gives δ=q_k−q=O_S(r^(k−1)), hence kδ→0. Expanding q_k^(k−1) around q gives a second bound δ=O_S(q^(k−1)); applying G′(q)=(1+P′(q))/(1−q) and the root equation gives δ=(1−q)²q^(k−1)/(1+P′(q))+O_S(kq^(2k−2)). Expanding log(q_k/q) yields the claimed coefficient and remainder. Under the stationary renewal measure with p_s=q^(s+1), the mean spacing M=q(1+P′(q)) is finite and the entropy per symbol is H(p)/M=−log q. Each occurrence of the hole starts at the last zero of a positive gap and requires exactly k−1 zero gaps followed by a positive gap. Renewal intensity times independence gives P(q)²q^(k−1)/M and establishes the exact normalization. All expansion constants are for fixed S. The source numerical checker for finite gap sets was inspected but not executed; the analytic and graph arguments establish the unrestricted range.

## originality

PASS

For the corrected sharp entropy-loss and cylinder-normalization claim. Dillon's theorem already implies the exact fixed-hole root by a two-vertex alternating-run specialization; the corrected presentation explicitly credits it and uses it only as a starting point. Cheriyath's general theorem expressly excludes the zero-ended interior-one family, apart from the modular context discussed separately. The arbitrary-S cylinder-avoidance overlap in Haydarov et al. guarantees a positive quantitative gap but does not give the sharp linear mass coefficient and quantified remainder. No reviewed statement mechanically supplies those results across finite and infinite S under the stated assumptions.

## value

PASS

The corrected claim resolves a motivated subfamily of a previously excluded hole shape. It gives a sharp topological loss with the intrinsic cylinder probability as leading term and quantified error in a regime genuinely including nonsofic systems. This is informative beyond merely computing the already-covered pressure root for a fixed hole or giving an unspecified positive entropy gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
