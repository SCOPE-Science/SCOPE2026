# Independent mathematical audit

## correctness

PASS

Writing y=τx, k=2τ(τ+2), G=1−e^(−y)(y²+2y+D)/D and g=e^(−y)(y²+k)/D, D=2(1+τ)², the log-density derivative at δ=1+ε is A(y)+εB(y), A=2y/(y²+k)−1=−((y−1)²+k−1)/(y²+k), B=g/G>0. Since yB→1, an analytic implicit-function argument gives a unique near-zero max y1=ε+O(ε²). For k<1, both simple roots 1±√(1−k) persist and become a minimum and a second maximum; for k>1 no others persist. At k=1, A''(1)=−1 and B(1)=2/[3(e−2)], with strict local concavity giving two roots y=1±2√ε/√[3(e−2)]+O(ε). Tail/compact sign bounds exclude other roots for each fixed τ. Independent high-precision root bracketing and symbolic derivative checks corroborate the theorem, without serving as a global root census.

## originality

PASS

The sharp numerical τ_c is already the baseline Haq cutoff in Ahsan-ul-Haq (2022), and exponentiated-CDF construction itself is Lehmann prior work: neither is novel. The contribution is the quantified near-δ=1 *additional near-origin mode* and sharp three-root phase count, including a critical square-root cusp with equality on the two-mode side. Full 2025 Alharthi article gives distribution and plots but no located fixed-τ small-ε theorem; Tashkandy's power-Haq law transforms the variable, not the CDF. Best-of-knowledge PASS subject to potential unindexed generic exponentiated-density bifurcation theorem.

## value

PASS

The number/location of interior modes is a natural shape feature of the published lifetime model, critical for selecting and interpreting density fits. Determining a rigorous two-mode versus one-mode threshold and a degenerate sqrt perturbative splitting gives a complete local bifurcation diagram, beyond a selected-parameter figure or routine derivative transcription.

The dated certificate retains the supplied scientific assessment, sources and limitations.
